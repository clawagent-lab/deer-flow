#!/usr/bin/env python3
# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""Generate detailed API reference markdown docs for every Python source file.

Maps each .py under src/, tests/, scripts/, and repo-root to
docs/api-reference/<relative-path>.py.md using AST extraction.

Features:
- File metadata (path, dotted module, line count, architecture category)
- Module docstring
- Full dependency list (imports / from-imports, with relative-import dots)
- Exported symbol table (classes, functions, async funcs, constants)
- Per-symbol detail: signature, decorators, bases, members, docstring
  with parsed Google-style Args/Returns/Raises/Examples sections
- Reverse dependency index (which modules import this one)
- Module-level README.md per directory
- Top-level INDEX.md grouping by module category
"""

from __future__ import annotations

import ast
import json
import os
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_ROOT = REPO_ROOT / "docs" / "api-reference"

SCAN_DIRS = ["src", "tests", "scripts"]
ROOT_PY_FILES = ["main.py", "server.py", "test_fix.py"]


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class SymbolInfo:
    kind: str  # class | function | async_function | assignment
    name: str
    signature: str = ""
    docstring: str = ""
    bases: list[str] = field(default_factory=list)
    decorators: list[str] = field(default_factory=list)
    line: int = 0
    end_line: int = 0
    members: list[str] = field(default_factory=list)


@dataclass
class ModuleInfo:
    path: str  # repo-relative path
    rel_module: str  # dotted module path (without __init__)
    is_package_init: bool = False
    docstring: str = ""
    symbols: list[SymbolInfo] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    from_imports: list[str] = field(default_factory=list)
    line_count: int = 0
    imported_by: list[str] = field(default_factory=list)  # reverse deps


# ---------------------------------------------------------------------------
# AST parsing
# ---------------------------------------------------------------------------


def _format_decorator(dec: ast.AST) -> str:
    """将 AST 装饰器节点格式化为 `@decorator` 形式的字符串。"""
    try:
        if isinstance(dec, ast.Call):
            func = ast.unparse(dec.func)
        else:
            func = ast.unparse(dec)
        return f"@{func}"
    except Exception:
        return "@<decorator>"


def _format_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    """将函数/异步函数节点的参数与返回注解格式化为签名字符串（含括号与 `-> 返回类型`）。"""
    try:
        args_str = ast.unparse(node.args)
    except Exception:
        args_str = "..."
    # ast.unparse(node.args) returns "(a, b=1, *args, **kwargs)" already including
    # parens since Python 3.9+; but defensively ensure parens.
    if not args_str.startswith("("):
        args_str = f"({args_str})"
    suffix = ""
    if node.returns:
        try:
            suffix = f" -> {ast.unparse(node.returns)}"
        except Exception:
            pass
    return f"{args_str}{suffix}"


def _docstring(node: Any) -> str:
    """安全提取 AST 节点的 docstring，失败时返回空字符串。"""
    try:
        doc = ast.get_docstring(node)
    except Exception:
        doc = None
    return (doc or "").strip()


def _base_names(bases: list[ast.AST]) -> list[str]:
    """将类定义的基类列表格式化为字符串列表（如 `BaseModel`、`Enum`）。"""
    out = []
    for b in bases:
        try:
            out.append(ast.unparse(b))
        except Exception:
            out.append("...")
    return out


def _class_members(node: ast.ClassDef) -> list[str]:
    """提取类体内的方法与属性名，用于在文档中展示成员概览。"""
    members = []
    for item in node.body:
        if isinstance(item, ast.AsyncFunctionDef):
            members.append(f"async def {item.name}")
        elif isinstance(item, ast.FunctionDef):
            # Skip dunder unless __init__
            members.append(f"def {item.name}")
        elif isinstance(item, ast.Assign):
            for t in item.targets:
                try:
                    members.append(f"attr {ast.unparse(t)}")
                except Exception:
                    pass
        elif isinstance(item, ast.AnnAssign):
            try:
                members.append(f"attr {ast.unparse(item.target)}")
            except Exception:
                pass
    return members


def _dotted_module(file_path: Path) -> tuple[str, bool]:
    """根据文件路径计算点分模块名（如 `src.graph.builder`），并返回是否为 `__init__.py`。"""
    rel = file_path.relative_to(REPO_ROOT)
    parts = list(rel.parts)
    is_init = parts[-1] == "__init__.py"
    if is_init:
        parts = parts[:-1]
    else:
        parts[-1] = parts[-1][:-3]
    return ".".join(parts), is_init


def parse_module(file_path: Path) -> ModuleInfo:
    """解析单个 Python 源文件，返回模块信息：docstring、顶层符号、导入、行数。"""
    src = file_path.read_text(encoding="utf-8")
    line_count = len(src.splitlines())

    dotted, is_init = _dotted_module(file_path)
    rel_path = str(file_path.relative_to(REPO_ROOT))

    try:
        tree = ast.parse(src, filename=str(file_path))
    except SyntaxError as e:
        return ModuleInfo(
            path=rel_path,
            rel_module=dotted,
            is_package_init=is_init,
            docstring=f"[PARSE ERROR] {e}",
            line_count=line_count,
        )

    info = ModuleInfo(
        path=rel_path,
        rel_module=dotted,
        is_package_init=is_init,
        docstring=_docstring(tree),
        line_count=line_count,
    )

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            kind = (
                "async_function"
                if isinstance(node, ast.AsyncFunctionDef)
                else "function"
            )
            info.symbols.append(
                SymbolInfo(
                    kind=kind,
                    name=node.name,
                    signature=_format_signature(node),
                    docstring=_docstring(node),
                    decorators=[_format_decorator(d) for d in node.decorator_list],
                    line=node.lineno,
                    end_line=getattr(node, "end_lineno", node.lineno),
                )
            )
        elif isinstance(node, ast.ClassDef):
            info.symbols.append(
                SymbolInfo(
                    kind="class",
                    name=node.name,
                    bases=_base_names(node.bases),
                    docstring=_docstring(node),
                    decorators=[_format_decorator(d) for d in node.decorator_list],
                    line=node.lineno,
                    end_line=getattr(node, "end_lineno", node.lineno),
                    members=_class_members(node),
                )
            )
        elif isinstance(node, ast.Assign):
            for t in node.targets:
                try:
                    name = ast.unparse(t)
                except Exception:
                    continue
                # Keep meaningful module-level constants (uppercase or non-trivial).
                if name.startswith("_"):
                    continue
                try:
                    value_preview = ast.unparse(node.value)
                except Exception:
                    value_preview = "..."
                if len(value_preview) > 120:
                    value_preview = value_preview[:117] + "..."
                info.symbols.append(
                    SymbolInfo(
                        kind="assignment",
                        name=name,
                        signature=value_preview,
                        line=node.lineno,
                        end_line=getattr(node, "end_lineno", node.lineno),
                    )
                )
        elif isinstance(node, ast.Import):
            for alias in node.names:
                info.imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            level = "." * node.level
            full_mod = f"{level}{mod}"
            names = ", ".join(a.name for a in node.names)
            info.from_imports.append(f"from {full_mod} import {names}")

    return info


# ---------------------------------------------------------------------------
# Docstring parsing (Google style)
# ---------------------------------------------------------------------------


_GOOGLE_SECTIONS = {
    "args": "参数",
    "arguments": "参数",
    "params": "参数",
    "parameters": "参数",
    "returns": "返回值",
    "return": "返回值",
    "yields": "生成值",
    "raises": "异常",
    "examples": "示例",
    "example": "示例",
    "note": "备注",
    "notes": "备注",
    "attributes": "属性",
}


def parse_google_docstring(doc: str) -> dict[str, str]:
    """Split a Google-style docstring into sections."""
    if not doc:
        return {"summary": "", "body": ""}
    lines = doc.splitlines()
    # Summary = first non-empty line(s) until a blank line or a section header.
    summary_lines: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            break
        # Section header like "Args:" or "Returns:"
        if re.match(r"^\s*[A-Za-z]+\s*:\s*$", line):
            break
        summary_lines.append(line)
        i += 1
    summary = "\n".join(summary_lines).strip()

    sections: dict[str, list[str]] = defaultdict(list)
    current: str | None = None
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^\s*([A-Za-z]+)\s*:\s*$", line)
        if m:
            header = m.group(1).lower()
            current = _GOOGLE_SECTIONS.get(header, header)
            i += 1
            continue
        if current is not None:
            sections[current].append(line)
        i += 1

    result: dict[str, str] = {"summary": summary}
    for k, v in sections.items():
        text = "\n".join(v).strip()
        if text:
            result[k] = text
    return result


# ---------------------------------------------------------------------------
# Architecture context
# ---------------------------------------------------------------------------


_CATEGORY_DESC = {
    "src": "DeerFlow 后端核心包，包含工作流、智能体、工具、配置等所有业务模块",
    "src/agents": "智能体构建与中间件（基于 LangChain 1.x `create_agent` + `AgentMiddleware`，封装动态提示词、工具拦截、模型钩子）",
    "src/citations": "引用元数据采集、抽取与格式化，支撑报告中的来源标注",
    "src/config": "配置加载（`conf.yaml` / `.env`）、模型与工具开关、报告样式、智能体映射",
    "src/crawler": "网页抓取与正文抽取（Jina、Readability、InfoQuest 等多客户端）",
    "src/eval": "报告评估：自动化指标（字数/引用/章节覆盖）+ LLM-as-Judge 综合评分",
    "src/graph": "LangGraph 主工作流：节点、状态、边、checkpoint、工具函数",
    "src/llms": "LLM 适配层（统一封装 dashscope 等提供商，按类型路由）",
    "src/podcast": "播客生成子图（脚本撰写 → TTS → 音频合成）",
    "src/ppt": "PPT 生成子图（大纲生成器 + 内容编排器）",
    "src/prompt_enhancer": "提示词增强子图（对用户输入做扩写/优化）",
    "src/prompts": "Jinja2 提示词模板与 Plan/Step 数据模型",
    "src/prose": "散文编辑子图（改写 improve、扩写 longer、缩写 shorter、修复 fix、续写 continue、精简 zap）",
    "src/rag": "检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂",
    "src/server": "FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）",
    "src/tools": "工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）",
    "src/utils": "通用工具（JSON 修复、日志脱敏、上下文管理）",
    "tests": "测试套件根目录（pytest + pytest-asyncio + pytest-cov，覆盖率门槛 25%）",
    "tests/unit": "单元测试（按模块组织，聚焦单个类/函数的行为）",
    "tests/integration": "集成测试（跨组件 / 外部服务，如 crawler、nodes、template、tts）",
    "scripts": "仓库脚本（API 文档生成器、license 头检查等）",
    "根目录": "仓库根目录入口文件（控制台 UI `main.py`、FastAPI 启动 `server.py`）",
    "src（根）": "src 包根目录文件（`__init__.py`、`workflow.py` 编排入口）",
    "tests（根）": "tests 根目录下的顶层测试（如 `test_state.py`、`test_ppt_localization.py`）",
}


def _arch_context(rel_path: str) -> str:
    """根据源文件相对路径推断其所属架构模块及中文描述。"""
    parts = rel_path.split("/")
    keys = []
    if parts[0] == "src" and len(parts) > 1:
        keys = [f"src/{parts[1]}", "src"]
    elif parts[0] == "tests":
        if len(parts) > 2 and parts[1] in ("unit", "integration"):
            keys = [f"tests/{parts[1]}", "tests"]
        else:
            keys = ["tests"]
    elif parts[0] == "scripts":
        keys = ["scripts"]
    else:
        keys = ["root"]
    for k in keys:
        if k in _CATEGORY_DESC:
            return f"{k} —— {_CATEGORY_DESC[k]}"
    return "/".join(parts[:2]) if len(parts) > 1 else parts[0]


# ---------------------------------------------------------------------------
# Reverse dependency index
# ---------------------------------------------------------------------------


def build_reverse_index(modules: list[ModuleInfo]) -> dict[str, list[str]]:
    """For each module dotted name, list modules that import it."""
    # Map of importable module name -> dotted name of importing module.
    # We consider both `from X import ...` and `import X`.
    reverse: dict[str, set[str]] = defaultdict(set)

    for m in modules:
        for imp in m.imports:
            # imp is a dotted module path, possibly with alias
            base = imp.split(" as ")[0].strip()
            if base.startswith("src."):
                reverse[base].add(m.rel_module)
        for fi in m.from_imports:
            # fi like "from .foo import bar" or "from src.x.y import z"
            mtch = re.match(r"from\s+(\S+)\s+import", fi)
            if not mtch:
                continue
            mod = mtch.group(1)
            if mod.startswith("src."):
                reverse[mod].add(m.rel_module)
            elif mod.startswith("."):
                # Relative import; resolve against package.
                # Skip precise resolution; mark by tail name.
                tail = mod.lstrip(".")
                if tail:
                    reverse[f"__rel__:{tail}"].add(m.rel_module)

    # Materialize: for each module, find all importers that reference it.
    result: dict[str, list[str]] = {}
    for m in modules:
        importers: set[str] = set()
        # Direct full-path match
        for key in (m.rel_module,):
            importers.update(reverse.get(key, set()))
        # Match by suffix (e.g. ".llm_judge" -> modules ending with .llm_judge)
        tail = m.rel_module.split(".")[-1] if "." in m.rel_module else m.rel_module
        if tail and not m.is_package_init:
            importers.update(reverse.get(f"__rel__:{tail}", set()))
        # Sort and dedupe, exclude self
        result[m.rel_module] = sorted(x for x in importers if x != m.rel_module)
    return result


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def _escape_table(s: str) -> str:
    """转义字符串中的 `|` 与换行，使其可安全嵌入 Markdown 表格单元格。"""
    return s.replace("|", "\\|").replace("\n", " ")


def render_symbol_detail(s: SymbolInfo, module_dotted: str) -> list[str]:
    """渲染单个符号（类/函数/常量）的详细文档段落，含签名、装饰器、基类、成员与 docstring 解析。"""
    lines: list[str] = []
    lines.append(f"### `{s.name}`")
    lines.append("")
    kind_zh = {
        "class": "类",
        "function": "函数",
        "async_function": "异步函数",
        "assignment": "模块常量",
    }.get(s.kind, s.kind)
    anchor = f"{module_dotted}.{s.name}"
    lines.append(
        f"- **类型**：{kind_zh}  |  **行号**：{s.line}–{s.end_line}  |  **完整限定名**：`{anchor}`"
    )
    if s.decorators:
        lines.append("- **装饰器**：" + ", ".join(f"`{d}`" for d in s.decorators))
    if s.bases:
        lines.append("- **基类**：" + ", ".join(f"`{b}`" for b in s.bases))

    if s.kind in ("function", "async_function"):
        kw = "async def" if s.kind == "async_function" else "def"
        lines.append("- **签名**：")
        lines.append("")
        lines.append("```python")
        lines.append(f"{kw} {s.name}{s.signature}:")
        lines.append("```")
    elif s.kind == "class":
        bases_str = "(" + ", ".join(s.bases) + ")" if s.bases else ""
        lines.append("- **定义**：")
        lines.append("")
        lines.append("```python")
        lines.append(f"class {s.name}{bases_str}:")
        lines.append("```")
        if s.members:
            lines.append("- **成员概览**：")
            lines.append("")
            for mem in s.members:
                lines.append(f"  - `{mem}`")
    elif s.kind == "assignment":
        lines.append("- **值**：")
        lines.append("")
        lines.append("```python")
        lines.append(f"{s.name} = {s.signature}")
        lines.append("```")

    lines.append("")
    if s.docstring:
        parsed = parse_google_docstring(s.docstring)
        if parsed.get("summary"):
            lines.append("**摘要**：")
            lines.append("")
            lines.append(parsed["summary"])
            lines.append("")
        for section, title in [
            ("参数", "参数"),
            ("返回值", "返回值"),
            ("生成值", "生成值"),
            ("异常", "异常"),
            ("属性", "属性"),
            ("备注", "备注"),
            ("示例", "示例"),
        ]:
            if parsed.get(section):
                lines.append(f"**{title}**：")
                lines.append("")
                lang = "python" if section in ("示例",) else "text"
                if section == "示例":
                    # Examples often already contain code; wrap as python if looks like code.
                    lines.append("```python")
                else:
                    lines.append(f"```{lang}")
                lines.append(parsed[section])
                lines.append("```")
                lines.append("")
        # Any other custom sections
        for k, v in parsed.items():
            if k in (
                "summary",
                "参数",
                "返回值",
                "生成值",
                "异常",
                "属性",
                "备注",
                "示例",
                "body",
            ):
                continue
            lines.append(f"**{k}**：")
            lines.append("")
            lines.append("```text")
            lines.append(v)
            lines.append("```")
            lines.append("")
    else:
        inferred = infer_docstring(s, module_dotted)
        if inferred:
            lines.append("**说明**（自动推断）：")
            lines.append("")
            lines.append(inferred)
            lines.append("")
        else:
            lines.append("_（无 docstring，可补充用途、参数、返回值、异常与示例。）_")
            lines.append("")
    return lines


def infer_docstring(s: SymbolInfo, module_dotted: str) -> str:
    """Infer a reasonable Chinese description for symbols missing docstrings.

    Recognizes common idioms: module-level logger, Logged* wrappers,
    LangGraph node functions, build_* factories, parse_uri helpers, etc.
    Returns empty string when no confident inference can be made.
    """
    name = s.name
    value = s.signature  # for assignments, this holds the RHS

    # 1) Module-level logger
    if name == "logger" and "logging.getLogger" in value:
        return "模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。"

    # 2) Logged* tool wrappers (created via create_logged_tool)
    if name.startswith("Logged") and "create_logged_tool" in value:
        base = name[len("Logged") :]
        return (
            f"对 `{base}` 工具的日志包装版本，由 `create_logged_tool({base})` 生成，"
            "在原始工具调用前后记录请求与响应，便于审计与调试。"
        )

    # 3) graph instance at module level
    if name == "graph" and "build_graph" in value:
        return "已编译的 LangGraph 工作流实例，模块导入时即构建完成，供 `invoke` / `astream` 直接调用。"

    # 4) workflow instance (subgraphs)
    if name == "workflow" and "build" in value.lower():
        return "已编译的子图工作流实例，模块导入时构建，封装该子模块的完整处理流程。"

    # 5) LangGraph node functions: *_node
    if s.kind in ("function", "async_function") and name.endswith("_node"):
        node = name[: -len("_node")]
        return (
            f"LangGraph 工作流节点函数，对应 `{node}` 节点。"
            "接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，"
            "并返回需要合并回 State 的部分字典或 `Command` 对象。"
        )

    # 6) build_* factory functions
    if s.kind in ("function", "async_function") and name.startswith("build_"):
        return f"工厂函数，构建并返回 `{name[len('build_')]:}` 相关的可运行对象（如图、检索器、智能体等）。"

    # 7) parse_uri helpers
    if name == "parse_uri" and s.kind in ("function", "async_function"):
        return (
            "解析 RAG 后端的 URI 字符串，拆分出 scheme、host、port、collection 等组成部分，"
            "供对应的 retriever 构造客户端时使用。"
        )

    # 8) get_search_config / get_*_config helpers
    if name == "get_search_config" and s.kind in ("function", "async_function"):
        return "从 `conf.yaml` 读取搜索引擎配置段并返回字典，供搜索工具初始化时使用。"
    if (
        name.startswith("get_")
        and name.endswith("_env")
        and s.kind in ("function", "async_function")
    ):
        target = name[len("get_") : -len("_env")].lower()
        return f"从环境变量读取 `{target}` 值，支持默认值与类型转换（{target}）。"

    # 9) load_examples in rag modules
    if name == "load_examples" and s.kind in ("function", "async_function"):
        return "加载示例文档集合，用于向向量库写入初始语料以便测试与演示。"

    # 10) _create_* private factories
    if name.startswith("_create_") and s.kind in ("function", "async_function"):
        return (
            f"私有工厂函数，创建 `{name[len('_create_') :]}` 实例，封装客户端构造细节。"
        )

    # 11) Constants: ALL_CAPS names
    if s.kind == "assignment" and name.isupper():
        # Heuristic by name keywords
        lname = name.lower()
        if "url" in lname or "endpoint" in lname:
            return f"外部服务 API 地址常量 `{name}`，在模块导入时从配置或环境变量读取。"
        if "max" in lname or "limit" in lname or "size" in lname:
            return f"数值上限常量 `{name}`，用于约束对应操作的规模或阈值。"
        if "allowed" in lname:
            return f"白名单常量 `{name}`，列出允许的取值集合，用于输入校验。"
        if "dangerous" in lname or "forbidden" in lname or "skip" in lname:
            return f"黑名单/跳过规则常量 `{name}`，列出需拒绝或排除的取值。"
        if "pattern" in lname:
            return f"正则模式常量 `{name}`，用于文本匹配或抽取。"
        if "criteria" in lname or "prompt" in lname:
            return f"评估/提示词常量 `{name}`，定义对应流程使用的文本模板或判据。"
        if "sections" in lname:
            return f"章节定义常量 `{name}`，列出报告应包含的章节顺序与名称。"
        return f"模块级常量 `{name}`，在导入时初始化，供本模块及相关流程引用。"

    # 12) dataclasses / pydantic models in known shapes
    if s.kind == "class":
        bases = [b.split("[")[0].split(".")[-1] for b in s.bases]
        if "BaseModel" in bases or any("BaseModel" in b for b in s.bases):
            return (
                f"Pydantic 数据模型 `{name}`，用于 API 请求/响应的结构化校验与序列化。"
                "字段即对应的数据契约。"
            )
        if "Enum" in bases or any("Enum" in b for b in s.bases):
            return f"枚举类型 `{name}`，定义该维度可选的取值集合。"
        if "dataclass" in " ".join(s.decorators):
            return f"数据类 `{name}`，作为值对象承载相关属性，通常用于在模块间传递结构化数据。"
        if "TypedDict" in bases or any("TypedDict" in b for b in s.bases):
            return f"TypedDict 类型 `{name}`，描述字典的字段结构，供类型检查器使用。"

    # 13) allowlist vars at module level (lowercase)
    if s.kind == "assignment" and "allowed_origins" in name.lower():
        return "CORS 允许来源集合，从配置解析得到，供 FastAPI 中间件校验跨域请求。"

    # 14) in_memory_store
    if name == "in_memory_store" and s.kind == "assignment":
        return "进程内会话存储字典，用于在无持久化 checkpoint 时保留会话级状态。"

    # 15) env (jinja2 Environment)
    if name == "env" and "Environment" in value:
        return "Jinja2 模板环境实例，配置了模板加载路径与自动转义，用于渲染提示词模板。"

    # 16) test fix mocks (test_fix.py)
    if "mock" in name.lower():
        return (
            f"测试用 mock 对象 `{name}`，用于在测试中替换真实 LLM 依赖以隔离外部调用。"
        )

    # 17) FastAPI route handlers (decorated with @app.post / @app.get etc.)
    if s.kind in ("function", "async_function"):
        decos = " ".join(s.decorators)
        if "@app." in decos or "@router." in decos:
            method = ""
            for m in ("post", "get", "put", "delete", "patch"):
                if f"@app.{m}" in decos or f"@router.{m}" in decos:
                    method = m.upper()
                    break
            # Extract path from decorator
            path = ""
            for d in s.decorators:
                if "@app." in d or "@router." in d:
                    path = d
                    break
            extra = f"（{method} {path}）" if path else ""
            return (
                f"FastAPI 路由处理函数{extra}。"
                "解析请求体并调用对应业务流程，返回 JSON 或 SSE 流式响应。"
            )

    # 18) app = FastAPI(...) instance
    if name == "app" and "FastAPI" in value:
        return (
            "FastAPI 应用实例：DeerFlow 的 HTTP 入口，挂载 chat / generate / enhance / RAG 等路由，"
            "并通过 lifespan 管理 PostgreSQL / MongoDB checkpoint 连接池。"
        )

    # 19) _make_event / _create_*_event helpers
    if name == "_make_event" or (name.startswith("_make_") and "event" in name):
        return "构造 SSE 事件字符串的辅助函数，将事件类型与数据组装为 `text/event-stream` 格式。"

    # 20) get_*_tool factory functions
    if (
        s.kind in ("function", "async_function")
        and name.startswith("get_")
        and name.endswith("_tool")
    ):
        target = name[len("get_") : -len("_tool")]
        return f"工厂函数，根据配置创建并返回 `{target}` 工具实例，供智能体调用。"

    # 21) Crawler / Extractor / Client classes (by name pattern)
    if s.kind == "class":
        if name.endswith("Client"):
            return f"外部服务客户端类 `{name}`，封装对应的 HTTP 调用与响应解析逻辑。"
        if name.endswith("Crawler"):
            return (
                f"爬虫类 `{name}`，实现 URL 抓取与正文抽取流程，协调各抽取器与客户端。"
            )
        if name.endswith("Extractor"):
            return f"正文抽取器类 `{name}`，从原始 HTML 中提取可读正文内容。"
        if name == "Article":
            return "文章数据类，承载抓取结果的标题、正文、URL 等字段。"
        if name.endswith("Tool"):
            return f"LangChain 工具类 `{name}`，封装为可在智能体中调用的 tool 接口。"
        if name.endswith("Wrapper"):
            return f"API 包装类 `{name}`，对底层 SDK 做适配与增强，提供统一调用接口。"
        if name.endswith("Embeddings"):
            return f"嵌入模型类 `{name}`，实现 LangChain Embeddings 接口，将文本转向量供向量库使用。"
        if name.endswith("Provider"):
            return f"RAG 后端 Provider 类 `{name}`，实现检索器接口，封装对应向量库的连接、写入与查询逻辑。"
        if name.endswith("Retriever"):
            return f"检索器类 `{name}`，定义 RAG 后端的统一接口契约。"
        if name == "Chunk":
            return "检索分块数据类，承载一段文档的文本、元数据与来源信息。"
        if name.endswith("Type") and name[0].isupper():
            return f"类型别名/枚举 `{name}`，定义对应维度的可选取值。"

    # 22) continue_to_* conditional edge functions
    if name.startswith("continue_to_") and s.kind in ("function", "async_function"):
        return (
            "LangGraph 条件边函数，根据当前 State 决定下一个执行节点，"
            "返回节点名字符串以驱动工作流路由。"
        )

    # 23) _test_workflow helper
    if name == "_test_workflow":
        return "测试用工作流构建函数，用于在开发/测试环境验证子图编排正确性。"

    # 24) main() in scripts
    if (
        name == "main"
        and s.kind in ("function", "async_function")
        and "scripts" in module_dotted
    ):
        return "脚本主入口函数，解析命令行参数并执行对应操作。"

    # 25) Literal type aliases (e.g. LLMType = Literal["basic", ...])
    if s.kind == "assignment" and "Literal[" in value:
        return (
            f"类型别名 `{name}`，基于 `typing.Literal` 约束可选取值集合，"
            "供类型检查器与 IDE 自动补全使用。"
        )

    # 26) AGENT_LLM_MAP and similar *_MAP dicts
    if s.kind == "assignment" and name.endswith("_MAP") and "{" in value:
        return (
            f"映射常量 `{name}`，定义键到值的静态对照表（如智能体到 LLM 类型的映射）。"
        )

    # 27) Test functions (test_*)
    if s.kind in ("function", "async_function") and name.startswith("test_"):
        return (
            f"测试用例函数 `{name}`。"
            "通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。"
        )

    # 28) Test classes (Test*)
    if s.kind == "class" and name.startswith("Test"):
        return (
            f"pytest 测试类 `{name}`，聚合一组相关的测试用例方法（以 `test_` 开头）。"
        )

    # 29) patch_* fixtures (monkeypatch helpers)
    if s.kind in ("function", "async_function") and name.startswith("patch_"):
        return (
            f"测试 fixture 函数 `{name}`，通过 monkeypatch 替换目标对象以隔离被测单元。"
        )

    # 30) Dummy* mock classes
    if s.kind == "class" and name.startswith("Dummy"):
        return f"测试用替身类 `{name}`，模拟真实对象的接口行为以隔离外部依赖。"

    # 31) load_state_class helper in tests
    if name == "load_state_class" and s.kind in ("function", "async_function"):
        return "测试辅助函数，动态加载 State 类（兼容不同实现）供测试用例使用。"

    # 32) misc test helpers
    if name == "patch_imports":
        return "测试 fixture，批量替换模块导入以隔离依赖。"
    if name == "has_real_db_connection":
        return "测试守卫函数，检测是否具备真实数据库连接，用于跳过需 DB 的测试。"
    if name == "project_root" and s.kind == "assignment":
        return "测试辅助常量，指向仓库根目录，用于定位测试资源文件。"
    if name == "module_name" and s.kind == "assignment":
        return "测试辅助常量，记录当前被测模块名。"
    if name == "client" and "TestClient" in value:
        return "FastAPI TestClient 实例，用于在测试中发送 HTTP 请求到应用。"

    # 33) temp_*_dir fixtures (pytest tmp_path based)
    if name.startswith("temp_") and "dir" in name.lower():
        return f"测试 fixture `{name}`，基于 pytest tmp_path 创建的临时目录，用于隔离文件系统副作用。"

    # 34) *_conf test fixtures
    if name.endswith("_conf") and "tests" in module_dotted:
        return f"测试配置 fixture `{name}`，构造被测模块所需的配置对象。"

    # 35) Re-exported model classes in tests (Step/Plan/State imported from src)
    if name in ("Step", "Plan", "State") and "tests" in module_dotted:
        return (
            f"测试中导入的数据模型 `{name}`（来自 src），用于构造测试用例的输入状态。"
        )

    # 36) pytest fixtures (decorated with @pytest.fixture)
    decos = " ".join(s.decorators)
    if "@pytest.fixture" in decos or "@pytest.mark" in decos:
        if name == "client":
            return (
                "pytest fixture，提供 FastAPI TestClient 实例供测试用例发送 HTTP 请求。"
            )
        if name == "project_root":
            return "pytest fixture，返回仓库根目录路径，用于定位测试资源文件。"
        return f"pytest fixture `{name}`，在测试用例执行前准备所需资源或对象。"

    # 37) sys.modules[...] monkey-patch assignments in test hacks
    if name.startswith("sys.modules["):
        return (
            "测试 hack：直接替换 `sys.modules` 中的模块缓存，用于隔离或注入 mock 模块。"
        )

    return ""


def render_markdown(info: ModuleInfo) -> list[str]:
    """渲染单个模块的完整 Markdown 文档，包含文件信息、概述、依赖、符号表、符号详解、调用关系与示例。"""
    lines: list[str] = []
    lines.append(f"# `{info.path}`")
    lines.append("")
    lines.append(
        "> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。"
    )
    lines.append("")

    # File info
    lines.append("## 文件信息")
    lines.append("")
    lines.append(f"- **相对路径**：`{info.path}`")
    lines.append(f"- **模块导入名**：`{info.rel_module}`")
    if info.is_package_init:
        lines.append("- **类型**：包初始化文件（`__init__.py`）")
    lines.append(f"- **代码行数**：{info.line_count}")
    lines.append(f"- **架构归属**：{_arch_context(info.path)}")
    lines.append("")

    # Overview
    lines.append("## 模块概述")
    lines.append("")
    if info.docstring:
        lines.append("```text")
        lines.append(info.docstring)
        lines.append("```")
    else:
        lines.append("_（该模块未提供 docstring。）_")
    lines.append("")

    # Dependencies
    lines.append("## 依赖关系（上游）")
    lines.append("")
    internal_upstream: list[str] = []
    external_upstream: list[str] = []
    for fi in info.from_imports:
        (
            internal_upstream
            if "src." in fi or fi.startswith("from .")
            else external_upstream
        ).append(fi)
    for imp in info.imports:
        (internal_upstream if imp.startswith("src.") else external_upstream).append(
            f"import {imp}"
        )

    if internal_upstream:
        lines.append("**内部依赖**（项目内模块）：")
        lines.append("")
        for d in internal_upstream:
            lines.append(f"- `{d}`")
        lines.append("")
    if external_upstream:
        lines.append("**外部依赖**（第三方库 / 标准库）：")
        lines.append("")
        for d in external_upstream:
            lines.append(f"- `{d}`")
        lines.append("")
    if not internal_upstream and not external_upstream:
        lines.append("_无导入。_")
        lines.append("")

    # Symbol table
    lines.append("## 导出符号表")
    lines.append("")
    if not info.symbols:
        lines.append("_该模块没有顶层类/函数/常量。_")
    else:
        lines.append("| 类型 | 名称 | 行号 | 签名 / 值 |")
        lines.append("|------|------|------|-----------|")
        for s in info.symbols:
            sig = _escape_table(s.signature or "")
            if len(sig) > 100:
                sig = sig[:97] + "..."
            kind_zh = {
                "class": "类",
                "function": "函数",
                "async_function": "异步函数",
                "assignment": "常量",
            }.get(s.kind, s.kind)
            lines.append(f"| {kind_zh} | `{s.name}` | {s.line} | `{sig}` |")
    lines.append("")

    # Symbol details
    lines.append("## 符号详解")
    lines.append("")
    if not info.symbols:
        lines.append("_无顶层符号。_")
        lines.append("")
    else:
        for s in info.symbols:
            lines.extend(render_symbol_detail(s, info.rel_module))

    # Reverse deps
    lines.append("## 调用关系（下游）")
    lines.append("")
    if info.imported_by:
        lines.append("**被以下模块导入**：")
        lines.append("")
        for imp in info.imported_by:
            lines.append(f"- `{imp}`")
        lines.append("")
    else:
        lines.append(
            "_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_"
        )
        lines.append("")

    # Example
    example_dir = REPO_ROOT / "scripts" / "api_reference_examples"
    example_file = example_dir / (info.path + ".example")
    lines.append("## 示例用法")
    lines.append("")
    if example_file.exists():
        example_text = example_file.read_text(encoding="utf-8").rstrip()
        lines.append("```python")
        lines.append(example_text)
        lines.append("```")
    else:
        # Pick a representative symbol for the example: prefer public functions
        # (non-dunder, non-private), then classes, then constants.
        def _example_priority(s: SymbolInfo) -> tuple:
            if s.name.startswith("_"):
                return (3, s.line)
            if s.kind in ("function", "async_function"):
                score = (
                    0
                    if s.name in ("main", "run", "ask", "evaluate", "build_graph")
                    else 1
                )
                return (0, score, s.line)
            if s.kind == "class":
                return (1, s.line)
            return (2, s.line)

        sample = min(info.symbols, key=_example_priority) if info.symbols else None
        lines.append("```python")
        if sample:
            lines.append(f"from {info.rel_module} import {sample.name}")
            lines.append("#")
            lines.append(f"# TODO: 结合业务场景补充 {sample.name} 的典型调用示例。")
        else:
            lines.append(f"# import {info.rel_module}")
            lines.append("# TODO: 补充该模块的典型使用示例。")
        lines.append("```")
    lines.append("")

    # Notes
    lines.append("## 备注")
    lines.append("")
    lines.append("- 自动生成时间：" + os.environ.get("GEN_TIMESTAMP", "unknown"))
    lines.append("- 重新生成：`python scripts/gen_api_reference.py`")
    lines.append("")
    return lines


# ---------------------------------------------------------------------------
# Module README and top-level index
# ---------------------------------------------------------------------------


def render_module_readme(dir_rel: str, modules: list[ModuleInfo]) -> list[str]:
    """渲染某个目录的 README.md：文件清单表 + 目录内 mermaid 依赖图。"""
    lines: list[str] = []
    lines.append(f"# `{dir_rel}/` 模块索引")
    lines.append("")
    lines.append(
        f"> 本目录下共有 {len(modules)} 个 Python 源文件，下表汇总了每个文件及其文档链接。"
    )
    lines.append("")
    if dir_rel in _CATEGORY_DESC:
        lines.append("**模块定位**：" + _CATEGORY_DESC[dir_rel])
        lines.append("")
    lines.append("| 源文件 | 文档 | 模块名 | 行数 | 顶层符号数 | 简述 |")
    lines.append("|--------|------|--------|------|------------|------|")
    for m in modules:
        doc_link = m.path + ".md"
        summary = m.docstring.splitlines()[0] if m.docstring else ""
        summary = _escape_table(summary)
        if len(summary) > 60:
            summary = summary[:57] + "..."
        lines.append(
            f"| `{m.path}` | [{doc_link}]({Path(doc_link).name}) | `{m.rel_module}` | {m.line_count} | {len(m.symbols)} | {summary} |"
        )
    lines.append("")
    # Dependency graph (within this directory)
    lines.append("## 目录内依赖关系")
    lines.append("")
    module_names = {m.rel_module for m in modules}
    # Build a tail-name lookup so relative imports (".nodes") can resolve.
    tail_to_full: dict[str, str] = {}
    for m in modules:
        tail = m.rel_module.split(".")[-1]
        tail_to_full.setdefault(tail, m.rel_module)
    has_edge = False
    mermaid_lines: list[str] = ["graph LR"]
    for m in modules:
        for fi in m.from_imports:
            mtch = re.match(r"from\s+(\S+)\s+import", fi)
            if not mtch:
                continue
            mod = mtch.group(1)
            target = None
            if mod in module_names:
                target = mod
            elif mod.startswith("."):
                tail = mod.lstrip(".")
                if tail in tail_to_full:
                    target = tail_to_full[tail]
            if target and target != m.rel_module:
                a = m.rel_module.replace(".", "_")
                b = target.replace(".", "_")
                mermaid_lines.append(f"    {b}[{target}] --> {a}[{m.rel_module}]")
                has_edge = True
    if has_edge:
        lines.append("```mermaid")
        lines.extend(mermaid_lines)
        lines.append("```")
    else:
        lines.append("_本目录内模块之间无直接导入关系（或仅通过包外路径引用）。_")
    lines.append("")
    return lines


def render_top_index(all_modules: list[ModuleInfo]) -> list[str]:
    """渲染顶层 INDEX.md：总览统计、按模块分组、架构 mermaid 概览图。"""
    lines: list[str] = []
    lines.append("# DeerFlow API 参考索引")
    lines.append("")
    lines.append(
        "> 本索引汇总仓库内所有 Python 源文件的 API 参考文档，按目录分组。"
        "每个文件对应一篇 `.py.md` 文档，包含文件信息、模块概述、依赖关系、"
        "导出符号表、符号详解、调用关系与示例用法。"
    )
    lines.append("")
    lines.append(
        "文档由 `scripts/gen_api_reference.py` 自动生成，覆盖 `src/`、`tests/`、`scripts/` 及根目录 Python 文件。"
    )
    lines.append("")

    # Stats
    total_lines = sum(m.line_count for m in all_modules)
    total_symbols = sum(len(m.symbols) for m in all_modules)
    lines.append("## 总览")
    lines.append("")
    lines.append(f"- **源文件数**：{len(all_modules)}")
    lines.append(f"- **代码总行数**：{total_lines:,}")
    lines.append(f"- **顶层符号总数**：{total_symbols}")
    lines.append("")

    # Group by top-level category
    groups: dict[str, list[ModuleInfo]] = defaultdict(list)
    for m in all_modules:
        parts = m.path.split("/")
        if parts[0] == "src":
            if len(parts) <= 2:
                # either src/__init__.py or src/<file>.py
                key = "src（根）"
            else:
                key = f"src/{parts[1]}"
        elif parts[0] == "tests":
            if len(parts) <= 2:
                key = "tests（根）"
            elif len(parts) == 3 and parts[1] not in ("unit", "integration"):
                # tests/<dir>/<file>.py but not under unit/integration
                key = f"tests/{parts[1]}"
            elif len(parts) >= 3:
                key = f"tests/{parts[1]}"
            else:
                key = "tests（根）"
        elif parts[0] == "scripts":
            key = "scripts"
        else:
            key = "根目录"
        groups[key].append(m)

    def _sort_key(k: str) -> tuple:
        order = {"根目录": 0, "src（根）": 1, "tests（根）": 5, "scripts": 6}
        if k in order:
            return (order[k], k)
        if k.startswith("src/"):
            return (2, k)
        if k.startswith("tests/"):
            return (4, k)
        return (9, k)

    ordered_keys = sorted(groups.keys(), key=_sort_key)

    lines.append("## 目录分组")
    lines.append("")
    for key in ordered_keys:
        mods = sorted(groups[key], key=lambda m: m.path)
        desc = _CATEGORY_DESC.get(key, "")
        lines.append(f"### {key}")
        lines.append("")
        if desc:
            lines.append(desc)
            lines.append("")
        lines.append(f"共 {len(mods)} 个文件，详见各目录下 `README.md`：")
        lines.append("")
        lines.append("| 源文件 | 文档 | 模块名 | 行数 | 符号数 |")
        lines.append("|--------|------|--------|------|--------|")
        for m in mods:
            doc_rel = m.path + ".md"
            lines.append(
                f"| `{m.path}` | [{doc_rel}]({doc_rel}) | `{m.rel_module}` | {m.line_count} | {len(m.symbols)} |"
            )
        lines.append("")

    # Architecture overview
    lines.append("## 架构概览")
    lines.append("")
    lines.append("```mermaid")
    lines.append("graph TD")
    lines.append("    User[用户/CLI-UI]")
    lines.append("    Server[FastAPI 服务<br/>src/server]")
    lines.append("    Graph[LangGraph 主工作流<br/>src/graph]")
    lines.append("    Agents[智能体<br/>src/agents]")
    lines.append("    LLM[LLM 适配<br/>src/llms]")
    lines.append("    Tools[工具集<br/>src/tools]")
    lines.append("    Crawler[爬虫<br/>src/crawler]")
    lines.append("    RAG[检索增强<br/>src/rag]")
    lines.append("    Prompts[提示词<br/>src/prompts]")
    lines.append("    Eval[评估<br/>src/eval]")
    lines.append("    Citations[引用<br/>src/citations]")
    lines.append("    Config[配置<br/>src/config]")
    lines.append("    Utils[工具函数<br/>src/utils]")
    lines.append("    User --> Server")
    lines.append("    Server --> Graph")
    lines.append("    Graph --> Agents")
    lines.append("    Agents --> LLM")
    lines.append("    Agents --> Tools")
    lines.append("    Agents --> Prompts")
    lines.append("    Tools --> Crawler")
    lines.append("    Tools --> RAG")
    lines.append("    Graph --> Citations")
    lines.append("    Graph --> Eval")
    lines.append("    Graph --> Config")
    lines.append("    Server --> Config")
    lines.append("    Agents --> Utils")
    lines.append("    Crawler --> Utils")
    lines.append("```")
    lines.append("")

    lines.append("## 子图模块")
    lines.append("")
    lines.append("- `src/podcast/`：播客生成子图")
    lines.append("- `src/ppt/`：PPT 生成子图")
    lines.append("- `src/prose/`：散文编辑子图（改写/扩写/缩写/修复/续写/精简）")
    lines.append("- `src/prompt_enhancer/`：提示词增强子图")
    lines.append("")
    return lines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def collect_files() -> list[Path]:
    """收集待处理的 Python 源文件列表（src/、tests/、scripts/ 及根目录 *.py）。"""
    files: list[Path] = []
    for d in SCAN_DIRS:
        base = REPO_ROOT / d
        if not base.exists():
            continue
        for p in base.rglob("*.py"):
            if "__pycache__" in p.parts:
                continue
            files.append(p)
    for name in ROOT_PY_FILES:
        p = REPO_ROOT / name
        if p.exists():
            files.append(p)
    return sorted(files)


def output_path_for(file_path: Path) -> Path:
    """根据源文件路径计算对应的文档输出路径（`<rel>.py.md`）。"""
    rel = file_path.relative_to(REPO_ROOT)
    return OUT_ROOT / (str(rel) + ".md")


def main() -> int:
    import datetime

    os.environ.setdefault(
        "GEN_TIMESTAMP", datetime.datetime.now().isoformat(timespec="seconds")
    )

    files = collect_files()
    print(f"Found {len(files)} python source files")

    # Parse all
    modules: list[ModuleInfo] = []
    for f in files:
        modules.append(parse_module(f))

    # Build reverse dependency index
    reverse = build_reverse_index(modules)
    for m in modules:
        m.imported_by = reverse.get(m.rel_module, [])

    # Render per-file docs
    manifest: list[dict[str, Any]] = []
    for m, f in zip(modules, files):
        md_lines = render_markdown(m)
        out = output_path_for(f)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(md_lines), encoding="utf-8")
        manifest.append(
            {
                "source": m.path,
                "module": m.rel_module,
                "doc": str(out.relative_to(REPO_ROOT)),
                "symbols": len(m.symbols),
                "lines": m.line_count,
                "imported_by": m.imported_by,
            }
        )

    # Render per-directory README
    dirs: dict[str, list[ModuleInfo]] = defaultdict(list)
    for m in modules:
        dir_rel = str(Path(m.path).parent)
        if dir_rel == ".":
            dir_rel = "."
        dirs[dir_rel].append(m)

    for dir_rel, mods in dirs.items():
        mods_sorted = sorted(mods, key=lambda x: x.path)
        readme_lines = render_module_readme(dir_rel, mods_sorted)
        out_dir = OUT_ROOT / dir_rel
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "README.md").write_text("\n".join(readme_lines), encoding="utf-8")

    # Top-level index
    index_lines = render_top_index(modules)
    (OUT_ROOT / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")

    # Manifest
    manifest_path = OUT_ROOT / "_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"Wrote {len(manifest)} file docs + {len(dirs)} READMEs + INDEX.md")
    print(f"Output root: {OUT_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

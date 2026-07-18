# `scripts/gen_api_reference.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`scripts/gen_api_reference.py`
- **模块导入名**：`scripts.gen_api_reference`
- **代码行数**：1291
- **架构归属**：scripts —— 仓库脚本（API 文档生成器、license 头检查等）

## 模块概述

```text
Generate detailed API reference markdown docs for every Python source file.

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
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from __future__ import annotations`
- `from collections import defaultdict`
- `from dataclasses import dataclass, field`
- `from pathlib import Path`
- `from typing import Any`
- `import ast`
- `import json`
- `import os`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `REPO_ROOT` | 33 | `Path(__file__).resolve().parent.parent` |
| 常量 | `OUT_ROOT` | 34 | `REPO_ROOT / 'docs' / 'api-reference'` |
| 常量 | `SCAN_DIRS` | 36 | `['src', 'tests', 'scripts']` |
| 常量 | `ROOT_PY_FILES` | 37 | `['main.py', 'server.py', 'test_fix.py']` |
| 类 | `SymbolInfo` | 46 | `` |
| 类 | `ModuleInfo` | 59 | `` |
| 函数 | `_format_decorator` | 76 | `(dec: ast.AST) -> str` |
| 函数 | `_format_signature` | 88 | `(node: ast.FunctionDef \| ast.AsyncFunctionDef) -> str` |
| 函数 | `_docstring` | 107 | `(node: Any) -> str` |
| 函数 | `_base_names` | 116 | `(bases: list[ast.AST]) -> list[str]` |
| 函数 | `_class_members` | 127 | `(node: ast.ClassDef) -> list[str]` |
| 函数 | `_dotted_module` | 150 | `(file_path: Path) -> tuple[str, bool]` |
| 函数 | `parse_module` | 162 | `(file_path: Path) -> ModuleInfo` |
| 函数 | `parse_google_docstring` | 279 | `(doc: str) -> dict[str, str]` |
| 函数 | `_arch_context` | 353 | `(rel_path: str) -> str` |
| 函数 | `build_reverse_index` | 379 | `(modules: list[ModuleInfo]) -> dict[str, list[str]]` |
| 函数 | `_escape_table` | 427 | `(s: str) -> str` |
| 函数 | `render_symbol_detail` | 432 | `(s: SymbolInfo, module_dotted: str) -> list[str]` |
| 函数 | `infer_docstring` | 540 | `(s: SymbolInfo, module_dotted: str) -> str` |
| 函数 | `render_markdown` | 837 | `(info: ModuleInfo) -> list[str]` |
| 函数 | `render_module_readme` | 1000 | `(dir_rel: str, modules: list[ModuleInfo]) -> list[str]` |
| 函数 | `render_top_index` | 1063 | `(all_modules: list[ModuleInfo]) -> list[str]` |
| 函数 | `collect_files` | 1198 | `() -> list[Path]` |
| 函数 | `output_path_for` | 1216 | `(file_path: Path) -> Path` |
| 函数 | `main` | 1222 | `() -> int` |

## 符号详解

### `REPO_ROOT`

- **类型**：模块常量  |  **行号**：33–33  |  **完整限定名**：`scripts.gen_api_reference.REPO_ROOT`
- **值**：

```python
REPO_ROOT = Path(__file__).resolve().parent.parent
```

**说明**（自动推断）：

模块级常量 `REPO_ROOT`，在导入时初始化，供本模块及相关流程引用。

### `OUT_ROOT`

- **类型**：模块常量  |  **行号**：34–34  |  **完整限定名**：`scripts.gen_api_reference.OUT_ROOT`
- **值**：

```python
OUT_ROOT = REPO_ROOT / 'docs' / 'api-reference'
```

**说明**（自动推断）：

模块级常量 `OUT_ROOT`，在导入时初始化，供本模块及相关流程引用。

### `SCAN_DIRS`

- **类型**：模块常量  |  **行号**：36–36  |  **完整限定名**：`scripts.gen_api_reference.SCAN_DIRS`
- **值**：

```python
SCAN_DIRS = ['src', 'tests', 'scripts']
```

**说明**（自动推断）：

模块级常量 `SCAN_DIRS`，在导入时初始化，供本模块及相关流程引用。

### `ROOT_PY_FILES`

- **类型**：模块常量  |  **行号**：37–37  |  **完整限定名**：`scripts.gen_api_reference.ROOT_PY_FILES`
- **值**：

```python
ROOT_PY_FILES = ['main.py', 'server.py', 'test_fix.py']
```

**说明**（自动推断）：

模块级常量 `ROOT_PY_FILES`，在导入时初始化，供本模块及相关流程引用。

### `SymbolInfo`

- **类型**：类  |  **行号**：46–55  |  **完整限定名**：`scripts.gen_api_reference.SymbolInfo`
- **装饰器**：`@dataclass`
- **定义**：

```python
class SymbolInfo:
```
- **成员概览**：

  - `attr kind`
  - `attr name`
  - `attr signature`
  - `attr docstring`
  - `attr bases`
  - `attr decorators`
  - `attr line`
  - `attr end_line`
  - `attr members`

**说明**（自动推断）：

数据类 `SymbolInfo`，作为值对象承载相关属性，通常用于在模块间传递结构化数据。

### `ModuleInfo`

- **类型**：类  |  **行号**：59–68  |  **完整限定名**：`scripts.gen_api_reference.ModuleInfo`
- **装饰器**：`@dataclass`
- **定义**：

```python
class ModuleInfo:
```
- **成员概览**：

  - `attr path`
  - `attr rel_module`
  - `attr is_package_init`
  - `attr docstring`
  - `attr symbols`
  - `attr imports`
  - `attr from_imports`
  - `attr line_count`
  - `attr imported_by`

**说明**（自动推断）：

数据类 `ModuleInfo`，作为值对象承载相关属性，通常用于在模块间传递结构化数据。

### `_format_decorator`

- **类型**：函数  |  **行号**：76–85  |  **完整限定名**：`scripts.gen_api_reference._format_decorator`
- **签名**：

```python
def _format_decorator(dec: ast.AST) -> str:
```

**摘要**：

将 AST 装饰器节点格式化为 `@decorator` 形式的字符串。

### `_format_signature`

- **类型**：函数  |  **行号**：88–104  |  **完整限定名**：`scripts.gen_api_reference._format_signature`
- **签名**：

```python
def _format_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
```

**摘要**：

将函数/异步函数节点的参数与返回注解格式化为签名字符串（含括号与 `-> 返回类型`）。

### `_docstring`

- **类型**：函数  |  **行号**：107–113  |  **完整限定名**：`scripts.gen_api_reference._docstring`
- **签名**：

```python
def _docstring(node: Any) -> str:
```

**摘要**：

安全提取 AST 节点的 docstring，失败时返回空字符串。

### `_base_names`

- **类型**：函数  |  **行号**：116–124  |  **完整限定名**：`scripts.gen_api_reference._base_names`
- **签名**：

```python
def _base_names(bases: list[ast.AST]) -> list[str]:
```

**摘要**：

将类定义的基类列表格式化为字符串列表（如 `BaseModel`、`Enum`）。

### `_class_members`

- **类型**：函数  |  **行号**：127–147  |  **完整限定名**：`scripts.gen_api_reference._class_members`
- **签名**：

```python
def _class_members(node: ast.ClassDef) -> list[str]:
```

**摘要**：

提取类体内的方法与属性名，用于在文档中展示成员概览。

### `_dotted_module`

- **类型**：函数  |  **行号**：150–159  |  **完整限定名**：`scripts.gen_api_reference._dotted_module`
- **签名**：

```python
def _dotted_module(file_path: Path) -> tuple[str, bool]:
```

**摘要**：

根据文件路径计算点分模块名（如 `src.graph.builder`），并返回是否为 `__init__.py`。

### `parse_module`

- **类型**：函数  |  **行号**：162–254  |  **完整限定名**：`scripts.gen_api_reference.parse_module`
- **签名**：

```python
def parse_module(file_path: Path) -> ModuleInfo:
```

**摘要**：

解析单个 Python 源文件，返回模块信息：docstring、顶层符号、导入、行数。

### `parse_google_docstring`

- **类型**：函数  |  **行号**：279–317  |  **完整限定名**：`scripts.gen_api_reference.parse_google_docstring`
- **签名**：

```python
def parse_google_docstring(doc: str) -> dict[str, str]:
```

**摘要**：

Split a Google-style docstring into sections.

### `_arch_context`

- **类型**：函数  |  **行号**：353–371  |  **完整限定名**：`scripts.gen_api_reference._arch_context`
- **签名**：

```python
def _arch_context(rel_path: str) -> str:
```

**摘要**：

根据源文件相对路径推断其所属架构模块及中文描述。

### `build_reverse_index`

- **类型**：函数  |  **行号**：379–419  |  **完整限定名**：`scripts.gen_api_reference.build_reverse_index`
- **签名**：

```python
def build_reverse_index(modules: list[ModuleInfo]) -> dict[str, list[str]]:
```

**摘要**：

For each module dotted name, list modules that import it.

### `_escape_table`

- **类型**：函数  |  **行号**：427–429  |  **完整限定名**：`scripts.gen_api_reference._escape_table`
- **签名**：

```python
def _escape_table(s: str) -> str:
```

**摘要**：

转义字符串中的 `|` 与换行，使其可安全嵌入 Markdown 表格单元格。

### `render_symbol_detail`

- **类型**：函数  |  **行号**：432–537  |  **完整限定名**：`scripts.gen_api_reference.render_symbol_detail`
- **签名**：

```python
def render_symbol_detail(s: SymbolInfo, module_dotted: str) -> list[str]:
```

**摘要**：

渲染单个符号（类/函数/常量）的详细文档段落，含签名、装饰器、基类、成员与 docstring 解析。

### `infer_docstring`

- **类型**：函数  |  **行号**：540–834  |  **完整限定名**：`scripts.gen_api_reference.infer_docstring`
- **签名**：

```python
def infer_docstring(s: SymbolInfo, module_dotted: str) -> str:
```

**摘要**：

Infer a reasonable Chinese description for symbols missing docstrings.

### `render_markdown`

- **类型**：函数  |  **行号**：837–992  |  **完整限定名**：`scripts.gen_api_reference.render_markdown`
- **签名**：

```python
def render_markdown(info: ModuleInfo) -> list[str]:
```

**摘要**：

渲染单个模块的完整 Markdown 文档，包含文件信息、概述、依赖、符号表、符号详解、调用关系与示例。

### `render_module_readme`

- **类型**：函数  |  **行号**：1000–1060  |  **完整限定名**：`scripts.gen_api_reference.render_module_readme`
- **签名**：

```python
def render_module_readme(dir_rel: str, modules: list[ModuleInfo]) -> list[str]:
```

**摘要**：

渲染某个目录的 README.md：文件清单表 + 目录内 mermaid 依赖图。

### `render_top_index`

- **类型**：函数  |  **行号**：1063–1190  |  **完整限定名**：`scripts.gen_api_reference.render_top_index`
- **签名**：

```python
def render_top_index(all_modules: list[ModuleInfo]) -> list[str]:
```

**摘要**：

渲染顶层 INDEX.md：总览统计、按模块分组、架构 mermaid 概览图。

### `collect_files`

- **类型**：函数  |  **行号**：1198–1213  |  **完整限定名**：`scripts.gen_api_reference.collect_files`
- **签名**：

```python
def collect_files() -> list[Path]:
```

**摘要**：

收集待处理的 Python 源文件列表（src/、tests/、scripts/ 及根目录 *.py）。

### `output_path_for`

- **类型**：函数  |  **行号**：1216–1219  |  **完整限定名**：`scripts.gen_api_reference.output_path_for`
- **签名**：

```python
def output_path_for(file_path: Path) -> Path:
```

**摘要**：

根据源文件路径计算对应的文档输出路径（`<rel>.py.md`）。

### `main`

- **类型**：函数  |  **行号**：1222–1287  |  **完整限定名**：`scripts.gen_api_reference.main`
- **签名**：

```python
def main() -> int:
```

**说明**（自动推断）：

脚本主入口函数，解析命令行参数并执行对应操作。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from scripts.gen_api_reference import main
#
# TODO: 结合业务场景补充 main 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

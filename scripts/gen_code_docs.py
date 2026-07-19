#!/usr/bin/env python3
"""Deep code-fact analyzer for DeerFlow Python modules.

For each .py file, emit a sibling .py.md that documents the module based on
*code facts* extracted by static analysis - not docstrings (most functions
don't have them). Extracted facts include:

  - module structure (imports, module-level constants, __all__)
  - classes: bases, MRO, decorators, class vars, methods grouped by kind
  - functions: decorators, args/defaults/annotations, sync/async,
    calls made, raises, returns, branching complexity
  - call edges within the file (who calls whom)
  - external symbols imported (which modules/types are depended on)
  - side-effect hints: subprocess, network, file IO, eval/exec, os.environ

Usage:
    python scripts/gen_code_docs.py [--root backend] [--out-root docs/code]
        [--include-skills] [--include-tests] [--force]

Output layout mirrors the source tree under <out-root>/<root>/.
Example: backend/packages/harness/deerflow/skills/types.py
      -> docs/code/backend/packages/harness/deerflow/skills/types.py.md
"""

from __future__ import annotations

import argparse
import ast
import os
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

# --------------------------------------------------------------------------- #
# Side-effect detectors                                                       #
# --------------------------------------------------------------------------- #

_NET_ATTRS = {
    "requests",
    "httpx",
    "urllib",
    "aiohttp",
    "socket",
    "http",
    "fetch",
    "get",
    "post",
    "put",
    "delete",
    "patch",
    "head",
    "request",
    "connect",
    "send",
    "recv",
}
# receiver names that indicate a real network client (so dict.get / task.get
# are not mis-flagged as network calls).
_NET_MODULES = {
    "requests",
    "httpx",
    "urllib",
    "aiohttp",
    "socket",
    "http",
    "client",
    "session",
    "conn",
    "connection",
    "ws",
    "websocket",
    "pool",
    "httpclient",
    "asyncclient",
    "apiclient",
}
_FILE_FUNCS = {
    "open",
    "read",
    "read_text",
    "read_bytes",
    "write",
    "write_text",
    "write_bytes",
    "readlines",
    "writelines",
    "mkdir",
    "unlink",
    "rmdir",
    "rename",
    "replace",
    "glob",
    "rglob",
    "iterdir",
    "exists",
    "stat",
    "touch",
    "chmod",
    "chown",
}
_SUBPROC_ATTRS = {
    "run",
    "Popen",
    "call",
    "check_call",
    "check_output",
    "create_subprocess_exec",
    "create_subprocess_shell",
}
_DANGER_ATTRS = {"eval", "exec", "compile", "__import__"}
_ENV_ATTRS = {"environ", "getenv", "putenv", "unsetenv"}
_REFLECT_ATTRS = {"getattr", "setattr", "delattr", "hasattr", "import_module"}


@dataclass
class SideEffects:
    network: list[str] = field(default_factory=list)
    file_io: list[str] = field(default_factory=list)
    subprocess: list[str] = field(default_factory=list)
    dangerous: list[str] = field(default_factory=list)
    env: list[str] = field(default_factory=list)
    reflection: list[str] = field(default_factory=list)

    def any(self) -> bool:
        return any(
            [
                self.network,
                self.file_io,
                self.subprocess,
                self.dangerous,
                self.env,
                self.reflection,
            ]
        )


class SideEffectVisitor(ast.NodeVisitor):
    """Walk a function/class body and collect side-effect call sites."""

    def __init__(self) -> None:
        self.fx = SideEffects()

    def _record(self, bucket: list[str], node: ast.Call, label: str) -> None:
        loc = f"L{node.lineno}"
        bucket.append(f"{label} ({loc})")

    def _call_label(self, node: ast.Call) -> str | None:
        func = node.func
        # direct name: open(...), eval(...)
        if isinstance(func, ast.Name):
            return func.id
        # attribute: x.get(...), requests.get(...), subprocess.run(...)
        if isinstance(func, ast.Attribute):
            return func.attr
        return None

    def visit_Call(self, node: ast.Call) -> None:
        label = self._call_label(node)
        if label:
            low = label.lower()
            if label in _FILE_FUNCS or low in _FILE_FUNCS:
                self._record(self.fx.file_io, node, label)
            elif label in _SUBPROC_ATTRS:
                self._record(self.fx.subprocess, node, label)
            elif label in _DANGER_ATTRS:
                self._record(self.fx.dangerous, node, label)
            elif label in _ENV_ATTRS:
                self._record(self.fx.env, node, label)
            elif label in _REFLECT_ATTRS:
                self._record(self.fx.reflection, node, label)
            elif low in _NET_ATTRS and isinstance(node.func, ast.Attribute):
                # require the receiver to look like a net module/client to
                # avoid flagging dict.get / task.get as network
                recv = node.func.value
                recv_name = ""
                if isinstance(recv, ast.Name):
                    recv_name = recv.id
                elif isinstance(recv, ast.Attribute):
                    recv_name = recv.attr
                if recv_name in _NET_MODULES or recv_name.lower() in _NET_MODULES:
                    self._record(self.fx.network, node, label)
        self.generic_visit(node)


# --------------------------------------------------------------------------- #
# Module analysis                                                             #
# --------------------------------------------------------------------------- #


@dataclass
class FuncFacts:
    name: str
    qualname: str
    kind: str  # function | async-function | method | classmethod | staticmethod | property
    lineno: int
    decorators: list[str]
    args: list[str]
    returns: str | None
    is_async: bool
    calls: list[str]  # unique callee names
    raises: list[str]
    returns_const: list[str]  # returned literals/names
    branch_count: int
    has_yield: bool
    has_star_args: bool  # *args/**kwargs
    side_fx: SideEffects
    body_size: int
    doc_summary: str  # first line of docstring IF present (info only)


@dataclass
class ClassFacts:
    name: str
    lineno: int
    decorators: list[str]
    bases: list[str]
    mro_hint: list[str]  # direct bases only
    class_vars: list[tuple[str, str]]  # (name, value-repr)
    methods: list[FuncFacts]
    nested_classes: list[str]
    is_abstract: bool  # has abstractmethod
    metaclass: str | None
    doc_summary: str


@dataclass
class ModuleFacts:
    path: Path
    rel_path: str
    imports: list[str]  # external symbols
    from_imports: list[tuple[str, list[str]]]  # (module, names)
    constants: list[tuple[str, str]]  # (name, value-repr)
    dunder_all: list[str] | None
    functions: list[FuncFacts]
    classes: list[ClassFacts]
    call_graph: dict[str, list[str]]  # caller -> callees
    has_main_guard: bool
    module_doc: str | None
    line_count: int


# --------------------------------------------------------------------------- #
# Extractors                                                                  #
# --------------------------------------------------------------------------- #


def _decorator_name(dec: ast.expr) -> str:
    if isinstance(dec, ast.Name):
        return dec.id
    if isinstance(dec, ast.Attribute):
        parts = []
        cur: ast.expr = dec
        while isinstance(cur, ast.Attribute):
            parts.append(cur.attr)
            cur = cur.value
        if isinstance(cur, ast.Name):
            parts.append(cur.id)
        return ".".join(reversed(parts))
    if isinstance(dec, ast.Call):
        return _decorator_name(dec.func) + "(...)"
    return ast.unparse(dec)


def _arg_repr(arg: ast.arg) -> str:
    name = arg.arg
    ann = ast.unparse(arg.annotation) if arg.annotation is not None else ""
    return f"{name}{': ' + ann if ann else ''}"


def _arg_list(node: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    parts: list[str] = []
    a = node.args
    # positional-only then normal
    for arg in list(a.posonlyargs) + list(a.args):
        parts.append(_arg_repr(arg))
    if a.vararg:
        parts.append(f"*{a.vararg.arg}")
    if a.kwonlyargs:
        if not a.vararg:
            parts.append("*")
        for arg in a.kwonlyargs:
            parts.append(_arg_repr(arg))
    if a.kwarg:
        parts.append(f"**{a.kwarg.arg}")
    return parts


def _return_repr(node: ast.Return) -> str | None:
    if node.value is None:
        return "None"
    return ast.unparse(node.value)


def _raise_name(node: ast.Raise) -> str:
    if node.exc is None:
        return "bare raise"
    return ast.unparse(node.exc)


class _CallCollector(ast.NodeVisitor):
    """Collect called names within a function body."""

    def __init__(self) -> None:
        self.calls: list[str] = []
        self.raises: list[str] = []
        self.returns: list[str] = []
        self.branches = 0
        self.has_yield = False

    def visit_Call(self, node: ast.Call) -> None:
        label: str
        if isinstance(node.func, ast.Name):
            label = node.func.id
        elif isinstance(node.func, ast.Attribute):
            label = node.func.attr
        else:
            label = ast.unparse(node.func)
        self.calls.append(label)
        self.generic_visit(node)

    def visit_Raise(self, node: ast.Raise) -> None:
        self.raises.append(_raise_name(node))
        self.generic_visit(node)

    def visit_Return(self, node: ast.Return) -> None:
        self.returns.append(_return_repr(node))
        self.generic_visit(node)

    # branch indicators
    def visit_If(self, node: ast.If) -> None:
        self.branches += 1
        self.generic_visit(node)

    def visit_For(self, node: ast.For) -> None:
        self.branches += 1
        self.generic_visit(node)

    def visit_AsyncFor(self, node: ast.AsyncFor) -> None:
        self.branches += 1
        self.generic_visit(node)

    def visit_While(self, node: ast.While) -> None:
        self.branches += 1
        self.generic_visit(node)

    def visit_With(self, node: ast.With) -> None:
        self.branches += 1
        self.generic_visit(node)

    def visit_AsyncWith(self, node: ast.AsyncWith) -> None:
        self.branches += 1
        self.generic_visit(node)

    def visit_Try(self, node: ast.Try) -> None:
        self.branches += 1
        self.generic_visit(node)

    def visit_Match(self, node: ast.Match) -> None:  # py3.10+
        self.branches += 1
        self.generic_visit(node)

    def visit_Yield(self, node: ast.Yield) -> None:
        self.has_yield = True

    def visit_YieldFrom(self, node: ast.YieldFrom) -> None:
        self.has_yield = True


def _const_repr(node: ast.expr, limit: int = 60) -> str:
    try:
        text = ast.unparse(node)
    except Exception:
        return "<expr>"
    if len(text) > limit:
        text = text[: limit - 3] + "..."
    return text


def _first_doc_line(doc: str | None) -> str:
    if not doc:
        return ""
    line = doc.strip().splitlines()[0].strip() if doc.strip() else ""
    return line[:120]


def _analyze_function(
    node: ast.FunctionDef | ast.AsyncFunctionDef, qualname_prefix: str, kind: str
) -> FuncFacts:
    cc = _CallCollector()
    cc.visit(node)

    fx_vis = SideEffectVisitor()
    for child in node.body:
        fx_vis.visit(child)

    decorators = [_decorator_name(d) for d in node.decorator_list]
    args = _arg_list(node)
    returns = ast.unparse(node.returns) if node.returns else None
    is_async = isinstance(node, ast.AsyncFunctionDef)

    # de-duplicate calls/raises/returns preserving order
    def _dedupe(seq: list[str]) -> list[str]:
        seen: set[str] = set()
        out: list[str] = []
        for x in seq:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out

    return FuncFacts(
        name=node.name,
        qualname=f"{qualname_prefix}.{node.name}" if qualname_prefix else node.name,
        kind=kind,
        lineno=node.lineno,
        decorators=decorators,
        args=args,
        returns=returns,
        is_async=is_async,
        calls=_dedupe(cc.calls),
        raises=_dedupe(cc.raises),
        returns_const=_dedupe(cc.returns),
        branch_count=cc.branches,
        has_yield=cc.has_yield,
        has_star_args=bool(node.args.vararg or node.args.kwarg),
        side_fx=fx_vis.fx,
        body_size=sum(1 for _ in ast.walk(node)),
        doc_summary=_first_doc_line(ast.get_docstring(node)),
    )


def _analyze_class(node: ast.ClassDef) -> ClassFacts:
    bases = [ast.unparse(b) for b in node.bases]
    decorators = [_decorator_name(d) for d in node.decorator_list]
    metaclass = None
    for kw in node.keywords:
        if kw.arg == "metaclass":
            metaclass = ast.unparse(kw.value)

    class_vars: list[tuple[str, str]] = []
    nested: list[str] = []
    methods: list[FuncFacts] = []
    is_abstract = False

    for stmt in node.body:
        if isinstance(stmt, ast.Assign):
            for tgt in stmt.targets:
                if isinstance(tgt, ast.Name):
                    class_vars.append((tgt.id, _const_repr(stmt.value)))
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            val = _const_repr(stmt.value) if stmt.value else "<annotated>"
            class_vars.append((stmt.target.id, val))
        elif isinstance(stmt, ast.FunctionDef):
            kind = "method"
            for dec in stmt.decorator_list:
                dn = _decorator_name(dec)
                if dn == "classmethod":
                    kind = "classmethod"
                elif dn == "staticmethod":
                    kind = "staticmethod"
                elif dn == "property":
                    kind = "property"
                if dn in ("abstractmethod", "abc.abstractmethod"):
                    is_abstract = True
            methods.append(_analyze_function(stmt, node.name, kind))
        elif isinstance(stmt, ast.AsyncFunctionDef):
            methods.append(_analyze_function(stmt, node.name, "async-method"))
        elif isinstance(stmt, ast.ClassDef):
            nested.append(stmt.name)

    return ClassFacts(
        name=node.name,
        lineno=node.lineno,
        decorators=decorators,
        bases=bases,
        mro_hint=bases,
        class_vars=class_vars,
        methods=methods,
        nested_classes=nested,
        is_abstract=is_abstract,
        metaclass=metaclass,
        doc_summary=_first_doc_line(ast.get_docstring(node)),
    )


def analyze_module(path: Path, rel_path: str) -> ModuleFacts:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))

    imports: list[str] = []
    from_imports: list[tuple[str, list[str]]] = []
    constants: list[tuple[str, str]] = []
    functions: list[FuncFacts] = []
    classes: list[ClassFacts] = []
    dunder_all: list[str] | None = None
    has_main_guard = False
    module_doc = ast.get_docstring(tree)

    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.asname or alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = ("." * (node.level or 0)) + (node.module or "")
            names = [a.asname or a.name for a in node.names]
            from_imports.append((mod, names))
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name):
                    if tgt.id == "__all__":
                        if isinstance(node.value, (ast.List, ast.Tuple)):
                            dunder_all = [
                                e.value
                                for e in node.value.elts
                                if isinstance(e, ast.Constant)
                                and isinstance(e.value, str)
                            ]
                        constants.append(("__all__", _const_repr(node.value)))
                    else:
                        constants.append((tgt.id, _const_repr(node.value)))
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            val = _const_repr(node.value) if node.value else "<annotated>"
            constants.append((node.target.id, val))
        elif isinstance(node, ast.FunctionDef):
            functions.append(_analyze_function(node, "", "function"))
        elif isinstance(node, ast.AsyncFunctionDef):
            functions.append(_analyze_function(node, "", "async-function"))
        elif isinstance(node, ast.ClassDef):
            classes.append(_analyze_class(node))
        elif isinstance(node, ast.If):
            # detect __main__ guard
            test = node.test
            if (
                isinstance(test, ast.Compare)
                and isinstance(test.left, ast.Name)
                and test.left.id == "__main__"
            ):
                has_main_guard = True

    # build call graph: caller -> callees (module-level funcs + methods)
    call_graph: dict[str, list[str]] = {}
    for f in functions:
        call_graph[f.name] = f.calls
    for c in classes:
        for m in c.methods:
            call_graph[f"{c.name}.{m.name}"] = m.calls

    line_count = source.count("\n") + 1
    return ModuleFacts(
        path=path,
        rel_path=rel_path,
        imports=imports,
        from_imports=from_imports,
        constants=constants,
        dunder_all=dunder_all,
        functions=functions,
        classes=classes,
        call_graph=call_graph,
        has_main_guard=has_main_guard,
        module_doc=module_doc,
        line_count=line_count,
    )


# --------------------------------------------------------------------------- #
# Rendering                                                                   #
# --------------------------------------------------------------------------- #


def _fmt_list(items: Iterable[str], bullet: str = "-") -> str:
    items = list(items)
    if not items:
        return "_无_"
    return "\n".join(f"{bullet} {x}" for x in items)


def _kind_emoji(kind: str) -> str:
    return {
        "function": "ƒ",
        "async-function": "⏵ƒ",
        "method": "m",
        "async-method": "⏵m",
        "classmethod": "cls",
        "staticmethod": "st",
        "property": "prop",
    }.get(kind, kind)


def _side_fx_section(fx: SideEffects) -> str:
    if not fx.any():
        return ""
    lines: list[str] = []
    if fx.network:
        lines.append(f"  - 网络调用: {', '.join(fx.network)}")
    if fx.file_io:
        lines.append(f"  - 文件IO: {', '.join(fx.file_io)}")
    if fx.subprocess:
        lines.append(f"  - 子进程: {', '.join(fx.subprocess)}")
    if fx.dangerous:
        lines.append(f"  - 危险执行: {', '.join(fx.dangerous)}")
    if fx.env:
        lines.append(f"  - 环境变量: {', '.join(fx.env)}")
    if fx.reflection:
        lines.append(f"  - 反射: {', '.join(fx.reflection)}")
    return "\n".join(lines)


def _func_block(f: FuncFacts, indent: str = "") -> str:
    async_tag = "async " if f.is_async else ""
    sig = f"{async_tag}{f.name}({', '.join(f.args)})"
    if f.returns:
        sig += f" -> {f.returns}"
    dec = f"  @{', '.join(f.decorators)}  " if f.decorators else ""
    out: list[str] = []
    out.append(f"{indent}#### `{_kind_emoji(f.kind)}` `{sig}`  {dec}L{f.lineno}")
    # one-line doc info (if present) - explicitly marked as info-only
    if f.doc_summary:
        out.append(f"{indent}  - _文档首行_（仅供参考）: {f.doc_summary}")
    # key facts
    facts: list[str] = []
    facts.append(f"分支数 {f.branch_count}，函数体节点数 {f.body_size}")
    if f.has_yield:
        facts.append("生成器（yield）")
    if f.has_star_args:
        facts.append("可变参数（*args/**kwargs）")
    if f.raises:
        facts.append(f"raise: {', '.join(f.raises)}")
    if f.returns_const:
        facts.append(f"return: {', '.join(f.returns_const)}")
    out.append(f"{indent}  - {'；'.join(facts)}")
    if f.calls:
        # cap to 20
        calls = f.calls[:20]
        more = f"（+{len(f.calls) - 20}）" if len(f.calls) > 20 else ""
        out.append(f"{indent}  - 调用: {', '.join(calls)}{more}")
    fx = _side_fx_section(f.side_fx)
    if fx:
        out.append(fx)
    return "\n".join(out)


def _class_block(c: ClassFacts) -> str:
    out: list[str] = []
    header = f"### 类 `{c.name}`  L{c.lineno}"
    if c.decorators:
        header += f"  @{', '.join(c.decorators)}"
    out.append(header)
    if c.bases:
        out.append(f"- 继承: {', '.join(c.bases)}")
    if c.metaclass:
        out.append(f"- metaclass: {c.metaclass}")
    if c.is_abstract:
        out.append("- 含 abstractmethod（抽象基类）")
    if c.doc_summary:
        out.append(f"- _文档首行_: {c.doc_summary}")
    if c.class_vars:
        out.append("- 类/实例变量:")
        for name, val in c.class_vars[:25]:
            out.append(f"  - `{name}` = {val}")
        if len(c.class_vars) > 25:
            out.append(f"  - …(+{len(c.class_vars) - 25})")
    if c.nested_classes:
        out.append(f"- 嵌套类: {', '.join(c.nested_classes)}")
    if c.methods:
        out.append("- 方法:")
        # group by kind
        by_kind: dict[str, list[FuncFacts]] = defaultdict(list)
        for m in c.methods:
            by_kind[m.kind].append(m)
        order = ["property", "classmethod", "staticmethod", "method", "async-method"]
        for kind in order:
            for m in by_kind.get(kind, []):
                out.append(_func_block(m, indent="  "))
    return "\n".join(out)


def render_module(mf: ModuleFacts) -> str:
    out: list[str] = []
    title = f"`{mf.rel_path}`"
    out.append(f"# {title}")
    out.append("")
    out.append("> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  ")
    out.append(f"> 源文件: `{mf.rel_path}`  ·  行数: {mf.line_count}")
    out.append("")

    # module doc (info only)
    if mf.module_doc:
        first = _first_doc_line(mf.module_doc)
        out.append(f"**模块文档首行**（仅供参考）: {first}")
        out.append("")

    # overview facts
    out.append("## 模块概览")
    out.append(
        f"- 函数 {len(mf.functions)} 个，类 {len(mf.classes)} 个，模块级常量 {len(mf.constants)} 个"
    )
    if mf.dunder_all:
        out.append(f"- `__all__`: {', '.join(mf.dunder_all)}")
    if mf.has_main_guard:
        out.append("- 含 `if __name__ == '__main__'` 入口")
    out.append("")

    # imports (dependency map)
    if mf.imports or mf.from_imports:
        out.append("## 依赖（import）")
        if mf.imports:
            out.append("- 模块: " + ", ".join(mf.imports))
        for mod, names in mf.from_imports:
            out.append(f"- `{mod}` -> {', '.join(names)}")
        out.append("")

    # constants
    if mf.constants:
        out.append("## 模块级常量")
        for name, val in mf.constants[:40]:
            out.append(f"- `{name}` = {val}")
        if len(mf.constants) > 40:
            out.append(f"- …(+{len(mf.constants) - 40})")
        out.append("")

    # functions
    if mf.functions:
        out.append("## 函数")
        for f in mf.functions:
            out.append(_func_block(f))
            out.append("")

    # classes
    if mf.classes:
        out.append("## 类")
        for c in mf.classes:
            out.append(_class_block(c))
            out.append("")

    # call graph summary
    if mf.call_graph:
        out.append("## 文件内调用关系")
        # only show callers that call something defined in-file
        local_names: set[str] = set()
        for f in mf.functions:
            local_names.add(f.name)
        for c in mf.classes:
            for meth in c.methods:
                local_names.add(meth.name)
        edges: list[str] = []
        for caller, callees in mf.call_graph.items():
            local_callees = [c for c in callees if c in local_names]
            if local_callees:
                edges.append(f"- `{caller}` -> {', '.join(local_callees)}")
        if edges:
            out.extend(edges)
        else:
            out.append("_无文件内调用_")
        out.append("")

    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Driver                                                                      #
# --------------------------------------------------------------------------- #


def collect_files(
    roots: list[Path], include_tests: bool, include_skills: bool
) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        for p in root.rglob("*.py"):
            if not p.is_file():
                continue
            if "__pycache__" in p.parts:
                continue
            if not include_tests and ("tests" in p.parts or "test" in p.parts):
                continue
            if p.name == "__init__.py":
                # still document __init__ if it has real content; skip empties
                try:
                    if p.stat().st_size < 50:
                        continue
                except OSError:
                    continue
            rp = p.resolve()
            if rp in seen:
                continue
            seen.add(rp)
            files.append(p)
    # skills
    if include_skills:
        for p in Path("skills").rglob("*.py"):
            if "__pycache__" in p.parts:
                continue
            if p.name == "__init__.py" and p.stat().st_size < 50:
                continue
            files.append(p)
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--root",
        action="append",
        default=None,
        help="source root (repeatable). default: backend",
    )
    ap.add_argument("--out-root", default="docs/code", help="output root directory")
    ap.add_argument("--include-skills", action="store_true", help="also scan skills/")
    ap.add_argument("--include-tests", action="store_true", help="also scan test files")
    ap.add_argument(
        "--force", action="store_true", help="overwrite even if target is newer"
    )
    ap.add_argument(
        "--limit", type=int, default=None, help="process only first N files (debug)"
    )
    args = ap.parse_args()

    roots = [Path(r) for r in (args.root or ["backend"])]
    files = collect_files(roots, args.include_tests, args.include_skills)
    if args.limit:
        files = files[: args.limit]

    out_root = Path(args.out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    total = len(files)
    ok = 0
    skipped = 0
    failed: list[tuple[str, str]] = []
    index_rows: list[tuple[str, str, int, int]] = []  # rel, doc, funcs, classes

    for i, path in enumerate(files, 1):
        try:
            rel = path.resolve().relative_to(Path.cwd().resolve())
        except ValueError:
            rel = path
        rel_str = str(rel)
        # output path: <out-root>/<rel>.md
        out_path = out_root / (rel_str + ".md")
        if out_path.exists() and not args.force:
            # still re-generate to keep fresh; --force is for explicit overwrite
            pass
        if out_path.exists() and not args.force:
            skipped += 1
            continue
        try:
            mf = analyze_module(path, rel_str)
            content = render_module(mf)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(content, encoding="utf-8")
            ok += 1
            index_rows.append(
                (
                    rel_str,
                    str(out_path.relative_to(out_root)),
                    len(mf.functions),
                    len(mf.classes),
                )
            )
        except Exception as e:  # noqa: BLE001
            failed.append((rel_str, f"{type(e).__name__}: {e}"))

        if i % 50 == 0 or i == total:
            print(
                f"[{i}/{total}] ok={ok} skipped={skipped} failed={len(failed)}",
                file=sys.stderr,
            )

    # INDEX
    index_path = out_root / "INDEX.md"
    lines = [
        "# 代码说明文档索引",
        "",
        f"自动生成，共 {len(index_rows)} 个模块。每个 `.py` 对应一个 `.py.md`。",
        "",
    ]
    # group by top dir
    by_top: dict[str, list[tuple[str, str, int, int]]] = defaultdict(list)
    for row in index_rows:
        top = row[0].split(os.sep)[0] if os.sep in row[0] else row[0]
        by_top[top].append(row)
    for top in sorted(by_top):
        lines.append(f"## {top}/")
        lines.append("")
        lines.append("| 文件 | 函数 | 类 | 文档 |")
        lines.append("|------|------|----|------|")
        for rel, doc, fns, cls in sorted(by_top[top]):
            disp = rel.replace("\\", "/")
            doc_disp = doc.replace("\\", "/")
            lines.append(f"| `{disp}` | {fns} | {cls} | [{doc_disp}]({doc_disp}) |")
        lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")

    print(
        f"\n完成: 生成 {ok} 个文档，跳过 {skipped}，失败 {len(failed)}", file=sys.stderr
    )
    print(f"索引: {index_path}", file=sys.stderr)
    if failed:
        print("\n失败列表:", file=sys.stderr)
        for rel, err in failed[:20]:
            print(f"  {rel}: {err}", file=sys.stderr)
        if len(failed) > 20:
            print(f"  …(+{len(failed) - 20})", file=sys.stderr)
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())

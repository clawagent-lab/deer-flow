# `backend/packages/harness/deerflow/skills/review/resource_graph.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/review/resource_graph.py`  ·  行数: 116

**模块文档首行**（仅供参考）: Deterministic package resource graph checks.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: re
- `__future__` -> annotations
- `pathlib` -> PurePosixPath
- `typing` -> Any
- `deerflow.skills.package_paths` -> is_eval_fixture_path
- `deerflow.skills.review.models` -> make_finding, normalize_relative_path

## 模块级常量
- `_MARKDOWN_LINK_RE` = re.compile('!?\\[[^\\]]*]\\(([^)\\s]+)(?:\\s+\\"[^\\"]*\\...
- `_CODE_SPAN_RE` = re.compile('`([^`]+)`')
- `_PATH_TOKEN_RE` = re.compile('(?<![\\w./-])(?:references|scripts|templates|...
- `_RESOURCE_DIRS` = {'references', 'scripts', 'templates', 'assets', 'evals'}

## 函数
#### `ƒ` `build_resource_graph(snapshot: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]`  L18
  - 分支数 10，函数体节点数 516；return: (graph, findings)
  - 调用: str, get, sorted, set, items, is_eval_fixture_path, _extract_references, _resolve_reference, add, PurePosixPath, append, make_finding

#### `ƒ` `_extract_references(content: str) -> set[str]`  L89
  - 分支数 4，函数体节点数 114；return: refs
  - 调用: set, finditer, add, split, group, strip

#### `ƒ` `_resolve_reference(source_path: str, raw_ref: str) -> str | None`  L102
  - 分支数 4，函数体节点数 99；return: None, '__ESCAPES__', normalize_relative_path(candidate)
  - 调用: strip, startswith, match, PurePosixPath, as_posix, normalize_relative_path

## 文件内调用关系
- `build_resource_graph` -> _extract_references, _resolve_reference

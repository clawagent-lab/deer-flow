# `backend/packages/harness/deerflow/runtime/store/_sqlite_utils.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/store/_sqlite_utils.py`  ·  行数: 29

**模块文档首行**（仅供参考）: Shared SQLite connection utilities for store and checkpointer providers.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: pathlib
- `__future__` -> annotations
- `deerflow.config.paths` -> resolve_path

## 函数
#### `ƒ` `resolve_sqlite_conn_str(raw: str) -> str`  L10
  - _文档首行_（仅供参考）: Return a SQLite connection string ready for use with store/checkpointer backends.
  - 分支数 1，函数体节点数 35；return: raw, str(resolve_path(raw))
  - 调用: startswith, str, resolve_path

#### `ƒ` `ensure_sqlite_parent_dir(conn_str: str) -> None`  L22
  - _文档首行_（仅供参考）: Create parent directory for a SQLite filesystem path.
  - 分支数 1，函数体节点数 41
  - 调用: startswith, mkdir, Path
  - 文件IO: mkdir (L28)

## 文件内调用关系
_无文件内调用_

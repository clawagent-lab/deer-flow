# `backend/app/gateway/path_utils.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/path_utils.py`  ·  行数: 33

**模块文档首行**（仅供参考）: Shared path resolution for thread virtual paths (e.g. mnt/user-data/outputs/...).

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `pathlib` -> Path
- `fastapi` -> HTTPException
- `deerflow.config.paths` -> get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id

## 函数
#### `ƒ` `resolve_thread_virtual_path(thread_id: str, virtual_path: str, user_id: str | None) -> Path`  L11
  - _文档首行_（仅供参考）: Resolve a virtual path to the actual filesystem path under thread user-data.
  - 分支数 1，函数体节点数 69；raise: HTTPException(status_code=status, detail=str(e))；return: get_paths().resolve_virtual_path(thread_id, virtual_path, user_id=user_id or get_effective_user_id())
  - 调用: resolve_virtual_path, get_paths, get_effective_user_id, str, HTTPException

## 文件内调用关系
_无文件内调用_

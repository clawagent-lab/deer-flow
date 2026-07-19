# `backend/packages/harness/deerflow/sandbox/local/list_dir.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/local/list_dir.py`  ·  行数: 69

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `pathlib` -> Path
- `deerflow.sandbox.search` -> should_ignore_name

## 函数
#### `ƒ` `list_dir(path: str, max_depth: int) -> list[str]`  L6
  - _文档首行_（仅供参考）: List files and directories up to max_depth levels deep.
  - 分支数 11，函数体节点数 250；return: result, True, False, None, sorted(result)
  - 调用: resolve, Path, is_dir, relative_to, iterdir, should_ignore_name, is_symlink, _is_within_root, append, str, _traverse, sorted
  - 文件IO: iterdir (L38)

## 文件内调用关系
_无文件内调用_

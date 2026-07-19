# `backend/packages/harness/deerflow/skills/review/digest.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/review/digest.py`  ·  行数: 34

**模块文档首行**（仅供参考）: Canonical package digest for review snapshots.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: hashlib
- `__future__` -> annotations
- `typing` -> Any
- `deerflow.skills.review.models` -> normalize_relative_path

## 函数
#### `ƒ` `compute_package_digest(snapshot: dict[str, Any]) -> str`  L11
  - _文档首行_（仅供参考）: Return a host-path-independent SHA-256 digest for a package snapshot.
  - 分支数 2，函数体节点数 191；return: f'sha256:{h.hexdigest()}'
  - 调用: get, normalize_relative_path, str, int, join, encode, append, sha256, sorted, update, to_bytes, len, hexdigest

## 文件内调用关系
_无文件内调用_

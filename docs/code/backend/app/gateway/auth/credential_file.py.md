# `backend/app/gateway/auth/credential_file.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/credential_file.py`  ·  行数: 49

**模块文档首行**（仅供参考）: Write initial admin credentials to a restricted file instead of logs.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: os
- `__future__` -> annotations
- `pathlib` -> Path
- `deerflow.config.paths` -> get_paths

## 模块级常量
- `_CREDENTIAL_FILENAME` = 'admin_initial_credentials.txt'

## 函数
#### `ƒ` `write_initial_credentials(email: str, password: str, *, label: str) -> Path`  L21
  - _文档首行_（仅供参考）: Write the admin email + password to ``{base_dir}/admin_initial_credentials.txt``.
  - 分支数 1，函数体节点数 112；return: target.resolve()
  - 调用: get_paths, mkdir, open, fdopen, write, resolve
  - 文件IO: mkdir (L35), open (L44), write (L46)

## 文件内调用关系
_无文件内调用_

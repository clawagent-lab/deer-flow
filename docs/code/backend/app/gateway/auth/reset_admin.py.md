# `backend/app/gateway/auth/reset_admin.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/reset_admin.py`  ·  行数: 92

**模块文档首行**（仅供参考）: CLI tool to reset an admin password.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: argparse, asyncio, secrets, sys
- `__future__` -> annotations
- `sqlalchemy` -> select
- `app.gateway.auth.credential_file` -> write_initial_credentials
- `app.gateway.auth.password` -> hash_password
- `app.gateway.auth.repositories.sqlite` -> SQLiteUserRepository
- `deerflow.persistence.user.model` -> UserRow

## 函数
#### `⏵ƒ` `async _run(email: str | None) -> int`  L27
  - 分支数 7，函数体节点数 268；return: 1, 0
  - 调用: get_app_config, init_engine_from_config, get_session_factory, print, SQLiteUserRepository, get_user_by_email, sf, limit, where, select, scalar_one_or_none, execute, get_user_by_id, token_urlsafe, hash_password, update_user, write_initial_credentials, close_engine

#### `ƒ` `main() -> None`  L81
  - 分支数 0，函数体节点数 53
  - 调用: ArgumentParser, add_argument, parse_args, run, _run, exit
  - 子进程: run (L86)

## 文件内调用关系
- `main` -> _run

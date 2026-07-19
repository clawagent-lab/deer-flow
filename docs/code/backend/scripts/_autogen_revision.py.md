# `backend/scripts/_autogen_revision.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/scripts/_autogen_revision.py`  ·  行数: 79

**模块文档首行**（仅供参考）: Generate a new alembic revision against an ephemeral SQLite DB.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: os, sys, tempfile, deerflow.persistence.models
- `__future__` -> annotations
- `pathlib` -> Path
- `alembic` -> command
- `alembic.config` -> Config
- `deerflow.persistence.bootstrap` -> _escape_url_for_alembic

## 模块级常量
- `BACKEND_DIR` = Path(__file__).resolve().parents[1]
- `MIGRATIONS_DIR` = BACKEND_DIR / 'packages/harness/deerflow/persistence/migr...

## 函数
#### `ƒ` `_alembic_config(url: str) -> Config`  L48
  - 分支数 0，函数体节点数 40；return: cfg
  - 调用: Config, set_main_option, str, _escape_url_for_alembic

#### `ƒ` `_build_temp_db_at_head() -> str`  L57
  - 分支数 0，函数体节点数 58；return: url
  - 调用: mkdtemp, replace, join, upgrade, _alembic_config
  - 文件IO: replace (L59)

#### `ƒ` `main() -> None`  L65
  - 分支数 1，函数体节点数 91
  - 调用: len, strip, print, exit, _build_temp_db_at_head, revision, _alembic_config

## 文件内调用关系
- `_build_temp_db_at_head` -> _alembic_config
- `main` -> _build_temp_db_at_head, _alembic_config

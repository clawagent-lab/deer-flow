# `backend/packages/harness/deerflow/persistence/migrations/env.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/migrations/env.py`  ·  行数: 104

**模块文档首行**（仅供参考）: Alembic environment for DeerFlow application tables.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 3 个
- `__all__`: LANGGRAPH_OWNED_TABLES, include_object

## 依赖（import）
- 模块: asyncio, logging
- `__future__` -> annotations
- `logging.config` -> fileConfig
- `alembic` -> context
- `sqlalchemy.ext.asyncio` -> create_async_engine
- `deerflow.persistence.base` -> Base
- `deerflow.persistence.migrations._env_filters` -> LANGGRAPH_OWNED_TABLES, include_object

## 模块级常量
- `__all__` = ['LANGGRAPH_OWNED_TABLES', 'include_object']
- `config` = context.config
- `target_metadata` = Base.metadata

## 函数
#### `ƒ` `run_migrations_offline() -> None`  L50
  - 分支数 1，函数体节点数 44
  - 调用: get_main_option, configure, begin_transaction, run_migrations

#### `ƒ` `do_run_migrations(connection)`  L63
  - 分支数 1，函数体节点数 33
  - 调用: configure, begin_transaction, run_migrations

#### `⏵ƒ` `async run_migrations_online() -> None`  L74
  - 分支数 3，函数体节点数 89
  - 调用: create_async_engine, get_main_option, startswith, cursor, execute, close, listens_for, connect, run_sync, dispose

## 文件内调用关系
_无文件内调用_

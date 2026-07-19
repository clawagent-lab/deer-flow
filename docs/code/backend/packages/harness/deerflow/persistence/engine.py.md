# `backend/packages/harness/deerflow/persistence/engine.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/engine.py`  ·  行数: 206

**模块文档首行**（仅供参考）: Async SQLAlchemy engine lifecycle management.

## 模块概览
- 函数 7 个，类 0 个，模块级常量 3 个

## 依赖（import）
- 模块: asyncio, json, logging
- `__future__` -> annotations
- `sqlalchemy.ext.asyncio` -> AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_engine` = None
- `_session_factory` = None

## 函数
#### `ƒ` `_json_serializer(obj: object) -> str`  L20
  - _文档首行_（仅供参考）: JSON serializer with ensure_ascii=False for Chinese character support.
  - 分支数 0，函数体节点数 19；return: json.dumps(obj, ensure_ascii=False)
  - 调用: dumps

#### `⏵ƒ` `async _auto_create_postgres_db(url: str) -> None`  L31
  - _文档首行_（仅供参考）: Connect to the ``postgres`` maintenance DB and CREATE DATABASE.
  - 分支数 3，函数体节点数 99；raise: ValueError('Cannot auto-create database: no database name in URL')
  - 调用: make_url, ValueError, set, create_async_engine, connect, execute, text, info, dispose

#### `⏵ƒ` `async init_engine(backend: str, *, url: str, echo: bool, pool_size: int, sqlite_dir: str) -> None`  L58
  - _文档首行_（仅供参考）: Create the async engine and session factory, then auto-create tables.
  - 分支数 8，函数体节点数 295；raise: ImportError("database.backend is set to 'postgres' but asyncpg is not installed.\nInstall it with:\n    cd backend && uv sync --all-packages --extra postgres\nOn the next `make dev` the postgres extra is auto-detected from\nconfig.yaml (database.backend: postgres) and reinstalled, so it\nwill not be wiped again. Set UV_EXTRAS=postgres in .env to opt in\nexplicitly. Or switch to backend: sqlite in config.yaml for\nsingle-node deployment."), ValueError(f'Unknown persistence backend: {backend!r}'), bare raise；return: None
  - 调用: info, ImportError, to_thread, create_async_engine, cursor, execute, close, listens_for, ValueError, async_sessionmaker, bootstrap_schema, str, _auto_create_postgres_db, dispose

#### `⏵ƒ` `async init_engine_from_config(config) -> None`  L174
  - _文档首行_（仅供参考）: Convenience: init engine from a DatabaseConfig object.
  - 分支数 1，函数体节点数 60；return: None
  - 调用: init_engine

#### `ƒ` `get_session_factory() -> async_sessionmaker[AsyncSession] | None`  L188
  - _文档首行_（仅供参考）: Return the async session factory, or None if backend=memory.
  - 分支数 0，函数体节点数 16；return: _session_factory

#### `ƒ` `get_engine() -> AsyncEngine | None`  L193
  - _文档首行_（仅供参考）: Return the async engine, or None if not initialized.
  - 分支数 0，函数体节点数 12；return: _engine

#### `⏵ƒ` `async close_engine() -> None`  L198
  - _文档首行_（仅供参考）: Dispose the engine, release all connections.
  - 分支数 1，函数体节点数 34
  - 调用: dispose, info

## 文件内调用关系
- `init_engine` -> _auto_create_postgres_db
- `init_engine_from_config` -> init_engine

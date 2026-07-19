# `backend/packages/harness/deerflow/runtime/checkpointer/async_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/checkpointer/async_provider.py`  ·  行数: 203

**模块文档首行**（仅供参考）: Async checkpointer factory.

## 模块概览
- 函数 7 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, contextlib, logging
- `__future__` -> annotations
- `collections.abc` -> AsyncIterator
- `langgraph.types` -> Checkpointer
- `deerflow.config.app_config` -> AppConfig, get_app_config
- `deerflow.runtime.checkpointer.provider` -> POSTGRES_CONN_REQUIRED, POSTGRES_INSTALL, SQLITE_INSTALL
- `deerflow.runtime.store._sqlite_utils` -> ensure_sqlite_parent_dir, resolve_sqlite_conn_str

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_prepare_sqlite_checkpointer_path(raw: str) -> str`  L38
  - 分支数 0，函数体节点数 24；return: conn_str
  - 调用: resolve_sqlite_conn_str, ensure_sqlite_parent_dir

#### `ƒ` `_prepare_database_sqlite_checkpointer_path(db_config) -> str`  L44
  - 分支数 0，函数体节点数 21；return: conn_str
  - 调用: ensure_sqlite_parent_dir

#### `ƒ` `_build_postgres_pool(conn_string: str)`  L50
  - _文档首行_（仅供参考）: Build an AsyncConnectionPool with TCP keepalive and connection checking.
  - 分支数 0，函数体节点数 39；return: AsyncConnectionPool(conn_string, kwargs={'autocommit': True, 'prepare_threshold': 0, 'row_factory': dict_row, 'keepalives': 1, 'keepalives_idle': 60, 'keepalives_interval': 10, 'keepalives_count': 6}, check=AsyncConnectionPool.check_connection)
  - 调用: AsyncConnectionPool

#### `ƒ` `_ensure_postgres_imports()`  L70
  - _文档首行_（仅供参考）: Import and return (AsyncPostgresSaver, AsyncConnectionPool), raising ImportError on failure.
  - 分支数 2，函数体节点数 39；raise: ImportError(POSTGRES_INSTALL)；return: (AsyncPostgresSaver, AsyncConnectionPool)
  - 调用: ImportError

#### `⏵ƒ` `async _async_checkpointer(config) -> AsyncIterator[Checkpointer]`    @contextlib.asynccontextmanager  L91
  - _文档首行_（仅供参考）: Async context manager that constructs and tears down a checkpointer.
  - 分支数 7，函数体节点数 171；生成器（yield）；raise: ImportError(SQLITE_INSTALL), ValueError(POSTGRES_CONN_REQUIRED), ValueError(f'Unknown checkpointer type: {config.type!r}')；return: None
  - 调用: ImportError, to_thread, from_conn_string, setup, ValueError, _ensure_postgres_imports, _build_postgres_pool, AsyncPostgresSaver

#### `⏵ƒ` `async _async_checkpointer_from_database(db_config) -> AsyncIterator[Checkpointer]`    @contextlib.asynccontextmanager  L132
  - _文档首行_（仅供参考）: Async context manager that constructs a checkpointer from unified DatabaseConfig.
  - 分支数 7，函数体节点数 165；生成器（yield）；raise: ImportError(SQLITE_INSTALL), ValueError('database.postgres_url is required for the postgres backend'), ValueError(f'Unknown database backend: {db_config.backend!r}')；return: None
  - 调用: ImportError, to_thread, from_conn_string, setup, ValueError, _ensure_postgres_imports, _build_postgres_pool, AsyncPostgresSaver

#### `⏵ƒ` `async make_checkpointer(app_config: AppConfig | None) -> AsyncIterator[Checkpointer]`    @contextlib.asynccontextmanager  L168
  - _文档首行_（仅供参考）: Async context manager that yields a checkpointer for the caller's lifetime.
  - 分支数 5，函数体节点数 103；生成器（yield）；return: None
  - 调用: get_app_config, _async_checkpointer, getattr, _async_checkpointer_from_database
  - 反射: getattr (L193)

## 文件内调用关系
- `_async_checkpointer` -> _ensure_postgres_imports, _build_postgres_pool
- `_async_checkpointer_from_database` -> _ensure_postgres_imports, _build_postgres_pool
- `make_checkpointer` -> _async_checkpointer, _async_checkpointer_from_database

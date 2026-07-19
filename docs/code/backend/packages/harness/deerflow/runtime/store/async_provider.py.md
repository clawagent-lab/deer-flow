# `backend/packages/harness/deerflow/runtime/store/async_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/store/async_provider.py`  ·  行数: 116

**模块文档首行**（仅供参考）: Async Store factory — backend mirrors runtime persistence configuration.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, contextlib, logging
- `__future__` -> annotations
- `collections.abc` -> AsyncIterator
- `langgraph.store.base` -> BaseStore
- `deerflow.config.app_config` -> AppConfig, get_app_config
- `deerflow.runtime.store.provider` -> POSTGRES_CONN_REQUIRED, POSTGRES_STORE_INSTALL, SQLITE_STORE_INSTALL, _resolve_store_config, ensure_sqlite_parent_dir, resolve_sqlite_conn_str

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `⏵ƒ` `async _async_store(config) -> AsyncIterator[BaseStore]`    @contextlib.asynccontextmanager  L45
  - _文档首行_（仅供参考）: Async context manager that constructs and tears down a Store.
  - 分支数 8，函数体节点数 194；生成器（yield）；raise: ImportError(SQLITE_STORE_INSTALL), ImportError(POSTGRES_STORE_INSTALL), ValueError(POSTGRES_CONN_REQUIRED), ValueError(f'Unknown store backend type: {config.type!r}')；return: None
  - 调用: info, ImportError, resolve_sqlite_conn_str, to_thread, from_conn_string, setup, ValueError

#### `⏵ƒ` `async make_store(app_config: AppConfig | None) -> AsyncIterator[BaseStore]`    @contextlib.asynccontextmanager  L97
  - _文档首行_（仅供参考）: Yield a Store selected from legacy or unified persistence config.
  - 分支数 2，函数体节点数 54；生成器（yield）
  - 调用: get_app_config, _resolve_store_config, _async_store

## 文件内调用关系
- `make_store` -> _async_store

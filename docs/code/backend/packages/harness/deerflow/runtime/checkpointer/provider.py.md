# `backend/packages/harness/deerflow/runtime/checkpointer/provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/checkpointer/provider.py`  ·  行数: 225

**模块文档首行**（仅供参考）: Sync checkpointer factory.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 7 个

## 依赖（import）
- 模块: contextlib, logging, threading
- `__future__` -> annotations
- `collections.abc` -> Iterator
- `langgraph.types` -> Checkpointer
- `deerflow.config.app_config` -> AppConfig, get_app_config
- `deerflow.config.checkpointer_config` -> CheckpointerConfig, ensure_config_loaded, get_checkpointer_config
- `deerflow.runtime.store._sqlite_utils` -> ensure_sqlite_parent_dir, resolve_sqlite_conn_str

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `SQLITE_INSTALL` = 'langgraph-checkpoint-sqlite is required for the SQLite c...
- `POSTGRES_INSTALL` = "langgraph-checkpoint-postgres is required for the Postgr...
- `POSTGRES_CONN_REQUIRED` = 'checkpointer.connection_string is required for the postg...
- `_checkpointer` = None
- `_checkpointer_ctx` = None
- `_checkpointer_lock` = threading.Lock()

## 函数
#### `ƒ` `_resolve_checkpointer_config(app_config: AppConfig) -> CheckpointerConfig`  L51
  - _文档首行_（仅供参考）: Resolve the checkpointer backend from legacy or unified application config.
  - 分支数 5，函数体节点数 111；raise: ValueError('database.postgres_url is required for the postgres backend'), ValueError(f'Unknown database backend: {database.backend!r}')；return: app_config.checkpointer, CheckpointerConfig(type='memory'), CheckpointerConfig(type='sqlite', connection_string=database.checkpointer_sqlite_path), CheckpointerConfig(type='postgres', connection_string=database.postgres_url)
  - 调用: CheckpointerConfig, ValueError

#### `ƒ` `_get_checkpointer_config() -> CheckpointerConfig`  L75
  - _文档首行_（仅供参考）: Load checkpointer config without holding the provider singleton lock.
  - 分支数 2，函数体节点数 47；return: legacy_config, CheckpointerConfig(type='memory'), _resolve_checkpointer_config(app_config)
  - 调用: ensure_config_loaded, get_checkpointer_config, get_app_config, CheckpointerConfig, _resolve_checkpointer_config

#### `ƒ` `_sync_checkpointer_cm(config: CheckpointerConfig) -> Iterator[Checkpointer]`    @contextlib.contextmanager  L96
  - _文档首行_（仅供参考）: Context manager that creates and tears down a sync checkpointer.
  - 分支数 8，函数体节点数 189；生成器（yield）；raise: ImportError(SQLITE_INSTALL), ImportError(POSTGRES_INSTALL), ValueError(POSTGRES_CONN_REQUIRED), ValueError(f'Unknown checkpointer type: {config.type!r}')；return: None
  - 调用: info, ImportError, resolve_sqlite_conn_str, ensure_sqlite_parent_dir, from_conn_string, setup, ValueError

#### `ƒ` `get_checkpointer() -> Checkpointer`  L152
  - _文档首行_（仅供参考）: Return the global sync checkpointer singleton, creating it on first call.
  - 分支数 3，函数体节点数 64；return: _checkpointer
  - 调用: _get_checkpointer_config, _sync_checkpointer_cm, __enter__

#### `ƒ` `reset_checkpointer() -> None`  L184
  - _文档首行_（仅供参考）: Reset the sync singleton, forcing recreation on the next call.
  - 分支数 3，函数体节点数 46
  - 调用: __exit__, warning

#### `ƒ` `checkpointer_context() -> Iterator[Checkpointer]`    @contextlib.contextmanager  L207
  - _文档首行_（仅供参考）: Sync context manager that yields a checkpointer and cleans up on exit.
  - 分支数 1，函数体节点数 36；生成器（yield）
  - 调用: _resolve_checkpointer_config, get_app_config, _sync_checkpointer_cm

## 文件内调用关系
- `_get_checkpointer_config` -> _resolve_checkpointer_config
- `get_checkpointer` -> _get_checkpointer_config, _sync_checkpointer_cm
- `checkpointer_context` -> _resolve_checkpointer_config, _sync_checkpointer_cm

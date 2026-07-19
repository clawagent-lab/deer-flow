# `backend/packages/harness/deerflow/persistence/bootstrap.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/bootstrap.py`  ·  行数: 527

**模块文档首行**（仅供参考）: Hybrid schema bootstrap for DeerFlow's application tables.

## 模块概览
- 函数 15 个，类 0 个，模块级常量 8 个

## 依赖（import）
- 模块: asyncio, logging, weakref
- `__future__` -> annotations
- `contextlib` -> asynccontextmanager
- `pathlib` -> Path
- `typing` -> Any
- `alembic` -> alembic_command
- `alembic.config` -> AlembicConfig
- `alembic.script` -> ScriptDirectory
- `sqlalchemy` -> sa_inspect
- `sqlalchemy` -> text
- `sqlalchemy.ext.asyncio` -> AsyncEngine

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_MIGRATIONS_DIR` = Path(__file__).resolve().parent / 'migrations'
- `_HEAD_REVISION` = None
- `_BASELINE_REVISION` = '0001_baseline'
- `_PG_LOCK_KEY` = 1003760593446778498
- `_BASELINE_TABLE_NAMES` = frozenset({'channel_connections', 'channel_conversations'...
- `_BASELINE_INDEX_NAMES` = frozenset({'idx_channel_connections_event_lookup', 'ix_ch...
- `_SQLITE_LOCKS` = weakref.WeakKeyDictionary()

## 函数
#### `ƒ` `_get_sqlite_local_lock(engine: AsyncEngine) -> asyncio.Lock`  L199
  - 分支数 1，函数体节点数 45；return: lock
  - 调用: get, Lock

#### `ƒ` `_escape_url_for_alembic(url: str) -> str`  L207
  - _文档首行_（仅供参考）: Double literal ``%`` so ``ConfigParser`` interpolation leaves the URL intact.
  - 分支数 0，函数体节点数 17；return: url.replace('%', '%%')
  - 调用: replace
  - 文件IO: replace (L217)

#### `ƒ` `_alembic_safe_url(engine: AsyncEngine) -> str`  L220
  - _文档首行_（仅供参考）: Render *engine*'s URL in a form alembic ``set_main_option`` accepts.
  - 分支数 0，函数体节点数 27；return: _escape_url_for_alembic(rendered)
  - 调用: render_as_string, _escape_url_for_alembic

#### `ƒ` `_get_alembic_config(engine: AsyncEngine) -> AlembicConfig`  L237
  - _文档首行_（仅供参考）: Build an in-process alembic config pointing at our migrations dir.
  - 分支数 0，函数体节点数 42；return: cfg
  - 调用: AlembicConfig, set_main_option, str, _alembic_safe_url

#### `ƒ` `_get_head_revision() -> str`  L250
  - _文档首行_（仅供参考）: Return the head revision id from ``versions/``, cached per process.
  - 分支数 2，函数体节点数 68；raise: RuntimeError('alembic has no head revision -- versions/ directory is empty')；return: _HEAD_REVISION
  - 调用: AlembicConfig, set_main_option, str, from_config, get_current_head, RuntimeError

#### `ƒ` `_reflect_state(sync_conn: Any) -> dict[str, bool]`  L264
  - _文档首行_（仅供参考）: Inspect *sync_conn* (sync connection inside ``run_sync``) and return:
  - 分支数 1，函数体节点数 81；return: {'has_alembic_version': 'alembic_version' in reflected, 'has_deerflow_tables': bool(reflected & metadata_tables)}
  - 调用: debug, sa_inspect, set, get_table_names, bool

#### `ƒ` `_decide_state(state: dict[str, bool]) -> str`  L291
  - _文档首行_（仅供参考）: Map a reflected DB state to one of three branch labels.
  - 分支数 2，函数体节点数 37；return: 'versioned', 'empty', 'legacy'

#### `ƒ` `_run_create_all_sync(sync_conn: Any) -> None`  L309
  - _文档首行_（仅供参考）: Create all DeerFlow-owned tables on *sync_conn*.
  - 分支数 1，函数体节点数 33
  - 调用: debug, create_all

#### `ƒ` `_run_baseline_create_all_sync(sync_conn: Any) -> None`  L322
  - _文档首行_（仅供参考）: Create only the baseline tables on *sync_conn* (idempotent via checkfirst).
  - 分支数 5，函数体节点数 118
  - 调用: debug, create_all, create, warning

#### `ƒ` `_stamp(cfg: AlembicConfig, revision: str) -> None`  L377
  - _文档首行_（仅供参考）: Synchronous alembic stamp; callers must wrap in ``asyncio.to_thread``.
  - 分支数 0，函数体节点数 21
  - 调用: stamp

#### `ƒ` `_upgrade(cfg: AlembicConfig, revision: str) -> None`  L382
  - _文档首行_（仅供参考）: Synchronous alembic upgrade; callers must wrap in ``asyncio.to_thread``.
  - 分支数 0，函数体节点数 21
  - 调用: upgrade

#### `⏵ƒ` `async _postgres_lock(engine: AsyncEngine)`    @asynccontextmanager  L393
  - _文档首行_（仅供参考）: Hold a Postgres session-level advisory lock for the body of the block.
  - 分支数 3，函数体节点数 84；生成器（yield）
  - 调用: connect, execute, text, info, warning

#### `⏵ƒ` `async _sqlite_lock(engine: AsyncEngine)`    @asynccontextmanager  L435
  - _文档首行_（仅供参考）: Serialise SQLite bootstrap inside one process; cross-process is
  - 分支数 1，函数体节点数 25；生成器（yield）
  - 调用: _get_sqlite_local_lock, info

#### `ƒ` `_bootstrap_lock(engine: AsyncEngine, *, backend: str)`  L460
  - 分支数 2，函数体节点数 41；raise: ValueError(f'bootstrap: unsupported backend {backend!r}')；return: _postgres_lock(engine), _sqlite_lock(engine)
  - 调用: _postgres_lock, _sqlite_lock, ValueError

#### `⏵ƒ` `async bootstrap_schema(engine: AsyncEngine, *, backend: str) -> None`  L473
  - _文档首行_（仅供参考）: Bring the DB schema to head.
  - 分支数 7，函数体节点数 214；raise: RuntimeError(f'bootstrap: unhandled decision {decision!r}')
  - 调用: _get_head_revision, _get_alembic_config, _bootstrap_lock, connect, run_sync, _decide_state, info, begin, to_thread, RuntimeError

## 文件内调用关系
- `_alembic_safe_url` -> _escape_url_for_alembic
- `_get_alembic_config` -> _alembic_safe_url
- `_sqlite_lock` -> _get_sqlite_local_lock
- `_bootstrap_lock` -> _postgres_lock, _sqlite_lock
- `bootstrap_schema` -> _get_head_revision, _get_alembic_config, _bootstrap_lock, _decide_state

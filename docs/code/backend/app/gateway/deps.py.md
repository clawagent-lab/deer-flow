# `backend/app/gateway/deps.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/deps.py`  ·  行数: 551

**模块文档首行**（仅供参考）: Centralized accessors for singleton objects stored on ``app.state``.

## 模块概览
- 函数 19 个，类 0 个，模块级常量 11 个

## 依赖（import）
- 模块: asyncio, logging, os
- `__future__` -> annotations
- `collections.abc` -> AsyncGenerator, Callable
- `contextlib` -> AsyncExitStack, asynccontextmanager
- `typing` -> TYPE_CHECKING, TypeVar, cast
- `fastapi` -> FastAPI, HTTPException, Request
- `langgraph.types` -> Checkpointer
- `deerflow.config.app_config` -> AppConfig, get_app_config
- `deerflow.persistence.feedback` -> FeedbackRepository
- `deerflow.runtime` -> RunContext, RunManager, StreamBridge
- `deerflow.runtime.events.store.base` -> RunEventStore
- `deerflow.runtime.runs.store.base` -> RunStore

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_RUN_DRAIN_TIMEOUT_SECONDS` = 5.0
- `T` = TypeVar('T')
- `get_stream_bridge` = _require('stream_bridge', 'Stream bridge')
- `get_run_manager` = _require('run_manager', 'Run manager')
- `get_checkpointer` = _require('checkpointer', 'Checkpointer')
- `get_run_event_store` = _require('run_event_store', 'Run event store')
- `get_feedback_repo` = _require('feedback_repo', 'Feedback')
- `get_run_store` = _require('run_store', 'Run store')
- `_cached_local_provider` = None
- `_cached_repo` = None

## 函数
#### `ƒ` `_enforce_postgres_for_multi_worker(config: AppConfig) -> None`  L49
  - _文档首行_（仅供参考）: Refuse to start when GATEWAY_WORKERS > 1 and safety preconditions are not met.
  - 分支数 4，函数体节点数 108；raise: SystemExit(f"GATEWAY_WORKERS={workers} requires database.backend='postgres', but database.backend is '{backend}'. SQLite cannot support concurrent multi-process access. Set GATEWAY_WORKERS=1 or switch to Postgres."), SystemExit(f"GATEWAY_WORKERS={workers} requires run_ownership.heartbeat_enabled=true. Without heartbeat, every run has a NULL lease, so reconciliation treats all inflight runs as orphans — Worker B would kill Worker A's live runs on every rolling update or scale-up. Set run_ownership.heartbeat_enabled=true in config.yaml.")；return: None
  - 调用: int, get, getattr, SystemExit
  - 反射: getattr (L73), getattr (L77)

#### `⏵ƒ` `async _drain_inflight_runs(run_manager: RunManager) -> None`  L88
  - _文档首行_（仅供参考）: Drain in-flight runs before the checkpointer is torn down (issue #3373).
  - 分支数 2，函数体节点数 70；raise: bare raise
  - 调用: create_task, shutdown, shield, exception

#### `⏵ƒ` `async _publish_recovered_run_stream_end(bridge: StreamBridge, recovered_runs: list[RunRecord], *, cleanup_delay: float) -> None`  L114
  - _文档首行_（仅供参考）: Terminate retained streams for runs recovered as orphaned at startup.
  - 分支数 5，函数体节点数 150
  - 调用: getattr, stream_exists, debug, publish_end, warning, create_task, cleanup, add_done_callback, _log_recovered_stream_cleanup_result
  - 反射: getattr (L122)

#### `ƒ` `_log_recovered_stream_cleanup_result(task: asyncio.Task[None], run_id: str) -> None`  L143
  - 分支数 2，函数体节点数 42；return: None
  - 调用: cancelled, result, warning

#### `⏵ƒ` `async _mark_latest_recovered_threads_error(run_manager: RunManager, thread_store: ThreadMetaStore, recovered_runs: list[RunRecord]) -> None`  L162
  - _文档首行_（仅供参考）: Mark thread status as error only when its newest run was recovered.
  - 分支数 5，函数体节点数 150
  - 调用: add, setdefault, set, items, list_by_thread, warning, update_status

#### `ƒ` `get_config() -> AppConfig`  L186
  - _文档首行_（仅供参考）: Return the freshest ``AppConfig`` for the current request.
  - 分支数 1，函数体节点数 31；raise: HTTPException(status_code=503, detail='Configuration not available')；return: get_app_config()
  - 调用: get_app_config, exception, HTTPException

#### `⏵ƒ` `async langgraph_runtime(app: FastAPI, startup_config: AppConfig) -> AsyncGenerator[None, None]`    @asynccontextmanager  L223
  - _文档首行_（仅供参考）: Bootstrap and tear down all LangGraph runtime singletons.
  - 分支数 5，函数体节点数 427；生成器（yield）
  - 调用: _enforce_postgres_for_multi_worker, AsyncExitStack, enter_async_context, make_stream_bridge, init_engine_from_config, make_checkpointer, make_store, get_session_factory, RunRepository, FeedbackRepository, MemoryRunStore, make_thread_store, ScheduledTaskRepository, ScheduledTaskRunRepository, getattr, make_run_event_store, RunManager, reconcile_orphaned_inflight_runs, now_iso, _publish_recovered_run_stream_end（+4）
  - 反射: getattr (L303), getattr (L308), getattr (L324), getattr (L325), getattr (L340)

#### `ƒ` `_require(attr: str, label: str) -> Callable[[Request], T]`  L351
  - _文档首行_（仅供参考）: Create a FastAPI dependency that returns ``app.state.<attr>`` or 503.
  - 分支数 1，函数体节点数 87；raise: HTTPException(status_code=503, detail=f'{label} not available')；return: cast(T, val), dep
  - 调用: getattr, HTTPException, cast
  - 反射: getattr (L355)

#### `ƒ` `get_store(request: Request)`  L372
  - _文档首行_（仅供参考）: Return the global store (may be ``None`` if not configured).
  - 分支数 0，函数体节点数 19；return: getattr(request.app.state, 'store', None)
  - 调用: getattr
  - 反射: getattr (L374)

#### `ƒ` `get_thread_store(request: Request) -> ThreadMetaStore`  L377
  - _文档首行_（仅供参考）: Return the thread metadata store (SQL or memory-backed).
  - 分支数 1，函数体节点数 40；raise: HTTPException(status_code=503, detail='Thread metadata store not available')；return: val
  - 调用: getattr, HTTPException
  - 反射: getattr (L379)

#### `ƒ` `get_scheduled_task_repo(request: Request)`  L385
  - 分支数 1，函数体节点数 36；raise: HTTPException(status_code=503, detail='Scheduled task repo not available')；return: val
  - 调用: getattr, HTTPException
  - 反射: getattr (L386)

#### `ƒ` `get_scheduled_task_run_repo(request: Request)`  L392
  - 分支数 1，函数体节点数 36；raise: HTTPException(status_code=503, detail='Scheduled task run repo not available')；return: val
  - 调用: getattr, HTTPException
  - 反射: getattr (L393)

#### `ƒ` `get_scheduled_task_service(request: Request)`  L399
  - 分支数 1，函数体节点数 36；raise: HTTPException(status_code=503, detail='Scheduled task service not available')；return: val
  - 调用: getattr, HTTPException
  - 反射: getattr (L400)

#### `ƒ` `get_run_context(request: Request) -> RunContext`  L406
  - _文档首行_（仅供参考）: Build a :class:`RunContext` from ``app.state`` singletons.
  - 分支数 0，函数体节点数 83；return: RunContext(checkpointer=get_checkpointer(request), store=get_store(request), event_store=get_run_event_store(request), run_events_config=getattr(request.app.state, 'run_events_config', None), thread_store=get_thread_store(request), app_config=get_config(), on_run_completed=getattr(request.app.state, 'scheduled_task_service', None).handle_run_completion if getattr(request.app.state, 'scheduled_task_service', None) is not None else None)
  - 调用: RunContext, get_checkpointer, get_store, get_run_event_store, getattr, get_thread_store, get_config
  - 反射: getattr (L420), getattr (L423), getattr (L423)

#### `ƒ` `get_local_provider() -> LocalAuthProvider`  L436
  - _文档首行_（仅供参考）: Get or create the cached LocalAuthProvider singleton.
  - 分支数 3，函数体节点数 62；raise: RuntimeError('get_local_provider() called before init_engine_from_config(); cannot access users table')；return: _cached_local_provider
  - 调用: get_session_factory, RuntimeError, SQLiteUserRepository, LocalAuthProvider

#### `⏵ƒ` `async get_current_user_from_request(request: Request)`  L458
  - _文档首行_（仅供参考）: Get the current authenticated user from the request cookie.
  - 分支数 5，函数体节点数 223；raise: HTTPException(status_code=401, detail=AuthErrorResponse(code=AuthErrorCode.NOT_AUTHENTICATED, message='Not authenticated').model_dump()), HTTPException(status_code=401, detail=AuthErrorResponse(code=token_error_to_code(payload), message=f'Token error: {payload.value}').model_dump()), HTTPException(status_code=401, detail=AuthErrorResponse(code=AuthErrorCode.USER_NOT_FOUND, message='User not found').model_dump()), HTTPException(status_code=401, detail=AuthErrorResponse(code=AuthErrorCode.TOKEN_INVALID, message='Token revoked (password changed)').model_dump())；return: state_user, user
  - 调用: getattr, get, HTTPException, model_dump, AuthErrorResponse, decode_token, isinstance, token_error_to_code, get_local_provider, get_user
  - 反射: getattr (L463), getattr (L464), getattr (L467)

#### `⏵ƒ` `async require_admin_user(request: Request, *, detail: str) -> None`  L509
  - _文档首行_（仅供参考）: Require the authenticated caller to be an admin user.
  - 分支数 2，函数体节点数 58；raise: HTTPException(status_code=403, detail=detail)
  - 调用: getattr, get_current_user_from_request, HTTPException
  - 反射: getattr (L523), getattr (L527)

#### `⏵ƒ` `async get_optional_user_from_request(request: Request)`  L531
  - _文档首行_（仅供参考）: Get optional authenticated user from request.
  - 分支数 1，函数体节点数 20；return: await get_current_user_from_request(request), None
  - 调用: get_current_user_from_request

#### `⏵ƒ` `async get_current_user(request: Request) -> str | None`  L542
  - _文档首行_（仅供参考）: Extract user_id from request cookie, or None if not authenticated.
  - 分支数 0，函数体节点数 33；return: str(user.id) if user else None
  - 调用: get_optional_user_from_request, str

## 文件内调用关系
- `_publish_recovered_run_stream_end` -> _log_recovered_stream_cleanup_result
- `langgraph_runtime` -> _enforce_postgres_for_multi_worker, _publish_recovered_run_stream_end, _mark_latest_recovered_threads_error, _drain_inflight_runs
- `get_run_context` -> get_store, get_thread_store, get_config
- `get_current_user_from_request` -> get_local_provider
- `require_admin_user` -> get_current_user_from_request
- `get_optional_user_from_request` -> get_current_user_from_request
- `get_current_user` -> get_optional_user_from_request

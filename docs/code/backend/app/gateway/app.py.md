# `backend/app/gateway/app.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/app.py`  ·  行数: 571

## 模块概览
- 函数 6 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: asyncio, logging
- `collections.abc` -> AsyncGenerator
- `contextlib` -> asynccontextmanager
- `fastapi` -> FastAPI
- `fastapi.middleware.cors` -> CORSMiddleware
- `app.gateway.auth_disabled` -> warn_if_auth_disabled_enabled
- `app.gateway.auth_middleware` -> AuthMiddleware
- `app.gateway.config` -> get_gateway_config
- `app.gateway.csrf_middleware` -> CSRFMiddleware, get_configured_cors_origins
- `app.gateway.deps` -> langgraph_runtime
- `app.gateway.routers` -> agents, artifacts, assistants_compat, auth, channel_connections, channels, console, features, feedback, github_webhooks, input_polish, mcp, memory, models, runs, scheduled_tasks, skills, suggestions, thread_runs, threads, uploads
- `app.gateway.trace_middleware` -> TraceMiddleware, resolve_trace_enabled
- `deerflow.config` -> deerflow_app_config
- `deerflow.logging_config` -> DEFAULT_LOG_DATE_FORMAT, DEFAULT_LOG_FORMAT, configure_logging
- `deerflow.tracing.monocle` -> setup_monocle_tracing_if_enabled
- `deerflow.uploads.manager` -> cleanup_stale_upload_staging_files

## 模块级常量
- `AppConfig` = deerflow_app_config.AppConfig
- `get_app_config` = deerflow_app_config.get_app_config
- `logger` = logging.getLogger(__name__)
- `_SHUTDOWN_HOOK_TIMEOUT_SECONDS` = 5.0
- `app` = create_app()

## 函数
#### `⏵ƒ` `async _ensure_admin_user(app: FastAPI) -> None`  L61
  - _文档首行_（仅供参考）: Startup hook: handle first boot and migrate orphan threads otherwise.
  - 分支数 8，函数体节点数 209；return: None
  - 调用: get_local_provider, warning, get_session_factory, count_admin_users, info, sf, limit, where, select, scalar_one_or_none, execute, str, getattr, _migrate_orphaned_threads, exception
  - 反射: getattr (L123)

#### `⏵ƒ` `async _iter_store_items(store, namespace, *, page_size: int)`  L133
  - _文档首行_（仅供参考）: Paginated async iterator over a LangGraph store namespace.
  - 分支数 4，函数体节点数 65；生成器（yield）；return: None
  - 调用: asearch, len

#### `⏵ƒ` `async _migrate_orphaned_threads(store, admin_user_id: str) -> int`  L153
  - _文档首行_（仅供参考）: Migrate LangGraph store threads with no user_id to the given admin.
  - 分支数 2，函数体节点数 90；return: migrated
  - 调用: _iter_store_items, get, aput

#### `⏵ƒ` `async lifespan(app: FastAPI) -> AsyncGenerator[None, None]`    @asynccontextmanager  L171
  - _文档首行_（仅供参考）: Application lifespan handler.
  - 分支数 19，函数体节点数 595；生成器（yield）；raise: RuntimeError(error_msg)
  - 调用: get_app_config, configure_logging, info, warn_if_auth_disabled_enabled, exception, RuntimeError, get_gateway_config, setup_monocle_tracing_if_enabled, get_memory_manager, getattr, callable, type, wait_for, to_thread, warning, langgraph_runtime, _ensure_admin_user, start_channel_service, get_status, ScheduledTaskService（+5）
  - 反射: getattr (L215), getattr (L260), getattr (L260), getattr (L298)

#### `ƒ` `create_app() -> FastAPI`  L344
  - _文档首行_（仅供参考）: Create and configure the FastAPI application.
  - 分支数 2，函数体节点数 463；return: {'status': 'healthy', 'service': 'deer-flow-gateway'}, app
  - 调用: get_gateway_config, FastAPI, add_middleware, sorted, get_configured_cors_origins, _resolve_trace_enabled_for_app_construction, include_router, is_route_enabled, info, warning, get

#### `ƒ` `_resolve_trace_enabled_for_app_construction() -> bool`  L559
  - _文档首行_（仅供参考）: Resolve the trace middleware flag without making imports require config.yaml.
  - 分支数 1，函数体节点数 26；return: resolve_trace_enabled(get_app_config()), False
  - 调用: resolve_trace_enabled, get_app_config, debug

## 文件内调用关系
- `_ensure_admin_user` -> _migrate_orphaned_threads
- `_migrate_orphaned_threads` -> _iter_store_items
- `lifespan` -> _ensure_admin_user
- `create_app` -> _resolve_trace_enabled_for_app_construction

# `backend/app/gateway/services.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/services.py`  ·  行数: 925

**模块文档首行**（仅供参考）: Run lifecycle service layer.

## 模块概览
- 函数 19 个，类 0 个，模块级常量 10 个

## 依赖（import）
- 模块: asyncio, json, logging, re
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `types` -> SimpleNamespace
- `typing` -> Any
- `fastapi` -> HTTPException, Request
- `langchain_core.messages` -> BaseMessage
- `langchain_core.messages.utils` -> convert_to_messages
- `langgraph.types` -> Command
- `app.gateway.auth_disabled` -> AUTH_SOURCE_INTERNAL
- `app.gateway.deps` -> get_checkpointer, get_local_provider, get_run_context, get_run_manager, get_stream_bridge
- `app.gateway.internal_auth` -> INTERNAL_OWNER_USER_ID_HEADER_NAME, INTERNAL_SYSTEM_ROLE, get_internal_user, get_trusted_internal_owner_user_id
- `app.gateway.utils` -> sanitize_log_param
- `deerflow.agents.middlewares.dynamic_context_middleware` -> _DYNAMIC_CONTEXT_REMINDER_KEY, _REMINDER_DATE_KEY
- `deerflow.config.app_config` -> get_app_config
- `deerflow.runtime` -> END_SENTINEL, HEARTBEAT_SENTINEL, ConflictError, DisconnectMode, RunManager, RunRecord, RunStatus, StreamBridge, UnsupportedStrategyError, run_agent
- `deerflow.runtime.goal` -> goal_thread_lock
- `deerflow.runtime.runs.naming` -> resolve_root_run_name
- `deerflow.runtime.secret_context` -> redact_config_secrets
- `deerflow.runtime.user_context` -> reset_current_user, set_current_user
- `deerflow.utils.messages` -> ORIGINAL_USER_CONTENT_KEY

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_TERMINAL_RUN_STATUSES` = {RunStatus.success, RunStatus.error, RunStatus.timeout, R...
- `_SERVER_OWNED_DYNAMIC_CONTEXT_KEYS` = frozenset({_DYNAMIC_CONTEXT_REMINDER_KEY, _REMINDER_DATE_...
- `_DEFAULT_ASSISTANT_ID` = 'lead_agent'
- `_CONTEXT_CONFIGURABLE_KEYS` = frozenset({'model_name', 'mode', 'thinking_enabled', 'rea...
- `_CONTEXT_INTERNAL_CALLER_KEYS` = frozenset({'non_interactive'})
- `_SERVER_OWNED_AUTHZ_CONTEXT_KEYS` = frozenset({'is_internal', 'authz_attributes', 'channel_us...
- `_CONTEXT_RUNTIME_ONLY_KEYS` = frozenset({'github_token', 'disable_clarification'})
- `_DEFAULT_RECURSION_LIMIT` = 100
- `_DEFAULT_MAX_RECURSION_LIMIT` = 1000

## 函数
#### `ƒ` `format_sse(event: str, data: Any, *, event_id: str | None) -> str`  L74
  - _文档首行_（仅供参考）: Format a single SSE frame.
  - 分支数 1，函数体节点数 84；return: '\n'.join(parts)
  - 调用: dumps, append, join

#### `ƒ` `_run_is_terminal(record: RunRecord) -> bool`  L90
  - 分支数 0，函数体节点数 16；return: record.status in _TERMINAL_RUN_STATUSES

#### `⏵ƒ` `async _terminal_record_stream_missing(bridge: StreamBridge, record: RunRecord) -> bool`  L94
  - _文档首行_（仅供参考）: True when a terminal run has no retained stream on bridges that can tell.
  - 分支数 3，函数体节点数 76；return: False, not bool(await stream_exists(record.run_id))
  - 调用: _run_is_terminal, getattr, bool, stream_exists, debug, sanitize_log_param
  - 反射: getattr (L98)

#### `ƒ` `normalize_stream_modes(raw: list[str] | str | None) -> list[str]`  L117
  - _文档首行_（仅供参考）: Normalize the stream_mode parameter to a list.
  - 分支数 2，函数体节点数 56；return: ['values'], [raw], raw if raw else ['values']
  - 调用: isinstance

#### `ƒ` `_strip_external_message_metadata(message: Any) -> Any`  L129
  - _文档首行_（仅供参考）: Remove server-owned metadata from an untrusted input message.
  - 分支数 3，函数体节点数 78；return: message, message.model_copy(update={'additional_kwargs': additional_kwargs})
  - 调用: isinstance, dict, pop, model_copy

#### `ƒ` `normalize_input(raw_input: dict[str, Any] | None, *, trusted_internal: bool) -> dict[str, Any]`  L142
  - _文档首行_（仅供参考）: Convert LangGraph Platform input format to LangChain state dict.
  - 分支数 7，函数体节点数 186；raise: HTTPException(status_code=400, detail=f'Invalid message at input.messages[{index}]: {exc}')；return: {}, {**raw_input, 'messages': converted}, raw_input
  - 调用: get, isinstance, enumerate, append, extend, convert_to_messages, HTTPException, _strip_external_message_metadata

#### `ƒ` `strip_internal_context_keys(config: dict[str, Any]) -> None`  L240
  - _文档首行_（仅供参考）: Drop internal-only keys a non-internal caller smuggled into the run config.
  - 分支数 3，函数体节点数 55
  - 调用: get, isinstance, pop

#### `ƒ` `merge_run_context_overrides(config: dict[str, Any], context: Mapping[str, Any] | None, *, internal: bool) -> None`  L255
  - _文档首行_（仅供参考）: Merge whitelisted keys from ``body.context`` into both ``config['configurable']``
  - 分支数 8，函数体节点数 192；return: None
  - 调用: setdefault, isinstance

#### `⏵ƒ` `async resolve_trusted_internal_owner_for_attribution(request: Request, owner_user_id: str | None) -> Any | None`  L297
  - _文档首行_（仅供参考）: Resolve the DeerFlow user used only for trusted internal attribution.
  - 分支数 3，函数体节点数 79；return: None, await get_local_provider().get_user(owner_user_id)
  - 调用: getattr, get_user, get_local_provider, exception, sanitize_log_param
  - 反射: getattr (L302), getattr (L303)

#### `ƒ` `inject_authenticated_user_context(config: dict[str, Any], request: Request, *, internal_owner_user: Any | None, request_context: Mapping[str, Any] | None) -> None`  L312
  - _文档首行_（仅供参考）: Stamp the authenticated user into the run context for background tools.
  - 分支数 12，函数体节点数 403；raise: TypeError('run context must be a mapping')；return: None
  - 调用: setdefault, isinstance, TypeError, pop, get, getattr, str
  - 反射: getattr (L343), getattr (L343), getattr (L350), getattr (L351), getattr (L355), getattr (L364), getattr (L367), getattr (L368), getattr (L369), getattr (L375), getattr (L376), getattr (L377)

#### `ƒ` `resolve_agent_factory(assistant_id: str | None)`  L380
  - _文档首行_（仅供参考）: Resolve the agent factory callable from config.
  - 分支数 0，函数体节点数 15；return: make_lead_agent

#### `ƒ` `_resolve_max_recursion_limit() -> int`  L404
  - _文档首行_（仅供参考）: Resolve the clamp ceiling from ``AppConfig.max_recursion_limit``.
  - 分支数 1，函数体节点数 19；return: get_app_config().max_recursion_limit, _DEFAULT_MAX_RECURSION_LIMIT
  - 调用: get_app_config

#### `ƒ` `_clamp_recursion_limit(value: Any, max_limit: int) -> int`  L417
  - _文档首行_（仅供参考）: Clamp a client-supplied ``recursion_limit`` into a safe server range.
  - 分支数 1，函数体节点数 47；return: _DEFAULT_RECURSION_LIMIT, min(value, max_limit)
  - 调用: isinstance, min

#### `ƒ` `build_run_config(thread_id: str, request_config: dict[str, Any] | None, metadata: dict[str, Any] | None, *, assistant_id: str | None) -> dict[str, Any]`  L429
  - _文档首行_（仅供参考）: Build a RunnableConfig dict for the agent.
  - 分支数 16，函数体节点数 544；raise: ValueError("request config 'context' must be a mapping or null."), ValueError(f'Invalid assistant_id {assistant_id!r}: must contain only letters, digits, and hyphens after normalization.')；return: config
  - 调用: warning, list, keys, get, isinstance, items, startswith, ValueError, update, _resolve_max_recursion_limit, _clamp_recursion_limit, replace, lower, strip, fullmatch, setdefault, resolve_root_run_name
  - 文件IO: replace (L523)

#### `⏵ƒ` `async apply_checkpoint_to_run_config(config: dict[str, Any], *, body: Any, thread_id: str, request: Request) -> None`  L544
  - _文档首行_（仅供参考）: Validate an optional run checkpoint and attach it to RunnableConfig.
  - 分支数 11，函数体节点数 346；raise: HTTPException(status_code=400, detail='checkpoint must be an object'), HTTPException(status_code=400, detail='checkpoint thread_id does not match request thread_id'), HTTPException(status_code=500, detail='Failed to validate checkpoint'), HTTPException(status_code=404, detail=f'Checkpoint {checkpoint_id} not found'), HTTPException(status_code=400, detail='request config configurable must be an object')；return: None
  - 调用: getattr, isinstance, HTTPException, get, str, get_checkpointer, aget_tuple, exception, sanitize_log_param, setdefault
  - 反射: getattr (L552), getattr (L553)

#### `⏵ƒ` `async start_run(body: Any, thread_id: str, request: Request) -> RunRecord`  L608
  - _文档首行_（仅供参考）: Create a RunRecord and launch the background agent task.
  - 分支数 17，函数体节点数 742；raise: HTTPException(status_code=400, detail=f'Model {model_name!r} is not in the configured model allowlist'), HTTPException(status_code=404, detail=f'Thread {thread_id} not found'), HTTPException(status_code=409, detail=str(exc)), HTTPException(status_code=501, detail=str(exc))；return: record
  - 调用: get_stream_bridge, get_run_manager, get_run_context, getattr, get, isinstance, str, get_app_config, get_model_config, HTTPException, get_trusted_internal_owner_user_id, check_access, set_current_user, SimpleNamespace, goal_thread_lock, create_or_reject, redact_config_secrets, update_owner, create, update_status（+15）
  - 反射: getattr (L631), getattr (L661), getattr (L664), getattr (L718), getattr (L718), getattr (L719), getattr (L731), getattr (L741)

#### `⏵ƒ` `async launch_scheduled_thread_run(*, thread_id: str, assistant_id: str | None, prompt: str, request: Request | None, app: Any | None, owner_user_id: str | None, metadata: dict[str, Any] | None) -> dict[str, Any]`  L773
  - 分支数 2，函数体节点数 205；raise: ValueError('launch_scheduled_thread_run requires request or app')；return: {'run_id': record.run_id, 'thread_id': record.thread_id}
  - 调用: ValueError, SimpleNamespace, get_internal_user, start_run

#### `⏵ƒ` `async sse_consumer(bridge: StreamBridge, record: RunRecord, request: Request, run_mgr: RunManager)`  L828
  - _文档首行_（仅供参考）: Async generator that yields SSE frames from the bridge.
  - 分支数 9，函数体节点数 187；生成器（yield）；return: None
  - 调用: get, _terminal_record_stream_missing, subscribe, is_disconnected, cancel

#### `⏵ƒ` `async wait_for_run_completion(bridge: StreamBridge, record: RunRecord, request: Request, run_mgr: RunManager) -> bool`  L873
  - _文档首行_（仅供参考）: Block until the run publishes ``END_SENTINEL``, honouring on_disconnect.
  - 分支数 8，函数体节点数 138；return: True, completed
  - 调用: _terminal_record_stream_missing, subscribe, is_disconnected, cancel

## 文件内调用关系
- `_terminal_record_stream_missing` -> _run_is_terminal
- `normalize_input` -> _strip_external_message_metadata
- `build_run_config` -> _resolve_max_recursion_limit, _clamp_recursion_limit
- `start_run` -> resolve_agent_factory, normalize_input, build_run_config, apply_checkpoint_to_run_config, merge_run_context_overrides, strip_internal_context_keys, resolve_trusted_internal_owner_for_attribution, inject_authenticated_user_context, normalize_stream_modes
- `launch_scheduled_thread_run` -> start_run
- `sse_consumer` -> _terminal_record_stream_missing
- `wait_for_run_completion` -> _terminal_record_stream_missing

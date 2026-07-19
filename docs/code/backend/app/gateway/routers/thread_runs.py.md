# `backend/app/gateway/routers/thread_runs.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/thread_runs.py`  ·  行数: 1004

**模块文档首行**（仅供参考）: Runs endpoints — create, stream, wait, cancel.

## 模块概览
- 函数 42 个，类 8 个，模块级常量 5 个

## 依赖（import）
- 模块: asyncio, logging
- `__future__` -> annotations
- `copy` -> deepcopy
- `datetime` -> UTC, datetime
- `typing` -> Any, Literal
- `fastapi` -> APIRouter, HTTPException, Query, Request
- `fastapi.responses` -> Response, StreamingResponse
- `langchain_core.messages` -> BaseMessage
- `pydantic` -> BaseModel, Field
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_checkpointer, get_current_user, get_feedback_repo, get_run_event_store, get_run_manager, get_run_store, get_stream_bridge
- `app.gateway.pagination` -> trim_run_message_page
- `app.gateway.services` -> sse_consumer, start_run, wait_for_run_completion
- `deerflow.runtime` -> CancelOutcome, RunRecord, RunStatus, serialize_channel_values_for_api
- `deerflow.utils.messages` -> ORIGINAL_USER_CONTENT_KEY, get_original_user_content_text, message_to_text
- `deerflow.workspace_changes` -> get_workspace_changes_response

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/threads', tags=['runs'])
- `REGENERATE_HISTORY_SCAN_LIMIT` = 200
- `REGENERATE_HISTORY_RAW_SCAN_LIMIT` = REGENERATE_HISTORY_SCAN_LIMIT * 2
- `THREAD_MESSAGE_PAGE_SCAN_BATCH` = 201

## 函数
#### `ƒ` `_is_duration_only_checkpoint(checkpoint_tuple: Any) -> bool`  L42
  - 分支数 0，函数体节点数 50；return: isinstance(writes, dict) and 'runtime_run_duration' in writes
  - 调用: getattr, isinstance, get
  - 反射: getattr (L43)

#### `ƒ` `compute_run_durations(runs) -> dict[str, int]`  L48
  - _文档首行_（仅供参考）: Map run_id -> duration in seconds from run timestamps.
  - 分支数 3，函数体节点数 122；return: durations
  - 调用: fromisoformat, replace, int, total_seconds, warning
  - 文件IO: replace (L56), replace (L57)

#### `ƒ` `_cancel_conflict_detail(run_id: str, record: RunRecord) -> str`  L161
  - 分支数 1，函数体节点数 49；return: f'Run {run_id} is not active on this worker and cannot be cancelled', f'Run {run_id} is not cancellable (status: {record.status.value})'

#### `ƒ` `_compute_retry_after(lease_expires_at: str | None, grace_seconds: int) -> int | None`  L167
  - _文档首行_（仅供参考）: Return seconds until the lease expires + grace, for ``Retry-After``.
  - 分支数 3，函数体节点数 96；return: None, max(1, int(remaining))
  - 调用: fromisoformat, replace, total_seconds, now, max, int
  - 文件IO: replace (L183)

#### `⏵ƒ` `async _raise_lease_valid_elsewhere(run_id: str, run_mgr, record: RunRecord) -> None`  L190
  - _文档首行_（仅供参考）: Re-fetch the lease and raise HTTP 409 + Retry-After.
  - 分支数 2，函数体节点数 95；raise: HTTPException(status_code=409, detail=f'Run {run_id} is active on another worker; retry after lease expiry.', headers=headers)
  - 调用: get, _compute_retry_after, str, HTTPException

#### `ƒ` `_record_to_response(record: RunRecord) -> RunResponse`  L215
  - 分支数 0，函数体节点数 103；return: RunResponse(run_id=record.run_id, thread_id=record.thread_id, assistant_id=record.assistant_id, status=record.status.value, metadata=record.metadata, kwargs=record.kwargs, multitask_strategy=record.multitask_strategy, created_at=record.created_at, updated_at=record.updated_at, total_input_tokens=record.total_input_tokens, total_output_tokens=record.total_output_tokens, total_tokens=record.total_tokens, llm_call_count=record.llm_call_count, lead_agent_tokens=record.lead_agent_tokens, subagent_tokens=record.subagent_tokens, middleware_tokens=record.middleware_tokens, message_count=record.message_count, stop_reason=record.stop_reason)
  - 调用: RunResponse

#### `ƒ` `_message_id(message: Any) -> str | None`  L238
  - 分支数 1，函数体节点数 54；return: str(value) if value else None
  - 调用: getattr, isinstance, get, str
  - 反射: getattr (L239)

#### `ƒ` `_message_type(message: Any) -> str | None`  L245
  - 分支数 2，函数体节点数 70；return: 'ai', str(value) if value else None
  - 调用: getattr, isinstance, get, str
  - 反射: getattr (L246)

#### `ƒ` `_message_name(message: Any) -> str | None`  L254
  - 分支数 1，函数体节点数 54；return: str(value) if value else None
  - 调用: getattr, isinstance, get, str
  - 反射: getattr (L255)

#### `ƒ` `_message_content(message: Any) -> Any`  L261
  - 分支数 1，函数体节点数 30；return: message.get('content'), getattr(message, 'content', None)
  - 调用: isinstance, get, getattr
  - 反射: getattr (L264)

#### `ƒ` `_message_text(message: Any) -> str`  L267
  - 分支数 0，函数体节点数 13；return: message_to_text(message)
  - 调用: message_to_text

#### `ƒ` `_message_additional_kwargs(message: Any) -> dict[str, Any]`  L271
  - 分支数 1，函数体节点数 67；return: dict(value or {}) if isinstance(value, dict) else {}
  - 调用: getattr, isinstance, get, dict
  - 反射: getattr (L272)

#### `ƒ` `_is_hidden_or_control_message(message: Any) -> bool`  L278
  - 分支数 0，函数体节点数 48；return: message_type == 'remove' or _message_name(message) == 'summary' or additional_kwargs.get('hide_from_ui') is True
  - 调用: _message_type, _message_additional_kwargs, _message_name, get

#### `ƒ` `_is_visible_human_message(message: Any) -> bool`  L284
  - 分支数 0，函数体节点数 25；return: _message_type(message) == 'human' and (not _is_hidden_or_control_message(message))
  - 调用: _message_type, _is_hidden_or_control_message

#### `ƒ` `_is_visible_ai_message(message: Any) -> bool`  L288
  - 分支数 0，函数体节点数 25；return: _message_type(message) == 'ai' and (not _is_hidden_or_control_message(message))
  - 调用: _message_type, _is_hidden_or_control_message

#### `ƒ` `_is_middleware_message_row(row: dict[str, Any]) -> bool`  L292
  - 分支数 0，函数体节点数 37；return: str((row.get('metadata') or {}).get('caller', '')).startswith('middleware:')
  - 调用: startswith, str, get

#### `ƒ` `_checkpoint_messages(checkpoint_tuple: Any) -> list[Any]`  L296
  - 分支数 0，函数体节点数 77；return: messages if isinstance(messages, list) else []
  - 调用: getattr, isinstance, get
  - 反射: getattr (L297)

#### `ƒ` `_checkpoint_configurable(checkpoint_tuple: Any) -> dict[str, Any]`  L303
  - 分支数 0，函数体节点数 62；return: dict(configurable) if isinstance(configurable, dict) else {}
  - 调用: getattr, isinstance, get, dict
  - 反射: getattr (L304)

#### `ƒ` `_checkpoint_response(checkpoint_tuple: Any) -> dict[str, Any]`  L309
  - 分支数 1，函数体节点数 73；raise: HTTPException(status_code=409, detail='Checkpoint is missing checkpoint_id')；return: {'checkpoint_ns': str(configurable.get('checkpoint_ns') or ''), 'checkpoint_id': str(checkpoint_id), 'checkpoint_map': configurable.get('checkpoint_map')}
  - 调用: _checkpoint_configurable, get, HTTPException, str

#### `ƒ` `_clean_human_message_for_regenerate(message: Any) -> dict[str, Any]`  L321
  - 分支数 2，函数体节点数 122；return: clean_message
  - 调用: _message_additional_kwargs, get_original_user_content_text, _message_content, pop, _message_id, _message_name

#### `ƒ` `_event_message_id(row: dict[str, Any]) -> str | None`  L341
  - 分支数 2，函数体节点数 57；return: _message_id(content), None
  - 调用: get, isinstance, _message_id

#### `ƒ` `_run_last_ai_matches_message(record: RunRecord, message: Any) -> bool`  L350
  - 分支数 2，函数体节点数 63；return: False, last_ai_message == target_text[:len(last_ai_message)]
  - 调用: strip, _message_text, len

#### `⏵ƒ` `async _find_target_run_id(thread_id: str, message_id: str, target_message: Any, request: Request) -> str`  L360
  - 分支数 6，函数体节点数 202；raise: HTTPException(status_code=409, detail='Could not find source run for assistant message')；return: run_id, fallback_record.run_id
  - 调用: get_run_event_store, list_messages, reversed, get, _event_message_id, isinstance, get_run_manager, get_current_user, list_by_thread, next, _run_last_ai_matches_message, len, warning, HTTPException

#### `⏵ƒ` `async _find_base_checkpoint_before_human(thread_id: str, human_message_id: str, request: Request) -> Any`  L389
  - 分支数 6，函数体节点数 201；raise: HTTPException(status_code=500, detail='Failed to inspect checkpoint history'), HTTPException(status_code=409, detail='Could not find an addressable checkpoint before the target user message'), HTTPException(status_code=409, detail=f'Could not locate target user message in recent checkpoint history (limit={REGENERATE_HISTORY_SCAN_LIMIT})')；return: previous_checkpoint
  - 调用: get_checkpointer, alist, _is_duration_only_checkpoint, exception, HTTPException, reversed, _checkpoint_messages, _message_id, get, _checkpoint_configurable, len, warning

#### `⏵ƒ` `async _prepare_regenerate_payload(thread_id: str, message_id: str, request: Request) -> RegeneratePrepareResponse`  L426
  - 分支数 7，函数体节点数 347；raise: HTTPException(status_code=500, detail='Failed to read latest checkpoint'), HTTPException(status_code=404, detail=f'Thread {thread_id} has no checkpoint'), HTTPException(status_code=404, detail=f'Message {message_id} not found'), HTTPException(status_code=409, detail='Only visible assistant messages can be regenerated'), HTTPException(status_code=409, detail='Only the latest assistant message can be regenerated'), HTTPException(status_code=409, detail='Could not find the user message for this assistant response'), HTTPException(status_code=409, detail='The source user message is missing an id')；return: RegeneratePrepareResponse(input={'messages': [_clean_human_message_for_regenerate(previous_human)]}, checkpoint=checkpoint, metadata=metadata, target_run_id=target_run_id)
  - 调用: get_checkpointer, aget_tuple, exception, HTTPException, _checkpoint_messages, next, enumerate, _message_id, _is_visible_ai_message, reversed, _is_visible_human_message, _find_base_checkpoint_before_human, _find_target_run_id, _checkpoint_response, RegeneratePrepareResponse, _clean_human_message_for_regenerate

#### `⏵ƒ` `async prepare_regenerate_run(thread_id: str, body: RegeneratePrepareRequest, request: Request) -> RegeneratePrepareResponse`    @router.post(...), require_permission(...)  L479
  - _文档首行_（仅供参考）: Prepare input and checkpoint for regenerating the latest assistant turn.
  - 分支数 0，函数体节点数 46；return: await _prepare_regenerate_payload(thread_id, body.message_id, request)
  - 调用: _prepare_regenerate_payload, post, require_permission

#### `⏵ƒ` `async create_run(thread_id: str, body: RunCreateRequest, request: Request) -> RunResponse`    @router.post(...), require_permission(...)  L490
  - _文档首行_（仅供参考）: Create a background run (returns immediately).
  - 分支数 0，函数体节点数 52；return: _record_to_response(record)
  - 调用: start_run, _record_to_response, post, require_permission

#### `⏵ƒ` `async stream_run(thread_id: str, body: RunCreateRequest, request: Request) -> StreamingResponse`    @router.post(...), require_permission(...)  L498
  - _文档首行_（仅供参考）: Create a run and stream events via SSE.
  - 分支数 0，函数体节点数 96；return: StreamingResponse(sse_consumer(bridge, record, request, run_mgr), media_type='text/event-stream', headers={'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'X-Accel-Buffering': 'no', 'Content-Location': f'/api/threads/{thread_id}/runs/{record.run_id}'})
  - 调用: get_stream_bridge, get_run_manager, start_run, StreamingResponse, sse_consumer, post, require_permission

#### `⏵ƒ` `async wait_run(thread_id: str, body: RunCreateRequest, request: Request) -> dict`    @router.post(...), require_permission(...)  L526
  - _文档首行_（仅供参考）: Create a run and block until it completes, returning the final state.
  - 分支数 4，函数体节点数 184；return: serialize_channel_values_for_api(channel_values), {'status': record.status.value, 'error': record.error}
  - 调用: get_stream_bridge, get_run_manager, start_run, wait_for_run_completion, get_checkpointer, aget_tuple, getattr, get, serialize_channel_values_for_api, exception, post, require_permission
  - 反射: getattr (L542)

#### `⏵ƒ` `async list_runs(thread_id: str, request: Request) -> list[RunResponse]`    @router.get(...), require_permission(...)  L553
  - _文档首行_（仅供参考）: List all runs for a thread.
  - 分支数 0，函数体节点数 79；return: [_record_to_response(r) for r in records]
  - 调用: get_run_manager, get_current_user, list_by_thread, _record_to_response, get, require_permission

#### `⏵ƒ` `async get_run(thread_id: str, run_id: str, request: Request) -> RunResponse`    @router.get(...), require_permission(...)  L563
  - _文档首行_（仅供参考）: Get details of a specific run.
  - 分支数 1，函数体节点数 97；raise: HTTPException(status_code=404, detail=f'Run {run_id} not found')；return: _record_to_response(record)
  - 调用: get_run_manager, get_current_user, get, HTTPException, _record_to_response, require_permission

#### `⏵ƒ` `async cancel_run(thread_id: str, run_id: str, request: Request, wait: bool, action: Literal['interrupt', 'rollback']) -> Response`    @router.post(...), require_permission(...)  L575
  - _文档首行_（仅供参考）: Cancel a running or pending run.
  - 分支数 5，函数体节点数 204；raise: HTTPException(status_code=404, detail=f'Run {run_id} not found'), HTTPException(status_code=409, detail=_cancel_conflict_detail(run_id, record))；return: Response(status_code=204), Response(status_code=202)
  - 调用: Query, get_run_manager, get, HTTPException, cancel, Response, _raise_lease_valid_elsewhere, _cancel_conflict_detail, post, require_permission

#### `⏵ƒ` `async join_run(thread_id: str, run_id: str, request: Request) -> StreamingResponse`    @router.get(...), require_permission(...)  L620
  - _文档首行_（仅供参考）: Join an existing run's SSE stream.
  - 分支数 2，函数体节点数 135；raise: HTTPException(status_code=404, detail=f'Run {run_id} not found'), HTTPException(status_code=409, detail=f'Run {run_id} is not active on this worker and cannot be streamed')；return: StreamingResponse(sse_consumer(bridge, record, request, run_mgr), media_type='text/event-stream', headers={'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'X-Accel-Buffering': 'no'})
  - 调用: get_run_manager, get, HTTPException, get_stream_bridge, StreamingResponse, sse_consumer, require_permission

#### `⏵ƒ` `async stream_existing_run(thread_id: str, run_id: str, request: Request, action: Literal['interrupt', 'rollback'] | None, wait: int)`    @router.get(...), router.post(...), require_permission(...)  L648
  - _文档首行_（仅供参考）: Join an existing run's SSE stream (GET), or cancel-then-stream (POST).
  - 分支数 8，函数体节点数 290；raise: HTTPException(status_code=404, detail=f'Run {run_id} not found'), HTTPException(status_code=409, detail=f'Run {run_id} is not active on this worker and cannot be streamed'), HTTPException(status_code=409, detail=_cancel_conflict_detail(run_id, record))；return: Response(status_code=202), Response(status_code=204), StreamingResponse(sse_consumer(bridge, record, request, run_mgr), media_type='text/event-stream', headers={'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'X-Accel-Buffering': 'no'})
  - 调用: Query, get_run_manager, get, HTTPException, get_stream_bridge, cancel, Response, _raise_lease_valid_elsewhere, _cancel_conflict_detail, StreamingResponse, sse_consumer, post, require_permission

#### `⏵ƒ` `async list_thread_messages(thread_id: str, request: Request, limit: int, before_seq: int | None, after_seq: int | None) -> list[dict]`    @router.get(...), require_permission(...)  L708
  - _文档首行_（仅供参考）: Return displayable messages for a thread (across all runs), with feedback attached.
  - 分支数 10，函数体节点数 394；return: messages
  - 调用: Query, get_run_event_store, list_messages, get_current_user, enumerate, get, get_feedback_repo, list_by_thread_grouped, set, values, get_run_manager, list_by_thread, compute_run_durations, isinstance, require_permission

#### `⏵ƒ` `async _scan_thread_message_page(thread_id: str, *, limit: int, before_seq: int | None, request: Request, user_id: str | None) -> tuple[list[dict[str, Any]], bool]`  L773
  - _文档首行_（仅供参考）: Select the newest ``limit + 1`` page-eligible rows before a cursor.
  - 分支数 8，函数体节点数 347；raise: RuntimeError('Run event message rows are missing sequence values'), RuntimeError('Run event message scan did not advance its cursor')；return: (list(reversed(visible_desc[:limit])), has_more)
  - 调用: get_run_event_store, get_run_manager, list_successful_regenerate_sources, len, list_messages, isinstance, get, error, RuntimeError, reversed, _is_middleware_message_row, append, min, list

#### `⏵ƒ` `async _enrich_thread_message_page(thread_id: str, rows: list[dict[str, Any]], *, request: Request, user_id: str | None) -> list[dict[str, Any]]`  L835
  - _文档首行_（仅供参考）: Attach run-scoped duration and feedback without mutating store rows.
  - 分支数 6，函数体节点数 358；return: data
  - 调用: deepcopy, isinstance, get, get_run_manager, get_many_by_thread, compute_run_durations, values, get_run_event_store, get_last_visible_ai_seq_by_run, get_feedback_repo, list_by_run_ids, setdefault

#### `⏵ƒ` `async list_thread_messages_page(thread_id: str, request: Request, limit: int, before_seq: int | None) -> ThreadMessagesPageResponse`    @router.get(...), require_permission(...)  L880
  - _文档首行_（仅供参考）: Return a backward page ordered by the thread-global event sequence.
  - 分支数 1，函数体节点数 143；raise: HTTPException(status_code=422, detail='after_seq is not supported by this backward-only endpoint')；return: ThreadMessagesPageResponse(data=data, has_more=has_more, next_before_seq=data[0]['seq'] if has_more else None)
  - 调用: Query, HTTPException, get_current_user, _scan_thread_message_page, _enrich_thread_message_page, ThreadMessagesPageResponse, get, require_permission

#### `⏵ƒ` `async list_run_messages(thread_id: str, run_id: str, request: Request, limit: int, before_seq: int | None, after_seq: int | None) -> dict`    @router.get(...), require_permission(...)  L908
  - _文档首行_（仅供参考）: Return paginated messages for a specific run.
  - 分支数 6，函数体节点数 267；return: {'data': data, 'has_more': has_more}
  - 调用: Query, get_run_event_store, list_messages_by_run, trim_run_message_page, get_run_manager, get, compute_run_durations, reversed, startswith, str, isinstance, require_permission

#### `⏵ƒ` `async list_run_events(thread_id: str, run_id: str, request: Request, event_types: str | None, task_id: str | None, limit: int, after_seq: int | None) -> list[dict]`    @router.get(...), require_permission(...)  L951
  - _文档首行_（仅供参考）: Return the full event stream for a run (debug/audit).
  - 分支数 0，函数体节点数 123；return: await event_store.list_events(thread_id, run_id, event_types=types, task_id=task_id, limit=limit, after_seq=after_seq)
  - 调用: Query, get_run_event_store, split, list_events, get, require_permission

#### `⏵ƒ` `async get_run_workspace_changes(thread_id: str, run_id: str, request: Request, include_files: bool, include_diff: bool) -> dict`    @router.get(...), require_permission(...)  L972
  - _文档首行_（仅供参考）: Return workspace/output file changes recorded for one run.
  - 分支数 0，函数体节点数 69；return: await get_workspace_changes_response(event_store, thread_id, run_id, include_files=include_files, include_diff=include_diff)
  - 调用: Query, get_run_event_store, get_workspace_changes_response, get, require_permission

#### `⏵ƒ` `async thread_token_usage(thread_id: str, request: Request, include_active: bool) -> ThreadTokenUsageResponse`    @router.get(...), require_permission(...)  L992
  - _文档首行_（仅供参考）: Thread-level token usage aggregation.
  - 分支数 1，函数体节点数 83；return: ThreadTokenUsageResponse(thread_id=thread_id, **agg)
  - 调用: Query, get_run_store, aggregate_tokens_by_thread, ThreadTokenUsageResponse, get, require_permission

## 类
### 类 `RunCreateRequest`  L71
- 继承: BaseModel
- 类/实例变量:
  - `assistant_id` = Field(default=None, description='Agent / assistant to use')
  - `input` = Field(default=None, description='Graph input (e.g. {messa...
  - `command` = Field(default=None, description='LangGraph Command')
  - `metadata` = Field(default=None, description='Run metadata')
  - `config` = Field(default=None, description='RunnableConfig overrides')
  - `context` = Field(default=None, description='DeerFlow context overrid...
  - `webhook` = Field(default=None, description='Completion callback URL')
  - `checkpoint_id` = Field(default=None, description='Resume from checkpoint')
  - `checkpoint` = Field(default=None, description='Full checkpoint object')
  - `interrupt_before` = Field(default=None, description='Nodes to interrupt before')
  - `interrupt_after` = Field(default=None, description='Nodes to interrupt after')
  - `stream_mode` = Field(default=None, description='Stream mode(s)')
  - `stream_subgraphs` = Field(default=False, description='Include subgraph events')
  - `stream_resumable` = Field(default=None, description='SSE resumable mode')
  - `on_disconnect` = Field(default='cancel', description='Behaviour on SSE dis...
  - `on_completion` = Field(default='keep', description='Delete temp thread on ...
  - `multitask_strategy` = Field(default='reject', description='Concurrency strategy')
  - `after_seconds` = Field(default=None, description='Delayed execution')
  - `if_not_exists` = Field(default='create', description='Thread creation poli...
  - `feedback_keys` = Field(default=None, description='LangSmith feedback keys')

### 类 `RegeneratePrepareRequest`  L94
- 继承: BaseModel
- 类/实例变量:
  - `message_id` = Field(..., min_length=1, description='Assistant message i...

### 类 `RegeneratePrepareResponse`  L98
- 继承: BaseModel
- 类/实例变量:
  - `input` = <annotated>
  - `checkpoint` = <annotated>
  - `metadata` = <annotated>
  - `target_run_id` = <annotated>

### 类 `ThreadMessagesPageResponse`  L105
- 继承: BaseModel
- 类/实例变量:
  - `data` = <annotated>
  - `has_more` = <annotated>
  - `next_before_seq` = None

### 类 `RunResponse`  L111
- 继承: BaseModel
- 类/实例变量:
  - `run_id` = <annotated>
  - `thread_id` = <annotated>
  - `assistant_id` = None
  - `status` = <annotated>
  - `metadata` = Field(default_factory=dict)
  - `kwargs` = Field(default_factory=dict)
  - `multitask_strategy` = 'reject'
  - `created_at` = ''
  - `updated_at` = ''
  - `total_input_tokens` = 0
  - `total_output_tokens` = 0
  - `total_tokens` = 0
  - `llm_call_count` = 0
  - `lead_agent_tokens` = 0
  - `subagent_tokens` = 0
  - `middleware_tokens` = 0
  - `message_count` = 0
  - `stop_reason` = None

### 类 `ThreadTokenUsageModelBreakdown`  L132
- 继承: BaseModel
- 类/实例变量:
  - `tokens` = 0
  - `runs` = Field(default=0, description='Number of runs in which thi...

### 类 `ThreadTokenUsageCallerBreakdown`  L140
- 继承: BaseModel
- 类/实例变量:
  - `lead_agent` = 0
  - `subagent` = 0
  - `middleware` = 0

### 类 `ThreadTokenUsageResponse`  L146
- 继承: BaseModel
- 类/实例变量:
  - `thread_id` = <annotated>
  - `total_tokens` = 0
  - `total_input_tokens` = 0
  - `total_output_tokens` = 0
  - `total_runs` = 0
  - `by_model` = Field(default_factory=dict)
  - `by_caller` = Field(default_factory=ThreadTokenUsageCallerBreakdown)

## 文件内调用关系
- `_raise_lease_valid_elsewhere` -> _compute_retry_after
- `_is_hidden_or_control_message` -> _message_type, _message_additional_kwargs, _message_name
- `_is_visible_human_message` -> _message_type, _is_hidden_or_control_message
- `_is_visible_ai_message` -> _message_type, _is_hidden_or_control_message
- `_checkpoint_response` -> _checkpoint_configurable
- `_clean_human_message_for_regenerate` -> _message_additional_kwargs, _message_content, _message_id, _message_name
- `_event_message_id` -> _message_id
- `_run_last_ai_matches_message` -> _message_text
- `_find_target_run_id` -> _event_message_id, _run_last_ai_matches_message
- `_find_base_checkpoint_before_human` -> _is_duration_only_checkpoint, _checkpoint_messages, _message_id, _checkpoint_configurable
- `_prepare_regenerate_payload` -> _checkpoint_messages, _message_id, _is_visible_ai_message, _is_visible_human_message, _find_base_checkpoint_before_human, _find_target_run_id, _checkpoint_response, _clean_human_message_for_regenerate
- `prepare_regenerate_run` -> _prepare_regenerate_payload
- `create_run` -> _record_to_response
- `list_runs` -> _record_to_response
- `get_run` -> _record_to_response
- `cancel_run` -> _raise_lease_valid_elsewhere, _cancel_conflict_detail
- `stream_existing_run` -> _raise_lease_valid_elsewhere, _cancel_conflict_detail
- `list_thread_messages` -> compute_run_durations
- `_scan_thread_message_page` -> _is_middleware_message_row
- `_enrich_thread_message_page` -> compute_run_durations
- `list_thread_messages_page` -> _scan_thread_message_page, _enrich_thread_message_page
- `list_run_messages` -> compute_run_durations

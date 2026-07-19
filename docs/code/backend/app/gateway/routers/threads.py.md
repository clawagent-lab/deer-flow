# `backend/app/gateway/routers/threads.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/threads.py`  ·  行数: 1260

**模块文档首行**（仅供参考）: Thread CRUD, state, and history endpoints.

## 模块概览
- 函数 37 个，类 15 个，模块级常量 6 个

## 依赖（import）
- 模块: copy, logging, shutil, uuid
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Any
- `fastapi` -> APIRouter, BackgroundTasks, HTTPException, Request
- `langgraph.checkpoint.base` -> empty_checkpoint, uuid6
- `pydantic` -> BaseModel, Field, field_validator
- `sqlalchemy.exc` -> IntegrityError
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_checkpointer, get_run_manager
- `app.gateway.internal_auth` -> get_trusted_internal_owner_user_id
- `app.gateway.utils` -> sanitize_log_param
- `deerflow.config.paths` -> Paths, get_paths
- `deerflow.config.summarization_config` -> ContextSize
- `deerflow.runtime` -> serialize_channel_values_for_api
- `deerflow.runtime.context_compaction` -> ContextCompactionDisabled, ContextCompactionFailed, ThreadCompactionResult, compact_thread_context
- `deerflow.runtime.goal` -> DEFAULT_MAX_GOAL_CONTINUATIONS, build_goal_state, ensure_thread_checkpoint, goal_thread_lock, read_thread_goal, write_thread_goal
- `deerflow.runtime.runs.worker` -> valid_duration_entry
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.utils.file_io` -> run_file_io
- `deerflow.utils.time` -> coerce_iso, now_iso

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/threads', tags=['threads'])
- `_SERVER_RESERVED_METADATA_KEYS` = frozenset({'owner_id', 'user_id'})
- `_SIDECAR_METADATA_KEY` = 'deerflow_sidecar'
- `_BRANCH_METADATA_KEY` = 'deerflow_branch'
- `_BRANCH_HISTORY_SCAN_LIMIT` = 200

## 函数
#### `ƒ` `_strip_reserved_metadata(metadata: dict[str, Any] | None) -> dict[str, Any]`  L69
  - _文档首行_（仅供参考）: Return ``metadata`` with server-controlled keys removed.
  - 分支数 1，函数体节点数 63；return: metadata or {}, {k: v for k, v in metadata.items() if k not in _SERVER_RESERVED_METADATA_KEYS}
  - 调用: items

#### `ƒ` `_message_id(message: Any) -> str | None`  L76
  - 分支数 1，函数体节点数 53；return: raw if isinstance(raw, str) and raw else None
  - 调用: isinstance, get, getattr
  - 反射: getattr (L80)

#### `ƒ` `_message_type(message: Any) -> str | None`  L84
  - 分支数 1，函数体节点数 53；return: raw if isinstance(raw, str) and raw else None
  - 调用: isinstance, get, getattr
  - 反射: getattr (L88)

#### `ƒ` `_message_additional_kwargs(message: Any) -> dict[str, Any]`  L92
  - 分支数 1，函数体节点数 54；return: raw if isinstance(raw, dict) else {}
  - 调用: isinstance, get, getattr
  - 反射: getattr (L96)

#### `ƒ` `_is_branch_visible_message(message: Any) -> bool`  L100
  - 分支数 1，函数体节点数 33；return: False, _message_type(message) in {'human', 'ai'}
  - 调用: get, _message_additional_kwargs, _message_type

#### `ƒ` `_is_branch_assistant_message(message: Any) -> bool`  L106
  - 分支数 0，函数体节点数 16；return: _message_type(message) == 'ai'
  - 调用: _message_type

#### `ƒ` `_checkpoint_messages(checkpoint_tuple: Any) -> list[Any]`  L110
  - 分支数 0，函数体节点数 66；return: list(messages) if isinstance(messages, list) else []
  - 调用: getattr, get, isinstance, list
  - 反射: getattr (L111)

#### `ƒ` `_checkpoint_id(checkpoint_tuple: Any) -> str | None`  L117
  - 分支数 0，函数体节点数 53；return: raw if isinstance(raw, str) and raw else None
  - 调用: getattr, get, isinstance
  - 反射: getattr (L118)

#### `ƒ` `_matches_branch_target(messages: list[Any], target_message_ids: set[str]) -> bool`  L123
  - 分支数 3，函数体节点数 138；return: False, not any((_is_branch_visible_message(message) for message in messages[target_end_index + 1:]))
  - 调用: _message_id, enumerate, issubset, keys, any, _is_branch_assistant_message, max, _is_branch_visible_message

#### `⏵ƒ` `async _find_branch_checkpoint(checkpointer: Any, thread_id: str, target_message_ids: set[str]) -> Any`  L137
  - 分支数 3，函数体节点数 87；raise: HTTPException(status_code=500, detail='Failed to find branch checkpoint'), HTTPException(status_code=409, detail='This turn can no longer be branched from.')；return: checkpoint_tuple
  - 调用: alist, _matches_branch_target, _checkpoint_messages, exception, sanitize_log_param, HTTPException

#### `⏵ƒ` `async _branch_targets_latest_turn(checkpointer: Any, thread_id: str, target_message_ids: set[str]) -> bool`  L149
  - _文档首行_（仅供参考）: Return True when the target turn is the final visible turn in the current state.
  - 分支数 3，函数体节点数 85；return: _matches_branch_target(messages, target_message_ids), False
  - 调用: alist, _checkpoint_messages, _matches_branch_target, warning, sanitize_log_param

#### `ƒ` `_ignore_branch_user_data(directory: str, names: list[str]) -> set[str]`  L176
  - 分支数 3，函数体节点数 92；return: ignored
  - 调用: set, Path, startswith, endswith, add, is_symlink

#### `ƒ` `_copy_branch_user_data_sync(paths: Paths, source_thread_id: str, target_thread_id: str, *, user_id: str) -> str`  L188
  - 分支数 1，函数体节点数 69；return: 'not_found', 'current_thread_best_effort'
  - 调用: sandbox_user_data_dir, exists, copytree
  - 文件IO: exists (L191)

#### `⏵ƒ` `async _copy_branch_user_data(source_thread_id: str, target_thread_id: str) -> str`  L198
  - 分支数 1，函数体节点数 63；return: await run_file_io(_copy_branch_user_data_sync, paths, source_thread_id, target_thread_id, user_id=user_id), 'failed'
  - 调用: get_paths, get_effective_user_id, run_file_io, warning, sanitize_log_param

#### `ƒ` `_default_branch_display_name(source_title: Any, *, source_is_branch: bool) -> str | None`  L213
  - 分支数 3，函数体节点数 68；return: None, display_name or None
  - 调用: isinstance, strip, startswith, lower, len

#### `ƒ` `_delete_thread_data(thread_id: str, paths: Paths | None, *, user_id: str | None) -> ThreadDeleteResponse`  L400
  - _文档首行_（仅供参考）: Delete local persisted filesystem data for a thread.
  - 分支数 1，函数体节点数 138；raise: HTTPException(status_code=422, detail=str(exc)), HTTPException(status_code=500, detail='Failed to delete local thread data.')；return: ThreadDeleteResponse(success=True, message=f'No local data for {thread_id}'), ThreadDeleteResponse(success=True, message=f'Deleted local thread data for {thread_id}')
  - 调用: get_paths, delete_thread_dir, HTTPException, str, debug, sanitize_log_param, ThreadDeleteResponse, exception, info

#### `ƒ` `_derive_thread_status(checkpoint_tuple) -> str`  L419
  - _文档首行_（仅供参考）: Derive thread status from checkpoint metadata.
  - 分支数 4，函数体节点数 72；return: 'idle', 'error', 'interrupted'
  - 调用: getattr, len
  - 反射: getattr (L423), getattr (L431)

#### `⏵ƒ` `async _ensure_thread_for_goal(thread_id: str, request: Request) -> None`  L438
  - _文档首行_（仅供参考）: Ensure a thread_meta row and root checkpoint exist for goal commands.
  - 分支数 6，函数体节点数 208；raise: HTTPException(status_code=500, detail='Failed to create thread'), HTTPException(status_code=500, detail='Failed to create thread checkpoint')
  - 调用: get_thread_store, get_checkpointer, get_trusted_internal_owner_user_id, get, update_owner, create, exception, sanitize_log_param, HTTPException, ensure_thread_checkpoint

#### `⏵ƒ` `async delete_thread_data(thread_id: str, request: Request) -> ThreadDeleteResponse`    @router.delete(...), require_permission(...)  L475
  - _文档首行_（仅供参考）: Delete local persisted filesystem data for a thread.
  - 分支数 4，函数体节点数 132；return: response
  - 调用: _delete_thread_data, get_effective_user_id, getattr, hasattr, adelete_thread, debug, sanitize_log_param, get_thread_store, delete, require_permission
  - 反射: getattr (L488), hasattr (L491)

#### `⏵ƒ` `async _resolve_existing_thread(thread_store: Any, thread_id: str, thread_owner_user_id: str | None, thread_owner_kwargs: dict[str, Any]) -> dict | None`  L507
  - _文档首行_（仅供参考）: Return the existing thread_meta record for an idempotent create.
  - 分支数 3，函数体节点数 116；return: existing_record
  - 调用: get, update_owner

#### `ƒ` `_existing_thread_response(thread_id: str, record: dict) -> ThreadResponse`  L530
  - 分支数 0，函数体节点数 55；return: ThreadResponse(thread_id=thread_id, status=record.get('status', 'idle'), created_at=coerce_iso(record.get('created_at', '')), updated_at=coerce_iso(record.get('updated_at', '')), metadata=record.get('metadata', {}))
  - 调用: ThreadResponse, get, coerce_iso

#### `⏵ƒ` `async create_thread(body: ThreadCreateRequest, request: Request) -> ThreadResponse`    @router.post(...)  L541
  - _文档首行_（仅供参考）: Create a new thread.
  - 分支数 4，函数体节点数 314；raise: HTTPException(status_code=500, detail='Failed to create thread')；return: _existing_thread_response(thread_id, existing_record), ThreadResponse(thread_id=thread_id, status='idle', created_at=now, updated_at=now, metadata=body.metadata)
  - 调用: get_checkpointer, get_thread_store, str, uuid4, now_iso, get_trusted_internal_owner_user_id, _resolve_existing_thread, _existing_thread_response, create, getattr, exception, sanitize_log_param, HTTPException, aput, empty_checkpoint, info, ThreadResponse, post
  - 反射: getattr (L568)

#### `⏵ƒ` `async branch_thread(thread_id: str, body: ThreadBranchRequest, request: Request) -> ThreadBranchResponse`    @router.post(...), require_permission(...)  L619
  - _文档首行_（仅供参考）: Create a new main-thread branch from a completed assistant turn.
  - 分支数 6，函数体节点数 480；raise: HTTPException(status_code=404, detail=f'Thread {thread_id} not found'), HTTPException(status_code=409, detail='Branching is only available in the main conversation.'), HTTPException(status_code=409, detail='This turn can no longer be branched from.'), HTTPException(status_code=500, detail='Failed to create branch')；return: ThreadBranchResponse(thread_id=new_thread_id, parent_thread_id=thread_id, parent_checkpoint_id=parent_checkpoint_id, branched_from_message_id=body.message_id, workspace_clone_mode=workspace_clone_mode)
  - 调用: get_checkpointer, get_thread_store, get, HTTPException, _find_branch_checkpoint, _checkpoint_id, _branch_targets_latest_turn, str, uuid4, now_iso, _default_branch_display_name, get_trusted_internal_owner_user_id, deepcopy, getattr, uuid6, update, dict, aput, exception, sanitize_log_param（+5）
  - 反射: getattr (L664), getattr (L665)

#### `⏵ƒ` `async search_threads(body: ThreadSearchRequest, request: Request) -> list[ThreadResponse]`    @router.post(...)  L710
  - _文档首行_（仅供参考）: Search and list threads.
  - 分支数 1，函数体节点数 163；raise: HTTPException(status_code=400, detail=str(exc))；return: [ThreadResponse(thread_id=r['thread_id'], status=r.get('status', 'idle'), created_at=coerce_iso(r.get('created_at', '')), updated_at=coerce_iso(r.get('updated_at', '')), metadata=r.get('metadata', {}), values={'title': r['display_name']} if r.get('display_name') else {}, interrupts={}) for r in rows]
  - 调用: get_thread_store, search, HTTPException, str, ThreadResponse, get, coerce_iso, post

#### `⏵ƒ` `async patch_thread(thread_id: str, body: ThreadPatchRequest, request: Request) -> ThreadResponse`    @router.patch(...), require_permission(...)  L748
  - _文档首行_（仅供参考）: Merge metadata into a thread record.
  - 分支数 2，函数体节点数 170；raise: HTTPException(status_code=404, detail=f'Thread {thread_id} not found'), HTTPException(status_code=500, detail='Failed to update thread')；return: ThreadResponse(thread_id=thread_id, status=record.get('status', 'idle'), created_at=coerce_iso(record.get('created_at', '')), updated_at=coerce_iso(record.get('updated_at', '')), metadata=record.get('metadata', {}))
  - 调用: get_thread_store, get, HTTPException, update_metadata, exception, sanitize_log_param, ThreadResponse, coerce_iso, patch, require_permission

#### `⏵ƒ` `async get_thread(thread_id: str, request: Request) -> ThreadResponse`    @router.get(...), require_permission(...)  L777
  - _文档首行_（仅供参考）: Get thread info.
  - 分支数 4，函数体节点数 343；raise: HTTPException(status_code=500, detail='Failed to get thread'), HTTPException(status_code=404, detail=f'Thread {thread_id} not found')；return: ThreadResponse(thread_id=thread_id, status=status, created_at=coerce_iso(record.get('created_at', '')), updated_at=coerce_iso(record.get('updated_at', '')), metadata=record.get('metadata', {}), values=serialize_channel_values_for_api(channel_values))
  - 调用: get_thread_store, get_checkpointer, get, aget_tuple, exception, sanitize_log_param, HTTPException, getattr, coerce_iso, items, _derive_thread_status, ThreadResponse, serialize_channel_values_for_api, require_permission
  - 反射: getattr (L806), getattr (L819)

#### `⏵ƒ` `async get_thread_goal(thread_id: str, request: Request) -> ThreadGoalResponse`    @router.get(...), require_permission(...)  L834
  - _文档首行_（仅供参考）: Return the active Claude-style goal for a thread, if any.
  - 分支数 1，函数体节点数 79；raise: HTTPException(status_code=500, detail='Failed to read thread goal')；return: ThreadGoalResponse(goal=goal)
  - 调用: get_checkpointer, read_thread_goal, exception, sanitize_log_param, HTTPException, ThreadGoalResponse, get, require_permission

#### `⏵ƒ` `async set_thread_goal(thread_id: str, body: ThreadGoalRequest, request: Request) -> ThreadGoalResponse`    @router.put(...), require_permission(...)  L847
  - _文档首行_（仅供参考）: Set or replace the active goal for a thread.
  - 分支数 2，函数体节点数 134；raise: HTTPException(status_code=422, detail=str(exc)), HTTPException(status_code=500, detail='Failed to set thread goal')；return: ThreadGoalResponse(goal=goal)
  - 调用: get_checkpointer, _ensure_thread_for_goal, build_goal_state, goal_thread_lock, write_thread_goal, HTTPException, str, exception, sanitize_log_param, ThreadGoalResponse, put, require_permission

#### `⏵ƒ` `async clear_thread_goal(thread_id: str, request: Request) -> ThreadGoalResponse`    @router.delete(...), require_permission(...)  L869
  - _文档首行_（仅供参考）: Clear the active goal for a thread.
  - 分支数 2，函数体节点数 95；raise: HTTPException(status_code=500, detail='Failed to clear thread goal')；return: ThreadGoalResponse(goal=None)
  - 调用: get_checkpointer, goal_thread_lock, write_thread_goal, ThreadGoalResponse, exception, sanitize_log_param, HTTPException, delete, require_permission

#### `ƒ` `_thread_compact_response(result: ThreadCompactionResult) -> ThreadCompactResponse`  L883
  - 分支数 0，函数体节点数 51；return: ThreadCompactResponse(thread_id=result.thread_id, compacted=result.compacted, reason=result.reason, removed_message_count=result.removed_message_count, preserved_message_count=result.preserved_message_count, summary_updated=result.summary_updated, checkpoint_id=result.checkpoint_id, total_tokens=result.total_tokens)
  - 调用: ThreadCompactResponse

#### `⏵ƒ` `async compact_thread(thread_id: str, body: ThreadCompactRequest, request: Request) -> ThreadCompactResponse`    @router.post(...), require_permission(...)  L898
  - _文档首行_（仅供参考）: Manually summarize old thread context while preserving the visible history.
  - 分支数 3，函数体节点数 196；raise: HTTPException(status_code=409, detail='Thread has a run in flight. Compact after the run finishes.'), HTTPException(status_code=409, detail='Context compaction is disabled.'), HTTPException(status_code=500, detail='Failed to compact thread context.'), HTTPException(status_code=404, detail=f'Thread {thread_id} not found'), bare raise；return: _thread_compact_response(result)
  - 调用: get_run_manager, get_checkpointer, to_tuple, goal_thread_lock, has_inflight, HTTPException, compact_thread_context, get_effective_user_id, exception, sanitize_log_param, _thread_compact_response, post, require_permission

#### `⏵ƒ` `async get_thread_state(thread_id: str, request: Request) -> ThreadStateResponse`    @router.get(...), require_permission(...)  L932
  - _文档首行_（仅供参考）: Get the latest state snapshot for a thread.
  - 分支数 4，函数体节点数 316；raise: HTTPException(status_code=500, detail='Failed to get thread state'), HTTPException(status_code=404, detail=f'Thread {thread_id} not found')；return: ThreadStateResponse(values=values, next=next_tasks, metadata=metadata, checkpoint={'id': checkpoint_id, 'ts': coerce_iso(metadata.get('created_at', ''))}, checkpoint_id=checkpoint_id, parent_checkpoint_id=parent_checkpoint_id, created_at=coerce_iso(metadata.get('created_at', '')), tasks=tasks)
  - 调用: get_checkpointer, aget_tuple, exception, sanitize_log_param, HTTPException, getattr, get, hasattr, serialize_channel_values_for_api, ThreadStateResponse, coerce_iso, require_permission
  - 反射: getattr (L950), getattr (L951), getattr (L953), getattr (L959), getattr (L964), hasattr (L965), getattr (L966), getattr (L966)

#### `⏵ƒ` `async update_thread_state(thread_id: str, body: ThreadStateUpdateRequest, request: Request) -> ThreadStateResponse`    @router.post(...), require_permission(...)  L984
  - _文档首行_（仅供参考）: Update thread state (e.g. for human-in-the-loop resume or title rename).
  - 分支数 10，函数体节点数 484；raise: HTTPException(status_code=500, detail='Failed to get thread state'), HTTPException(status_code=404, detail=f'Thread {thread_id} not found'), HTTPException(status_code=500, detail='Failed to update thread state')；return: ThreadStateResponse(values=serialize_channel_values_for_api(channel_values), next=[], metadata=metadata, checkpoint_id=new_checkpoint_id, created_at=coerce_iso(metadata.get('created_at', '')))
  - 调用: get_checkpointer, get_thread_store, aget_tuple, exception, sanitize_log_param, HTTPException, dict, getattr, get, update, now_iso, str, uuid6, aput, isinstance, update_display_name, debug, ThreadStateResponse, serialize_channel_values_for_api, coerce_iso（+2）
  - 反射: getattr (L1019), getattr (L1020)

#### `ƒ` `_ai_message_lacks_duration(message: dict[str, Any]) -> bool`  L1084
  - 分支数 0，函数体节点数 52；return: message.get('type') == 'ai' and (not isinstance(additional_kwargs, dict) or 'turn_duration' not in additional_kwargs)
  - 调用: get, isinstance

#### `ƒ` `_checkpoint_run_durations(metadata: Any) -> dict[str, int]`  L1089
  - 分支数 1，函数体节点数 70；return: {}, {run_id: duration_seconds for run_id, duration_seconds in raw_durations.items() if valid_duration_entry(run_id, duration_seconds)}
  - 调用: isinstance, get, items, valid_duration_entry

#### `ƒ` `_set_message_turn_duration(message: dict[str, Any], run_id: str, run_durations: dict[str, int]) -> None`  L1096
  - 分支数 2，函数体节点数 91；return: None
  - 调用: get, isinstance, setdefault

#### `⏵ƒ` `async get_thread_history(thread_id: str, body: ThreadHistoryRequest, request: Request, background_tasks: BackgroundTasks) -> list[HistoryEntry]`    @router.post(...), require_permission(...)  L1108
  - _文档首行_（仅供参考）: Get checkpoint history for a thread.
  - 分支数 25，函数体节点数 850；raise: HTTPException(status_code=500, detail='Failed to get thread history')；return: entries
  - 调用: get_checkpointer, alist, getattr, get, serialize_channel_values_for_api, _checkpoint_run_durations, isinstance, setdefault, _set_message_turn_duration, any, _ai_message_lacks_duration, get_run_manager, get_run_event_store, list_by_thread, list_messages, compute_run_durations, add_task, warning, hasattr, items（+8）
  - 反射: getattr (L1132), getattr (L1133), getattr (L1134), getattr (L1135), getattr (L1236), hasattr (L1237)

## 类
### 类 `ThreadDeleteResponse`  L230
- 继承: BaseModel
- _文档首行_: Response model for thread cleanup.
- 类/实例变量:
  - `success` = <annotated>
  - `message` = <annotated>

### 类 `ThreadResponse`  L237
- 继承: BaseModel
- _文档首行_: Response model for a single thread.
- 类/实例变量:
  - `thread_id` = Field(description='Unique thread identifier')
  - `status` = Field(default='idle', description='Thread status: idle, b...
  - `created_at` = Field(default='', description='ISO timestamp')
  - `updated_at` = Field(default='', description='ISO timestamp')
  - `metadata` = Field(default_factory=dict, description='Thread metadata')
  - `values` = Field(default_factory=dict, description='Current state ch...
  - `interrupts` = Field(default_factory=dict, description='Pending interrup...

### 类 `ThreadCreateRequest`  L249
- 继承: BaseModel
- _文档首行_: Request body for creating a thread.
- 类/实例变量:
  - `thread_id` = Field(default=None, description='Optional thread ID (auto...
  - `assistant_id` = Field(default=None, description='Associate thread with an...
  - `metadata` = Field(default_factory=dict, description='Initial metadata')
  - `_strip_reserved` = field_validator('metadata')(classmethod(lambda cls, v: _s...

### 类 `ThreadSearchRequest`  L259
- 继承: BaseModel
- _文档首行_: Request body for searching threads.
- 类/实例变量:
  - `metadata` = Field(default_factory=dict, description='Metadata filter ...
  - `limit` = Field(default=100, ge=1, le=1000, description='Maximum re...
  - `offset` = Field(default=0, ge=0, description='Pagination offset')
  - `status` = Field(default=None, description='Filter by thread status')
- 方法:
  #### `cls` `_validate_metadata_filters(cls, v: dict[str, Any]) -> dict[str, Any]`    @field_validator(...), classmethod  L269
    - _文档首行_（仅供参考）: Reject filter entries the SQL backend cannot compile.
    - 分支数 5，函数体节点数 132；raise: ValueError(f"Invalid metadata filter entries: {', '.join(bad_entries)}")；return: v
    - 调用: items, validate_metadata_filter_key, append, validate_metadata_filter_value, type, ValueError, join, field_validator

### 类 `ThreadStateResponse`  L290
- 继承: BaseModel
- _文档首行_: Response model for thread state.
- 类/实例变量:
  - `values` = Field(default_factory=dict, description='Current channel ...
  - `next` = Field(default_factory=list, description='Next tasks to ex...
  - `metadata` = Field(default_factory=dict, description='Checkpoint metad...
  - `checkpoint` = Field(default_factory=dict, description='Checkpoint info')
  - `checkpoint_id` = Field(default=None, description='Current checkpoint ID')
  - `parent_checkpoint_id` = Field(default=None, description='Parent checkpoint ID')
  - `created_at` = Field(default=None, description='Checkpoint timestamp')
  - `tasks` = Field(default_factory=list, description='Interrupted task...

### 类 `ThreadPatchRequest`  L303
- 继承: BaseModel
- _文档首行_: Request body for patching thread metadata.
- 类/实例变量:
  - `metadata` = Field(default_factory=dict, description='Metadata to merge')
  - `_strip_reserved` = field_validator('metadata')(classmethod(lambda cls, v: _s...

### 类 `ThreadStateUpdateRequest`  L311
- 继承: BaseModel
- _文档首行_: Request body for updating thread state (human-in-the-loop resume).
- 类/实例变量:
  - `values` = Field(default=None, description='Channel values to merge')
  - `checkpoint_id` = Field(default=None, description='Checkpoint to branch from')
  - `checkpoint` = Field(default=None, description='Full checkpoint object')
  - `as_node` = Field(default=None, description='Node identity for the up...

### 类 `ThreadGoalRequest`  L320
- 继承: BaseModel
- _文档首行_: Request body for setting a thread-scoped goal.
- 类/实例变量:
  - `objective` = Field(..., min_length=1, max_length=4000, description='Co...
  - `max_continuations` = Field(default=DEFAULT_MAX_GOAL_CONTINUATIONS, ge=0, le=DE...

### 类 `ThreadGoalResponse`  L332
- 继承: BaseModel
- _文档首行_: Response model for a thread goal.
- 类/实例变量:
  - `goal` = Field(default=None, description='Current goal state, or n...

### 类 `ThreadCompactRequest`  L338
- 继承: BaseModel
- _文档首行_: Request body for manually compacting a thread's active context.
- 类/实例变量:
  - `force` = Field(default=True, description='Run compaction even if a...
  - `keep` = Field(default=None, description='Optional retention polic...
  - `agent_name` = Field(default=None, max_length=128, description='Optional...

### 类 `ThreadCompactResponse`  L346
- 继承: BaseModel
- _文档首行_: Response model for manual thread-context compaction.
- 类/实例变量:
  - `thread_id` = <annotated>
  - `compacted` = <annotated>
  - `reason` = None
  - `removed_message_count` = 0
  - `preserved_message_count` = 0
  - `summary_updated` = False
  - `checkpoint_id` = None
  - `total_tokens` = 0

### 类 `HistoryEntry`  L359
- 继承: BaseModel
- _文档首行_: Single checkpoint history entry.
- 类/实例变量:
  - `checkpoint_id` = <annotated>
  - `parent_checkpoint_id` = None
  - `metadata` = Field(default_factory=dict)
  - `values` = Field(default_factory=dict)
  - `created_at` = None
  - `next` = Field(default_factory=list)

### 类 `ThreadHistoryRequest`  L370
- 继承: BaseModel
- _文档首行_: Request body for checkpoint history.
- 类/实例变量:
  - `limit` = Field(default=10, ge=1, le=100, description='Maximum entr...
  - `before` = Field(default=None, description='Cursor for pagination')

### 类 `ThreadBranchRequest`  L377
- 继承: BaseModel
- _文档首行_: Request body for creating a branch from a completed assistant turn.
- 类/实例变量:
  - `message_id` = Field(..., min_length=1, description='Target assistant me...
  - `message_ids` = Field(default_factory=list, description='All assistant me...
  - `title` = Field(default=None, max_length=256, description='Optional...

### 类 `ThreadBranchResponse`  L385
- 继承: BaseModel
- _文档首行_: Response model for a thread branch.
- 类/实例变量:
  - `thread_id` = <annotated>
  - `parent_thread_id` = <annotated>
  - `parent_checkpoint_id` = <annotated>
  - `branched_from_message_id` = <annotated>
  - `workspace_clone_mode` = <annotated>

## 文件内调用关系
- `_is_branch_visible_message` -> _message_additional_kwargs, _message_type
- `_is_branch_assistant_message` -> _message_type
- `_matches_branch_target` -> _message_id, _is_branch_assistant_message, _is_branch_visible_message
- `_find_branch_checkpoint` -> _matches_branch_target, _checkpoint_messages
- `_branch_targets_latest_turn` -> _checkpoint_messages, _matches_branch_target
- `delete_thread_data` -> _delete_thread_data
- `create_thread` -> _resolve_existing_thread, _existing_thread_response
- `branch_thread` -> _find_branch_checkpoint, _checkpoint_id, _branch_targets_latest_turn, _default_branch_display_name, _copy_branch_user_data
- `get_thread` -> _derive_thread_status
- `set_thread_goal` -> _ensure_thread_for_goal
- `compact_thread` -> _thread_compact_response
- `get_thread_history` -> _checkpoint_run_durations, _set_message_turn_duration, _ai_message_lacks_duration

# `backend/packages/harness/deerflow/runtime/runs/worker.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/runs/worker.py`  ·  行数: 1576

**模块文档首行**（仅供参考）: Background agent execution.

## 模块概览
- 函数 34 个，类 2 个，模块级常量 4 个

## 依赖（import）
- 模块: asyncio, copy, inspect, logging, os, threading, weakref
- `__future__` -> annotations
- `collections.abc` -> AsyncIterator
- `contextlib` -> asynccontextmanager
- `dataclasses` -> dataclass, field
- `datetime` -> datetime
- `functools` -> lru_cache
- `typing` -> Any, Literal, cast
- `langgraph.checkpoint.base` -> empty_checkpoint
- `deerflow.agents.goal_state` -> GoalEvaluation, GoalState
- `deerflow.config.app_config` -> AppConfig
- `deerflow.runtime.context_keys` -> CURRENT_RUN_PRE_EXISTING_MESSAGE_IDS_KEY
- `deerflow.runtime.goal` -> DEFAULT_MAX_GOAL_CONTINUATIONS, DEFAULT_MAX_NO_PROGRESS_CONTINUATIONS, GoalWriteConflict, _call_checkpointer_method, _is_visible_message, _message_type, attach_goal_evaluation, compute_no_progress_count, create_goal_evaluator_model, evaluate_goal_completion, goal_thread_lock, latest_visible_assistant_signature, make_goal_continuation_message, read_thread_goal, should_continue_goal, visible_conversation_signature, write_thread_goal
- `deerflow.runtime.serialization` -> serialize
- `deerflow.runtime.stream_bridge` -> StreamBridge
- `deerflow.runtime.user_context` -> get_effective_user_id, resolve_runtime_user_id
- `deerflow.trace_context` -> DEERFLOW_TRACE_METADATA_KEY, is_trace_id_from_request_header, resolve_deerflow_trace_id
- `deerflow.tracing` -> inject_langfuse_metadata
- `deerflow.utils.messages` -> message_to_text
- `deerflow.workspace_changes` -> capture_workspace_snapshot, record_workspace_changes
- `deerflow.workspace_changes.types` -> WorkspaceSnapshot
- `.manager` -> RunManager, RunRecord
- `.naming` -> resolve_root_run_name
- `.schemas` -> RunStatus

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_checkpoint_locks_guard` = threading.Lock()
- `_checkpoint_locks_by_loop` = weakref.WeakKeyDictionary()
- `_VALID_LG_MODES` = {'values', 'updates', 'checkpoints', 'tasks', 'debug', 'm...

## 函数
#### `⏵ƒ` `async _checkpoint_thread_lock(thread_id: str) -> AsyncIterator[None]`    @asynccontextmanager  L80
  - _文档首行_（仅供参考）: Serialize checkpoint mutations for one thread without blocking goal commands.
  - 分支数 4，函数体节点数 94；生成器（yield）
  - 调用: get_running_loop, get, Lock

#### `ƒ` `_build_runtime_context(thread_id: str, run_id: str, caller_context: Any | None, app_config: AppConfig | None) -> dict[str, Any]`  L101
  - _文档首行_（仅供参考）: Build the dict that becomes ``ToolRuntime.context`` for the run.
  - 分支数 4，函数体节点数 108；return: runtime_ctx
  - 调用: isinstance, items, setdefault

#### `ƒ` `_install_runtime_context(config: dict, runtime_context: dict[str, Any]) -> None`  L148
  - 分支数 4，函数体节点数 128；return: None
  - 调用: get, isinstance, setdefault, dict

#### `ƒ` `_compute_agent_factory_supports_app_config(agent_factory: Any) -> bool`  L164
  - 分支数 1，函数体节点数 30；return: 'app_config' in inspect.signature(agent_factory).parameters, False
  - 调用: signature

#### `ƒ` `_cached_agent_factory_supports_app_config(agent_factory: Any) -> bool`    @lru_cache(...)  L172
  - 分支数 0，函数体节点数 18；return: _compute_agent_factory_supports_app_config(agent_factory)
  - 调用: _compute_agent_factory_supports_app_config, lru_cache

#### `ƒ` `_agent_factory_supports_app_config(agent_factory: Any) -> bool`  L176
  - 分支数 1，函数体节点数 23；return: _cached_agent_factory_supports_app_config(agent_factory), _compute_agent_factory_supports_app_config(agent_factory)
  - 调用: _cached_agent_factory_supports_app_config, _compute_agent_factory_supports_app_config

#### `⏵ƒ` `async run_agent(bridge: StreamBridge, run_manager: RunManager, record: RunRecord, *, ctx: RunContext, agent_factory: Any, graph_input: dict, config: dict, stream_modes: list[str] | None, stream_subgraphs: bool, interrupt_before: list[str] | Literal['*'] | None, interrupt_after: list[str] | Literal['*'] | None) -> None`  L246
  - _文档首行_（仅供参考）: Execute an agent in the background, publishing events to *bridge*.
  - 分支数 67，函数体节点数 2453；return: RunnableConfig(**continuation_config), goal_evaluator_model, None
  - 调用: set, info, wait_for_prior_finalizing, RunJournal, getattr, update_run_progress, set_status, get_effective_user_id, capture_workspace_snapshot, warning, aget_tuple, get, deepcopy, _collect_pre_existing_message_ids, publish, _build_runtime_context, frozenset, isinstance, resolve_deerflow_trace_id, is_trace_id_from_request_header（+51）
  - 文件IO: replace (L687), replace (L688)
  - 反射: getattr (L313), getattr (L336), getattr (L340), getattr (L341), getattr (L342), getattr (L430), getattr (L676)

#### `ƒ` `_checkpoint_id(checkpoint_tuple: Any) -> str | None`  L727
  - 分支数 2，函数体节点数 113；return: checkpoint_id, checkpoint['id'], None
  - 调用: getattr, isinstance, get
  - 反射: getattr (L728), getattr (L733)

#### `ƒ` `_goal_instance_matches(left: GoalState | None, right: GoalState | None) -> bool`  L739
  - 分支数 1，函数体节点数 91；return: False, same_status and same_objective and same_created_at
  - 调用: get

#### `ƒ` `_read_checkpoint_messages(checkpoint_tuple: Any) -> list[Any]`  L748
  - 分支数 0，函数体节点数 77；return: messages if isinstance(messages, list) else []
  - 调用: getattr, isinstance, get
  - 反射: getattr (L749)

#### `ƒ` `_read_checkpoint_goal(checkpoint_tuple: Any) -> GoalState | None`  L755
  - 分支数 0，函数体节点数 77；return: copy.deepcopy(raw_goal) if isinstance(raw_goal, dict) else None
  - 调用: getattr, isinstance, get, deepcopy
  - 反射: getattr (L756)

#### `ƒ` `_has_durable_goal_turn_receipt(checkpoint_tuple: Any, messages: list[Any]) -> bool`  L762
  - _文档首行_（仅供参考）: Return true when a completed visible assistant turn is safely checkpointed.
  - 分支数 5，函数体节点数 92；return: False, _message_type(visible_messages[-1]) == 'ai'
  - 调用: _checkpoint_id, getattr, _is_visible_message, strip, message_to_text, append, _message_type
  - 反射: getattr (L771)

#### `ƒ` `_stand_down_reason(goal: GoalState, evaluation: GoalEvaluation, no_progress_count: int) -> str | None`  L782
  - 分支数 4，函数体节点数 88；return: None, f"blocked:{evaluation['blocker']}", 'max_continuations_reached', 'no_progress_detected'
  - 调用: int, get

#### `⏵ƒ` `async _persist_goal_evaluation(*, bridge: StreamBridge, checkpointer: Any, thread_id: str, run_id: str, goal: GoalState, evaluation: GoalEvaluation, no_progress_count: int, continuation_count: int | None, stand_down_reason: str | None, evidence_signature: str) -> GoalState | None`  L796
  - 分支数 5，函数体节点数 232；return: None, updated_goal
  - 调用: goal_thread_lock, _call_checkpointer_method, _read_checkpoint_goal, _goal_instance_matches, int, get, max, _checkpoint_id, attach_goal_evaluation, write_thread_goal, publish, serialize, warning

#### `⏵ƒ` `async _reread_goal_and_checkpoint(checkpointer: Any, thread_id: str) -> tuple[GoalState | None, Any]`  L854
  - _文档首行_（仅供参考）: Re-read the goal and latest checkpoint together for a concurrency re-check.
  - 分支数 0，函数体节点数 60；return: (goal, checkpoint_tuple)
  - 调用: read_thread_goal, _call_checkpointer_method

#### `⏵ƒ` `async _prepare_goal_continuation_input(*, bridge: StreamBridge, checkpointer: Any, thread_id: str, run_id: str, model_name: str | None, app_config: AppConfig | None, evaluator_model_factory: Any | None, abort_event: asyncio.Event | None, user_id: str | None, deerflow_trace_id: str | None) -> dict[str, Any] | None`  L866
  - _文档首行_（仅供参考）: Evaluate the active goal and return a hidden continuation input if needed.
  - 分支数 22，函数体节点数 855；return: None, await _persist_goal_evaluation(bridge=bridge, checkpointer=checkpointer, thread_id=thread_id, run_id=run_id, goal=goal, evaluation=evaluation, no_progress_count=no_progress_count, continuation_count=continuation_count, stand_down_reason=stand_down_reason, evidence_signature=evidence_signature), {'messages': [make_goal_continuation_message(updated_goal, evaluation)]}
  - 调用: is_set, read_thread_goal, warning, get, _persist_goal_evaluation, _call_checkpointer_method, _checkpoint_id, _read_checkpoint_messages, visible_conversation_signature, latest_visible_assistant_signature, _has_durable_goal_turn_receipt, GoalEvaluation, compute_no_progress_count, _persist, evaluator_model_factory, evaluate_goal_completion, _reread_goal_and_checkpoint, _goal_instance_matches, goal_thread_lock, _read_checkpoint_goal（+8）

#### `⏵ƒ` `async _rollback_to_pre_run_checkpoint(*, checkpointer: Any, thread_id: str, run_id: str, pre_run_checkpoint_id: str | None, pre_run_snapshot: dict[str, Any] | None, snapshot_capture_failed: bool) -> None`  L1058
  - _文档首行_（仅供参考）: Restore thread state to the checkpoint snapshot captured before run start.
  - 分支数 14，函数体节点数 581；raise: RuntimeError(f'Run {run_id} rollback restore returned invalid config: expected dict'), RuntimeError(f'Run {run_id} rollback restore returned invalid config payload'), RuntimeError(f'Run {run_id} rollback restore did not return checkpoint_id'), RuntimeError(f'Run {run_id} rollback failed: pending_write is not a 3-tuple: {item!r}'), RuntimeError(f'Run {run_id} rollback failed: pending_write has non-string channel: task_id={task_id!r}, channel={channel!r}')；return: None
  - 调用: info, warning, _call_checkpointer_method, get, isinstance, _new_checkpoint_marker, dict, RuntimeError, len, append, setdefault, str, items

#### `ƒ` `_new_checkpoint_marker() -> dict[str, str]`  L1151
  - 分支数 0，函数体节点数 32；return: {'id': marker['id'], 'ts': marker['ts']}
  - 调用: empty_checkpoint

#### `ƒ` `_bump_channel_version(checkpointer: Any, current_version: Any) -> Any`  L1156
  - _文档首行_（仅供参考）: Return a strictly-different next version for a checkpoint channel.
  - 分支数 8，函数体节点数 139；return: next_version, int(current_version) + 1, current_version + 1, current_version + 1.0, str(int(current_version) + 1), f'{current_version}.1', 1
  - 调用: getattr, callable, get_next_version, isinstance, int, str
  - 反射: getattr (L1168)

#### `ƒ` `_checkpoint_identity(ckpt_tuple: Any | None, checkpoint: dict[str, Any]) -> str | None`  L1196
  - 分支数 2，函数体节点数 113；return: checkpoint_id, checkpoint_id if isinstance(checkpoint_id, str) and checkpoint_id else None
  - 调用: getattr, isinstance, get
  - 反射: getattr (L1197)

#### `ƒ` `_checkpoint_namespace(ckpt_tuple: Any | None) -> str`  L1207
  - 分支数 0，函数体节点数 73；return: checkpoint_ns if isinstance(checkpoint_ns, str) else ''
  - 调用: getattr, isinstance, get
  - 反射: getattr (L1208)

#### `ƒ` `_graph_input_messages(graph_input: Any | None) -> list[Any]`  L1214
  - 分支数 3，函数体节点数 64；return: [], messages, list(messages)
  - 调用: isinstance, get, list

#### `ƒ` `_title_generation_state(channel_values: dict[str, Any], graph_input: Any | None) -> dict[str, Any]`  L1225
  - 分支数 2，函数体节点数 73；return: state
  - 调用: dict, get, _graph_input_messages

#### `ƒ` `valid_duration_entry(run_id: Any, duration_seconds: Any) -> bool`  L1235
  - _文档首行_（仅供参考）: Check that (run_id, duration_seconds) is a well-formed duration entry.
  - 分支数 0，函数体节点数 43；return: isinstance(run_id, str) and bool(run_id) and isinstance(duration_seconds, int) and (not isinstance(duration_seconds, bool))
  - 调用: isinstance, bool

#### `⏵ƒ` `async persist_run_durations(*, checkpointer: Any, thread_id: str, durations: dict[str, int]) -> bool`  L1240
  - _文档首行_（仅供参考）: Merge validated run durations into a metadata-only checkpoint.
  - 分支数 6，函数体节点数 400；return: False, True
  - 调用: max, items, valid_duration_entry, _checkpoint_thread_lock, range, _call_checkpointer_method, dict, getattr, get, isinstance, update, _checkpoint_identity, _new_checkpoint_marker, sorted, _checkpoint_namespace
  - 反射: getattr (L1264), getattr (L1265), getattr (L1275)

#### `⏵ƒ` `async _persist_run_duration(*, checkpointer: Any, thread_id: str, run_id: str, duration_seconds: int) -> None`  L1307
  - _文档首行_（仅供参考）: Persist one completed run duration in the thread checkpoint metadata.
  - 分支数 0，函数体节点数 34
  - 调用: persist_run_durations

#### `⏵ƒ` `async _ensure_interrupted_title(*, checkpointer: Any, thread_id: str, app_config: AppConfig | None, graph_input: Any | None) -> str | None`  L1322
  - _文档首行_（仅供参考）: Persist a local fallback title for interrupted first-turn runs.
  - 分支数 7，函数体节点数 500；return: existing_title, None, title
  - 调用: TitleMiddleware, range, _call_checkpointer_method, deepcopy, getattr, empty_checkpoint, dict, get, _generate_title_result, _title_generation_state, isinstance, _checkpoint_identity, _new_checkpoint_marker, update, _bump_channel_version, _checkpoint_namespace
  - 反射: getattr (L1337), getattr (L1352), getattr (L1382)

#### `ƒ` `_lg_mode_to_sse_event(mode: str) -> str`  L1404
  - _文档首行_（仅供参考）: Map LangGraph internal stream_mode name to SSE event name.
  - 分支数 0，函数体节点数 12；return: mode

#### `ƒ` `_error_fallback_message_from_metadata(metadata: dict[str, Any], content: Any) -> str`  L1416
  - 分支数 3，函数体节点数 105；return: detail.strip(), reason.strip(), content.strip()[:2000], 'LLM provider failed after retries'
  - 调用: get, isinstance, strip

#### `ƒ` `_message_id(obj: Any) -> str | None`  L1428
  - _文档首行_（仅供参考）: Best-effort extraction of a stable message id from a message-like object.
  - 分支数 3，函数体节点数 71；return: msg_id, raw, None
  - 调用: getattr, isinstance, get
  - 反射: getattr (L1430)

#### `ƒ` `_try_extract_from_message(obj: Any, pre_existing_ids: set[str] | None) -> str | None`  L1440
  - _文档首行_（仅供参考）: Try to extract fallback marker from a single message object or dict.
  - 分支数 5，函数体节点数 136；return: None, _error_fallback_message_from_metadata(additional_kwargs, getattr(obj, 'content', None)), _error_fallback_message_from_metadata(nested_kwargs, obj.get('content'))
  - 调用: _message_id, getattr, isinstance, get, _error_fallback_message_from_metadata
  - 反射: getattr (L1455), getattr (L1457)

#### `ƒ` `_extract_llm_error_fallback_message(value: Any, pre_existing_ids: set[str] | None) -> str | None`  L1466
  - _文档首行_（仅供参考）: Find LLM fallback markers in streamed LangGraph chunks.
  - 分支数 12，函数体节点数 223；return: result, None, walk(value)
  - 调用: isinstance, get, _try_extract_from_message, set, id, add, values, walk

#### `ƒ` `_collect_pre_existing_message_ids(snapshot: dict[str, Any] | None) -> set[str]`  L1525
  - _文档首行_（仅供参考）: Pull stable message ids out of a pre-run checkpoint snapshot.
  - 分支数 6，函数体节点数 153；return: set(), ids
  - 调用: isinstance, set, get, _message_id, add

#### `ƒ` `_unpack_stream_item(item: Any, lg_modes: list[str], stream_subgraphs: bool) -> tuple[str | None, Any]`  L1552
  - _文档首行_（仅供参考）: Unpack a multi-mode or subgraph stream item into (mode, chunk).
  - 分支数 4，函数体节点数 165；return: (str(mode), chunk), (None, None), (lg_modes[0] if lg_modes else None, item)
  - 调用: isinstance, len, str

## 类
### 类 `RunContext`  L131  @dataclass(...)
- _文档首行_: Infrastructure dependencies for a single agent run.
- 类/实例变量:
  - `checkpointer` = <annotated>
  - `store` = field(default=None)
  - `event_store` = field(default=None)
  - `run_events_config` = field(default=None)
  - `thread_store` = field(default=None)
  - `app_config` = field(default=None)
  - `on_run_completed` = field(default=None)

### 类 `_SubagentEventBuffer`  L184
- _文档首行_: Buffer subagent ``task_*`` step events and flush them in one locked batch (#3779).
- 类/实例变量:
  - `FLUSH_THRESHOLD` = 25
- 方法:
  #### `m` `__init__(self, event_store: Any | None, thread_id: str, run_id: str) -> None`  L208
    - 分支数 0，函数体节点数 58
  #### `⏵m` `async add(self, chunk: Any) -> None`  L214
    - _文档首行_（仅供参考）: Buffer one custom stream chunk; flush on a terminal event or threshold.
    - 分支数 3，函数体节点数 87；return: None
    - 调用: subagent_run_event, append, len, flush
  #### `⏵m` `async flush(self) -> None`  L231
    - _文档首行_（仅供参考）: Persist buffered events in one ``put_batch`` call; swallow store errors.
    - 分支数 2，函数体节点数 83；return: None
    - 调用: put_batch, warning, len

## 文件内调用关系
- `_cached_agent_factory_supports_app_config` -> _compute_agent_factory_supports_app_config
- `_agent_factory_supports_app_config` -> _cached_agent_factory_supports_app_config, _compute_agent_factory_supports_app_config
- `run_agent` -> _collect_pre_existing_message_ids, _build_runtime_context, _install_runtime_context, _agent_factory_supports_app_config, add, _checkpoint_thread_lock, _extract_llm_error_fallback_message, _lg_mode_to_sse_event, _unpack_stream_item, _prepare_goal_continuation_input, _rollback_to_pre_run_checkpoint, flush, _ensure_interrupted_title, _persist_run_duration
- `_has_durable_goal_turn_receipt` -> _checkpoint_id
- `_persist_goal_evaluation` -> _read_checkpoint_goal, _goal_instance_matches, _checkpoint_id
- `_prepare_goal_continuation_input` -> _persist_goal_evaluation, _checkpoint_id, _read_checkpoint_messages, _has_durable_goal_turn_receipt, _reread_goal_and_checkpoint, _goal_instance_matches, _read_checkpoint_goal, _stand_down_reason
- `_rollback_to_pre_run_checkpoint` -> _new_checkpoint_marker
- `_title_generation_state` -> _graph_input_messages
- `persist_run_durations` -> valid_duration_entry, _checkpoint_thread_lock, _checkpoint_identity, _new_checkpoint_marker, _checkpoint_namespace
- `_persist_run_duration` -> persist_run_durations
- `_ensure_interrupted_title` -> _title_generation_state, _checkpoint_identity, _new_checkpoint_marker, _bump_channel_version, _checkpoint_namespace
- `_try_extract_from_message` -> _message_id, _error_fallback_message_from_metadata
- `_extract_llm_error_fallback_message` -> _try_extract_from_message, add
- `_collect_pre_existing_message_ids` -> _message_id, add
- `_SubagentEventBuffer.add` -> flush

# `backend/packages/harness/deerflow/agents/middlewares/loop_detection_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/loop_detection_middleware.py`  ·  行数: 733

**模块文档首行**（仅供参考）: Middleware to detect and break repetitive tool call loops.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 12 个

## 依赖（import）
- 模块: hashlib, json, logging, threading
- `__future__` -> annotations
- `collections` -> Counter, OrderedDict, defaultdict, deque
- `collections.abc` -> Awaitable, Callable
- `copy` -> deepcopy
- `typing` -> TYPE_CHECKING, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> HumanMessage
- `langgraph.runtime` -> Runtime
- `deerflow.agents.middlewares._bounded_dict` -> BoundedDict

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_DEFAULT_WARN_THRESHOLD` = 3
- `_DEFAULT_HARD_LIMIT` = 5
- `_DEFAULT_WINDOW_SIZE` = 20
- `_DEFAULT_MAX_TRACKED_THREADS` = 100
- `_DEFAULT_TOOL_FREQ_WARN` = 30
- `_DEFAULT_TOOL_FREQ_HARD_LIMIT` = 50
- `_MAX_PENDING_WARNINGS_PER_RUN` = 4
- `_WARNING_MSG` = '[LOOP DETECTED] You are repeating the same tool calls. S...
- `_TOOL_FREQ_WARNING_MSG` = '[LOOP DETECTED] You have called {tool_name} {count} time...
- `_HARD_STOP_MSG` = '[FORCED STOP] Repeated tool calls exceeded the safety li...
- `_TOOL_FREQ_HARD_STOP_MSG` = '[FORCED STOP] Tool {tool_name} called {count} times — ex...

## 函数
#### `ƒ` `_normalize_tool_call_args(raw_args: object) -> tuple[dict, str | None]`  L86
  - _文档首行_（仅供参考）: Normalize tool call args to a dict plus an optional fallback key.
  - 分支数 5，函数体节点数 127；return: (raw_args, None), ({}, raw_args), (parsed, None), ({}, json.dumps(parsed, sort_keys=True, default=str)), ({}, None), ({}, json.dumps(raw_args, sort_keys=True, default=str))
  - 调用: isinstance, loads, dumps

#### `ƒ` `_stable_tool_key(name: str, args: dict, fallback_key: str | None) -> str`  L112
  - _文档首行_（仅供参考）: Derive a stable key from salient args without overfitting to noise.
  - 分支数 7，函数体节点数 299；return: f'{path}:{bucket_start}-{bucket_end}', fallback_key, json.dumps(args, sort_keys=True, default=str), json.dumps(stable_args, sort_keys=True, default=str)
  - 调用: get, int, sorted, max, dumps

#### `ƒ` `_hash_tool_calls(tool_calls: list[dict]) -> str`  L155
  - _文档首行_（仅供参考）: Deterministic hash of a set of tool calls (name + stable key).
  - 分支数 1，函数体节点数 121；return: hashlib.md5(blob.encode()).hexdigest()[:12]
  - 调用: get, _normalize_tool_call_args, _stable_tool_key, append, sort, dumps, hexdigest, md5, encode

## 类
### 类 `LoopDetectionMiddleware`  L187
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Detects and breaks repetitive tool call loops.
- 方法:
  #### `cls` `from_config(cls, config: LoopDetectionConfig) -> LoopDetectionMiddleware`    @classmethod  L288
    - _文档首行_（仅供参考）: Construct from a Pydantic-validated config, trusting its validation.
    - 分支数 0，函数体节点数 74；return: cls(warn_threshold=config.warn_threshold, hard_limit=config.hard_limit, window_size=config.window_size, max_tracked_threads=config.max_tracked_threads, tool_freq_warn=config.tool_freq_warn, tool_freq_hard_limit=config.tool_freq_hard_limit, tool_freq_overrides={name: (o.warn, o.hard_limit) for name, o in config.tool_freq_overrides.items()})
    - 调用: cls, items
  #### `st` `_append_text(content: str | list | None, text: str) -> str | list`    @staticmethod  L544
    - _文档首行_（仅供参考）: Append *text* to AIMessage content, handling str, list, and None.
    - 分支数 3，函数体节点数 89；return: text, [*content, {'type': 'text', 'text': f'\n\n{text}'}], content + f'\n\n{text}', str(content) + f'\n\n{text}'
    - 调用: isinstance, str
  #### `st` `_build_hard_stop_update(last_msg, content: str | list) -> dict`    @staticmethod  L561
    - _文档首行_（仅供参考）: Clear tool-call metadata so forced-stop messages serialize as plain assistant text.
    - 分支数 2，函数体节点数 110；return: update
    - 调用: dict, getattr, pop, deepcopy, get
  - 反射: getattr (L568), getattr (L573)
  #### `st` `_format_warning_message(warnings: list[str]) -> str`    @staticmethod  L638
    - _文档首行_（仅供参考）: Merge pending warnings into one prompt message.
    - 分支数 0，函数体节点数 35；return: '\n\n'.join(deduped)
    - 调用: list, fromkeys, join
  #### `m` `__init__(self, warn_threshold: int, hard_limit: int, window_size: int, max_tracked_threads: int, tool_freq_warn: int, tool_freq_hard_limit: int, tool_freq_overrides: dict[str, tuple[int, int]] | None)`  L220
    - 分支数 0，函数体节点数 388
    - 调用: __init__, super, max, values, Lock, OrderedDict, defaultdict, BoundedDict
  #### `m` `_get_thread_id(self, runtime: Runtime) -> str`  L300
    - _文档首行_（仅供参考）: Extract thread_id from runtime context for per-thread tracking.
    - 分支数 1，函数体节点数 38；return: str(thread_id), 'default'
    - 调用: get, str
  #### `m` `_get_run_id(self, runtime: Runtime) -> str`  L307
    - _文档首行_（仅供参考）: Extract run_id from runtime context for per-run warning scoping.
    - 分支数 1，函数体节点数 50；return: ctx['run_id'], str(id(runtime))
    - 调用: getattr, isinstance, str, id
  - 反射: getattr (L327)
  #### `m` `consume_stop_reason(self, run_id: str | None) -> str | None`  L333
    - _文档首行_（仅供参考）: Pop and return the stop reason the hard-stop set for this run.
    - 分支数 1，函数体节点数 33；return: self._stop_reason.pop(run_id, None)
    - 调用: pop
  #### `m` `_pending_key(self, runtime: Runtime) -> tuple[str, str]`  L347
    - _文档首行_（仅供参考）: Return the pending-warning key for the current thread/run.
    - 分支数 0，函数体节点数 35；return: (self._get_thread_id(runtime), self._get_run_id(runtime))
    - 调用: _get_thread_id, _get_run_id
  #### `m` `_evict_if_needed(self) -> None`  L351
    - _文档首行_（仅供参考）: Evict least recently used threads if over the limit.
    - 分支数 3，函数体节点数 106
    - 调用: len, popitem, pop, list, _drop_pending_warning_key_locked, debug
  #### `m` `_drop_pending_warning_key_locked(self, key: tuple[str, str]) -> None`  L366
    - _文档首行_（仅供参考）: Drop all pending-warning bookkeeping for one thread/run key.
    - 分支数 0，函数体节点数 39
    - 调用: pop
  #### `m` `_touch_pending_warning_key_locked(self, key: tuple[str, str]) -> None`  L374
    - _文档首行_（仅供参考）: Mark a pending-warning key as recently used.
    - 分支数 0，函数体节点数 37
    - 调用: move_to_end
  #### `m` `_prune_pending_warning_state_locked(self, protected_key: tuple[str, str]) -> None`  L382
    - _文档首行_（仅供参考）: Cap pending-warning state across abnormal or concurrent runs.
    - 分支数 2，函数体节点数 77；return: None
    - 调用: len, _drop_pending_warning_key_locked
  #### `m` `_queue_pending_warning(self, runtime: Runtime, warning: str) -> None`  L395
    - _文档首行_（仅供参考）: Queue one transient warning for the current thread/run with caps.
    - 分支数 3，函数体节点数 96
    - 调用: _pending_key, append, len, _touch_pending_warning_key_locked, _prune_pending_warning_state_locked
  #### `m` `_track_and_check(self, state: AgentState, runtime: Runtime) -> tuple[str | None, bool]`  L407
    - _文档首行_（仅供参考）: Track tool calls and check for loops.
    - 分支数 19，函数体节点数 656；return: (None, False), (_HARD_STOP_MSG, True), (_WARNING_MSG, False), (_TOOL_FREQ_HARD_STOP_MSG.format(tool_name=name, count=freq_count), True), (_TOOL_FREQ_WARNING_MSG.format(tool_name=name, count=freq_count), False)
    - 调用: get, getattr, _get_thread_id, _hash_tool_calls, move_to_end, _evict_if_needed, append, len, intersection_update, pop, count, error, add, warning, popleft, format, discard
  - 反射: getattr (L424), getattr (L427)
  #### `m` `_apply(self, state: AgentState, runtime: Runtime) -> dict | None`  L580
    - 分支数 4，函数体节点数 165；return: {'messages': [stripped_msg]}, None
    - 调用: _track_and_check, _get_run_id, getattr, isinstance, get, _append_text, model_copy, _build_hard_stop_update, _queue_pending_warning
  - 反射: getattr (L597)
  #### `m` `_clear_other_run_pending_warnings(self, runtime: Runtime) -> None`  L623
    - _文档首行_（仅供参考）: Drop stale pending warnings for previous runs in this thread.
    - 分支数 3，函数体节点数 68
    - 调用: _pending_key, list, _drop_pending_warning_key_locked
  #### `m` `_clear_current_run_pending_warnings(self, runtime: Runtime) -> None`  L631
    - _文档首行_（仅供参考）: Drop pending warnings owned by the current thread/run.
    - 分支数 1，函数体节点数 33
    - 调用: _pending_key, _drop_pending_warning_key_locked
  #### `m` `before_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L644
    - 分支数 0，函数体节点数 26；return: None
    - 调用: _clear_other_run_pending_warnings
  #### `m` `after_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L654
    - 分支数 0，函数体节点数 26；return: self._apply(state, runtime)
    - 调用: _apply
  #### `m` `after_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L662
    - 分支数 0，函数体节点数 26；return: None
    - 调用: _clear_current_run_pending_warnings
  #### `m` `_drain_pending_warnings(self, runtime: Runtime) -> list[str]`  L671
    - _文档首行_（仅供参考）: Pop and return all queued warnings for *runtime*'s thread/run.
    - 分支数 1，函数体节点数 58；return: warnings
    - 调用: _pending_key, pop
  #### `m` `_augment_request(self, request: ModelRequest) -> ModelRequest`  L679
    - _文档首行_（仅供参考）: Append queued loop warnings (if any) to the outgoing message list.
    - 分支数 1，函数体节点数 63；return: request, request.override(messages=new_messages)
    - 调用: _drain_pending_warnings, HumanMessage, _format_warning_message, override
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L699
    - 分支数 0，函数体节点数 34；return: handler(self._augment_request(request))
    - 调用: handler, _augment_request
  #### `m` `reset(self, thread_id: str | None) -> None`  L714
    - _文档首行_（仅供参考）: Clear tracking state. If thread_id given, clear only that thread.
    - 分支数 4，函数体节点数 150
    - 调用: pop, list, _drop_pending_warning_key_locked, clear
  #### `⏵m` `async abefore_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L649
    - 分支数 0，函数体节点数 26；return: None
    - 调用: _clear_other_run_pending_warnings
  #### `⏵m` `async aafter_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L658
    - 分支数 0，函数体节点数 26；return: self._apply(state, runtime)
    - 调用: _apply
  #### `⏵m` `async aafter_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L667
    - 分支数 0，函数体节点数 26；return: None
    - 调用: _clear_current_run_pending_warnings
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L707
    - 分支数 0，函数体节点数 39；return: await handler(self._augment_request(request))
    - 调用: handler, _augment_request

## 文件内调用关系
- `_hash_tool_calls` -> _normalize_tool_call_args, _stable_tool_key
- `LoopDetectionMiddleware.__init__` -> __init__
- `LoopDetectionMiddleware._pending_key` -> _get_thread_id, _get_run_id
- `LoopDetectionMiddleware._evict_if_needed` -> _drop_pending_warning_key_locked
- `LoopDetectionMiddleware._prune_pending_warning_state_locked` -> _drop_pending_warning_key_locked
- `LoopDetectionMiddleware._queue_pending_warning` -> _pending_key, _touch_pending_warning_key_locked, _prune_pending_warning_state_locked
- `LoopDetectionMiddleware._track_and_check` -> _get_thread_id, _hash_tool_calls, _evict_if_needed
- `LoopDetectionMiddleware._apply` -> _track_and_check, _get_run_id, _append_text, _build_hard_stop_update, _queue_pending_warning
- `LoopDetectionMiddleware._clear_other_run_pending_warnings` -> _pending_key, _drop_pending_warning_key_locked
- `LoopDetectionMiddleware._clear_current_run_pending_warnings` -> _pending_key, _drop_pending_warning_key_locked
- `LoopDetectionMiddleware.before_agent` -> _clear_other_run_pending_warnings
- `LoopDetectionMiddleware.abefore_agent` -> _clear_other_run_pending_warnings
- `LoopDetectionMiddleware.after_model` -> _apply
- `LoopDetectionMiddleware.aafter_model` -> _apply
- `LoopDetectionMiddleware.after_agent` -> _clear_current_run_pending_warnings
- `LoopDetectionMiddleware.aafter_agent` -> _clear_current_run_pending_warnings
- `LoopDetectionMiddleware._drain_pending_warnings` -> _pending_key
- `LoopDetectionMiddleware._augment_request` -> _drain_pending_warnings, _format_warning_message
- `LoopDetectionMiddleware.wrap_model_call` -> _augment_request
- `LoopDetectionMiddleware.awrap_model_call` -> _augment_request
- `LoopDetectionMiddleware.reset` -> _drop_pending_warning_key_locked

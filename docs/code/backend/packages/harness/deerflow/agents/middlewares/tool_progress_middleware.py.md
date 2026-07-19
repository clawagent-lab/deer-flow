# `backend/packages/harness/deerflow/agents/middlewares/tool_progress_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/tool_progress_middleware.py`  ·  行数: 579

**模块文档首行**（仅供参考）: Middleware for task-level tool call progress tracking with a state machine.

## 模块概览
- 函数 6 个，类 2 个，模块级常量 3 个

## 依赖（import）
- 模块: logging, re, threading
- `__future__` -> annotations
- `collections` -> OrderedDict, defaultdict
- `collections.abc` -> Awaitable, Callable, Sequence
- `dataclasses` -> dataclass, field, replace
- `typing` -> TYPE_CHECKING, Literal, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> HumanMessage, ToolMessage
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.runtime` -> Runtime
- `langgraph.types` -> Command
- `deerflow.agents.middlewares.tool_result_meta` -> TOOL_META_KEY, ToolResultMeta

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_MAX_PENDING_PER_RUN` = 3
- `_MAX_CONTENT_FOR_WORDSET` = 8192

## 函数
#### `ƒ` `word_set(content: str) -> frozenset[str]`  L100
  - _文档首行_（仅供参考）: Extract lowercase words of length >= 3 for Jaccard similarity.
  - 分支数 0，函数体节点数 33；return: frozenset(re.findall('\\b\\w{3,}\\b', content[:_MAX_CONTENT_FOR_WORDSET].lower()))
  - 调用: frozenset, findall, lower

#### `ƒ` `is_near_duplicate(current: frozenset[str], recent: Sequence[frozenset[str]], threshold: float, min_words: int) -> bool`  L110
  - _文档首行_（仅供参考）: Return True if current is similar to any of the last 3 recent word sets.
  - 分支数 5，函数体节点数 105；return: False, True
  - 调用: len

#### `ƒ` `_message_content_str(msg: ToolMessage) -> str`  L130
  - 分支数 0，函数体节点数 23；return: msg.content if isinstance(msg.content, str) else ''
  - 调用: isinstance

#### `ƒ` `_parse_tool_meta(meta_dict: object) -> ToolResultMeta | None`  L134
  - _文档首行_（仅供参考）: Safely deserialize a ToolResultMeta from a raw dict; returns None on schema mismatch.
  - 分支数 2，函数体节点数 46；return: None, ToolResultMeta(**meta_dict)
  - 调用: isinstance, ToolResultMeta, warning

#### `ƒ` `_format_hint(meta: ToolResultMeta) -> str`  L149
  - 分支数 0，函数体节点数 76；return: f'{base} {suffix}'.strip()
  - 调用: get, strip

#### `ƒ` `_block_reason(meta: ToolResultMeta) -> str`  L175
  - 分支数 0，函数体节点数 34；return: {'no_results': 'Repeated no-results — rewrite your query or try a different tool.', 'not_found': 'Repeated not-found — rewrite your query or try a different resource.', 'rate_limited': 'Repeated rate-limiting — summarize current findings and proceed.', 'transient': 'Repeated transient failures — try a different approach.', 'auth': 'Authentication failure — this tool cannot be used.', 'config': 'Tool is not configured — this tool cannot be used.', 'internal': 'Repeated internal errors — this tool is unavailable.'}.get(meta.error_type or '', 'Tool has not produced new information after multiple attempts — summarize and move on.')
  - 调用: get

## 类
### 类 `ToolPhaseState`  L84  @dataclass(...)
- _文档首行_: Per (thread_id, tool_name) tracking state.
- 类/实例变量:
  - `phase` = 'active'
  - `consecutive_problems` = 0
  - `block_reason` = None
  - `recent_word_sets` = field(default_factory=tuple)

### 类 `ToolProgressMiddleware`  L194
- 继承: AgentMiddleware[AgentState]
- _文档首行_: State-machine-based tool stagnation guard (RFC #3177).
- 方法:
  #### `cls` `from_config(cls, config: ToolProgressConfig) -> ToolProgressMiddleware`    @classmethod  L228
    - 分支数 0，函数体节点数 52；return: cls(stagnation_threshold=config.stagnation_threshold, warn_escalation_count=config.warn_escalation_count, inject_assessment=config.inject_assessment, jaccard_threshold=config.jaccard_similarity_threshold, min_words=config.min_word_count_for_similarity, exempt_tools=set(config.exempt_tools), max_tracked_threads=config.max_tracked_threads)
    - 调用: cls, set
  #### `st` `_thread_id(runtime: Runtime) -> str`    @staticmethod  L243
    - 分支数 0，函数体节点数 36；return: str(tid) if tid else 'default'
    - 调用: get, str
  #### `st` `_run_id(runtime: Runtime) -> str`    @staticmethod  L248
    - 分支数 0，函数体节点数 36；return: str(rid) if rid else 'default'
    - 调用: get, str
  #### `m` `__init__(self, *, stagnation_threshold: int, warn_escalation_count: int, inject_assessment: bool, jaccard_threshold: float, min_words: int, exempt_tools: set[str] | None, max_tracked_threads: int) -> None`  L197
    - 分支数 0，函数体节点数 173
    - 调用: Lock, OrderedDict, defaultdict
  #### `m` `_pending_key(self, runtime: Runtime) -> tuple[str, str]`  L252
    - 分支数 0，函数体节点数 33；return: (self._thread_id(runtime), self._run_id(runtime))
    - 调用: _thread_id, _run_id
  #### `m` `_get_state(self, thread_id: str, tool_name: str) -> ToolPhaseState`  L258
    - 分支数 3，函数体节点数 118；return: self._phase_states[thread_id].get(tool_name, ToolPhaseState())
    - 调用: len, popitem, move_to_end, get, ToolPhaseState
  #### `m` `_set_state(self, thread_id: str, tool_name: str, state: ToolPhaseState) -> None`  L269
    - 分支数 0，函数体节点数 28
  #### `m` `_get_block_reason(self, runtime: Runtime, tool_name: str) -> str | None`  L272
    - 分支数 2，函数体节点数 81；return: None, tool_state.block_reason if tool_state is not None and tool_state.phase == 'blocked' else None
    - 调用: _thread_id, get
  #### `m` `_make_blocked_message(self, request: ToolCallRequest, tool_name: str, block_reason: str) -> ToolMessage`  L284
    - 分支数 0，函数体节点数 57；return: ToolMessage(content=f'[TOOL_BLOCKED] {block_reason}', tool_call_id=str(request.tool_call.get('id', '')), name=tool_name, status='error', additional_kwargs={TOOL_META_KEY: {'status': 'error', 'error_type': 'blocked_by_progress_guard', 'recoverable_by_model': True, 'recommended_next_action': 'summarize', 'source': 'progress_middleware'}})
    - 调用: ToolMessage, str, get
  #### `m` `_update_state_from_result(self, result: ToolMessage | Command, tool_name: str, runtime: Runtime) -> ToolMessage | Command`  L301
    - _文档首行_（仅供参考）: Update the state machine from a tool result; queue hints if warranted.
    - 分支数 9，函数体节点数 246；return: result
    - 调用: isinstance, _parse_tool_meta, get, warning, _message_content_str, _thread_id, _get_state, _assess_and_transition, _set_state, info, _queue_assessment
  #### `m` `_assess_and_transition(self, state: ToolPhaseState, meta: ToolResultMeta, content: str) -> tuple[ToolPhaseState, str | None]`  L352
    - _文档首行_（仅供参考）: Return (new_state, hint_text_or_None).
    - 分支数 6，函数体节点数 309；return: (state, None), (replace(state, phase='blocked', consecutive_problems=new_count, block_reason=_block_reason(meta)), None), (replace(state, consecutive_problems=0, phase='active', recent_word_sets=new_recent), None), (new_state, hint)
    - 调用: replace, _block_reason, word_set, frozenset, is_near_duplicate, _format_hint
  - 文件IO: replace (L380), replace (L395), replace (L404), replace (L408), replace (L411), replace (L413)
  #### `m` `_queue_assessment(self, runtime: Runtime, text: str) -> None`  L420
    - 分支数 3，函数体节点数 73；return: None
    - 调用: _pending_key, len, append
  #### `m` `_drain_pending(self, runtime: Runtime) -> list[str]`  L433
    - 分支数 1，函数体节点数 40；return: self._pending.pop(key, [])
    - 调用: _pending_key, pop
  #### `m` `_clear_stale_pending(self, runtime: Runtime) -> None`  L438
    - 分支数 3，函数体节点数 67
    - 调用: _pending_key, list
  #### `m` `_reset_run_states(self, runtime: Runtime) -> None`  L445
    - _文档首行_（仅供参考）: Reset all per-run tool state for the thread at the start of a new agent run.
    - 分支数 3，函数体节点数 80；return: None
    - 调用: _thread_id, get, list, items, replace
  - 文件IO: replace (L473)
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L485
    - 分支数 3，函数体节点数 149；return: handler(request), self._make_blocked_message(request, tool_name, block_reason), self._update_state_from_result(handler(request), tool_name, runtime)
    - 调用: str, get, handler, getattr, _get_block_reason, info, _thread_id, _make_blocked_message, _update_state_from_result
  - 反射: getattr (L493)
  #### `m` `_augment_request(self, request: ModelRequest) -> ModelRequest`  L533
    - 分支数 1，函数体节点数 96；return: request, request.override(messages=new_messages)
    - 调用: _drain_pending, list, fromkeys, debug, len, _pending_key, HumanMessage, join, override
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L550
    - 分支数 0，函数体节点数 34；return: handler(self._augment_request(request))
    - 调用: handler, _augment_request
  #### `m` `before_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L569
    - 分支数 0，函数体节点数 34；return: None
    - 调用: _clear_stale_pending, _reset_run_states
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L508
    - 分支数 3，函数体节点数 156；return: await handler(request), self._make_blocked_message(request, tool_name, block_reason), self._update_state_from_result(await handler(request), tool_name, runtime)
    - 调用: str, get, handler, getattr, _get_block_reason, info, _thread_id, _make_blocked_message, _update_state_from_result
  - 反射: getattr (L516)
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L558
    - 分支数 0，函数体节点数 39；return: await handler(self._augment_request(request))
    - 调用: handler, _augment_request
  #### `⏵m` `async abefore_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L575
    - 分支数 0，函数体节点数 34；return: None
    - 调用: _clear_stale_pending, _reset_run_states

## 文件内调用关系
- `ToolProgressMiddleware._pending_key` -> _thread_id, _run_id
- `ToolProgressMiddleware._get_block_reason` -> _thread_id
- `ToolProgressMiddleware._update_state_from_result` -> _parse_tool_meta, _message_content_str, _thread_id, _get_state, _assess_and_transition, _set_state, _queue_assessment
- `ToolProgressMiddleware._assess_and_transition` -> _block_reason, word_set, is_near_duplicate, _format_hint
- `ToolProgressMiddleware._queue_assessment` -> _pending_key
- `ToolProgressMiddleware._drain_pending` -> _pending_key
- `ToolProgressMiddleware._clear_stale_pending` -> _pending_key
- `ToolProgressMiddleware._reset_run_states` -> _thread_id
- `ToolProgressMiddleware.wrap_tool_call` -> _get_block_reason, _thread_id, _make_blocked_message, _update_state_from_result
- `ToolProgressMiddleware.awrap_tool_call` -> _get_block_reason, _thread_id, _make_blocked_message, _update_state_from_result
- `ToolProgressMiddleware._augment_request` -> _drain_pending, _pending_key
- `ToolProgressMiddleware.wrap_model_call` -> _augment_request
- `ToolProgressMiddleware.awrap_model_call` -> _augment_request
- `ToolProgressMiddleware.before_agent` -> _clear_stale_pending, _reset_run_states
- `ToolProgressMiddleware.abefore_agent` -> _clear_stale_pending, _reset_run_states

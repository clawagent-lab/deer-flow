# `backend/packages/harness/deerflow/runtime/goal.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/goal.py`  ·  行数: 563

**模块文档首行**（仅供参考）: Thread-scoped goal state and evaluator helpers.

## 模块概览
- 函数 28 个，类 2 个，模块级常量 16 个

## 依赖（import）
- 模块: asyncio, copy, hashlib, inspect, json, logging, os, threading, weakref, llm_text
- `__future__` -> annotations
- `collections.abc` -> AsyncIterator
- `contextlib` -> asynccontextmanager
- `typing` -> Any, Literal, NamedTuple
- `langchain_core.messages` -> HumanMessage, SystemMessage
- `langgraph.checkpoint.base` -> empty_checkpoint, uuid6
- `deerflow.agents.goal_state` -> GoalBlocker, GoalEvaluation, GoalState
- `deerflow.models` -> create_chat_model
- `deerflow.tracing` -> inject_langfuse_metadata
- `deerflow.utils.messages` -> message_to_text
- `deerflow.utils.time` -> now_iso

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_MAX_GOAL_CONTINUATIONS` = 8
- `DEFAULT_MAX_NO_PROGRESS_CONTINUATIONS` = 2
- `MAX_GOAL_OBJECTIVE_CHARS` = 4000
- `MAX_GOAL_REASON_CHARS` = 1000
- `MAX_GOAL_EVIDENCE_CHARS` = 1000
- `MAX_GOAL_CONVERSATION_CHARS` = 12000
- `MAX_GOAL_CONVERSATION_MESSAGES` = 30
- `GOAL_BLOCKERS` = {'none', 'missing_evidence', 'needs_user_input', 'run_fai...
- `CONTINUABLE_GOAL_BLOCKERS` = {'goal_not_met_yet'}
- `GOAL_CLEAR_ALIASES` = frozenset({'clear', 'reset', 'off'})
- `_extract_response_text` = llm_text.extract_response_text
- `_strip_markdown_code_fence` = llm_text.strip_markdown_code_fence
- `_strip_think_blocks` = llm_text.strip_think_blocks
- `_goal_locks_guard` = threading.Lock()
- `_goal_locks_by_loop` = weakref.WeakKeyDictionary()

## 函数
#### `⏵ƒ` `async goal_thread_lock(thread_id: str) -> AsyncIterator[None]`    @asynccontextmanager  L68
  - _文档首行_（仅供参考）: Serialize goal read-modify-write sequences within the current event loop.
  - 分支数 4，函数体节点数 94；生成器（yield）
  - 调用: get_running_loop, get, Lock

#### `ƒ` `parse_goal_command(args: str) -> GoalCommand`  L92
  - _文档首行_（仅供参考）: Parse the argument string of a ``/goal`` command into an intent.
  - 分支数 2，函数体节点数 49；return: GoalCommand('status'), GoalCommand('clear'), GoalCommand('set', stripped)
  - 调用: strip, GoalCommand, lower

#### `ƒ` `normalize_goal_objective(objective: str) -> str`  L108
  - _文档首行_（仅供参考）: Normalize and validate user-provided goal text.
  - 分支数 2，函数体节点数 57；raise: ValueError('Goal objective must not be empty.'), ValueError(f'Goal objective must be at most {MAX_GOAL_OBJECTIVE_CHARS} characters.')；return: normalized
  - 调用: join, split, strip, ValueError, len

#### `ƒ` `build_goal_state(objective: str, *, max_continuations: int, max_no_progress_continuations: int, now: str | None) -> GoalState`  L118
  - _文档首行_（仅供参考）: Create a fresh active goal state for a thread.
  - 分支数 0，函数体节点数 93；return: GoalState(objective=objective, status='active', created_at=timestamp, updated_at=timestamp, continuation_count=0, max_continuations=capped_max, no_progress_count=0, max_no_progress_continuations=max(0, int(max_no_progress_continuations)))
  - 调用: normalize_goal_objective, max, min, int, now_iso, GoalState

#### `ƒ` `parse_goal_evaluation_response(text: str) -> GoalEvaluation`  L141
  - _文档首行_（仅供参考）: Parse the evaluator's JSON object response.
  - 分支数 4，函数体节点数 197；raise: ValueError('Goal evaluator response did not contain a JSON object.'), ValueError('Goal evaluator response was not valid JSON.'), ValueError('Goal evaluator JSON must be an object.'), ValueError("Goal evaluator JSON must include boolean 'satisfied'.")；return: GoalEvaluation(satisfied=satisfied, blocker=blocker, reason=reason, evidence_summary=evidence_summary)
  - 调用: _strip_markdown_code_fence, _strip_think_blocks, find, rfind, ValueError, loads, isinstance, get, _normalize_evaluation_text, _normalize_goal_blocker, GoalEvaluation

#### `ƒ` `_normalize_evaluation_text(value: object, *, max_chars: int) -> str`  L168
  - 分支数 1，函数体节点数 40；return: '', ' '.join(value.strip().split())[:max_chars]
  - 调用: isinstance, join, split, strip

#### `ƒ` `_normalize_goal_blocker(value: object, *, satisfied: bool) -> GoalBlocker`  L174
  - 分支数 2，函数体节点数 41；return: 'none', value, 'missing_evidence'
  - 调用: isinstance

#### `ƒ` `_message_type(message: Any) -> str | None`  L182
  - 分支数 3，函数体节点数 78；return: 'ai', 'human', str(value) if value else None
  - 调用: getattr, isinstance, get, str
  - 反射: getattr (L183)

#### `ƒ` `_additional_kwargs(message: Any) -> dict[str, Any]`  L193
  - 分支数 1，函数体节点数 64；return: dict(value) if isinstance(value, dict) else {}
  - 调用: getattr, isinstance, get, dict
  - 反射: getattr (L194)

#### `ƒ` `_is_visible_message(message: Any) -> bool`  L200
  - 分支数 1，函数体节点数 33；return: False, _message_type(message) in {'human', 'ai'}
  - 调用: get, _additional_kwargs, _message_type

#### `ƒ` `has_visible_assistant_evidence(messages: list[Any]) -> bool`  L206
  - _文档首行_（仅供参考）: Return true when the evaluator can inspect at least one visible AI reply.
  - 分支数 0，函数体节点数 49；return: any((_is_visible_message(message) and _message_type(message) == 'ai' and bool(message_to_text(message).strip()) for message in messages))
  - 调用: any, _is_visible_message, _message_type, bool, strip, message_to_text

#### `ƒ` `visible_conversation_signature(messages: list[Any]) -> str`  L211
  - _文档首行_（仅供参考）: Return a stable lightweight signature for the visible evaluator evidence.
  - 分支数 2，函数体节点数 73；return: json.dumps(visible[-MAX_GOAL_CONVERSATION_MESSAGES:], ensure_ascii=False, sort_keys=True)
  - 调用: _is_visible_message, append, _message_type, strip, message_to_text, dumps

#### `ƒ` `format_visible_conversation(messages: list[Any]) -> str`  L226
  - _文档首行_（仅供参考）: Return the user-visible conversation evidence for goal evaluation.
  - 分支数 3，函数体节点数 131；return: conversation
  - 调用: _is_visible_message, strip, message_to_text, _message_type, append, join, len

#### `ƒ` `create_goal_evaluator_model(*, model_name: str | None, app_config: Any | None) -> Any`  L242
  - _文档首行_（仅供参考）: Create the non-thinking chat model used by the goal evaluator.
  - 分支数 0，函数体节点数 34；return: create_chat_model(name=model_name, thinking_enabled=False, app_config=app_config, attach_tracing=True)
  - 调用: create_chat_model

#### `ƒ` `_resolve_environment() -> str | None`  L266
  - 分支数 0，函数体节点数 26；return: os.environ.get('DEER_FLOW_ENV') or os.environ.get('ENVIRONMENT')
  - 调用: get

#### `⏵ƒ` `async evaluate_goal_completion(goal: GoalState, messages: list[Any], *, model: Any | None, model_name: str | None, app_config: Any | None, thread_id: str | None, user_id: str | None, deerflow_trace_id: str | None) -> GoalEvaluation`  L270
  - _文档首行_（仅供参考）: Ask a small non-thinking model whether the active goal is satisfied.
  - 分支数 2，函数体节点数 207；return: GoalEvaluation(satisfied=False, blocker='missing_evidence', reason='No visible assistant evidence is available yet.', evidence_summary=''), parse_goal_evaluation_response(_extract_response_text(response.content))
  - 调用: format_visible_conversation, has_visible_assistant_evidence, GoalEvaluation, create_goal_evaluator_model, inject_langfuse_metadata, _resolve_environment, ainvoke, SystemMessage, HumanMessage, parse_goal_evaluation_response, _extract_response_text

#### `ƒ` `should_continue_goal(goal: GoalState, evaluation: GoalEvaluation, *, no_progress_count: int | None) -> bool`  L330
  - _文档首行_（仅供参考）: Return whether another hidden continuation turn should run.
  - 分支数 3，函数体节点数 107；return: False, current_no_progress < max_no_progress
  - 调用: int, get

#### `ƒ` `latest_visible_assistant_signature(messages: list[Any]) -> str`  L343
  - _文档首行_（仅供参考）: Return a stable signature of the latest visible assistant evidence.
  - 分支数 3，函数体节点数 71；return: hashlib.sha256(text.encode('utf-8')).hexdigest(), ''
  - 调用: reversed, _is_visible_message, _message_type, strip, message_to_text, hexdigest, sha256, encode

#### `ƒ` `compute_goal_progress_key(evaluation: GoalEvaluation, *, evidence_signature: str) -> str`  L362
  - _文档首行_（仅供参考）: Return a stable key used to detect repeated non-progress evaluations.
  - 分支数 0，函数体节点数 39；return: json.dumps({'satisfied': evaluation['satisfied'], 'blocker': evaluation['blocker'], 'evidence_signature': evidence_signature}, ensure_ascii=False, sort_keys=True)
  - 调用: dumps

#### `ƒ` `compute_no_progress_count(goal: GoalState, evaluation: GoalEvaluation, *, evidence_signature: str) -> int`  L380
  - _文档首行_（仅供参考）: Increment repeated-progress count when visible evidence has not advanced.
  - 分支数 2，函数体节点数 81；return: 0, int(goal.get('no_progress_count', 0)) + 1
  - 调用: compute_goal_progress_key, get, isinstance, int

#### `ƒ` `make_goal_continuation_message(goal: GoalState, evaluation: GoalEvaluation) -> HumanMessage`  L391
  - _文档首行_（仅供参考）: Build the hidden user message that asks the agent to keep working.
  - 分支数 0，函数体节点数 65；return: HumanMessage(content=content, additional_kwargs={'hide_from_ui': True, 'deerflow_goal_continuation': True})
  - 调用: get, HumanMessage

#### `⏵ƒ` `async _call_checkpointer_method(checkpointer: Any, async_name: str, sync_name: str, *args, **kwargs) -> Any`  L411
  - 分支数 2，函数体节点数 125；可变参数（*args/**kwargs）；raise: AttributeError(f'Missing checkpointer method: {async_name}/{sync_name}')；return: await result if inspect.isawaitable(result) else result
  - 调用: getattr, async_method, isawaitable, AttributeError, to_thread
  - 反射: getattr (L412), getattr (L416)

#### `ƒ` `_next_channel_version(checkpointer: Any, current_version: Any) -> Any`  L425
  - 分支数 2，函数体节点数 49；return: get_next_version(current_version, None), current_version + 1, 1
  - 调用: getattr, callable, get_next_version, isinstance
  - 反射: getattr (L426)

#### `⏵ƒ` `async ensure_thread_checkpoint(checkpointer: Any, thread_id: str) -> None`  L434
  - _文档首行_（仅供参考）: Create an empty root checkpoint for *thread_id* when none exists.
  - 分支数 1，函数体节点数 77；return: None
  - 调用: _call_checkpointer_method, now_iso, empty_checkpoint

#### `ƒ` `_checkpoint_id_from_tuple(checkpoint_tuple: Any) -> str | None`  L450
  - 分支数 2，函数体节点数 113；return: checkpoint_id, checkpoint['id'], None
  - 调用: getattr, isinstance, get
  - 反射: getattr (L451), getattr (L456)

#### `⏵ƒ` `async read_thread_goal(checkpointer: Any, thread_id: str) -> GoalState | None`  L462
  - _文档首行_（仅供参考）: Read the latest thread goal from checkpoint state.
  - 分支数 1，函数体节点数 114；return: None, copy.deepcopy(raw_goal) if isinstance(raw_goal, dict) else None
  - 调用: _call_checkpointer_method, getattr, isinstance, get, deepcopy
  - 反射: getattr (L468)

#### `⏵ƒ` `async write_thread_goal(checkpointer: Any, thread_id: str, goal: GoalState | None, *, as_node: str, create_if_missing: bool, expected_checkpoint_id: str | None) -> dict[str, Any]`  L474
  - _文档首行_（仅供参考）: Write a new checkpoint with the thread goal set or cleared.
  - 分支数 4，函数体节点数 384；raise: LookupError(f'Thread {thread_id} checkpoint not found'), GoalWriteConflict(f'Thread {thread_id} goal checkpoint changed while preparing write')；return: channel_values
  - 调用: ensure_thread_checkpoint, _call_checkpointer_method, LookupError, _checkpoint_id_from_tuple, GoalWriteConflict, dict, getattr, get, pop, deepcopy, _next_channel_version, str, uuid6, now_iso
  - 反射: getattr (L502), getattr (L503)

#### `ƒ` `attach_goal_evaluation(goal: GoalState, evaluation: GoalEvaluation, *, run_id: str, continuation_count: int | None, no_progress_count: int | None, stand_down_reason: str | None, evidence_signature: str) -> GoalState`  L534
  - _文档首行_（仅供参考）: Return a goal copy with the latest evaluator result attached.
  - 分支数 3，函数体节点数 155；return: next_goal
  - 调用: deepcopy, now_iso, get, compute_goal_progress_key

## 类
### 类 `GoalWriteConflict`  L63
- 继承: RuntimeError
- _文档首行_: Raised when a goal write is based on a stale checkpoint.

### 类 `GoalCommand`  L85
- 继承: NamedTuple
- _文档首行_: Parsed intent of a ``/goal`` slash command argument string.
- 类/实例变量:
  - `kind` = <annotated>
  - `objective` = ''

## 文件内调用关系
- `build_goal_state` -> normalize_goal_objective
- `parse_goal_evaluation_response` -> _normalize_evaluation_text, _normalize_goal_blocker
- `_is_visible_message` -> _additional_kwargs, _message_type
- `has_visible_assistant_evidence` -> _is_visible_message, _message_type
- `visible_conversation_signature` -> _is_visible_message, _message_type
- `format_visible_conversation` -> _is_visible_message, _message_type
- `evaluate_goal_completion` -> format_visible_conversation, has_visible_assistant_evidence, create_goal_evaluator_model, _resolve_environment, parse_goal_evaluation_response
- `latest_visible_assistant_signature` -> _is_visible_message, _message_type
- `compute_no_progress_count` -> compute_goal_progress_key
- `ensure_thread_checkpoint` -> _call_checkpointer_method
- `read_thread_goal` -> _call_checkpointer_method
- `write_thread_goal` -> ensure_thread_checkpoint, _call_checkpointer_method, _checkpoint_id_from_tuple, _next_channel_version
- `attach_goal_evaluation` -> compute_goal_progress_key

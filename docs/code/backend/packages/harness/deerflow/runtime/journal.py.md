# `backend/packages/harness/deerflow/runtime/journal.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/journal.py`  ·  行数: 747

**模块文档首行**（仅供参考）: Run event capture via LangChain callbacks.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: asyncio, logging, time
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable, Mapping
- `datetime` -> UTC, datetime
- `typing` -> TYPE_CHECKING, Any, cast
- `uuid` -> UUID
- `langchain_core.callbacks` -> BaseCallbackHandler
- `langchain_core.messages` -> AIMessage, AnyMessage, BaseMessage, HumanMessage, ToolMessage
- `langgraph.types` -> Command
- `deerflow.agents.human_input` -> read_human_input_response
- `deerflow.utils.messages` -> message_to_text, restore_original_human_message

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_LEGACY_SUMMARY_MESSAGE_NAME` = 'summary'
- `_RECONCILED_TOOL_MESSAGE_NAMES` = frozenset({'ask_clarification'})
- `_PERSISTED_HIDDEN_HUMAN_INPUT_RESPONSE_SOURCES` = frozenset({'ask_clarification'})

## 函数
#### `ƒ` `_should_persist_human_input_message(message: BaseMessage) -> bool`  L45
  - 分支数 3，函数体节点数 71；return: False, True, response is not None and response['source'] in _PERSISTED_HIDDEN_HUMAN_INPUT_RESPONSE_SOURCES
  - 调用: isinstance, get, read_human_input_response

## 类
### 类 `RunJournal`  L56
- 继承: BaseCallbackHandler
- _文档首行_: LangChain callback handler that captures events to RunEventStore.
- 方法:
  #### `prop` `had_llm_error_fallback(self) -> bool`    @property  L741
    - 分支数 0，函数体节点数 12；return: self._had_llm_error_fallback
  #### `prop` `llm_error_fallback_message(self) -> str | None`    @property  L745
    - 分支数 0，函数体节点数 15；return: self._llm_error_fallback_message
  #### `st` `_message_text(message: BaseMessage) -> str`    @staticmethod  L126
    - _文档首行_（仅供参考）: Extract displayable text from a message's mixed content shape.
    - 分支数 0，函数体节点数 19；return: message_to_text(message, text_attribute_fallback=True)
    - 调用: message_to_text
  #### `st` `_message_identity(message: BaseMessage) -> str | None`    @staticmethod  L374
    - 分支数 2，函数体节点数 70；return: f'tool:{tool_call_id}', f'message:{message_id}', None
    - 调用: getattr, isinstance
  - 反射: getattr (L375), getattr (L378)
  #### `st` `_tool_call_value(tool_call: Any, key: str) -> Any`    @staticmethod  L384
    - 分支数 1，函数体节点数 37；return: tool_call.get(key), getattr(tool_call, key, None)
    - 调用: isinstance, get, getattr
  - 反射: getattr (L387)
  #### `st` `_extract_cache_read(usage_dict: dict) -> int`    @staticmethod  L543
    - _文档首行_（仅供参考）: Prompt-cache-hit input tokens from LangChain's normalized usage.
    - 分支数 2，函数体节点数 62；return: 0, max(int(details.get('cache_read') or 0), 0)
    - 调用: get, isinstance, max, int
  #### `m` `__init__(self, run_id: str, thread_id: str, event_store: RunEventStore, *, track_token_usage: bool, flush_threshold: int, progress_reporter: Callable[[dict], Awaitable[None]] | None, progress_flush_interval: float)`  L59
    - 分支数 0，函数体节点数 391
    - 调用: __init__, super, set
  #### `m` `_record_message_summary(self, message: BaseMessage, *, caller: str | None) -> None`  L130
    - _文档首行_（仅供参考）: Update run-level convenience fields for persisted run rows.
    - 分支数 2，函数体节点数 89
    - 调用: isinstance, getattr, strip, _message_text
  - 反射: getattr (L137)
  #### `m` `on_chain_start(self, serialized: dict[str, Any], inputs: dict[str, Any], *, run_id: UUID, parent_run_id: UUID | None, tags: list[str] | None, metadata: dict[str, Any] | None, **kwargs) -> None`  L143
    - 分支数 1，函数体节点数 119；可变参数（*args/**kwargs）
    - 调用: _identify_caller, get, _put
  #### `m` `on_chain_end(self, outputs: Any, *, run_id: UUID, parent_run_id: UUID | None, **kwargs) -> None`  L165
    - 分支数 1，函数体节点数 58；可变参数（*args/**kwargs）；return: None
    - 调用: _reconcile_final_tool_messages, _put, _flush_sync
  #### `m` `on_chain_error(self, error: BaseException, *, run_id: UUID, **kwargs) -> None`  L181
    - 分支数 0，函数体节点数 45；可变参数（*args/**kwargs）
    - 调用: _put, str, type, _flush_sync
  #### `m` `on_chat_model_start(self, serialized: dict, messages: list[list[BaseMessage]], *, run_id: UUID, tags: list[str] | None, **kwargs) -> None`  L192
    - _文档首行_（仅供参考）: Capture structured prompt messages for llm_request event.
    - 分支数 5，函数体节点数 211；可变参数（*args/**kwargs）
    - 调用: str, monotonic, add, debug, len, _identify_caller, reversed, _should_persist_human_input_message, restore_original_human_message, set_first_human_message, _message_text, _put, model_dump, _record_message_summary
  #### `m` `on_llm_start(self, serialized: dict, prompts: list[str], *, run_id: UUID, parent_run_id: UUID | None, tags: list[str] | None, metadata: dict[str, Any] | None, **kwargs) -> None`  L239
    - 分支数 0，函数体节点数 70；可变参数（*args/**kwargs）
    - 调用: str, monotonic
  #### `m` `on_llm_end(self, response: Any, *, run_id: UUID, parent_run_id: UUID | None, tags: list[str] | None, **kwargs) -> None`  L243
    - 分支数 17，函数体节点数 652；可变参数（*args/**kwargs）
    - 调用: debug, hasattr, append, warning, _identify_caller, _remember_current_run_tool_calls, str, pop, int, monotonic, getattr, dict, isinstance, get, strip, _message_text, add, _put, model_dump, _record_message_summary（+4）
  - 反射: hasattr (L256), getattr (L271), getattr (L273), getattr (L332)
  #### `m` `on_llm_error(self, error: BaseException, *, run_id: UUID, **kwargs) -> None`  L343
    - 分支数 0，函数体节点数 43；可变参数（*args/**kwargs）
    - 调用: pop, str, _put
  #### `m` `on_tool_start(self, serialized, input_str, *, run_id, parent_run_id, tags, metadata, inputs, **kwargs)`  L347
    - _文档首行_（仅供参考）: Handle tool start event, cache tool call ID for later correlation
    - 分支数 0，函数体节点数 38；可变参数（*args/**kwargs）
    - 调用: str, debug
  #### `m` `on_tool_end(self, output, *, run_id, parent_run_id, **kwargs)`  L352
    - _文档首行_（仅供参考）: Handle tool end event, append message and clear node data
    - 分支数 5，函数体节点数 134；可变参数（*args/**kwargs）
    - 调用: isinstance, cast, _persist_tool_result_message, get, warning, type, debug
  #### `m` `_remember_current_run_tool_calls(self, message: AnyMessage, *, caller: str) -> None`  L389
    - 分支数 5，函数体节点数 131；return: None
    - 调用: isinstance, getattr, _tool_call_value, str
  - 反射: getattr (L392), getattr (L395)
  #### `m` `_persist_tool_result_message(self, message: BaseMessage) -> None`  L405
    - 分支数 1，函数体节点数 54
    - 调用: _put, model_dump, _message_identity, add, _record_message_summary
  #### `m` `_final_output_messages(self, outputs: Any) -> list[Any]`  L412
    - 分支数 1，函数体节点数 47；return: messages if isinstance(messages, list) else [], []
    - 调用: isinstance, get
  #### `m` `_should_reconcile_tool_message(self, message: ToolMessage) -> bool`  L418
    - 分支数 4，函数体节点数 123；return: False, identity is not None and identity not in self._persisted_tool_message_identities
    - 调用: get, getattr, isinstance, _message_identity
  - 反射: getattr (L421), getattr (L427)
  #### `m` `_reconcile_final_tool_messages(self, outputs: Any) -> None`  L433
    - 分支数 3，函数体节点数 44
    - 调用: _final_output_messages, isinstance, _should_reconcile_tool_message, _persist_tool_result_message
  #### `m` `_put(self, *, event_type: str, category: str, content: str | dict, metadata: dict | None) -> None`  L440
    - 分支数 1，函数体节点数 90
    - 调用: append, isoformat, now, len, _flush_sync
  #### `m` `_flush_sync(self) -> None`  L455
    - _文档首行_（仅供参考）: Best-effort flush of buffer to RunEventStore.
    - 分支数 3，函数体节点数 86；return: None
    - 调用: get_running_loop, copy, clear, create_task, _flush_async, add, add_done_callback
  #### `m` `_on_flush_done(self, task: asyncio.Task) -> None`  L493
    - 分支数 2，函数体节点数 46；return: None
    - 调用: discard, cancelled, exception, warning
  #### `m` `_identify_caller(self, tags: list[str] | None) -> str`  L501
    - 分支数 2，函数体节点数 63；return: tag, 'lead_agent'
    - 调用: isinstance, startswith
  #### `m` `_record_model_usage(self, model_name: str | None, input_tokens: int, output_tokens: int, total_tokens: int, cache_read_tokens: int) -> None`  L511
    - _文档首行_（仅供参考）: Add a single LLM call's token usage to the per-model accumulator.
    - 分支数 2，函数体节点数 122；return: None
    - 调用: setdefault, int, get
  #### `m` `record_external_llm_usage_records(self, records: list[dict[str, int | str | None]]) -> None`  L555
    - _文档首行_（仅供参考）: Record token usage from external sources (e.g., subagents).
    - 分支数 8，函数体节点数 284；return: None
    - 调用: str, get, add, startswith, _record_model_usage, int, _schedule_progress_flush
  #### `m` `set_first_human_message(self, content: str) -> None`  L609
    - _文档首行_（仅供参考）: Record the first human message for convenience fields.
    - 分支数 0，函数体节点数 24
  #### `m` `record_middleware(self, tag: str, *, name: str, hook: str, action: str, changes: dict) -> None`  L613
    - _文档首行_（仅供参考）: Record a middleware state-change event.
    - 分支数 0，函数体节点数 49
    - 调用: _put
  #### `m` `record_memory_context(self, *, content_sha256: str) -> None`  L634
    - _文档首行_（仅供参考）: Record the effective hidden memory block for this run.
    - 分支数 1，函数体节点数 36；return: None
    - 调用: _put
  #### `m` `_schedule_progress_flush(self) -> None`  L673
    - _文档首行_（仅供参考）: Best-effort throttled progress snapshot for active run visibility.
    - 分支数 4，函数体节点数 130；return: None
    - 调用: monotonic, _schedule_delayed_progress_flush, done, get_running_loop, create_task, _flush_progress_async, get_completion_data
  #### `m` `_schedule_delayed_progress_flush(self, delay: float) -> None`  L693
    - 分支数 2，函数体节点数 77；return: None
    - 调用: done, get_running_loop, max, create_task, _flush_progress_async
  #### `m` `get_completion_data(self) -> dict`  L724
    - _文档首行_（仅供参考）: Return accumulated token and message data for run completion.
    - 分支数 0，函数体节点数 82；return: {'total_input_tokens': self._total_input_tokens, 'total_output_tokens': self._total_output_tokens, 'total_tokens': self._total_tokens, 'llm_call_count': self._llm_call_count, 'lead_agent_tokens': self._lead_agent_tokens, 'subagent_tokens': self._subagent_tokens, 'middleware_tokens': self._middleware_tokens, 'token_usage_by_model': {model: dict(usage) for model, usage in self._tokens_by_model.items()}, 'message_count': self._msg_count, 'last_ai_message': self._last_ai_msg, 'first_human_message': self._first_human_msg}
    - 调用: dict, items
  #### `⏵m` `async _flush_async(self, batch: list[dict]) -> None`  L480
    - 分支数 1，函数体节点数 57
    - 调用: put_batch, warning, len
  #### `⏵m` `async flush(self) -> None`  L651
    - _文档首行_（仅供参考）: Force flush remaining buffer. Called in worker's finally block.
    - 分支数 5，函数体节点数 160；raise: bare raise
    - 调用: gather, tuple, done, cancel, put_batch
  #### `⏵m` `async _flush_progress_async(self, *, snapshot: dict | None, delay: float) -> None`  L704
    - 分支数 4，函数体节点数 143；return: None
    - 调用: sleep, get_completion_data, _progress_reporter, monotonic, warning, _schedule_delayed_progress_flush

## 文件内调用关系
- `RunJournal.__init__` -> __init__
- `RunJournal._record_message_summary` -> _message_text
- `RunJournal.on_chain_start` -> _identify_caller, _put
- `RunJournal.on_chain_end` -> _reconcile_final_tool_messages, _put, _flush_sync
- `RunJournal.on_chain_error` -> _put, _flush_sync
- `RunJournal.on_chat_model_start` -> _identify_caller, _should_persist_human_input_message, set_first_human_message, _message_text, _put, _record_message_summary
- `RunJournal.on_llm_end` -> _identify_caller, _remember_current_run_tool_calls, _message_text, _put, _record_message_summary, _record_model_usage, _extract_cache_read, _schedule_progress_flush
- `RunJournal.on_llm_error` -> _put
- `RunJournal.on_tool_end` -> _persist_tool_result_message
- `RunJournal._remember_current_run_tool_calls` -> _tool_call_value
- `RunJournal._persist_tool_result_message` -> _put, _message_identity, _record_message_summary
- `RunJournal._should_reconcile_tool_message` -> _message_identity
- `RunJournal._reconcile_final_tool_messages` -> _final_output_messages, _should_reconcile_tool_message, _persist_tool_result_message
- `RunJournal._put` -> _flush_sync
- `RunJournal._flush_sync` -> _flush_async
- `RunJournal.record_external_llm_usage_records` -> _record_model_usage, _schedule_progress_flush
- `RunJournal.record_middleware` -> _put
- `RunJournal.record_memory_context` -> _put
- `RunJournal._schedule_progress_flush` -> _schedule_delayed_progress_flush, _flush_progress_async, get_completion_data
- `RunJournal._schedule_delayed_progress_flush` -> _flush_progress_async
- `RunJournal._flush_progress_async` -> get_completion_data, _schedule_delayed_progress_flush

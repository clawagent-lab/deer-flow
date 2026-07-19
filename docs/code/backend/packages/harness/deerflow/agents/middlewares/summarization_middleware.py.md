# `backend/packages/harness/deerflow/agents/middlewares/summarization_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/summarization_middleware.py`  ·  行数: 515

**模块文档首行**（仅供参考）: Summarization middleware extensions for DeerFlow.

## 模块概览
- 函数 3 个，类 4 个，模块级常量 2 个

## 依赖（import）
- 模块: html, logging
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> Any, Protocol, override, runtime_checkable
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> SummarizationMiddleware
- `langchain_core.messages` -> AnyMessage, HumanMessage, RemoveMessage, get_buffer_string, trim_messages
- `langgraph.config` -> get_config
- `langgraph.constants` -> TAG_NOSTREAM
- `langgraph.graph.message` -> REMOVE_ALL_MESSAGES
- `langgraph.runtime` -> Runtime
- `deerflow.agents.middlewares.dynamic_context_middleware` -> is_dynamic_context_reminder
- `deerflow.config.app_config` -> get_app_config
- `deerflow.models` -> create_chat_model

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SUMMARY_TRIGGER_MESSAGE_NAME` = 'summary'

## 函数
#### `ƒ` `_resolve_thread_id(runtime: Runtime) -> str | None`  L54
  - _文档首行_（仅供参考）: Resolve the current thread ID from runtime context or LangGraph config.
  - 分支数 2，函数体节点数 64；return: None, thread_id
  - 调用: get, get_config

#### `ƒ` `_resolve_agent_name(runtime: Runtime) -> str | None`  L66
  - _文档首行_（仅供参考）: Resolve the current agent name from runtime context or LangGraph config.
  - 分支数 2，函数体节点数 64；return: None, agent_name
  - 调用: get, get_config

#### `ƒ` `create_summarization_middleware(*, app_config: Any | None, keep: tuple[str, int | float] | None, skip_memory_flush: bool) -> DeerFlowSummarizationMiddleware | None`  L447
  - _文档首行_（仅供参考）: Create the configured summarization middleware.
  - 分支数 7，函数体节点数 273；return: None, DeerFlowSummarizationMiddleware(**kwargs, before_summarization=hooks)
  - 调用: get_app_config, isinstance, to_tuple, create_chat_model, with_config, append, DeerFlowSummarizationMiddleware

## 类
### 类 `SummarizationEvent`  L27  @dataclass(...)
- _文档首行_: Context emitted before conversation history is summarized away.
- 类/实例变量:
  - `messages_to_summarize` = <annotated>
  - `preserved_messages` = <annotated>
  - `thread_id` = <annotated>
  - `agent_name` = <annotated>
  - `runtime` = <annotated>

### 类 `ContextCompactionResult`  L38  @dataclass(...)
- _文档首行_: Result of summarizing old context and retaining the active tail.
- 类/实例变量:
  - `summary_text` = <annotated>
  - `messages_to_summarize` = <annotated>
  - `preserved_messages` = <annotated>
  - `total_tokens` = <annotated>

### 类 `BeforeSummarizationHook`  L48  @runtime_checkable
- 继承: Protocol
- _文档首行_: Hook invoked before summarization removes messages from state.
- 方法:
  #### `m` `__call__(self, event: SummarizationEvent) -> None`  L51
    - 分支数 0，函数体节点数 9

### 类 `DeerFlowSummarizationMiddleware`  L78
- 继承: SummarizationMiddleware
- _文档首行_: Summarization middleware with pre-compression hook dispatch.
- 方法:
  #### `st` `_summary_count_message(summary_text: str) -> HumanMessage`    @staticmethod  L151
    - 分支数 0，函数体节点数 19；return: HumanMessage(content=summary_text, name=_SUMMARY_TRIGGER_MESSAGE_NAME)
    - 调用: HumanMessage
  #### `st` `_bound_text(text: str, cap: int) -> str`    @staticmethod  L160
    - 分支数 4，函数体节点数 123；return: text, '', text[:cap], f'{text[:head]}{omitted_marker}{text[-tail:]}'
    - 调用: len, max
  #### `m` `__init__(self, *args, before_summarization: list[BeforeSummarizationHook] | None, **kwargs) -> None`  L81
    - 分支数 0，函数体节点数 103；可变参数（*args/**kwargs）
    - 调用: __init__, super, list, get, getattr, with_config
  - 反射: getattr (L98)
  #### `m` `_create_summary(self, messages_to_summarize: list[AnyMessage]) -> str | None`    @override  L103
    - 分支数 0，函数体节点数 25；return: self._summarize_with(messages_to_summarize)
    - 调用: _summarize_with
  #### `m` `_summarize_with(self, messages_to_summarize: list[AnyMessage], previous_summary: str | None) -> str | None`  L110
    - _文档首行_（仅供参考）: Mirror the parent ``_create_summary`` but invoke the nostream-tagged model.
    - 分支数 3，函数体节点数 91；return: 'No previous conversation history.', 'Previous conversation was too long to summarize.', response.text.strip(), None
    - 调用: _build_summary_prompt, invoke, strip, exception
  #### `m` `_messages_for_trigger_count(self, messages: list[AnyMessage], summary_text: str | None) -> list[AnyMessage]`  L154
    - 分支数 1，函数体节点数 44；return: messages, [*messages, self._summary_count_message(summary_text)]
    - 调用: _summary_count_message
  #### `m` `_trim_summary_section_text(self, text: str, max_tokens: int, *, strategy: str) -> str`  L174
    - 分支数 4，函数体节点数 119；return: '', content, self._bound_text(text, max_tokens)
    - 调用: strip, max, trim_messages, HumanMessage, isinstance, debug, _bound_text
  #### `m` `_build_summary_input_text(self, formatted_messages: str, previous_summary: str | None) -> str | None`  L195
    - 分支数 5，函数体节点数 201；return: None, '\n'.join(parts)
    - 调用: strip, max, _trim_summary_section_text, extend, escape, join
  #### `m` `_build_summary_prompt(self, messages_to_summarize: list[AnyMessage], previous_summary: str | None) -> str | None`  L254
    - _文档首行_（仅供参考）: Build the summary prompt, returning ``None`` when trimming leaves nothing.
    - 分支数 3，函数体节点数 99；return: None, self.summary_prompt.format(messages=formatted_messages).rstrip()
    - 调用: _trim_messages_for_summary, get_buffer_string, _build_summary_input_text, rstrip, format
  #### `m` `before_model(self, state: AgentState, runtime: Runtime) -> dict | None`  L269
    - 分支数 0，函数体节点数 24；return: self._maybe_summarize(state, runtime)
    - 调用: _maybe_summarize
  #### `m` `_prepare_compaction(self, state: AgentState, *, force: bool) -> tuple[list[AnyMessage], list[AnyMessage], str | None, int] | None`  L275
    - 分支数 3，函数体节点数 186；return: None, (messages_to_summarize, preserved_messages, previous_summary, total_tokens)
    - 调用: _ensure_message_ids, isinstance, get, _messages_for_trigger_count, token_counter, _should_summarize, _determine_cutoff_index, _partition_messages, _preserve_dynamic_context_reminders
  #### `m` `compact_state(self, state: AgentState, runtime: Runtime, *, force: bool) -> ContextCompactionResult | None`  L300
    - 分支数 2，函数体节点数 107；return: None, ContextCompactionResult(summary_text=summary, messages_to_summarize=tuple(messages_to_summarize), preserved_messages=tuple(preserved_messages), total_tokens=total_tokens)
    - 调用: _prepare_compaction, _fire_hooks, _summarize_with, ContextCompactionResult, tuple
  #### `m` `_maybe_summarize(self, state: AgentState, runtime: Runtime) -> dict | None`  L344
    - 分支数 1，函数体节点数 58；return: None, {'messages': [RemoveMessage(id=REMOVE_ALL_MESSAGES), *result.preserved_messages], 'summary_text': result.summary_text}
    - 调用: compact_state, RemoveMessage
  #### `m` `_preserve_dynamic_context_reminders(self, messages_to_summarize: list[AnyMessage], preserved_messages: list[AnyMessage]) -> tuple[list[AnyMessage], list[AnyMessage]]`  L368
    - _文档首行_（仅供参考）: Keep hidden dynamic-context reminders and their ID-swap peers out of summary compression.
    - 分支数 5，函数体节点数 199；return: (messages_to_summarize, preserved_messages), (remaining, rescued + preserved_messages)
    - 调用: is_dynamic_context_reminder, set, removesuffix, add, any, startswith, append
  #### `m` `_fire_hooks(self, messages_to_summarize: list[AnyMessage], preserved_messages: list[AnyMessage], runtime: Runtime) -> None`  L422
    - 分支数 3，函数体节点数 107；return: None
    - 调用: SummarizationEvent, tuple, _resolve_thread_id, _resolve_agent_name, hook, getattr, type, exception
  - 反射: getattr (L443)
  #### `⏵m` `async _acreate_summary(self, messages_to_summarize: list[AnyMessage]) -> str | None`    @override  L107
    - 分支数 0，函数体节点数 26；return: await self._asummarize_with(messages_to_summarize)
    - 调用: _asummarize_with
  #### `⏵m` `async _asummarize_with(self, messages_to_summarize: list[AnyMessage], previous_summary: str | None) -> str | None`  L133
    - _文档首行_（仅供参考）: Async counterpart of :meth:`_summarize_with` using the nostream model.
    - 分支数 3，函数体节点数 92；return: 'No previous conversation history.', 'Previous conversation was too long to summarize.', response.text.strip(), None
    - 调用: _build_summary_prompt, ainvoke, strip, exception
  #### `⏵m` `async abefore_model(self, state: AgentState, runtime: Runtime) -> dict | None`  L272
    - 分支数 0，函数体节点数 25；return: await self._amaybe_summarize(state, runtime)
    - 调用: _amaybe_summarize
  #### `⏵m` `async acompact_state(self, state: AgentState, runtime: Runtime, *, force: bool) -> ContextCompactionResult | None`  L322
    - 分支数 2，函数体节点数 108；return: None, ContextCompactionResult(summary_text=summary, messages_to_summarize=tuple(messages_to_summarize), preserved_messages=tuple(preserved_messages), total_tokens=total_tokens)
    - 调用: _prepare_compaction, _fire_hooks, _asummarize_with, ContextCompactionResult, tuple
  #### `⏵m` `async _amaybe_summarize(self, state: AgentState, runtime: Runtime) -> dict | None`  L356
    - 分支数 1，函数体节点数 59；return: None, {'messages': [RemoveMessage(id=REMOVE_ALL_MESSAGES), *result.preserved_messages], 'summary_text': result.summary_text}
    - 调用: acompact_state, RemoveMessage

## 文件内调用关系
- `DeerFlowSummarizationMiddleware.__init__` -> __init__
- `DeerFlowSummarizationMiddleware._create_summary` -> _summarize_with
- `DeerFlowSummarizationMiddleware._acreate_summary` -> _asummarize_with
- `DeerFlowSummarizationMiddleware._summarize_with` -> _build_summary_prompt
- `DeerFlowSummarizationMiddleware._asummarize_with` -> _build_summary_prompt
- `DeerFlowSummarizationMiddleware._messages_for_trigger_count` -> _summary_count_message
- `DeerFlowSummarizationMiddleware._trim_summary_section_text` -> _bound_text
- `DeerFlowSummarizationMiddleware._build_summary_input_text` -> _trim_summary_section_text
- `DeerFlowSummarizationMiddleware._build_summary_prompt` -> _build_summary_input_text
- `DeerFlowSummarizationMiddleware.before_model` -> _maybe_summarize
- `DeerFlowSummarizationMiddleware.abefore_model` -> _amaybe_summarize
- `DeerFlowSummarizationMiddleware._prepare_compaction` -> _messages_for_trigger_count, _preserve_dynamic_context_reminders
- `DeerFlowSummarizationMiddleware.compact_state` -> _prepare_compaction, _fire_hooks, _summarize_with
- `DeerFlowSummarizationMiddleware.acompact_state` -> _prepare_compaction, _fire_hooks, _asummarize_with
- `DeerFlowSummarizationMiddleware._maybe_summarize` -> compact_state
- `DeerFlowSummarizationMiddleware._amaybe_summarize` -> acompact_state
- `DeerFlowSummarizationMiddleware._fire_hooks` -> _resolve_thread_id, _resolve_agent_name

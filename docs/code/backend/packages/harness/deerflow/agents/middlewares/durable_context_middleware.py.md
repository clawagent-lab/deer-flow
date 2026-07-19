# `backend/packages/harness/deerflow/agents/middlewares/durable_context_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/durable_context_middleware.py`  ·  行数: 288

**模块文档首行**（仅供参考）: Durable-context middleware: inject summary, delegation ledger, and skills.

## 模块概览
- 函数 12 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: posixpath
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable, Collection
- `html` -> escape
- `typing` -> override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> AnyMessage, HumanMessage, SystemMessage
- `langgraph.runtime` -> Runtime
- `deerflow.agents.middlewares.delegation_ledger` -> extract_delegations, render_delegation_ledger
- `deerflow.agents.middlewares.skill_context` -> extract_skills, render_skill_context
- `deerflow.agents.thread_state` -> _DELEGATION_LEDGER_MAX_ENTRIES, TERMINAL_STATUSES
- `deerflow.config.summarization_config` -> DEFAULT_SKILL_FILE_READ_TOOL_NAMES
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.runtime.context_keys` -> CURRENT_RUN_PRE_EXISTING_MESSAGE_IDS_KEY

## 模块级常量
- `_DURABLE_CONTEXT_DATA_KEY` = 'durable_context_data'
- `_SUMMARY_RENDER_CHAR_BUDGET` = 6000
- `_AUTHORITY_CONTRACT` = '\n'.join(['## Durable context authority contract', 'A fo...
- `_DELEGATION_STABLE_FIELDS` = ('description', 'subagent_type', 'status', 'run_id', 'res...

## 函数
#### `ƒ` `_normalize_skills_root(skills_container_path: str | None) -> str`  L43
  - 分支数 0，函数体节点数 22；return: posixpath.normpath(skills_container_path or DEFAULT_SKILLS_CONTAINER_PATH)
  - 调用: normpath

#### `ƒ` `_bound_text(text: str, cap: int) -> str`  L47
  - 分支数 4，函数体节点数 121；return: text, '', text[:cap], f'{text[:head]}{omitted_marker}{text[-tail:]}'
  - 调用: len, max

#### `ƒ` `_insert_after_leading_system_messages(messages: list, injected: list) -> list`  L62
  - 分支数 1，函数体节点数 67；return: [*messages[:index], *injected, *messages[index:]]
  - 调用: len, isinstance

#### `ƒ` `_render_durable_context_data(summary_text: str | None, ledger: list, skills: list) -> str`  L69
  - 分支数 4，函数体节点数 125；return: '', '<durable_context_data>\n' + '\n\n'.join(data_parts) + '\n</durable_context_data>'
  - 调用: _bound_text, str, append, escape, render_delegation_ledger, render_skill_context, join

#### `ƒ` `_retained_delegation_window(delegations: list[dict], existing: list[dict]) -> list[dict]`  L88
  - 分支数 4，函数体节点数 112；return: delegations, delegations[index:], delegations[-_DELEGATION_LEDGER_MAX_ENTRIES:]
  - 调用: len, isinstance, get, enumerate

#### `ƒ` `_filter_changed_delegations(delegations: list[dict], existing: list[dict]) -> list[dict]`  L101
  - 分支数 4，函数体节点数 162；return: changed
  - 调用: _retained_delegation_window, get, isinstance, append, any

#### `ƒ` `_runtime_run_id(runtime: Runtime | None) -> str | None`  L117
  - 分支数 1，函数体节点数 54；return: None, str(run_id) if run_id else None
  - 调用: getattr, isinstance, get, str
  - 反射: getattr (L118)

#### `ƒ` `_runtime_pre_existing_message_ids(runtime: Runtime | None) -> frozenset[str]`  L125
  - 分支数 2，函数体节点数 87；return: frozenset(), frozenset((str(message_id) for message_id in raw_ids if message_id))
  - 调用: getattr, isinstance, frozenset, get, str
  - 反射: getattr (L126)

#### `ƒ` `_message_id(message: object) -> str | None`  L135
  - 分支数 1，函数体节点数 47；return: str(message_id) if message_id else None
  - 调用: isinstance, get, getattr, str
  - 反射: getattr (L139)

#### `ƒ` `_messages_after_pre_existing_boundary(messages: list[AnyMessage], pre_existing_message_ids: frozenset[str]) -> list[AnyMessage]`  L143
  - 分支数 3，函数体节点数 78；return: [], messages[index + 1:]
  - 调用: range, len, _message_id

#### `ƒ` `_current_run_messages(messages: list[AnyMessage], run_id: str | None, pre_existing_message_ids: frozenset[str]) -> list[AnyMessage]`  L152
  - _文档首行_（仅供参考）: Return the message tail where this invocation may have emitted tasks.
  - 分支数 6，函数体节点数 169；return: messages, messages[index + 1:], _messages_after_pre_existing_boundary(messages, pre_existing_message_ids)
  - 调用: range, len, isinstance, get, _message_id, _messages_after_pre_existing_boundary

#### `ƒ` `_with_run_id(delegations: list[dict], run_id: str | None, existing: list[dict]) -> list[dict]`  L177
  - _文档首行_（仅供参考）: Tag only new delegation ids with the current run_id.
  - 分支数 4，函数体节点数 167；return: delegations, tagged
  - 调用: get, isinstance, append, items

## 类
### 类 `DurableContextMiddleware`  L196
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Capture delegations + loaded skills; inject durable context ephemerally.
- 方法:
  #### `m` `__init__(self, *, skills_container_path: str | None, skill_file_read_tool_names: Collection[str] | None) -> None`  L199
    - 分支数 0，函数体节点数 57
    - 调用: __init__, super, _normalize_skills_root, frozenset
  #### `m` `before_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L210
    - 分支数 0，函数体节点数 26；return: self._capture(state, runtime)
    - 调用: _capture
  #### `m` `after_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L218
    - 分支数 0，函数体节点数 26；return: self._capture_delegations(state, runtime)
    - 调用: _capture_delegations
  #### `m` `_capture_delegations(self, state: AgentState, runtime: Runtime | None) -> dict | None`  L225
    - 分支数 1，函数体节点数 91；return: {'delegations': delegations}, None
    - 调用: _runtime_run_id, _runtime_pre_existing_message_ids, _current_run_messages, get, _filter_changed_delegations, _with_run_id, extract_delegations
  #### `m` `_capture(self, state: AgentState, runtime: Runtime | None) -> dict | None`  L238
    - 分支数 2，函数体节点数 89；return: updates or None
    - 调用: _capture_delegations, update, extract_skills
  #### `m` `_inject(self, request: ModelRequest) -> ModelRequest`  L249
    - 分支数 1，函数体节点数 101；return: request, request.override(messages=messages)
    - 调用: _render_durable_context_data, get, _insert_after_leading_system_messages, list, SystemMessage, HumanMessage, override
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L274
    - 分支数 0，函数体节点数 34；return: handler(self._inject(request))
    - 调用: handler, _inject
  #### `⏵m` `async abefore_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L214
    - 分支数 0，函数体节点数 26；return: self._capture(state, runtime)
    - 调用: _capture
  #### `⏵m` `async aafter_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L222
    - 分支数 0，函数体节点数 26；return: self._capture_delegations(state, runtime)
    - 调用: _capture_delegations
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L282
    - 分支数 0，函数体节点数 39；return: await handler(self._inject(request))
    - 调用: handler, _inject

## 文件内调用关系
- `_render_durable_context_data` -> _bound_text
- `_filter_changed_delegations` -> _retained_delegation_window
- `_messages_after_pre_existing_boundary` -> _message_id
- `_current_run_messages` -> _message_id, _messages_after_pre_existing_boundary
- `DurableContextMiddleware.__init__` -> __init__, _normalize_skills_root
- `DurableContextMiddleware.before_model` -> _capture
- `DurableContextMiddleware.abefore_model` -> _capture
- `DurableContextMiddleware.after_model` -> _capture_delegations
- `DurableContextMiddleware.aafter_model` -> _capture_delegations
- `DurableContextMiddleware._capture_delegations` -> _runtime_run_id, _runtime_pre_existing_message_ids, _current_run_messages, _filter_changed_delegations, _with_run_id
- `DurableContextMiddleware._capture` -> _capture_delegations
- `DurableContextMiddleware._inject` -> _render_durable_context_data, _insert_after_leading_system_messages
- `DurableContextMiddleware.wrap_model_call` -> _inject
- `DurableContextMiddleware.awrap_model_call` -> _inject

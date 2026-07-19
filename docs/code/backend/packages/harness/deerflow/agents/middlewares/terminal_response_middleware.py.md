# `backend/packages/harness/deerflow/agents/middlewares/terminal_response_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/terminal_response_middleware.py`  ·  行数: 215

**模块文档首行**（仅供参考）: Ensure tool-using lead-agent turns end with a visible assistant response.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 3 个

## 依赖（import）
- 模块: threading
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `typing` -> Any, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse, hook_config
- `langchain_core.messages` -> AIMessage, HumanMessage, RemoveMessage, ToolMessage
- `langgraph.runtime` -> Runtime
- `deerflow.agents.middlewares._bounded_dict` -> BoundedDict

## 模块级常量
- `_RECOVERY_PROMPT` = '<system_reminder>\nYour previous response after the tool...
- `_FALLBACK_CONTENT` = 'The model completed the tool run but returned no final r...
- `_TOOL_CALL_FINISH_REASONS` = {'tool_calls', 'function_call'}

## 函数
#### `ƒ` `_has_visible_content(message: AIMessage) -> bool`  L30
  - _文档首行_（仅供参考）: Return whether an AI message contains user-visible text.
  - 分支数 6，函数体节点数 112；return: bool(content.strip()), True, False
  - 调用: isinstance, bool, strip, get

#### `ƒ` `_has_tool_call_intent_or_error(message: AIMessage) -> bool`  L46
  - _文档首行_（仅供参考）: Keep tool routing and malformed tool-call handling out of this guard.
  - 分支数 2，函数体节点数 73；return: True, response_metadata.get('finish_reason') in _TOOL_CALL_FINISH_REASONS
  - 调用: getattr, get
  - 反射: getattr (L48)

#### `ƒ` `_tool_result_in_current_turn(messages: list[Any]) -> bool`  L57
  - _文档首行_（仅供参考）: Return whether a tool result follows the latest real user message.
  - 分支数 4，函数体节点数 95；return: False, any((isinstance(message, ToolMessage) for message in messages[latest_user_index + 1:]))
  - 调用: enumerate, isinstance, get, any

## 类
### 类 `TerminalResponseMiddleware`  L74
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Retry one empty post-tool response, then persist a visible error fallback.
- 方法:
  #### `st` `_key(runtime: Runtime) -> tuple[str, str]`    @staticmethod  L84
    - 分支数 1，函数体节点数 94；return: (thread_id, run_id), ('unknown-thread', str(id(runtime)))
    - 调用: getattr, isinstance, str, get, id
  - 反射: getattr (L85)
  #### `m` `__init__(self) -> None`  L77
    - 分支数 0，函数体节点数 75
    - 调用: __init__, super, Lock, BoundedDict
  #### `m` `_clear(self, runtime: Runtime) -> None`  L94
    - 分支数 1，函数体节点数 45
    - 调用: _key, pop
  #### `m` `_clear_other_runs(self, runtime: Runtime) -> None`  L100
    - 分支数 2，函数体节点数 87
    - 调用: _key, pop
  #### `m` `_apply(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None`  L108
    - 分支数 6，函数体节点数 231；return: None, {'messages': message_updates, 'jump_to': 'model'}, {'messages': [fallback]}
    - 调用: list, get, isinstance, _has_visible_content, _has_tool_call_intent_or_error, _tool_result_in_current_turn, _key, RemoveMessage, dict, update, model_copy
  #### `m` `_augment_request(self, request: ModelRequest) -> ModelRequest`  L151
    - 分支数 2，函数体节点数 88；return: request, request.override(messages=[*request.messages, reminder])
    - 调用: _key, pop, HumanMessage, override
  #### `m` `before_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L166
    - 分支数 0，函数体节点数 34；return: None
    - 调用: _clear_other_runs, _clear
  #### `m` `after_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None`    @hook_config(...), override  L182
    - 分支数 0，函数体节点数 41；return: self._apply(state, runtime)
    - 调用: _apply, hook_config
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L191
    - 分支数 0，函数体节点数 34；return: handler(self._augment_request(request))
    - 调用: handler, _augment_request
  #### `m` `after_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L207
    - 分支数 0，函数体节点数 26；return: None
    - 调用: _clear
  #### `⏵m` `async abefore_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L175
    - 分支数 0，函数体节点数 34；return: None
    - 调用: _clear_other_runs, _clear
  #### `⏵m` `async aafter_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None`    @hook_config(...), override  L187
    - 分支数 0，函数体节点数 41；return: self._apply(state, runtime)
    - 调用: _apply, hook_config
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L199
    - 分支数 0，函数体节点数 39；return: await handler(self._augment_request(request))
    - 调用: handler, _augment_request
  #### `⏵m` `async aafter_agent(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L212
    - 分支数 0，函数体节点数 26；return: None
    - 调用: _clear

## 文件内调用关系
- `TerminalResponseMiddleware.__init__` -> __init__
- `TerminalResponseMiddleware._clear` -> _key
- `TerminalResponseMiddleware._clear_other_runs` -> _key
- `TerminalResponseMiddleware._apply` -> _has_visible_content, _has_tool_call_intent_or_error, _tool_result_in_current_turn, _key
- `TerminalResponseMiddleware._augment_request` -> _key
- `TerminalResponseMiddleware.before_agent` -> _clear_other_runs, _clear
- `TerminalResponseMiddleware.abefore_agent` -> _clear_other_runs, _clear
- `TerminalResponseMiddleware.after_model` -> _apply
- `TerminalResponseMiddleware.aafter_model` -> _apply
- `TerminalResponseMiddleware.wrap_model_call` -> _augment_request
- `TerminalResponseMiddleware.awrap_model_call` -> _augment_request
- `TerminalResponseMiddleware.after_agent` -> _clear
- `TerminalResponseMiddleware.aafter_agent` -> _clear

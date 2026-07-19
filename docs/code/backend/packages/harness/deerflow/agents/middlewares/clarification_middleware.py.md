# `backend/packages/harness/deerflow/agents/middlewares/clarification_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/clarification_middleware.py`  ·  行数: 289

**模块文档首行**（仅供参考）: Middleware for intercepting clarification requests and presenting them to the user.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging
- `collections.abc` -> Callable
- `hashlib` -> sha256
- `typing` -> Any, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> ToolMessage
- `langgraph.graph` -> END
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `ClarificationMiddlewareState`  L19
- 继承: AgentState
- _文档首行_: Compatible with the `ThreadState` schema.

### 类 `ClarificationMiddleware`  L25
- 继承: AgentMiddleware[ClarificationMiddlewareState]
- _文档首行_: Intercepts clarification tool calls and interrupts execution to present questions to the user.
- 类/实例变量:
  - `state_schema` = ClarificationMiddlewareState
- 方法:
  #### `m` `_stable_message_id(self, tool_call_id: str, formatted_message: str) -> str`  L40
    - _文档首行_（仅供参考）: Build a deterministic message ID so retried clarification calls replace, not append.
    - 分支数 1，函数体节点数 47；return: f'clarification:{tool_call_id}', f'clarification:{digest}'
    - 调用: hexdigest, sha256, encode
  #### `m` `_normalize_options(self, raw_options: Any) -> list[str]`  L47
    - _文档首行_（仅供参考）: Normalize tool-provided options into displayable string values.
    - 分支数 4，函数体节点数 92；return: [], [str(option) for option in options]
    - 调用: isinstance, loads, str
  #### `m` `_build_human_input_payload(self, args: dict[str, Any], *, tool_call_id: str, request_id: str) -> dict[str, Any]`  L67
    - _文档首行_（仅供参考）: Build the structured UI payload while keeping ToolMessage.content as fallback.
    - 分支数 3，函数体节点数 189；return: payload
    - 调用: _normalize_options, get, str, enumerate
  #### `m` `_is_chinese(self, text: str) -> bool`  L101
    - _文档首行_（仅供参考）: Check if text contains Chinese characters.
    - 分支数 0，函数体节点数 27；return: any(('一' <= char <= '鿿' for char in text))
    - 调用: any
  #### `m` `_format_clarification_message(self, args: dict) -> str`  L112
    - _文档首行_（仅供参考）: Format the clarification arguments into a user-friendly message.
    - 分支数 3，函数体节点数 182；return: '\n'.join(message_parts)
    - 调用: get, _normalize_options, append, len, enumerate, join
  #### `m` `_is_disabled(self, request: ToolCallRequest) -> bool`  L157
    - _文档首行_（仅供参考）: Whether clarifications are suppressed for this run.
    - 分支数 1，函数体节点数 47；return: False, bool(context.get('disable_clarification'))
    - 调用: getattr, bool, get
  - 反射: getattr (L167), getattr (L168)
  #### `m` `_handle_disabled_clarification(self, request: ToolCallRequest) -> ToolMessage`  L173
    - _文档首行_（仅供参考）: Suppress a clarification and tell the agent to proceed.
    - 分支数 0，函数体节点数 49；return: ToolMessage(id=self._stable_message_id(tool_call_id, 'proceed-without-clarification'), content='Clarification is disabled in this context — the human is not present to answer synchronously. Do not ask for confirmation. Proceed with your best judgment, carry out the requested action, and state any assumptions you made in your final response.', tool_call_id=tool_call_id, name='ask_clarification')
    - 调用: get, info, ToolMessage, _stable_message_id
  #### `m` `_handle_clarification(self, request: ToolCallRequest) -> Command`  L195
    - _文档首行_（仅供参考）: Handle clarification request and return command to interrupt execution.
    - 分支数 0，函数体节点数 134；return: Command(update={'messages': [tool_message]}, goto=END)
    - 调用: get, info, debug, _format_clarification_message, _stable_message_id, _build_human_input_payload, ToolMessage, Command
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L241
    - _文档首行_（仅供参考）: Intercept ask_clarification tool calls and interrupt execution (sync version).
    - 分支数 2，函数体节点数 75；return: handler(request), self._handle_disabled_clarification(request), self._handle_clarification(request)
    - 调用: get, handler, _is_disabled, _handle_disabled_clarification, _handle_clarification
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L266
    - _文档首行_（仅供参考）: Intercept ask_clarification tool calls and interrupt execution (async version).
    - 分支数 2，函数体节点数 76；return: await handler(request), self._handle_disabled_clarification(request), self._handle_clarification(request)
    - 调用: get, handler, _is_disabled, _handle_disabled_clarification, _handle_clarification

## 文件内调用关系
- `ClarificationMiddleware._build_human_input_payload` -> _normalize_options
- `ClarificationMiddleware._format_clarification_message` -> _normalize_options
- `ClarificationMiddleware._handle_disabled_clarification` -> _stable_message_id
- `ClarificationMiddleware._handle_clarification` -> _format_clarification_message, _stable_message_id, _build_human_input_payload
- `ClarificationMiddleware.wrap_tool_call` -> _is_disabled, _handle_disabled_clarification, _handle_clarification
- `ClarificationMiddleware.awrap_tool_call` -> _is_disabled, _handle_disabled_clarification, _handle_clarification

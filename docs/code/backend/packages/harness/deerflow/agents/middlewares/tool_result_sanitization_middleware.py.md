# `backend/packages/harness/deerflow/agents/middlewares/tool_result_sanitization_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/tool_result_sanitization_middleware.py`  ·  行数: 157

**模块文档首行**（仅供参考）: Neutralize prompt-injection control tokens in untrusted tool results.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `dataclasses` -> dc_replace
- `typing` -> override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> ToolMessage
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_REMOTE_CONTENT_TOOL_NAMES` = frozenset({'web_fetch', 'web_search', 'image_search', 'we...

## 函数
#### `ƒ` `_neutralize_content(content: object) -> object`  L65
  - _文档首行_（仅供参考）: Return *content* with untrusted tags neutralized, preserving its shape.
  - 分支数 5，函数体节点数 130；return: neutralize_untrusted_tags(content), rebuilt, content
  - 调用: isinstance, neutralize_untrusted_tags, append, get

#### `ƒ` `_sanitize_tool_message(message: ToolMessage) -> ToolMessage`  L96
  - _文档首行_（仅供参考）: Return a copy of *message* with its content neutralized, or the original.
  - 分支数 1，函数体节点数 42；return: message, message.model_copy(update={'content': new_content})
  - 调用: _neutralize_content, model_copy

#### `ƒ` `_sanitize_result(result: ToolMessage | Command) -> ToolMessage | Command`  L104
  - _文档首行_（仅供参考）: Neutralize a tool-call result (``ToolMessage`` or ``Command``).
  - 分支数 4，函数体节点数 131；return: _sanitize_tool_message(result), dc_replace(result, update={**update, 'messages': new_messages}), result
  - 调用: isinstance, _sanitize_tool_message, getattr, get, any, dc_replace
  - 反射: getattr (L108)

## 类
### 类 `ToolResultSanitizationMiddleware`  L118
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Escape injection/framework tags in remote tool results before the model sees them.
- 方法:
  #### `m` `_should_sanitize(self, request: ToolCallRequest) -> bool`  L133
    - 分支数 0，函数体节点数 21；return: request.tool_call.get('name') in _REMOTE_CONTENT_TOOL_NAMES
    - 调用: get
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L137
    - 分支数 1，函数体节点数 58；return: result, _sanitize_result(result)
    - 调用: handler, _should_sanitize, _sanitize_result
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L148
    - 分支数 1，函数体节点数 63；return: result, _sanitize_result(result)
    - 调用: handler, _should_sanitize, _sanitize_result

## 文件内调用关系
- `_sanitize_tool_message` -> _neutralize_content
- `_sanitize_result` -> _sanitize_tool_message
- `ToolResultSanitizationMiddleware.wrap_tool_call` -> _should_sanitize, _sanitize_result
- `ToolResultSanitizationMiddleware.awrap_tool_call` -> _should_sanitize, _sanitize_result

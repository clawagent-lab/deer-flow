# `backend/packages/harness/deerflow/agents/middlewares/deferred_tool_filter_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/deferred_tool_filter_middleware.py`  ·  行数: 113

**模块文档首行**（仅供参考）: Middleware to filter deferred tool schemas from model binding.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `collections.abc` -> Awaitable, Callable
- `typing` -> override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> ToolMessage
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `DeferredToolFilterMiddleware`  L29
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Hide deferred tool schemas from the bound model until promoted.
- 方法:
  #### `m` `__init__(self, deferred_names: frozenset[str], catalog_hash: str | None)`  L37
    - 分支数 0，函数体节点数 37
    - 调用: __init__, super
  #### `m` `_promoted(self, state) -> set[str]`  L42
    - 分支数 1，函数体节点数 57；return: set(promoted.get('names') or []), set()
    - 调用: get, set
  #### `m` `_hidden(self, state) -> set[str]`  L48
    - 分支数 0，函数体节点数 27；return: set(self._deferred) - self._promoted(state)
    - 调用: set, _promoted
  #### `m` `_filter_tools(self, request: ModelRequest) -> ModelRequest`  L51
    - 分支数 3，函数体节点数 107；return: request, request.override(tools=active)
    - 调用: _hidden, getattr, len, debug, override
  - 反射: getattr (L57)
  #### `m` `_blocked_tool_message(self, request: ToolCallRequest) -> ToolMessage | None`  L62
    - 分支数 2，函数体节点数 95；return: None, ToolMessage(content=f"Error: Tool '{name}' is deferred and has not been promoted yet. Call tool_search first to expose and promote this tool's schema, then retry.", tool_call_id=tool_call_id, name=name, status='error')
    - 调用: str, get, _hidden, ToolMessage
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L77
    - 分支数 0，函数体节点数 34；return: handler(self._filter_tools(request))
    - 调用: handler, _filter_tools
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L85
    - 分支数 1，函数体节点数 56；return: blocked, handler(request)
    - 调用: _blocked_tool_message, handler
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L96
    - 分支数 0，函数体节点数 39；return: await handler(self._filter_tools(request))
    - 调用: handler, _filter_tools
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L104
    - 分支数 1，函数体节点数 61；return: blocked, await handler(request)
    - 调用: _blocked_tool_message, handler

## 文件内调用关系
- `DeferredToolFilterMiddleware.__init__` -> __init__
- `DeferredToolFilterMiddleware._hidden` -> _promoted
- `DeferredToolFilterMiddleware._filter_tools` -> _hidden
- `DeferredToolFilterMiddleware._blocked_tool_message` -> _hidden
- `DeferredToolFilterMiddleware.wrap_model_call` -> _filter_tools
- `DeferredToolFilterMiddleware.wrap_tool_call` -> _blocked_tool_message
- `DeferredToolFilterMiddleware.awrap_model_call` -> _filter_tools
- `DeferredToolFilterMiddleware.awrap_tool_call` -> _blocked_tool_message

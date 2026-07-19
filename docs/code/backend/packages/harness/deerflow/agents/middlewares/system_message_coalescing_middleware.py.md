# `backend/packages/harness/deerflow/agents/middlewares/system_message_coalescing_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/system_message_coalescing_middleware.py`  ·  行数: 151

**模块文档首行**（仅供参考）: Middleware to coalesce multiple SystemMessages into a single leading one.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `collections.abc` -> Awaitable, Callable
- `typing` -> override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> SystemMessage
- `deerflow.agents.middlewares.dynamic_context_middleware` -> is_dynamic_context_reminder

## 函数
#### `ƒ` `_flatten_content(content) -> str`  L41
  - _文档首行_（仅供参考）: Convert message content to a plain string, handling both str and list types.
  - 分支数 5，函数体节点数 102；return: content, '\n'.join(parts), str(content)
  - 调用: isinstance, append, str, join

#### `ƒ` `_coalesce_request(request: ModelRequest) -> ModelRequest | None`  L63
  - _文档首行_（仅供参考）: Merge ``request.system_message`` and in-``messages`` SystemMessages into one.
  - 分支数 4，函数体节点数 254；return: None, request.override(system_message=merged, messages=non_system)
  - 调用: isinstance, append, extend, enumerate, is_dynamic_context_reminder, len, update, SystemMessage, join, _flatten_content, override

## 类
### 类 `SystemMessageCoalescingMiddleware`  L119
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Merge all SystemMessages into a single leading SystemMessage.
- 方法:
  #### `st` `_maybe_coalesce(request: ModelRequest) -> ModelRequest`    @staticmethod  L130
    - 分支数 1，函数体节点数 29；return: request, coalesced
    - 调用: _coalesce_request
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L137
    - 分支数 0，函数体节点数 34；return: handler(self._maybe_coalesce(request))
    - 调用: handler, _maybe_coalesce
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L145
    - 分支数 0，函数体节点数 39；return: await handler(self._maybe_coalesce(request))
    - 调用: handler, _maybe_coalesce

## 文件内调用关系
- `_coalesce_request` -> _flatten_content
- `SystemMessageCoalescingMiddleware._maybe_coalesce` -> _coalesce_request
- `SystemMessageCoalescingMiddleware.wrap_model_call` -> _maybe_coalesce
- `SystemMessageCoalescingMiddleware.awrap_model_call` -> _maybe_coalesce

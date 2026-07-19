# `backend/packages/harness/deerflow/guardrails/middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/guardrails/middleware.py`  ·  行数: 217

**模块文档首行**（仅供参考）: GuardrailMiddleware - evaluates tool calls against a GuardrailProvider before execution.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `collections.abc` -> Awaitable, Callable
- `datetime` -> UTC, datetime
- `typing` -> override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> ToolMessage
- `langgraph.errors` -> GraphBubbleUp
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command
- `deerflow.authz.principal` -> normalize_authz_attributes
- `deerflow.guardrails.provider` -> GuardrailDecision, GuardrailProvider, GuardrailReason, GuardrailRequest

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_REASON_MESSAGE_LIMIT` = 500

## 类
### 类 `GuardrailMiddleware`  L23
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Evaluate tool calls against a GuardrailProvider before execution.
- 方法:
  #### `st` `_resolve_context(request: ToolCallRequest) -> dict`    @staticmethod  L38
    - 分支数 0，函数体节点数 48；return: context if isinstance(context, dict) else {}
    - 调用: getattr, isinstance
  - 反射: getattr (L39), getattr (L40)
  #### `m` `__init__(self, provider: GuardrailProvider, *, fail_closed: bool, passport: str | None)`  L32
    - 分支数 0，函数体节点数 38
  #### `m` `_build_request(self, request: ToolCallRequest, context: dict) -> GuardrailRequest`  L43
    - 分支数 0，函数体节点数 142；return: GuardrailRequest(tool_name=str(request.tool_call.get('name', '')), tool_input=request.tool_call.get('args', {}), agent_id=self.passport, thread_id=context.get('thread_id'), is_subagent=bool(context.get('is_subagent')), timestamp=datetime.now(UTC).isoformat(), user_id=context.get('user_id'), user_role=context.get('user_role'), oauth_provider=context.get('oauth_provider'), oauth_id=context.get('oauth_id'), run_id=context.get('run_id'), tool_call_id=request.tool_call.get('id'), channel_user_id=context.get('channel_user_id'), is_internal=context.get('is_internal') is True, authz_attributes=normalize_authz_attributes(context.get('authz_attributes')))
    - 调用: GuardrailRequest, str, get, bool, isoformat, now, normalize_authz_attributes
  #### `m` `_build_denied_message(self, request: ToolCallRequest, decision: GuardrailDecision) -> ToolMessage`  L62
    - 分支数 0，函数体节点数 104；return: ToolMessage(content=f"Guardrail denied: tool '{tool_name}' was blocked ({reason_code}). Reason: {reason_text}. Choose an alternative approach.", tool_call_id=tool_call_id, name=tool_name, status='error')
    - 调用: str, get, ToolMessage
  #### `m` `_record_guardrail_event(self, context: dict, guardrail_request: GuardrailRequest, decision: GuardrailDecision, *, action: str, provider_error: bool) -> None`  L74
    - _文档首行_（仅供参考）: Persist a security-relevant guardrail decision to RunJournal.
    - 分支数 2，函数体节点数 170；return: None
    - 调用: get, record_middleware, type, debug
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L125
    - 分支数 3，函数体节点数 238；raise: bare raise；return: self._build_denied_message(request, decision), handler(request)
    - 调用: _resolve_context, _build_request, evaluate, exception, GuardrailDecision, GuardrailReason, _record_guardrail_event, _build_denied_message, handler, warning
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L172
    - 分支数 3，函数体节点数 245；raise: bare raise；return: self._build_denied_message(request, decision), await handler(request)
    - 调用: _resolve_context, _build_request, aevaluate, exception, GuardrailDecision, GuardrailReason, _record_guardrail_event, _build_denied_message, handler, warning

## 文件内调用关系
- `GuardrailMiddleware.wrap_tool_call` -> _resolve_context, _build_request, _record_guardrail_event, _build_denied_message
- `GuardrailMiddleware.awrap_tool_call` -> _resolve_context, _build_request, _record_guardrail_event, _build_denied_message

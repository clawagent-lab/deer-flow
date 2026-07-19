# `backend/packages/harness/deerflow/authz/adapter.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/authz/adapter.py`  ·  行数: 117

**模块文档首行**（仅供参考）: Adapter that presents an AuthorizationProvider as a GuardrailProvider.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `deerflow.authz.principal` -> build_principal_from_context
- `deerflow.authz.provider` -> AuthorizationProvider, AuthzDecision, AuthzRequest
- `deerflow.guardrails.provider` -> GuardrailDecision, GuardrailReason, GuardrailRequest

## 类
### 类 `GuardrailAuthorizationAdapter`  L25
- _文档首行_: Adapt an :class:`AuthorizationProvider` to the ``GuardrailProvider`` Protocol.
- 类/实例变量:
  - `name` = 'authorization'
- 方法:
  #### `st` `_to_guardrail(d: AuthzDecision) -> GuardrailDecision`    @staticmethod  L87
    - _文档首行_（仅供参考）: Convert an authorization decision to a guardrail decision.
    - 分支数 0，函数体节点数 52；return: GuardrailDecision(allow=d.allow, reasons=[GuardrailReason(code=r.code, message=r.message) for r in d.reasons], policy_id=d.policy_id, metadata=d.metadata)
    - 调用: GuardrailDecision, GuardrailReason
  #### `m` `__init__(self, provider: AuthorizationProvider, *, default_role: str, resource_type: str, action: str) -> None`  L43
    - 分支数 0，函数体节点数 47
  #### `m` `_to_authz(self, gr: GuardrailRequest) -> AuthzRequest`  L56
    - _文档首行_（仅供参考）: Map a guardrail request to an authorization request.
    - 分支数 0，函数体节点数 116；return: AuthzRequest(principal=principal, resource=self._resource_type, action=self._action, target=gr.tool_name, context={'thread_id': gr.thread_id, 'run_id': gr.run_id, 'tool_call_id': gr.tool_call_id, 'tool_input': gr.tool_input, 'is_subagent': gr.is_subagent, 'agent_id': gr.agent_id, 'timestamp': gr.timestamp})
    - 调用: build_principal_from_context, AuthzRequest
  #### `m` `evaluate(self, request: GuardrailRequest) -> GuardrailDecision`  L96
    - _文档首行_（仅供参考）: Synchronous evaluation: delegate to ``provider.authorize``.
    - 分支数 0，函数体节点数 35；return: self._to_guardrail(decision)
    - 调用: authorize, _to_authz, _to_guardrail
  #### `⏵m` `async aevaluate(self, request: GuardrailRequest) -> GuardrailDecision`  L110
    - _文档首行_（仅供参考）: Async evaluation: delegate to ``provider.aauthorize``.
    - 分支数 0，函数体节点数 36；return: self._to_guardrail(decision)
    - 调用: aauthorize, _to_authz, _to_guardrail

## 文件内调用关系
- `GuardrailAuthorizationAdapter.evaluate` -> _to_authz, _to_guardrail
- `GuardrailAuthorizationAdapter.aevaluate` -> _to_authz, _to_guardrail

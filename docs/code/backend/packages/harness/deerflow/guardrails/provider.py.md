# `backend/packages/harness/deerflow/guardrails/provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/guardrails/provider.py`  ·  行数: 69

**模块文档首行**（仅供参考）: GuardrailProvider protocol and data structures for pre-tool-call authorization.

## 模块概览
- 函数 0 个，类 4 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass, field
- `typing` -> Any, Protocol, runtime_checkable

## 类
### 类 `GuardrailRequest`  L10  @dataclass
- _文档首行_: Context passed to the provider for each tool call.
- 类/实例变量:
  - `tool_name` = <annotated>
  - `tool_input` = <annotated>
  - `agent_id` = None
  - `thread_id` = None
  - `is_subagent` = False
  - `timestamp` = ''
  - `user_id` = None
  - `user_role` = None
  - `oauth_provider` = None
  - `oauth_id` = None
  - `run_id` = None
  - `tool_call_id` = None
  - `channel_user_id` = None
  - `is_internal` = False
  - `authz_attributes` = field(default_factory=dict)

### 类 `GuardrailReason`  L34  @dataclass
- _文档首行_: Structured reason for an allow/deny decision (OAP reason object).
- 类/实例变量:
  - `code` = <annotated>
  - `message` = ''

### 类 `GuardrailDecision`  L42  @dataclass
- _文档首行_: Provider's allow/deny verdict (aligned with OAP Decision object).
- 类/实例变量:
  - `allow` = <annotated>
  - `reasons` = field(default_factory=list)
  - `policy_id` = None
  - `metadata` = field(default_factory=dict)

### 类 `GuardrailProvider`  L52  @runtime_checkable
- 继承: Protocol
- _文档首行_: Contract for pluggable tool-call authorization.
- 类/实例变量:
  - `name` = <annotated>
- 方法:
  #### `m` `evaluate(self, request: GuardrailRequest) -> GuardrailDecision`  L62
    - _文档首行_（仅供参考）: Evaluate whether a tool call should proceed.
    - 分支数 0，函数体节点数 12
  #### `⏵m` `async aevaluate(self, request: GuardrailRequest) -> GuardrailDecision`  L66
    - _文档首行_（仅供参考）: Async variant.
    - 分支数 0，函数体节点数 12

## 文件内调用关系
_无文件内调用_

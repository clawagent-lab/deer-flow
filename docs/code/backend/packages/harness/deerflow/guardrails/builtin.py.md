# `backend/packages/harness/deerflow/guardrails/builtin.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/guardrails/builtin.py`  ·  行数: 28

**模块文档首行**（仅供参考）: Built-in guardrail providers that ship with DeerFlow.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `deerflow.guardrails.provider` -> GuardrailDecision, GuardrailReason, GuardrailRequest

## 类
### 类 `AllowlistProvider`  L6
- _文档首行_: Simple allowlist/denylist provider. No external dependencies.
- 类/实例变量:
  - `name` = 'allowlist'
- 方法:
  #### `m` `__init__(self, *, allowed_tools: list[str] | None, denied_tools: list[str] | None)`  L11
    - 分支数 0，函数体节点数 58
    - 调用: set
  #### `m` `evaluate(self, request: GuardrailRequest) -> GuardrailDecision`  L19
    - 分支数 2，函数体节点数 99；return: GuardrailDecision(allow=False, reasons=[GuardrailReason(code='oap.tool_not_allowed', message=f"tool '{request.tool_name}' not in allowlist")]), GuardrailDecision(allow=False, reasons=[GuardrailReason(code='oap.tool_not_allowed', message=f"tool '{request.tool_name}' is denied")]), GuardrailDecision(allow=True, reasons=[GuardrailReason(code='oap.allowed')])
    - 调用: GuardrailDecision, GuardrailReason
  #### `⏵m` `async aevaluate(self, request: GuardrailRequest) -> GuardrailDecision`  L26
    - 分支数 0，函数体节点数 16；return: self.evaluate(request)
    - 调用: evaluate

## 文件内调用关系
- `AllowlistProvider.aevaluate` -> evaluate

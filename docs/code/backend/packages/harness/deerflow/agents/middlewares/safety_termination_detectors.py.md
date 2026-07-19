# `backend/packages/harness/deerflow/agents/middlewares/safety_termination_detectors.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/safety_termination_detectors.py`  ·  行数: 238

**模块文档首行**（仅供参考）: Detectors for provider-side safety termination signals.

## 模块概览
- 函数 2 个，类 5 个，模块级常量 1 个
- `__all__`: AnthropicRefusalDetector, GeminiSafetyDetector, OpenAICompatibleContentFilterDetector, SafetyTermination, SafetyTerminationDetector, default_detectors

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass, field
- `typing` -> Any, Protocol, runtime_checkable
- `langchain_core.messages` -> AIMessage

## 模块级常量
- `__all__` = ['AnthropicRefusalDetector', 'GeminiSafetyDetector', 'Ope...

## 函数
#### `ƒ` `_get_metadata_value(message: AIMessage, field_name: str) -> str | None`  L61
  - _文档首行_（仅供参考）: Read a string-typed value from either ``response_metadata`` or
  - 分支数 3，函数体节点数 74；return: value, None
  - 调用: getattr, isinstance, get
  - 反射: getattr (L73)

#### `ƒ` `default_detectors() -> list[SafetyTerminationDetector]`  L221
  - _文档首行_（仅供参考）: Built-in detector set used when no custom detectors are configured.
  - 分支数 0，函数体节点数 22；return: [OpenAICompatibleContentFilterDetector(), AnthropicRefusalDetector(), GeminiSafetyDetector()]
  - 调用: OpenAICompatibleContentFilterDetector, AnthropicRefusalDetector, GeminiSafetyDetector

## 类
### 类 `SafetyTermination`  L24  @dataclass(...)
- _文档首行_: A detected safety-related termination signal.
- 类/实例变量:
  - `detector` = <annotated>
  - `reason_field` = <annotated>
  - `reason_value` = <annotated>
  - `extras` = field(default_factory=dict)

### 类 `SafetyTerminationDetector`  L46  @runtime_checkable
- 继承: Protocol
- _文档首行_: Strategy interface for provider safety termination detection.
- 类/实例变量:
  - `name` = <annotated>
- 方法:
  #### `m` `detect(self, message: AIMessage) -> SafetyTermination | None`  L51
    - _文档首行_（仅供参考）: Return a SafetyTermination if *message* indicates provider safety
    - 分支数 0，函数体节点数 15

### 类 `OpenAICompatibleContentFilterDetector`  L82
- _文档首行_: OpenAI-compatible content_filter signal.
- 类/实例变量:
  - `name` = 'openai_compatible_content_filter'
- 方法:
  #### `m` `__init__(self, finish_reasons: list[str] | tuple[str, ...] | None) -> None`  L96
    - 分支数 0，函数体节点数 65
    - 调用: frozenset, lower
  #### `m` `detect(self, message: AIMessage) -> SafetyTermination | None`  L100
    - 分支数 3，函数体节点数 113；return: None, SafetyTermination(detector=self.name, reason_field='finish_reason', reason_value=value, extras=extras)
    - 调用: _get_metadata_value, lower, getattr, isinstance, get, SafetyTermination
  - 反射: getattr (L108)

### 类 `AnthropicRefusalDetector`  L122
- _文档首行_: Anthropic ``stop_reason == "refusal"`` signal.
- 类/实例变量:
  - `name` = 'anthropic_refusal'
- 方法:
  #### `m` `__init__(self, stop_reasons: list[str] | tuple[str, ...] | None) -> None`  L132
    - 分支数 0，函数体节点数 65
    - 调用: frozenset, lower
  #### `m` `detect(self, message: AIMessage) -> SafetyTermination | None`  L136
    - 分支数 1，函数体节点数 55；return: None, SafetyTermination(detector=self.name, reason_field='stop_reason', reason_value=value)
    - 调用: _get_metadata_value, lower, SafetyTermination

### 类 `GeminiSafetyDetector`  L147
- _文档首行_: Gemini / Vertex AI safety-related finish reasons.
- 类/实例变量:
  - `name` = 'gemini_safety'
  - `_DEFAULT_FINISH_REASONS` = ('SAFETY', 'BLOCKLIST', 'PROHIBITED_CONTENT', 'SPII', 'RE...
- 方法:
  #### `m` `__init__(self, finish_reasons: list[str] | tuple[str, ...] | None) -> None`  L196
    - 分支数 0，函数体节点数 66
    - 调用: frozenset, upper
  #### `m` `detect(self, message: AIMessage) -> SafetyTermination | None`  L200
    - 分支数 3，函数体节点数 113；return: None, SafetyTermination(detector=self.name, reason_field='finish_reason', reason_value=value, extras=extras)
    - 调用: _get_metadata_value, upper, getattr, isinstance, get, SafetyTermination
  - 反射: getattr (L206)

## 文件内调用关系
- `OpenAICompatibleContentFilterDetector.detect` -> _get_metadata_value
- `AnthropicRefusalDetector.detect` -> _get_metadata_value
- `GeminiSafetyDetector.detect` -> _get_metadata_value

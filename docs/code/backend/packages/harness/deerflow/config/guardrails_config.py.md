# `backend/packages/harness/deerflow/config/guardrails_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/guardrails_config.py`  ·  行数: 49

**模块文档首行**（仅供参考）: Configuration for pre-tool-call authorization.

## 模块概览
- 函数 3 个，类 2 个，模块级常量 1 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 模块级常量
- `_guardrails_config` = None

## 函数
#### `ƒ` `get_guardrails_config() -> GuardrailsConfig`  L30
  - _文档首行_（仅供参考）: Get the guardrails config, returning defaults if not loaded.
  - 分支数 1，函数体节点数 22；return: _guardrails_config
  - 调用: GuardrailsConfig

#### `ƒ` `load_guardrails_config_from_dict(data: dict) -> GuardrailsConfig`  L38
  - _文档首行_（仅供参考）: Load guardrails config from a dict (called during AppConfig loading).
  - 分支数 0，函数体节点数 23；return: _guardrails_config
  - 调用: model_validate

#### `ƒ` `reset_guardrails_config() -> None`  L45
  - _文档首行_（仅供参考）: Reset the cached config instance. Used in tests to prevent singleton leaks.
  - 分支数 0，函数体节点数 10

## 类
### 类 `GuardrailProviderConfig`  L6
- 继承: BaseModel
- _文档首行_: Configuration for a guardrail provider.
- 类/实例变量:
  - `use` = Field(description="Class path (e.g. 'deerflow.guardrails....
  - `config` = Field(default_factory=dict, description='Provider-specifi...

### 类 `GuardrailsConfig`  L13
- 继承: BaseModel
- _文档首行_: Configuration for pre-tool-call authorization.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Enable guardrail middle...
  - `fail_closed` = Field(default=True, description='Block tool calls if prov...
  - `passport` = Field(default=None, description='OAP passport path or hos...
  - `provider` = Field(default=None, description='Guardrail provider confi...

## 文件内调用关系
_无文件内调用_

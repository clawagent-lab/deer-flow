# `backend/packages/harness/deerflow/config/token_budget_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/token_budget_config.py`  ·  行数: 22

**模块文档首行**（仅供参考）: Config for token budget middleware.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `pydantic` -> BaseModel, Field, model_validator

## 类
### 类 `TokenBudgetConfig`  L6
- 继承: BaseModel
- _文档首行_: Configuration for per-run token budget enforcement.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Whether to enable per-r...
  - `max_tokens` = Field(default=200000, ge=1000, description='Maximum total...
  - `max_input_tokens` = Field(default=None, ge=1, description='Optional separate ...
  - `max_output_tokens` = Field(default=None, ge=1, description='Optional separate ...
  - `warn_threshold` = Field(default=0.8, ge=0.0, le=1.0, description='Fraction ...
  - `hard_stop_threshold` = Field(default=1.0, ge=0.0, le=1.0, description='Fraction ...
- 方法:
  #### `m` `validate_thresholds(self) -> 'TokenBudgetConfig'`    @model_validator(...)  L17
    - _文档首行_（仅供参考）: Ensure hard stop cannot trigger before the warning.
    - 分支数 1，函数体节点数 30；raise: ValueError('hard_stop_threshold must be >= warn_threshold')；return: self
    - 调用: ValueError, model_validator

## 文件内调用关系
_无文件内调用_

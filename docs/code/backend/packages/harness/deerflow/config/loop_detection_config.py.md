# `backend/packages/harness/deerflow/config/loop_detection_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/loop_detection_config.py`  ·  行数: 74

**模块文档首行**（仅供参考）: Configuration for loop detection middleware.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 0 个

## 依赖（import）
- `pydantic` -> BaseModel, Field, model_validator

## 类
### 类 `ToolFreqOverride`  L6
- 继承: BaseModel
- _文档首行_: Per-tool frequency threshold override.
- 类/实例变量:
  - `warn` = Field(ge=1)
  - `hard_limit` = Field(ge=1)
- 方法:
  #### `m` `_validate(self) -> 'ToolFreqOverride'`    @model_validator(...)  L18
    - 分支数 1，函数体节点数 28；raise: ValueError('hard_limit must be >= warn')；return: self
    - 调用: ValueError, model_validator

### 类 `LoopDetectionConfig`  L24
- 继承: BaseModel
- _文档首行_: Configuration for repetitive tool-call loop detection.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether to enable repeti...
  - `warn_threshold` = Field(default=3, ge=1, description='Number of identical t...
  - `hard_limit` = Field(default=5, ge=1, description='Number of identical t...
  - `window_size` = Field(default=20, ge=1, description='Number of recent too...
  - `max_tracked_threads` = Field(default=100, ge=1, description='Maximum number of t...
  - `tool_freq_warn` = Field(default=30, ge=1, description='Number of calls to t...
  - `tool_freq_hard_limit` = Field(default=50, ge=1, description='Number of calls to t...
  - `tool_freq_overrides` = Field(default_factory=dict, description='Per-tool overrid...
- 方法:
  #### `m` `validate_thresholds(self) -> 'LoopDetectionConfig'`    @model_validator(...)  L67
    - _文档首行_（仅供参考）: Ensure hard stop cannot happen before the warning threshold.
    - 分支数 2，函数体节点数 46；raise: ValueError('hard_limit must be greater than or equal to warn_threshold'), ValueError('tool_freq_hard_limit must be greater than or equal to tool_freq_warn')；return: self
    - 调用: ValueError, model_validator

## 文件内调用关系
_无文件内调用_

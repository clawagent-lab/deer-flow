# `backend/packages/harness/deerflow/config/summarization_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/summarization_config.py`  ·  行数: 80

**模块文档首行**（仅供参考）: Configuration for conversation summarization.

## 模块概览
- 函数 3 个，类 2 个，模块级常量 3 个

## 依赖（import）
- `typing` -> Literal
- `pydantic` -> BaseModel, Field

## 模块级常量
- `ContextSizeType` = Literal['fraction', 'tokens', 'messages']
- `DEFAULT_SKILL_FILE_READ_TOOL_NAMES` = ('read_file', 'read', 'view', 'cat')
- `_summarization_config` = SummarizationConfig()

## 函数
#### `ƒ` `get_summarization_config() -> SummarizationConfig`  L65
  - _文档首行_（仅供参考）: Get the current summarization configuration.
  - 分支数 0，函数体节点数 9；return: _summarization_config

#### `ƒ` `set_summarization_config(config: SummarizationConfig) -> None`  L70
  - _文档首行_（仅供参考）: Set the summarization configuration.
  - 分支数 0，函数体节点数 14

#### `ƒ` `load_summarization_config_from_dict(config_dict: dict) -> None`  L76
  - _文档首行_（仅供参考）: Load summarization configuration from a dictionary.
  - 分支数 0，函数体节点数 18
  - 调用: SummarizationConfig

## 类
### 类 `ContextSize`  L11
- 继承: BaseModel
- _文档首行_: Context size specification for trigger or keep parameters.
- 类/实例变量:
  - `type` = Field(description='Type of context size specification')
  - `value` = Field(description='Value for the context size specificati...
- 方法:
  #### `m` `to_tuple(self) -> tuple[ContextSizeType, int | float]`  L17
    - _文档首行_（仅供参考）: Convert to tuple format expected by SummarizationMiddleware.
    - 分支数 0，函数体节点数 30；return: (self.type, self.value)

### 类 `SummarizationConfig`  L22
- 继承: BaseModel
- _文档首行_: Configuration for automatic conversation summarization.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Whether to enable autom...
  - `model_name` = Field(default=None, description='Model name to use for su...
  - `trigger` = Field(default=None, description="One or more thresholds t...
  - `keep` = Field(default_factory=lambda: ContextSize(type='messages'...
  - `trim_tokens_to_summarize` = Field(default=4000, description='Maximum tokens to keep w...
  - `summary_prompt` = Field(default=None, description='Custom prompt template f...
  - `skill_file_read_tool_names` = Field(default_factory=lambda: list(DEFAULT_SKILL_FILE_REA...

## 文件内调用关系
_无文件内调用_

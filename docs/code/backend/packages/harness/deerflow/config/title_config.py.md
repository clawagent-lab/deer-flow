# `backend/packages/harness/deerflow/config/title_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/title_config.py`  ·  行数: 67

**模块文档首行**（仅供参考）: Configuration for automatic thread title generation.

## 模块概览
- 函数 4 个，类 1 个，模块级常量 1 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 模块级常量
- `_title_config` = TitleConfig()

## 函数
#### `ƒ` `get_title_config() -> TitleConfig`  L39
  - _文档首行_（仅供参考）: Get the current title configuration.
  - 分支数 0，函数体节点数 9；return: _title_config

#### `ƒ` `set_title_config(config: TitleConfig) -> None`  L44
  - _文档首行_（仅供参考）: Set the title configuration.
  - 分支数 0，函数体节点数 14

#### `ƒ` `load_title_config_from_dict(config_dict: dict) -> None`  L50
  - _文档首行_（仅供参考）: Load title configuration from a dictionary.
  - 分支数 0，函数体节点数 18
  - 调用: TitleConfig

#### `ƒ` `reset_title_config() -> None`  L56
  - _文档首行_（仅供参考）: Restore the title configuration to its pristine ``TitleConfig()`` default.
  - 分支数 0，函数体节点数 12
  - 调用: TitleConfig

## 类
### 类 `TitleConfig`  L6
- 继承: BaseModel
- _文档首行_: Configuration for automatic thread title generation.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether to enable automa...
  - `max_words` = Field(default=6, ge=1, le=20, description='Maximum number...
  - `max_chars` = Field(default=60, ge=10, le=200, description='Maximum num...
  - `model_name` = Field(default=None, description='Model name to use for LL...
  - `prompt_template` = Field(default='Generate a concise title (max {max_words} ...

## 文件内调用关系
_无文件内调用_

# `backend/packages/harness/deerflow/config/checkpointer_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/checkpointer_config.py`  ·  行数: 65

**模块文档首行**（仅供参考）: Configuration for LangGraph checkpointer.

## 模块概览
- 函数 4 个，类 1 个，模块级常量 2 个

## 依赖（import）
- `typing` -> Literal
- `pydantic` -> BaseModel, Field

## 模块级常量
- `CheckpointerType` = Literal['memory', 'sqlite', 'postgres']
- `_checkpointer_config` = None

## 函数
#### `ƒ` `get_checkpointer_config() -> CheckpointerConfig | None`  L33
  - _文档首行_（仅供参考）: Get the current checkpointer configuration, or None if not configured.
  - 分支数 0，函数体节点数 12；return: _checkpointer_config

#### `ƒ` `set_checkpointer_config(config: CheckpointerConfig | None) -> None`  L38
  - _文档首行_（仅供参考）: Set the checkpointer configuration.
  - 分支数 0，函数体节点数 17

#### `ƒ` `ensure_config_loaded() -> None`  L44
  - _文档首行_（仅供参考）: Lazily load app config when checkpointer config has not been initialized.
  - 分支数 2，函数体节点数 37；return: None
  - 调用: get_checkpointer_config, get_app_config

#### `ƒ` `load_checkpointer_config_from_dict(config_dict: dict | None) -> None`  L58
  - _文档首行_（仅供参考）: Load checkpointer configuration from a dictionary.
  - 分支数 1，函数体节点数 32；return: None
  - 调用: CheckpointerConfig

## 类
### 类 `CheckpointerConfig`  L10
- 继承: BaseModel
- _文档首行_: Configuration for LangGraph state persistence checkpointer.
- 类/实例变量:
  - `type` = Field(description="Checkpointer backend type. 'memory' is...
  - `connection_string` = Field(default=None, description="Connection string for sq...

## 文件内调用关系
- `ensure_config_loaded` -> get_checkpointer_config

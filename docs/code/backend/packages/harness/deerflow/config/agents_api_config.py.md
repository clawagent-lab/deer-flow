# `backend/packages/harness/deerflow/config/agents_api_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/agents_api_config.py`  ·  行数: 33

**模块文档首行**（仅供参考）: Configuration for the custom agents management API.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 1 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 模块级常量
- `_agents_api_config` = AgentsApiConfig()

## 函数
#### `ƒ` `get_agents_api_config() -> AgentsApiConfig`  L18
  - _文档首行_（仅供参考）: Get the current agents API configuration.
  - 分支数 0，函数体节点数 9；return: _agents_api_config

#### `ƒ` `set_agents_api_config(config: AgentsApiConfig) -> None`  L23
  - _文档首行_（仅供参考）: Set the agents API configuration.
  - 分支数 0，函数体节点数 14

#### `ƒ` `load_agents_api_config_from_dict(config_dict: dict) -> None`  L29
  - _文档首行_（仅供参考）: Load agents API configuration from a dictionary.
  - 分支数 0，函数体节点数 18
  - 调用: AgentsApiConfig

## 类
### 类 `AgentsApiConfig`  L6
- 继承: BaseModel
- _文档首行_: Configuration for custom-agent and user-profile management routes.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Whether to expose the c...

## 文件内调用关系
_无文件内调用_

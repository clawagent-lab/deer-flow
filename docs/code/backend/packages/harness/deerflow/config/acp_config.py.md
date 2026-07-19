# `backend/packages/harness/deerflow/config/acp_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/acp_config.py`  ·  行数: 52

**模块文档首行**（仅供参考）: ACP (Agent Client Protocol) agent configuration loaded from config.yaml.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `collections.abc` -> Mapping
- `pydantic` -> BaseModel, Field

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_acp_agents` = {}

## 函数
#### `ƒ` `get_acp_agents() -> dict[str, ACPAgentConfig]`  L32
  - _文档首行_（仅供参考）: Get the currently configured ACP agents.
  - 分支数 0，函数体节点数 17；return: _acp_agents

#### `ƒ` `load_acp_config_from_dict(config_dict: Mapping[str, Mapping[str, object]] | None) -> None`  L41
  - _文档首行_（仅供参考）: Load ACP agent configuration from a dictionary (typically from config.yaml).
  - 分支数 1，函数体节点数 82
  - 调用: ACPAgentConfig, items, info, len, list, keys

## 类
### 类 `ACPAgentConfig`  L11
- 继承: BaseModel
- _文档首行_: Configuration for a single ACP-compatible agent.
- 类/实例变量:
  - `command` = Field(description='Command to launch the ACP agent subpro...
  - `args` = Field(default_factory=list, description='Additional comma...
  - `env` = Field(default_factory=dict, description='Environment vari...
  - `description` = Field(description="Description of the agent's capabilitie...
  - `model` = Field(default=None, description='Model hint passed to the...
  - `auto_approve_permissions` = Field(default=False, description='When True, DeerFlow aut...

## 文件内调用关系
_无文件内调用_

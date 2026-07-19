# `backend/packages/harness/deerflow/config/extensions_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/extensions_config.py`  ·  行数: 347

**模块文档首行**（仅供参考）: Unified extensions configuration for MCP servers and skills.

## 模块概览
- 函数 5 个，类 6 个，模块级常量 2 个

## 依赖（import）
- 模块: json, logging, os
- `pathlib` -> Path
- `typing` -> Any, Literal
- `pydantic` -> BaseModel, ConfigDict, Field, field_validator, model_validator
- `deerflow.config.runtime_paths` -> existing_project_file

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_extensions_config` = None

## 函数
#### `ƒ` `resolve_effective_mcp_routing(server_config: McpServerConfig | None, original_tool_name: str) -> dict[str, Any]`  L114
  - _文档首行_（仅供参考）: Merge server-level routing with per-tool overrides for one MCP tool.
  - 分支数 2，函数体节点数 97；return: McpRoutingConfig().model_dump(mode='json'), effective
  - 调用: model_dump, McpRoutingConfig, get, update

#### `ƒ` `get_extensions_config() -> ExtensionsConfig`  L293
  - _文档首行_（仅供参考）: Get the extensions config instance.
  - 分支数 1，函数体节点数 24；return: _extensions_config
  - 调用: from_file

#### `ƒ` `reload_extensions_config(config_path: str | None) -> ExtensionsConfig`  L308
  - _文档首行_（仅供参考）: Reload the extensions config from file and update the cached instance.
  - 分支数 0，函数体节点数 27；return: _extensions_config
  - 调用: from_file

#### `ƒ` `reset_extensions_config() -> None`  L326
  - _文档首行_（仅供参考）: Reset the cached extensions config instance.
  - 分支数 0，函数体节点数 10

#### `ƒ` `set_extensions_config(config: ExtensionsConfig) -> None`  L337
  - _文档首行_（仅供参考）: Set a custom extensions config instance.
  - 分支数 0，函数体节点数 14

## 类
### 类 `McpRoutingConfig`  L16
- 继承: BaseModel
- _文档首行_: Soft routing hints for MCP tool preference.
- 类/实例变量:
  - `mode` = Field(default='off', description='Whether to emit prompt ...
  - `priority` = Field(default=0, description='Ordering key for routing hi...
  - `keywords` = Field(default_factory=list, description='Operator-authore...
  - `model_config` = ConfigDict(extra='forbid')
- 方法:
  #### `cls` `_clamp_priority(cls, value: int) -> int`    @field_validator(...), classmethod  L35
    - 分支数 2，函数体节点数 51；return: 0, 100, value
    - 调用: warning, field_validator

### 类 `McpToolOverride`  L45
- 继承: BaseModel
- _文档首行_: Per-tool MCP configuration overrides.
- 类/实例变量:
  - `routing` = Field(default_factory=McpRoutingConfig)
  - `model_config` = ConfigDict(extra='allow')

### 类 `McpOAuthConfig`  L52
- 继承: BaseModel
- _文档首行_: OAuth configuration for an MCP server (HTTP/SSE transports).
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether OAuth token inje...
  - `token_url` = Field(description='OAuth token endpoint URL')
  - `grant_type` = Field(default='client_credentials', description='OAuth gr...
  - `client_id` = Field(default=None, description='OAuth client ID')
  - `client_secret` = Field(default=None, description='OAuth client secret')
  - `refresh_token` = Field(default=None, description='OAuth refresh token (for...
  - `scope` = Field(default=None, description='OAuth scope')
  - `audience` = Field(default=None, description='OAuth audience (provider...
  - `token_field` = Field(default='access_token', description='Field name con...
  - `token_type_field` = Field(default='token_type', description='Field name conta...
  - `expires_in_field` = Field(default='expires_in', description='Field name conta...
  - `default_token_type` = Field(default='Bearer', description='Default token type w...
  - `refresh_skew_seconds` = Field(default=60, description='Refresh token this many se...
  - `extra_token_params` = Field(default_factory=dict, description='Additional form ...
  - `model_config` = ConfigDict(extra='allow')

### 类 `McpServerConfig`  L75
- 继承: BaseModel
- _文档首行_: Configuration for a single MCP server.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether this MCP server ...
  - `type` = Field(default='stdio', description="Transport type: 'stdi...
  - `command` = Field(default=None, description='Command to execute to st...
  - `args` = Field(default_factory=list, description='Arguments to pas...
  - `env` = Field(default_factory=dict, description='Environment vari...
  - `url` = Field(default=None, description='URL of the MCP server (f...
  - `headers` = Field(default_factory=dict, description='HTTP headers to ...
  - `oauth` = Field(default=None, description='OAuth configuration (for...
  - `description` = Field(default='', description='Human-readable description...
  - `routing` = Field(default_factory=McpRoutingConfig, description='Soft...
  - `tools` = Field(default_factory=dict, description='Per-original-too...
  - `tool_call_timeout` = Field(default=None, description='Timeout in seconds for i...
  - `model_config` = ConfigDict(extra='allow')
- 方法:
  #### `cls` `_accept_transport_alias(cls, data: Any) -> Any`    @model_validator(...), classmethod  L97
    - _文档首行_（仅供参考）: Accept the MCP-spec ``transport`` field as an alias for ``type``.
    - 分支数 2，函数体节点数 59；return: data
    - 调用: isinstance, get, model_validator

### 类 `SkillStateConfig`  L126
- 继承: BaseModel
- _文档首行_: Configuration for a single skill's state.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether this skill is en...

### 类 `ExtensionsConfig`  L132
- 继承: BaseModel
- _文档首行_: Unified configuration for MCP servers and skills.
- 类/实例变量:
  - `mcp_servers` = Field(default_factory=dict, description='Map of MCP serve...
  - `skills` = Field(default_factory=dict, description='Map of skill nam...
  - `model_config` = ConfigDict(extra='allow', populate_by_name=True)
- 方法:
  #### `cls` `resolve_config_path(cls, config_path: str | None) -> Path | None`    @classmethod  L147
    - _文档首行_（仅供参考）: Resolve the extensions config file path.
    - 分支数 7，函数体节点数 167；raise: FileNotFoundError(f'Extensions config file specified by param `config_path` not found at {path}'), FileNotFoundError(f'Extensions config file specified by environment variable `DEER_FLOW_EXTENSIONS_CONFIG_PATH` not found at {path}')；return: path, project_config, None
    - 调用: Path, exists, FileNotFoundError, getenv, existing_project_file, resolve
  - 文件IO: exists (L172), exists (L177), exists (L193)
  - 环境变量: getenv (L175), getenv (L176)
  #### `cls` `from_file(cls, config_path: str | None) -> 'ExtensionsConfig'`    @classmethod  L200
    - _文档首行_（仅供参考）: Load extensions config from JSON file.
    - 分支数 3，函数体节点数 117；raise: ValueError(f'Extensions config file at {resolved_path} is not valid JSON: {e}'), RuntimeError(f'Failed to load extensions config from {resolved_path}: {e}')；return: cls(mcp_servers={}, skills={}), cls.model_validate(config_data)
    - 调用: resolve_config_path, cls, open, load, resolve_env_variables, model_validate, ValueError, RuntimeError
  - 文件IO: open (L217)
  #### `cls` `resolve_env_variables(cls, config: Any) -> Any`    @classmethod  L227
    - _文档首行_（仅供参考）: Recursively resolve environment variables in the config.
    - 分支数 6，函数体节点数 138；return: config, '', env_value, {key: cls.resolve_env_variables(value) for key, value in config.items()}, [cls.resolve_env_variables(item) for item in config], tuple((cls.resolve_env_variables(item) for item in config))
    - 调用: isinstance, startswith, getenv, resolve_env_variables, items, tuple
  - 环境变量: getenv (L241)
  #### `m` `get_enabled_mcp_servers(self) -> dict[str, McpServerConfig]`  L260
    - _文档首行_（仅供参考）: Get only the enabled MCP servers.
    - 分支数 0，函数体节点数 39；return: {name: config for name, config in self.mcp_servers.items() if config.enabled}
    - 调用: items
  #### `m` `is_skill_enabled(self, skill_name: str, skill_category: str) -> bool`  L268
    - _文档首行_（仅供参考）: Check if a skill is enabled.
    - 分支数 1，函数体节点数 46；return: skill_category in ('public', 'custom', 'legacy'), skill_config.enabled
    - 调用: get

## 文件内调用关系
- `get_extensions_config` -> from_file
- `reload_extensions_config` -> from_file
- `ExtensionsConfig.from_file` -> resolve_config_path, resolve_env_variables
- `ExtensionsConfig.resolve_env_variables` -> resolve_env_variables

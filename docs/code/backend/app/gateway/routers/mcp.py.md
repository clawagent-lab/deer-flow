# `backend/app/gateway/routers/mcp.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/mcp.py`  ·  行数: 483

## 模块概览
- 函数 13 个，类 5 个，模块级常量 9 个

## 依赖（import）
- 模块: asyncio, json, logging, os, re
- `pathlib` -> Path
- `typing` -> Any, Literal
- `fastapi` -> APIRouter, HTTPException, Request, status
- `pydantic` -> BaseModel, ConfigDict, Field
- `app.gateway.deps` -> require_admin_user
- `deerflow.config.extensions_config` -> ExtensionsConfig, McpRoutingConfig, McpToolOverride, get_extensions_config, reload_extensions_config
- `deerflow.mcp.cache` -> reset_mcp_tools_cache

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api', tags=['mcp'])
- `_mcp_config_write_lock` = asyncio.Lock()
- `_ADMIN_REQUIRED_DETAIL` = 'Admin privileges required to manage MCP configuration.'
- `_MCP_STDIO_COMMAND_ALLOWLIST_ENV` = 'DEER_FLOW_MCP_STDIO_COMMAND_ALLOWLIST'
- `_DEFAULT_MCP_STDIO_COMMAND_ALLOWLIST` = frozenset({'npx', 'uvx'})
- `_SHELL_METACHARS` = frozenset(';|&`$<>\n\r')
- `_MASKED_VALUE` = '***'
- `_SENSITIVE_EXTRA_KEY_RE` = re.compile('(^|_)(api_key|apikey|access_key|private_key|c...

## 函数
#### `ƒ` `_normalize_config_key(key: str) -> str`  L102
  - 分支数 0，函数体节点数 48；return: re.sub('[^a-z0-9]+', '_', with_boundaries.lower()).strip('_')
  - 调用: sub, strip, lower

#### `ƒ` `_is_sensitive_extra_key(key: str) -> bool`  L108
  - 分支数 0，函数体节点数 21；return: bool(_SENSITIVE_EXTRA_KEY_RE.search(_normalize_config_key(key)))
  - 调用: bool, search, _normalize_config_key

#### `ƒ` `_mask_sensitive_extra_value(value: Any) -> Any`  L112
  - 分支数 2，函数体节点数 70；return: {key: _MASKED_VALUE if _is_sensitive_extra_key(str(key)) else _mask_sensitive_extra_value(nested) for key, nested in value.items()}, [_mask_sensitive_extra_value(item) for item in value], value
  - 调用: isinstance, _is_sensitive_extra_key, str, _mask_sensitive_extra_value, items

#### `ƒ` `_merge_extra_value_preserving_masked(key: str, incoming_value: Any, existing_value: Any, *, existing_present: bool) -> Any`  L120
  - 分支数 5，函数体节点数 192；raise: HTTPException(status_code=400, detail=f"Cannot set extra config key '{key}' to masked value '***'; provide a real value.")；return: existing_value, merged, [_merge_extra_value_preserving_masked(key, nested_value, existing_value[index], existing_present=True) for index, nested_value in enumerate(incoming_value)], incoming_value
  - 调用: _is_sensitive_extra_key, HTTPException, isinstance, items, _merge_extra_value_preserving_masked, str, get, len, enumerate

#### `ƒ` `_allowed_stdio_commands() -> set[str]`  L147
  - _文档首行_（仅供参考）: Return executable names allowed for API-managed stdio MCP servers.
  - 分支数 1，函数体节点数 69；return: base, base | extra
  - 调用: get, set, strip, split

#### `ƒ` `_stdio_command_name(command: str | None, *, server_name: str) -> str`  L157
  - _文档首行_（仅供参考）: Normalize and validate a stdio command field from the API boundary.
  - 分支数 2，函数体节点数 128；raise: HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"MCP server '{server_name}' with stdio transport requires a command."), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"MCP server '{server_name}' command must be a single executable name; put parameters in args instead.")；return: stripped
  - 调用: strip, HTTPException, any, isspace

#### `ƒ` `_validate_mcp_update_request(request: McpConfigUpdateRequest) -> None`  L176
  - _文档首行_（仅供参考）: Validate API-submitted MCP config before it is persisted.
  - 分支数 3，函数体节点数 111；raise: HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"MCP server '{name}' uses disallowed stdio command '{command_name}'. Allowed commands: {allowed}. Configure {_MCP_STDIO_COMMAND_ALLOWLIST_ENV} to extend this list.")
  - 调用: _allowed_stdio_commands, items, lower, _stdio_command_name, join, sorted, HTTPException

#### `ƒ` `_mask_server_config(server: McpServerConfigResponse) -> McpServerConfigResponse`  L198
  - _文档首行_（仅供参考）: Return a copy of server config with sensitive fields masked.
  - 分支数 1，函数体节点数 122；return: server.model_copy(update={'env': masked_env, 'headers': masked_headers, 'oauth': masked_oauth, **masked_extra})
  - 调用: model_copy, _is_sensitive_extra_key, _mask_sensitive_extra_value, items

#### `ƒ` `_merge_preserving_secrets(incoming: McpServerConfigResponse, existing: McpServerConfigResponse) -> McpServerConfigResponse`  L225
  - _文档首行_（仅供参考）: Merge incoming config with existing, preserving secrets masked by GET.
  - 分支数 12，函数体节点数 424；raise: HTTPException(status_code=400, detail=f"Cannot set env key '{k}' to masked value '***'; provide a real value."), HTTPException(status_code=400, detail=f"Cannot set header '{k}' to masked value '***'; provide a real value.")；return: incoming.model_copy(update=update)
  - 调用: items, HTTPException, model_copy, _merge_extra_value_preserving_masked, get

#### `⏵ƒ` `async get_mcp_configuration(request: Request) -> McpConfigResponse`    @router.get(...)  L311
  - _文档首行_（仅供参考）: Get the current MCP configuration.
  - 分支数 0，函数体节点数 77；return: McpConfigResponse(mcp_servers=servers)
  - 调用: require_admin_user, get_extensions_config, _mask_server_config, McpServerConfigResponse, model_dump, items, McpConfigResponse, get

#### `ƒ` `_apply_mcp_config_update(body: McpConfigUpdateRequest) -> dict`  L340
  - _文档首行_（仅供参考）: Worker-thread body for :func:`update_mcp_configuration`.
  - 分支数 8，函数体节点数 327；return: reloaded_config.mcp_servers
  - 调用: resolve_config_path, cwd, info, get_extensions_config, exists, open, load, get, items, _merge_preserving_secrets, McpServerConfigResponse, dict, model_dump, dump, reload_extensions_config
  - 文件IO: exists (L365), open (L366), open (L392)

#### `⏵ƒ` `async reset_mcp_tools_cache_endpoint(request: Request) -> McpCacheResetResponse`    @router.post(...)  L410
  - _文档首行_（仅供参考）: Reset cached MCP tools and persistent sessions process-wide.
  - 分支数 0，函数体节点数 44；return: McpCacheResetResponse(success=True, message='MCP tools cache reset. Tools will reload on next use.')
  - 调用: require_admin_user, reset_mcp_tools_cache, McpCacheResetResponse, post

#### `⏵ƒ` `async update_mcp_configuration(request: Request, body: McpConfigUpdateRequest) -> McpConfigResponse`    @router.put(...)  L431
  - _文档首行_（仅供参考）: Update the MCP configuration.
  - 分支数 2，函数体节点数 135；raise: bare raise, HTTPException(status_code=500, detail=f'Failed to update MCP configuration: {str(e)}')；return: McpConfigResponse(mcp_servers=servers)
  - 调用: require_admin_user, _validate_mcp_update_request, to_thread, _mask_server_config, McpServerConfigResponse, model_dump, items, reset_mcp_tools_cache, McpConfigResponse, error, HTTPException, str, put

## 类
### 类 `McpOAuthConfigResponse`  L33
- 继承: BaseModel
- _文档首行_: OAuth configuration for an MCP server.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether OAuth token inje...
  - `token_url` = Field(default='', description='OAuth token endpoint URL')
  - `grant_type` = Field(default='client_credentials', description='OAuth gr...
  - `client_id` = Field(default=None, description='OAuth client ID')
  - `client_secret` = Field(default=None, description='OAuth client secret')
  - `refresh_token` = Field(default=None, description='OAuth refresh token')
  - `scope` = Field(default=None, description='OAuth scope')
  - `audience` = Field(default=None, description='OAuth audience')
  - `token_field` = Field(default='access_token', description='Token response...
  - `token_type_field` = Field(default='token_type', description='Token response f...
  - `expires_in_field` = Field(default='expires_in', description='Token response f...
  - `default_token_type` = Field(default='Bearer', description='Default token type w...
  - `refresh_skew_seconds` = Field(default=60, description='Refresh this many seconds ...
  - `extra_token_params` = Field(default_factory=dict, description='Additional form ...

### 类 `McpServerConfigResponse`  L52
- 继承: BaseModel
- _文档首行_: Response model for MCP server configuration.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether this MCP server ...
  - `type` = Field(default='stdio', description="Transport type: 'stdi...
  - `command` = Field(default=None, description='Command to execute to st...
  - `args` = Field(default_factory=list, description='Arguments to pas...
  - `env` = Field(default_factory=dict, description='Environment vari...
  - `url` = Field(default=None, description='URL of the MCP server (f...
  - `headers` = Field(default_factory=dict, description='HTTP headers to ...
  - `oauth` = Field(default=None, description='OAuth configuration for ...
  - `description` = Field(default='', description='Human-readable description...
  - `routing` = Field(default_factory=McpRoutingConfig, description='Soft...
  - `tools` = Field(default_factory=dict, description='Per-original-too...
  - `tool_call_timeout` = Field(default=None, description='Timeout in seconds for i...
  - `model_config` = ConfigDict(extra='allow')

### 类 `McpConfigResponse`  L70
- 继承: BaseModel
- _文档首行_: Response model for MCP configuration.
- 类/实例变量:
  - `mcp_servers` = Field(default_factory=dict, description='Map of MCP serve...

### 类 `McpConfigUpdateRequest`  L79
- 继承: BaseModel
- _文档首行_: Request model for updating MCP configuration.
- 类/实例变量:
  - `mcp_servers` = Field(..., description='Map of MCP server name to configu...

### 类 `McpCacheResetResponse`  L88
- 继承: BaseModel
- _文档首行_: Response model for resetting the MCP tools cache.
- 类/实例变量:
  - `success` = Field(description='Whether the MCP tools cache was reset')
  - `message` = Field(description='Human-readable reset status')

## 文件内调用关系
- `_is_sensitive_extra_key` -> _normalize_config_key
- `_mask_sensitive_extra_value` -> _is_sensitive_extra_key, _mask_sensitive_extra_value
- `_merge_extra_value_preserving_masked` -> _is_sensitive_extra_key, _merge_extra_value_preserving_masked
- `_validate_mcp_update_request` -> _allowed_stdio_commands, _stdio_command_name
- `_mask_server_config` -> _is_sensitive_extra_key, _mask_sensitive_extra_value
- `_merge_preserving_secrets` -> _merge_extra_value_preserving_masked
- `get_mcp_configuration` -> _mask_server_config
- `_apply_mcp_config_update` -> _merge_preserving_secrets
- `update_mcp_configuration` -> _validate_mcp_update_request, _mask_server_config

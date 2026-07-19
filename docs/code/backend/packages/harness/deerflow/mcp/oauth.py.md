# `backend/packages/harness/deerflow/mcp/oauth.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/mcp/oauth.py`  ·  行数: 171

**模块文档首行**（仅供参考）: OAuth token support for MCP HTTP/SSE servers.

## 模块概览
- 函数 2 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, logging
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `datetime` -> UTC, datetime, timedelta
- `typing` -> Any
- `deerflow.config.extensions_config` -> ExtensionsConfig, McpOAuthConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `build_oauth_tool_interceptor(extensions_config: ExtensionsConfig) -> Any | None`  L132
  - _文档首行_（仅供参考）: Build a tool interceptor that injects OAuth Authorization headers.
  - 分支数 2，函数体节点数 104；return: None, await handler(request), await handler(request.override(headers=updated_headers)), oauth_interceptor
  - 调用: from_extensions_config, has_oauth_servers, get_authorization_header, handler, dict, override

#### `⏵ƒ` `async get_initial_oauth_headers(extensions_config: ExtensionsConfig) -> dict[str, str]`  L150
  - _文档首行_（仅供参考）: Get initial OAuth Authorization headers for MCP server connections.
  - 分支数 4，函数体节点数 118；return: {}, {name: value for name, value in headers.items() if value}
  - 调用: from_extensions_config, has_oauth_servers, oauth_server_names, get_authorization_header, warning, items

## 类
### 类 `_OAuthToken`  L17  @dataclass
- _文档首行_: Cached OAuth token.
- 类/实例变量:
  - `access_token` = <annotated>
  - `token_type` = <annotated>
  - `expires_at` = <annotated>

### 类 `OAuthTokenManager`  L25
- _文档首行_: Acquire/cache/refresh OAuth tokens for MCP servers.
- 方法:
  #### `cls` `from_extensions_config(cls, extensions_config: ExtensionsConfig) -> OAuthTokenManager`    @classmethod  L34
    - 分支数 2，函数体节点数 69；return: cls(oauth_by_server)
    - 调用: items, get_enabled_mcp_servers, cls
  #### `st` `_is_expiring(token: _OAuthToken, oauth: McpOAuthConfig) -> bool`    @staticmethod  L68
    - 分支数 0，函数体节点数 45；return: token.expires_at <= now + timedelta(seconds=max(oauth.refresh_skew_seconds, 0))
    - 调用: now, timedelta, max
  #### `m` `__init__(self, oauth_by_server: dict[str, McpOAuthConfig])`  L28
    - 分支数 0，函数体节点数 67
    - 调用: Lock
  #### `m` `has_oauth_servers(self) -> bool`  L41
    - 分支数 0，函数体节点数 13；return: bool(self._oauth_by_server)
    - 调用: bool
  #### `m` `oauth_server_names(self) -> list[str]`  L44
    - 分支数 0，函数体节点数 20；return: list(self._oauth_by_server.keys())
    - 调用: list, keys
  #### `⏵m` `async get_authorization_header(self, server_name: str) -> str | None`  L47
    - 分支数 4，函数体节点数 173；return: None, f'{token.token_type} {token.access_token}', f'{fresh.token_type} {fresh.access_token}'
    - 调用: get, _is_expiring, _fetch_token, info
  #### `⏵m` `async _fetch_token(self, oauth: McpOAuthConfig) -> _OAuthToken`  L72
    - 分支数 13，函数体节点数 381；raise: ValueError('OAuth client_credentials requires client_id and client_secret'), ValueError('OAuth refresh_token grant requires refresh_token'), ValueError(f'Unsupported OAuth grant type: {oauth.grant_type}'), ValueError(f"OAuth token response missing '{oauth.token_field}'")；return: _OAuthToken(access_token=access_token, token_type=token_type, expires_at=expires_at)
    - 调用: ValueError, AsyncClient, post, raise_for_status, json, get, isinstance, str, int, now, timedelta, max, _OAuthToken
  - 网络调用: post (L102)

## 文件内调用关系
- `build_oauth_tool_interceptor` -> from_extensions_config, has_oauth_servers, get_authorization_header
- `get_initial_oauth_headers` -> from_extensions_config, has_oauth_servers, oauth_server_names, get_authorization_header
- `OAuthTokenManager.get_authorization_header` -> _is_expiring, _fetch_token

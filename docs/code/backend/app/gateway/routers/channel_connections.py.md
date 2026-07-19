# `backend/app/gateway/routers/channel_connections.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/channel_connections.py`  ·  行数: 696

**模块文档首行**（仅供参考）: Browser-facing APIs for user-owned IM channel bindings.

## 模块概览
- 函数 33 个，类 7 个，模块级常量 9 个

## 依赖（import）
- 模块: asyncio, logging, secrets
- `__future__` -> annotations
- `datetime` -> UTC, datetime, timedelta
- `typing` -> Any
- `fastapi` -> APIRouter, HTTPException, Request, Response
- `pydantic` -> BaseModel, Field
- `app.channels.runtime_config_store` -> ChannelRuntimeConfigStore, apply_runtime_connection_config, merge_runtime_channel_configs
- `app.gateway.deps` -> require_admin_user
- `deerflow.config.channel_connections_config` -> ChannelConnectionsConfig
- `deerflow.persistence.channel_connections` -> ChannelConnectionRepository
- `deerflow.persistence.engine` -> get_session_factory

## 模块级常量
- `router` = APIRouter(prefix='/api/channels', tags=['channel-connecti...
- `logger` = logging.getLogger(__name__)
- `_STATE_TTL_SECONDS` = 600
- `_MAX_PENDING_CONNECT_CODES_PER_PROVIDER` = 5
- `_MASKED_CREDENTIAL_VALUE` = '********'
- `_ADMIN_REQUIRED_DETAIL` = 'Admin privileges required to manage channel runtime cred...
- `_PROVIDER_META` = {'telegram': {'display_name': 'Telegram', 'auth_mode': 'd...
- `_CREDENTIAL_FIELDS` = {'telegram': ({'name': 'bot_token', 'label': 'Bot token',...
- `_RUNTIME_REQUIREMENTS` = {'telegram': ('bot_token',), 'slack': ('bot_token', 'app_...

## 函数
#### `ƒ` `_get_user_id(request: Request) -> str`  L133
  - 分支数 1，函数体节点数 41；raise: HTTPException(status_code=401, detail='Authentication required')；return: str(user.id)
  - 调用: getattr, HTTPException, str
  - 反射: getattr (L134)

#### `ƒ` `_get_app_config()`  L140
  - 分支数 0，函数体节点数 8；return: get_app_config()
  - 调用: get_app_config

#### `⏵ƒ` `async _get_runtime_config_store(request: Request) -> ChannelRuntimeConfigStore`  L146
  - 分支数 1，函数体节点数 57；return: store
  - 调用: getattr, isinstance, to_thread
  - 反射: getattr (L147)

#### `⏵ƒ` `async _get_channel_connections_config(request: Request) -> ChannelConnectionsConfig`  L157
  - 分支数 1，函数体节点数 68；return: config
  - 调用: getattr, isinstance, _get_app_config, apply_runtime_connection_config, _get_runtime_config_store
  - 反射: getattr (L158)

#### `⏵ƒ` `async _get_channels_config(request: Request) -> dict[str, Any]`  L166
  - 分支数 1，函数体节点数 69；return: state_config, result
  - 调用: getattr, isinstance, _load_channels_config, _get_channel_connections_config
  - 反射: getattr (L167)

#### `⏵ƒ` `async _load_channels_config(request: Request, config: ChannelConnectionsConfig) -> dict[str, Any]`  L176
  - 分支数 0，函数体节点数 78；return: result
  - 调用: _get_app_config, get, isinstance, dict, merge_runtime_channel_configs, _get_runtime_config_store

#### `ƒ` `_get_repository(request: Request, config: ChannelConnectionsConfig) -> ChannelConnectionRepository`  L189
  - 分支数 2，函数体节点数 77；raise: HTTPException(status_code=503, detail='Channel connection persistence is not available')；return: repo
  - 调用: getattr, isinstance, get_session_factory, HTTPException, ChannelConnectionRepository
  - 反射: getattr (L190)

#### `ƒ` `_provider_config(config: ChannelConnectionsConfig, provider: str)`  L203
  - 分支数 2，函数体节点数 51；raise: HTTPException(status_code=404, detail='Unknown channel provider')；return: provider_config
  - 调用: HTTPException, getattr
  - 反射: getattr (L211)

#### `ƒ` `_runtime_channel_configured(provider: str, channels_config: dict[str, Any]) -> bool`  L217
  - 分支数 1，函数体节点数 81；return: False, all((str(runtime_config.get(key) or '').strip() for key in _RUNTIME_REQUIREMENTS[provider]))
  - 调用: get, isinstance, all, strip, str

#### `ƒ` `_runtime_unavailable_reason(provider: str) -> str`  L224
  - 分支数 0，函数体节点数 37；return: f'Enter the required {display_name} credentials to connect this channel.'
  - 调用: get

#### `ƒ` `_runtime_not_running_reason(provider: str) -> str`  L230
  - 分支数 0，函数体节点数 36；return: f'{display_name} channel is configured but is not running. Check the credentials and service logs.'
  - 调用: get

#### `ƒ` `_runtime_channel_running(provider: str) -> bool | None`  L236
  - 分支数 5，函数体节点数 112；return: None, False, bool(channel_status.get('running'))
  - 调用: debug, get_channel_service, get_status, get, isinstance, bool

#### `⏵ƒ` `async _ensure_runtime_channel_ready_if_available(provider: str, channels_config: dict[str, Any]) -> bool | None`  L260
  - 分支数 5，函数体节点数 125；return: None, await ensure_channel_ready(provider, runtime_config), False
  - 调用: get, isinstance, debug, get_channel_service, getattr, ensure_channel_ready, exception
  - 反射: getattr (L278)

#### `ƒ` `_provider_unavailable_reason(config: ChannelConnectionsConfig, channels_config: dict[str, Any], provider: str) -> str | None`  L289
  - 分支数 4，函数体节点数 89；return: None, _runtime_unavailable_reason(provider), _runtime_not_running_reason(provider)
  - 调用: _provider_config, _runtime_unavailable_reason, _runtime_channel_configured, _runtime_channel_running, _runtime_not_running_reason

#### `ƒ` `_provider_status(config: ChannelConnectionsConfig, channels_config: dict[str, Any], provider: str) -> tuple[dict[str, bool], str | None]`  L306
  - 分支数 0，函数体节点数 94；return: ({'enabled': declared['enabled'], 'configured': configured}, unavailable_reason)
  - 调用: provider_status, _provider_unavailable_reason, _runtime_channel_configured

#### `ƒ` `_new_binding_code() -> str`  L317
  - 分支数 0，函数体节点数 11；return: secrets.token_urlsafe(16)
  - 调用: token_urlsafe

#### `⏵ƒ` `async _create_state(repo: ChannelConnectionRepository, *, owner_user_id: str, provider: str) -> str`  L321
  - 分支数 1，函数体节点数 80；raise: HTTPException(status_code=429, detail='Too many pending channel connection codes. Wait for existing codes to expire or use one of them.')；return: state
  - 调用: now, _new_binding_code, create_oauth_state_within_cap, timedelta, HTTPException

#### `ƒ` `_connect_instruction(provider: str, code: str) -> str`  L347
  - 分支数 2，函数体节点数 61；raise: HTTPException(status_code=404, detail='Unknown channel provider')；return: f'Send /start {code} to the DeerFlow Telegram bot.', f"Send /connect {code} to the DeerFlow {meta['display_name']} bot."
  - 调用: get, HTTPException

#### `ƒ` `_connect_url(config: ChannelConnectionsConfig, provider: str, code: str) -> str | None`  L356
  - 分支数 2，函数体节点数 70；raise: HTTPException(status_code=404, detail='Unknown channel provider')；return: f'https://t.me/{provider_config.bot_username}?start={code}', None
  - 调用: _provider_config, get, HTTPException

#### `ƒ` `_connection_updated_at(connection: dict[str, Any]) -> datetime`  L365
  - 分支数 3，函数体节点数 92；return: value if value.tzinfo is not None else value.replace(tzinfo=UTC), datetime.fromisoformat(value.replace('Z', '+00:00')), datetime.min.replace(tzinfo=UTC)
  - 调用: get, isinstance, replace, fromisoformat
  - 网络调用: get (L366)
  - 文件IO: replace (L368), replace (L371), replace (L374)

#### `ƒ` `_newest_connection_by_provider(connections: list[dict[str, Any]]) -> dict[str, dict[str, Any]]`  L377
  - 分支数 2，函数体节点数 110；return: by_provider
  - 调用: get, _connection_updated_at

#### `ƒ` `_credential_fields(provider: str) -> list[ChannelCredentialFieldResponse]`  L386
  - 分支数 1，函数体节点数 48；raise: HTTPException(status_code=404, detail='Unknown channel provider')；return: [ChannelCredentialFieldResponse(**field) for field in fields]
  - 调用: get, HTTPException, ChannelCredentialFieldResponse

#### `ƒ` `_credential_values(provider: str, channels_config: dict[str, Any]) -> dict[str, str]`  L393
  - 分支数 3，函数体节点数 121；return: {}, values
  - 调用: get, isinstance, _credential_fields, strip, str

#### `ƒ` `_provider_response(config: ChannelConnectionsConfig, channels_config: dict[str, Any], provider: str, meta: dict[str, str], connection: dict[str, Any] | None) -> ChannelProviderResponse`  L407
  - 分支数 6，函数体节点数 253；return: ChannelProviderResponse(provider=provider, display_name=meta['display_name'], enabled=status['enabled'], configured=status['configured'], connectable=status['enabled'] and status['configured'] and (unavailable_reason is None), unavailable_reason=unavailable_reason, auth_mode=meta['auth_mode'], connection_status=connection_status, credential_fields=_credential_fields(provider), credential_values=credential_values)
  - 调用: _provider_status, is_auth_disabled, _credential_values, get, strip, str, _provider_config, ChannelProviderResponse, _credential_fields

#### `ƒ` `_required_runtime_values(provider: str, values: dict[str, str], existing_config: dict[str, Any] | None) -> dict[str, str]`  L453
  - 分支数 5，函数体节点数 233；raise: HTTPException(status_code=400, detail=f"Missing required channel configuration: {', '.join(missing)}")；return: cleaned
  - 调用: _credential_fields, get, strip, str, isinstance, append, HTTPException, join

#### `⏵ƒ` `async _restart_runtime_channel_if_available(provider: str, runtime_config: dict[str, Any]) -> bool | None`  L478
  - 分支数 2，函数体节点数 61；return: None, await service.configure_channel(provider, runtime_config)
  - 调用: exception, get_channel_service, configure_channel

#### `⏵ƒ` `async _sync_runtime_channel_after_removal(provider: str, channels_config: dict[str, Any]) -> bool | None`  L491
  - 分支数 3，函数体节点数 97；return: None, await service.configure_channel(provider, runtime_config), await service.remove_channel(provider)
  - 调用: exception, get_channel_service, get, isinstance, configure_channel, remove_channel

#### `⏵ƒ` `async get_channel_providers(request: Request) -> ChannelProvidersResponse`    @router.get(...)  L509
  - 分支数 4，函数体节点数 212；raise: bare raise；return: ChannelProvidersResponse(enabled=config.enabled, providers=providers)
  - 调用: _get_channel_connections_config, _get_channels_config, _get_repository, _get_user_id, list_connections, _newest_connection_by_provider, provider_status, gather, _ensure_runtime_channel_ready_if_available, _runtime_channel_configured, get, append, _provider_response, ChannelProvidersResponse

#### `⏵ƒ` `async get_channel_connections(request: Request) -> ChannelConnectionsResponse`    @router.get(...)  L539
  - 分支数 1，函数体节点数 80；return: ChannelConnectionsResponse(connections=[]), ChannelConnectionsResponse(connections=[ChannelConnectionResponse(**row) for row in rows])
  - 调用: _get_channel_connections_config, ChannelConnectionsResponse, _get_repository, list_connections, _get_user_id, ChannelConnectionResponse, get

#### `⏵ƒ` `async disconnect_channel_connection(connection_id: str, request: Request) -> Response`    @router.delete(...)  L549
  - 分支数 2，函数体节点数 89；raise: HTTPException(status_code=400, detail='Channel connections are disabled'), HTTPException(status_code=404, detail='Channel connection not found')；return: Response(status_code=204)
  - 调用: _get_channel_connections_config, HTTPException, _get_repository, disconnect_connection, _get_user_id, Response, delete

#### `⏵ƒ` `async disconnect_channel_provider_runtime(provider: str, request: Request) -> ChannelProviderResponse`    @router.delete(...)  L565
  - 分支数 6，函数体节点数 256；raise: HTTPException(status_code=400, detail='Channel connections are disabled'), HTTPException(status_code=400, detail='Channel provider is not enabled'), bare raise, HTTPException(status_code=400, detail=f'Failed to stop {display_name} channel. Try again.')；return: _provider_response(config, live_channels_config, provider, _PROVIDER_META[provider])
  - 调用: require_admin_user, _get_channel_connections_config, HTTPException, _provider_config, _get_repository, _get_channels_config, dict, pop, _sync_runtime_channel_after_removal, disconnect_provider_connections, _get_runtime_config_store, to_thread, _provider_response, delete

#### `⏵ƒ` `async connect_channel_provider(provider: str, request: Request) -> ChannelConnectResponse`    @router.post(...)  L612
  - 分支数 5，函数体节点数 214；raise: HTTPException(status_code=400, detail='Channel connections are disabled'), HTTPException(status_code=400, detail='Channel provider is not enabled'), HTTPException(status_code=400, detail=unavailable_reason), HTTPException(status_code=400, detail='Channel provider is not configured')；return: ChannelConnectResponse(provider=provider, mode=_PROVIDER_META[provider]['auth_mode'], url=_connect_url(config, provider, code), code=code, instruction=_connect_instruction(provider, code), expires_in=_STATE_TTL_SECONDS)
  - 调用: _get_channel_connections_config, _get_channels_config, HTTPException, _provider_config, _runtime_channel_configured, _ensure_runtime_channel_ready_if_available, _provider_status, _get_repository, _create_state, _get_user_id, ChannelConnectResponse, _connect_url, _connect_instruction, post

#### `⏵ƒ` `async configure_channel_provider_runtime(provider: str, body: ChannelRuntimeConfigRequest, request: Request) -> ChannelProviderResponse`    @router.post(...)  L647
  - 分支数 5，函数体节点数 305；raise: HTTPException(status_code=400, detail='Channel connections are disabled'), HTTPException(status_code=400, detail='Channel provider is not enabled'), HTTPException(status_code=400, detail=f'Failed to start {display_name} channel. Check the values and try again.')；return: _provider_response(config, live_channels_config, provider, _PROVIDER_META[provider])
  - 调用: require_admin_user, _get_channel_connections_config, HTTPException, _provider_config, _get_channels_config, get, isinstance, dict, _required_runtime_values, _restart_runtime_channel_if_available, _get_runtime_config_store, to_thread, _provider_response, post

## 类
### 类 `ChannelCredentialFieldResponse`  L33
- 继承: BaseModel
- 类/实例变量:
  - `name` = <annotated>
  - `label` = <annotated>
  - `type` = 'text'
  - `required` = True

### 类 `ChannelProviderResponse`  L40
- 继承: BaseModel
- 类/实例变量:
  - `provider` = <annotated>
  - `display_name` = <annotated>
  - `enabled` = <annotated>
  - `configured` = <annotated>
  - `connectable` = <annotated>
  - `unavailable_reason` = None
  - `auth_mode` = <annotated>
  - `connection_status` = <annotated>
  - `credential_fields` = Field(default_factory=list)
  - `credential_values` = Field(default_factory=dict)

### 类 `ChannelProvidersResponse`  L53
- 继承: BaseModel
- 类/实例变量:
  - `enabled` = <annotated>
  - `providers` = <annotated>

### 类 `ChannelConnectionResponse`  L58
- 继承: BaseModel
- 类/实例变量:
  - `id` = <annotated>
  - `provider` = <annotated>
  - `status` = <annotated>
  - `external_account_id` = None
  - `external_account_name` = None
  - `workspace_id` = None
  - `workspace_name` = None
  - `scopes` = Field(default_factory=list)
  - `metadata` = Field(default_factory=dict)

### 类 `ChannelConnectionsResponse`  L70
- 继承: BaseModel
- 类/实例变量:
  - `connections` = <annotated>

### 类 `ChannelConnectResponse`  L74
- 继承: BaseModel
- 类/实例变量:
  - `provider` = <annotated>
  - `mode` = <annotated>
  - `url` = None
  - `code` = <annotated>
  - `instruction` = <annotated>
  - `expires_in` = <annotated>

### 类 `ChannelRuntimeConfigRequest`  L83
- 继承: BaseModel
- 类/实例变量:
  - `values` = Field(default_factory=dict)

## 文件内调用关系
- `_get_channel_connections_config` -> _get_app_config, _get_runtime_config_store
- `_get_channels_config` -> _load_channels_config, _get_channel_connections_config
- `_load_channels_config` -> _get_app_config, _get_runtime_config_store
- `_provider_unavailable_reason` -> _provider_config, _runtime_unavailable_reason, _runtime_channel_configured, _runtime_channel_running, _runtime_not_running_reason
- `_provider_status` -> _provider_unavailable_reason, _runtime_channel_configured
- `_create_state` -> _new_binding_code
- `_connect_url` -> _provider_config
- `_newest_connection_by_provider` -> _connection_updated_at
- `_credential_values` -> _credential_fields
- `_provider_response` -> _provider_status, _credential_values, _provider_config, _credential_fields
- `_required_runtime_values` -> _credential_fields
- `get_channel_providers` -> _get_channel_connections_config, _get_channels_config, _get_repository, _get_user_id, _newest_connection_by_provider, _ensure_runtime_channel_ready_if_available, _runtime_channel_configured, _provider_response
- `get_channel_connections` -> _get_channel_connections_config, _get_repository, _get_user_id
- `disconnect_channel_connection` -> _get_channel_connections_config, _get_repository, _get_user_id
- `disconnect_channel_provider_runtime` -> _get_channel_connections_config, _provider_config, _get_repository, _get_channels_config, _sync_runtime_channel_after_removal, _get_runtime_config_store, _provider_response
- `connect_channel_provider` -> _get_channel_connections_config, _get_channels_config, _provider_config, _runtime_channel_configured, _ensure_runtime_channel_ready_if_available, _provider_status, _get_repository, _create_state, _get_user_id, _connect_url, _connect_instruction
- `configure_channel_provider_runtime` -> _get_channel_connections_config, _provider_config, _get_channels_config, _required_runtime_values, _restart_runtime_channel_if_available, _get_runtime_config_store, _provider_response

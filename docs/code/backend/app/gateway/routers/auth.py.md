# `backend/app/gateway/routers/auth.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/auth.py`  ·  行数: 836

**模块文档首行**（仅供参考）: Authentication endpoints.

## 模块概览
- 函数 24 个，类 5 个，模块级常量 13 个

## 依赖（import）
- 模块: asyncio, logging, os, re, secrets, time, urllib.parse
- `ipaddress` -> ip_address, ip_network
- `fastapi` -> APIRouter, Depends, Form, HTTPException, Request, Response, status
- `fastapi.security` -> OAuth2PasswordRequestForm
- `pydantic` -> BaseModel, EmailStr, Field, field_validator
- `starlette.responses` -> RedirectResponse
- `app.gateway.auth` -> UserResponse, create_access_token
- `app.gateway.auth.config` -> get_auth_config
- `app.gateway.auth.errors` -> AuthErrorCode, AuthErrorResponse
- `app.gateway.auth.oidc` -> OIDCError, OIDCService
- `app.gateway.auth.oidc_state` -> OIDCStatePayload, compute_code_challenge, delete_state_cookie, generate_code_verifier, generate_nonce, generate_oidc_state, get_state_cookie, set_state_cookie
- `app.gateway.auth.session_cookie` -> ACCESS_TOKEN_COOKIE_NAME, SESSION_PERSISTENCE_COOKIE_NAME, set_session_cookie
- `app.gateway.auth.session_cookie_state` -> SKIP_AUTH_CSRF_COOKIE_STATE_ATTR
- `app.gateway.auth.user_provisioning` -> get_or_provision_oidc_user
- `app.gateway.csrf_middleware` -> CSRF_COOKIE_NAME, _request_origin, auth_csrf_cookie_settings, generate_csrf_token, is_secure_request
- `app.gateway.deps` -> get_current_user_from_request, get_local_provider
- `deerflow.config.auth_config` -> OIDCProviderConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/v1/auth', tags=['auth'])
- `_COMMON_PASSWORDS` = frozenset({'password', 'password1', 'password12', 'passwo...
- `_MAX_LOGIN_ATTEMPTS` = 5
- `_LOCKOUT_SECONDS` = 300
- `_login_attempts` = {}
- `_MAX_TRACKED_IPS` = 10000
- `_SETUP_STATUS_CACHE` = {}
- `_SETUP_STATUS_CACHE_TTL_SECONDS` = 60
- `_MAX_TRACKED_SETUP_STATUS_IPS` = 10000
- `_SETUP_STATUS_INFLIGHT` = {}
- `_SETUP_STATUS_INFLIGHT_GUARD` = asyncio.Lock()
- `_OIDC_PROVIDER_KEY_RE` = re.compile('^[a-zA-Z0-9_-]+$')

## 函数
#### `ƒ` `_password_is_common(password: str) -> bool`  L102
  - _文档首行_（仅供参考）: Case-insensitive blocklist check.
  - 分支数 0，函数体节点数 19；return: password.lower() in _COMMON_PASSWORDS
  - 调用: lower

#### `ƒ` `_validate_strong_password(value: str) -> str`  L113
  - _文档首行_（仅供参考）: Pydantic field-validator body shared by Register + ChangePassword.
  - 分支数 1，函数体节点数 23；raise: ValueError('Password is too common; choose a stronger password.')；return: value
  - 调用: _password_is_common, ValueError

#### `ƒ` `_set_session_cookie(response: Response, token: str, request: Request, *, remember_me: bool | None) -> None`  L156
  - _文档首行_（仅供参考）: Set the access_token HttpOnly cookie on the response.
  - 分支数 0，函数体节点数 34
  - 调用: set_session_cookie

#### `ƒ` `_trusted_proxies() -> list`  L177
  - _文档首行_（仅供参考）: Parse ``AUTH_TRUSTED_PROXIES`` env var into a list of ip_network objects.
  - 分支数 4，函数体节点数 84；return: [], nets
  - 调用: strip, getenv, split, append, ip_network, warning
  - 环境变量: getenv (L185)

#### `ƒ` `_get_client_ip(request: Request) -> str`  L200
  - _文档首行_（仅供参考）: Extract the real client IP for rate limiting.
  - 分支数 4，函数体节点数 93；return: real_ip, peer_host or 'unknown'
  - 调用: _trusted_proxies, ip_address, any, strip, get

#### `ƒ` `_check_rate_limit(ip: str) -> None`  L238
  - _文档首行_（仅供参考）: Raise 429 if the IP is currently locked out.
  - 分支数 3，函数体节点数 66；raise: HTTPException(status_code=429, detail='Too many login attempts. Try again later.')；return: None
  - 调用: get, time, HTTPException

#### `ƒ` `_record_login_failure(ip: str) -> None`  L256
  - _文档首行_（仅供参考）: Record a failed login attempt for the given IP.
  - 分支数 5，函数体节点数 205
  - 调用: len, time, items, sorted, get

#### `ƒ` `_record_login_success(ip: str) -> None`  L280
  - _文档首行_（仅供参考）: Clear failure counter for the given IP on successful login.
  - 分支数 0，函数体节点数 17
  - 调用: pop

#### `⏵ƒ` `async login_local(request: Request, response: Response, form_data: OAuth2PasswordRequestForm, remember_me: bool)`    @router.post(...)  L289
  - _文档首行_（仅供参考）: Local email/password login.
  - 分支数 1，函数体节点数 161；raise: HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=AuthErrorResponse(code=AuthErrorCode.INVALID_CREDENTIALS, message='Incorrect email or password').model_dump())；return: LoginResponse(expires_in=get_auth_config().token_expiry_days * 24 * 3600, needs_setup=user.needs_setup)
  - 调用: Depends, Form, _get_client_ip, _check_rate_limit, authenticate, get_local_provider, _record_login_failure, HTTPException, model_dump, AuthErrorResponse, _record_login_success, create_access_token, str, _set_session_cookie, LoginResponse, get_auth_config, post

#### `⏵ƒ` `async register(request: Request, response: Response, body: RegisterRequest)`    @router.post(...)  L319
  - _文档首行_（仅供参考）: Register a new user account (always 'user' role).
  - 分支数 1，函数体节点数 136；raise: HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=AuthErrorResponse(code=AuthErrorCode.EMAIL_ALREADY_EXISTS, message='Email already registered').model_dump())；return: UserResponse(id=str(user.id), email=user.email, system_role=user.system_role, oauth_provider=user.oauth_provider)
  - 调用: create_user, get_local_provider, HTTPException, model_dump, AuthErrorResponse, create_access_token, str, _set_session_cookie, UserResponse, post

#### `⏵ƒ` `async logout(request: Request, response: Response)`    @router.post(...)  L340
  - _文档首行_（仅供参考）: Logout current user by clearing the cookie.
  - 分支数 0，函数体节点数 86；return: MessageResponse(message='Successfully logged out')
  - 调用: is_secure_request, delete_cookie, setattr, MessageResponse, post
  - 反射: setattr (L346)

#### `⏵ƒ` `async change_password(request: Request, response: Response, body: ChangePasswordRequest)`    @router.post(...)  L351
  - _文档首行_（仅供参考）: Change password for the currently authenticated user.
  - 分支数 6，函数体节点数 318；raise: HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=AuthErrorResponse(code=AuthErrorCode.INVALID_CREDENTIALS, message='Password changes are not available when DEER_FLOW_AUTH_DISABLED=1.').model_dump()), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=AuthErrorResponse(code=AuthErrorCode.INVALID_CREDENTIALS, message='OAuth users cannot change password').model_dump()), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=AuthErrorResponse(code=AuthErrorCode.INVALID_CREDENTIALS, message='Current password is incorrect').model_dump()), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=AuthErrorResponse(code=AuthErrorCode.EMAIL_ALREADY_EXISTS, message='Email already in use').model_dump())；return: MessageResponse(message='Password changed successfully')
  - 调用: get_current_user_from_request, getattr, HTTPException, model_dump, AuthErrorResponse, verify_password_async, get_local_provider, get_user_by_email, str, hash_password_async, update_user, create_access_token, _set_session_cookie, _set_csrf_cookie, MessageResponse, post
  - 反射: getattr (L365)

#### `⏵ƒ` `async get_me(request: Request)`    @router.get(...)  L408
  - _文档首行_（仅供参考）: Get current authenticated user info.
  - 分支数 0，函数体节点数 57；return: UserResponse(id=str(user.id), email=user.email, system_role=user.system_role, needs_setup=user.needs_setup, oauth_provider=user.oauth_provider)
  - 调用: get_current_user_from_request, UserResponse, str, get

#### `⏵ƒ` `async setup_status(request: Request)`    @router.get(...)  L432
  - _文档首行_（仅供参考）: Check if an admin account exists. Returns needs_setup=True when no admin exists.
  - 分支数 14，函数体节点数 363；return: cached_result, {'needs_setup': admin_count == 0}, result
  - 调用: _get_client_ip, time, get, len, items, sorted, count_admin_users, get_local_provider, create_task, _compute_setup_status, pop

#### `⏵ƒ` `async initialize_admin(request: Request, response: Response, body: InitializeAdminRequest)`    @router.post(...)  L499
  - _文档首行_（仅供参考）: Create the first admin account on initial system setup.
  - 分支数 3，函数体节点数 216；raise: HTTPException(status_code=status.HTTP_409_CONFLICT, detail=AuthErrorResponse(code=AuthErrorCode.SYSTEM_ALREADY_INITIALIZED, message='System already initialized').model_dump()), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=AuthErrorResponse(code=AuthErrorCode.EMAIL_ALREADY_EXISTS, message='Email already registered').model_dump())；return: UserResponse(id=str(user.id), email=user.email, system_role=user.system_role, oauth_provider=user.oauth_provider)
  - 调用: count_admin_users, get_local_provider, HTTPException, model_dump, AuthErrorResponse, create_user, create_access_token, str, _set_session_cookie, UserResponse, post

#### `ƒ` `_get_oidc_service() -> OIDCService`  L540
  - _文档首行_（仅供参考）: Get (or create) the singleton OIDC service instance.
  - 分支数 1，函数体节点数 28；return: _get_oidc_service._instance
  - 调用: hasattr, OIDCService
  - 反射: hasattr (L542)

#### `⏵ƒ` `async close_oidc_service() -> None`  L547
  - 分支数 1，函数体节点数 33
  - 调用: getattr, close, delattr
  - 反射: getattr (L548), delattr (L551)

#### `ƒ` `_set_csrf_cookie(response: Response, request: Request) -> None`  L554
  - _文档首行_（仅供参考）: Set the CSRF double-submit cookie (needed for GET-based OIDC callback).
  - 分支数 0，函数体节点数 51
  - 调用: generate_csrf_token, auth_csrf_cookie_settings, set_cookie

#### `ƒ` `_resolve_oidc_redirect_uri(request: Request, provider_id: str, provider_config: OIDCProviderConfig) -> str`  L571
  - _文档首行_（仅供参考）: Resolve the redirect URI for an OIDC provider.
  - 分支数 2，函数体节点数 69；return: provider_config.redirect_uri, f'{origin}/api/v1/auth/callback/{provider_id}'
  - 调用: _request_origin, get

#### `⏵ƒ` `async list_auth_providers()`    @router.get(...)  L591
  - _文档首行_（仅供参考）: List enabled SSO providers for the login page.
  - 分支数 2，函数体节点数 80；return: {'providers': []}, {'providers': providers}
  - 调用: get_app_config, items, append, get

#### `⏵ƒ` `async oauth_login(request: Request, provider: str, next: str | None, remember_me: bool)`    @router.get(...)  L618
  - _文档首行_（仅供参考）: Initiate OIDC login flow.
  - 分支数 4，函数体节点数 335；raise: HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='SSO authentication is not enabled'), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid provider ID'), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Unknown SSO provider: {provider}'), HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail='Failed to connect to SSO provider')；return: redirect_response
  - 调用: get_app_config, HTTPException, match, get, validate_next_param, _resolve_oidc_redirect_uri, generate_oidc_state, generate_nonce, generate_code_verifier, compute_code_challenge, _get_oidc_service, discover, error, build_authorization_url, OIDCStatePayload, RedirectResponse, set_state_cookie

#### `⏵ƒ` `async oauth_callback(request: Request, provider: str, code: str | None, state: str | None, error: str | None, error_description: str | None)`    @router.get(...)  L697
  - _文档首行_（仅供参考）: OIDC callback endpoint.
  - 分支数 10，函数体节点数 613；raise: HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='SSO authentication is not enabled'), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid provider ID'), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Unknown SSO provider: {provider}'), HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Missing code or state parameter'), HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Missing or expired OIDC state cookie'), HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='OIDC state mismatch'), HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail='Failed to connect to SSO provider')；return: RedirectResponse(url=redirect, status_code=status.HTTP_302_FOUND), redirect_response
  - 调用: get_app_config, warning, _build_error_redirect, RedirectResponse, HTTPException, match, get, get_state_cookie, compare_digest, _resolve_oidc_redirect_uri, _get_oidc_service, discover, error, authenticate_callback, get_or_provision_oidc_user, get_local_provider, create_access_token, str, quote, _set_session_cookie（+2）

#### `ƒ` `_build_error_redirect(frontend_base_url: str | None, error_code: str) -> str`  L815
  - _文档首行_（仅供参考）: Build a frontend redirect URL with an error parameter.
  - 分支数 0，函数体节点数 32；return: f'{base}/login?error={error_code}'

#### `ƒ` `validate_next_param(next_param: str | None) -> str | None`  L821
  - _文档首行_（仅供参考）: Validate and sanitize the ``next`` redirect parameter.
  - 分支数 4，函数体节点数 67；return: None, next_param
  - 调用: startswith

## 类
### 类 `LoginResponse`  L49
- 继承: BaseModel
- _文档首行_: Response model for login — token only lives in HttpOnly cookie.
- 类/实例变量:
  - `expires_in` = <annotated>
  - `needs_setup` = False

### 类 `RegisterRequest`  L126
- 继承: BaseModel
- _文档首行_: Request model for user registration.
- 类/实例变量:
  - `email` = <annotated>
  - `password` = Field(..., min_length=8)
  - `remember_me` = True
  - `_strong_password` = field_validator('password')(classmethod(lambda cls, v: _v...

### 类 `ChangePasswordRequest`  L136
- 继承: BaseModel
- _文档首行_: Request model for password change (also handles setup flow).
- 类/实例变量:
  - `current_password` = <annotated>
  - `new_password` = Field(..., min_length=8)
  - `new_email` = None
  - `remember_me` = None
  - `_strong_password` = field_validator('new_password')(classmethod(lambda cls, v...

### 类 `MessageResponse`  L147
- 继承: BaseModel
- _文档首行_: Generic message response.
- 类/实例变量:
  - `message` = <annotated>

### 类 `InitializeAdminRequest`  L488
- 继承: BaseModel
- _文档首行_: Request model for first-boot admin account creation.
- 类/实例变量:
  - `email` = <annotated>
  - `password` = Field(..., min_length=8)
  - `remember_me` = True
  - `_strong_password` = field_validator('password')(classmethod(lambda cls, v: _v...

## 文件内调用关系
- `_validate_strong_password` -> _password_is_common
- `_get_client_ip` -> _trusted_proxies
- `login_local` -> _get_client_ip, _check_rate_limit, _record_login_failure, _record_login_success, _set_session_cookie
- `register` -> _set_session_cookie
- `change_password` -> _set_session_cookie, _set_csrf_cookie
- `setup_status` -> _get_client_ip
- `initialize_admin` -> _set_session_cookie
- `oauth_login` -> validate_next_param, _resolve_oidc_redirect_uri, _get_oidc_service
- `oauth_callback` -> _build_error_redirect, _resolve_oidc_redirect_uri, _get_oidc_service, _set_session_cookie, _set_csrf_cookie

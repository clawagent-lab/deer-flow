# `backend/app/gateway/csrf_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/csrf_middleware.py`  ·  行数: 264

**模块文档首行**（仅供参考）: CSRF protection middleware for FastAPI.

## 模块概览
- 函数 15 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: os, secrets
- `collections.abc` -> Awaitable, Callable
- `urllib.parse` -> urlsplit
- `fastapi` -> Request, Response
- `starlette.middleware.base` -> BaseHTTPMiddleware
- `starlette.responses` -> JSONResponse
- `starlette.types` -> ASGIApp
- `app.gateway.auth.config` -> get_auth_config
- `app.gateway.auth.session_cookie_state` -> SESSION_COOKIE_ISSUED_STATE_ATTR, SESSION_COOKIE_MAX_AGE_STATE_ATTR, SESSION_COOKIE_SECURE_STATE_ATTR, SKIP_AUTH_CSRF_COOKIE_STATE_ATTR
- `app.gateway.auth_disabled` -> is_auth_disabled

## 模块级常量
- `CSRF_COOKIE_NAME` = 'csrf_token'
- `CSRF_HEADER_NAME` = 'X-CSRF-Token'
- `CSRF_TOKEN_LENGTH` = 64
- `_AUTH_EXEMPT_PATHS` = frozenset({'/api/v1/auth/login/local', '/api/v1/auth/logo...

## 函数
#### `ƒ` `is_secure_request(request: Request) -> bool`  L26
  - _文档首行_（仅供参考）: Detect whether the original client request was made over HTTPS.
  - 分支数 0，函数体节点数 18；return: _request_scheme(request) == 'https'
  - 调用: _request_scheme

#### `ƒ` `generate_csrf_token() -> str`  L31
  - _文档首行_（仅供参考）: Generate a secure random CSRF token.
  - 分支数 0，函数体节点数 14；return: secrets.token_urlsafe(CSRF_TOKEN_LENGTH)
  - 调用: token_urlsafe

#### `ƒ` `should_check_csrf(request: Request) -> bool`  L36
  - _文档首行_（仅供参考）: Determine if a request needs CSRF validation.
  - 分支数 4，函数体节点数 66；return: False, True
  - 调用: is_auth_disabled, rstrip, startswith

#### `ƒ` `is_auth_endpoint(request: Request) -> bool`  L69
  - _文档首行_（仅供参考）: Check if the request is to an auth endpoint.
  - 分支数 0，函数体节点数 24；return: request.url.path.rstrip('/') in _AUTH_EXEMPT_PATHS
  - 调用: rstrip

#### `ƒ` `_host_with_optional_port(hostname: str, port: int | None, scheme: str) -> str`  L77
  - _文档首行_（仅供参考）: Return normalized host[:port], omitting default ports.
  - 分支数 2，函数体节点数 95；return: host, f'{host}:{port}'
  - 调用: lower, startswith

#### `ƒ` `_normalize_origin(origin: str) -> str | None`  L88
  - _文档首行_（仅供参考）: Return a normalized scheme://host[:port] origin, or None for invalid input.
  - 分支数 3，函数体节点数 107；return: None, f'{scheme}://{_host_with_optional_port(parsed.hostname, port, scheme)}'
  - 调用: urlsplit, strip, lower, _host_with_optional_port

#### `ƒ` `_configured_cors_origins() -> set[str]`  L107
  - _文档首行_（仅供参考）: Return explicit configured browser origins that may call auth routes.
  - 分支数 3，函数体节点数 75；return: origins
  - 调用: set, split, get, strip, _normalize_origin, add

#### `ƒ` `get_configured_cors_origins() -> set[str]`  L120
  - _文档首行_（仅供参考）: Return normalized explicit browser origins from GATEWAY_CORS_ORIGINS.
  - 分支数 0，函数体节点数 14；return: _configured_cors_origins()
  - 调用: _configured_cors_origins

#### `ƒ` `_first_header_value(value: str | None) -> str | None`  L125
  - _文档首行_（仅供参考）: Return the first value from a comma-separated proxy header.
  - 分支数 1，函数体节点数 44；return: None, first or None
  - 调用: strip, split

#### `ƒ` `_forwarded_param(request: Request, name: str) -> str | None`  L133
  - _文档首行_（仅供参考）: Extract a parameter from the first RFC 7239 Forwarded header entry.
  - 分支数 3，函数体节点数 92；return: None, value.strip().strip('"') or None
  - 调用: _first_header_value, get, split, partition, strip, lower

#### `ƒ` `_request_scheme(request: Request) -> str`  L146
  - _文档首行_（仅供参考）: Resolve the original request scheme from trusted proxy headers.
  - 分支数 0，函数体节点数 43；return: scheme.lower()
  - 调用: _forwarded_param, _first_header_value, get, lower

#### `ƒ` `_request_origin(request: Request) -> str | None`  L152
  - _文档首行_（仅供参考）: Build the origin for the URL the browser is targeting.
  - 分支数 1，函数体节点数 113；return: _normalize_origin(f'{scheme}://{host}')
  - 调用: _request_scheme, _forwarded_param, _first_header_value, get, rsplit, _normalize_origin

#### `ƒ` `is_allowed_auth_origin(request: Request) -> bool`  L164
  - _文档首行_（仅供参考）: Allow auth POSTs only from the same origin or explicit configured origins.
  - 分支数 2，函数体节点数 74；return: True, False, normalized_origin in _configured_cors_origins() or (request_origin is not None and normalized_origin == request_origin)
  - 调用: get, _normalize_origin, _request_origin, _configured_cors_origins

#### `ƒ` `auth_csrf_cookie_settings(request: Request) -> tuple[bool, int | None]`  L185
  - _文档首行_（仅供参考）: Return ``(secure, max_age)`` for auth-created CSRF cookies.
  - 分支数 1，函数体节点数 99；return: (bool(getattr(request.state, SESSION_COOKIE_SECURE_STATE_ATTR, is_secure_request(request))), getattr(request.state, SESSION_COOKIE_MAX_AGE_STATE_ATTR, None)), (secure, max_age)
  - 调用: getattr, bool, is_secure_request, get_auth_config
  - 反射: getattr (L187), getattr (L190), getattr (L191)

#### `ƒ` `get_csrf_token(request: Request) -> str | None`  L257
  - _文档首行_（仅供参考）: Get the CSRF token from the current request's cookies.
  - 分支数 0，函数体节点数 22；return: request.cookies.get(CSRF_COOKIE_NAME)
  - 调用: get

## 类
### 类 `CSRFMiddleware`  L199
- 继承: BaseHTTPMiddleware
- _文档首行_: Middleware that implements CSRF protection using Double Submit Cookie pattern.
- 方法:
  #### `m` `__init__(self, app: ASGIApp) -> None`  L202
    - 分支数 0，函数体节点数 16
    - 调用: __init__, super
  #### `⏵m` `async dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response`  L205
    - 分支数 5，函数体节点数 215；return: JSONResponse(status_code=403, content={'detail': 'Cross-site auth request denied.'}), JSONResponse(status_code=403, content={'detail': 'CSRF token missing. Include X-CSRF-Token header.'}), JSONResponse(status_code=403, content={'detail': 'CSRF token mismatch.'}), response
    - 调用: is_auth_endpoint, should_check_csrf, is_allowed_auth_origin, JSONResponse, get, compare_digest, call_next, getattr, generate_csrf_token, auth_csrf_cookie_settings, set_cookie
  - 反射: getattr (L236)

## 文件内调用关系
- `is_secure_request` -> _request_scheme
- `_normalize_origin` -> _host_with_optional_port
- `_configured_cors_origins` -> _normalize_origin
- `get_configured_cors_origins` -> _configured_cors_origins
- `_forwarded_param` -> _first_header_value
- `_request_scheme` -> _forwarded_param, _first_header_value
- `_request_origin` -> _request_scheme, _forwarded_param, _first_header_value, _normalize_origin
- `is_allowed_auth_origin` -> _normalize_origin, _request_origin, _configured_cors_origins
- `auth_csrf_cookie_settings` -> is_secure_request
- `CSRFMiddleware.__init__` -> __init__
- `CSRFMiddleware.dispatch` -> is_auth_endpoint, should_check_csrf, is_allowed_auth_origin, generate_csrf_token, auth_csrf_cookie_settings

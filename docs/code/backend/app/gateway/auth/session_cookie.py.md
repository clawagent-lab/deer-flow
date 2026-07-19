# `backend/app/gateway/auth/session_cookie.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/session_cookie.py`  ·  行数: 111

**模块文档首行**（仅供参考）: Browser session cookie policy for Gateway authentication.

## 模块概览
- 函数 6 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: logging, os
- `dataclasses` -> dataclass
- `ipaddress` -> ip_address
- `fastapi` -> Request, Response
- `app.gateway.auth.config` -> get_auth_config
- `app.gateway.auth.session_cookie_state` -> SESSION_COOKIE_ISSUED_STATE_ATTR, SESSION_COOKIE_MAX_AGE_STATE_ATTR, SESSION_COOKIE_SECURE_STATE_ATTR
- `app.gateway.csrf_middleware` -> is_secure_request

## 模块级常量
- `ACCESS_TOKEN_COOKIE_NAME` = 'access_token'
- `SESSION_PERSISTENCE_COOKIE_NAME` = 'deerflow_session_persistent'
- `ALLOW_INSECURE_PERSISTENT_COOKIE_ENV` = 'DEER_FLOW_AUTH_ALLOW_INSECURE_PERSISTENT_COOKIE'
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_env_flag_enabled(name: str) -> bool`  L34
  - 分支数 0，函数体节点数 31；return: os.environ.get(name, '').strip().lower() in {'1', 'true', 'yes', 'on'}
  - 调用: lower, strip, get

#### `ƒ` `_request_hostname(request: Request) -> str`  L38
  - _文档首行_（仅供参考）: Return the direct request host without trusting forwarded host headers.
  - 分支数 1，函数体节点数 28；return: request.url.hostname.lower(), ''
  - 调用: lower

#### `ƒ` `is_local_browser_origin(request: Request) -> bool`  L45
  - _文档首行_（仅供参考）: Return True for loopback browser origins where HTTP persistence is acceptable.
  - 分支数 2，函数体节点数 47；return: True, ip_address(host).is_loopback, False
  - 调用: _request_hostname, endswith, ip_address

#### `ƒ` `_remember_me_from_cookie(request: Request, *, default: bool) -> bool`  L56
  - 分支数 2，函数体节点数 41；return: True, False, default
  - 调用: get

#### `ƒ` `resolve_session_cookie_policy(request: Request, *, remember_me: bool | None, default_remember_me: bool) -> SessionCookiePolicy`  L65
  - _文档首行_（仅供参考）: Resolve session cookie settings from user intent and deployment context.
  - 分支数 4，函数体节点数 135；return: SessionCookiePolicy(secure=secure, max_age=None, reason='session_requested'), SessionCookiePolicy(secure=True, max_age=lifetime_seconds, reason='secure_persistent'), SessionCookiePolicy(secure=False, max_age=lifetime_seconds, reason='localhost_persistent'), SessionCookiePolicy(secure=False, max_age=lifetime_seconds, reason='operator_insecure_persistent'), SessionCookiePolicy(secure=False, max_age=None, reason='public_http_session')
  - 调用: _remember_me_from_cookie, is_secure_request, get_auth_config, SessionCookiePolicy, is_local_browser_origin, _env_flag_enabled

#### `ƒ` `set_session_cookie(response: Response, request: Request, token: str, *, remember_me: bool | None, default_remember_me: bool) -> SessionCookiePolicy`  L86
  - _文档首行_（仅供参考）: Set the HttpOnly access-token cookie and stamp its lifetime on request state.
  - 分支数 0，函数体节点数 175；return: policy
  - 调用: _remember_me_from_cookie, resolve_session_cookie_policy, set_cookie, setattr, debug
  - 反射: setattr (L106), setattr (L107), setattr (L108)

## 类
### 类 `SessionCookiePolicy`  L26  @dataclass(...)
- _文档首行_: Resolved cookie settings for a session-creating auth response.
- 类/实例变量:
  - `secure` = <annotated>
  - `max_age` = <annotated>
  - `reason` = <annotated>

## 文件内调用关系
- `is_local_browser_origin` -> _request_hostname
- `resolve_session_cookie_policy` -> _remember_me_from_cookie, is_local_browser_origin, _env_flag_enabled
- `set_session_cookie` -> _remember_me_from_cookie, resolve_session_cookie_policy

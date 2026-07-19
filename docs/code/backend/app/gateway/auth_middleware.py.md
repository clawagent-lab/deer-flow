# `backend/app/gateway/auth_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth_middleware.py`  ·  行数: 160

**模块文档首行**（仅供参考）: Global authentication middleware — fail-closed safety net.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 2 个

## 依赖（import）
- `collections.abc` -> Callable
- `fastapi` -> HTTPException, Request, Response
- `starlette.middleware.base` -> BaseHTTPMiddleware
- `starlette.responses` -> JSONResponse
- `starlette.types` -> ASGIApp
- `app.gateway.auth.errors` -> AuthErrorCode, AuthErrorResponse
- `app.gateway.auth_disabled` -> AUTH_SOURCE_AUTH_DISABLED, AUTH_SOURCE_INTERNAL, AUTH_SOURCE_SESSION, get_auth_disabled_user, is_auth_disabled
- `app.gateway.authz` -> _ALL_PERMISSIONS, AuthContext
- `app.gateway.internal_auth` -> INTERNAL_AUTH_HEADER_NAME, get_internal_user, is_valid_internal_auth_token
- `deerflow.runtime.user_context` -> reset_current_user, set_current_user

## 模块级常量
- `_PUBLIC_PATH_PREFIXES` = ('/health', '/docs', '/redoc', '/openapi.json', '/api/v1/...
- `_PUBLIC_EXACT_PATHS` = frozenset({'/api/v1/auth/login/local', '/api/v1/auth/regi...

## 函数
#### `ƒ` `_is_public(path: str) -> bool`  L58
  - 分支数 1，函数体节点数 42；return: True, any((path.startswith(prefix) for prefix in _PUBLIC_PATH_PREFIXES))
  - 调用: rstrip, any, startswith

## 类
### 类 `AuthMiddleware`  L65
- 继承: BaseHTTPMiddleware
- _文档首行_: Strict auth gate: reject requests without a valid session.
- 方法:
  #### `m` `__init__(self, app: ASGIApp) -> None`  L85
    - 分支数 0，函数体节点数 16
    - 调用: __init__, super
  #### `⏵m` `async dispatch(self, request: Request, call_next: Callable) -> Response`  L88
    - 分支数 9，函数体节点数 258；return: await call_next(request), JSONResponse(status_code=exc.status_code, content={'detail': exc.detail}), JSONResponse(status_code=401, content={'detail': AuthErrorResponse(code=AuthErrorCode.NOT_AUTHENTICATED, message='Authentication required').model_dump()})
    - 调用: _is_public, call_next, is_valid_internal_auth_token, get, strip, get_internal_user, get_current_user_from_request, is_auth_disabled, JSONResponse, get_auth_disabled_user, model_dump, AuthErrorResponse, AuthContext, set_current_user, reset_current_user

## 文件内调用关系
- `AuthMiddleware.__init__` -> __init__
- `AuthMiddleware.dispatch` -> _is_public

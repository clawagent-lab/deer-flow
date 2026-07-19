# `backend/app/gateway/langgraph_auth.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/langgraph_auth.py`  ·  行数: 118

**模块文档首行**（仅供参考）: LangGraph compatibility auth handler — shares JWT logic with Gateway.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: secrets
- `langgraph_sdk` -> Auth
- `app.gateway.auth.errors` -> TokenError
- `app.gateway.auth.jwt` -> decode_token
- `app.gateway.auth_disabled` -> AUTH_DISABLED_USER_ID, is_auth_disabled
- `app.gateway.deps` -> get_local_provider

## 模块级常量
- `auth` = Auth()
- `_CSRF_METHODS` = frozenset({'POST', 'PUT', 'DELETE', 'PATCH'})

## 函数
#### `ƒ` `_check_csrf(request) -> None`  L32
  - _文档首行_（仅供参考）: Enforce Double Submit Cookie CSRF check for state-changing requests.
  - 分支数 4，函数体节点数 104；raise: Auth.exceptions.HTTPException(status_code=403, detail='CSRF token missing. Include X-CSRF-Token header.'), Auth.exceptions.HTTPException(status_code=403, detail='CSRF token mismatch.')；return: None
  - 调用: getattr, upper, is_auth_disabled, get, HTTPException, compare_digest
  - 反射: getattr (L38)

#### `⏵ƒ` `async authenticate(request)`    @auth.authenticate  L62
  - _文档首行_（仅供参考）: Validate the session cookie, decode JWT, and check token_version.
  - 分支数 5，函数体节点数 138；raise: Auth.exceptions.HTTPException(status_code=401, detail='Not authenticated'), Auth.exceptions.HTTPException(status_code=401, detail='Invalid token'), Auth.exceptions.HTTPException(status_code=401, detail='User not found'), Auth.exceptions.HTTPException(status_code=401, detail='Token revoked (password changed)')；return: AUTH_DISABLED_USER_ID, payload.sub
  - 调用: _check_csrf, is_auth_disabled, get, HTTPException, decode_token, isinstance, get_user, get_local_provider

#### `⏵ƒ` `async add_owner_filter(ctx: Auth.types.AuthContext, value: dict)`    @auth.on  L106
  - _文档首行_（仅供参考）: Inject user_id metadata on writes; filter by user_id on reads.
  - 分支数 0，函数体节点数 49；return: {'user_id': ctx.user.identity}
  - 调用: setdefault

## 文件内调用关系
- `authenticate` -> _check_csrf

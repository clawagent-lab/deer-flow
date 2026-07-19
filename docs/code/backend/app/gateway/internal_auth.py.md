# `backend/app/gateway/internal_auth.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/internal_auth.py`  ·  行数: 86

**模块文档首行**（仅供参考）: Authentication for trusted Gateway internal callers.

## 模块概览
- 函数 5 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: os, secrets
- `__future__` -> annotations
- `types` -> SimpleNamespace
- `typing` -> Any
- `deerflow.config.paths` -> make_safe_user_id
- `deerflow.runtime.user_context` -> DEFAULT_USER_ID

## 模块级常量
- `INTERNAL_AUTH_HEADER_NAME` = 'X-DeerFlow-Internal-Token'
- `INTERNAL_OWNER_USER_ID_HEADER_NAME` = 'X-DeerFlow-Owner-User-Id'
- `INTERNAL_AUTH_ENV_VAR` = 'DEER_FLOW_INTERNAL_AUTH_TOKEN'
- `INTERNAL_SYSTEM_ROLE` = 'internal'
- `_INTERNAL_AUTH_TOKEN` = _load_internal_auth_token()

## 函数
#### `ƒ` `_load_internal_auth_token() -> str`  L19
  - 分支数 1，函数体节点数 29；return: token, secrets.token_urlsafe(32)
  - 调用: get, token_urlsafe

#### `ƒ` `create_internal_auth_headers(*, owner_user_id: str | None) -> dict[str, str]`  L29
  - _文档首行_（仅供参考）: Return headers that authenticate trusted Gateway internal calls.
  - 分支数 1，函数体节点数 44；return: headers

#### `ƒ` `is_valid_internal_auth_token(token: str | None) -> bool`  L37
  - _文档首行_（仅供参考）: Return True when *token* matches this Gateway worker's internal token.
  - 分支数 0，函数体节点数 29；return: bool(token) and secrets.compare_digest(token, _INTERNAL_AUTH_TOKEN)
  - 调用: bool, compare_digest

#### `ƒ` `get_internal_user(owner_user_id: str | None)`  L42
  - _文档首行_（仅供参考）: Return the synthetic user used for trusted internal channel calls.
  - 分支数 1，函数体节点数 37；return: SimpleNamespace(id=effective_id, system_role=INTERNAL_SYSTEM_ROLE)
  - 调用: make_safe_user_id, SimpleNamespace

#### `ƒ` `get_trusted_internal_owner_user_id(request: Any) -> str | None`  L70
  - _文档首行_（仅供参考）: Return the owner override for a trusted internal request, if present.
  - 分支数 2，函数体节点数 74；return: None, owner_user_id or None
  - 调用: getattr, get, strip
  - 反射: getattr (L77), getattr (L77), getattr (L78)

## 文件内调用关系
_无文件内调用_

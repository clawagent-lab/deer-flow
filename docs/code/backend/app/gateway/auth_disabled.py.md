# `backend/app/gateway/auth_disabled.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth_disabled.py`  ·  行数: 58

**模块文档首行**（仅供参考）: Shared helpers for local/E2E auth-disabled mode.

## 模块概览
- 函数 5 个，类 0 个，模块级常量 9 个

## 依赖（import）
- 模块: logging, os
- `__future__` -> annotations
- `types` -> SimpleNamespace
- `deerflow.runtime.user_context` -> DEFAULT_USER_ID

## 模块级常量
- `AUTH_DISABLED_ENV_VAR` = 'DEER_FLOW_AUTH_DISABLED'
- `AUTH_DISABLED_USER_ID` = DEFAULT_USER_ID
- `AUTH_DISABLED_USER_EMAIL` = 'default@test.local'
- `AUTH_SOURCE_SESSION` = 'session'
- `AUTH_SOURCE_INTERNAL` = 'internal'
- `AUTH_SOURCE_AUTH_DISABLED` = 'auth_disabled'
- `_PRODUCTION_ENV_VARS` = ('DEER_FLOW_ENV', 'ENVIRONMENT')
- `_PRODUCTION_ENV_VALUES` = frozenset({'prod', 'production'})
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `is_explicit_production_environment() -> bool`  L25
  - 分支数 0，函数体节点数 34；return: any((os.environ.get(name, '').strip().lower() in _PRODUCTION_ENV_VALUES for name in _PRODUCTION_ENV_VARS))
  - 调用: any, lower, strip, get

#### `ƒ` `is_auth_disabled_requested() -> bool`  L29
  - 分支数 0，函数体节点数 17；return: os.environ.get(AUTH_DISABLED_ENV_VAR) == '1'
  - 调用: get

#### `ƒ` `is_auth_disabled() -> bool`  L33
  - 分支数 0，函数体节点数 15；return: is_auth_disabled_requested() and (not is_explicit_production_environment())
  - 调用: is_auth_disabled_requested, is_explicit_production_environment

#### `ƒ` `warn_if_auth_disabled_enabled() -> None`  L37
  - 分支数 1，函数体节点数 21；return: None
  - 调用: is_auth_disabled, warning

#### `ƒ` `get_auth_disabled_user()`  L48
  - 分支数 0，函数体节点数 22；return: SimpleNamespace(id=AUTH_DISABLED_USER_ID, email=AUTH_DISABLED_USER_EMAIL, password_hash=None, system_role='admin', needs_setup=False, token_version=0, oauth_provider=None)
  - 调用: SimpleNamespace

## 文件内调用关系
- `is_auth_disabled` -> is_auth_disabled_requested, is_explicit_production_environment
- `warn_if_auth_disabled_enabled` -> is_auth_disabled

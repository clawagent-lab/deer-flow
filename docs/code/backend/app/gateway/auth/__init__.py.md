# `backend/app/gateway/auth/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/__init__.py`  ·  行数: 43

**模块文档首行**（仅供参考）: Authentication module for DeerFlow.

## 模块概览
- 函数 0 个，类 0 个，模块级常量 1 个
- `__all__`: AuthConfig, get_auth_config, set_auth_config, AuthErrorCode, AuthErrorResponse, TokenError, TokenPayload, create_access_token, decode_token, hash_password, verify_password, User, UserResponse, AuthProvider, LocalAuthProvider, UserRepository

## 依赖（import）
- `app.gateway.auth.config` -> AuthConfig, get_auth_config, set_auth_config
- `app.gateway.auth.errors` -> AuthErrorCode, AuthErrorResponse, TokenError
- `app.gateway.auth.jwt` -> TokenPayload, create_access_token, decode_token
- `app.gateway.auth.local_provider` -> LocalAuthProvider
- `app.gateway.auth.models` -> User, UserResponse
- `app.gateway.auth.password` -> hash_password, verify_password
- `app.gateway.auth.providers` -> AuthProvider
- `app.gateway.auth.repositories.base` -> UserRepository

## 模块级常量
- `__all__` = ['AuthConfig', 'get_auth_config', 'set_auth_config', 'Aut...

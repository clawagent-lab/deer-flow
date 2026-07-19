# `backend/app/gateway/auth/user_provisioning.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/user_provisioning.py`  ·  行数: 113

**模块文档首行**（仅供参考）: User provisioning for OIDC logins.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `fastapi` -> HTTPException, status
- `app.gateway.auth.local_provider` -> LocalAuthProvider
- `app.gateway.auth.oidc` -> OIDCIdentity
- `deerflow.config.auth_config` -> OIDCProviderConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `⏵ƒ` `async get_or_provision_oidc_user(provider_id: str, provider_config: OIDCProviderConfig, identity: OIDCIdentity, local_provider: LocalAuthProvider) -> dict`  L22
  - _文档首行_（仅供参考）: Resolve an OIDC identity to a DeerFlow user.
  - 分支数 9，函数体节点数 287；raise: HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Your email could not be verified by the identity provider. Please contact your administrator.'), HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='The identity provider did not provide an email address.'), HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Your email domain is not allowed. Please use an approved email address.'), HTTPException(status_code=status.HTTP_409_CONFLICT, detail='An account with this email already exists. Contact your administrator to link it to your SSO account.'), HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Automatic account creation is disabled. Contact your administrator.')；return: {'user': existing, 'created': False}, {'user': user, 'created': True}
  - 调用: get_user_by_oauth, HTTPException, lower, rsplit, lstrip, get_user_by_email, _resolve_role, create_oauth_user, info

#### `ƒ` `_resolve_role(email: str, admin_emails: list[str]) -> str`  L109
  - _文档首行_（仅供参考）: Return ``admin`` if the email is in the admin list, otherwise ``user``.
  - 分支数 0，函数体节点数 46；return: 'admin' if any((e.lower() == email_lower for e in admin_emails)) else 'user'
  - 调用: lower, any

## 文件内调用关系
- `get_or_provision_oidc_user` -> _resolve_role

# `backend/app/gateway/auth/local_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/local_provider.py`  ·  行数: 133

**模块文档首行**（仅供参考）: Local email/password authentication provider.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `app.gateway.auth.models` -> User
- `app.gateway.auth.password` -> hash_password_async, needs_rehash, verify_password_async
- `app.gateway.auth.providers` -> AuthProvider
- `app.gateway.auth.repositories.base` -> UserRepository

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `LocalAuthProvider`  L13
- 继承: AuthProvider
- _文档首行_: Email/password authentication provider using local database.
- 方法:
  #### `m` `__init__(self, repository: UserRepository)`  L16
    - _文档首行_（仅供参考）: Initialize with a UserRepository.
    - 分支数 0，函数体节点数 15
  #### `⏵m` `async authenticate(self, credentials: dict) -> User | None`  L24
    - _文档首行_（仅供参考）: Authenticate with email and password.
    - 分支数 6，函数体节点数 140；return: None, user
    - 调用: get, get_user_by_email, verify_password_async, needs_rehash, hash_password_async, update_user, warning
  #### `⏵m` `async get_user(self, user_id: str) -> User | None`  L61
    - _文档首行_（仅供参考）: Get user by ID.
    - 分支数 0，函数体节点数 24；return: await self._repo.get_user_by_id(user_id)
    - 调用: get_user_by_id
  #### `⏵m` `async create_user(self, email: str, password: str | None, system_role: str, needs_setup: bool) -> User`  L65
    - _文档首行_（仅供参考）: Create a new local user.
    - 分支数 0，函数体节点数 67；return: await self._repo.create_user(user)
    - 调用: hash_password_async, User, create_user
  #### `⏵m` `async get_user_by_oauth(self, provider: str, oauth_id: str) -> User | None`  L86
    - _文档首行_（仅供参考）: Get user by OAuth provider and ID.
    - 分支数 0，函数体节点数 29；return: await self._repo.get_user_by_oauth(provider, oauth_id)
    - 调用: get_user_by_oauth
  #### `⏵m` `async count_users(self) -> int`  L90
    - _文档首行_（仅供参考）: Return total number of registered users.
    - 分支数 0，函数体节点数 16；return: await self._repo.count_users()
    - 调用: count_users
  #### `⏵m` `async count_admin_users(self) -> int`  L94
    - _文档首行_（仅供参考）: Return number of admin users.
    - 分支数 0，函数体节点数 16；return: await self._repo.count_admin_users()
    - 调用: count_admin_users
  #### `⏵m` `async update_user(self, user: User) -> User`  L98
    - _文档首行_（仅供参考）: Update an existing user.
    - 分支数 0，函数体节点数 21；return: await self._repo.update_user(user)
    - 调用: update_user
  #### `⏵m` `async get_user_by_email(self, email: str) -> User | None`  L102
    - _文档首行_（仅供参考）: Get user by email.
    - 分支数 0，函数体节点数 24；return: await self._repo.get_user_by_email(email)
    - 调用: get_user_by_email
  #### `⏵m` `async create_oauth_user(self, email: str, oauth_provider: str, oauth_id: str, system_role: str) -> User`  L106
    - _文档首行_（仅供参考）: Create a new user from an OAuth/OIDC login.
    - 分支数 0，函数体节点数 53；return: await self._repo.create_user(user)
    - 调用: User, create_user

## 文件内调用关系
- `LocalAuthProvider.authenticate` -> get_user_by_email, update_user
- `LocalAuthProvider.create_user` -> create_user
- `LocalAuthProvider.get_user_by_oauth` -> get_user_by_oauth
- `LocalAuthProvider.count_users` -> count_users
- `LocalAuthProvider.count_admin_users` -> count_admin_users
- `LocalAuthProvider.update_user` -> update_user
- `LocalAuthProvider.get_user_by_email` -> get_user_by_email
- `LocalAuthProvider.create_oauth_user` -> create_user

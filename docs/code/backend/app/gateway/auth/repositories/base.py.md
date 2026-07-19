# `backend/app/gateway/auth/repositories/base.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/repositories/base.py`  ·  行数: 103

**模块文档首行**（仅供参考）: User repository interface for abstracting database operations.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 0 个

## 依赖（import）
- `abc` -> ABC, abstractmethod
- `app.gateway.auth.models` -> User

## 类
### 类 `UserNotFoundError`  L8
- 继承: LookupError
- _文档首行_: Raised when a user repository operation targets a non-existent row.

### 类 `UserRepository`  L18
- 继承: ABC
- _文档首行_: Abstract interface for user data storage.
- 方法:
  #### `⏵m` `async create_user(self, user: User) -> User`    @abstractmethod  L26
    - _文档首行_（仅供参考）: Create a new user.
    - 分支数 0，函数体节点数 15；raise: NotImplementedError
  #### `⏵m` `async get_user_by_id(self, user_id: str) -> User | None`    @abstractmethod  L41
    - _文档首行_（仅供参考）: Get user by ID.
    - 分支数 0，函数体节点数 18；raise: NotImplementedError
  #### `⏵m` `async get_user_by_email(self, email: str) -> User | None`    @abstractmethod  L53
    - _文档首行_（仅供参考）: Get user by email.
    - 分支数 0，函数体节点数 18；raise: NotImplementedError
  #### `⏵m` `async update_user(self, user: User) -> User`    @abstractmethod  L65
    - _文档首行_（仅供参考）: Update an existing user.
    - 分支数 0，函数体节点数 15；raise: NotImplementedError
  #### `⏵m` `async count_users(self) -> int`    @abstractmethod  L82
    - _文档首行_（仅供参考）: Return total number of registered users.
    - 分支数 0，函数体节点数 12；raise: NotImplementedError
  #### `⏵m` `async count_admin_users(self) -> int`    @abstractmethod  L87
    - _文档首行_（仅供参考）: Return number of users with system_role == 'admin'.
    - 分支数 0，函数体节点数 12；raise: NotImplementedError
  #### `⏵m` `async get_user_by_oauth(self, provider: str, oauth_id: str) -> User | None`    @abstractmethod  L92
    - _文档首行_（仅供参考）: Get user by OAuth provider and ID.
    - 分支数 0，函数体节点数 21；raise: NotImplementedError

## 文件内调用关系
_无文件内调用_

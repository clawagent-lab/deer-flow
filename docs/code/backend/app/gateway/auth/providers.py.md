# `backend/app/gateway/auth/providers.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/providers.py`  ·  行数: 25

**模块文档首行**（仅供参考）: Auth provider abstraction.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `abc` -> ABC, abstractmethod
- `app.gateway.auth.models` -> User

## 类
### 类 `AuthProvider`  L6
- 继承: ABC
- _文档首行_: Abstract base class for authentication providers.
- 方法:
  #### `⏵m` `async authenticate(self, credentials: dict) -> 'User | None'`    @abstractmethod  L10
    - _文档首行_（仅供参考）: Authenticate user with given credentials.
    - 分支数 0，函数体节点数 14；raise: NotImplementedError
  #### `⏵m` `async get_user(self, user_id: str) -> 'User | None'`    @abstractmethod  L18
    - _文档首行_（仅供参考）: Retrieve user by ID.
    - 分支数 0，函数体节点数 14；raise: NotImplementedError

## 文件内调用关系
_无文件内调用_

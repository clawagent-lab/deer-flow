# `backend/app/gateway/authz.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/authz.py`  ·  行数: 320

**模块文档首行**（仅供参考）: Authorization decorators and context for DeerFlow.

## 模块概览
- 函数 5 个，类 2 个，模块级常量 3 个

## 依赖（import）
- 模块: functools, inspect
- `__future__` -> annotations
- `collections.abc` -> Callable
- `types` -> SimpleNamespace
- `typing` -> TYPE_CHECKING, Any, ParamSpec, TypeVar
- `fastapi` -> HTTPException, Request

## 模块级常量
- `P` = ParamSpec('P')
- `T` = TypeVar('T')
- `_ALL_PERMISSIONS` = [Permissions.THREADS_READ, Permissions.THREADS_WRITE, Per...

## 函数
#### `ƒ` `get_auth_context(request: Request) -> AuthContext | None`  L107
  - _文档首行_（仅供参考）: Get AuthContext from request state.
  - 分支数 0，函数体节点数 22；return: getattr(request.state, 'auth', None)
  - 调用: getattr
  - 反射: getattr (L109)

#### `ƒ` `_make_test_request_stub() -> Any`  L122
  - _文档首行_（仅供参考）: Create a minimal request-like object for direct unit calls.
  - 分支数 0，函数体节点数 18；return: SimpleNamespace(state=SimpleNamespace(), cookies={}, _deerflow_test_bypass_auth=True)
  - 调用: SimpleNamespace

#### `⏵ƒ` `async _authenticate(request: Request) -> AuthContext`  L131
  - _文档首行_（仅供参考）: Authenticate request and return AuthContext.
  - 分支数 1，函数体节点数 45；return: AuthContext(user=None, permissions=[]), AuthContext(user=user, permissions=_ALL_PERMISSIONS)
  - 调用: get_optional_user_from_request, AuthContext

#### `ƒ` `require_auth(func: Callable[P, T]) -> Callable[P, T]`  L147
  - _文档首行_（仅供参考）: Decorator that authenticates the request and enforces authentication.
  - 分支数 4，函数体节点数 162；raise: ValueError("require_auth decorator requires 'request' parameter"), HTTPException(status_code=401, detail='Authentication required')；return: await func(*args, **kwargs), wrapper
  - 调用: get, signature, _make_test_request_stub, ValueError, getattr, func, _authenticate, HTTPException, wraps
  - 反射: getattr (L182)

#### `ƒ` `require_permission(resource: str, action: str, owner_check: bool, require_existing: bool) -> Callable[[Callable[P, T]], Callable[P, T]]`  L197
  - _文档首行_（仅供参考）: Decorator that checks permission for resource:action.
  - 分支数 11，函数体节点数 396；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=403, detail=f'Permission denied: {resource}:{action}'), ValueError("require_permission with owner_check=True requires 'thread_id' parameter"), HTTPException(status_code=404, detail=f'Thread {thread_id} not found')；return: await func(*args, **kwargs), wrapper, decorator
  - 调用: get, signature, _make_test_request_stub, func, getattr, _authenticate, HTTPException, has_permission, ValueError, get_thread_store, check_access, str, strip, wraps
  - 反射: getattr (L251), getattr (L254), getattr (L293)

## 类
### 类 `Permissions`  L48
- _文档首行_: Permission constants for resource:action format.
- 类/实例变量:
  - `THREADS_READ` = 'threads:read'
  - `THREADS_WRITE` = 'threads:write'
  - `THREADS_DELETE` = 'threads:delete'
  - `RUNS_CREATE` = 'runs:create'
  - `RUNS_READ` = 'runs:read'
  - `RUNS_CANCEL` = 'runs:cancel'

### 类 `AuthContext`  L62
- _文档首行_: Authentication context for the current request.
- 类/实例变量:
  - `__slots__` = ('user', 'permissions')
- 方法:
  #### `prop` `is_authenticated(self) -> bool`    @property  L79
    - _文档首行_（仅供参考）: Check if user is authenticated.
    - 分支数 0，函数体节点数 17；return: self.user is not None
  #### `m` `__init__(self, user: User | None, permissions: list[str] | None)`  L74
    - 分支数 0，函数体节点数 39
  #### `m` `has_permission(self, resource: str, action: str) -> bool`  L83
    - _文档首行_（仅供参考）: Check if context has permission for resource:action.
    - 分支数 0，函数体节点数 33；return: permission in self.permissions
  #### `m` `require_user(self) -> User`  L96
    - _文档首行_（仅供参考）: Get user or raise 401.
    - 分支数 1，函数体节点数 27；raise: HTTPException(status_code=401, detail='Authentication required')；return: self.user
    - 调用: HTTPException

## 文件内调用关系
- `require_auth` -> _make_test_request_stub, _authenticate
- `require_permission` -> _make_test_request_stub, _authenticate, has_permission

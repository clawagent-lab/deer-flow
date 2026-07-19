# `backend/packages/harness/deerflow/runtime/user_context.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/user_context.py`  ·  行数: 196

**模块文档首行**（仅供参考）: Request-scoped user context for user-based authorization.

## 模块概览
- 函数 7 个，类 2 个，模块级常量 3 个

## 依赖（import）
- `__future__` -> annotations
- `contextvars` -> ContextVar, Token
- `typing` -> Final, Protocol, runtime_checkable

## 模块级常量
- `_current_user` = ContextVar('deerflow_current_user', default=None)
- `DEFAULT_USER_ID` = 'default'
- `AUTO` = _AutoSentinel()

## 函数
#### `ƒ` `set_current_user(user: CurrentUser) -> Token[CurrentUser | None]`  L55
  - _文档首行_（仅供参考）: Set the current user for this async task.
  - 分支数 0，函数体节点数 24；return: _current_user.set(user)
  - 调用: set

#### `ƒ` `reset_current_user(token: Token[CurrentUser | None]) -> None`  L65
  - _文档首行_（仅供参考）: Restore the context to the state captured by ``token``.
  - 分支数 0，函数体节点数 23
  - 调用: reset

#### `ƒ` `get_current_user() -> CurrentUser | None`  L70
  - _文档首行_（仅供参考）: Return the current user, or ``None`` if unset.
  - 分支数 0，函数体节点数 15；return: _current_user.get()
  - 调用: get

#### `ƒ` `require_current_user() -> CurrentUser`  L79
  - _文档首行_（仅供参考）: Return the current user, or raise :class:`RuntimeError`.
  - 分支数 1，函数体节点数 28；raise: RuntimeError('repository accessed without user context')；return: user
  - 调用: get, RuntimeError

#### `ƒ` `get_effective_user_id() -> str`  L100
  - _文档首行_（仅供参考）: Return the current user's id as a string, or DEFAULT_USER_ID if unset.
  - 分支数 1，函数体节点数 31；return: DEFAULT_USER_ID, str(user.id)
  - 调用: get, str

#### `ƒ` `resolve_runtime_user_id(runtime: object | None) -> str`  L112
  - _文档首行_（仅供参考）: Single source of truth for a tool/middleware's effective user_id.
  - 分支数 2，函数体节点数 52；return: str(ctx_user_id), get_effective_user_id()
  - 调用: getattr, isinstance, get, str, get_effective_user_id
  - 反射: getattr (L132)

#### `ƒ` `resolve_user_id(value: str | None | _AutoSentinel, *, method_name: str) -> str | None`  L166
  - _文档首行_（仅供参考）: Resolve the user_id parameter passed to a repository method.
  - 分支数 2，函数体节点数 65；raise: RuntimeError(f'{method_name} called with user_id=AUTO but no user context is set; pass an explicit user_id, set the contextvar via auth middleware, or opt out with user_id=None for migration/CLI paths.')；return: str(user.id), value
  - 调用: isinstance, get, RuntimeError, str

## 类
### 类 `CurrentUser`  L42  @runtime_checkable
- 继承: Protocol
- _文档首行_: Structural type for the current authenticated user.
- 类/实例变量:
  - `id` = <annotated>

### 类 `_AutoSentinel`  L149
- _文档首行_: Singleton marker meaning 'resolve user_id from contextvar'.
- 类/实例变量:
  - `_instance` = None
- 方法:
  #### `m` `__new__(cls) -> _AutoSentinel`  L154
    - 分支数 1，函数体节点数 31；return: cls._instance
    - 调用: __new__, super
  #### `m` `__repr__(self) -> str`  L159
    - 分支数 0，函数体节点数 7；return: '<AUTO>'

## 文件内调用关系
- `resolve_runtime_user_id` -> get_effective_user_id
- `_AutoSentinel.__new__` -> __new__

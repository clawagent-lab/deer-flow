# `backend/app/gateway/auth/repositories/sqlite.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/repositories/sqlite.py`  ·  行数: 128

**模块文档首行**（仅供参考）: SQLAlchemy-backed UserRepository implementation.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC
- `uuid` -> UUID
- `sqlalchemy` -> func, select
- `sqlalchemy.exc` -> IntegrityError
- `sqlalchemy.ext.asyncio` -> AsyncSession, async_sessionmaker
- `app.gateway.auth.models` -> User
- `app.gateway.auth.repositories.base` -> UserNotFoundError, UserRepository
- `deerflow.persistence.user.model` -> UserRow

## 类
### 类 `SQLiteUserRepository`  L27
- 继承: UserRepository
- _文档首行_: Async user repository backed by the shared SQLAlchemy engine.
- 方法:
  #### `st` `_row_to_user(row: UserRow) -> User`    @staticmethod  L36
    - 分支数 0，函数体节点数 78；return: User(id=UUID(row.id), email=row.email, password_hash=row.password_hash, system_role=row.system_role, created_at=row.created_at if row.created_at.tzinfo else row.created_at.replace(tzinfo=UTC), oauth_provider=row.oauth_provider, oauth_id=row.oauth_id, needs_setup=row.needs_setup, token_version=row.token_version)
    - 调用: User, UUID, replace
  - 文件IO: replace (L44)
  #### `st` `_user_to_row(user: User) -> UserRow`    @staticmethod  L52
    - 分支数 0，函数体节点数 61；return: UserRow(id=str(user.id), email=user.email, password_hash=user.password_hash, system_role=user.system_role, created_at=user.created_at, oauth_provider=user.oauth_provider, oauth_id=user.oauth_id, needs_setup=user.needs_setup, token_version=user.token_version)
    - 调用: UserRow, str
  #### `m` `__init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None`  L30
    - 分支数 0，函数体节点数 18
  #### `⏵m` `async create_user(self, user: User) -> User`  L67
    - _文档首行_（仅供参考）: Insert a new user. Raises ``ValueError`` on duplicate email.
    - 分支数 2，函数体节点数 71；raise: ValueError(f'Email already registered: {user.email}')；return: user
    - 调用: _user_to_row, _sf, add, commit, rollback, ValueError
  #### `⏵m` `async get_user_by_id(self, user_id: str) -> User | None`  L79
    - 分支数 1，函数体节点数 48；return: self._row_to_user(row) if row is not None else None
    - 调用: _sf, get, _row_to_user
  - 网络调用: get (L81)
  #### `⏵m` `async get_user_by_email(self, email: str) -> User | None`  L84
    - 分支数 1，函数体节点数 73；return: self._row_to_user(row) if row is not None else None
    - 调用: where, select, _sf, execute, scalar_one_or_none, _row_to_user
  #### `⏵m` `async update_user(self, user: User) -> User`  L91
    - 分支数 2，函数体节点数 126；raise: UserNotFoundError(f'User {user.id} no longer exists')；return: user
    - 调用: _sf, get, str, UserNotFoundError, commit
  - 网络调用: get (L93)
  #### `⏵m` `async count_users(self) -> int`  L112
    - 分支数 1，函数体节点数 42；return: await session.scalar(stmt) or 0
    - 调用: select_from, select, count, _sf, scalar
  #### `⏵m` `async count_admin_users(self) -> int`  L117
    - 分支数 1，函数体节点数 52；return: await session.scalar(stmt) or 0
    - 调用: where, select_from, select, count, _sf, scalar
  #### `⏵m` `async get_user_by_oauth(self, provider: str, oauth_id: str) -> User | None`  L122
    - 分支数 1，函数体节点数 84；return: self._row_to_user(row) if row is not None else None
    - 调用: where, select, _sf, execute, scalar_one_or_none, _row_to_user

## 文件内调用关系
- `SQLiteUserRepository.create_user` -> _user_to_row
- `SQLiteUserRepository.get_user_by_id` -> _row_to_user
- `SQLiteUserRepository.get_user_by_email` -> _row_to_user
- `SQLiteUserRepository.get_user_by_oauth` -> _row_to_user

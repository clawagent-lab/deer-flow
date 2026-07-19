# `backend/packages/harness/deerflow/persistence/user/model.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/user/model.py`  ·  行数: 60

**模块文档首行**（仅供参考）: ORM model for the users table.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> Boolean, DateTime, Index, String, text
- `sqlalchemy.orm` -> Mapped, mapped_column
- `deerflow.persistence.base` -> Base

## 类
### 类 `UserRow`  L22
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'users'
  - `id` = mapped_column(String(36), primary_key=True)
  - `email` = mapped_column(String(320), unique=True, nullable=False, i...
  - `password_hash` = mapped_column(String(128), nullable=True)
  - `system_role` = mapped_column(String(16), nullable=False, default='user')
  - `created_at` = mapped_column(DateTime(timezone=True), nullable=False, de...
  - `oauth_provider` = mapped_column(String(32), nullable=True)
  - `oauth_id` = mapped_column(String(128), nullable=True)
  - `needs_setup` = mapped_column(Boolean, nullable=False, default=False)
  - `token_version` = mapped_column(nullable=False, default=0)
  - `__table_args__` = (Index('idx_users_oauth_identity', 'oauth_provider', 'oau...

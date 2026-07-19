# `backend/packages/harness/deerflow/persistence/feedback/model.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/feedback/model.py`  ·  行数: 33

**模块文档首行**（仅供参考）: ORM model for user feedback on runs.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> DateTime, String, Text, UniqueConstraint
- `sqlalchemy.orm` -> Mapped, mapped_column
- `deerflow.persistence.base` -> Base

## 类
### 类 `FeedbackRow`  L13
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'feedback'
  - `__table_args__` = (UniqueConstraint('thread_id', 'run_id', 'user_id', name=...
  - `feedback_id` = mapped_column(String(64), primary_key=True)
  - `run_id` = mapped_column(String(64), nullable=False, index=True)
  - `thread_id` = mapped_column(String(64), nullable=False, index=True)
  - `user_id` = mapped_column(String(64), index=True)
  - `message_id` = mapped_column(String(64))
  - `rating` = mapped_column(nullable=False)
  - `comment` = mapped_column(Text)
  - `created_at` = mapped_column(DateTime(timezone=True), default=lambda: da...

# `backend/packages/harness/deerflow/persistence/models/run_event.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/models/run_event.py`  ·  行数: 36

**模块文档首行**（仅供参考）: ORM model for run events.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> JSON, DateTime, Index, String, Text, UniqueConstraint
- `sqlalchemy.orm` -> Mapped, mapped_column
- `deerflow.persistence.base` -> Base

## 类
### 类 `RunEventRow`  L13
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'run_events'
  - `id` = mapped_column(primary_key=True, autoincrement=True)
  - `thread_id` = mapped_column(String(64), nullable=False)
  - `run_id` = mapped_column(String(64), nullable=False)
  - `user_id` = mapped_column(String(64), nullable=True, index=True)
  - `event_type` = mapped_column(String(32), nullable=False)
  - `category` = mapped_column(String(16), nullable=False)
  - `content` = mapped_column(Text, default='')
  - `event_metadata` = mapped_column(JSON, default=dict)
  - `seq` = mapped_column(nullable=False)
  - `created_at` = mapped_column(DateTime(timezone=True), default=lambda: da...
  - `__table_args__` = (UniqueConstraint('thread_id', 'seq', name='uq_events_thr...

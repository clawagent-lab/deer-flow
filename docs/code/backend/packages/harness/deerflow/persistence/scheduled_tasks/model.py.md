# `backend/packages/harness/deerflow/persistence/scheduled_tasks/model.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/scheduled_tasks/model.py`  ·  行数: 40

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> JSON, DateTime, Integer, String, Text
- `sqlalchemy.orm` -> Mapped, mapped_column
- `deerflow.persistence.base` -> Base

## 类
### 类 `ScheduledTaskRow`  L11
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'scheduled_tasks'
  - `id` = mapped_column(String(64), primary_key=True)
  - `user_id` = mapped_column(String(64), index=True)
  - `thread_id` = mapped_column(String(64), index=True, nullable=True)
  - `context_mode` = mapped_column(String(32), default='fresh_thread_per_run')
  - `assistant_id` = mapped_column(String(128), nullable=True)
  - `title` = mapped_column(String(255))
  - `prompt` = mapped_column(Text)
  - `schedule_type` = mapped_column(String(16))
  - `schedule_spec` = mapped_column(JSON, default=dict)
  - `timezone` = mapped_column(String(64))
  - `status` = mapped_column(String(16), default='enabled', index=True)
  - `overlap_policy` = mapped_column(String(16), default='skip')
  - `next_run_at` = mapped_column(DateTime(timezone=True), index=True, nullab...
  - `last_run_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `last_run_id` = mapped_column(String(64), nullable=True)
  - `last_thread_id` = mapped_column(String(64), nullable=True)
  - `last_error` = mapped_column(Text, nullable=True)
  - `lease_owner` = mapped_column(String(128), nullable=True)
  - `lease_expires_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `run_count` = mapped_column(Integer, default=0)
  - `created_at` = mapped_column(DateTime(timezone=True), default=lambda: da...
  - `updated_at` = mapped_column(DateTime(timezone=True), default=lambda: da...

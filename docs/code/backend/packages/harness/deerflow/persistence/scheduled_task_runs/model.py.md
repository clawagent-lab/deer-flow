# `backend/packages/harness/deerflow/persistence/scheduled_task_runs/model.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/scheduled_task_runs/model.py`  ·  行数: 25

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> DateTime, String, Text
- `sqlalchemy.orm` -> Mapped, mapped_column
- `deerflow.persistence.base` -> Base

## 类
### 类 `ScheduledTaskRunRow`  L11
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'scheduled_task_runs'
  - `id` = mapped_column(String(64), primary_key=True)
  - `task_id` = mapped_column(String(64), index=True)
  - `thread_id` = mapped_column(String(64), index=True)
  - `run_id` = mapped_column(String(64), nullable=True)
  - `scheduled_for` = mapped_column(DateTime(timezone=True))
  - `trigger` = mapped_column(String(16))
  - `status` = mapped_column(String(16), index=True)
  - `error` = mapped_column(Text, nullable=True)
  - `started_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `finished_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `created_at` = mapped_column(DateTime(timezone=True), default=lambda: da...

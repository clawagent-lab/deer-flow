# `backend/packages/harness/deerflow/persistence/thread_meta/model.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/thread_meta/model.py`  ·  行数: 24

**模块文档首行**（仅供参考）: ORM model for thread metadata.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> JSON, DateTime, String
- `sqlalchemy.orm` -> Mapped, mapped_column
- `deerflow.persistence.base` -> Base

## 类
### 类 `ThreadMetaRow`  L13
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'threads_meta'
  - `thread_id` = mapped_column(String(64), primary_key=True)
  - `assistant_id` = mapped_column(String(128), index=True)
  - `user_id` = mapped_column(String(64), index=True)
  - `display_name` = mapped_column(String(256))
  - `status` = mapped_column(String(20), default='idle')
  - `metadata_json` = mapped_column(JSON, default=dict)
  - `created_at` = mapped_column(DateTime(timezone=True), default=lambda: da...
  - `updated_at` = mapped_column(DateTime(timezone=True), default=lambda: da...

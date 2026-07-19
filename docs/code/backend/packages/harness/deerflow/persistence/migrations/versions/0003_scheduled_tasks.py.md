# `backend/packages/harness/deerflow/persistence/migrations/versions/0003_scheduled_tasks.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/migrations/versions/0003_scheduled_tasks.py`  ·  行数: 95

**模块文档首行**（仅供参考）: scheduled tasks.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: sa
- `__future__` -> annotations
- `collections.abc` -> Sequence
- `alembic` -> op

## 模块级常量
- `revision` = '0003_scheduled_tasks'
- `down_revision` = '0002_runs_token_usage'
- `branch_labels` = None
- `depends_on` = None

## 函数
#### `ƒ` `upgrade() -> None`  L21
  - 分支数 3，函数体节点数 648；return: None
  - 调用: get_bind, inspect, has_table, create_table, Column, String, Text, JSON, DateTime, Integer, PrimaryKeyConstraint, batch_alter_table, create_index

#### `ƒ` `downgrade() -> None`  L82
  - 分支数 2，函数体节点数 90
  - 调用: batch_alter_table, drop_index, drop_table

## 文件内调用关系
_无文件内调用_

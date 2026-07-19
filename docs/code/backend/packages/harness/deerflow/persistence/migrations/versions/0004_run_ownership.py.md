# `backend/packages/harness/deerflow/persistence/migrations/versions/0004_run_ownership.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/migrations/versions/0004_run_ownership.py`  ·  行数: 135

**模块文档首行**（仅供参考）: run ownership.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: logging, sa
- `__future__` -> annotations
- `collections.abc` -> Sequence
- `alembic` -> op

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `revision` = '0004_run_ownership'
- `down_revision` = '0003_scheduled_tasks'
- `branch_labels` = None
- `depends_on` = None

## 函数
#### `ƒ` `_dedupe_active_runs_per_thread() -> None`  L24
  - _文档首行_（仅供参考）: Cancel superseded active rows so the partial unique index can be built.
  - 分支数 2，函数体节点数 84；return: None
  - 调用: get_bind, text, list, fetchall, execute, warning

#### `ƒ` `upgrade() -> None`  L90
  - 分支数 4，函数体节点数 154
  - 调用: safe_add_column, Column, String, DateTime, inspect, get_bind, get_indexes, batch_alter_table, create_index, _dedupe_active_runs_per_thread, text

#### `ƒ` `downgrade() -> None`  L120
  - 分支数 4，函数体节点数 103
  - 调用: get_bind, inspect, get_indexes, batch_alter_table, drop_index, safe_drop_column

## 文件内调用关系
- `upgrade` -> _dedupe_active_runs_per_thread

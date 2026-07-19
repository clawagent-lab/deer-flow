# `backend/packages/harness/deerflow/persistence/migrations/versions/0001_baseline.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/migrations/versions/0001_baseline.py`  ·  行数: 292

**模块文档首行**（仅供参考）: baseline -- chain root for DeerFlow application schema.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: sa
- `__future__` -> annotations
- `collections.abc` -> Sequence
- `alembic` -> op

## 模块级常量
- `revision` = '0001_baseline'
- `down_revision` = None
- `branch_labels` = None
- `depends_on` = None

## 函数
#### `ƒ` `upgrade() -> None`  L49
  - _文档首行_（仅供参考）: Upgrade schema.
  - 分支数 8，函数体节点数 2177
  - 调用: create_table, Column, String, JSON, DateTime, PrimaryKeyConstraint, UniqueConstraint, batch_alter_table, create_index, f, text, Text, Integer, Boolean, ForeignKeyConstraint

#### `ƒ` `downgrade() -> None`  L240
  - _文档首行_（仅供参考）: Downgrade schema.
  - 分支数 8，函数体节点数 431
  - 调用: drop_table, batch_alter_table, drop_index, f, text

## 文件内调用关系
_无文件内调用_

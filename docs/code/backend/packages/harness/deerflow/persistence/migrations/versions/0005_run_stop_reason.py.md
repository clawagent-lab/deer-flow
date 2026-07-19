# `backend/packages/harness/deerflow/persistence/migrations/versions/0005_run_stop_reason.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/migrations/versions/0005_run_stop_reason.py`  ·  行数: 29

**模块文档首行**（仅供参考）: run stop_reason

## 模块概览
- 函数 2 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: sa
- `__future__` -> annotations
- `collections.abc` -> Sequence
- `alembic` -> op

## 模块级常量
- `revision` = '0005_run_stop_reason'
- `down_revision` = '0004_run_ownership'
- `branch_labels` = None
- `depends_on` = None

## 函数
#### `ƒ` `upgrade() -> None`  L21
  - 分支数 0，函数体节点数 24
  - 调用: safe_add_column, Column, String

#### `ƒ` `downgrade() -> None`  L27
  - 分支数 0，函数体节点数 11
  - 调用: drop_column

## 文件内调用关系
_无文件内调用_

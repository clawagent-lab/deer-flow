# `backend/packages/harness/deerflow/persistence/migrations/versions/0002_runs_token_usage.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/migrations/versions/0002_runs_token_usage.py`  ·  行数: 70

**模块文档首行**（仅供参考）: Add ``runs.token_usage_by_model`` column.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: sa
- `__future__` -> annotations
- `collections.abc` -> Sequence
- `deerflow.persistence.migrations._helpers` -> safe_add_column, safe_drop_column

## 模块级常量
- `revision` = '0002_runs_token_usage'
- `down_revision` = '0001_baseline'
- `branch_labels` = None
- `depends_on` = None

## 函数
#### `ƒ` `upgrade() -> None`  L56
  - 分支数 0，函数体节点数 28
  - 调用: safe_add_column, Column, JSON, text

#### `ƒ` `downgrade() -> None`  L68
  - 分支数 0，函数体节点数 9
  - 调用: safe_drop_column

## 文件内调用关系
_无文件内调用_

# `backend/packages/harness/deerflow/persistence/migrations/_helpers.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/migrations/_helpers.py`  ·  行数: 190

**模块文档首行**（仅供参考）: Idempotent helpers for alembic column revisions.

## 模块概览
- 函数 7 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: logging, sa
- `__future__` -> annotations
- `alembic` -> op

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_EQUIVALENT_TYPE_FAMILIES` = (frozenset({'JSON', 'JSONB'}),)

## 函数
#### `ƒ` `_inspector() -> sa.Inspector`  L47
  - 分支数 0，函数体节点数 17；return: sa.inspect(op.get_bind())
  - 调用: inspect, get_bind

#### `ƒ` `_normalize_default(value: object) -> str | None`  L51
  - _文档首行_（仅供参考）: Normalize a server-default value for cross-source comparison.
  - 分支数 5，函数体节点数 153；return: None, text or None
  - 调用: isinstance, str, strip, startswith, endswith, split

#### `ƒ` `_normalize_type(value: object) -> str`  L78
  - _文档首行_（仅供参考）: Normalize a SQLAlchemy ``TypeEngine`` (or reflected type) for comparison.
  - 分支数 1，函数体节点数 52；return: '', s.upper().split('(', 1)[0].strip()
  - 调用: isinstance, repr, strip, split, upper

#### `ƒ` `_type_equivalent(actual: object, desired: object) -> bool`  L107
  - _文档首行_（仅供参考）: True if *actual* and *desired* are the same type or a known equivalent.
  - 分支数 2，函数体节点数 77；return: True, any((pair <= fam for fam in _EQUIVALENT_TYPE_FAMILIES))
  - 调用: _normalize_type, frozenset, any

#### `ƒ` `_check_column_drift(table: str, desired: sa.Column, actual: dict) -> None`  L123
  - _文档首行_（仅供参考）: Warn if an existing column's attributes diverge from the desired model.
  - 分支数 4，函数体节点数 200
  - 调用: bool, get, append, _normalize_default, _type_equivalent, _normalize_type, warning, join

#### `ƒ` `safe_add_column(table: str, column: sa.Column) -> None`  L159
  - _文档首行_（仅供参考）: ``op.add_column`` that no-ops when the table or column is missing/present.
  - 分支数 3，函数体节点数 96；return: None
  - 调用: _inspector, get_table_names, get_columns, _check_column_drift, batch_alter_table, add_column

#### `ƒ` `safe_drop_column(table: str, column_name: str) -> None`  L180
  - _文档首行_（仅供参考）: ``op.drop_column`` that no-ops when the table or column is already gone.
  - 分支数 3，函数体节点数 74；return: None
  - 调用: _inspector, get_table_names, get_columns, batch_alter_table, drop_column

## 文件内调用关系
- `_type_equivalent` -> _normalize_type
- `_check_column_drift` -> _normalize_default, _type_equivalent, _normalize_type
- `safe_add_column` -> _inspector, _check_column_drift
- `safe_drop_column` -> _inspector

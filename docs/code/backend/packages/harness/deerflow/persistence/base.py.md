# `backend/packages/harness/deerflow/persistence/base.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/base.py`  ·  行数: 56

**模块文档首行**（仅供参考）: SQLAlchemy declarative base with automatic to_dict support.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `functools` -> cache
- `sqlalchemy` -> sa_inspect
- `sqlalchemy.orm` -> DeclarativeBase

## 函数
#### `ƒ` `_column_keys(cls: type) -> tuple[str, ...]`    @cache  L19
  - _文档首行_（仅供参考）: Mapped column keys for an ORM class, in mapper order.
  - 分支数 0，函数体节点数 39；return: tuple((c.key for c in sa_inspect(cls).mapper.column_attrs))
  - 调用: tuple, sa_inspect

## 类
### 类 `Base`  L29
- 继承: DeclarativeBase
- _文档首行_: Base class for all DeerFlow ORM models.
- 方法:
  #### `m` `to_dict(self, *, exclude: set[str] | None) -> dict`  L37
    - _文档首行_（仅供参考）: Convert ORM instance to plain dict.
    - 分支数 1，函数体节点数 70；return: {k: getattr(self, k) for k in keys if k not in exclude}, {k: getattr(self, k) for k in keys}
    - 调用: _column_keys, type, getattr
  - 反射: getattr (L50), getattr (L51)
  #### `m` `__repr__(self) -> str`  L53
    - 分支数 0，函数体节点数 52；return: f'{type(self).__name__}({cols})'
    - 调用: join, getattr, _column_keys, type
  - 反射: getattr (L54)

## 文件内调用关系
- `Base.to_dict` -> _column_keys
- `Base.__repr__` -> _column_keys

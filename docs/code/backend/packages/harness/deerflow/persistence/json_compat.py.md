# `backend/packages/harness/deerflow/persistence/json_compat.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/json_compat.py`  ·  行数: 196

**模块文档首行**（仅供参考）: Dialect-aware JSON value matching for SQLAlchemy (SQLite + PostgreSQL).

## 模块概览
- 函数 9 个，类 2 个，模块级常量 6 个

## 依赖（import）
- 模块: re
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> Any
- `sqlalchemy` -> BigInteger, Float, String, bindparam
- `sqlalchemy.ext.compiler` -> compiles
- `sqlalchemy.sql.compiler` -> SQLCompiler
- `sqlalchemy.sql.expression` -> ColumnElement
- `sqlalchemy.sql.visitors` -> InternalTraversal
- `sqlalchemy.types` -> Boolean, TypeEngine

## 模块级常量
- `_KEY_CHARSET_RE` = re.compile('^[A-Za-z0-9_\\-]+$')
- `ALLOWED_FILTER_VALUE_TYPES` = (type(None), bool, int, float, str)
- `_INT64_MIN` = -2 ** 63
- `_INT64_MAX` = 2 ** 63 - 1
- `_SQLITE` = _Dialect(null_type='null', num_types=('integer', 'real'),...
- `_PG` = _Dialect(null_type='null', num_types=('number',), num_cas...

## 函数
#### `ƒ` `validate_metadata_filter_key(key: object) -> bool`  L28
  - _文档首行_（仅供参考）: Return True if *key* is safe for use as a JSON metadata filter key.
  - 分支数 0，函数体节点数 29；return: isinstance(key, str) and bool(_KEY_CHARSET_RE.match(key))
  - 调用: isinstance, bool, match

#### `ƒ` `validate_metadata_filter_value(value: object) -> bool`  L39
  - _文档首行_（仅供参考）: Return True if *value* is an allowed type for a JSON metadata filter.
  - 分支数 3，函数体节点数 56；return: False, True
  - 调用: isinstance

#### `ƒ` `_bind(compiler: SQLCompiler, value: object, sa_type: TypeEngine[Any], **kw) -> str`  L134
  - 分支数 0，函数体节点数 43；可变参数（*args/**kwargs）；return: compiler.process(param, **kw)
  - 调用: bindparam, process

#### `ƒ` `_type_check(typeof: str, types: tuple[str, ...]) -> str`  L139
  - 分支数 1，函数体节点数 68；return: f"{typeof} = '{types[0]}'", f'{typeof} IN ({quoted})'
  - 调用: len, join

#### `ƒ` `_build_clause(compiler: SQLCompiler, typeof: str, extract: str, value: object, dialect: _Dialect, **kw) -> str`  L146
  - 分支数 6，函数体节点数 282；可变参数（*args/**kwargs）；return: f"{typeof} = '{dialect.null_type}'", f"{typeof} = '{bool_str}'", f"({typeof} = '{dialect.bool_type}' AND {extract} = '{bool_str}')", f'(CASE WHEN {_type_check(typeof, dialect.int_types)} AND {extract} ~ {dialect.int_guard} THEN CAST({extract} AS {dialect.int_cast}) END = {bp})', f'({_type_check(typeof, dialect.int_types)} AND CAST({extract} AS {dialect.int_cast}) = {bp})', f'({_type_check(typeof, dialect.num_types)} AND CAST({extract} AS {dialect.num_cast}) = {bp})', f"({typeof} = '{dialect.string_type}' AND {extract} = {bp})"
  - 调用: isinstance, _bind, BigInteger, _type_check, Float, str, String

#### `ƒ` `_compile_sqlite(element: JsonMatch, compiler: SQLCompiler, **kw) -> str`    @compiles(...)  L169
  - 分支数 1，函数体节点数 111；可变参数（*args/**kwargs）；raise: ValueError(f'Key escaped validation: {element.key!r}')；return: _build_clause(compiler, typeof, extract, element.value, _SQLITE, **kw)
  - 调用: validate_metadata_filter_key, ValueError, process, _build_clause, compiles

#### `ƒ` `_compile_pg(element: JsonMatch, compiler: SQLCompiler, **kw) -> str`    @compiles(...)  L180
  - 分支数 1，函数体节点数 104；可变参数（*args/**kwargs）；raise: ValueError(f'Key escaped validation: {element.key!r}')；return: _build_clause(compiler, typeof, extract, element.value, _PG, **kw)
  - 调用: validate_metadata_filter_key, ValueError, process, _build_clause, compiles

#### `ƒ` `_compile_default(element: JsonMatch, compiler: SQLCompiler, **kw) -> str`    @compiles(...)  L190
  - 分支数 0，函数体节点数 31；可变参数（*args/**kwargs）；raise: NotImplementedError(f'JsonMatch supports only sqlite and postgresql; got dialect: {compiler.dialect.name}')
  - 调用: NotImplementedError, compiles

#### `ƒ` `json_match(column: ColumnElement, key: str, value: object) -> JsonMatch`  L194
  - 分支数 0，函数体节点数 23；return: JsonMatch(column, key, value)
  - 调用: JsonMatch

## 类
### 类 `JsonMatch`  L60
- 继承: ColumnElement
- _文档首行_: Dialect-portable ``column[key] == value`` for JSON columns.
- 类/实例变量:
  - `inherit_cache` = True
  - `type` = Boolean()
  - `_is_implicitly_boolean` = True
  - `_traverse_internals` = [('column', InternalTraversal.dp_clauseelement), ('key', ...
- 方法:
  #### `m` `__init__(self, column: ColumnElement, key: str, value: object) -> None`  L81
    - 分支数 3，函数体节点数 114；raise: ValueError(f'JsonMatch key must match {_KEY_CHARSET_RE.pattern!r}; got: {key!r}'), TypeError(f'JsonMatch int value out of signed 64-bit range [-2**63, 2**63-1]: {value!r}'), TypeError(f'JsonMatch value must be None, bool, int, float, or str; got: {type(value).__name__!r}')
    - 调用: validate_metadata_filter_key, ValueError, validate_metadata_filter_value, isinstance, TypeError, type, __init__, super

### 类 `_Dialect`  L95  @dataclass(...)
- _文档首行_: Per-dialect names used when emitting JSON type/value comparisons.
- 类/实例变量:
  - `null_type` = <annotated>
  - `num_types` = <annotated>
  - `num_cast` = <annotated>
  - `int_types` = <annotated>
  - `int_cast` = <annotated>
  - `int_guard` = <annotated>
  - `string_type` = <annotated>
  - `bool_type` = <annotated>

## 文件内调用关系
- `_build_clause` -> _bind, _type_check
- `_compile_sqlite` -> validate_metadata_filter_key, _build_clause
- `_compile_pg` -> validate_metadata_filter_key, _build_clause
- `JsonMatch.__init__` -> validate_metadata_filter_key, validate_metadata_filter_value, __init__

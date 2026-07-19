# `backend/packages/harness/deerflow/config/reload_boundary.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/reload_boundary.py`  ·  行数: 121

**模块文档首行**（仅供参考）: Single source of truth for the config hot-reload boundary.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 2 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Iterator

## 模块级常量
- `STARTUP_ONLY_PREFIX` = 'startup-only:'
- `STARTUP_ONLY_FIELDS` = {'database': 'init_engine_from_config() runs once during ...

## 函数
#### `ƒ` `iter_startup_only_field_paths() -> Iterator[str]`  L78
  - _文档首行_（仅供参考）: Yield every registered restart-required field path.
  - 分支数 0，函数体节点数 16；return: iter(STARTUP_ONLY_FIELDS)
  - 调用: iter

#### `ƒ` `is_startup_only_field(field_path: str) -> bool`  L83
  - _文档首行_（仅供参考）: Return ``True`` when *field_path* is registered as restart-required.
  - 分支数 0，函数体节点数 16；return: field_path in STARTUP_ONLY_FIELDS

#### `ƒ` `format_field_description(field_path: str, *, field_doc: str | None) -> str`  L93
  - _文档首行_（仅供参考）: Build the standardised description for a registered field.
  - 分支数 1，函数体节点数 57；return: header, f'{header}\n\n{field_doc.strip()}'
  - 调用: strip

## 文件内调用关系
_无文件内调用_

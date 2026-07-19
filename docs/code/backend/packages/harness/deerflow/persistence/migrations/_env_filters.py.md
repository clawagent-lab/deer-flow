# `backend/packages/harness/deerflow/persistence/migrations/_env_filters.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/migrations/_env_filters.py`  ·  行数: 37

**模块文档首行**（仅供参考）: Object filters used by ``env.py`` to scope alembic to DeerFlow tables.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations

## 模块级常量
- `LANGGRAPH_OWNED_TABLES` = frozenset({'checkpoints', 'checkpoint_blobs', 'checkpoint...

## 函数
#### `ƒ` `include_object(object_, name, type_, reflected, compare_to)`  L24
  - _文档首行_（仅供参考）: Returns False for any LangGraph-owned table or for an index/constraint
  - 分支数 2，函数体节点数 58；return: False, True
  - 调用: getattr
  - 反射: getattr (L33), getattr (L34)

## 文件内调用关系
_无文件内调用_

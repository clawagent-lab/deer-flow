# `backend/app/gateway/pagination.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/pagination.py`  ·  行数: 16

**模块文档首行**（仅供参考）: Shared pagination helpers for gateway routers.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations

## 函数
#### `ƒ` `trim_run_message_page(rows: list[dict], *, limit: int, after_seq: int | None) -> tuple[list[dict], bool]`  L6
  - _文档首行_（仅供参考）: Trim a ``limit + 1`` run-message page while preserving page boundaries.
  - 分支数 2，函数体节点数 87；return: (rows, False), (rows[:limit], True), (rows[-limit:], True)
  - 调用: len

## 文件内调用关系
_无文件内调用_

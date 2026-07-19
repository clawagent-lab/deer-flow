# `backend/sitecustomize.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/sitecustomize.py`  ·  行数: 27

**模块文档首行**（仅供参考）: Process-wide Python startup customizations for backend entrypoints.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: asyncio, sys
- `__future__` -> annotations

## 函数
#### `ƒ` `_configure_windows_event_loop_policy() -> None`  L14
  - 分支数 3，函数体节点数 51；return: None
  - 调用: getattr, isinstance, get_event_loop_policy, set_event_loop_policy, selector_policy
  - 反射: getattr (L18)

## 文件内调用关系
_无文件内调用_

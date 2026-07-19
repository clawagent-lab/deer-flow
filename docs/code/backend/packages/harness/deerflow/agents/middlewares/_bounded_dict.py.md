# `backend/packages/harness/deerflow/agents/middlewares/_bounded_dict.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/_bounded_dict.py`  ·  行数: 33

**模块文档首行**（仅供参考）: A small bounded ``OrderedDict`` shared by guard middlewares.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `collections` -> OrderedDict
- `typing` -> Any

## 类
### 类 `BoundedDict`  L15
- 继承: OrderedDict
- _文档首行_: An ``OrderedDict`` that evicts the oldest entry once ``maxsize`` is reached.
- 方法:
  #### `m` `__init__(self, maxsize: int, *args, **kwds) -> None`  L24
    - 分支数 0，函数体节点数 35；可变参数（*args/**kwargs）
    - 调用: __init__, super
  #### `m` `__setitem__(self, key: Any, value: Any) -> None`  L28
    - 分支数 2，函数体节点数 48
    - 调用: len, popitem, __setitem__, super

## 文件内调用关系
- `BoundedDict.__init__` -> __init__
- `BoundedDict.__setitem__` -> __setitem__

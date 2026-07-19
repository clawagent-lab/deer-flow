# `backend/packages/harness/deerflow/agents/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/__init__.py`  ·  行数: 38

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个
- `__all__`: create_deerflow_agent, RuntimeFeatures, Next, Prev, make_lead_agent, SandboxState, ThreadState

## 依赖（import）
- `.features` -> Next, Prev, RuntimeFeatures

## 模块级常量
- `__all__` = ['create_deerflow_agent', 'RuntimeFeatures', 'Next', 'Pre...

## 函数
#### `ƒ` `__getattr__(name: str)`  L14
  - 分支数 3，函数体节点数 103；raise: AttributeError(f'module {__name__!r} has no attribute {name!r}')；return: create_deerflow_agent, make_lead_agent, exports[name]
  - 调用: globals, prime_enabled_skills_cache, update, AttributeError

## 文件内调用关系
_无文件内调用_

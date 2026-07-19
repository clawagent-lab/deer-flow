# `backend/packages/harness/deerflow/subagents/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/subagents/__init__.py`  ·  行数: 25

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个
- `__all__`: SubagentConfig, SubagentExecutor, SubagentResult, get_available_subagent_names, get_subagent_config, list_subagents

## 依赖（import）
- `.config` -> SubagentConfig
- `.registry` -> get_available_subagent_names, get_subagent_config, list_subagents

## 模块级常量
- `__all__` = ['SubagentConfig', 'SubagentExecutor', 'SubagentResult', ...

## 函数
#### `ƒ` `__getattr__(name: str)`  L14
  - 分支数 1，函数体节点数 55；raise: AttributeError(f'module {__name__!r} has no attribute {name!r}')；return: exports[name]
  - 调用: update, globals, AttributeError

## 文件内调用关系
_无文件内调用_

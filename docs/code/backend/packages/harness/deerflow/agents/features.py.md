# `backend/packages/harness/deerflow/agents/features.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/features.py`  ·  行数: 71

**模块文档首行**（仅供参考）: Declarative feature flags and middleware positioning for create_deerflow_agent.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> TYPE_CHECKING, Literal
- `langchain.agents.middleware` -> AgentMiddleware

## 函数
#### `ƒ` `Next(anchor: type[AgentMiddleware])`  L49
  - _文档首行_（仅供参考）: Declare this middleware should be placed after *anchor* in the chain.
  - 分支数 1，函数体节点数 67；raise: TypeError(f'@Next expects an AgentMiddleware subclass, got {anchor!r}')；return: cls, decorator
  - 调用: isinstance, issubclass, TypeError

#### `ƒ` `Prev(anchor: type[AgentMiddleware])`  L61
  - _文档首行_（仅供参考）: Declare this middleware should be placed before *anchor* in the chain.
  - 分支数 1，函数体节点数 67；raise: TypeError(f'@Prev expects an AgentMiddleware subclass, got {anchor!r}')；return: cls, decorator
  - 调用: isinstance, issubclass, TypeError

## 类
### 类 `RuntimeFeatures`  L18  @dataclass
- _文档首行_: Declarative feature flags for ``create_deerflow_agent``.
- 类/实例变量:
  - `sandbox` = True
  - `memory` = False
  - `memory_config` = None
  - `summarization` = False
  - `subagent` = False
  - `vision` = False
  - `auto_title` = False
  - `guardrail` = False
  - `loop_detection` = True
  - `token_budget` = False

## 文件内调用关系
_无文件内调用_

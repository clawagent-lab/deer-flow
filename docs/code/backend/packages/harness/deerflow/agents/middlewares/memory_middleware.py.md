# `backend/packages/harness/deerflow/agents/middlewares/memory_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/memory_middleware.py`  ·  行数: 109

**模块文档首行**（仅供参考）: Middleware for memory mechanism.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `typing` -> TYPE_CHECKING, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langgraph.config` -> get_config
- `langgraph.runtime` -> Runtime
- `deerflow.agents.memory` -> get_memory_manager
- `deerflow.config.memory_config` -> get_memory_config
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.trace_context` -> DEERFLOW_TRACE_METADATA_KEY, get_current_trace_id, normalize_trace_id

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `MemoryMiddlewareState`  L22
- 继承: AgentState
- _文档首行_: Compatible with the `ThreadState` schema.

### 类 `MemoryMiddleware`  L28
- 继承: AgentMiddleware[MemoryMiddlewareState]
- _文档首行_: Middleware that queues conversation for memory update after agent execution.
- 类/实例变量:
  - `state_schema` = MemoryMiddlewareState
- 方法:
  #### `m` `__init__(self, agent_name: str | None, *, memory_config: 'MemoryConfig | None')`  L40
    - _文档首行_（仅供参考）: Initialize the MemoryMiddleware.
    - 分支数 0，函数体节点数 36
    - 调用: __init__, super
  #### `m` `after_agent(self, state: MemoryMiddlewareState, runtime: Runtime) -> dict | None`    @override  L53
    - _文档首行_（仅供参考）: Queue conversation for memory update after agent completes.
    - 分支数 7，函数体节点数 250；return: None
    - 调用: get_memory_config, get, get_config, debug, get_effective_user_id, isinstance, normalize_trace_id, get_current_trace_id, add, get_memory_manager

## 文件内调用关系
- `MemoryMiddleware.__init__` -> __init__

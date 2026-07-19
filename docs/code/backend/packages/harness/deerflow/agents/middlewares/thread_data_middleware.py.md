# `backend/packages/harness/deerflow/agents/middlewares/thread_data_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/thread_data_middleware.py`  ·  行数: 119

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `datetime` -> UTC, datetime
- `typing` -> NotRequired, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> HumanMessage
- `langgraph.config` -> get_config
- `langgraph.runtime` -> Runtime
- `deerflow.agents.thread_state` -> ThreadDataState
- `deerflow.config.paths` -> Paths, get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `ThreadDataMiddlewareState`  L18
- 继承: AgentState
- _文档首行_: Compatible with the `ThreadState` schema.
- 类/实例变量:
  - `thread_data` = <annotated>

### 类 `ThreadDataMiddleware`  L24
- 继承: AgentMiddleware[ThreadDataMiddlewareState]
- _文档首行_: Create thread data directories for each thread execution.
- 类/实例变量:
  - `state_schema` = ThreadDataMiddlewareState
- 方法:
  #### `m` `__init__(self, base_dir: str | None, lazy_init: bool)`  L39
    - _文档首行_（仅供参考）: Initialize the middleware.
    - 分支数 0，函数体节点数 46
    - 调用: __init__, super, Paths, get_paths
  #### `m` `_get_thread_paths(self, thread_id: str, user_id: str | None) -> dict[str, str]`  L52
    - _文档首行_（仅供参考）: Get the paths for a thread's data directories.
    - 分支数 0，函数体节点数 75；return: {'workspace_path': str(self._paths.sandbox_work_dir(thread_id, user_id=user_id)), 'uploads_path': str(self._paths.sandbox_uploads_dir(thread_id, user_id=user_id)), 'outputs_path': str(self._paths.sandbox_outputs_dir(thread_id, user_id=user_id))}
    - 调用: str, sandbox_work_dir, sandbox_uploads_dir, sandbox_outputs_dir
  #### `m` `_create_thread_directories(self, thread_id: str, user_id: str | None) -> dict[str, str]`  L68
    - _文档首行_（仅供参考）: Create the thread data directories.
    - 分支数 0，函数体节点数 49；return: self._get_thread_paths(thread_id, user_id=user_id)
    - 调用: ensure_thread_dirs, _get_thread_paths
  #### `m` `before_agent(self, state: ThreadDataMiddlewareState, runtime: Runtime) -> dict | None`    @override  L82
    - 分支数 4，函数体节点数 220；raise: ValueError('Thread ID is required in runtime context or config.configurable')；return: {'thread_data': {**paths}, 'messages': messages}
    - 调用: get, get_config, ValueError, get_effective_user_id, _get_thread_paths, _create_thread_directories, debug, list, isinstance, HumanMessage, isoformat, now

## 文件内调用关系
- `ThreadDataMiddleware.__init__` -> __init__
- `ThreadDataMiddleware._create_thread_directories` -> _get_thread_paths
- `ThreadDataMiddleware.before_agent` -> _get_thread_paths, _create_thread_directories

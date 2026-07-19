# `backend/packages/harness/deerflow/sandbox/middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/middleware.py`  ·  行数: 219

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, logging
- `collections.abc` -> Awaitable, Callable
- `dataclasses` -> dc_replace
- `typing` -> NotRequired, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> ToolMessage
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.runtime` -> Runtime
- `langgraph.types` -> Command
- `deerflow.agents.thread_state` -> SandboxStateField, ThreadDataState
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.sandbox` -> get_sandbox_provider

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `SandboxMiddlewareState`  L21
- 继承: AgentState
- _文档首行_: Compatible with the `ThreadState` schema.
- 类/实例变量:
  - `sandbox` = <annotated>
  - `thread_data` = <annotated>

### 类 `SandboxMiddleware`  L28
- 继承: AgentMiddleware[SandboxMiddlewareState]
- _文档首行_: Create a sandbox environment and assign it to an agent.
- 类/实例变量:
  - `state_schema` = SandboxMiddlewareState
- 方法:
  #### `st` `_read_sandbox_id_from_state(state: object) -> str | None`    @staticmethod  L152
    - 分支数 2，函数体节点数 66；return: None, sandbox_id if isinstance(sandbox_id, str) else None
    - 调用: isinstance, get
  #### `st` `_attach_sandbox_update(result: ToolMessage | Command, sandbox_id: str) -> ToolMessage | Command`    @staticmethod  L162
    - _文档首行_（仅供参考）: Wrap or merge ``result`` so that ``sandbox.sandbox_id`` is persisted.
    - 分支数 2，函数体节点数 87；return: Command(update={**sandbox_update, 'messages': [result]}), dc_replace(result, update=merged_update), result
    - 调用: isinstance, Command, dc_replace
  #### `st` `_read_sandbox_id_from_request(request: ToolCallRequest) -> str | None`    @staticmethod  L183
    - _文档首行_（仅供参考）: Read sandbox_id from runtime.state (where ensure_sandbox_initialized writes).
    - 分支数 1，函数体节点数 48；return: None, SandboxMiddleware._read_sandbox_id_from_state(runtime.state)
    - 调用: _read_sandbox_id_from_state
  #### `m` `__init__(self, lazy_init: bool)`  L41
    - _文档首行_（仅供参考）: Initialize sandbox middleware.
    - 分支数 0，函数体节点数 23
    - 调用: __init__, super
  #### `m` `_acquire_sandbox(self, thread_id: str, *, user_id: str) -> str`  L52
    - 分支数 0，函数体节点数 44；return: sandbox_id
    - 调用: get_sandbox_provider, acquire, info
  #### `m` `before_agent(self, state: SandboxMiddlewareState, runtime: Runtime) -> dict | None`    @override  L68
    - 分支数 3，函数体节点数 128；return: super().before_agent(state, runtime), {'sandbox': {'sandbox_id': sandbox_id}}
    - 调用: before_agent, super, get, _acquire_sandbox, resolve_runtime_user_id, info
  #### `m` `after_agent(self, state: SandboxMiddlewareState, runtime: Runtime) -> dict | None`    @override  L101
    - 分支数 2，函数体节点数 121；return: None, super().after_agent(state, runtime)
    - 调用: get, info, release, get_sandbox_provider, after_agent, super
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L191
    - 分支数 2，函数体节点数 87；return: result, self._attach_sandbox_update(result, curr_sandbox_id)
    - 调用: _read_sandbox_id_from_request, handler, _attach_sandbox_update
  #### `⏵m` `async _acquire_sandbox_async(self, thread_id: str, *, user_id: str) -> str`  L58
    - 分支数 0，函数体节点数 45；return: sandbox_id
    - 调用: get_sandbox_provider, acquire_async, info
  #### `⏵m` `async _release_sandbox_async(self, sandbox_id: str) -> None`  L64
    - 分支数 0，函数体节点数 21
    - 调用: to_thread, get_sandbox_provider
  #### `⏵m` `async abefore_agent(self, state: SandboxMiddlewareState, runtime: Runtime) -> dict | None`    @override  L84
    - 分支数 3，函数体节点数 132；return: await super().abefore_agent(state, runtime), {'sandbox': {'sandbox_id': sandbox_id}}
    - 调用: abefore_agent, super, get, _acquire_sandbox_async, resolve_runtime_user_id, info
  #### `⏵m` `async aafter_agent(self, state: SandboxMiddlewareState, runtime: Runtime) -> dict | None`    @override  L119
    - 分支数 2，函数体节点数 122；return: None, await super().aafter_agent(state, runtime)
    - 调用: get, info, _release_sandbox_async, aafter_agent, super
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L206
    - 分支数 2，函数体节点数 92；return: result, self._attach_sandbox_update(result, curr_sandbox_id)
    - 调用: _read_sandbox_id_from_request, handler, _attach_sandbox_update

## 文件内调用关系
- `SandboxMiddleware.__init__` -> __init__
- `SandboxMiddleware.before_agent` -> before_agent, _acquire_sandbox
- `SandboxMiddleware.abefore_agent` -> abefore_agent, _acquire_sandbox_async
- `SandboxMiddleware.after_agent` -> after_agent
- `SandboxMiddleware.aafter_agent` -> _release_sandbox_async, aafter_agent
- `SandboxMiddleware._read_sandbox_id_from_request` -> _read_sandbox_id_from_state
- `SandboxMiddleware.wrap_tool_call` -> _read_sandbox_id_from_request, _attach_sandbox_update
- `SandboxMiddleware.awrap_tool_call` -> _read_sandbox_id_from_request, _attach_sandbox_update

# `backend/packages/harness/deerflow/mcp/session_pool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/mcp/session_pool.py`  ·  行数: 461

**模块文档首行**（仅供参考）: Persistent MCP session pool for stateful tool calls.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 3 个

## 依赖（import）
- 模块: asyncio, logging, threading
- `__future__` -> annotations
- `collections` -> OrderedDict
- `typing` -> Any
- `mcp` -> ClientSession

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_pool` = None
- `_pool_lock` = threading.Lock()

## 函数
#### `ƒ` `get_session_pool() -> MCPSessionPool`  L442
  - _文档首行_（仅供参考）: Return the global session-pool singleton.
  - 分支数 2，函数体节点数 26；return: _pool
  - 调用: MCPSessionPool

#### `ƒ` `reset_session_pool() -> None`  L456
  - _文档首行_（仅供参考）: Reset the singleton (used in tests and the MCP cache reset path).
  - 分支数 1，函数体节点数 14

## 类
### 类 `MCPSessionPool`  L47
- _文档首行_: Manages persistent MCP sessions scoped by ``(server_name, scope_key)``.
- 类/实例变量:
  - `MAX_SESSIONS` = 256
  - `SESSION_CLOSE_TIMEOUT` = 5.0
- 方法:
  #### `st` `_signal_close(loop: asyncio.AbstractEventLoop, close_evt: asyncio.Event) -> None`    @staticmethod  L270
    - _文档首行_（仅供参考）: Ask an owner task to shut down without waiting.
    - 分支数 2，函数体节点数 39；return: None
    - 调用: is_closed, call_soon_threadsafe
  #### `m` `__init__(self) -> None`  L53
    - 分支数 0，函数体节点数 114
    - 调用: OrderedDict, Lock
  #### `m` `close_all_sync(self) -> None`  L378
    - _文档首行_（仅供参考）: Close all sessions on their owning event loops (synchronous).
    - 分支数 8，函数体节点数 233
    - 调用: list, values, clear, get_running_loop, is_closed, set, cancel, is_running, run_coroutine_threadsafe, _shutdown, result, run_until_complete, debug
  #### `⏵m` `async _run_session(self, connection: dict[str, Any], ready: asyncio.Future[ClientSession], close_evt: asyncio.Event) -> None`  L84
    - _文档首行_（仅供参考）: Own a single MCP session for its entire lifetime.
    - 分支数 6，函数体节点数 144；return: None
    - 调用: create_session, __aenter__, done, set_exception, initialize, set_result, wait, __aexit__, warning
  #### `⏵m` `async get_session(self, server_name: str, scope_key: str, connection: dict[str, Any]) -> ClientSession`  L126
    - _文档首行_（仅供参考）: Get or create a persistent MCP session.
    - 分支数 18，函数体节点数 746；raise: bare raise, asyncio.CancelledError('MCP session pool was closed while the session was being created')；return: session, await asyncio.shield(join)
    - 调用: get_running_loop, is_closed, move_to_end, pop, append, get, create_future, Event, create_task, _run_session, len, next, iter, items, _shutdown, _shutdown_entry, _signal_close, shield, done, cancelled（+6）
  #### `⏵m` `async _shutdown(self, close_evt: asyncio.Event, task: asyncio.Task[Any], cancel: bool) -> None`  L284
    - _文档首行_（仅供参考）: Signal an owner task and wait for it to finish (runs on its loop).
    - 分支数 2，函数体节点数 62
    - 调用: set, cancel, debug
  #### `⏵m` `async _shutdown_entry(self, loop: asyncio.AbstractEventLoop, task: asyncio.Task[Any], close_evt: asyncio.Event, cancel: bool) -> None`  L305
    - _文档首行_（仅供参考）: Shut down one entry, routing the close to its owning loop.
    - 分支数 6，函数体节点数 148；return: None
    - 调用: is_closed, get_running_loop, _shutdown, is_running, run_coroutine_threadsafe, wrap_future, warning, _signal_close, call_soon_threadsafe
  #### `⏵m` `async close_scope(self, scope_key: str) -> None`  L342
    - _文档首行_（仅供参考）: Close all sessions for a given scope (e.g. thread_id).
    - 分支数 3，函数体节点数 149
    - 调用: pop, _shutdown_entry
  #### `⏵m` `async close_server(self, server_name: str) -> None`  L354
    - _文档首行_（仅供参考）: Close all sessions for a given server.
    - 分支数 3，函数体节点数 149
    - 调用: pop, _shutdown_entry
  #### `⏵m` `async close_all(self) -> None`  L366
    - _文档首行_（仅供参考）: Close every managed session.
    - 分支数 3，函数体节点数 108
    - 调用: list, values, clear, _shutdown_entry

## 文件内调用关系
- `MCPSessionPool.get_session` -> _run_session, _shutdown, _shutdown_entry, _signal_close
- `MCPSessionPool._shutdown_entry` -> _shutdown, _signal_close
- `MCPSessionPool.close_scope` -> _shutdown_entry
- `MCPSessionPool.close_server` -> _shutdown_entry
- `MCPSessionPool.close_all` -> _shutdown_entry
- `MCPSessionPool.close_all_sync` -> _shutdown

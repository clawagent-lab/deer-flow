# `backend/packages/harness/deerflow/tui/persistence.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/persistence.py`  ·  行数: 112

**模块文档首行**（仅供参考）: Shared-persistence wiring so terminal sessions show up in the Web UI.

## 模块概览
- 函数 1 个，类 2 个，模块级常量 0 个

## 依赖（import）
- 模块: asyncio, threading
- `__future__` -> annotations
- `collections.abc` -> Awaitable
- `typing` -> Any
- `deerflow.runtime.user_context` -> DEFAULT_USER_ID

## 函数
#### `ƒ` `build_persistence() -> tuple[_LoopThread, ThreadMetaWriter]`  L91
  - _文档首行_（仅供参考）: Initialise the shared engine on a background loop and return a writer.
  - 分支数 2，函数体节点数 90；return: (loop, ThreadMetaWriter(loop, store))
  - 调用: _LoopThread, get_app_config, run, init_engine_from_config, get_session_factory, make_thread_store, ThreadMetaWriter
  - 子进程: run (L105)

## 类
### 类 `_LoopThread`  L28
- _文档首行_: A daemon thread running a single asyncio event loop for DB work.
- 方法:
  #### `m` `__init__(self) -> None`  L31
    - 分支数 0，函数体节点数 41
    - 调用: new_event_loop, Thread, start
  #### `m` `_run(self) -> None`  L36
    - 分支数 0，函数体节点数 22
    - 调用: set_event_loop, run_forever
  #### `m` `run(self, coro: Awaitable[Any], *, timeout: float) -> Any`  L40
    - 分支数 0，函数体节点数 38；return: future.result(timeout)
    - 调用: run_coroutine_threadsafe, result
  #### `m` `close(self) -> None`  L44
    - 分支数 0，函数体节点数 18
    - 调用: call_soon_threadsafe

### 类 `ThreadMetaWriter`  L48
- _文档首行_: Writes/updates ``threads_meta`` rows for the local default user.
- 方法:
  #### `prop` `enabled(self) -> bool`    @property  L61
    - 分支数 0，函数体节点数 15；return: self._store is not None
  #### `m` `__init__(self, loop: _LoopThread, store: Any) -> None`  L55
    - 分支数 0，函数体节点数 31
  #### `m` `ensure_created(self, thread_id: str, *, assistant_id: str | None, metadata: dict | None) -> None`  L64
    - 分支数 2，函数体节点数 59；return: None
    - 调用: run, _ensure_created
  - 子进程: run (L68)
  #### `m` `set_title(self, thread_id: str, title: str) -> None`  L82
    - 分支数 2，函数体节点数 57；return: None
    - 调用: run, update_display_name
  - 子进程: run (L86)
  #### `⏵m` `async _ensure_created(self, thread_id: str, assistant_id: str | None, metadata: dict | None) -> None`  L72
    - 分支数 1，函数体节点数 70
    - 调用: get, create

## 文件内调用关系
- `build_persistence` -> run
- `ThreadMetaWriter.ensure_created` -> run, _ensure_created
- `ThreadMetaWriter.set_title` -> run

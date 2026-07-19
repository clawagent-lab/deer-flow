# `backend/packages/harness/deerflow/tui/session.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/session.py`  ·  行数: 93

**模块文档首行**（仅供参考）: Embedded session wiring for the TUI.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> TYPE_CHECKING

## 函数
#### `ƒ` `open_session(persistence: bool) -> Session`  L73
  - _文档首行_（仅供参考）: Build an embedded session backed by the configured checkpointer.
  - 分支数 1，函数体节点数 66；return: Session(client=client), Session(client=client, writer=writer, _loop=loop)
  - 调用: get_checkpointer, DeerFlowClient, Session, build_persistence

## 类
### 类 `Session`  L22  @dataclass
- 类/实例变量:
  - `client` = <annotated>
  - `writer` = None
  - `_loop` = None
- 方法:
  #### `m` `resolve_thread(self, plan: LaunchPlan) -> str | None`  L27
    - _文档首行_（仅供参考）: Resolve the thread id to run against, honoring --resume / --continue.
    - 分支数 3，函数体节点数 66；return: self.resolve_ref(plan.thread_id), threads[0].get('thread_id'), None
    - 调用: resolve_ref, get, list_threads
  #### `m` `resolve_ref(self, ref: str) -> str`  L37
    - _文档首行_（仅供参考）: Resolve a thread reference (id or title) to a thread id.
    - 分支数 4，函数体节点数 91；return: ref, thread.get('thread_id') or ref
    - 调用: get, list_threads, any
  #### `m` `recent_threads(self, limit: int) -> list[dict]`  L55
    - 分支数 0，函数体节点数 30；return: self.client.list_threads(limit=limit).get('thread_list', [])
    - 调用: get, list_threads
  #### `m` `close(self) -> None`  L58
    - _文档首行_（仅供参考）: Stop the background DB loop and dispose the engine (best-effort).
    - 分支数 2，函数体节点数 48；return: None
    - 调用: run, close_engine, close
  - 子进程: run (L67)

## 文件内调用关系
- `Session.resolve_thread` -> resolve_ref
- `Session.close` -> close

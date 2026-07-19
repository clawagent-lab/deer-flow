# `backend/packages/harness/deerflow/runtime/events/store/memory.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/events/store/memory.py`  ·  行数: 175

**模块文档首行**（仅供参考）: In-memory RunEventStore. Used when run_events.backend=memory (default) and in tests.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: bisect
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `deerflow.runtime.events.store.base` -> RunEventStore
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel

## 类
### 类 `MemoryRunEventStore`  L16
- 继承: RunEventStore
- 方法:
  #### `m` `__init__(self) -> None`  L17
    - 分支数 0，函数体节点数 116
  #### `m` `_next_seq(self, thread_id: str) -> int`  L33
    - 分支数 0，函数体节点数 43；return: next_val
    - 调用: get
  #### `m` `_put_one(self, *, thread_id: str, run_id: str, event_type: str, category: str, content: str | dict, metadata: dict | None, created_at: str | None) -> dict`  L39
    - 分支数 1，函数体节点数 181；return: record
    - 调用: _next_seq, isoformat, now, append, setdefault
  #### `⏵m` `async put(self, *, thread_id, run_id, event_type, category, content, metadata, created_at)`  L68
    - 分支数 0，函数体节点数 40；return: self._put_one(thread_id=thread_id, run_id=run_id, event_type=event_type, category=category, content=content, metadata=metadata, created_at=created_at)
    - 调用: _put_one
  #### `⏵m` `async put_batch(self, events)`  L89
    - 分支数 1，函数体节点数 36；return: results
    - 调用: _put_one, append
  #### `⏵m` `async list_messages(self, thread_id, *, limit, before_seq, after_seq, user_id: str | None | _AutoSentinel)`  L96
    - 分支数 2，函数体节点数 132；return: messages[max(0, hi - limit):hi], messages[lo:lo + limit], messages[-limit:]
    - 调用: get, bisect_left, max, bisect_right
  #### `⏵m` `async list_events(self, thread_id, run_id, *, event_types, task_id, limit, after_seq)`  L113
    - 分支数 3，函数体节点数 129；return: run_events[:limit]
    - 调用: get
  #### `⏵m` `async list_messages_by_run(self, thread_id, run_id, *, limit, before_seq, after_seq)`  L125
    - 分支数 1，函数体节点数 127；return: window[:limit], window[-limit:]
    - 调用: get, bisect_right, len, bisect_left
  #### `⏵m` `async get_last_visible_ai_seq_by_run(self, thread_id, run_ids, *, user_id: str | None | _AutoSentinel)`  L140
    - 分支数 3，函数体节点数 131；return: result
    - 调用: get, reversed, str, startswith
  #### `⏵m` `async count_messages(self, thread_id)`  L151
    - 分支数 0，函数体节点数 19；return: len(self._messages.get(thread_id, []))
    - 调用: len, get
  #### `⏵m` `async delete_by_thread(self, thread_id)`  L154
    - 分支数 0，函数体节点数 68；return: len(events)
    - 调用: pop, len
  #### `⏵m` `async delete_by_run(self, thread_id, run_id)`  L162
    - 分支数 1，函数体节点数 134；return: 0, removed
    - 调用: get, len, pop

## 文件内调用关系
- `MemoryRunEventStore._put_one` -> _next_seq
- `MemoryRunEventStore.put` -> _put_one
- `MemoryRunEventStore.put_batch` -> _put_one

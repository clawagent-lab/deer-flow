# `backend/packages/harness/deerflow/runtime/events/store/db.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/events/store/db.py`  ·  行数: 382

**模块文档首行**（仅供参考）: SQLAlchemy-backed RunEventStore implementation.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, json, logging
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any
- `sqlalchemy` -> delete, func, select, text
- `sqlalchemy.ext.asyncio` -> AsyncSession, async_sessionmaker
- `deerflow.persistence.models.run_event` -> RunEventRow
- `deerflow.runtime.events.store.base` -> RunEventStore
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel, get_current_user, resolve_user_id
- `deerflow.utils.time` -> coerce_iso

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `DbRunEventStore`  L26
- 继承: RunEventStore
- 方法:
  #### `st` `_row_to_dict(row: RunEventRow) -> dict`    @staticmethod  L46
    - 分支数 3，函数体节点数 149；return: d
    - 调用: to_dict, pop, get, isinstance, coerce_iso, loads, debug
  #### `st` `_content_to_db(content: Any, metadata: dict | None) -> tuple[str, dict]`    @staticmethod  L78
    - 分支数 2，函数体节点数 91；return: (content, metadata), (db_content, metadata)
    - 调用: isinstance, dumps
  #### `st` `_user_id_from_context() -> str | None`    @staticmethod  L90
    - _文档首行_（仅供参考）: Soft read of user_id from contextvar for write paths.
    - 分支数 0，函数体节点数 32；return: str(user.id) if user is not None else None
    - 调用: get_current_user, str
  #### `m` `__init__(self, session_factory: async_sessionmaker[AsyncSession], *, max_trace_content: int)`  L27
    - 分支数 0，函数体节点数 46
  #### `m` `_get_write_lock(self, thread_id: str) -> asyncio.Lock`  L37
    - _文档首行_（仅供参考）: Return (creating if needed) the per-thread seq-assignment lock.
    - 分支数 1，函数体节点数 52；return: lock
    - 调用: get, Lock
  #### `m` `_truncate_trace(self, category: str, content: Any, metadata: dict | None) -> tuple[Any, dict]`  L67
    - 分支数 2，函数体节点数 122；return: (content, metadata or {})
    - 调用: isinstance, dumps, encode, len, decode
  #### `⏵m` `async _max_seq_for_thread(session: AsyncSession, thread_id: str) -> int | None`    @staticmethod  L108
    - _文档首行_（仅供参考）: Return the current max seq while serializing writers per thread.
    - 分支数 1，函数体节点数 109；return: await session.scalar(stmt), await session.scalar(stmt.with_for_update())
    - 调用: where, select, max, get_bind, execute, text, scalar, with_for_update
  #### `⏵m` `async put(self, *, thread_id, run_id, event_type, category, content, metadata, created_at)`  L129
    - _文档首行_（仅供参考）: Write a single event — low-frequency path only.
    - 分支数 3，函数体节点数 170；return: self._row_to_dict(row)
    - 调用: _truncate_trace, _content_to_db, _user_id_from_context, _get_write_lock, _sf, begin, _max_seq_for_thread, RunEventRow, fromisoformat, now, add, _row_to_dict
  #### `⏵m` `async put_batch(self, events)`  L160
    - 分支数 6，函数体节点数 287；raise: ValueError(f'put_batch requires all events to belong to the same thread; got {thread_ids!r}')；return: [], [self._row_to_dict(r) for r in rows]
    - 调用: len, ValueError, _user_id_from_context, _get_write_lock, _sf, begin, _max_seq_for_thread, get, _truncate_trace, _content_to_db, RunEventRow, fromisoformat, now, add, append, _row_to_dict
  #### `⏵m` `async list_messages(self, thread_id, *, limit, before_seq, after_seq, user_id: str | None | _AutoSentinel)`  L197
    - 分支数 6，函数体节点数 255；return: [self._row_to_dict(r) for r in result.scalars()], [self._row_to_dict(r) for r in reversed(rows)]
    - 调用: resolve_user_id, where, select, limit, order_by, asc, _sf, execute, _row_to_dict, scalars, desc, list, reversed
  #### `⏵m` `async list_events(self, thread_id, run_id, *, event_types, task_id, limit, after_seq, user_id: str | None | _AutoSentinel)`  L229
    - 分支数 5，函数体节点数 211；return: [self._row_to_dict(r) for r in result.scalars()]
    - 调用: resolve_user_id, where, select, in_, as_string, limit, order_by, asc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async list_messages_by_run(self, thread_id, run_id, *, limit, before_seq, after_seq, user_id: str | None | _AutoSentinel)`  L260
    - 分支数 6，函数体节点数 264；return: [self._row_to_dict(r) for r in result.scalars()], [self._row_to_dict(r) for r in reversed(rows)]
    - 调用: resolve_user_id, where, select, limit, order_by, asc, _sf, execute, _row_to_dict, scalars, desc, list, reversed
  #### `⏵m` `async get_last_visible_ai_seq_by_run(self, thread_id, run_ids, *, user_id: str | None | _AutoSentinel)`  L295
    - 分支数 3，函数体节点数 189；return: {}, {run_id: seq for run_id, seq in result if isinstance(seq, int)}
    - 调用: resolve_user_id, as_string, group_by, where, select, max, in_, like, coalesce, _sf, execute, isinstance
  #### `⏵m` `async count_messages(self, thread_id, *, user_id: str | None | _AutoSentinel)`  L325
    - 分支数 2，函数体节点数 103；return: await session.scalar(stmt) or 0
    - 调用: resolve_user_id, where, select_from, select, count, _sf, scalar
  #### `⏵m` `async delete_by_thread(self, thread_id, *, user_id: str | None | _AutoSentinel)`  L338
    - 分支数 4，函数体节点数 178；return: count
    - 调用: resolve_user_id, _sf, append, where, select_from, select, count, scalar, execute, delete, commit, get, locked, pop
  #### `⏵m` `async delete_by_run(self, thread_id, run_id, *, user_id: str | None | _AutoSentinel)`  L364
    - 分支数 3，函数体节点数 149；return: count
    - 调用: resolve_user_id, _sf, append, where, select_from, select, count, scalar, execute, delete, commit

## 文件内调用关系
- `DbRunEventStore.put` -> _truncate_trace, _content_to_db, _user_id_from_context, _get_write_lock, _max_seq_for_thread, _row_to_dict
- `DbRunEventStore.put_batch` -> _user_id_from_context, _get_write_lock, _max_seq_for_thread, _truncate_trace, _content_to_db, _row_to_dict
- `DbRunEventStore.list_messages` -> _row_to_dict
- `DbRunEventStore.list_events` -> _row_to_dict
- `DbRunEventStore.list_messages_by_run` -> _row_to_dict

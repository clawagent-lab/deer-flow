# `backend/packages/harness/deerflow/runtime/events/store/jsonl.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/events/store/jsonl.py`  ·  行数: 281

**模块文档首行**（仅供参考）: JSONL file-backed RunEventStore implementation.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, json, logging, re
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `pathlib` -> Path
- `typing` -> Any
- `deerflow.runtime.events.store.base` -> RunEventStore
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SAFE_ID_PATTERN` = re.compile('^[A-Za-z0-9_\\-]+$')

## 类
### 类 `JsonlRunEventStore`  L41
- 继承: RunEventStore
- 方法:
  #### `st` `_validate_id(value: str, label: str) -> str`    @staticmethod  L52
    - _文档首行_（仅供参考）: Validate that an ID is safe for use in filesystem paths.
    - 分支数 1，函数体节点数 46；raise: ValueError(f'Invalid {label}: must be alphanumeric/dash/underscore, got {value!r}')；return: value
    - 调用: match, ValueError
  #### `m` `__init__(self, base_dir: str | Path | None)`  L42
    - 分支数 0，函数体节点数 65
    - 调用: Path
  #### `m` `_get_write_lock(self, thread_id: str) -> asyncio.Lock`  L48
    - 分支数 0，函数体节点数 25；return: self._write_locks.setdefault(thread_id, asyncio.Lock())
    - 调用: setdefault, Lock
  #### `m` `_thread_dir(self, thread_id: str) -> Path`  L58
    - 分支数 0，函数体节点数 32；return: self._base_dir / 'threads' / thread_id / 'runs'
    - 调用: _validate_id
  #### `m` `_run_file(self, thread_id: str, run_id: str) -> Path`  L62
    - 分支数 0，函数体节点数 35；return: self._thread_dir(thread_id) / f'{run_id}.jsonl'
    - 调用: _validate_id, _thread_dir
  #### `m` `_next_seq(self, thread_id: str) -> int`  L66
    - 分支数 0，函数体节点数 39；return: self._seq_counters[thread_id]
    - 调用: get
  #### `m` `_compute_max_seq(self, thread_id: str) -> int`  L70
    - _文档首行_（仅供参考）: Scan all run files for a thread and return the current max seq (blocking I/O).
    - 分支数 4，函数体节点数 98；return: max_seq
    - 调用: _thread_dir, exists, glob, splitlines, strip, read_text, loads, max, get, debug
  - 文件IO: exists (L74), glob (L75), read_text (L76)
  #### `m` `_write_record(self, record: dict) -> None`  L91
    - 分支数 1，函数体节点数 70
    - 调用: _run_file, mkdir, open, write, dumps
  - 文件IO: mkdir (L93), open (L94), write (L95)
  #### `m` `_read_thread_events(self, thread_id: str) -> list[dict]`  L97
    - _文档首行_（仅供参考）: Read all events for a thread, sorted by seq (blocking I/O).
    - 分支数 5，函数体节点数 122；return: events
    - 调用: _thread_dir, exists, sorted, glob, splitlines, strip, read_text, append, loads, debug, sort, get
  - 文件IO: exists (L101), glob (L103), read_text (L104)
  #### `m` `_read_run_events(self, thread_id: str, run_id: str) -> list[dict]`  L114
    - _文档首行_（仅供参考）: Read events for a specific run file (blocking I/O).
    - 分支数 4，函数体节点数 115；return: [], events
    - 调用: _run_file, exists, splitlines, strip, read_text, append, loads, debug, sort, get
  - 文件IO: exists (L117), read_text (L120)
  #### `m` `_delete_thread_files(self, thread_id: str) -> None`  L130
    - 分支数 2，函数体节点数 38
    - 调用: _thread_dir, exists, glob, unlink
  - 文件IO: exists (L132), glob (L133), unlink (L134)
  #### `m` `_delete_run_file(self, thread_id: str, run_id: str) -> None`  L136
    - 分支数 1，函数体节点数 34
    - 调用: _run_file, exists, unlink
  - 文件IO: exists (L138), unlink (L139)
  #### `m` `_append_records(self, path: Path, records: list[dict[str, Any]]) -> None`  L204
    - 分支数 1，函数体节点数 82
    - 调用: mkdir, join, dumps, open, write
  - 文件IO: mkdir (L205), open (L207), write (L208)
  #### `⏵m` `async _ensure_seq_loaded(self, thread_id: str) -> None`  L84
    - _文档首行_（仅供参考）: Load max seq from existing files into the in-memory counter (non-blocking).
    - 分支数 1，函数体节点数 45；return: None
    - 调用: to_thread
  #### `⏵m` `async put(self, *, thread_id, run_id, event_type, category, content, metadata, created_at)`  L141
    - 分支数 1，函数体节点数 100；return: record
    - 调用: _get_write_lock, _ensure_seq_loaded, _next_seq, isoformat, now, to_thread
  #### `⏵m` `async put_batch(self, events)`  L158
    - _文档首行_（仅供参考）: Persist a batch of events atomically per-thread.
    - 分支数 3，函数体节点数 118；return: [], results
    - 调用: append, setdefault, items, _write_batch_async, extend
  #### `⏵m` `async _write_batch_async(self, thread_id: str, batch: list[dict[str, Any]]) -> list[dict[str, Any]]`  L181
    - 分支数 2，函数体节点数 196；return: records
    - 调用: _get_write_lock, _ensure_seq_loaded, _next_seq, get, isoformat, now, append, _run_file, to_thread
  #### `⏵m` `async list_messages(self, thread_id, *, limit, before_seq, after_seq, user_id: str | None | _AutoSentinel)`  L210
    - 分支数 2，函数体节点数 137；return: messages[-limit:], messages[:limit]
    - 调用: to_thread, get
  #### `⏵m` `async list_events(self, thread_id, run_id, *, event_types, task_id, limit, after_seq)`  L223
    - 分支数 3，函数体节点数 127；return: events[:limit]
    - 调用: to_thread, get
  #### `⏵m` `async list_messages_by_run(self, thread_id, run_id, *, limit, before_seq, after_seq)`  L233
    - 分支数 3，函数体节点数 140；return: filtered[:limit], filtered[-limit:] if len(filtered) > limit else filtered
    - 调用: to_thread, get, len
  #### `⏵m` `async get_last_visible_ai_seq_by_run(self, thread_id, run_ids, *, user_id: str | None | _AutoSentinel)`  L245
    - 分支数 3，函数体节点数 139；return: result, await asyncio.to_thread(_scan)
    - 调用: reversed, _read_run_events, str, get, startswith, to_thread
  #### `⏵m` `async count_messages(self, thread_id)`  L258
    - 分支数 0，函数体节点数 39；return: sum((1 for e in all_events if e.get('category') == 'message'))
    - 调用: to_thread, sum, get
  #### `⏵m` `async delete_by_thread(self, thread_id)`  L262
    - 分支数 1，函数体节点数 74；return: count
    - 调用: _get_write_lock, to_thread, len, pop
  #### `⏵m` `async delete_by_run(self, thread_id, run_id)`  L275
    - 分支数 1，函数体节点数 57；return: count
    - 调用: _get_write_lock, to_thread, len

## 文件内调用关系
- `JsonlRunEventStore._thread_dir` -> _validate_id
- `JsonlRunEventStore._run_file` -> _validate_id, _thread_dir
- `JsonlRunEventStore._compute_max_seq` -> _thread_dir
- `JsonlRunEventStore._write_record` -> _run_file
- `JsonlRunEventStore._read_thread_events` -> _thread_dir
- `JsonlRunEventStore._read_run_events` -> _run_file
- `JsonlRunEventStore._delete_thread_files` -> _thread_dir
- `JsonlRunEventStore._delete_run_file` -> _run_file
- `JsonlRunEventStore.put` -> _get_write_lock, _ensure_seq_loaded, _next_seq
- `JsonlRunEventStore.put_batch` -> _write_batch_async
- `JsonlRunEventStore._write_batch_async` -> _get_write_lock, _ensure_seq_loaded, _next_seq, _run_file
- `JsonlRunEventStore.get_last_visible_ai_seq_by_run` -> _read_run_events
- `JsonlRunEventStore.delete_by_thread` -> _get_write_lock
- `JsonlRunEventStore.delete_by_run` -> _get_write_lock

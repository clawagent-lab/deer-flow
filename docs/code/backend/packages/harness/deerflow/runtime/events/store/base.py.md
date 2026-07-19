# `backend/packages/harness/deerflow/runtime/events/store/base.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/events/store/base.py`  ·  行数: 136

**模块文档首行**（仅供参考）: Abstract interface for run event storage.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: abc
- `__future__` -> annotations
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel

## 类
### 类 `RunEventStore`  L19
- 继承: abc.ABC
- _文档首行_: Run event stream storage interface.
- 方法:
  #### `⏵m` `async put(self, *, thread_id: str, run_id: str, event_type: str, category: str, content: str | dict, metadata: dict | None, created_at: str | None) -> dict`    @abc.abstractmethod  L31
    - _文档首行_（仅供参考）: Write an event, auto-assign seq, return the complete record.
    - 分支数 0，函数体节点数 45
  #### `⏵m` `async put_batch(self, events: list[dict]) -> list[dict]`    @abc.abstractmethod  L45
    - _文档首行_（仅供参考）: Batch-write events. Used by RunJournal flush buffer.
    - 分支数 0，函数体节点数 22
  #### `⏵m` `async list_messages(self, thread_id: str, *, limit: int, before_seq: int | None, after_seq: int | None, user_id: str | None | _AutoSentinel) -> list[dict]`    @abc.abstractmethod  L53
    - _文档首行_（仅供参考）: Return displayable messages (category=message) for a thread, ordered by seq ascending.
    - 分支数 0，函数体节点数 48
  #### `⏵m` `async list_events(self, thread_id: str, run_id: str, *, event_types: list[str] | None, task_id: str | None, limit: int, after_seq: int | None) -> list[dict]`    @abc.abstractmethod  L74
    - _文档首行_（仅供参考）: Return the full event stream for a run, ordered by seq ascending.
    - 分支数 0，函数体节点数 50
  #### `⏵m` `async list_messages_by_run(self, thread_id: str, run_id: str, *, limit: int, before_seq: int | None, after_seq: int | None) -> list[dict]`    @abc.abstractmethod  L94
    - _文档首行_（仅供参考）: Return displayable messages (category=message) for a specific run, ordered by seq ascending.
    - 分支数 0，函数体节点数 39
  #### `⏵m` `async get_last_visible_ai_seq_by_run(self, thread_id: str, run_ids: set[str], *, user_id: str | None | _AutoSentinel) -> dict[str, int]`    @abc.abstractmethod  L112
    - _文档首行_（仅供参考）: Return each run's last non-middleware AI message sequence.
    - 分支数 0，函数体节点数 41
  #### `⏵m` `async count_messages(self, thread_id: str) -> int`    @abc.abstractmethod  L126
    - _文档首行_（仅供参考）: Count displayable messages (category=message) in a thread.
    - 分支数 0，函数体节点数 14
  #### `⏵m` `async delete_by_thread(self, thread_id: str) -> int`    @abc.abstractmethod  L130
    - _文档首行_（仅供参考）: Delete all events for a thread. Return the number of deleted events.
    - 分支数 0，函数体节点数 14
  #### `⏵m` `async delete_by_run(self, thread_id: str, run_id: str) -> int`    @abc.abstractmethod  L134
    - _文档首行_（仅供参考）: Delete all events for a specific run. Return the number of deleted events.
    - 分支数 0，函数体节点数 17

## 文件内调用关系
_无文件内调用_

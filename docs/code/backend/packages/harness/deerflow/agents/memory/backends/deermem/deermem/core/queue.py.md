# `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/queue.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/queue.py`  ·  行数: 375

**模块文档首行**（仅供参考）: Memory update queue with debounce mechanism.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: logging, threading, time
- `__future__` -> annotations
- `dataclasses` -> dataclass, field
- `datetime` -> UTC, datetime
- `typing` -> TYPE_CHECKING, Any
- `..config` -> DeerMemConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `ConversationContext`  L21  @dataclass
- _文档首行_: Context for a conversation to be processed for memory update.
- 类/实例变量:
  - `thread_id` = <annotated>
  - `messages` = <annotated>
  - `timestamp` = field(default_factory=lambda: datetime.now(UTC))
  - `agent_name` = None
  - `user_id` = None
  - `trace_id` = None
  - `correction_detected` = False
  - `reinforcement_detected` = False

### 类 `MemoryUpdateQueue`  L34
- _文档首行_: Queue for memory updates with debounce mechanism.
- 方法:
  #### `prop` `pending_count(self) -> int`    @property  L365
    - _文档首行_（仅供参考）: Get the number of pending updates.
    - 分支数 1，函数体节点数 23；return: len(self._queue)
    - 调用: len
  #### `prop` `is_processing(self) -> bool`    @property  L371
    - _文档首行_（仅供参考）: Check if the queue is currently being processed.
    - 分支数 1，函数体节点数 20；return: self._processing
  #### `st` `_queue_key(thread_id: str, user_id: str | None, agent_name: str | None) -> tuple[str, str | None, str | None]`    @staticmethod  L58
    - _文档首行_（仅供参考）: Return the debounce identity for a memory update target.
    - 分支数 0，函数体节点数 48；return: (thread_id, user_id, agent_name)
  #### `m` `__init__(self, config: DeerMemConfig, updater: MemoryUpdater)`  L42
    - _文档首行_（仅供参考）: Initialize the memory update queue with injected config + updater.
    - 分支数 0，函数体节点数 86
    - 调用: Lock
  #### `m` `add(self, thread_id: str, messages: list[Any], agent_name: str | None, user_id: str | None, trace_id: str | None, correction_detected: bool, reinforcement_detected: bool) -> None`  L66
    - _文档首行_（仅供参考）: Add a conversation to the update queue.
    - 分支数 1，函数体节点数 100
    - 调用: _enqueue_locked, _reset_timer, info, len
  #### `m` `add_nowait(self, thread_id: str, messages: list[Any], agent_name: str | None, user_id: str | None, trace_id: str | None, correction_detected: bool, reinforcement_detected: bool) -> None`  L104
    - _文档首行_（仅供参考）: Add a conversation and start processing immediately in the background.
    - 分支数 1，函数体节点数 101
    - 调用: _enqueue_locked, _schedule_timer, info, len
  #### `m` `_enqueue_locked(self, *, thread_id: str, messages: list[Any], agent_name: str | None, user_id: str | None, trace_id: str | None, correction_detected: bool, reinforcement_detected: bool) -> None`  L129
    - 分支数 0，函数体节点数 199
    - 调用: _queue_key, next, ConversationContext, append
  #### `m` `_reset_timer(self) -> None`  L160
    - _文档首行_（仅供参考）: Reset the debounce timer.
    - 分支数 0，函数体节点数 34
    - 调用: _schedule_timer, debug
  #### `m` `_schedule_timer(self, delay_seconds: float) -> None`  L167
    - _文档首行_（仅供参考）: Schedule queue processing after the provided delay.
    - 分支数 1，函数体节点数 57
    - 调用: cancel, Timer, start
  #### `m` `_process_queue(self, *, skip_inter_item_delay: bool) -> None`  L180
    - _文档首行_（仅供参考）: Process all queued conversation contexts.
    - 分支数 12，函数体节点数 312；return: None
    - 调用: current_thread, copy, clear, info, len, update_memory, warning, error, sleep, _schedule_timer
  #### `m` `flush(self, *, skip_inter_item_delay: bool) -> None`  L256
    - _文档首行_（仅供参考）: Force immediate processing of the queue.
    - 分支数 2，函数体节点数 47
    - 调用: cancel, _process_queue
  #### `m` `flush_sync(self, timeout: float) -> bool`  L273
    - _文档首行_（仅供参考）: Best-effort synchronous flush bounded by ``timeout`` seconds.
    - 分支数 5，函数体节点数 188；return: True, False, bool(success) and (not self.is_processing)
    - 调用: monotonic, join, max, Event, flush, exception, set, Thread, start, wait, bool
  #### `m` `flush_nowait(self) -> None`  L343
    - _文档首行_（仅供参考）: Start queue processing immediately in a background thread.
    - 分支数 1，函数体节点数 19
    - 调用: _schedule_timer
  #### `m` `clear(self) -> None`  L350
    - _文档首行_（仅供参考）: Clear the queue without processing.
    - 分支数 2，函数体节点数 60
    - 调用: cancel, clear

## 文件内调用关系
- `MemoryUpdateQueue.add` -> _enqueue_locked, _reset_timer
- `MemoryUpdateQueue.add_nowait` -> _enqueue_locked, _schedule_timer
- `MemoryUpdateQueue._enqueue_locked` -> _queue_key
- `MemoryUpdateQueue._reset_timer` -> _schedule_timer
- `MemoryUpdateQueue._process_queue` -> clear, _schedule_timer
- `MemoryUpdateQueue.flush` -> _process_queue
- `MemoryUpdateQueue.flush_sync` -> flush
- `MemoryUpdateQueue.flush_nowait` -> _schedule_timer
- `MemoryUpdateQueue.clear` -> clear

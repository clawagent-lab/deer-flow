# `backend/packages/harness/deerflow/runtime/stream_bridge/memory.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/stream_bridge/memory.py`  ·  行数: 161

**模块文档首行**（仅供参考）: In-memory stream bridge backed by an in-process event log.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, logging, time
- `__future__` -> annotations
- `collections.abc` -> AsyncIterator
- `dataclasses` -> dataclass, field
- `typing` -> Any
- `.base` -> END_SENTINEL, HEARTBEAT_SENTINEL, StreamBridge, StreamEvent

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `_RunStream`  L18  @dataclass
- 类/实例变量:
  - `events` = field(default_factory=list)
  - `condition` = field(default_factory=asyncio.Condition)
  - `ended` = False
  - `start_offset` = 0

### 类 `MemoryStreamBridge`  L25
- 继承: StreamBridge
- _文档首行_: Per-run in-memory event log implementation.
- 方法:
  #### `st` `_parse_event_seq(event_id: str) -> int | None`    @staticmethod  L52
    - _文档首行_（仅供参考）: Extract the per-run sequence number from a ``{ts}-{seq}`` event id.
    - 分支数 2，函数体节点数 48；return: None, int(seq_text)
    - 调用: rpartition, int
  #### `m` `__init__(self, *, queue_maxsize: int) -> None`  L32
    - 分支数 0，函数体节点数 47
  #### `m` `_get_or_create_stream(self, run_id: str) -> _RunStream`  L39
    - 分支数 1，函数体节点数 48；return: self._streams[run_id]
    - 调用: _RunStream
  #### `m` `_next_id(self, run_id: str) -> str`  L45
    - 分支数 0，函数体节点数 67；return: f'{ts}-{seq}'
    - 调用: get, int, time
  #### `m` `_resolve_start_offset(self, stream: _RunStream, last_event_id: str | None) -> int`  L67
    - 分支数 4，函数体节点数 113；return: stream.start_offset, stream.start_offset + local_index + 1
    - 调用: _parse_event_seq, len, warning
  #### `⏵m` `async stream_exists(self, run_id: str) -> bool`  L89
    - _文档首行_（仅供参考）: Return whether the in-process event log still has data for *run_id*.
    - 分支数 0，函数体节点数 19；return: run_id in self._streams
  #### `⏵m` `async publish(self, run_id: str, event: str, data: Any) -> None`  L95
    - 分支数 2，函数体节点数 115
    - 调用: _get_or_create_stream, StreamEvent, _next_id, append, len, notify_all
  #### `⏵m` `async publish_end(self, run_id: str) -> None`  L106
    - 分支数 1，函数体节点数 37
    - 调用: _get_or_create_stream, notify_all
  #### `⏵m` `async subscribe(self, run_id: str, *, last_event_id: str | None, heartbeat_interval: float) -> AsyncIterator[StreamEvent]`  L112
    - 分支数 8，函数体节点数 182；生成器（yield）；return: None
    - 调用: _get_or_create_stream, _resolve_start_offset, warning, len, wait_for, wait
  #### `⏵m` `async cleanup(self, run_id: str, *, delay: float) -> None`  L152
    - 分支数 1，函数体节点数 48
    - 调用: sleep, pop
  #### `⏵m` `async close(self) -> None`  L158
    - 分支数 0，函数体节点数 20
    - 调用: clear

## 文件内调用关系
- `MemoryStreamBridge._resolve_start_offset` -> _parse_event_seq
- `MemoryStreamBridge.publish` -> _get_or_create_stream, _next_id
- `MemoryStreamBridge.publish_end` -> _get_or_create_stream
- `MemoryStreamBridge.subscribe` -> _get_or_create_stream, _resolve_start_offset

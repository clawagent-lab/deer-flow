# `backend/packages/harness/deerflow/runtime/stream_bridge/base.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/stream_bridge/base.py`  ·  行数: 75

**模块文档首行**（仅供参考）: Abstract stream bridge protocol.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: abc
- `__future__` -> annotations
- `collections.abc` -> AsyncIterator
- `dataclasses` -> dataclass
- `typing` -> Any

## 模块级常量
- `HEARTBEAT_SENTINEL` = StreamEvent(id='', event='__heartbeat__', data=None)
- `END_SENTINEL` = StreamEvent(id='', event='__end__', data=None)

## 类
### 类 `StreamEvent`  L17  @dataclass(...)
- _文档首行_: Single stream event.
- 类/实例变量:
  - `id` = <annotated>
  - `event` = <annotated>
  - `data` = <annotated>

### 类 `StreamBridge`  L37
- 继承: abc.ABC
- 含 abstractmethod（抽象基类）
- _文档首行_: Abstract base for stream bridges.
- 类/实例变量:
  - `supports_cross_process` = False
- 方法:
  #### `m` `subscribe(self, run_id: str, *, last_event_id: str | None, heartbeat_interval: float) -> AsyncIterator[StreamEvent]`    @abc.abstractmethod  L51
    - _文档首行_（仅供参考）: Async iterator that yields events for *run_id* (consumer side).
    - 分支数 0，函数体节点数 29
  #### `⏵m` `async publish(self, run_id: str, event: str, data: Any) -> None`    @abc.abstractmethod  L43
    - _文档首行_（仅供参考）: Enqueue a single event for *run_id* (producer side).
    - 分支数 0，函数体节点数 19
  #### `⏵m` `async publish_end(self, run_id: str) -> None`    @abc.abstractmethod  L47
    - _文档首行_（仅供参考）: Signal that no more events will be produced for *run_id*.
    - 分支数 0，函数体节点数 13
  #### `⏵m` `async cleanup(self, run_id: str, *, delay: float) -> None`    @abc.abstractmethod  L66
    - _文档首行_（仅供参考）: Release resources associated with *run_id*.
    - 分支数 0，函数体节点数 17
  #### `⏵m` `async close(self) -> None`  L73
    - _文档首行_（仅供参考）: Release backend resources.  Default is a no-op.
    - 分支数 0，函数体节点数 6

## 文件内调用关系
_无文件内调用_

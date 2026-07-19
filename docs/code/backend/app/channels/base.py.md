# `backend/app/channels/base.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/base.py`  ·  行数: 200

**模块文档首行**（仅供参考）: Abstract base class for IM channels.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, logging
- `__future__` -> annotations
- `abc` -> ABC, abstractmethod
- `collections.abc` -> Awaitable, Callable
- `concurrent.futures` -> FutureCancelledError
- `typing` -> Any, TypeVar
- `app.channels.commands` -> extract_connect_code
- `app.channels.message_bus` -> InboundMessage, InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `T` = TypeVar('T')

## 类
### 类 `Channel`  L20
- 继承: ABC
- _文档首行_: Base class for all IM channel implementations.
- 方法:
  #### `prop` `is_running(self) -> bool`    @property  L38
    - 分支数 0，函数体节点数 12；return: self._running
  #### `prop` `supports_streaming(self) -> bool`    @property  L42
    - 分支数 0，函数体节点数 9；return: False
  #### `m` `__init__(self, name: str, bus: MessageBus, config: dict[str, Any]) -> None`  L30
    - 分支数 0，函数体节点数 61
    - 调用: get
  #### `m` `_log_future_error(self, fut: Any, name: str, msg_id: Any) -> None`  L109
    - _文档首行_（仅供参考）: Callback for concurrent futures scheduled from channel worker threads.
    - 分支数 2，函数体节点数 77；return: None
    - 调用: exception, error
  #### `m` `_pending_connect_code(self, text: str) -> str | None`  L122
    - _文档首行_（仅供参考）: Return the one-time bind code if *text* is a ``/connect <code>`` command
    - 分支数 1，函数体节点数 29；return: None, extract_connect_code(text)
    - 调用: extract_connect_code
  #### `m` `_make_inbound(self, chat_id: str, user_id: str, text: str, *, msg_type: InboundMessageType, thread_ts: str | None, files: list[dict[str, Any]] | None, metadata: dict[str, Any] | None) -> InboundMessage`  L135
    - _文档首行_（仅供参考）: Convenience factory for creating InboundMessage instances.
    - 分支数 0，函数体节点数 101；return: InboundMessage(channel_name=self.name, chat_id=chat_id, user_id=user_id, text=text, msg_type=msg_type, thread_ts=thread_ts, files=files or [], metadata=metadata or {})
    - 调用: InboundMessage
  #### `⏵m` `async start(self) -> None`    @abstractmethod  L48
    - _文档首行_（仅供参考）: Start listening for messages from the external platform.
    - 分支数 0，函数体节点数 8
  #### `⏵m` `async stop(self) -> None`    @abstractmethod  L52
    - _文档首行_（仅供参考）: Gracefully stop the channel.
    - 分支数 0，函数体节点数 8
  #### `⏵m` `async send(self, msg: OutboundMessage) -> None`    @abstractmethod  L58
    - _文档首行_（仅供参考）: Send a message back to the external platform.
    - 分支数 0，函数体节点数 11
  #### `⏵m` `async send_file(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L65
    - _文档首行_（仅供参考）: Upload a single file attachment to the platform.
    - 分支数 0，函数体节点数 15；return: False
  #### `⏵m` `async _send_with_retry(self, operation: Callable[[], Awaitable[T]], *, max_retries: int, log_prefix: str | None, operation_name: str) -> T`  L75
    - _文档首行_（仅供参考）: Run an outbound send operation with the shared channel retry policy.
    - 分支数 4，函数体节点数 170；raise: RuntimeError(f'{self.name} {operation_name} failed without an exception from any attempt'), last_exc；return: await operation()
    - 调用: range, operation, warning, sleep, error, RuntimeError
  #### `⏵m` `async _on_outbound(self, msg: OutboundMessage) -> None`  L158
    - _文档首行_（仅供参考）: Outbound callback registered with the bus.
    - 分支数 5，函数体节点数 104；return: None
    - 调用: send, exception, send_file, warning
  #### `⏵m` `async receive_file(self, msg: InboundMessage, thread_id: str, *, user_id: str | None) -> InboundMessage`  L181
    - _文档首行_（仅供参考）: Optionally process and materialize inbound file attachments for this channel.
    - 分支数 0，函数体节点数 26；return: msg

## 文件内调用关系
- `Channel._on_outbound` -> send, send_file

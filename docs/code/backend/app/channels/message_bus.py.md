# `backend/app/channels/message_bus.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/message_bus.py`  ·  行数: 191

**模块文档首行**（仅供参考）: MessageBus — async pub/sub hub that decouples channels from the agent dispatcher.

## 模块概览
- 函数 0 个，类 5 个，模块级常量 4 个

## 依赖（import）
- 模块: asyncio, logging, time
- `__future__` -> annotations
- `collections.abc` -> Callable, Coroutine
- `dataclasses` -> dataclass, field
- `enum` -> StrEnum
- `pathlib` -> Path
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `PENDING_CLARIFICATION_METADATA_KEY` = 'pending_clarification'
- `RESOLVED_FROM_PENDING_CLARIFICATION_METADATA_KEY` = 'resolved_from_pending_clarification'
- `OutboundCallback` = Callable[[OutboundMessage], Coroutine[Any, Any, None]]

## 类
### 类 `InboundMessageType`  L25
- 继承: StrEnum
- _文档首行_: Types of messages arriving from IM channels.
- 类/实例变量:
  - `CHAT` = 'chat'
  - `COMMAND` = 'command'

### 类 `InboundMessage`  L33  @dataclass
- _文档首行_: A message arriving from an IM channel toward the agent dispatcher.
- 类/实例变量:
  - `channel_name` = <annotated>
  - `chat_id` = <annotated>
  - `user_id` = <annotated>
  - `text` = <annotated>
  - `msg_type` = InboundMessageType.CHAT
  - `thread_ts` = None
  - `topic_id` = None
  - `connection_id` = None
  - `owner_user_id` = None
  - `workspace_id` = None
  - `files` = field(default_factory=list)
  - `metadata` = field(default_factory=dict)
  - `created_at` = field(default_factory=time.time)

### 类 `ResolvedAttachment`  L74  @dataclass
- _文档首行_: A file attachment resolved to a host filesystem path, ready for upload.
- 类/实例变量:
  - `virtual_path` = <annotated>
  - `actual_path` = <annotated>
  - `filename` = <annotated>
  - `mime_type` = <annotated>
  - `size` = <annotated>
  - `is_image` = <annotated>

### 类 `OutboundMessage`  L95  @dataclass
- _文档首行_: A message from the agent dispatcher back to a channel.
- 类/实例变量:
  - `channel_name` = <annotated>
  - `chat_id` = <annotated>
  - `thread_id` = <annotated>
  - `text` = <annotated>
  - `artifacts` = field(default_factory=list)
  - `attachments` = field(default_factory=list)
  - `is_final` = True
  - `thread_ts` = None
  - `connection_id` = None
  - `owner_user_id` = None
  - `metadata` = field(default_factory=dict)
  - `created_at` = field(default_factory=time.time)

### 类 `MessageBus`  L134
- _文档首行_: Async pub/sub hub connecting channels and the agent dispatcher.
- 方法:
  #### `prop` `inbound_queue(self) -> asyncio.Queue[InboundMessage]`    @property  L164
    - 分支数 0，函数体节点数 18；return: self._inbound_queue
  #### `m` `__init__(self) -> None`  L142
    - 分支数 0，函数体节点数 35
    - 调用: Queue
  #### `m` `subscribe_outbound(self, callback: OutboundCallback) -> None`  L169
    - _文档首行_（仅供参考）: Register an async callback for outbound messages.
    - 分支数 0，函数体节点数 19
    - 调用: append
  #### `m` `unsubscribe_outbound(self, callback: OutboundCallback) -> None`  L173
    - _文档首行_（仅供参考）: Remove a previously registered outbound callback.
    - 分支数 0，函数体节点数 30
  #### `⏵m` `async publish_inbound(self, msg: InboundMessage) -> None`  L148
    - _文档首行_（仅供参考）: Enqueue an inbound message from a channel.
    - 分支数 0，函数体节点数 48
    - 调用: put, info, qsize
  #### `⏵m` `async get_inbound(self) -> InboundMessage`  L159
    - _文档首行_（仅供参考）: Block until the next inbound message is available.
    - 分支数 0，函数体节点数 16；return: await self._inbound_queue.get()
    - 调用: get
  #### `⏵m` `async publish_outbound(self, msg: OutboundMessage) -> None`  L177
    - _文档首行_（仅供参考）: Dispatch an outbound message to all registered listeners.
    - 分支数 2，函数体节点数 67
    - 调用: info, len, callback, exception

## 文件内调用关系
_无文件内调用_

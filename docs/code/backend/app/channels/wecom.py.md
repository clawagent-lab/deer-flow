# `backend/app/channels/wecom.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/wecom.py`  ·  行数: 471

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, base64, hashlib, logging
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `typing` -> Any, cast
- `app.channels.base` -> Channel
- `app.channels.commands` -> is_known_channel_command
- `app.channels.connection_identity` -> attach_connection_identity
- `app.channels.message_bus` -> InboundMessage, InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `WeComChannel`  L24
- 继承: Channel
- 方法:
  #### `prop` `supports_streaming(self) -> bool`    @property  L36
    - 分支数 0，函数体节点数 9；return: True
  #### `m` `__init__(self, bus: MessageBus, config: dict[str, Any]) -> None`  L25
    - 分支数 0，函数体节点数 120
    - 调用: __init__, super
  #### `m` `_clear_ws_context(self, thread_ts: str | None) -> None`  L39
    - 分支数 1，函数体节点数 38；return: None
    - 调用: pop
  #### `m` `_on_ws_task_done(self, task: asyncio.Task) -> None`  L93
    - 分支数 2，函数体节点数 40；return: None
    - 调用: cancelled, exception, error
  #### `m` `_on_ws_error(self, error: Any) -> None`  L104
    - 分支数 0，函数体节点数 16
    - 调用: error
  #### `m` `_on_ws_disconnected(self, *args) -> None`  L107
    - 分支数 0，函数体节点数 32；可变参数（*args/**kwargs）
    - 调用: warning
  #### `⏵m` `async _send_ws_upload_command(self, req_id: str, body: dict[str, Any], cmd: str) -> dict[str, Any]`  L45
    - 分支数 2，函数体节点数 132；raise: RuntimeError('WeCom WebSocket client is not available'), RuntimeError('Installed wecom-aibot-python-sdk does not expose the WebSocket media upload API expected by DeerFlow. Use wecom-aibot-python-sdk==0.1.6 or update the adapter.')；return: await send_reply_async(req_id, body, cmd)
    - 调用: RuntimeError, getattr, callable, cast, send_reply_async
  - 反射: getattr (L49), getattr (L50)
  #### `⏵m` `async start(self) -> None`  L57
    - 分支数 3，函数体节点数 297；return: None
    - 调用: get, isinstance, error, WSClient, WSClientOptions, on, create_task, connect, add_done_callback, subscribe_outbound, info
  #### `⏵m` `async stop(self) -> None`  L111
    - 分支数 4，函数体节点数 93
    - 调用: unsubscribe_outbound, cancel, disconnect, clear, info
  #### `⏵m` `async send(self, msg: OutboundMessage, *, _max_retries: int) -> None`  L130
    - 分支数 1，函数体节点数 36；return: None
    - 调用: _send_ws, warning
  #### `⏵m` `async _on_outbound(self, msg: OutboundMessage) -> None`  L136
    - 分支数 7，函数体节点数 133；return: None
    - 调用: send, exception, _clear_ws_context, send_file, warning
  #### `⏵m` `async send_file(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L159
    - 分支数 7，函数体节点数 214；return: True, False
    - 调用: get, warning, _upload_media_ws, str, reply, debug, exception
  #### `⏵m` `async _on_ws_text(self, frame: dict[str, Any]) -> None`  L199
    - 分支数 1，函数体节点数 113；return: None
    - 调用: get, strip, _publish_ws_inbound
  #### `⏵m` `async _on_ws_mixed(self, frame: dict[str, Any]) -> None`  L207
    - 分支数 7，函数体节点数 273；return: None
    - 调用: get, strip, append, isinstance, join, _publish_ws_inbound
  #### `⏵m` `async _on_ws_image(self, frame: dict[str, Any]) -> None`  L238
    - 分支数 1，函数体节点数 110；return: None
    - 调用: get, isinstance, _publish_ws_inbound
  #### `⏵m` `async _on_ws_file(self, frame: dict[str, Any]) -> None`  L257
    - 分支数 1，函数体节点数 110；return: None
    - 调用: get, isinstance, _publish_ws_inbound
  #### `⏵m` `async _publish_ws_inbound(self, frame: dict[str, Any], text: str, *, files: list[dict[str, Any]] | None) -> None`  L276
    - 分支数 6，函数体节点数 284；return: None
    - 调用: get, _pending_connect_code, _bind_connection_from_connect_code, str, is_known_channel_command, _make_inbound, generate_req_id, reply_stream, _attach_connection_identity, publish_inbound
  #### `⏵m` `async _attach_connection_identity(self, inbound: InboundMessage) -> InboundMessage`  L335
    - 分支数 0，函数体节点数 42；return: await attach_connection_identity(inbound, repo=self._connection_repo, provider='wecom', workspace_id=str(inbound.metadata.get('aibotid') or '') or None, fallback_without_workspace=True)
    - 调用: attach_connection_identity, str, get
  #### `⏵m` `async _bind_connection_from_connect_code(self, *, frame: dict[str, Any], user_id: str, code: str) -> bool`  L344
    - 分支数 3，函数体节点数 169；return: False, True
    - 调用: consume_oauth_state, _send_connection_reply, get, str, upsert_connection
  #### `⏵m` `async _send_connection_reply(self, frame: dict[str, Any], text: str) -> None`  L373
    - 分支数 1，函数体节点数 45；return: None
    - 调用: reply
  #### `⏵m` `async _send_ws(self, msg: OutboundMessage, *, _max_retries: int) -> None`  L378
    - 分支数 5，函数体节点数 187；return: None
    - 调用: get, generate_req_id, _send_with_retry, reply_stream, bool, send_message
  #### `⏵m` `async _upload_media_ws(self, *, media_type: str, filename: str, path: str, size: int) -> str | None`  L410
    - 分支数 10，函数体节点数 352；return: None, media_id
    - 调用: warning, md5, open, iter, read, update, hexdigest, generate_req_id, int, _send_ws_upload_command, get, range, decode, b64encode
  - 文件IO: open (L432), read (L433), open (L451), read (L453)

## 文件内调用关系
- `WeComChannel.__init__` -> __init__
- `WeComChannel.send` -> _send_ws
- `WeComChannel._on_outbound` -> send, _clear_ws_context, send_file
- `WeComChannel.send_file` -> _upload_media_ws
- `WeComChannel._on_ws_text` -> _publish_ws_inbound
- `WeComChannel._on_ws_mixed` -> _publish_ws_inbound
- `WeComChannel._on_ws_image` -> _publish_ws_inbound
- `WeComChannel._on_ws_file` -> _publish_ws_inbound
- `WeComChannel._publish_ws_inbound` -> _bind_connection_from_connect_code, _attach_connection_identity
- `WeComChannel._bind_connection_from_connect_code` -> _send_connection_reply
- `WeComChannel._upload_media_ws` -> _send_ws_upload_command

# `backend/app/channels/discord.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/discord.py`  ·  行数: 644

**模块文档首行**（仅供参考）: Discord channel integration using discord.py.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, io, json, logging, threading
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Any
- `app.channels.base` -> Channel
- `app.channels.commands` -> is_known_channel_command
- `app.channels.connection_identity` -> attach_connection_identity
- `app.channels.message_bus` -> InboundMessage, InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_DISCORD_MAX_MESSAGE_LEN` = 2000

## 类
### 类 `DiscordChannel`  L23
- 继承: Channel
- _文档首行_: Discord bot channel.
- 方法:
  #### `st` `_read_attachment_bytes(path: str) -> bytes`    @staticmethod  L168
    - _文档首行_（仅供参考）: Read an attachment file synchronously (intended for ``asyncio.to_thread``).
    - 分支数 1，函数体节点数 27；return: fp.read()
    - 调用: open, read
  - 文件IO: open (L170), read (L171)
  #### `st` `_split_text(text: str) -> list[str]`    @staticmethod  L627
    - 分支数 4，函数体节点数 112；return: [''], chunks
    - 调用: len, rfind, append, lstrip
  #### `m` `__init__(self, bus: MessageBus, config: dict[str, Any]) -> None`  L37
    - 分支数 4，函数体节点数 327
    - 调用: __init__, super, strip, str, get, set, add, int, bool, Lock, home
  #### `m` `_load_active_threads(self) -> None`  L115
    - _文档首行_（仅供参考）: Restore Discord thread mappings from the dedicated JSON file on startup.
    - 分支数 5，函数体节点数 132；return: None
    - 调用: exists, debug, loads, read_text, clear, items, add, info, len, exception
  - 文件IO: exists (L119), read_text (L122)
  #### `m` `_record_thread_mapping(self, channel_id: str, thread_id: str) -> None`  L133
    - _文档首行_（仅供参考）: Synchronously update the in-memory channel->thread mapping and its reverse-lookup set.
    - 分支数 1，函数体节点数 58
    - 调用: get, discard, add
  #### `m` `_persist_thread_mappings(self) -> None`  L150
    - _文档首行_（仅供参考）: Flush the current in-memory thread mappings to disk.
    - 分支数 2，函数体节点数 64
    - 调用: dict, mkdir, write_text, dumps, exception
  - 文件IO: mkdir (L162), write_text (L163)
  #### `m` `_publish(self, inbound) -> None`  L468
    - _文档首行_（仅供参考）: Publish an inbound message to the main event loop.
    - 分支数 1，函数体节点数 70
    - 调用: is_running, run_coroutine_threadsafe, publish_inbound, add_done_callback, exception
  #### `m` `_run_client(self) -> None`  L528
    - 分支数 4，函数体节点数 101
    - 调用: new_event_loop, set_event_loop, run_until_complete, start, exception, is_closed, close
  #### `⏵m` `async start(self) -> None`  L76
    - 分支数 3，函数体节点数 188；return: None
    - 调用: error, default, Client, none, get_event_loop, _on_message, subscribe_outbound, Thread, start, to_thread, info
  #### `⏵m` `async stop(self) -> None`  L173
    - 分支数 5，函数体节点数 190
    - 调用: unsubscribe_outbound, list, items, done, cancel, debug, clear, is_running, run_coroutine_threadsafe, close, wait_for, wrap_future, warning, exception, join, info
  #### `⏵m` `async send(self, msg: OutboundMessage) -> None`  L202
    - 分支数 2，函数体节点数 122；return: None
    - 调用: run_coroutine_threadsafe, _stop_typing, wrap_future, _resolve_target, error, _split_text, send
  #### `⏵m` `async send_file(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L217
    - 分支数 3，函数体节点数 190；return: False, True
    - 调用: run_coroutine_threadsafe, _stop_typing, wrap_future, _resolve_target, error, to_thread, str, File, BytesIO, send, info, exception
  #### `⏵m` `async _start_typing(self, channel, chat_id: str, thread_ts: str | None) -> None`  L245
    - _文档首行_（仅供参考）: Starts a loop to send periodic typing indicators.
    - 分支数 4，函数体节点数 89；return: None
    - 调用: trigger_typing, sleep, create_task, _typing_loop
  #### `⏵m` `async _stop_typing(self, chat_id: str, thread_ts: str | None) -> None`  L265
    - _文档首行_（仅供参考）: Stops the typing loop for a specific target.
    - 分支数 1，函数体节点数 65
    - 调用: pop, done, cancel, debug
  #### `⏵m` `async _add_reaction(self, message) -> None`  L273
    - _文档首行_（仅供参考）: Add a checkmark reaction to acknowledge the message was received.
    - 分支数 1，函数体节点数 32
    - 调用: add_reaction, debug
  #### `⏵m` `async _on_message(self, message) -> None`  L280
    - 分支数 23，函数体节点数 1126；return: None
    - 调用: strip, replace, _pending_connect_code, _bind_connection_from_connect_code, isinstance, str, is_known_channel_command, _make_inbound, _attach_connection_identity, _publish, create_task, _start_typing, _add_reaction, debug, _create_thread, _record_thread_mapping, to_thread, info, _get_channel_or_thread
  - 文件IO: replace (L316), replace (L316), replace (L316)
  #### `⏵m` `async _attach_connection_identity(self, inbound: InboundMessage, guild_id: str | None) -> InboundMessage`  L474
    - 分支数 0，函数体节点数 34；return: await attach_connection_identity(inbound, repo=self._connection_repo, provider='discord', workspace_id=guild_id, fallback_without_workspace=True)
    - 调用: attach_connection_identity
  #### `⏵m` `async _bind_connection_from_connect_code(self, message, code: str) -> bool`  L483
    - 分支数 3，函数体节点数 229；return: False, True
    - 调用: consume_oauth_state, _send_connection_reply, getattr, str, upsert_connection
  - 反射: getattr (L492), getattr (L493), getattr (L494), getattr (L495), getattr (L500), getattr (L505), getattr (L505), getattr (L507), getattr (L510)
  #### `⏵m` `async _send_connection_reply(message, text: str) -> None`    @staticmethod  L518
    - 分支数 2，函数体节点数 54；return: None
    - 调用: getattr, send, exception
  - 反射: getattr (L519), getattr (L520)
  #### `⏵m` `async _create_thread(self, message)`  L543
    - 分支数 4，函数体节点数 174；return: None, await message.create_thread(name=thread_name)
    - 调用: info, create_thread, exception
  #### `⏵m` `async _resolve_target(self, msg: OutboundMessage)`  L581
    - 分支数 5，函数体节点数 101；return: None, target
    - 调用: append, _get_channel_or_thread
  #### `⏵m` `async _get_channel_or_thread(self, raw_id: str)`  L597
    - 分支数 3，函数体节点数 84；return: None, await asyncio.wrap_future(get_future)
    - 调用: int, run_coroutine_threadsafe, _fetch_channel, wrap_future, exception
  #### `⏵m` `async _fetch_channel(self, target_id: int)`  L613
    - 分支数 3，函数体节点数 53；return: None, channel, await self._client.fetch_channel(target_id)
    - 调用: get_channel, fetch_channel

## 文件内调用关系
- `DiscordChannel.__init__` -> __init__
- `DiscordChannel.start` -> _on_message, start
- `DiscordChannel.send` -> _stop_typing, _resolve_target, _split_text, send
- `DiscordChannel.send_file` -> _stop_typing, _resolve_target, send
- `DiscordChannel._on_message` -> _bind_connection_from_connect_code, _attach_connection_identity, _publish, _start_typing, _add_reaction, _create_thread, _record_thread_mapping, _get_channel_or_thread
- `DiscordChannel._bind_connection_from_connect_code` -> _send_connection_reply
- `DiscordChannel._send_connection_reply` -> send
- `DiscordChannel._run_client` -> start
- `DiscordChannel._resolve_target` -> _get_channel_or_thread
- `DiscordChannel._get_channel_or_thread` -> _fetch_channel

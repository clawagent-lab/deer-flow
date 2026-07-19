# `backend/app/channels/telegram.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/telegram.py`  ·  行数: 562

**模块文档首行**（仅供参考）: Telegram channel — connects via long-polling (no public IP needed).

## 模块概览
- 函数 0 个，类 1 个，模块级常量 6 个

## 依赖（import）
- 模块: asyncio, logging, threading, time
- `__future__` -> annotations
- `typing` -> Any
- `app.channels.base` -> Channel
- `app.channels.connection_identity` -> attach_connection_identity
- `app.channels.message_bus` -> InboundMessage, InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `TELEGRAM_MAX_MESSAGE_LENGTH` = 4096
- `STREAM_EDIT_MIN_INTERVAL_SECONDS` = 1.0
- `STREAM_EDIT_GROUP_MIN_INTERVAL_SECONDS` = 3.0
- `MAX_TRACKED_STREAM_MESSAGES` = 256
- `_monotonic` = time.monotonic

## 类
### 类 `TelegramChannel`  L30
- 继承: Channel
- _文档首行_: Telegram bot channel using long-polling.
- 方法:
  #### `prop` `supports_streaming(self) -> bool`    @property  L57
    - 分支数 0，函数体节点数 9；return: True
  #### `st` `_stream_key(chat_id: str, thread_ts: str | None) -> str`    @staticmethod  L299
    - 分支数 0，函数体节点数 27；return: f"{chat_id}:{thread_ts or ''}"
  #### `st` `_parse_message_id(value: str | None) -> int | None`    @staticmethod  L303
    - 分支数 1，函数体节点数 35；return: int(value) if value else None, None
    - 调用: int
  #### `st` `_is_retry_after(exc: Exception) -> bool`    @staticmethod  L320
    - 分支数 0，函数体节点数 20；return: getattr(exc, 'retry_after', None) is not None
    - 调用: getattr
  - 反射: getattr (L321)
  #### `st` `_retry_after_seconds(exc: Exception) -> float`    @staticmethod  L324
    - 分支数 1，函数体节点数 41；return: float(value.total_seconds()), float(value)
    - 调用: getattr, hasattr, float, total_seconds
  - 反射: getattr (L325), hasattr (L326)
  #### `st` `_is_not_modified(exc: Exception) -> bool`    @staticmethod  L331
    - 分支数 0，函数体节点数 21；return: 'message is not modified' in str(exc).lower()
    - 调用: lower, str
  #### `st` `_split_message(text: str) -> list[str]`    @staticmethod  L335
    - 分支数 0，函数体节点数 48；return: [text[i:i + TELEGRAM_MAX_MESSAGE_LENGTH] for i in range(0, len(text), TELEGRAM_MAX_MESSAGE_LENGTH)] or [text]
    - 调用: range, len
  #### `st` `_telegram_display_name(user) -> str`    @staticmethod  L390
    - 分支数 2，函数体节点数 68；return: full_name, username, str(getattr(user, 'id', ''))
    - 调用: getattr, isinstance, str
  - 反射: getattr (L391), getattr (L394), getattr (L397)
  #### `st` `_strip_bot_username_from_leading_command(text: str, bot_username: str | None) -> str`    @staticmethod  L445
    - 分支数 4，函数体节点数 146；return: text, normalized
    - 调用: lower, lstrip, startswith, split, rsplit, len
  #### `m` `__init__(self, bus: MessageBus, config: dict[str, Any]) -> None`  L38
    - 分支数 2，函数体节点数 165
    - 调用: __init__, super, set, get, add, int
  #### `m` `_register_stream_message(self, key: str, *, message_id: int, last_text: str, last_edit_at: float) -> None`  L309
    - 分支数 1，函数体节点数 76
    - 调用: pop, len, next, iter
  #### `m` `_run_polling(self) -> None`  L359
    - _文档首行_（仅供参考）: Run telegram polling in a dedicated thread.
    - 分支数 4，函数体节点数 164
    - 调用: new_event_loop, set_event_loop, run_until_complete, initialize, start, start_polling, run_forever, exception, stop, shutdown
  #### `m` `_check_user(self, user_id: int) -> bool`  L384
    - 分支数 1，函数体节点数 26；return: True, user_id in self._allowed_users
  #### `m` `_get_bot_username(self, context) -> str | None`  L437
    - 分支数 1，函数体节点数 70；return: str(username) if username else None
    - 调用: getattr, str
  - 反射: getattr (L438), getattr (L439), getattr (L441), getattr (L441)
  #### `⏵m` `async start(self) -> None`  L60
    - 分支数 3，函数体节点数 293；return: None
    - 调用: error, get, get_event_loop, subscribe_outbound, build, token, ApplicationBuilder, add_handler, CommandHandler, MessageHandler, Thread, start, info
  #### `⏵m` `async stop(self) -> None`  L106
    - 分支数 2，函数体节点数 84
    - 调用: unsubscribe_outbound, is_running, call_soon_threadsafe, join, info
  #### `⏵m` `async send(self, msg: OutboundMessage, *, _max_retries: int) -> None`  L117
    - 分支数 4，函数体节点数 157；return: None
    - 调用: int, error, _stream_key, _send_stream_update, _parse_message_id, pop, _finalize_stream_message, _send_new_message
  #### `⏵m` `async _send_stream_update(self, chat_id: int, key: str, text: str, reply_to: int | None) -> None`  L140
    - _文档首行_（仅供参考）: Edit the in-flight streamed message with accumulated text.
    - 分支数 11，函数体节点数 331；return: None
    - 调用: len, get, send_message, exception, _register_stream_message, _monotonic, edit_message_text, _is_not_modified, _is_retry_after, debug, warning
  #### `⏵m` `async _finalize_stream_message(self, chat_id: int, chat_key: str, state: dict[str, Any], text: str) -> None`  L197
    - _文档首行_（仅供参考）: Apply the final text: edit the streamed message, splitting overflow into follow-ups.
    - 分支数 3，函数体节点数 143
    - 调用: _split_message, _edit_final_chunk, _send_new_message
  #### `⏵m` `async _edit_final_chunk(self, bot, chat_id: int, message_id: int, text: str) -> bool`  L216
    - _文档首行_（仅供参考）: Edit with one rate-limit retry. Returns False if the edit could not be applied.
    - 分支数 4，函数体节点数 101；return: True, False
    - 调用: range, edit_message_text, _is_not_modified, _is_retry_after, sleep, _retry_after_seconds, warning
  #### `⏵m` `async _send_new_message(self, chat_id: int, chat_key: str, text: str, *, _max_retries: int) -> int | None`  L232
    - _文档首行_（仅供参考）: Send a fresh message with retry/backoff. Returns the sent message_id.
    - 分支数 1，函数体节点数 123；return: sent.message_id, await self._send_with_retry(send_message, max_retries=_max_retries, log_prefix='[Telegram]')
    - 调用: get, send_message, _send_with_retry
  #### `⏵m` `async send_file(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L254
    - 分支数 9，函数体节点数 289；return: False, True
    - 调用: int, error, warning, get, open, send_photo, InputFile, send_document, info, exception
  - 文件IO: open (L274), open (L282)
  #### `⏵m` `async _send_running_reply(self, chat_id: str, reply_to_message_id: int) -> None`  L338
    - _文档首行_（仅供参考）: Send a 'Working on it...' reply and register it as the stream target.
    - 分支数 2，函数体节点数 98；return: None
    - 调用: send_message, int, _register_stream_message, _stream_key, str, info, exception
  #### `⏵m` `async _bind_connection_from_start_token(self, update, state_token: str) -> bool`  L399
    - 分支数 2，函数体节点数 179；return: False, True
    - 调用: consume_oauth_state, reply_text, str, upsert_connection, _telegram_display_name, getattr, info
  - 反射: getattr (L421)
  #### `⏵m` `async _attach_connection_identity(self, inbound: InboundMessage) -> InboundMessage`  L429
    - 分支数 0，函数体节点数 27；return: await attach_connection_identity(inbound, repo=self._connection_repo, provider='telegram', workspace_id=inbound.chat_id)
    - 调用: attach_connection_identity
  #### `⏵m` `async _cmd_start(self, update, context) -> None`  L464
    - _文档首行_（仅供参考）: Handle /start command.
    - 分支数 3，函数体节点数 78；return: None
    - 调用: getattr, _bind_connection_from_start_token, str, _check_user, reply_text
  - 反射: getattr (L466)
  #### `⏵m` `async _process_incoming_with_reply(self, chat_id: str, msg_id: int, inbound: InboundMessage) -> None`  L477
    - 分支数 0，函数体节点数 35
    - 调用: _send_running_reply, publish_inbound
  #### `⏵m` `async _cmd_generic(self, update, context) -> None`  L481
    - _文档首行_（仅供参考）: Forward slash commands to the channel manager.
    - 分支数 4，函数体节点数 243；return: None
    - 调用: _check_user, _strip_bot_username_from_leading_command, strip, _get_bot_username, str, _make_inbound, _attach_connection_identity, is_running, run_coroutine_threadsafe, _process_incoming_with_reply, add_done_callback, _log_future_error, warning
  #### `⏵m` `async _on_text(self, update, context) -> None`  L519
    - _文档首行_（仅供参考）: Handle regular text messages.
    - 分支数 5，函数体节点数 249；return: None
    - 调用: _check_user, _strip_bot_username_from_leading_command, strip, _get_bot_username, str, _make_inbound, _attach_connection_identity, is_running, run_coroutine_threadsafe, _process_incoming_with_reply, add_done_callback, _log_future_error, warning

## 文件内调用关系
- `TelegramChannel.__init__` -> __init__
- `TelegramChannel.start` -> start
- `TelegramChannel.send` -> _stream_key, _send_stream_update, _parse_message_id, _finalize_stream_message, _send_new_message
- `TelegramChannel._send_stream_update` -> _register_stream_message, _is_not_modified, _is_retry_after
- `TelegramChannel._finalize_stream_message` -> _split_message, _edit_final_chunk, _send_new_message
- `TelegramChannel._edit_final_chunk` -> _is_not_modified, _is_retry_after, _retry_after_seconds
- `TelegramChannel._send_running_reply` -> _register_stream_message, _stream_key
- `TelegramChannel._run_polling` -> start, stop
- `TelegramChannel._bind_connection_from_start_token` -> _telegram_display_name
- `TelegramChannel._cmd_start` -> _bind_connection_from_start_token, _check_user
- `TelegramChannel._process_incoming_with_reply` -> _send_running_reply
- `TelegramChannel._cmd_generic` -> _check_user, _strip_bot_username_from_leading_command, _get_bot_username, _attach_connection_identity, _process_incoming_with_reply
- `TelegramChannel._on_text` -> _check_user, _strip_bot_username_from_leading_command, _get_bot_username, _attach_connection_identity, _process_incoming_with_reply

# `backend/app/channels/feishu.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/feishu.py`  ·  行数: 1140

**模块文档首行**（仅供参考）: Feishu/Lark channel — connects to Feishu via WebSocket (no public IP needed).

## 模块概览
- 函数 1 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: asyncio, json, logging, re, threading, time
- `__future__` -> annotations
- `typing` -> Any, Literal
- `app.channels.base` -> Channel
- `app.channels.commands` -> is_known_channel_command, strip_leading_mentions
- `app.channels.connection_identity` -> attach_connection_identity
- `app.channels.message_bus` -> PENDING_CLARIFICATION_METADATA_KEY, RESOLVED_FROM_PENDING_CLARIFICATION_METADATA_KEY, InboundMessage, InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX, get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.sandbox.sandbox_provider` -> get_sandbox_provider

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `PENDING_CLARIFICATION_TTL_SECONDS` = 30 * 60
- `FEISHU_INBOUND_BATCH_WINDOW_SECONDS` = 0.75
- `SOURCE_PREVIEW_METADATA_KEY` = 'feishu_source_preview'

## 函数
#### `ƒ` `_is_feishu_command(text: str) -> bool`  L35
  - 分支数 0，函数体节点数 13；return: is_known_channel_command(text)
  - 调用: is_known_channel_command

## 类
### 类 `FeishuChannel`  L39
- 继承: Channel
- _文档首行_: Feishu/Lark IM channel using the ``lark-oapi`` WebSocket client.
- 方法:
  #### `prop` `supports_streaming(self) -> bool`    @property  L129
    - 分支数 0，函数体节点数 9；return: True
  #### `prop` `is_running(self) -> bool`    @property  L133
    - 分支数 1，函数体节点数 33；return: False, self._thread is not None and self._thread.is_alive()
    - 调用: is_alive
  #### `cls` `_compose_card_text(cls, text: str, metadata: dict[str, Any] | None) -> str`    @classmethod  L116
    - 分支数 3，函数体节点数 108；return: text, f'{quoted_preview}\n\n{text}'
    - 调用: isinstance, get, strip, join, splitlines
  #### `st` `_non_empty_str(value: Any) -> str | None`    @staticmethod  L80
    - 分支数 1，函数体节点数 35；return: value.strip(), None
    - 调用: isinstance, strip
  #### `st` `_pending_key(chat_id: str, user_id: str) -> tuple[str, str]`    @staticmethod  L86
    - 分支数 0，函数体节点数 27；return: (chat_id, user_id)
  #### `st` `_should_include_source_preview(*, chat_type: str | None, root_id: str | None, parent_id: str | None, thread_id: str | None) -> bool`    @staticmethod  L90
    - 分支数 1，函数体节点数 50；return: False, bool(root_id or parent_id or thread_id)
    - 调用: bool
  #### `st` `_compact_source_preview(text: str) -> str | None`    @staticmethod  L102
    - 分支数 3，函数体节点数 96；return: None, preview
    - 调用: strip, splitlines, join, len, rstrip
  #### `st` `_build_card_content(text: str) -> str`    @staticmethod  L474
    - _文档首行_（仅供参考）: Build a Feishu interactive card with markdown content.
    - 分支数 0，函数体节点数 38；return: json.dumps(card)
    - 调用: dumps
  #### `st` `_is_batchable_file_inbound(*, msg_type: InboundMessageType, text: str, files: list[dict[str, Any]], root_id: str | None, parent_id: str | None, thread_id: str | None) -> bool`    @staticmethod  L791
    - 分支数 0，函数体节点数 81；return: msg_type == InboundMessageType.CHAT and text in {'[file]', '[image]'} and (len(files) == 1) and (not (root_id or parent_id or thread_id))
    - 调用: len
  #### `st` `_log_task_error(task: asyncio.Task, name: str, msg_id: str) -> None`    @staticmethod  L898
    - _文档首行_（仅供参考）: Callback for background asyncio tasks to surface errors.
    - 分支数 2，函数体节点数 63
    - 调用: exception, error, info
  #### `m` `__init__(self, bus: MessageBus, config: dict[str, Any]) -> None`  L57
    - 分支数 0，函数体节点数 253
    - 调用: __init__, super, set, Lock
  #### `m` `_build_event_handler(self, lark)`  L138
    - 分支数 0，函数体节点数 52；return: lark.EventDispatcherHandler.builder('', '').register_p2_im_message_receive_v1(self._on_message).register_p2_im_message_message_read_v1(self._on_ignored_message_event).register_p2_im_message_reaction_created_v1(self._on_ignored_message_event).register_p2_im_message_reaction_deleted_v1(self._on_ignored_message_event).register_p2_im_message_recalled_v1(self._on_ignored_message_event).build()
    - 调用: build, register_p2_im_message_recalled_v1, register_p2_im_message_reaction_deleted_v1, register_p2_im_message_reaction_created_v1, register_p2_im_message_message_read_v1, register_p2_im_message_receive_v1, builder
  #### `m` `_run_ws(self, app_id: str, app_secret: str, domain: str) -> None`  L218
    - _文档首行_（仅供参考）: Construct and run the lark WS client in a thread with a fresh event loop.
    - 分支数 2，函数体节点数 109
    - 调用: new_event_loop, set_event_loop, _build_event_handler, Client, start, exception
  #### `m` `_on_ignored_message_event(self, event) -> None`  L256
    - 分支数 0，函数体节点数 19
    - 调用: debug, type
  #### `m` `_track_background_task(self, task: asyncio.Task, *, name: str, msg_id: str) -> None`  L528
    - _文档首行_（仅供参考）: Keep a strong reference to fire-and-forget tasks and surface errors.
    - 分支数 0，函数体节点数 53
    - 调用: add, add_done_callback, _finalize_background_task
  #### `m` `_finalize_background_task(self, task: asyncio.Task, name: str, msg_id: str) -> None`  L533
    - 分支数 0，函数体节点数 37
    - 调用: discard, _log_task_error
  #### `m` `_ensure_running_card_started(self, source_message_id: str, text: str, *, metadata: dict[str, Any] | None) -> asyncio.Task | None`  L553
    - _文档首行_（仅供参考）: Start running-card creation once per source message.
    - 分支数 2，函数体节点数 124；return: None, running_card_task
    - 调用: get, create_task, _create_running_card, add_done_callback, _finalize_running_card_task
  #### `m` `_finalize_running_card_task(self, source_message_id: str, task: asyncio.Task) -> None`  L574
    - 分支数 1，函数体节点数 48
    - 调用: get, pop, _log_task_error
  #### `m` `_remember_thread_mapping(self, msg: OutboundMessage, *topic_ids) -> None`  L667
    - 分支数 5，函数体节点数 206；可变参数（*args/**kwargs）；return: None
    - 调用: get, isinstance, set, _non_empty_str, add, set_thread_id, exception
  #### `m` `_remember_pending_clarification(self, msg: OutboundMessage, card_message_id: str | None) -> None`  L701
    - 分支数 3，函数体节点数 192；return: None
    - 调用: get, _non_empty_str, _pending_key, time, append, setdefault, info
  #### `m` `_consume_pending_clarification(self, chat_id: str, user_id: str) -> dict[str, Any] | None`  L732
    - 分支数 5，函数体节点数 164；return: None, pending
    - 调用: _pending_key, get, time, pop, isinstance, info
  #### `m` `_ensure_pending_thread_mapping(self, chat_id: str, user_id: str, pending: dict[str, Any]) -> None`  L754
    - 分支数 2，函数体节点数 110；return: None
    - 调用: get, _non_empty_str, set_thread_id, exception
  #### `m` `_resolve_topic_id(self, chat_id: str, msg_id: str, *, root_id: str | None, parent_id: str | None, thread_id: str | None) -> tuple[str, bool]`  L765
    - 分支数 5，函数体节点数 130；return: (candidate, True), (root_id or msg_id, False)
    - 调用: get, _non_empty_str, get_thread_id, exception
  #### `m` `_schedule_prepare_inbound(self, msg_id: str, inbound: InboundMessage, *, source_message_ids: list[str] | None) -> None`  L802
    - 分支数 1，函数体节点数 103
    - 调用: is_running, info, run_coroutine_threadsafe, _prepare_inbound, add_done_callback, _log_future_error, warning
  #### `m` `_schedule_batch_flush(self, key: tuple[str, str], source_message_id: str) -> None`  L819
    - 分支数 1，函数体节点数 82
    - 调用: is_running, run_coroutine_threadsafe, _flush_pending_inbound_batch_after, add_done_callback, _log_future_error, warning
  #### `m` `_queue_file_inbound_batch(self, msg_id: str, inbound: InboundMessage) -> bool`  L826
    - 分支数 5，函数体节点数 322；return: True
    - 调用: _pending_key, get, time, append, join, extend, list, info, len, _schedule_batch_flush, _schedule_prepare_inbound
  #### `m` `_pop_pending_inbound_batch(self, key: tuple[str, str], *, anchor_message_id: str | None) -> tuple[str, InboundMessage, list[str]] | None`  L871
    - 分支数 3，函数体节点数 116；return: None, (batch['anchor_message_id'], batch['inbound'], list(batch['message_ids']))
    - 调用: get, pop, list
  #### `m` `_on_message(self, event) -> None`  L954
    - _文档首行_（仅供参考）: Called by lark-oapi when a message is received (runs in lark thread).
    - 分支数 28，函数体节点数 910；return: None
    - 调用: info, type, getattr, _non_empty_str, loads, get, isinstance, append, join, strip, len, _pending_connect_code, is_running, run_coroutine_threadsafe, _bind_connection_from_connect_code, add_done_callback, _log_future_error, warning, strip_leading_mentions, _is_feishu_command（+10）
  - 反射: getattr (L963), getattr (L964), getattr (L965), getattr (L966)
  #### `⏵m` `async start(self) -> None`  L149
    - 分支数 3，函数体节点数 307；return: None
    - 调用: error, get, build, domain, app_secret, app_id, builder, info, get_event_loop, subscribe_outbound, Thread, start
  #### `⏵m` `async stop(self) -> None`  L259
    - 分支数 3，函数体节点数 101
    - 调用: unsubscribe_outbound, list, cancel, clear, values, join, info
  #### `⏵m` `async send(self, msg: OutboundMessage, *, _max_retries: int) -> None`  L273
    - 分支数 1，函数体节点数 69；return: None
    - 调用: warning, info, len, _send_with_retry, _send_card_message
  #### `⏵m` `async send_file(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L291
    - 分支数 6，函数体节点数 332；return: False, True
    - 调用: warning, _upload_image, dumps, _upload_file, build, request_body, message_id, builder, content, msg_type, to_thread, receive_id_type, receive_id, info, exception
  #### `⏵m` `async _upload_image(self, path) -> str`  L326
    - _文档首行_（仅供参考）: Upload an image to Feishu and return the image_key.
    - 分支数 2，函数体节点数 111；raise: RuntimeError(f'Feishu image upload failed: code={response.code}, msg={response.msg}')；return: response.data.image_key
    - 调用: open, str, build, request_body, builder, image, image_type, to_thread, success, RuntimeError
  - 文件IO: open (L328)
  #### `⏵m` `async _upload_file(self, path, filename: str) -> str`  L335
    - _文档首行_（仅供参考）: Upload a file to Feishu and return the file_key.
    - 分支数 6，函数体节点数 192；raise: RuntimeError(f'Feishu file upload failed: code={response.code}, msg={response.msg}')；return: response.data.file_key
    - 调用: hasattr, lower, open, str, build, request_body, builder, file, file_name, file_type, to_thread, success, RuntimeError
  - 文件IO: open (L349)
  - 反射: hasattr (L337)
  #### `⏵m` `async receive_file(self, msg: InboundMessage, thread_id: str, *, user_id: str | None) -> InboundMessage`  L356
    - _文档首行_（仅供参考）: Download a Feishu file into the thread uploads directory.
    - 分支数 5，函数体节点数 171；return: msg
    - 调用: warning, get, _receive_single_file, replace
  - 文件IO: replace (L372), replace (L375)
  #### `⏵m` `async _receive_single_file(self, message_id: str, file_key: str, type: Literal['image', 'file'], thread_id: str, *, user_id: str | None) -> str`  L379
    - 分支数 11，函数体节点数 548；return: self._api_client.im.v1.message_resource.get(request), f'Failed to obtain the [{type}]', virtual_path
    - 调用: build, type, file_key, message_id, builder, get, to_thread, exception, success, warning, get_log_id, getattr, get_paths, get_effective_user_id, ensure_thread_dirs, resolve, sandbox_uploads_dir, rsplit, sub, write_bytes（+4）
  - 文件IO: write_bytes (L445)
  - 反射: getattr (L410), getattr (L431)
  #### `⏵m` `async _add_reaction(self, message_id: str, emoji_type: str) -> None`  L488
    - _文档首行_（仅供参考）: Add an emoji reaction to a message.
    - 分支数 2，函数体节点数 125；return: None
    - 调用: build, request_body, message_id, builder, reaction_type, emoji_type, to_thread, info, exception
  #### `⏵m` `async _reply_card(self, message_id: str, text: str) -> str | None`  L499
    - _文档首行_（仅供参考）: Reply with an interactive card and return the created card message ID.
    - 分支数 1，函数体节点数 116；return: None, getattr(response_data, 'message_id', None)
    - 调用: _build_card_content, build, request_body, message_id, builder, content, msg_type, to_thread, getattr
  - 反射: getattr (L507), getattr (L508)
  #### `⏵m` `async _create_card(self, chat_id: str, text: str) -> None`  L510
    - _文档首行_（仅供参考）: Create a new card message in the target chat.
    - 分支数 1，函数体节点数 95；return: None
    - 调用: _build_card_content, build, request_body, receive_id_type, builder, content, msg_type, receive_id, to_thread
  #### `⏵m` `async _update_card(self, message_id: str, text: str) -> None`  L519
    - _文档首行_（仅供参考）: Patch an existing card message in place.
    - 分支数 1，函数体节点数 95；return: None
    - 调用: _build_card_content, build, request_body, message_id, builder, content, to_thread
  #### `⏵m` `async _create_running_card(self, source_message_id: str, text: str, *, metadata: dict[str, Any] | None) -> str | None`  L537
    - _文档首行_（仅供参考）: Create the running card and cache its message ID when available.
    - 分支数 1，函数体节点数 88；return: running_card_id
    - 调用: _reply_card, _compose_card_text, info, warning
  #### `⏵m` `async _ensure_running_card(self, source_message_id: str, text: str, *, metadata: dict[str, Any] | None) -> str | None`  L579
    - _文档首行_（仅供参考）: Ensure the in-thread running card exists and track its message ID.
    - 分支数 2，函数体节点数 85；return: running_card_id, self._running_card_ids.get(source_message_id), await running_card_task
    - 调用: get, _ensure_running_card_started
  #### `⏵m` `async _send_running_reply(self, message_id: str, *, metadata: dict[str, Any] | None) -> None`  L600
    - _文档首行_（仅供参考）: Reply to a message in-thread with a running card.
    - 分支数 1，函数体节点数 49
    - 调用: _ensure_running_card, exception
  #### `⏵m` `async _send_card_message(self, msg: OutboundMessage) -> None`  L607
    - _文档首行_（仅供参考）: Send or update the Feishu card tied to the current request.
    - 分支数 9，函数体节点数 321；raise: bare raise；return: None
    - 调用: get, _compose_card_text, _update_card, exception, _reply_card, _remember_thread_mapping, _remember_pending_clarification, info, warning, _ensure_running_card, pop, _add_reaction, _create_card
  #### `⏵m` `async _flush_pending_inbound_batch_after(self, key: tuple[str, str], anchor_message_id: str) -> None`  L881
    - 分支数 1，函数体节点数 100；return: None
    - 调用: sleep, _pop_pending_inbound_batch, info, len, _prepare_inbound
  #### `⏵m` `async _prepare_inbound(self, msg_id: str, inbound, *, source_message_ids: list[str] | None) -> None`  L909
    - _文档首行_（仅供参考）: Kick off Feishu side effects without delaying inbound dispatch.
    - 分支数 1，函数体节点数 101
    - 调用: _attach_connection_identity, create_task, _add_reaction, _track_background_task, _ensure_running_card_started, publish_inbound
  #### `⏵m` `async _attach_connection_identity(self, inbound: InboundMessage) -> InboundMessage`  L919
    - 分支数 0，函数体节点数 27；return: await attach_connection_identity(inbound, repo=self._connection_repo, provider='feishu', workspace_id=inbound.chat_id)
    - 调用: attach_connection_identity
  #### `⏵m` `async _bind_connection_from_connect_code(self, *, message_id: str, chat_id: str, user_id: str, code: str) -> bool`  L927
    - 分支数 3，函数体节点数 135；return: False, True
    - 调用: consume_oauth_state, _reply_card, upsert_connection

## 文件内调用关系
- `FeishuChannel.__init__` -> __init__
- `FeishuChannel.start` -> start
- `FeishuChannel._run_ws` -> _build_event_handler, start
- `FeishuChannel.send` -> _send_card_message
- `FeishuChannel.send_file` -> _upload_image, _upload_file
- `FeishuChannel.receive_file` -> _receive_single_file
- `FeishuChannel._reply_card` -> _build_card_content
- `FeishuChannel._create_card` -> _build_card_content
- `FeishuChannel._update_card` -> _build_card_content
- `FeishuChannel._track_background_task` -> _finalize_background_task
- `FeishuChannel._finalize_background_task` -> _log_task_error
- `FeishuChannel._create_running_card` -> _reply_card, _compose_card_text
- `FeishuChannel._ensure_running_card_started` -> _create_running_card, _finalize_running_card_task
- `FeishuChannel._finalize_running_card_task` -> _log_task_error
- `FeishuChannel._ensure_running_card` -> _ensure_running_card_started
- `FeishuChannel._send_running_reply` -> _ensure_running_card
- `FeishuChannel._send_card_message` -> _compose_card_text, _update_card, _reply_card, _remember_thread_mapping, _remember_pending_clarification, _ensure_running_card, _add_reaction, _create_card
- `FeishuChannel._remember_thread_mapping` -> _non_empty_str
- `FeishuChannel._remember_pending_clarification` -> _non_empty_str, _pending_key
- `FeishuChannel._consume_pending_clarification` -> _pending_key
- `FeishuChannel._ensure_pending_thread_mapping` -> _non_empty_str
- `FeishuChannel._resolve_topic_id` -> _non_empty_str
- `FeishuChannel._schedule_prepare_inbound` -> is_running, _prepare_inbound
- `FeishuChannel._schedule_batch_flush` -> is_running, _flush_pending_inbound_batch_after
- `FeishuChannel._queue_file_inbound_batch` -> _pending_key, _schedule_batch_flush, _schedule_prepare_inbound
- `FeishuChannel._flush_pending_inbound_batch_after` -> _pop_pending_inbound_batch, _prepare_inbound
- `FeishuChannel._prepare_inbound` -> _attach_connection_identity, _add_reaction, _track_background_task, _ensure_running_card_started
- `FeishuChannel._bind_connection_from_connect_code` -> _reply_card
- `FeishuChannel._on_message` -> _non_empty_str, is_running, _bind_connection_from_connect_code, _is_feishu_command, _resolve_topic_id, _consume_pending_clarification, _ensure_pending_thread_mapping, _should_include_source_preview, _compact_source_preview, _is_batchable_file_inbound, _queue_file_inbound_batch, _schedule_prepare_inbound

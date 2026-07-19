# `backend/app/channels/dingtalk.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/dingtalk.py`  ·  行数: 823

**模块文档首行**（仅供参考）: DingTalk channel implementation.

## 模块概览
- 函数 6 个，类 2 个，模块级常量 10 个

## 依赖（import）
- 模块: asyncio, json, logging, re, threading, time, httpx
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Any
- `app.channels.base` -> Channel
- `app.channels.commands` -> is_known_channel_command
- `app.channels.connection_identity` -> attach_connection_identity
- `app.channels.message_bus` -> InboundMessage, InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DINGTALK_API_BASE` = 'https://api.dingtalk.com'
- `_TOKEN_REFRESH_MARGIN_SECONDS` = 300
- `_CONVERSATION_TYPE_P2P` = '1'
- `_CONVERSATION_TYPE_GROUP` = '2'
- `_MAX_UPLOAD_SIZE_BYTES` = 20 * 1024 * 1024
- `_FENCED_CODE_BLOCK_RE` = re.compile('```(\\w*)\\n(.*?)```', re.DOTALL)
- `_INLINE_CODE_RE` = re.compile('`([^`\\n]+)`')
- `_HORIZONTAL_RULE_RE` = re.compile('^-{3,}$', re.MULTILINE)
- `_TABLE_SEPARATOR_RE` = re.compile('^\\|[-:| ]+\\|$', re.MULTILINE)

## 函数
#### `ƒ` `_normalize_conversation_type(raw: Any) -> str`  L33
  - _文档首行_（仅供参考）: Normalize ``conversationType`` to ``"1"`` (P2P) or ``"2"`` (group).
  - 分支数 2，函数体节点数 42；return: _CONVERSATION_TYPE_P2P, _CONVERSATION_TYPE_GROUP
  - 调用: strip, str

#### `ƒ` `_normalize_allowed_users(allowed_users: Any) -> set[str]`  L46
  - 分支数 3，函数体节点数 93；return: set(), {str(uid) for uid in values if str(uid)}
  - 调用: set, isinstance, warning, type, str

#### `ƒ` `_is_dingtalk_command(text: str) -> bool`  L62
  - 分支数 0，函数体节点数 13；return: is_known_channel_command(text)
  - 调用: is_known_channel_command

#### `ƒ` `_extract_text_from_rich_text(rich_text_list: list) -> str`  L66
  - 分支数 2，函数体节点数 56；return: ' '.join(parts)
  - 调用: isinstance, append, join

#### `ƒ` `_convert_markdown_table(text: str) -> str`  L80
  - 分支数 4，函数体节点数 236；return: '\n'.join(result)
  - 调用: split, len, startswith, strip, match, zip, append, join

#### `ƒ` `_adapt_markdown_for_dingtalk(text: str) -> str`  L103
  - _文档首行_（仅供参考）: Adapt markdown for DingTalk's limited sampleMarkdown renderer.
  - 分支数 0，函数体节点数 129；return: f'{prefix}{quoted_lines}\n', text
  - 调用: group, rstrip, join, split, sub, _convert_markdown_table

## 类
### 类 `DingTalkChannel`  L120
- 继承: Channel
- _文档首行_: DingTalk IM channel using Stream Push (WebSocket, no public IP needed).
- 方法:
  #### `prop` `supports_streaming(self) -> bool`    @property  L142
    - 分支数 0，函数体节点数 15；return: bool(self._card_template_id)
    - 调用: bool
  #### `st` `_extract_text(message: Any) -> str`    @staticmethod  L453
    - 分支数 2，函数体节点数 65；return: message.text.content.strip(), _extract_text_from_rich_text(message.rich_text_content.rich_text_list).strip(), ''
    - 调用: strip, _extract_text_from_rich_text
  #### `st` `_connection_workspace_id(conversation_type: str, conversation_id: str) -> str | None`    @staticmethod  L469
    - 分支数 1，函数体节点数 31；return: conversation_id, None
  #### `st` `_api_headers(token: str) -> dict[str, str]`    @staticmethod  L615
    - 分支数 0，函数体节点数 24；return: {'x-acs-dingtalk-access-token': token, 'Content-Type': 'application/json'}
  #### `m` `__init__(self, bus: MessageBus, config: dict[str, Any]) -> None`  L123
    - 分支数 0，函数体节点数 209
    - 调用: __init__, super, _normalize_allowed_users, get, Lock
  #### `m` `_resolve_routing(self, msg: OutboundMessage) -> tuple[str, str, str]`  L203
    - _文档首行_（仅供参考）: Return (conversation_type, sender_staff_id, conversation_id).
    - 分支数 1，函数体节点数 96；return: (conversation_type, sender_staff_id, conversation_id)
    - 调用: _normalize_conversation_type, get
  #### `m` `_run_stream(self, client_id: str, client_secret: str) -> None`  L340
    - 分支数 2，函数体节点数 88
    - 调用: Credential, DingTalkStreamClient, register_callback_handler, _DingTalkMessageHandler, start_forever, exception
  #### `m` `_on_chatbot_message(self, message: Any) -> None`  L358
    - 分支数 10，函数体节点数 444；return: None
    - 调用: _normalize_conversation_type, _extract_text, info, _pending_connect_code, is_running, run_coroutine_threadsafe, _bind_connection_from_connect_code, add_done_callback, _log_future_error, warning, debug, len, _is_dingtalk_command, _make_inbound, _make_card_source_key, _prepare_inbound, exception
  #### `m` `_make_card_source_key(self, inbound: InboundMessage) -> str`  L705
    - 分支数 0，函数体节点数 52；return: f"{m.get('conversation_type', '')}:{m.get('sender_staff_id', '')}:{m.get('conversation_id', '')}:{m.get('message_id', '')}"
    - 调用: get
  #### `m` `_make_card_source_key_from_outbound(self, msg: OutboundMessage) -> str`  L709
    - 分支数 0，函数体节点数 63；return: f"{m.get('conversation_type', '')}:{m.get('sender_staff_id', '')}:{m.get('conversation_id', '')}:{correlation_id}"
    - 调用: get
  #### `⏵m` `async start(self) -> None`  L145
    - 分支数 4，函数体节点数 164；return: None
    - 调用: error, get, get_running_loop, info, subscribe_outbound, Thread, start
  #### `⏵m` `async stop(self) -> None`  L180
    - 分支数 5，函数体节点数 131
    - 调用: unsubscribe_outbound, hasattr, disconnect, debug, clear, join, info
  - 反射: hasattr (L187)
  #### `⏵m` `async send(self, msg: OutboundMessage, *, _max_retries: int) -> None`  L217
    - 分支数 6，函数体节点数 245；return: None
    - 调用: _resolve_routing, _make_card_source_key_from_outbound, get, _stream_update_card, warning, pop, _send_markdown_fallback, _send_group_message, _send_p2p_message, _send_with_retry
  #### `⏵m` `async _send_markdown_fallback(self, robot_code: str, conversation_type: str, sender_staff_id: str, conversation_id: str, text: str) -> None`  L263
    - 分支数 2，函数体节点数 64；raise: bare raise
    - 调用: _send_group_message, _send_p2p_message, exception
  #### `⏵m` `async send_file(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L280
    - 分支数 6，函数体节点数 291；return: False, True
    - 调用: warning, _resolve_routing, _upload_media, dumps, str, _get_access_token, AsyncClient, Timeout, post, _api_headers, raise_for_status, info, exception
  - 网络调用: post (L309), post (L320)
  #### `⏵m` `async _prepare_inbound(self, chat_id: str, inbound: InboundMessage) -> None`  L461
    - 分支数 0，函数体节点数 43
    - 调用: _attach_connection_identity, _send_running_reply, publish_inbound
  #### `⏵m` `async _attach_connection_identity(self, inbound: InboundMessage) -> InboundMessage`  L474
    - 分支数 0，函数体节点数 69；return: await attach_connection_identity(inbound, repo=self._connection_repo, provider='dingtalk', workspace_id=self._connection_workspace_id(conversation_type, conversation_id), fallback_without_workspace=True)
    - 调用: str, get, attach_connection_identity, _connection_workspace_id
  #### `⏵m` `async _bind_connection_from_connect_code(self, *, conversation_type: str, sender_staff_id: str, sender_nick: str, conversation_id: str, code: str) -> bool`  L485
    - 分支数 3，函数体节点数 157；return: False, True
    - 调用: consume_oauth_state, _send_connection_reply, upsert_connection, _connection_workspace_id
  #### `⏵m` `async _send_connection_reply(self, conversation_type: str, sender_staff_id: str, conversation_id: str, text: str) -> None`  L536
    - 分支数 3，函数体节点数 63；return: None
    - 调用: _send_text_message_to_group, _send_text_message_to_user
  #### `⏵m` `async _send_running_reply(self, chat_id: str, inbound: InboundMessage) -> None`  L551
    - 分支数 5，函数体节点数 185；return: None
    - 调用: get, _make_card_source_key, pop, _create_and_deliver_card, info, _send_text_message_to_group, _send_text_message_to_user, exception
  #### `⏵m` `async _get_access_token(self) -> str`  L582
    - 分支数 7，函数体节点数 242；raise: ValueError(f'DingTalk access token response must be a JSON object, got {type(data).__name__}'), ValueError('DingTalk access token response did not contain a usable accessToken')；return: self._cached_token
    - 调用: monotonic, AsyncClient, Timeout, post, raise_for_status, json, isinstance, ValueError, type, get, strip, int, warning
  - 网络调用: post (L589)
  #### `⏵m` `async _send_text_message_to_user(self, robot_code: str, user_id: str, text: str) -> None`  L621
    - 分支数 1，函数体节点数 88
    - 调用: _get_access_token, AsyncClient, Timeout, post, _api_headers, dumps, raise_for_status
  - 网络调用: post (L624)
  #### `⏵m` `async _send_text_message_to_group(self, robot_code: str, conversation_id: str, text: str) -> None`  L636
    - 分支数 1，函数体节点数 86
    - 调用: _get_access_token, AsyncClient, Timeout, post, _api_headers, dumps, raise_for_status
  - 网络调用: post (L639)
  #### `⏵m` `async _send_p2p_message(self, robot_code: str, user_id: str, text: str) -> None`  L651
    - 分支数 2，函数体节点数 131
    - 调用: _adapt_markdown_for_dingtalk, _get_access_token, AsyncClient, Timeout, post, _api_headers, dumps, raise_for_status, json, get, info, warning
  - 网络调用: post (L655)
  #### `⏵m` `async _send_group_message(self, robot_code: str, conversation_id: str, text: str, *, at_user_ids: list[str] | None) -> None`  L672
    - 分支数 2，函数体节点数 140
    - 调用: _adapt_markdown_for_dingtalk, _get_access_token, AsyncClient, Timeout, post, _api_headers, dumps, raise_for_status, json, get, info, warning
  - 网络调用: post (L686)
  #### `⏵m` `async _create_and_deliver_card(self, initial_text: str, *, chatbot_message: Any) -> str | None`  L714
    - 分支数 4，函数体节点数 128；return: None, card_instance_id
    - 调用: warning, AICardReplier, async_create_and_deliver_card, info, exception
  #### `⏵m` `async _stream_update_card(self, out_track_id: str, content: str, *, is_finalize: bool, is_error: bool) -> None`  L746
    - 分支数 1，函数体节点数 67；raise: RuntimeError(f'No AICardReplier found for track ID {out_track_id}')
    - 调用: get, RuntimeError, async_streaming
  #### `⏵m` `async _upload_media(self, file_path: str | Path, media_type: str) -> str | None`  L769
    - 分支数 4，函数体节点数 178；return: None, payload.get('mediaId')
    - 调用: to_thread, Path, _get_access_token, AsyncClient, Timeout, post, raise_for_status, json, exception, isinstance, warning, type, get
  - 网络调用: post (L774)

### 类 `_DingTalkMessageHandler`  L795
- _文档首行_: Callback handler registered with dingtalk-stream.
- 方法:
  #### `m` `__init__(self, channel: DingTalkChannel) -> None`  L798
    - 分支数 0，函数体节点数 14
  #### `m` `pre_start(self) -> None`  L801
    - 分支数 1，函数体节点数 31
    - 调用: hasattr
  - 反射: hasattr (L802)
  #### `⏵m` `async raw_process(self, callback_message: Any) -> Any`  L805
    - 分支数 0，函数体节点数 78；return: ack_message
    - 调用: process, AckMessage
  #### `⏵m` `async process(self, callback: Any) -> tuple[int, str]`  L817
    - 分支数 0，函数体节点数 52；return: (dingtalk_stream.AckMessage.STATUS_OK, 'OK')
    - 调用: from_dict, _on_chatbot_message

## 文件内调用关系
- `_adapt_markdown_for_dingtalk` -> _convert_markdown_table
- `DingTalkChannel.__init__` -> __init__, _normalize_allowed_users
- `DingTalkChannel.start` -> start
- `DingTalkChannel._resolve_routing` -> _normalize_conversation_type
- `DingTalkChannel.send` -> _resolve_routing, _make_card_source_key_from_outbound, _stream_update_card, _send_markdown_fallback, _send_group_message, _send_p2p_message
- `DingTalkChannel._send_markdown_fallback` -> _send_group_message, _send_p2p_message
- `DingTalkChannel.send_file` -> _resolve_routing, _upload_media, _get_access_token, _api_headers
- `DingTalkChannel._on_chatbot_message` -> _normalize_conversation_type, _extract_text, _bind_connection_from_connect_code, _is_dingtalk_command, _make_card_source_key, _prepare_inbound
- `DingTalkChannel._extract_text` -> _extract_text_from_rich_text
- `DingTalkChannel._prepare_inbound` -> _attach_connection_identity, _send_running_reply
- `DingTalkChannel._attach_connection_identity` -> _connection_workspace_id
- `DingTalkChannel._bind_connection_from_connect_code` -> _send_connection_reply, _connection_workspace_id
- `DingTalkChannel._send_connection_reply` -> _send_text_message_to_group, _send_text_message_to_user
- `DingTalkChannel._send_running_reply` -> _make_card_source_key, _create_and_deliver_card, _send_text_message_to_group, _send_text_message_to_user
- `DingTalkChannel._send_text_message_to_user` -> _get_access_token, _api_headers
- `DingTalkChannel._send_text_message_to_group` -> _get_access_token, _api_headers
- `DingTalkChannel._send_p2p_message` -> _adapt_markdown_for_dingtalk, _get_access_token, _api_headers
- `DingTalkChannel._send_group_message` -> _adapt_markdown_for_dingtalk, _get_access_token, _api_headers
- `DingTalkChannel._upload_media` -> _get_access_token
- `_DingTalkMessageHandler.raw_process` -> process
- `_DingTalkMessageHandler.process` -> _on_chatbot_message

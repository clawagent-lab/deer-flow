# `backend/app/channels/slack.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/slack.py`  ·  行数: 411

**模块文档首行**（仅供参考）: Slack channel — connects via Socket Mode (no public IP needed).

## 模块概览
- 函数 2 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, logging
- `__future__` -> annotations
- `typing` -> Any
- `markdown_to_mrkdwn` -> SlackMarkdownConverter
- `app.channels.base` -> Channel
- `app.channels.commands` -> is_known_channel_command
- `app.channels.connection_identity` -> attach_connection_identity
- `app.channels.message_bus` -> InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_slack_md_converter` = SlackMarkdownConverter()

## 函数
#### `ƒ` `_normalize_allowed_users(allowed_users: Any) -> set[str]`  L21
  - 分支数 3，函数体节点数 95；return: set(), {str(user_id) for user_id in values if str(user_id)}
  - 调用: set, isinstance, warning, type, str

#### `ƒ` `_strip_leading_slack_bot_mention(text: str, bot_user_id: str | None) -> str`  L37
  - 分支数 4，函数体节点数 98；return: text, text[end + 1:].lstrip()
  - 调用: startswith, find, lstrip, split

## 类
### 类 `SlackChannel`  L51
- 继承: Channel
- _文档首行_: Slack IM channel using Socket Mode (WebSocket, no public IP).
- 方法:
  #### `st` `_add_reaction_with_client(web_client, channel_id: str, timestamp: str, emoji: str) -> None`    @staticmethod  L229
    - 分支数 2，函数体节点数 54
    - 调用: reactions_add, str, warning
  #### `m` `__init__(self, bus: MessageBus, config: dict[str, Any]) -> None`  L62
    - 分支数 0，函数体节点数 136
    - 调用: __init__, super, _normalize_allowed_users, get, lstrip, str
  #### `m` `_add_reaction(self, channel_id: str, timestamp: str, emoji: str) -> None`  L240
    - _文档首行_（仅供参考）: Add an emoji reaction to a message (best-effort, non-blocking).
    - 分支数 1，函数体节点数 39；return: None
    - 调用: _add_reaction_with_client
  #### `m` `_send_running_reply(self, channel_id: str, thread_ts: str) -> None`  L246
    - _文档首行_（仅供参考）: Send a 'Working on it......' reply in the thread (called from SDK thread).
    - 分支数 2，函数体节点数 60；return: None
    - 调用: chat_postMessage, info, exception
  #### `m` `_on_socket_event(self, client, req) -> None`  L260
    - _文档首行_（仅供参考）: Called by slack-sdk for each Socket Mode event.
    - 分支数 5，函数体节点数 188；return: None
    - 调用: _SocketModeResponse, send_socket_mode_response, next, get, isinstance, _handle_message_event, exception
  #### `m` `_handle_message_event(self, event: dict, *, team_id: str | None) -> None`  L290
    - 分支数 9，函数体节点数 349；return: None
    - 调用: get, strip, _strip_leading_slack_bot_mention, _pending_connect_code, is_running, run_coroutine_threadsafe, _bind_connection_from_connect_code, str, debug, is_known_channel_command, _make_inbound, _add_reaction, _send_running_reply, publish_inbound, _publish_inbound_with_connection
  #### `⏵m` `async start(self) -> None`  L73
    - 分支数 5，函数体节点数 206；return: None
    - 调用: error, get, _initialize_operator_web_client, str, SocketModeClient, get_event_loop, append, subscribe_outbound, run_in_executor, info
  #### `⏵m` `async stop(self) -> None`  L116
    - 分支数 1，函数体节点数 48
    - 调用: unsubscribe_outbound, close, info
  #### `⏵m` `async send(self, msg: OutboundMessage, *, _max_retries: int) -> None`  L124
    - 分支数 6，函数体节点数 167；raise: bare raise；return: None
    - 调用: _get_web_client_for_message, convert, to_thread, _send_with_retry
  #### `⏵m` `async send_file(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L169
    - 分支数 3，函数体节点数 129；return: False, True
    - 调用: _get_web_client_for_message, str, to_thread, info, exception
  #### `⏵m` `async _initialize_operator_web_client(self, bot_token: str) -> None`  L193
    - 分支数 4，函数体节点数 124；return: None
    - 调用: _web_client_factory, to_thread, isinstance, get, getattr, callable, auth_get, warning
  - 反射: getattr (L201)
  #### `⏵m` `async _get_web_client_for_message(self, msg: OutboundMessage)`  L208
    - 分支数 4，函数体节点数 148；return: self._web_client, cached[1], web_client
    - 调用: get_credentials, get, _web_client_factory
  #### `⏵m` `async _publish_inbound_with_connection(self, inbound, *, team_id: str | None) -> None`  L358
    - 分支数 0，函数体节点数 37
    - 调用: _attach_connection_identity, publish_inbound
  #### `⏵m` `async _attach_connection_identity(self, inbound, *, team_id: str | None)`  L362
    - 分支数 0，函数体节点数 47；return: await attach_connection_identity(inbound, repo=self._connection_repo, provider='slack', workspace_id=workspace_id)
    - 调用: str, get, attach_connection_identity
  #### `⏵m` `async _bind_connection_from_connect_code(self, *, event: dict, team_id: str, code: str) -> bool`  L371
    - 分支数 3，函数体节点数 189；return: False, True
    - 调用: str, get, consume_oauth_state, _post_connection_reply, upsert_connection
  #### `⏵m` `async _post_connection_reply(self, channel_id: str, text: str, thread_ts: str | None) -> None`  L401
    - 分支数 3，函数体节点数 91；return: None
    - 调用: to_thread, exception

## 文件内调用关系
- `SlackChannel.__init__` -> __init__, _normalize_allowed_users
- `SlackChannel.start` -> _initialize_operator_web_client
- `SlackChannel.send` -> _get_web_client_for_message
- `SlackChannel.send_file` -> _get_web_client_for_message
- `SlackChannel._add_reaction` -> _add_reaction_with_client
- `SlackChannel._on_socket_event` -> _handle_message_event
- `SlackChannel._handle_message_event` -> _strip_leading_slack_bot_mention, _bind_connection_from_connect_code, _add_reaction, _send_running_reply, _publish_inbound_with_connection
- `SlackChannel._publish_inbound_with_connection` -> _attach_connection_identity
- `SlackChannel._bind_connection_from_connect_code` -> _post_connection_reply

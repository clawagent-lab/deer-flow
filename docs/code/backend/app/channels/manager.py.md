# `backend/app/channels/manager.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/manager.py`  ·  行数: 2014

**模块文档首行**（仅供参考）: ChannelManager — consumes inbound messages and dispatches them to the DeerFlow agent via Gateway.

## 模块概览
- 函数 35 个，类 6 个，模块级常量 22 个

## 依赖（import）
- 模块: asyncio, logging, mimetypes, re, time, httpx
- `__future__` -> annotations
- `collections` -> OrderedDict
- `collections.abc` -> Awaitable, Callable, Mapping
- `dataclasses` -> dataclass
- `pathlib` -> Path
- `typing` -> Any
- `urllib.parse` -> quote
- `langgraph_sdk.errors` -> ConflictError
- `app.channels` -> _feishu_run_policy
- `app.channels.commands` -> KNOWN_CHANNEL_COMMANDS
- `app.channels.message_bus` -> PENDING_CLARIFICATION_METADATA_KEY, InboundMessage, InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment
- `app.channels.run_policy` -> CHANNEL_RUN_POLICY, ChannelRunPolicy
- `app.channels.store` -> ChannelStore
- `app.gateway.csrf_middleware` -> CSRF_COOKIE_NAME, CSRF_HEADER_NAME, generate_csrf_token
- `app.gateway.github` -> _github_run_policy
- `app.gateway.internal_auth` -> create_internal_auth_headers
- `deerflow.config.agents_config` -> load_agent_config
- `deerflow.config.paths` -> make_safe_user_id
- `deerflow.runtime.goal` -> parse_goal_command
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.skills.slash` -> parse_slash_skill_reference
- `deerflow.skills.storage` -> get_or_new_skill_storage
- `deerflow.skills.storage.skill_storage` -> SkillStorage
- `deerflow.utils.messages` -> ORIGINAL_USER_CONTENT_KEY

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_LANGGRAPH_URL` = 'http://localhost:8001/api'
- `DEFAULT_GATEWAY_URL` = 'http://localhost:8001'
- `DEFAULT_ASSISTANT_ID` = 'lead_agent'
- `CUSTOM_AGENT_NAME_PATTERN` = re.compile('^[A-Za-z0-9-]+$')
- `DEFAULT_RUN_CONFIG` = {'recursion_limit': 100}
- `DEFAULT_RUN_CONTEXT` = {'thinking_enabled': True, 'is_plan_mode': False, 'subage...
- `STREAM_UPDATE_MIN_INTERVAL_SECONDS` = 1.0
- `STREAM_UPDATE_MIN_CHARS` = 60
- `STREAM_MODES` = ['messages-tuple', 'values']
- `MESSAGE_STREAM_EVENTS` = ('messages-tuple', 'messages')
- `THREAD_BUSY_MESSAGE` = 'This conversation is already processing another request....
- `BOUND_IDENTITY_REQUIRED_MESSAGE` = 'Connect this channel from DeerFlow Settings, complete th...
- `BOUND_IDENTITY_UNAVAILABLE_MESSAGE` = 'Channel connection verification is temporarily unavailab...
- `INBOUND_DEDUPE_TTL_SECONDS` = 10 * 60
- `INBOUND_DEDUPE_MAX_ENTRIES` = 4096
- `INBOUND_DEDUPE_METADATA_KEYS` = ('event_id', 'message_id', 'msg_id')
- `CHANNEL_CAPABILITIES` = {'dingtalk': {'supports_streaming': False}, 'discord': {'...
- `InboundFileReader` = Callable[[dict[str, Any], httpx.AsyncClient], Awaitable[b...
- `_METADATA_DROP_KEYS` = frozenset({'raw_message', 'ref_msg'})
- `INBOUND_FILE_READERS` = {}
- `_OUTPUTS_VIRTUAL_PREFIX` = '/mnt/user-data/outputs/'

## 函数
#### `ƒ` `_slim_metadata(meta: dict[str, Any]) -> dict[str, Any]`  L98
  - _文档首行_（仅供参考）: Return a shallow copy of *meta* with known-large keys removed.
  - 分支数 0，函数体节点数 49；return: {k: v for k, v in meta.items() if k not in _METADATA_DROP_KEYS}
  - 调用: items

#### `ƒ` `register_inbound_file_reader(channel_name: str, reader: InboundFileReader) -> None`  L106
  - 分支数 0，函数体节点数 18

#### `⏵ƒ` `async _read_http_inbound_file(file_info: dict[str, Any], client: httpx.AsyncClient) -> bytes | None`  L110
  - 分支数 1，函数体节点数 72；return: None, resp.content
  - 调用: get, isinstance, raise_for_status
  - 网络调用: get (L115)

#### `⏵ƒ` `async _read_wecom_inbound_file(file_info: dict[str, Any], client: httpx.AsyncClient) -> bytes | None`  L120
  - 分支数 3，函数体节点数 95；return: None, data, decrypt_file(data, aeskey)
  - 调用: _read_http_inbound_file, isinstance, get, exception, decrypt_file

#### `⏵ƒ` `async _read_wechat_inbound_file(file_info: dict[str, Any], client: httpx.AsyncClient) -> bytes | None`  L138
  - 分支数 3，函数体节点数 113；return: await asyncio.to_thread(Path(raw_path).read_bytes), None, await _read_http_inbound_file({'url': full_url}, client)
  - 调用: get, isinstance, strip, to_thread, Path, exception, _read_http_inbound_file

#### `ƒ` `_is_thread_busy_error(exc: BaseException | None) -> bool`  L193
  - 分支数 2，函数体节点数 37；return: False, True, 'already running a task' in str(exc)
  - 调用: isinstance, str

#### `ƒ` `_as_dict(value: Any) -> dict[str, Any]`  L201
  - 分支数 0，函数体节点数 30；return: dict(value) if isinstance(value, Mapping) else {}
  - 调用: isinstance, dict

#### `ƒ` `_merge_dicts(*layers) -> dict[str, Any]`  L205
  - 分支数 2，函数体节点数 53；可变参数（*args/**kwargs）；return: merged
  - 调用: isinstance, update

#### `ƒ` `_normalize_custom_agent_name(raw_value: str) -> str`  L213
  - _文档首行_（仅供参考）: Normalize legacy channel assistant IDs into valid custom agent names.
  - 分支数 2，函数体节点数 58；raise: InvalidChannelSessionConfigError("Channel session assistant_id is empty. Use 'lead_agent' or a valid custom agent name."), InvalidChannelSessionConfigError(f"Invalid channel session assistant_id {raw_value!r}. Use 'lead_agent' or a custom agent name containing only letters, digits, and hyphens.")；return: normalized
  - 调用: replace, lower, strip, InvalidChannelSessionConfigError, fullmatch
  - 文件IO: replace (L215)

#### `ƒ` `_extract_response_text(result: dict | list) -> str`  L223
  - _文档首行_（仅供参考）: Extract the last AI message text from a LangGraph runs.wait result.
  - 分支数 15，函数体节点数 245；return: '', content, text
  - 调用: isinstance, get, reversed, _is_hidden_human_control_message, append, join

#### `ƒ` `_messages_from_result(result: dict | list) -> list[Any]`  L279
  - 分支数 3，函数体节点数 59；return: result, messages, []
  - 调用: isinstance, get

#### `ƒ` `_current_turn_messages(result: dict | list) -> list[dict[str, Any]]`  L289
  - 分支数 3，函数体节点数 97；return: current_turn
  - 调用: _messages_from_result, reversed, isinstance, get, append, reverse

#### `ƒ` `_has_current_turn_clarification(result: dict | list) -> bool`  L302
  - _文档首行_（仅供参考）: Return True only when the current turn's final result is clarification.
  - 分支数 7，函数体节点数 93；return: msg.get('name') == 'ask_clarification', False
  - 调用: reversed, _current_turn_messages, get, isinstance

#### `ƒ` `_response_metadata(base_metadata: dict[str, Any], *, pending_clarification: bool) -> dict[str, Any]`  L320
  - 分支数 1，函数体节点数 49；return: metadata
  - 调用: _slim_metadata

#### `ƒ` `_thread_channel_metadata(msg: InboundMessage) -> dict[str, Any]`  L327
  - 分支数 3，函数体节点数 91；return: {'channel_source': channel_source}

#### `ƒ` `_extract_text_content(content: Any) -> str`  L343
  - _文档首行_（仅供参考）: Extract text from a streaming payload content field.
  - 分支数 10，函数体节点数 163；return: content, ''.join(parts), value, ''
  - 调用: isinstance, append, get, join

#### `ƒ` `_merge_stream_text(existing: str, chunk: str) -> str`  L369
  - _文档首行_（仅供参考）: Merge either delta text or cumulative text into a single snapshot.
  - 分支数 3，函数体节点数 60；return: existing, chunk, existing + chunk
  - 调用: len, startswith

#### `ƒ` `_extract_stream_message_id(payload: Any, metadata: Any) -> str | None`  L387
  - _文档首行_（仅供参考）: Best-effort extraction of the streamed AI message identifier.
  - 分支数 5，函数体节点数 94；return: value, None
  - 调用: isinstance, append, get

#### `ƒ` `_accumulate_stream_text(buffers: dict[str, str], current_message_id: str | None, event_data: Any) -> tuple[str | None, str | None]`  L403
  - _文档首行_（仅供参考）: Convert a ``messages-tuple`` event into the latest displayable AI text.
  - 分支数 8，函数体节点数 284；return: (buffers[message_id], message_id), (None, current_message_id)
  - 调用: isinstance, len, _merge_stream_text, get, lower, str, _extract_text_content, _extract_stream_message_id

#### `ƒ` `_extract_artifacts(result: dict | list) -> list[str]`  L440
  - _文档首行_（仅供参考）: Extract artifact paths from the last AI response cycle only.
  - 分支数 10，函数体节点数 193；return: [], artifacts
  - 调用: isinstance, get, reversed, _is_hidden_human_control_message, extend

#### `ƒ` `_is_hidden_human_control_message(msg: Mapping[str, Any]) -> bool`  L475
  - _文档首行_（仅供参考）: Return whether a human message is an internal control message hidden from UI.
  - 分支数 2，函数体节点数 60；return: False, additional_kwargs.get('hide_from_ui') is True
  - 调用: get, isinstance

#### `ƒ` `_format_artifact_text(artifacts: list[str]) -> str`  L487
  - _文档首行_（仅供参考）: Format artifact paths into a human-readable text block listing filenames.
  - 分支数 1，函数体节点数 59；return: f'Created File: 📎 {filenames[0]}', 'Created Files: 📎 ' + '、'.join(filenames)
  - 调用: basename, len, join

#### `ƒ` `_unknown_command_reply(command: str | None) -> str`  L500
  - 分支数 1，函数体节点数 42；return: f'Unknown command: /{command}. Available commands: {available}', f'Unknown command. Available commands: {available}'
  - 调用: join, sorted

#### `ƒ` `_human_input_message(content: str, *, original_content: str | None) -> dict[str, Any]`  L507
  - 分支数 1，函数体节点数 69；return: message

#### `ƒ` `_auth_disabled_owner_user_id() -> str | None`  L514
  - 分支数 1，函数体节点数 33；return: None, AUTH_DISABLED_USER_ID if is_auth_disabled() else None
  - 调用: debug, is_auth_disabled

#### `ƒ` `_effective_owner_user_id(msg: InboundMessage) -> str | None`  L523
  - 分支数 0，函数体节点数 20；return: _auth_disabled_owner_user_id() or msg.owner_user_id
  - 调用: _auth_disabled_owner_user_id

#### `ƒ` `_apply_effective_owner(msg: InboundMessage) -> InboundMessage`  L527
  - 分支数 1，函数体节点数 28；return: msg
  - 调用: _effective_owner_user_id

#### `ƒ` `_owner_headers(msg: InboundMessage) -> dict[str, str] | None`  L534
  - 分支数 1，函数体节点数 40；return: None, create_internal_auth_headers(owner_user_id=owner_user_id)
  - 调用: _effective_owner_user_id, create_internal_auth_headers

#### `ƒ` `_safe_user_id_for_run(raw_user_id: str) -> str`  L541
  - 分支数 1，函数体节点数 35；return: get_paths().prepare_user_dir_for_raw_id(raw_user_id), make_safe_user_id(raw_user_id)
  - 调用: prepare_user_dir_for_raw_id, get_paths, exception, make_safe_user_id

#### `ƒ` `_channel_storage_user_id(msg: InboundMessage) -> str | None`  L551
  - _文档首行_（仅供参考）: Resolve the canonical DeerFlow user id for a channel-triggered message.
  - 分支数 2，函数体节点数 44；return: _safe_user_id_for_run(owner_user_id), _safe_user_id_for_run(msg.user_id), None
  - 调用: _effective_owner_user_id, _safe_user_id_for_run

#### `ƒ` `_resolve_slash_skill_command(text: str, available_skills: set[str] | None, storage: SkillStorage | Callable[[], SkillStorage] | None) -> _SlashSkillCommandResolution | None`  L579
  - 分支数 5，函数体节点数 191；raise: SlashSkillCommandResolutionError('Failed to resolve slash skill command. Please check the skill configuration.')；return: None, _SlashSkillCommandResolution(failure_message=f'Skill `/{reference.name}` is installed but disabled. Enable it before using slash activation.'), _SlashSkillCommandResolution(failure_message=f'Skill `/{reference.name}` is not available for this agent.'), _SlashSkillCommandResolution(route_to_chat=True)
  - 调用: parse_slash_skill_reference, callable, storage, get_or_new_skill_storage, load_skills, next, _SlashSkillCommandResolution, exception, SlashSkillCommandResolutionError

#### `ƒ` `_resolve_attachments(thread_id: str, artifacts: list[str], *, user_id: str | None) -> list[ResolvedAttachment]`  L605
  - _文档首行_（仅供参考）: Resolve virtual artifact paths to host filesystem paths with metadata.
  - 分支数 5，函数体节点数 244；return: attachments
  - 调用: get_paths, get_effective_user_id, resolve, sandbox_outputs_dir, startswith, warning, resolve_virtual_path, relative_to, is_file, guess_type, str, append, ResolvedAttachment, stat
  - 文件IO: stat (L646)

#### `ƒ` `_prepare_artifact_delivery(thread_id: str, response_text: str, artifacts: list[str], *, user_id: str | None) -> tuple[str, list[ResolvedAttachment]]`  L655
  - _文档首行_（仅供参考）: Resolve attachments and append filename fallbacks to the text response.
  - 分支数 3，函数体节点数 175；return: (response_text, attachments)
  - 调用: _resolve_attachments, _format_artifact_text

#### `⏵ƒ` `async _ingest_inbound_files(thread_id: str, msg: InboundMessage, *, user_id: str | None) -> list[dict[str, Any]]`  L684
  - 分支数 10，函数体节点数 455；return: [], (target, existing), created
  - 调用: ensure_uploads_dir, iterdir, is_file, to_thread, get, AsyncClient, Timeout, enumerate, isinstance, file_reader, exception, warning, claim_unique_filename, normalize_filename, append, len
  - 文件IO: iterdir (L700)

#### `ƒ` `_format_uploaded_files_block(files: list[dict[str, Any]]) -> str`  L771
  - 分支数 2，函数体节点数 210；return: '\n'.join(lines)
  - 调用: append, get, int, bool, join

## 类
### 类 `InvalidChannelSessionConfigError`  L158
- 继承: ValueError
- _文档首行_: Raised when IM channel session overrides contain invalid agent config.

### 类 `SlashSkillCommandResolutionError`  L162
- 继承: RuntimeError
- _文档首行_: Raised when IM slash-skill command resolution cannot complete safely.

### 类 `_SlashSkillCommandResolution`  L167  @dataclass(...)
- 类/实例变量:
  - `route_to_chat` = False
  - `failure_message` = None

### 类 `_BoundIdentityRejection`  L173  @dataclass(...)
- 类/实例变量:
  - `message` = BOUND_IDENTITY_REQUIRED_MESSAGE
  - `outbound_connection_id` = None
  - `outbound_owner_user_id` = None

### 类 `_SerializedThreadRunState`  L186  @dataclass(...)
- _文档首行_: Per-thread lock state for channels that queue same-thread turns.
- 类/实例变量:
  - `lock` = <annotated>
  - `waiters` = 0

### 类 `ChannelManager`  L798
- _文档首行_: Core dispatcher that bridges IM channels to the DeerFlow agent.
- 方法:
  #### `st` `_channel_supports_streaming(channel_name: str) -> bool`    @staticmethod  L849
    - 分支数 2，函数体节点数 55；return: channel.supports_streaming, CHANNEL_CAPABILITIES.get(channel_name, {}).get('supports_streaming', False)
    - 调用: get_channel_service, get_channel, get
  #### `st` `_inbound_dedupe_key(msg: InboundMessage) -> tuple[str, str, str, str] | None`    @staticmethod  L1151
    - 分支数 8，函数体节点数 181；return: None, (msg.channel_name, str(workspace_id), msg.chat_id, message_id)
    - 调用: get, str, isinstance
  #### `st` `_log_task_error(task: asyncio.Task) -> None`    @staticmethod  L1220
    - _文档首行_（仅供参考）: Surface unhandled exceptions from background tasks.
    - 分支数 2，函数体节点数 42；return: None
    - 调用: cancelled, exception, error
  #### `m` `__init__(self, bus: MessageBus, store: ChannelStore, *, max_concurrency: int, langgraph_url: str, gateway_url: str, assistant_id: str, default_session: dict[str, Any] | None, channel_sessions: dict[str, Any] | None, connection_repo: Any | None, require_bound_identity: bool) -> None`  L806
    - 分支数 0，函数体节点数 305
    - 调用: _as_dict, dict, set, generate_csrf_token, OrderedDict
  #### `m` `_resolve_session_layer(self, msg: InboundMessage) -> tuple[dict[str, Any], dict[str, Any]]`  L859
    - 分支数 0，函数体节点数 83；return: (channel_layer, user_layer)
    - 调用: _as_dict, get
  #### `m` `_begin_serialized_thread_run(self, *, channel_name: str, thread_id: str) -> tuple[_SerializedThreadRunState | None, bool]`  L865
    - 分支数 2，函数体节点数 125；return: (None, False), (state, queued)
    - 调用: get, _SerializedThreadRunState, Lock, locked
  #### `m` `_finish_serialized_thread_run(self, *, channel_name: str, thread_id: str, state: _SerializedThreadRunState | None, lock_acquired: bool) -> None`  L884
    - 分支数 3，函数体节点数 78；return: None
    - 调用: release, locked, pop
  #### `m` `_resolve_run_params(self, msg: InboundMessage, thread_id: str) -> tuple[str, dict[str, Any], dict[str, Any]]`  L916
    - 分支数 8，函数体节点数 482；return: (assistant_id, run_config, run_context)
    - 调用: _resolve_session_layer, isinstance, get, strip, _merge_dicts, dict, _channel_storage_user_id, setdefault, _normalize_custom_agent_name, max
  #### `m` `_resolve_available_skill_names(self, msg: InboundMessage) -> set[str] | None`  L1055
    - 分支数 3，函数体节点数 139；return: {'bootstrap'}, None, set(agent_config.skills)
    - 调用: get_thread_id, _resolve_run_params, get, isinstance, strip, load_agent_config, _normalize_custom_agent_name, set
  #### `m` `_get_client(self)`  L1076
    - _文档首行_（仅供参考）: Return the ``langgraph_sdk`` async client, creating it on first use.
    - 分支数 1，函数体节点数 55；return: self._client
    - 调用: get_client, create_internal_auth_headers
  #### `m` `_get_skill_storage(self) -> SkillStorage`  L1091
    - 分支数 1，函数体节点数 26；return: self._skill_storage
    - 调用: get_or_new_skill_storage
  #### `m` `_is_duplicate_inbound(self, msg: InboundMessage) -> bool`  L1178
    - 分支数 5，函数体节点数 149；return: False, True
    - 调用: _inbound_dedupe_key, monotonic, next, iter, items, popitem, len, info
  #### `m` `_release_inbound_dedupe_key(self, msg: InboundMessage) -> None`  L1207
    - _文档首行_（仅供参考）: Drop a recorded dedupe key so a provider redelivery can be reprocessed.
    - 分支数 1，函数体节点数 36
    - 调用: _inbound_dedupe_key, pop
  #### `⏵m` `async _publish_progress_update(self, msg: InboundMessage, thread_id: str, text: str) -> None`  L901
    - 分支数 0，函数体节点数 66
    - 调用: publish_outbound, OutboundMessage, _response_metadata
  #### `⏵m` `async _apply_channel_policy(self, msg: InboundMessage, run_context: dict[str, Any]) -> ChannelRunPolicy | None`  L1012
    - _文档首行_（仅供参考）: Apply per-channel run policy that needs ``run_context`` access.
    - 分支数 4，函数体节点数 97；return: None, policy
    - 调用: get, credentials_provider, warning
  #### `⏵m` `async start(self) -> None`  L1098
    - _文档首行_（仅供参考）: Start the dispatch loop.
    - 分支数 1，函数体节点数 58；return: None
    - 调用: Semaphore, create_task, _dispatch_loop, info
  #### `⏵m` `async stop(self) -> None`  L1107
    - _文档首行_（仅供参考）: Stop the dispatch loop.
    - 分支数 2，函数体节点数 51
    - 调用: cancel, info
  #### `⏵m` `async _dispatch_loop(self) -> None`  L1121
    - 分支数 3，函数体节点数 117
    - 调用: info, wait_for, get_inbound, _is_duplicate_inbound, len, create_task, _handle_message, add_done_callback
  #### `⏵m` `async _handle_message(self, msg: InboundMessage) -> None`  L1228
    - 分支数 5，函数体节点数 202；return: None
    - 调用: _apply_effective_owner, _get_bound_identity_rejection, _reject_unbound_channel_message, _handle_command, _handle_chat, warning, _send_error, str, exception, _release_inbound_dedupe_key
  #### `⏵m` `async _get_bound_identity_rejection(self, msg: InboundMessage) -> _BoundIdentityRejection | None`  L1277
    - _文档首行_（仅供参考）: Return None when *msg* may proceed; otherwise return rejection routing hints.
    - 分支数 7，函数体节点数 192；return: None, _BoundIdentityRejection(), _BoundIdentityRejection(message=BOUND_IDENTITY_UNAVAILABLE_MESSAGE), _BoundIdentityRejection(outbound_connection_id=connection_id, outbound_owner_user_id=owner_user_id)
    - 调用: get, _auth_disabled_owner_user_id, bool, _BoundIdentityRejection, find_connection_by_external_identity
  - 网络调用: get (L1319), get (L1320)
  #### `⏵m` `async _reject_unbound_channel_message(self, msg: InboundMessage, *, bound_identity_rejection: _BoundIdentityRejection) -> None`  L1325
    - 分支数 0，函数体节点数 82
    - 调用: info, OutboundMessage, _slim_metadata, publish_outbound
  #### `⏵m` `async _lookup_thread_id(self, msg: InboundMessage) -> str | None`  L1348
    - 分支数 1，函数体节点数 67；return: await self._connection_repo.get_thread_id(msg.connection_id, msg.chat_id, msg.topic_id), self.store.get_thread_id(msg.channel_name, msg.chat_id, topic_id=msg.topic_id)
    - 调用: get_thread_id
  #### `⏵m` `async _store_thread_id(self, msg: InboundMessage, thread_id: str) -> None`  L1357
    - 分支数 1，函数体节点数 94；return: None
    - 调用: set_thread_id
  #### `⏵m` `async _create_thread(self, client, msg: InboundMessage) -> str`  L1377
    - _文档首行_（仅供参考）: Create a new thread through Gateway and store the mapping.
    - 分支数 6，函数体节点数 268；raise: bare raise；return: preferred_thread_id, thread_id
    - 调用: _thread_channel_metadata, _owner_headers, isinstance, get, create, warning, info, _store_thread_id
  #### `⏵m` `async _get_or_create_thread(self, client, msg: InboundMessage) -> tuple[str, bool]`  L1442
    - _文档首行_（仅供参考）: Return ``(thread_id, created)``, creating a thread only if needed.
    - 分支数 4，函数体节点数 123；return: (thread_id, False), (await self._create_thread(client, msg), True)
    - 调用: _lookup_thread_id, setdefault, Lock, _create_thread, pop
  #### `⏵m` `async _update_thread_channel_metadata(self, client, msg: InboundMessage, thread_id: str) -> None`  L1472
    - _文档首行_（仅供参考）: Best-effort source metadata backfill for existing IM-created threads.
    - 分支数 4，函数体节点数 119；return: None
    - 调用: _thread_channel_metadata, _owner_headers, update, debug, len, clear, add
  #### `⏵m` `async _handle_chat(self, msg: InboundMessage, extra_context: dict[str, Any] | None, *, bound_identity_checked: bool) -> None`  L1491
    - 分支数 6，函数体节点数 237；return: None
    - 调用: _get_bound_identity_rejection, _reject_unbound_channel_message, _get_client, _channel_storage_user_id, _get_or_create_thread, info, _update_thread_channel_metadata, _begin_serialized_thread_run, _publish_progress_update, acquire, _handle_chat_on_thread, _finish_serialized_thread_run
  #### `⏵m` `async _handle_chat_on_thread(self, client, msg: InboundMessage, thread_id: str, *, extra_context: dict[str, Any] | None, storage_user_id: str | None) -> None`  L1550
    - 分支数 13，函数体节点数 615；raise: bare raise；return: None
    - 调用: _channel_storage_user_id, _resolve_run_params, _apply_channel_policy, get_channel_service, get_channel, info, len, receive_file, update, _ingest_inbound_files, strip, _format_uploaded_files_block, _human_input_message, _channel_supports_streaming, _handle_streaming_chat, _owner_headers, create, _is_thread_busy_error, warning, _send_error（+9）
  #### `⏵m` `async _handle_streaming_chat(self, client, msg: InboundMessage, thread_id: str, assistant_id: str, run_config: dict[str, Any], run_context: dict[str, Any], human_message: dict[str, Any], storage_user_id: str | None) -> None`  L1692
    - 分支数 16，函数体节点数 682
    - 调用: info, len, list, _owner_headers, stream, getattr, _accumulate_stream_text, isinstance, _has_current_turn_clarification, _extract_response_text, monotonic, publish_outbound, OutboundMessage, _response_metadata, _is_thread_busy_error, warning, exception, _extract_artifacts, _prepare_artifact_delivery, _format_artifact_text
  - 反射: getattr (L1729), getattr (L1730)
  #### `⏵m` `async _handle_command(self, msg: InboundMessage) -> None`  L1824
    - 分支数 14，函数体节点数 537；return: None
    - 调用: _get_bound_identity_rejection, _reject_unbound_channel_message, strip, split, _unknown_command_reply, removeprefix, lower, startswith, len, _dc_replace, _handle_chat, _get_client, _create_thread, _lookup_thread_id, _fetch_gateway, _handle_goal_command, to_thread, _resolve_slash_skill_command, _resolve_available_skill_names, OutboundMessage（+2）
  #### `⏵m` `async _goal_request(self, method: str, thread_id: str, *, headers: dict[str, str], json: dict[str, Any] | None) -> dict[str, Any]`  L1917
    - 分支数 2，函数体节点数 141；return: response.json() or {}
    - 调用: AsyncClient, getattr, lower, request, quote, raise_for_status, json
  - 反射: getattr (L1926)
  #### `⏵m` `async _handle_goal_command(self, msg: InboundMessage, args: str) -> str | None`  L1934
    - 分支数 8，函数体节点数 237；return: 'No active goal.', 'Failed to fetch goal information.', f"Goal: {goal.get('objective')}" if goal else 'No active goal.', 'Goal cleared.', 'Failed to clear goal.', 'Failed to set goal.', None
    - 调用: parse_goal_command, _lookup_thread_id, _owner_headers, create_internal_auth_headers, get, _goal_request, exception, _create_thread, _get_client, _dc_replace, _handle_chat
  #### `⏵m` `async _fetch_gateway(self, path: str, kind: str, *, msg: InboundMessage | None) -> str`  L1974
    - _文档首行_（仅供参考）: Fetch data from the Gateway API for command responses.
    - 分支数 4，函数体节点数 190；return: f'Failed to fetch {kind} information.', 'Available models:\n' + '\n'.join((f'• {n}' for n in names)) if names else 'No models configured.', f'Memory contains {len(facts)} fact(s).', str(data)
    - 调用: _owner_headers, AsyncClient, get, create_internal_auth_headers, raise_for_status, json, exception, join, len, str
  - 网络调用: get (L1981)
  #### `⏵m` `async _send_error(self, msg: InboundMessage, error_text: str) -> None`  L2002
    - 分支数 0，函数体节点数 75
    - 调用: OutboundMessage, _lookup_thread_id, _slim_metadata, publish_outbound

## 文件内调用关系
- `_read_wecom_inbound_file` -> _read_http_inbound_file
- `_read_wechat_inbound_file` -> _read_http_inbound_file
- `_extract_response_text` -> _is_hidden_human_control_message
- `_current_turn_messages` -> _messages_from_result
- `_has_current_turn_clarification` -> _current_turn_messages
- `_response_metadata` -> _slim_metadata
- `_accumulate_stream_text` -> _merge_stream_text, _extract_text_content, _extract_stream_message_id
- `_extract_artifacts` -> _is_hidden_human_control_message
- `_effective_owner_user_id` -> _auth_disabled_owner_user_id
- `_apply_effective_owner` -> _effective_owner_user_id
- `_owner_headers` -> _effective_owner_user_id
- `_channel_storage_user_id` -> _effective_owner_user_id, _safe_user_id_for_run
- `_prepare_artifact_delivery` -> _resolve_attachments, _format_artifact_text
- `ChannelManager.__init__` -> _as_dict
- `ChannelManager._resolve_session_layer` -> _as_dict
- `ChannelManager._publish_progress_update` -> _response_metadata
- `ChannelManager._resolve_run_params` -> _resolve_session_layer, _merge_dicts, _channel_storage_user_id, _normalize_custom_agent_name
- `ChannelManager._resolve_available_skill_names` -> _resolve_run_params, _normalize_custom_agent_name
- `ChannelManager.start` -> _dispatch_loop
- `ChannelManager._dispatch_loop` -> _is_duplicate_inbound, _handle_message
- `ChannelManager._is_duplicate_inbound` -> _inbound_dedupe_key
- `ChannelManager._release_inbound_dedupe_key` -> _inbound_dedupe_key
- `ChannelManager._handle_message` -> _apply_effective_owner, _get_bound_identity_rejection, _reject_unbound_channel_message, _handle_command, _handle_chat, _send_error, _release_inbound_dedupe_key
- `ChannelManager._get_bound_identity_rejection` -> _auth_disabled_owner_user_id
- `ChannelManager._reject_unbound_channel_message` -> _slim_metadata
- `ChannelManager._create_thread` -> _thread_channel_metadata, _owner_headers, _store_thread_id
- `ChannelManager._get_or_create_thread` -> _lookup_thread_id, _create_thread
- `ChannelManager._update_thread_channel_metadata` -> _thread_channel_metadata, _owner_headers
- `ChannelManager._handle_chat` -> _get_bound_identity_rejection, _reject_unbound_channel_message, _get_client, _channel_storage_user_id, _get_or_create_thread, _update_thread_channel_metadata, _begin_serialized_thread_run, _publish_progress_update, _handle_chat_on_thread, _finish_serialized_thread_run
- `ChannelManager._handle_chat_on_thread` -> _channel_storage_user_id, _resolve_run_params, _apply_channel_policy, _ingest_inbound_files, _format_uploaded_files_block, _human_input_message, _channel_supports_streaming, _handle_streaming_chat, _owner_headers, _is_thread_busy_error, _send_error, _extract_response_text, _has_current_turn_clarification, _extract_artifacts, _prepare_artifact_delivery, _format_artifact_text, _response_metadata
- `ChannelManager._handle_streaming_chat` -> _owner_headers, _accumulate_stream_text, _has_current_turn_clarification, _extract_response_text, _response_metadata, _is_thread_busy_error, _extract_artifacts, _prepare_artifact_delivery, _format_artifact_text
- `ChannelManager._handle_command` -> _get_bound_identity_rejection, _reject_unbound_channel_message, _unknown_command_reply, _handle_chat, _get_client, _create_thread, _lookup_thread_id, _fetch_gateway, _handle_goal_command, _resolve_slash_skill_command, _resolve_available_skill_names, _slim_metadata
- `ChannelManager._handle_goal_command` -> _lookup_thread_id, _owner_headers, _goal_request, _create_thread, _get_client, _handle_chat
- `ChannelManager._fetch_gateway` -> _owner_headers
- `ChannelManager._send_error` -> _lookup_thread_id, _slim_metadata

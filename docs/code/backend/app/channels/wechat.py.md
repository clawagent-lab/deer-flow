# `backend/app/channels/wechat.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/wechat.py`  ·  行数: 1478

**模块文档首行**（仅供参考）: WeChat channel — connects to iLink via long-polling.

## 模块概览
- 函数 11 个，类 3 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, base64, binascii, hashlib, json, logging, math, mimetypes, secrets, tempfile, time, httpx
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `enum` -> IntEnum
- `pathlib` -> Path
- `typing` -> Any
- `urllib.parse` -> quote
- `cryptography.hazmat.primitives` -> padding
- `cryptography.hazmat.primitives.ciphers` -> Cipher, algorithms, modes
- `app.channels.base` -> Channel
- `app.channels.commands` -> is_known_channel_command
- `app.channels.connection_identity` -> attach_connection_identity
- `app.channels.message_bus` -> InboundMessage, InboundMessageType, MessageBus, OutboundMessage, ResolvedAttachment

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_build_ilink_client_version(version: str) -> str`  L50
  - 分支数 2，函数体节点数 112；return: 0, max(0, min(int(parts[index] or 0), 255)), str(major << 16 | minor << 8 | patch)
  - 调用: strip, split, len, max, min, int, _part, str

#### `ƒ` `_build_wechat_uin() -> str`  L67
  - 分支数 0，函数体节点数 27；return: base64.b64encode(str(secrets.randbits(32)).encode('utf-8')).decode('utf-8')
  - 调用: decode, b64encode, encode, str, randbits

#### `ƒ` `_md5_hex(content: bytes) -> str`  L71
  - 分支数 0，函数体节点数 18；return: hashlib.md5(content).hexdigest()
  - 调用: hexdigest, md5

#### `ƒ` `_encrypted_size_for_aes_128_ecb(plaintext_size: int) -> int`  L75
  - 分支数 1，函数体节点数 30；raise: ValueError('plaintext_size must be non-negative')；return: (plaintext_size // 16 + 1) * 16
  - 调用: ValueError

#### `ƒ` `_validate_aes_128_key(key: bytes) -> None`  L81
  - 分支数 1，函数体节点数 20；raise: ValueError('AES-128-ECB requires a 16-byte key')
  - 调用: len, ValueError

#### `ƒ` `_encrypt_aes_128_ecb(content: bytes, key: bytes) -> bytes`  L86
  - 分支数 0，函数体节点数 86；return: encryptor.update(padded) + encryptor.finalize()
  - 调用: _validate_aes_128_key, padder, PKCS7, update, finalize, Cipher, AES, ECB, encryptor

#### `ƒ` `_decrypt_aes_128_ecb(content: bytes, key: bytes) -> bytes`  L95
  - 分支数 0，函数体节点数 86；return: unpadder.update(padded) + unpadder.finalize()
  - 调用: _validate_aes_128_key, Cipher, AES, ECB, decryptor, update, finalize, unpadder, PKCS7

#### `ƒ` `_safe_media_filename(prefix: str, extension: str, message_id: str | None, index: int | None) -> str`  L104
  - 分支数 0，函数体节点数 93；return: f'{prefix}-{safe_msg}{suffix}{safe_ext}'
  - 调用: startswith, replace
  - 文件IO: replace (L106), replace (L106)

#### `ƒ` `_build_cdn_upload_url(cdn_base_url: str, upload_param: str, filekey: str) -> str`  L111
  - 分支数 0，函数体节点数 40；return: f"{cdn_base_url.rstrip('/')}/upload?encrypted_query_param={quote(upload_param, safe='')}&filekey={quote(filekey, safe='')}"
  - 调用: rstrip, quote

#### `ƒ` `_encode_outbound_media_aes_key(aes_key: bytes) -> str`  L115
  - 分支数 0，函数体节点数 26；return: base64.b64encode(aes_key.hex().encode('utf-8')).decode('utf-8')
  - 调用: decode, b64encode, encode, hex

#### `ƒ` `_detect_image_extension_and_mime(content: bytes) -> tuple[str, str] | None`  L119
  - 分支数 5，函数体节点数 103；return: ('.png', 'image/png'), ('.jpg', 'image/jpeg'), ('.gif', 'image/gif'), ('.webp', 'image/webp'), ('.bmp', 'image/bmp'), None
  - 调用: startswith, len

## 类
### 类 `MessageItemType`  L34
- 继承: IntEnum
- 类/实例变量:
  - `NONE` = 0
  - `TEXT` = 1
  - `IMAGE` = 2
  - `VOICE` = 3
  - `FILE` = 4
  - `VIDEO` = 5

### 类 `UploadMediaType`  L43
- 继承: IntEnum
- 类/实例变量:
  - `IMAGE` = 1
  - `VIDEO` = 2
  - `FILE` = 3
  - `VOICE` = 4

### 类 `WechatChannel`  L133
- 继承: Channel
- _文档首行_: WeChat iLink bot channel using long-polling.
- 类/实例变量:
  - `DEFAULT_BASE_URL` = 'https://ilinkai.weixin.qq.com'
  - `DEFAULT_CDN_BASE_URL` = 'https://novac2c.cdn.weixin.qq.com/c2c'
  - `DEFAULT_CHANNEL_VERSION` = '1.0'
  - `DEFAULT_POLLING_TIMEOUT` = 35.0
  - `DEFAULT_RETRY_DELAY` = 5.0
  - `DEFAULT_QRCODE_POLL_INTERVAL` = 2.0
  - `DEFAULT_QRCODE_POLL_TIMEOUT` = 180.0
  - `DEFAULT_QRCODE_BOT_TYPE` = 3
  - `DEFAULT_API_TIMEOUT` = 15.0
  - `DEFAULT_CONFIG_TIMEOUT` = 10.0
  - `DEFAULT_CDN_TIMEOUT` = 30.0
  - `DEFAULT_IMAGE_DOWNLOAD_DIRNAME` = 'downloads'
  - `DEFAULT_MAX_IMAGE_BYTES` = 20 * 1024 * 1024
  - `DEFAULT_MAX_OUTBOUND_IMAGE_BYTES` = 20 * 1024 * 1024
  - `DEFAULT_MAX_INBOUND_FILE_BYTES` = 50 * 1024 * 1024
  - `DEFAULT_MAX_OUTBOUND_FILE_BYTES` = 50 * 1024 * 1024
  - `DEFAULT_ALLOWED_FILE_EXTENSIONS` = frozenset({'.txt', '.md', '.pdf', '.csv', '.json', '.yaml...
  - `DEFAULT_ALLOWED_FILE_MIME_TYPES` = frozenset({'application/pdf', 'application/json', 'applic...
- 方法:
  #### `cls` `_parse_aes_key_candidate(cls, value: Any, *, prefer_hex: bool) -> bytes | None`    @classmethod  L1203
    - 分支数 9，函数体节点数 190；return: value, None, cls._parse_aes_key_candidate(bytes(value), prefer_hex=prefer_hex), key
    - 调用: isinstance, _validate_aes_128_key, _parse_aes_key_candidate, bytes, strip, fromhex, _decode_base64_aes_key, decoder, validator
  #### `cls` `_resolve_media_aes_key(cls, *payloads) -> bytes | None`    @classmethod  L1238
    - 分支数 8，函数体节点数 134；可变参数（*args/**kwargs）；return: key, None
    - 调用: isinstance, _parse_aes_key_candidate, get, _resolve_media_aes_key
  #### `st` `_extract_cdn_full_url(media: Mapping[str, Any] | None) -> str | None`    @staticmethod  L900
    - 分支数 1，函数体节点数 66；return: None, full_url.strip() if isinstance(full_url, str) and full_url.strip() else None
    - 调用: isinstance, get, strip
  #### `st` `_extract_upload_full_url(upload_data: Mapping[str, Any] | None) -> str | None`    @staticmethod  L907
    - 分支数 1，函数体节点数 66；return: None, upload_full_url.strip() if isinstance(upload_full_url, str) and upload_full_url.strip() else None
    - 调用: isinstance, get, strip
  #### `st` `_extract_upload_param(upload_data: Mapping[str, Any] | None) -> str | None`    @staticmethod  L914
    - 分支数 1，函数体节点数 66；return: None, upload_param.strip() if isinstance(upload_param, str) and upload_param.strip() else None
    - 调用: isinstance, get, strip
  #### `st` `_decode_base64_aes_key(value: str) -> bytes | None`    @staticmethod  L1161
    - 分支数 8，函数体节点数 192；return: None, decoded, key
    - 调用: strip, _validate_aes_128_key, decode, fromhex, len, b64decode, urlsafe_b64decode, _normalize_decoded, decoder
  #### `st` `_describe_media_key_state(*, item: Mapping[str, Any] | None, item_payload: Mapping[str, Any] | None, media: Mapping[str, Any] | None) -> dict[str, Any]`    @staticmethod  L1258
    - 分支数 5，函数体节点数 219；return: {}, details, {'item': _interesting(item), 'item_payload': _interesting(item_payload), 'media': _interesting(media)}
    - 调用: isinstance, get, len, strip, type, _interesting
  #### `st` `_extract_ref_message(raw_message: Mapping[str, Any]) -> dict[str, Any] | None`    @staticmethod  L1298
    - 分支数 4，函数体节点数 90；return: None, dict(ref_msg)
    - 调用: get, isinstance, dict
  #### `st` `_normalize_inbound_filename(raw_filename: Any, *, default_prefix: str, message_id: str, index: int) -> str`    @staticmethod  L1319
    - 分支数 2，函数体节点数 65；return: candidate, _safe_media_filename(default_prefix, '.bin', message_id=message_id, index=index)
    - 调用: isinstance, strip, Path, _safe_media_filename
  #### `st` `_extract_text(raw_message: dict[str, Any]) -> str`    @staticmethod  L1438
    - 分支数 4，函数体节点数 129；return: '\n'.join(parts)
    - 调用: get, isinstance, int, strip, append, join
  #### `st` `_resolve_state_dir(raw_state_dir: Any) -> Path | None`    @staticmethod  L1452
    - 分支数 1，函数体节点数 42；return: None, Path(raw_state_dir).expanduser()
    - 调用: isinstance, strip, expanduser, Path
  #### `st` `_coerce_float(value: Any, default: float) -> float`    @staticmethod  L1458
    - 分支数 1，函数体节点数 53；return: default, parsed if math.isfinite(parsed) and parsed > 0 else default
    - 调用: float, isfinite
  #### `st` `_coerce_int(value: Any, default: int) -> int`    @staticmethod  L1466
    - 分支数 1，函数体节点数 29；return: int(value), default
    - 调用: int
  #### `st` `_coerce_str_set(value: Any, default: frozenset[str]) -> set[str]`    @staticmethod  L1473
    - 分支数 1，函数体节点数 109；return: set(default), normalized or set(default)
    - 调用: isinstance, set, startswith, strip, str, lower
  #### `m` `__init__(self, bus: MessageBus, config: dict[str, Any]) -> None`  L222
    - 分支数 0，函数体节点数 619
    - 调用: __init__, super, Lock, rstrip, str, get, _coerce_float, bool, _coerce_int, strip, _coerce_str_set, _resolve_state_dir
  #### `m` `_resolve_context_token(self, msg: OutboundMessage) -> str | None`  L838
    - 分支数 2，函数体节点数 83；return: metadata_token.strip(), self._context_tokens_by_thread[msg.thread_ts], self._context_tokens_by_chat.get(msg.chat_id)
    - 调用: get, isinstance, strip
  #### `m` `_check_user(self, user_id: str) -> bool`  L846
    - 分支数 1，函数体节点数 26；return: True, user_id in self._allowed_users
  #### `m` `_current_longpoll_timeout_seconds(self) -> float`  L851
    - 分支数 1，函数体节点数 29；return: self._server_longpoll_timeout_seconds, self._polling_timeout
  #### `m` `_update_longpoll_timeout(self, data: Mapping[str, Any]) -> None`  L856
    - 分支数 4，函数体节点数 73；return: None
    - 调用: get, float
  #### `m` `_base_info(self) -> dict[str, str]`  L870
    - 分支数 0，函数体节点数 20；return: {'channel_version': self._channel_version}
  #### `m` `_common_headers(self) -> dict[str, str]`  L873
    - 分支数 2，函数体节点数 62；return: headers
    - 调用: _build_ilink_client_version, _build_wechat_uin
  #### `m` `_public_headers(self) -> dict[str, str]`  L884
    - 分支数 0，函数体节点数 22；return: {'Content-Type': 'application/json', **self._common_headers()}
    - 调用: _common_headers
  #### `m` `_auth_headers(self) -> dict[str, str]`  L890
    - 分支数 0，函数体节点数 37；return: headers
    - 调用: _common_headers
  #### `m` `_build_upload_request(self, *, filekey: str, media_type: UploadMediaType, to_user_id: str, plaintext: bytes, aes_key: bytes, thumb_plaintext: bytes | None, no_need_thumb: bool) -> dict[str, Any]`  L920
    - 分支数 2，函数体节点数 145；return: payload
    - 调用: _validate_aes_128_key, int, len, _md5_hex, _encrypted_size_for_aes_128_ecb, hex, update
  #### `m` `_build_outbound_image_item(self, upload_data: Mapping[str, Any], aes_key: bytes, *, ciphertext_size: int) -> dict[str, Any]`  L981
    - 分支数 1，函数体节点数 100；return: {'media': media, 'mid_size': ciphertext_size}
    - 调用: _encode_outbound_media_aes_key, get, isinstance, strip
  #### `m` `_build_outbound_file_item(self, upload_data: Mapping[str, Any], aes_key: bytes, filename: str, plaintext: bytes) -> dict[str, Any]`  L1002
    - 分支数 1，函数体节点数 113；return: {'media': media, 'file_name': filename, 'md5': _md5_hex(plaintext), 'len': str(len(plaintext))}
    - 调用: _encode_outbound_media_aes_key, get, isinstance, strip, _md5_hex, str, len
  #### `m` `_download_dir(self) -> Path | None`  L1023
    - 分支数 1，函数体节点数 28；return: None, self._state_dir / self.DEFAULT_IMAGE_DOWNLOAD_DIRNAME
  #### `m` `_stage_downloaded_file(self, filename: str, content: bytes) -> Path | None`  L1147
    - 分支数 2，函数体节点数 75；return: None, path
    - 调用: _download_dir, mkdir, write_bytes, exception
  - 文件IO: mkdir (L1152), write_bytes (L1154)
  #### `m` `_is_allowed_file_type(self, filename: str, mime_type: str) -> bool`  L1310
    - 分支数 2，函数体节点数 59；return: False, True, mime_type in self.DEFAULT_ALLOWED_FILE_MIME_TYPES
    - 调用: lower, Path, startswith
  #### `m` `_ensure_success(self, data: dict[str, Any], operation: str) -> None`  L1326
    - 分支数 1，函数体节点数 86；raise: RuntimeError(f'iLink {operation} failed: ret={ret} errcode={errcode} errmsg={errmsg}')；return: None
    - 调用: get, RuntimeError
  #### `m` `_load_state(self) -> None`  L1334
    - 分支数 3，函数体节点数 92；return: None
    - 调用: _load_auth_state, exists, loads, read_text, warning, get, isinstance
  - 文件IO: exists (L1336), read_text (L1339)
  #### `m` `_save_state(self) -> None`  L1347
    - 分支数 2，函数体节点数 66；return: None
    - 调用: mkdir, write_text, dumps, warning
  - 文件IO: mkdir (L1351), write_text (L1352)
  #### `m` `_load_auth_state(self) -> None`  L1356
    - 分支数 7，函数体节点数 165；return: None
    - 调用: exists, loads, read_text, warning, isinstance, dict, get, strip
  - 文件IO: exists (L1357), read_text (L1360)
  #### `m` `_save_auth_state(self, *, status: str, bot_token: str | None, ilink_bot_id: str | None, qrcode: str | None, qrcode_img_content: str | None) -> dict[str, Any]`  L1378
    - 分支数 10，函数体节点数 322；raise: bare raise；return: data
    - 调用: dict, int, time, pop, mkdir, NamedTemporaryFile, dump, close, replace, Path, unlink, warning, chmod, debug
  - 文件IO: mkdir (L1411), replace (L1420), unlink (L1423), chmod (L1432)
  #### `⏵m` `async start(self) -> None`  L265
    - 分支数 3，函数体节点数 125；return: None
    - 调用: to_thread, error, get_running_loop, _ensure_client, subscribe_outbound, create_task, _poll_loop, info
  #### `⏵m` `async stop(self) -> None`  L289
    - 分支数 3，函数体节点数 84
    - 调用: unsubscribe_outbound, cancel, aclose, info
  #### `⏵m` `async send(self, msg: OutboundMessage, *, _max_retries: int) -> None`  L307
    - 分支数 3，函数体节点数 106；return: None
    - 调用: strip, _ensure_authenticated, warning, _resolve_context_token, _send_text_message
  #### `⏵m` `async _send_text_message(self, *, chat_id: str, context_token: str, text: str, client_id_prefix: str, max_retries: int) -> None`  L329
    - 分支数 0，函数体节点数 124
    - 调用: int, time, token_hex, _base_info, _request_json, _ensure_success, _send_with_retry
  #### `⏵m` `async send_file(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L366
    - 分支数 1，函数体节点数 38；return: await self._send_image_attachment(msg, attachment), await self._send_file_attachment(msg, attachment)
    - 调用: _send_image_attachment, _send_file_attachment
  #### `⏵m` `async _send_image_attachment(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L371
    - 分支数 8，函数体节点数 450；return: False, True
    - 调用: warning, _ensure_authenticated, _resolve_context_token, to_thread, exception, token_bytes, _safe_media_filename, _build_upload_request, _request_json, _base_info, _ensure_success, _extract_upload_full_url, _extract_upload_param, _build_cdn_upload_url, _encrypt_aes_128_ecb, _upload_cdn_bytes, dict, _build_outbound_image_item, len, int（+1）
  #### `⏵m` `async _send_file_attachment(self, msg: OutboundMessage, attachment: ResolvedAttachment) -> bool`  L457
    - 分支数 9，函数体节点数 483；return: False, True
    - 调用: _is_allowed_file_type, warning, _ensure_authenticated, _resolve_context_token, to_thread, exception, token_bytes, _safe_media_filename, _build_upload_request, _request_json, _base_info, _ensure_success, _extract_upload_full_url, _extract_upload_param, _build_cdn_upload_url, _encrypt_aes_128_ecb, _upload_cdn_bytes, dict, _build_outbound_file_item, int（+1）
  #### `⏵m` `async _poll_loop(self) -> None`  L547
    - 分支数 8，函数体节点数 328；raise: bare raise
    - 调用: _ensure_authenticated, sleep, _request_json, _base_info, max, _current_longpoll_timeout_seconds, get, to_thread, error, warning, _update_longpoll_timeout, _handle_update, isinstance, exception
  #### `⏵m` `async _handle_update(self, raw_message: Any) -> None`  L615
    - 分支数 9，函数体节点数 320；return: None
    - 调用: isinstance, get, strip, str, _extract_text, _pending_connect_code, _bind_connection_from_connect_code, _check_user, _extract_inbound_files, _make_inbound, is_known_channel_command, _extract_ref_message, _attach_connection_identity, publish_inbound
  #### `⏵m` `async _attach_connection_identity(self, inbound: InboundMessage) -> InboundMessage`  L673
    - 分支数 0，函数体节点数 27；return: await attach_connection_identity(inbound, repo=self._connection_repo, provider='wechat', workspace_id=inbound.chat_id)
    - 调用: attach_connection_identity
  #### `⏵m` `async _bind_connection_from_connect_code(self, *, chat_id: str, context_token: str, code: str) -> bool`  L681
    - 分支数 3，函数体节点数 129；return: False, True
    - 调用: consume_oauth_state, _send_connection_reply, upsert_connection
  #### `⏵m` `async _send_connection_reply(self, chat_id: str, context_token: str, text: str) -> None`  L707
    - 分支数 1，函数体节点数 39；return: None
    - 调用: _send_text_message
  #### `⏵m` `async _ensure_authenticated(self) -> bool`  L718
    - 分支数 5，函数体节点数 77；return: True, False, bool(auth_state.get('bot_token'))
    - 调用: to_thread, _bind_via_qrcode, exception, bool, get
  #### `⏵m` `async _bind_via_qrcode(self) -> dict[str, Any]`  L737
    - 分支数 7，函数体节点数 370；raise: RuntimeError('iLink get_bot_qrcode did not return qrcode'), RuntimeError('iLink QR confirmation succeeded without bot_token'), RuntimeError(f'iLink QR code flow ended with status={status}'), TimeoutError('Timed out waiting for WeChat QR confirmation')；return: await asyncio.to_thread(self._save_auth_state, status='confirmed', bot_token=token, ilink_bot_id=self._ilink_bot_id, qrcode=qrcode, qrcode_img_content=qrcode_img_content or None)
    - 调用: _request_public_get_json, strip, str, get, RuntimeError, warning, to_thread, monotonic, max, lower, sleep, TimeoutError
  #### `⏵m` `async _request_json(self, path: str, payload: dict[str, Any], *, timeout: float | None) -> dict[str, Any]`  L802
    - 分支数 0，函数体节点数 105；return: data if isinstance(data, dict) else {}
    - 调用: _ensure_client, post, _auth_headers, raise_for_status, json, isinstance
  - 网络调用: post (L804)
  #### `⏵m` `async _request_public_get_json(self, path: str, params: dict[str, Any] | None, *, timeout: float | None) -> dict[str, Any]`  L814
    - 分支数 0，函数体节点数 109；return: data if isinstance(data, dict) else {}
    - 调用: _ensure_client, get, _public_headers, raise_for_status, json, isinstance
  - 网络调用: get (L822)
  #### `⏵m` `async _ensure_client(self) -> httpx.AsyncClient`  L832
    - 分支数 1，函数体节点数 47；return: self._client
    - 调用: max, AsyncClient
  #### `⏵m` `async _download_cdn_bytes(self, url: str, *, timeout: float | None) -> bytes`  L953
    - 分支数 0，函数体节点数 55；return: response.content
    - 调用: _ensure_client, get, raise_for_status
  - 网络调用: get (L955)
  #### `⏵m` `async _upload_cdn_bytes(self, url: str, content: bytes, *, content_type: str, timeout: float | None, method: str) -> str | None`  L959
    - 分支数 1，函数体节点数 111；return: response.headers.get('x-encrypted-param')
    - 调用: _ensure_client, upper, post, put, raise_for_status, get
  - 网络调用: post (L975), put (L977)
  #### `⏵m` `async _extract_inbound_files(self, raw_message: Mapping[str, Any]) -> list[dict[str, Any]]`  L1028
    - 分支数 7，函数体节点数 210；return: files
    - 调用: get, isinstance, str, enumerate, int, _extract_image_file, append, _extract_file_item
  #### `⏵m` `async _extract_image_file(self, item: Mapping[str, Any], *, message_id: str, index: int) -> dict[str, Any] | None`  L1049
    - 分支数 6，函数体节点数 324；return: None, {'type': 'image', 'filename': stored_path.name, 'size': len(decrypted), 'path': str(stored_path), 'mime_type': mime_type, 'source': 'wechat', 'message_item_type': int(MessageItemType.IMAGE), 'full_url': full_url}
    - 调用: get, isinstance, _extract_cdn_full_url, warning, _resolve_media_aes_key, _describe_media_key_state, _download_cdn_bytes, _decrypt_aes_128_ecb, len, _detect_image_extension_and_mime, _safe_media_filename, to_thread, guess_type, str, int
  #### `⏵m` `async _extract_file_item(self, item: Mapping[str, Any], *, message_id: str, index: int) -> dict[str, Any] | None`  L1097
    - 分支数 7，函数体节点数 328；return: None, {'type': 'file', 'filename': stored_path.name, 'size': len(decrypted), 'path': str(stored_path), 'mime_type': mime_type, 'source': 'wechat', 'message_item_type': int(MessageItemType.FILE), 'full_url': full_url}
    - 调用: get, isinstance, _extract_cdn_full_url, warning, _resolve_media_aes_key, _describe_media_key_state, _normalize_inbound_filename, guess_type, _is_allowed_file_type, _download_cdn_bytes, _decrypt_aes_128_ecb, len, to_thread, str, int

## 文件内调用关系
- `_encrypt_aes_128_ecb` -> _validate_aes_128_key
- `_decrypt_aes_128_ecb` -> _validate_aes_128_key
- `WechatChannel.__init__` -> __init__, _coerce_float, _coerce_int, _coerce_str_set, _resolve_state_dir
- `WechatChannel.start` -> _ensure_client, _poll_loop
- `WechatChannel.send` -> _ensure_authenticated, _resolve_context_token, _send_text_message
- `WechatChannel._send_text_message` -> _base_info, _request_json, _ensure_success
- `WechatChannel.send_file` -> _send_image_attachment, _send_file_attachment
- `WechatChannel._send_image_attachment` -> _ensure_authenticated, _resolve_context_token, _safe_media_filename, _build_upload_request, _request_json, _base_info, _ensure_success, _extract_upload_full_url, _extract_upload_param, _build_cdn_upload_url, _encrypt_aes_128_ecb, _upload_cdn_bytes, _build_outbound_image_item
- `WechatChannel._send_file_attachment` -> _is_allowed_file_type, _ensure_authenticated, _resolve_context_token, _safe_media_filename, _build_upload_request, _request_json, _base_info, _ensure_success, _extract_upload_full_url, _extract_upload_param, _build_cdn_upload_url, _encrypt_aes_128_ecb, _upload_cdn_bytes, _build_outbound_file_item
- `WechatChannel._poll_loop` -> _ensure_authenticated, _request_json, _base_info, _current_longpoll_timeout_seconds, _update_longpoll_timeout, _handle_update
- `WechatChannel._handle_update` -> _extract_text, _bind_connection_from_connect_code, _check_user, _extract_inbound_files, _extract_ref_message, _attach_connection_identity
- `WechatChannel._bind_connection_from_connect_code` -> _send_connection_reply
- `WechatChannel._send_connection_reply` -> _send_text_message
- `WechatChannel._ensure_authenticated` -> _bind_via_qrcode
- `WechatChannel._bind_via_qrcode` -> _request_public_get_json
- `WechatChannel._request_json` -> _ensure_client, _auth_headers
- `WechatChannel._request_public_get_json` -> _ensure_client, _public_headers
- `WechatChannel._common_headers` -> _build_ilink_client_version, _build_wechat_uin
- `WechatChannel._public_headers` -> _common_headers
- `WechatChannel._auth_headers` -> _common_headers
- `WechatChannel._build_upload_request` -> _validate_aes_128_key, _md5_hex, _encrypted_size_for_aes_128_ecb
- `WechatChannel._download_cdn_bytes` -> _ensure_client
- `WechatChannel._upload_cdn_bytes` -> _ensure_client
- `WechatChannel._build_outbound_image_item` -> _encode_outbound_media_aes_key
- `WechatChannel._build_outbound_file_item` -> _encode_outbound_media_aes_key, _md5_hex
- `WechatChannel._extract_inbound_files` -> _extract_image_file, _extract_file_item
- `WechatChannel._extract_image_file` -> _extract_cdn_full_url, _resolve_media_aes_key, _describe_media_key_state, _download_cdn_bytes, _decrypt_aes_128_ecb, _detect_image_extension_and_mime, _safe_media_filename
- `WechatChannel._extract_file_item` -> _extract_cdn_full_url, _resolve_media_aes_key, _describe_media_key_state, _normalize_inbound_filename, _is_allowed_file_type, _download_cdn_bytes, _decrypt_aes_128_ecb
- `WechatChannel._stage_downloaded_file` -> _download_dir
- `WechatChannel._decode_base64_aes_key` -> _validate_aes_128_key
- `WechatChannel._parse_aes_key_candidate` -> _validate_aes_128_key, _parse_aes_key_candidate, _decode_base64_aes_key
- `WechatChannel._resolve_media_aes_key` -> _parse_aes_key_candidate, _resolve_media_aes_key
- `WechatChannel._normalize_inbound_filename` -> _safe_media_filename
- `WechatChannel._load_state` -> _load_auth_state

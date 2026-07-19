# `backend/packages/harness/deerflow/persistence/channel_connections/sql.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/channel_connections/sql.py`  ·  行数: 550

**模块文档首行**（仅供参考）: SQL repository for user-owned IM channel connections.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: base64, hashlib, json, logging, uuid
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any
- `cryptography.fernet` -> Fernet, InvalidToken
- `sqlalchemy` -> delete, func, select, text, update
- `sqlalchemy.exc` -> IntegrityError
- `sqlalchemy.ext.asyncio` -> AsyncSession, async_sessionmaker
- `deerflow.persistence.channel_connections.model` -> ChannelConnectionRow, ChannelConversationRow, ChannelCredentialRow, ChannelOAuthStateRow
- `deerflow.utils.time` -> coerce_iso

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_UPSERT_MAX_ATTEMPTS` = 3

## 类
### 类 `ChannelCredentialCipher`  L35
- _文档首行_: Encrypts provider credentials before they are persisted.
- 方法:
  #### `cls` `from_key(cls, key: str) -> ChannelCredentialCipher`    @classmethod  L42
    - 分支数 0，函数体节点数 41；return: cls(Fernet(base64.urlsafe_b64encode(digest)))
    - 调用: digest, sha256, encode, cls, Fernet, urlsafe_b64encode
  #### `m` `__init__(self, fernet: Fernet) -> None`  L38
    - 分支数 0，函数体节点数 14
  #### `m` `encrypt_text(self, value: str | None) -> str | None`  L46
    - 分支数 1，函数体节点数 43；return: None, 'fernet:v1:' + self._fernet.encrypt(value.encode('utf-8')).decode('ascii')
    - 调用: decode, encrypt, encode
  #### `m` `decrypt_text(self, value: str | None) -> str | None`  L51
    - 分支数 1，函数体节点数 49；return: None, self._fernet.decrypt(token.encode('ascii')).decode('utf-8')
    - 调用: removeprefix, decode, decrypt, encode

### 类 `ChannelConnectionRepository`  L58
- _文档首行_: Persistence facade for channel connections, credentials, and conversations.
- 方法:
  #### `st` `_new_id() -> str`    @staticmethod  L76
    - 分支数 0，函数体节点数 14；return: uuid.uuid4().hex
    - 调用: uuid4
  #### `st` `_normalize_optional_identity(value: str | None) -> str`    @staticmethod  L80
    - 分支数 0，函数体节点数 18；return: value or ''
  #### `st` `_coerce_datetime(value: datetime | None) -> datetime | None`    @staticmethod  L84
    - 分支数 1，函数体节点数 42；return: value, value.replace(tzinfo=UTC)
    - 调用: replace
  - 文件IO: replace (L87)
  #### `st` `_connection_to_dict(row: ChannelConnectionRow) -> dict[str, Any]`    @staticmethod  L97
    - 分支数 2，函数体节点数 141；return: data
    - 调用: to_dict, pop, get, isinstance, coerce_iso
  #### `st` `hash_state(state: str) -> str`    @staticmethod  L283
    - 分支数 0，函数体节点数 24；return: hashlib.sha256(state.encode('utf-8')).hexdigest()
    - 调用: hexdigest, sha256, encode
  #### `st` `_oauth_scope_lock_key(owner_user_id: str, provider: str) -> int`    @staticmethod  L401
    - 分支数 0，函数体节点数 50；return: int.from_bytes(digest[:8], 'big') & 9223372036854775807
    - 调用: digest, sha256, encode, from_bytes
  #### `m` `__init__(self, session_factory: async_sessionmaker[AsyncSession], *, cipher: ChannelCredentialCipher | None) -> None`  L61
    - 分支数 0，函数体节点数 32
  #### `m` `_encrypt_optional_secret(self, value: str | None) -> str | None`  L89
    - 分支数 2，函数体节点数 45；raise: RuntimeError('channel connection encryption key is required')；return: None, self._cipher.encrypt_text(value)
    - 调用: RuntimeError, encrypt_text
  #### `⏵m` `async close(self) -> None`  L70
    - 分支数 0，函数体节点数 11
    - 调用: close_engine
  #### `⏵m` `async upsert_connection(self, *, owner_user_id: str, provider: str, external_account_id: str | None, external_account_name: str | None, workspace_id: str | None, workspace_name: str | None, bot_user_id: str | None, scopes: list[str] | None, capabilities: dict[str, Any] | None, metadata: dict[str, Any] | None, status: str) -> dict[str, Any]`  L110
    - 分支数 7，函数体节点数 520；raise: last_error；return: None, self._connection_to_dict(row)
    - 调用: _normalize_optional_identity, list, dict, execute, where, select, scalars, values, update, in_, delete, session_factory, range, scalar_one_or_none, _revoke_other_active_owners, ChannelConnectionRow, _new_id, add, _apply, commit（+3）
  #### `⏵m` `async list_connections(self, owner_user_id: str) -> list[dict[str, Any]]`  L194
    - 分支数 1，函数体节点数 88；return: [self._connection_to_dict(row) for row in result.scalars()]
    - 调用: session_factory, execute, order_by, where, select, desc, _connection_to_dict, scalars
  #### `⏵m` `async disconnect_connection(self, *, connection_id: str, owner_user_id: str) -> bool`  L199
    - 分支数 3，函数体节点数 94；return: False, True
    - 调用: session_factory, get, delete, commit
  - 网络调用: get (L201), get (L206), delete (L208)
  #### `⏵m` `async disconnect_provider_connections(self, *, provider: str) -> int`  L212
    - _文档首行_（仅供参考）: Revoke all active user connections for an instance-wide provider removal.
    - 分支数 2，函数体节点数 140；return: 0, len(connection_ids)
    - 调用: session_factory, execute, where, select, scalars, values, update, in_, delete, commit, len
  #### `⏵m` `async store_credentials(self, connection_id: str, *, access_token: str | None, refresh_token: str | None, token_type: str | None, expires_at: datetime | None, refresh_expires_at: datetime | None, extra: dict[str, Any] | None) -> None`  L230
    - 分支数 3，函数体节点数 209；raise: RuntimeError('channel connection encryption key is required')
    - 调用: RuntimeError, session_factory, get, ChannelCredentialRow, add, encrypt_text, dumps, commit
  - 网络调用: get (L244)
  #### `⏵m` `async get_credentials(self, connection_id: str) -> dict[str, Any] | None`  L257
    - 分支数 4，函数体节点数 164；return: None, {'connection_id': row.connection_id, 'access_token': self._cipher.decrypt_text(row.encrypted_access_token), 'refresh_token': self._cipher.decrypt_text(row.encrypted_refresh_token), 'token_type': row.token_type, 'expires_at': self._coerce_datetime(row.expires_at), 'refresh_expires_at': self._coerce_datetime(row.refresh_expires_at), 'extra': json.loads(extra_raw) if extra_raw else {}}
    - 调用: session_factory, get, decrypt_text, _coerce_datetime, loads, warning
  - 网络调用: get (L261)
  #### `⏵m` `async create_oauth_state(self, *, owner_user_id: str, provider: str, state: str, expires_at: datetime, code_verifier: str | None, nonce_hash: str | None, redirect_after: str | None, requested_scopes: list[str] | None, metadata: dict[str, Any] | None) -> None`  L286
    - 分支数 1，函数体节点数 143
    - 调用: ChannelOAuthStateRow, hash_state, _encrypt_optional_secret, list, dict, session_factory, add, commit
  #### `⏵m` `async create_oauth_state_within_cap(self, *, owner_user_id: str, provider: str, state: str, expires_at: datetime, max_pending: int, now: datetime | None, code_verifier: str | None, nonce_hash: str | None, redirect_after: str | None, requested_scopes: list[str] | None, metadata: dict[str, Any] | None) -> bool`  L314
    - _文档首行_（仅供参考）: Atomically enforce the per-(owner, provider) pending cap, then insert.
    - 分支数 2，函数体节点数 298；return: False, True
    - 调用: now, session_factory, _serialize_oauth_owner_scope, execute, where, delete, select_from, select, count, is_, int, scalar_one, rollback, add, ChannelOAuthStateRow, hash_state, _encrypt_optional_secret, list, dict, commit
  #### `⏵m` `async _serialize_oauth_owner_scope(self, session: AsyncSession, owner_user_id: str, provider: str) -> None`  L385
    - _文档首行_（仅供参考）: Serialize concurrent pending-cap transactions for one (owner, provider).
    - 分支数 2，函数体节点数 71
    - 调用: execute, text, _oauth_scope_lock_key
  #### `⏵m` `async delete_expired_oauth_states(self, *, now: datetime | None) -> int`  L406
    - 分支数 1，函数体节点数 78；return: int(result.rowcount or 0)
    - 调用: now, session_factory, execute, where, delete, commit, int
  #### `⏵m` `async count_oauth_states(self, *, owner_user_id: str, provider: str, active_only: bool, now: datetime | None) -> int`  L413
    - 分支数 2，函数体节点数 131；return: int(result.scalar_one())
    - 调用: now, extend, is_, session_factory, execute, where, select_from, select, count, int, scalar_one
  #### `⏵m` `async consume_oauth_state(self, *, provider: str, state: str, now: datetime | None) -> dict[str, Any] | None`  L438
    - 分支数 4，函数体节点数 255；return: None, {'owner_user_id': row.owner_user_id, 'provider': row.provider, 'requested_scopes': row.requested_scopes_json or [], 'metadata': row.metadata_json or {}, 'redirect_after': row.redirect_after}
    - 调用: now, hash_state, session_factory, execute, where, delete, get, commit, _coerce_datetime, values, update, is_
  - 网络调用: get (L449)
  #### `⏵m` `async find_connection_by_external_identity(self, *, provider: str, external_account_id: str, workspace_id: str | None) -> dict[str, Any] | None`  L480
    - 分支数 1，函数体节点数 140；return: self._connection_to_dict(row) if row is not None else None
    - 调用: session_factory, execute, limit, order_by, where, select, _normalize_optional_identity, desc, scalar_one_or_none, _connection_to_dict
  #### `⏵m` `async set_thread_id(self, *, connection_id: str, owner_user_id: str, provider: str, external_conversation_id: str, thread_id: str, external_topic_id: str | None) -> None`  L502
    - 分支数 2，函数体节点数 164
    - 调用: session_factory, where, select, scalar_one_or_none, execute, ChannelConversationRow, _new_id, add, commit
  #### `⏵m` `async get_thread_id(self, connection_id: str, external_conversation_id: str, external_topic_id: str | None) -> str | None`  L537
    - 分支数 1，函数体节点数 82；return: (await session.execute(stmt)).scalar_one_or_none()
    - 调用: session_factory, where, select, scalar_one_or_none, execute

## 文件内调用关系
- `ChannelConnectionRepository._encrypt_optional_secret` -> encrypt_text
- `ChannelConnectionRepository.upsert_connection` -> _normalize_optional_identity, _new_id, _connection_to_dict
- `ChannelConnectionRepository.list_connections` -> _connection_to_dict
- `ChannelConnectionRepository.store_credentials` -> encrypt_text
- `ChannelConnectionRepository.get_credentials` -> decrypt_text, _coerce_datetime
- `ChannelConnectionRepository.create_oauth_state` -> hash_state, _encrypt_optional_secret
- `ChannelConnectionRepository.create_oauth_state_within_cap` -> _serialize_oauth_owner_scope, hash_state, _encrypt_optional_secret
- `ChannelConnectionRepository._serialize_oauth_owner_scope` -> _oauth_scope_lock_key
- `ChannelConnectionRepository.consume_oauth_state` -> hash_state, _coerce_datetime
- `ChannelConnectionRepository.find_connection_by_external_identity` -> _normalize_optional_identity, _connection_to_dict
- `ChannelConnectionRepository.set_thread_id` -> _new_id

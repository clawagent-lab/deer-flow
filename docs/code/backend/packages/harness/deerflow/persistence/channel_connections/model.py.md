# `backend/packages/harness/deerflow/persistence/channel_connections/model.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/channel_connections/model.py`  ·  行数: 126

**模块文档首行**（仅供参考）: ORM models for user-owned IM channel connections.

## 模块概览
- 函数 1 个，类 4 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> JSON, DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint, text
- `sqlalchemy.orm` -> Mapped, mapped_column
- `deerflow.persistence.base` -> Base

## 函数
#### `ƒ` `_utc_now() -> datetime`  L13
  - 分支数 0，函数体节点数 12；return: datetime.now(UTC)
  - 调用: now

## 类
### 类 `ChannelConnectionRow`  L17
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'channel_connections'
  - `id` = mapped_column(String(64), primary_key=True)
  - `owner_user_id` = mapped_column(String(64), nullable=False, index=True)
  - `provider` = mapped_column(String(32), nullable=False, index=True)
  - `status` = mapped_column(String(32), nullable=False, default='connec...
  - `external_account_id` = mapped_column(String(128), nullable=False, default='')
  - `external_account_name` = mapped_column(String(256), nullable=True)
  - `workspace_id` = mapped_column(String(128), nullable=False, default='')
  - `workspace_name` = mapped_column(String(256), nullable=True)
  - `bot_user_id` = mapped_column(String(128), nullable=True)
  - `scopes_json` = mapped_column(JSON, default=list)
  - `capabilities_json` = mapped_column(JSON, default=dict)
  - `metadata_json` = mapped_column(JSON, default=dict)
  - `created_at` = mapped_column(DateTime(timezone=True), nullable=False, de...
  - `updated_at` = mapped_column(DateTime(timezone=True), nullable=False, de...
  - `last_seen_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `last_error_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `__table_args__` = (UniqueConstraint('owner_user_id', 'provider', 'external_...

### 类 `ChannelCredentialRow`  L66
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'channel_credentials'
  - `connection_id` = mapped_column(String(64), ForeignKey('channel_connections...
  - `encrypted_access_token` = mapped_column(Text, nullable=True)
  - `encrypted_refresh_token` = mapped_column(Text, nullable=True)
  - `token_type` = mapped_column(String(32), nullable=True)
  - `expires_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `refresh_expires_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `encrypted_extra_json` = mapped_column(Text, nullable=True)
  - `version` = mapped_column(Integer, nullable=False, default=1)
  - `updated_at` = mapped_column(DateTime(timezone=True), nullable=False, de...

### 类 `ChannelOAuthStateRow`  L84
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'channel_oauth_states'
  - `state_hash` = mapped_column(String(128), primary_key=True)
  - `owner_user_id` = mapped_column(String(64), nullable=False, index=True)
  - `provider` = mapped_column(String(32), nullable=False, index=True)
  - `code_verifier_encrypted` = mapped_column(Text, nullable=True)
  - `nonce_hash` = mapped_column(String(128), nullable=True)
  - `redirect_after` = mapped_column(Text, nullable=True)
  - `requested_scopes_json` = mapped_column(JSON, default=list)
  - `metadata_json` = mapped_column(JSON, default=dict)
  - `expires_at` = mapped_column(DateTime(timezone=True), nullable=False)
  - `consumed_at` = mapped_column(DateTime(timezone=True), nullable=True)
  - `created_at` = mapped_column(DateTime(timezone=True), nullable=False, de...

### 类 `ChannelConversationRow`  L100
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'channel_conversations'
  - `id` = mapped_column(String(64), primary_key=True)
  - `connection_id` = mapped_column(String(64), ForeignKey('channel_connections...
  - `owner_user_id` = mapped_column(String(64), nullable=False, index=True)
  - `provider` = mapped_column(String(32), nullable=False, index=True)
  - `external_conversation_id` = mapped_column(String(128), nullable=False)
  - `external_topic_id` = mapped_column(String(128), nullable=False, default='')
  - `thread_id` = mapped_column(String(64), nullable=False, index=True)
  - `created_at` = mapped_column(DateTime(timezone=True), nullable=False, de...
  - `updated_at` = mapped_column(DateTime(timezone=True), nullable=False, de...
  - `__table_args__` = (UniqueConstraint('connection_id', 'external_conversation...

## 文件内调用关系
_无文件内调用_

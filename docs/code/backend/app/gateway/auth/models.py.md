# `backend/app/gateway/auth/models.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/models.py`  ·  行数: 43

**模块文档首行**（仅供参考）: User Pydantic models for authentication.

## 模块概览
- 函数 1 个，类 2 个，模块级常量 0 个

## 依赖（import）
- `datetime` -> UTC, datetime
- `typing` -> Literal
- `uuid` -> UUID, uuid4
- `pydantic` -> BaseModel, ConfigDict, EmailStr, Field

## 函数
#### `ƒ` `_utc_now() -> datetime`  L10
  - _文档首行_（仅供参考）: Return current UTC time (timezone-aware).
  - 分支数 0，函数体节点数 14；return: datetime.now(UTC)
  - 调用: now

## 类
### 类 `User`  L15
- 继承: BaseModel
- _文档首行_: Internal user representation.
- 类/实例变量:
  - `model_config` = ConfigDict(from_attributes=True)
  - `id` = Field(default_factory=uuid4, description='Primary key')
  - `email` = Field(..., description='Unique email address')
  - `password_hash` = Field(None, description='bcrypt hash, nullable for OAuth ...
  - `system_role` = Field(default='user')
  - `created_at` = Field(default_factory=_utc_now)
  - `oauth_provider` = Field(None, description="e.g. 'github', 'google'")
  - `oauth_id` = Field(None, description='User ID from OAuth provider')
  - `needs_setup` = Field(default=False, description='True when a reset accou...
  - `token_version` = Field(default=0, description='Incremented on password cha...

### 类 `UserResponse`  L35
- 继承: BaseModel
- _文档首行_: Response model for user info endpoint.
- 类/实例变量:
  - `id` = <annotated>
  - `email` = <annotated>
  - `system_role` = <annotated>
  - `needs_setup` = False
  - `oauth_provider` = Field(None, description="OAuth/SSO provider ID if the use...

## 文件内调用关系
_无文件内调用_

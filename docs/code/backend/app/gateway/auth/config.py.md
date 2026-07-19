# `backend/app/gateway/auth/config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/config.py`  ·  行数: 86

**模块文档首行**（仅供参考）: Authentication configuration for DeerFlow.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 3 个

## 依赖（import）
- 模块: logging, os, secrets
- `pydantic` -> BaseModel, Field

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SECRET_FILE` = '.jwt_secret'
- `_auth_config` = None

## 函数
#### `ƒ` `_load_or_create_secret() -> str`  L35
  - _文档首行_（仅供参考）: Load persisted JWT secret from ``{base_dir}/.jwt_secret``, or generate and persist a new one.
  - 分支数 5，函数体节点数 155；raise: RuntimeError(f'Failed to read JWT secret from {secret_file}. Set AUTH_JWT_SECRET explicitly or fix DEER_FLOW_HOME/base directory permissions so DeerFlow can read its persisted auth secret.'), RuntimeError(f'Failed to persist JWT secret to {secret_file}. Set AUTH_JWT_SECRET explicitly or fix DEER_FLOW_HOME/base directory permissions so DeerFlow can store a stable auth secret.')；return: secret
  - 调用: get_paths, exists, strip, read_text, RuntimeError, token_urlsafe, mkdir, open, fdopen, write
  - 文件IO: exists (L43), read_text (L44), mkdir (L52), open (L53), write (L55)

#### `ƒ` `get_auth_config() -> AuthConfig`  L61
  - _文档首行_（仅供参考）: Get the global AuthConfig instance. Parses from env on first call.
  - 分支数 2，函数体节点数 70；return: _auth_config
  - 调用: load_dotenv, get, _load_or_create_secret, warning, AuthConfig

#### `ƒ` `set_auth_config(config: AuthConfig) -> None`  L82
  - _文档首行_（仅供参考）: Set the global AuthConfig instance (for testing).
  - 分支数 0，函数体节点数 14

## 类
### 类 `AuthConfig`  L14
- 继承: BaseModel
- _文档首行_: JWT and auth-related configuration. Parsed once at startup.
- 类/实例变量:
  - `jwt_secret` = Field(..., description='Secret key for JWT signing. MUST ...
  - `token_expiry_days` = Field(default=7, ge=1, le=30)
  - `oauth_github_client_id` = Field(default=None)
  - `oauth_github_client_secret` = Field(default=None)

## 文件内调用关系
- `get_auth_config` -> _load_or_create_secret

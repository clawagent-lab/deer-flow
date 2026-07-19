# `backend/app/gateway/auth/oidc_state.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/oidc_state.py`  ·  行数: 123

**模块文档首行**（仅供参考）: OIDC state management via signed HttpOnly cookies.

## 模块概览
- 函数 11 个，类 1 个，模块级常量 5 个

## 依赖（import）
- 模块: secrets, time, jwt
- `__future__` -> annotations
- `fastapi` -> Request, Response
- `pydantic` -> BaseModel, Field
- `app.gateway.auth.config` -> get_auth_config
- `app.gateway.csrf_middleware` -> is_secure_request

## 模块级常量
- `OIDC_STATE_COOKIE_PREFIX` = 'df_oidc_state_'
- `OIDC_STATE_MAX_AGE` = 300
- `OIDC_STATE_BYTES` = 32
- `OIDC_NONCE_BYTES` = 16
- `OIDC_CODE_VERIFIER_BYTES` = 32

## 函数
#### `ƒ` `_sign_state_payload(payload: OIDCStatePayload) -> str`  L39
  - _文档首行_（仅供参考）: Sign the state payload with the JWT secret to prevent tampering.
  - 分支数 0，函数体节点数 32；return: jwt.encode(payload.model_dump(), secret, algorithm='HS256')
  - 调用: get_auth_config, encode, model_dump

#### `ƒ` `_verify_state_signed(signed: str, max_age: int) -> OIDCStatePayload | None`  L45
  - _文档首行_（仅供参考）: Verify a signed state payload and return it, or None if invalid/expired.
  - 分支数 2，函数体节点数 79；return: None, payload
  - 调用: get_auth_config, decode, OIDCStatePayload, time

#### `ƒ` `generate_oidc_state() -> str`  L58
  - _文档首行_（仅供参考）: Generate a cryptographically random state string.
  - 分支数 0，函数体节点数 14；return: secrets.token_urlsafe(OIDC_STATE_BYTES)
  - 调用: token_urlsafe

#### `ƒ` `generate_nonce() -> str`  L63
  - _文档首行_（仅供参考）: Generate a cryptographically random nonce for ID token validation.
  - 分支数 0，函数体节点数 14；return: secrets.token_urlsafe(OIDC_NONCE_BYTES)
  - 调用: token_urlsafe

#### `ƒ` `generate_code_verifier() -> str`  L68
  - _文档首行_（仅供参考）: Generate a PKCE code verifier (plain random string).
  - 分支数 0，函数体节点数 14；return: secrets.token_urlsafe(OIDC_CODE_VERIFIER_BYTES)
  - 调用: token_urlsafe

#### `ƒ` `compute_code_challenge(verifier: str) -> str`  L73
  - _文档首行_（仅供参考）: Compute the S256 PKCE code challenge from a verifier.
  - 分支数 0，函数体节点数 29；return: _base64url_encode(hashlib.sha256(verifier.encode('ascii')).digest())
  - 调用: _base64url_encode, digest, sha256, encode

#### `ƒ` `_base64url_encode(data: bytes) -> str`  L80
  - _文档首行_（仅供参考）: Base64url-encode without padding, as required by RFC 7636 and OIDC.
  - 分支数 0，函数体节点数 27；return: base64.urlsafe_b64encode(data).rstrip(b'=').decode('ascii')
  - 调用: decode, rstrip, urlsafe_b64encode

#### `ƒ` `_cookie_name(provider: str) -> str`  L87
  - 分支数 0，函数体节点数 15；return: f'{OIDC_STATE_COOKIE_PREFIX}{provider}'

#### `ƒ` `set_state_cookie(response: Response, request: Request, payload: OIDCStatePayload) -> None`  L91
  - _文档首行_（仅供参考）: Set the signed OIDC state cookie on the response.
  - 分支数 0，函数体节点数 65
  - 调用: _sign_state_payload, is_secure_request, set_cookie, _cookie_name

#### `ƒ` `get_state_cookie(request: Request, provider: str) -> OIDCStatePayload | None`  L106
  - _文档首行_（仅供参考）: Read and verify the signed OIDC state cookie for the given provider.
  - 分支数 1，函数体节点数 43；return: None, _verify_state_signed(signed)
  - 调用: get, _cookie_name, _verify_state_signed

#### `ƒ` `delete_state_cookie(response: Response, request: Request, provider: str) -> None`  L114
  - _文档首行_（仅供参考）: Delete the OIDC state cookie.
  - 分支数 0，函数体节点数 45
  - 调用: is_secure_request, delete_cookie, _cookie_name

## 类
### 类 `OIDCStatePayload`  L27
- 继承: BaseModel
- _文档首行_: Payload stored inside the signed OIDC state cookie.
- 类/实例变量:
  - `provider` = Field(description='OIDC provider ID (must match the state...
  - `state` = Field(description='Cryptographically random state value —...
  - `nonce` = Field(default=None, description='OIDC nonce, verified aga...
  - `code_verifier` = Field(default=None, description='PKCE code verifier, sent...
  - `next_path` = Field(default='/workspace', description='Redirect target ...
  - `remember_me` = Field(default=True, description='Whether the resulting De...
  - `issued_at` = Field(default_factory=time.time, description='Unix timest...

## 文件内调用关系
- `compute_code_challenge` -> _base64url_encode
- `set_state_cookie` -> _sign_state_payload, _cookie_name
- `get_state_cookie` -> _cookie_name, _verify_state_signed
- `delete_state_cookie` -> _cookie_name

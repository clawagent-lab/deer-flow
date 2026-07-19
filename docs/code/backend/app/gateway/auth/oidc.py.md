# `backend/app/gateway/auth/oidc.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/auth/oidc.py`  ·  行数: 434

**模块文档首行**（仅供参考）: OIDC (OpenID Connect) authentication service.

## 模块概览
- 函数 1 个，类 7 个，模块级常量 4 个

## 依赖（import）
- 模块: logging, secrets, time, httpx, jwt
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> Any
- `urllib.parse` -> urlencode
- `jwt` -> PyJWK

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `OIDC_DISCOVERY_PATH` = '/.well-known/openid-configuration'
- `METADATA_CACHE_TTL` = 300
- `JWKS_CACHE_TTL` = 300

## 函数
#### `ƒ` `_constant_time_compare(a: str, b: str) -> bool`  L431
  - _文档首行_（仅供参考）: Constant-time string comparison.
  - 分支数 0，函数体节点数 22；return: secrets.compare_digest(a, b)
  - 调用: compare_digest

## 类
### 类 `OIDCMetadata`  L30  @dataclass(...)
- _文档首行_: Resolved OIDC provider metadata after discovery.
- 类/实例变量:
  - `issuer` = <annotated>
  - `authorization_endpoint` = <annotated>
  - `token_endpoint` = <annotated>
  - `userinfo_endpoint` = <annotated>
  - `jwks_uri` = <annotated>

### 类 `OIDCIdentity`  L41  @dataclass(...)
- _文档首行_: Normalized identity extracted from an OIDC provider response.
- 类/实例变量:
  - `provider` = <annotated>
  - `subject` = <annotated>
  - `email` = <annotated>
  - `email_verified` = <annotated>
  - `name` = <annotated>
  - `claims` = <annotated>

### 类 `OIDCError`  L52
- 继承: Exception
- _文档首行_: Base error for OIDC operations. Message is safe for API responses.

### 类 `OIDCProviderError`  L56
- 继承: OIDCError
- _文档首行_: The OIDC provider returned an error (e.g. access_denied).

### 类 `OIDCValidationError`  L60
- 继承: OIDCError
- _文档首行_: ID token validation failed.

### 类 `OIDCUserInfoMismatch`  L64
- 继承: OIDCError
- _文档首行_: UserInfo sub does not match ID token sub.

### 类 `OIDCService`  L71
- _文档首行_: OIDC authentication service.
- 方法:
  #### `m` `__init__(self, metadata_cache_ttl: float, jwks_cache_ttl: float) -> None`  L79
    - 分支数 0，函数体节点数 109
    - 调用: AsyncClient, Timeout
  #### `m` `_metadata_from_dict(self, data: dict[str, Any], overrides: dict[str, str | None] | None) -> OIDCMetadata`  L131
    - _文档首行_（仅供参考）: Build OIDCMetadata from a discovery dict, applying endpoint overrides.
    - 分支数 0，函数体节点数 110；return: OIDCMetadata(issuer=data['issuer'], authorization_endpoint=overrides.get('authorization_endpoint') or data['authorization_endpoint'], token_endpoint=overrides.get('token_endpoint') or data['token_endpoint'], userinfo_endpoint=overrides.get('userinfo_endpoint') or data.get('userinfo_endpoint'), jwks_uri=overrides.get('jwks_uri') or data['jwks_uri'])
    - 调用: OIDCMetadata, get
  #### `m` `build_authorization_url(self, metadata: OIDCMetadata, client_id: str, redirect_uri: str, scopes: list[str], state: str, nonce: str | None, code_challenge: str | None) -> str`  L144
    - _文档首行_（仅供参考）: Build the OIDC authorization URL for the provider.
    - 分支数 2，函数体节点数 115；return: f'{metadata.authorization_endpoint}?{urlencode(params)}'
    - 调用: join, urlencode
  #### `⏵m` `async close(self) -> None`  L90
    - _文档首行_（仅供参考）: Close the underlying HTTP client.
    - 分支数 0，函数体节点数 15
    - 调用: aclose
  #### `⏵m` `async discover(self, issuer: str, overrides: dict[str, str | None] | None) -> OIDCMetadata`  L96
    - _文档首行_（仅供参考）: Fetch and cache OIDC discovery metadata from the issuer.
    - 分支数 4，函数体节点数 254；raise: OIDCError(f'OIDC discovery failed for issuer {issuer}: HTTP {exc.response.status_code}'), OIDCError(f'OIDC discovery failed for issuer {issuer}: {exc}'), OIDCError(f'OIDC discovery response from {issuer} is missing the issuer field'), OIDCError(f"OIDC discovered issuer '{discovered_issuer}' does not match configured issuer '{issuer}'")；return: self._metadata_from_dict(cached[1], overrides), self._metadata_from_dict(data, overrides)
    - 调用: time, get, _metadata_from_dict, rstrip, raise_for_status, json, OIDCError
  #### `⏵m` `async exchange_code(self, metadata: OIDCMetadata, client_id: str, client_secret: str | None, code: str, redirect_uri: str, code_verifier: str | None, auth_method: str) -> dict[str, Any]`  L175
    - _文档首行_（仅供参考）: Exchange the authorization code for tokens at the token endpoint.
    - 分支数 5，函数体节点数 256；raise: OIDCError(f'Token exchange failed: HTTP {exc.response.status_code} — {body}'), OIDCError(f'Token exchange failed: {exc}')；return: resp.json()
    - 调用: decode, b64encode, encode, post, raise_for_status, json, OIDCError
  #### `⏵m` `async _load_jwks(self, jwks_uri: str, force_refresh: bool) -> dict[str, Any]`  L221
    - _文档首行_（仅供参考）: Load (and cache) JWKS from the provider.
    - 分支数 2，函数体节点数 164；raise: OIDCError(f'JWKS fetch failed: HTTP {exc.response.status_code}'), OIDCError(f'JWKS fetch failed: {exc}')；return: cached[1], data
    - 调用: time, get, raise_for_status, json, OIDCError
  #### `⏵m` `async _resolve_signing_key(self, jwks_data: dict[str, Any], kid: str | None, algorithm: str, jwks_uri: str) -> Any | None`  L243
    - _文档首行_（仅供参考）: Find the signing key matching ``kid`` in the JWKS.
    - 分支数 4，函数体节点数 118；raise: OIDCValidationError(f'JWK for kid={kid} is invalid: {exc}')；return: jwk.key, None
    - 调用: get, PyJWK, warning, OIDCValidationError
  #### `⏵m` `async validate_id_token(self, metadata: OIDCMetadata, client_id: str, id_token: str, nonce: str | None) -> dict[str, Any]`  L273
    - _文档首行_（仅供参考）: Validate the ID token and return its claims.
    - 分支数 7，函数体节点数 303；raise: OIDCValidationError(f"ID token uses unsupported algorithm '{alg}'"), OIDCValidationError(f'No matching JWK found for kid={kid} after JWKS refresh'), OIDCValidationError('ID token has expired'), OIDCValidationError('ID token has an invalid issuer'), OIDCValidationError('ID token has an invalid audience'), OIDCValidationError(f'ID token validation failed: {exc}'), OIDCValidationError('ID token is missing the nonce claim'), OIDCValidationError('ID token nonce does not match')；return: claims
    - 调用: _load_jwks, get_unverified_header, get, OIDCValidationError, _resolve_signing_key, decode, _constant_time_compare
  #### `⏵m` `async fetch_userinfo(self, metadata: OIDCMetadata, access_token: str, expected_sub: str) -> dict[str, Any]`  L338
    - _文档首行_（仅供参考）: Fetch userinfo from the UserInfo endpoint.
    - 分支数 3，函数体节点数 148；raise: OIDCError(f'UserInfo fetch failed: HTTP {exc.response.status_code}'), OIDCError(f'UserInfo fetch failed: {exc}'), OIDCUserInfoMismatch('UserInfo sub does not match ID token sub')；return: {}, userinfo
    - 调用: get, raise_for_status, json, OIDCError, OIDCUserInfoMismatch
  #### `⏵m` `async authenticate_callback(self, provider_id: str, metadata: OIDCMetadata, client_id: str, client_secret: str | None, code: str, redirect_uri: str, code_verifier: str | None, nonce: str | None, auth_method: str) -> OIDCIdentity`  L364
    - _文档首行_（仅供参考）: Orchestrate the full OIDC callback: token exchange, ID token validation, userinfo.
    - 分支数 3，函数体节点数 244；raise: OIDCError('Token response is missing id_token')；return: OIDCIdentity(provider=provider_id, subject=claims['sub'], email=email, email_verified=email_verified, name=merged.get('name'), claims=merged)
    - 调用: exchange_code, get, OIDCError, validate_id_token, fetch_userinfo, warning, OIDCIdentity

## 文件内调用关系
- `OIDCService.discover` -> _metadata_from_dict
- `OIDCService.validate_id_token` -> _load_jwks, _resolve_signing_key, _constant_time_compare
- `OIDCService.authenticate_callback` -> exchange_code, validate_id_token, fetch_userinfo

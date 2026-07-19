# `backend/app/gateway/github/app_auth.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/github/app_auth.py`  ·  行数: 230

**模块文档首行**（仅供参考）: GitHub App authentication helpers.

## 模块概览
- 函数 7 个，类 2 个，模块级常量 10 个

## 依赖（import）
- 模块: asyncio, logging, os, time, httpx, jwt
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `pathlib` -> Path

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_APP_JWT_TTL_SECONDS` = 9 * 60
- `_INSTALLATION_TOKEN_LEEWAY_SECONDS` = 5 * 60
- `_APP_ID_ENV` = 'GITHUB_APP_ID'
- `_PRIVATE_KEY_PATH_ENV` = 'GITHUB_APP_PRIVATE_KEY_PATH'
- `_PRIVATE_KEY_ENV` = 'GITHUB_APP_PRIVATE_KEY'
- `_GITHUB_API_BASE` = 'https://api.github.com'
- `_token_cache` = {}
- `_install_locks` = {}
- `_install_locks_lock` = asyncio.Lock()

## 函数
#### `⏵ƒ` `async _lock_for(installation_id: int) -> asyncio.Lock`  L71
  - _文档首行_（仅供参考）: Return the lock dedicated to ``installation_id``, creating on demand.
  - 分支数 2，函数体节点数 51；return: lock
  - 调用: get, Lock

#### `ƒ` `app_id() -> int`  L81
  - _文档首行_（仅供参考）: Return the configured GitHub App id, or raise if unset.
  - 分支数 2，函数体节点数 60；raise: GitHubAppAuthError(f'{_APP_ID_ENV} is not set'), GitHubAppAuthError(f'{_APP_ID_ENV}={raw!r} is not an integer')；return: int(raw.strip())
  - 调用: get, GitHubAppAuthError, int, strip

#### `ƒ` `load_app_private_key() -> str`  L96
  - _文档首行_（仅供参考）: Return the App's RSA private key as a PEM string.
  - 分支数 3，函数体节点数 101；raise: GitHubAppAuthError(f'Neither {_PRIVATE_KEY_ENV} nor {_PRIVATE_KEY_PATH_ENV} is set'), GitHubAppAuthError(f'{_PRIVATE_KEY_PATH_ENV} points to nonexistent file: {p}')；return: inline, p.read_text(encoding='utf-8')
  - 调用: get, strip, GitHubAppAuthError, expanduser, Path, exists, read_text
  - 文件IO: exists (L112), read_text (L114)

#### `ƒ` `mint_app_jwt(*, now: float | None) -> str`  L117
  - _文档首行_（仅供参考）: Sign a short-lived JWT identifying this App to GitHub.
  - 分支数 0，函数体节点数 69；return: jwt.encode(payload, load_app_private_key(), algorithm='RS256')
  - 调用: int, time, str, app_id, encode, load_app_private_key

#### `⏵ƒ` `async _request_new_installation_token(installation_id: int, *, client: httpx.AsyncClient | None) -> _CachedToken`  L138
  - _文档首行_（仅供参考）: Hit ``POST /app/installations/{id}/access_tokens`` once.
  - 分支数 3，函数体节点数 165；raise: GitHubAppAuthError(f'Failed to mint installation token (status={resp.status_code} body={resp.text!r})')；return: _CachedToken(token=token, expires_at=expires_at), await _do(c), await _do(client)
  - 调用: mint_app_jwt, post, GitHubAppAuthError, json, time, _CachedToken, AsyncClient, _do

#### `⏵ƒ` `async mint_installation_token(installation_id: int, *, client: httpx.AsyncClient | None, force_refresh: bool) -> str`  L169
  - _文档首行_（仅供参考）: Return a valid installation access token, minting if necessary.
  - 分支数 5，函数体节点数 161；raise: GitHubAppAuthError(f'installation_id must be positive, got {installation_id!r}')；return: cached.token, fresh.token
  - 调用: GitHubAppAuthError, get, time, _lock_for, _request_new_installation_token

#### `ƒ` `_clear_token_cache_for_tests() -> None`  L226
  - _文档首行_（仅供参考）: Drop every cached token. Tests reach for this between cases.
  - 分支数 0，函数体节点数 17
  - 调用: clear

## 类
### 类 `GitHubAppAuthError`  L48
- 继承: RuntimeError
- _文档首行_: Raised when GitHub App credentials are missing or invalid.

### 类 `_CachedToken`  L53  @dataclass
- 类/实例变量:
  - `token` = <annotated>
  - `expires_at` = <annotated>

## 文件内调用关系
- `mint_app_jwt` -> app_id, load_app_private_key
- `_request_new_installation_token` -> mint_app_jwt
- `mint_installation_token` -> _lock_for, _request_new_installation_token

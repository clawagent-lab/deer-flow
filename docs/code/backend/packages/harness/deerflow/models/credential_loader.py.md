# `backend/packages/harness/deerflow/models/credential_loader.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/credential_loader.py`  ·  行数: 220

**模块文档首行**（仅供参考）: Auto-load credentials from Claude Code CLI and Codex CLI.

## 模块概览
- 函数 10 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: json, logging, os, time
- `dataclasses` -> dataclass
- `pathlib` -> Path
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `OAUTH_ANTHROPIC_BETAS` = 'oauth-2025-04-20,claude-code-20250219,interleaved-thinki...

## 函数
#### `ƒ` `is_oauth_token(token: str) -> bool`  L29
  - _文档首行_（仅供参考）: Check if a token is a Claude Code OAuth token (not a standard API key).
  - 分支数 0，函数体节点数 24；return: isinstance(token, str) and 'sk-ant-oat' in token
  - 调用: isinstance

#### `ƒ` `_resolve_credential_path(env_var: str, default_relative_path: str) -> Path`  L59
  - 分支数 1，函数体节点数 40；return: Path(configured_path).expanduser(), _home_dir() / default_relative_path
  - 调用: getenv, expanduser, Path, _home_dir
  - 环境变量: getenv (L60)

#### `ƒ` `_home_dir() -> Path`  L66
  - 分支数 1，函数体节点数 31；return: Path(home).expanduser(), Path.home()
  - 调用: getenv, expanduser, Path, home
  - 环境变量: getenv (L67)

#### `ƒ` `_load_json_file(path: Path, label: str) -> dict[str, Any] | None`  L73
  - 分支数 3，函数体节点数 105；return: None, json.loads(path.read_text())
  - 调用: exists, debug, is_dir, warning, loads, read_text
  - 文件IO: exists (L74), read_text (L82)

#### `ƒ` `_read_secret_from_file_descriptor(env_var: str) -> str | None`  L88
  - 分支数 3，函数体节点数 102；return: None, secret or None
  - 调用: getenv, int, warning, strip, decode, read
  - 文件IO: read (L100)
  - 环境变量: getenv (L89)

#### `ƒ` `_credential_from_direct_token(access_token: str, source: str) -> ClaudeCodeCredential | None`  L108
  - 分支数 1，函数体节点数 38；return: None, ClaudeCodeCredential(access_token=token, source=source)
  - 调用: strip, ClaudeCodeCredential

#### `ƒ` `_iter_claude_code_credential_paths() -> list[Path]`  L115
  - 分支数 2，函数体节点数 83；return: paths
  - 调用: getenv, append, expanduser, Path, _home_dir
  - 环境变量: getenv (L117)

#### `ƒ` `_extract_claude_code_credential(data: dict[str, Any], source: str) -> ClaudeCodeCredential | None`  L128
  - 分支数 2，函数体节点数 100；return: None, cred
  - 调用: get, debug, ClaudeCodeCredential, warning

#### `ƒ` `load_claude_code_credential() -> ClaudeCodeCredential | None`  L149
  - _文档首行_（仅供参考）: Load OAuth credential from explicit Claude Code handoff sources.
  - 分支数 7，函数体节点数 183；return: cred, None
  - 调用: getenv, _credential_from_direct_token, info, _read_secret_from_file_descriptor, expanduser, Path, _iter_claude_code_credential_paths, _load_json_file, _extract_claude_code_credential
  - 环境变量: getenv (L169), getenv (L169), getenv (L183)

#### `ƒ` `load_codex_cli_credential() -> CodexCliCredential | None`  L198
  - _文档首行_（仅供参考）: Load credential from Codex CLI (~/.codex/auth.json).
  - 分支数 3，函数体节点数 133；return: None, CodexCliCredential(access_token=access_token, account_id=account_id, source='codex-cli')
  - 调用: _resolve_credential_path, _load_json_file, get, isinstance, debug, info, CodexCliCredential

## 类
### 类 `ClaudeCodeCredential`  L35  @dataclass
- _文档首行_: Claude Code CLI OAuth credential.
- 类/实例变量:
  - `access_token` = <annotated>
  - `refresh_token` = ''
  - `expires_at` = 0
  - `source` = ''
- 方法:
  #### `prop` `is_expired(self) -> bool`    @property  L44
    - 分支数 1，函数体节点数 35；return: False, time.time() * 1000 > self.expires_at - 60000
    - 调用: time

### 类 `CodexCliCredential`  L51  @dataclass
- _文档首行_: Codex CLI credential.
- 类/实例变量:
  - `access_token` = <annotated>
  - `account_id` = ''
  - `source` = ''

## 文件内调用关系
- `_resolve_credential_path` -> _home_dir
- `_iter_claude_code_credential_paths` -> _home_dir
- `load_claude_code_credential` -> _credential_from_direct_token, _read_secret_from_file_descriptor, _iter_claude_code_credential_paths, _load_json_file, _extract_claude_code_credential
- `load_codex_cli_credential` -> _resolve_credential_path, _load_json_file

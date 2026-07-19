# `backend/packages/harness/deerflow/config/paths.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/paths.py`  ·  行数: 419

## 模块概览
- 函数 9 个，类 1 个，模块级常量 7 个

## 依赖（import）
- 模块: hashlib, logging, os, re, shutil
- `pathlib` -> Path, PureWindowsPath
- `deerflow.config.runtime_paths` -> runtime_home

## 模块级常量
- `VIRTUAL_PATH_PREFIX` = '/mnt/user-data'
- `_SAFE_THREAD_ID_RE` = re.compile('^[A-Za-z0-9_\\-]+$')
- `_SAFE_USER_ID_RE` = re.compile('^[A-Za-z0-9_\\-]+$')
- `_UNSAFE_USER_ID_CHAR_RE` = re.compile('[^A-Za-z0-9_\\-]')
- `_SAFE_USER_ID_DIGEST_HEX_LEN` = 16
- `logger` = logging.getLogger(__name__)
- `_paths` = None

## 函数
#### `ƒ` `_default_local_base_dir() -> Path`  L21
  - _文档首行_（仅供参考）: Return the caller project's writable DeerFlow state directory.
  - 分支数 0，函数体节点数 10；return: runtime_home()
  - 调用: runtime_home

#### `ƒ` `_validate_thread_id(thread_id: str) -> str`  L26
  - _文档首行_（仅供参考）: Validate a thread ID before using it in filesystem paths.
  - 分支数 1，函数体节点数 32；raise: ValueError(f'Invalid thread_id {thread_id!r}: only alphanumeric characters, hyphens, and underscores are allowed.')；return: thread_id
  - 调用: match, ValueError

#### `ƒ` `_validate_user_id(user_id: str) -> str`  L33
  - _文档首行_（仅供参考）: Validate a user ID before using it in filesystem paths.
  - 分支数 1，函数体节点数 32；raise: ValueError(f'Invalid user_id {user_id!r}: only alphanumeric characters, hyphens, and underscores are allowed.')；return: user_id
  - 调用: match, ValueError

#### `ƒ` `make_safe_user_id(raw: str) -> str`  L40
  - _文档首行_（仅供参考）: Normalize an external identity into the user-id charset (``[A-Za-z0-9_-]``).
  - 分支数 2，函数体节点数 71；raise: ValueError('user_id must be a non-empty string.')；return: raw, f'{sanitized}-{digest}'
  - 调用: ValueError, sub, hexdigest, sha256, encode

#### `ƒ` `_legacy_safe_user_id(raw: str, sanitized: str) -> str`  L57
  - _文档首行_（仅供参考）: Bucket name produced by the previous (SHA-1) digest revision for ``raw``.
  - 分支数 0，函数体节点数 45；return: f'{sanitized}-{digest}'
  - 调用: hexdigest, sha1, encode

#### `ƒ` `_join_host_path(base: str, *parts) -> str`  L63
  - _文档首行_（仅供参考）: Join host filesystem path segments while preserving native style.
  - 分支数 4，函数体节点数 92；可变参数（*args/**kwargs）；return: base, str(result)
  - 调用: match, startswith, PureWindowsPath, str, Path

#### `ƒ` `join_host_path(base: str, *parts) -> str`  L86
  - _文档首行_（仅供参考）: Join host filesystem path segments while preserving native style.
  - 分支数 0，函数体节点数 22；可变参数（*args/**kwargs）；return: _join_host_path(base, *parts)
  - 调用: _join_host_path

#### `ƒ` `get_paths() -> Paths`  L401
  - _文档首行_（仅供参考）: Return the global Paths singleton (lazy-initialized).
  - 分支数 1，函数体节点数 22；return: _paths
  - 调用: Paths

#### `ƒ` `resolve_path(path: str) -> Path`  L409
  - _文档首行_（仅供参考）: Resolve *path* to an absolute ``Path``.
  - 分支数 1，函数体节点数 43；return: p.resolve()
  - 调用: Path, is_absolute, get_paths, resolve

## 类
### 类 `Paths`  L91
- _文档首行_: Centralized path configuration for DeerFlow application data.
- 方法:
  #### `prop` `host_base_dir(self) -> Path`    @property  L121
    - _文档首行_（仅供参考）: Host-visible base dir for Docker volume mount sources.
    - 分支数 1，函数体节点数 30；return: Path(env), self.base_dir
    - 调用: getenv, Path
  - 环境变量: getenv (L131)
  #### `prop` `base_dir(self) -> Path`    @property  L142
    - _文档首行_（仅供参考）: Root directory for all application data.
    - 分支数 2，函数体节点数 45；return: self._base_dir, Path(env_home).resolve(), _default_local_base_dir()
    - 调用: getenv, resolve, Path, _default_local_base_dir
  - 环境变量: getenv (L147)
  #### `prop` `memory_file(self) -> Path`    @property  L153
    - _文档首行_（仅供参考）: Path to the persisted memory file: `{base_dir}/memory.json`.
    - 分支数 0，函数体节点数 17；return: self.base_dir / 'memory.json'
  #### `prop` `user_md_file(self) -> Path`    @property  L158
    - _文档首行_（仅供参考）: Path to the global user profile file: `{base_dir}/USER.md`.
    - 分支数 0，函数体节点数 17；return: self.base_dir / 'USER.md'
  #### `prop` `agents_dir(self) -> Path`    @property  L163
    - _文档首行_（仅供参考）: Legacy root for shared (pre user-isolation) custom agents: `{base_dir}/agents/`.
    - 分支数 0，函数体节点数 17；return: self.base_dir / 'agents'
  #### `m` `__init__(self, base_dir: str | Path | None) -> None`  L117
    - 分支数 0，函数体节点数 35
    - 调用: resolve, Path
  #### `m` `_host_base_dir_str(self) -> str`  L135
    - _文档首行_（仅供参考）: Return the host base dir as a raw string for bind mounts.
    - 分支数 1，函数体节点数 28；return: env, str(self.base_dir)
    - 调用: getenv, str
  - 环境变量: getenv (L137)
  #### `m` `agent_dir(self, name: str) -> Path`  L172
    - _文档首行_（仅供参考）: Legacy per-agent directory (no user isolation): `{base_dir}/agents/{name}/`.
    - 分支数 0，函数体节点数 22；return: self.agents_dir / name.lower()
    - 调用: lower
  #### `m` `agent_memory_file(self, name: str) -> Path`  L176
    - _文档首行_（仅供参考）: Legacy per-agent memory file: `{base_dir}/agents/{name}/memory.json`.
    - 分支数 0，函数体节点数 21；return: self.agent_dir(name) / 'memory.json'
    - 调用: agent_dir
  #### `m` `user_dir(self, user_id: str) -> Path`  L180
    - _文档首行_（仅供参考）: Directory for a specific user: `{base_dir}/users/{user_id}/`.
    - 分支数 0，函数体节点数 25；return: self.base_dir / 'users' / _validate_user_id(user_id)
    - 调用: _validate_user_id
  #### `m` `prepare_user_dir_for_raw_id(self, raw_user_id: str) -> str`  L184
    - _文档首行_（仅供参考）: Return the safe user ID and migrate this ID's legacy unsafe-id bucket.
    - 分支数 3，函数体节点数 119；return: safe_user_id
    - 调用: make_safe_user_id, sub, _legacy_safe_user_id, exists, is_dir, rename, info, exception
  - 文件IO: exists (L202), rename (L204)
  #### `m` `user_memory_file(self, user_id: str) -> Path`  L210
    - _文档首行_（仅供参考）: Per-user memory file: `{base_dir}/users/{user_id}/memory.json`.
    - 分支数 0，函数体节点数 21；return: self.user_dir(user_id) / 'memory.json'
    - 调用: user_dir
  #### `m` `user_agents_dir(self, user_id: str) -> Path`  L214
    - _文档首行_（仅供参考）: Per-user root for that user's custom agents: `{base_dir}/users/{user_id}/agents/`.
    - 分支数 0，函数体节点数 21；return: self.user_dir(user_id) / 'agents'
    - 调用: user_dir
  #### `m` `user_agent_dir(self, user_id: str, agent_name: str) -> Path`  L218
    - _文档首行_（仅供参考）: Per-user per-agent directory: `{base_dir}/users/{user_id}/agents/{name}/`.
    - 分支数 0，函数体节点数 28；return: self.user_agents_dir(user_id) / agent_name.lower()
    - 调用: user_agents_dir, lower
  #### `m` `user_agent_memory_file(self, user_id: str, agent_name: str) -> Path`  L222
    - _文档首行_（仅供参考）: Per-user per-agent memory: `{base_dir}/users/{user_id}/agents/{name}/memory.json`.
    - 分支数 0，函数体节点数 26；return: self.user_agent_dir(user_id, agent_name) / 'memory.json'
    - 调用: user_agent_dir
  #### `m` `user_skills_dir(self, user_id: str) -> Path`  L226
    - _文档首行_（仅供参考）: Per-user root for that user's custom skills: `{base_dir}/users/{user_id}/skills/`.
    - 分支数 0，函数体节点数 21；return: self.user_dir(user_id) / 'skills'
    - 调用: user_dir
  #### `m` `user_custom_skills_dir(self, user_id: str) -> Path`  L230
    - _文档首行_（仅供参考）: Per-user custom skills directory: `{base_dir}/users/{user_id}/skills/custom/`.
    - 分支数 0，函数体节点数 21；return: self.user_skills_dir(user_id) / 'custom'
    - 调用: user_skills_dir
  #### `m` `thread_dir(self, thread_id: str, *, user_id: str | None) -> Path`  L239
    - _文档首行_（仅供参考）: Host path for a thread's data.
    - 分支数 1，函数体节点数 56；return: self.user_dir(user_id) / 'threads' / _validate_thread_id(thread_id), self.base_dir / 'threads' / _validate_thread_id(thread_id)
    - 调用: user_dir, _validate_thread_id
  #### `m` `sandbox_work_dir(self, thread_id: str, *, user_id: str | None) -> Path`  L259
    - _文档首行_（仅供参考）: Host path for the agent's workspace directory.
    - 分支数 0，函数体节点数 34；return: self.thread_dir(thread_id, user_id=user_id) / 'user-data' / 'workspace'
    - 调用: thread_dir
  #### `m` `sandbox_uploads_dir(self, thread_id: str, *, user_id: str | None) -> Path`  L267
    - _文档首行_（仅供参考）: Host path for user-uploaded files.
    - 分支数 0，函数体节点数 34；return: self.thread_dir(thread_id, user_id=user_id) / 'user-data' / 'uploads'
    - 调用: thread_dir
  #### `m` `sandbox_outputs_dir(self, thread_id: str, *, user_id: str | None) -> Path`  L275
    - _文档首行_（仅供参考）: Host path for agent-generated artifacts.
    - 分支数 0，函数体节点数 34；return: self.thread_dir(thread_id, user_id=user_id) / 'user-data' / 'outputs'
    - 调用: thread_dir
  #### `m` `acp_workspace_dir(self, thread_id: str, *, user_id: str | None) -> Path`  L283
    - _文档首行_（仅供参考）: Host path for the ACP workspace of a specific thread.
    - 分支数 0，函数体节点数 31；return: self.thread_dir(thread_id, user_id=user_id) / 'acp-workspace'
    - 调用: thread_dir
  #### `m` `sandbox_user_data_dir(self, thread_id: str, *, user_id: str | None) -> Path`  L294
    - _文档首行_（仅供参考）: Host path for the user-data root.
    - 分支数 0，函数体节点数 31；return: self.thread_dir(thread_id, user_id=user_id) / 'user-data'
    - 调用: thread_dir
  #### `m` `host_thread_dir(self, thread_id: str, *, user_id: str | None) -> str`  L302
    - _文档首行_（仅供参考）: Host path for a thread directory, preserving Windows path syntax.
    - 分支数 1，函数体节点数 59；return: _join_host_path(self._host_base_dir_str(), 'users', _validate_user_id(user_id), 'threads', _validate_thread_id(thread_id)), _join_host_path(self._host_base_dir_str(), 'threads', _validate_thread_id(thread_id))
    - 调用: _join_host_path, _host_base_dir_str, _validate_user_id, _validate_thread_id
  #### `m` `host_sandbox_user_data_dir(self, thread_id: str, *, user_id: str | None) -> str`  L308
    - _文档首行_（仅供参考）: Host path for a thread's user-data root.
    - 分支数 0，函数体节点数 32；return: _join_host_path(self.host_thread_dir(thread_id, user_id=user_id), 'user-data')
    - 调用: _join_host_path, host_thread_dir
  #### `m` `host_sandbox_work_dir(self, thread_id: str, *, user_id: str | None) -> str`  L312
    - _文档首行_（仅供参考）: Host path for the workspace mount source.
    - 分支数 0，函数体节点数 32；return: _join_host_path(self.host_sandbox_user_data_dir(thread_id, user_id=user_id), 'workspace')
    - 调用: _join_host_path, host_sandbox_user_data_dir
  #### `m` `host_sandbox_uploads_dir(self, thread_id: str, *, user_id: str | None) -> str`  L316
    - _文档首行_（仅供参考）: Host path for the uploads mount source.
    - 分支数 0，函数体节点数 32；return: _join_host_path(self.host_sandbox_user_data_dir(thread_id, user_id=user_id), 'uploads')
    - 调用: _join_host_path, host_sandbox_user_data_dir
  #### `m` `host_sandbox_outputs_dir(self, thread_id: str, *, user_id: str | None) -> str`  L320
    - _文档首行_（仅供参考）: Host path for the outputs mount source.
    - 分支数 0，函数体节点数 32；return: _join_host_path(self.host_sandbox_user_data_dir(thread_id, user_id=user_id), 'outputs')
    - 调用: _join_host_path, host_sandbox_user_data_dir
  #### `m` `host_acp_workspace_dir(self, thread_id: str, *, user_id: str | None) -> str`  L324
    - _文档首行_（仅供参考）: Host path for the ACP workspace mount source.
    - 分支数 0，函数体节点数 32；return: _join_host_path(self.host_thread_dir(thread_id, user_id=user_id), 'acp-workspace')
    - 调用: _join_host_path, host_thread_dir
  #### `m` `ensure_thread_dirs(self, thread_id: str, *, user_id: str | None) -> None`  L328
    - _文档首行_（仅供参考）: Create all standard sandbox directories for a thread.
    - 分支数 1，函数体节点数 78
    - 调用: sandbox_work_dir, sandbox_uploads_dir, sandbox_outputs_dir, acp_workspace_dir, mkdir, chmod
  - 文件IO: mkdir (L347), chmod (L348)
  #### `m` `delete_thread_dir(self, thread_id: str, *, user_id: str | None) -> None`  L350
    - _文档首行_（仅供参考）: Delete all persisted data for a thread.
    - 分支数 1，函数体节点数 43
    - 调用: thread_dir, exists, rmtree
  - 文件IO: exists (L356)
  #### `m` `resolve_virtual_path(self, thread_id: str, virtual_path: str, *, user_id: str | None) -> Path`  L359
    - _文档首行_（仅供参考）: Resolve a sandbox virtual path to the actual host filesystem path.
    - 分支数 2，函数体节点数 133；raise: ValueError(f'Path must start with /{prefix}'), ValueError('Access denied: path traversal detected')；return: actual
    - 调用: lstrip, startswith, ValueError, len, resolve, sandbox_user_data_dir, relative_to

## 文件内调用关系
- `join_host_path` -> _join_host_path
- `resolve_path` -> get_paths
- `Paths.base_dir` -> _default_local_base_dir
- `Paths.agent_memory_file` -> agent_dir
- `Paths.user_dir` -> _validate_user_id
- `Paths.prepare_user_dir_for_raw_id` -> make_safe_user_id, _legacy_safe_user_id
- `Paths.user_memory_file` -> user_dir
- `Paths.user_agents_dir` -> user_dir
- `Paths.user_agent_dir` -> user_agents_dir
- `Paths.user_agent_memory_file` -> user_agent_dir
- `Paths.user_skills_dir` -> user_dir
- `Paths.user_custom_skills_dir` -> user_skills_dir
- `Paths.thread_dir` -> user_dir, _validate_thread_id
- `Paths.sandbox_work_dir` -> thread_dir
- `Paths.sandbox_uploads_dir` -> thread_dir
- `Paths.sandbox_outputs_dir` -> thread_dir
- `Paths.acp_workspace_dir` -> thread_dir
- `Paths.sandbox_user_data_dir` -> thread_dir
- `Paths.host_thread_dir` -> _join_host_path, _host_base_dir_str, _validate_user_id, _validate_thread_id
- `Paths.host_sandbox_user_data_dir` -> _join_host_path, host_thread_dir
- `Paths.host_sandbox_work_dir` -> _join_host_path, host_sandbox_user_data_dir
- `Paths.host_sandbox_uploads_dir` -> _join_host_path, host_sandbox_user_data_dir
- `Paths.host_sandbox_outputs_dir` -> _join_host_path, host_sandbox_user_data_dir
- `Paths.host_acp_workspace_dir` -> _join_host_path, host_thread_dir
- `Paths.ensure_thread_dirs` -> sandbox_work_dir, sandbox_uploads_dir, sandbox_outputs_dir, acp_workspace_dir
- `Paths.delete_thread_dir` -> thread_dir
- `Paths.resolve_virtual_path` -> sandbox_user_data_dir

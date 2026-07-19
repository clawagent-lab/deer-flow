# `backend/packages/harness/deerflow/sandbox/local/local_sandbox_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/local/local_sandbox_provider.py`  ·  行数: 444

## 模块概览
- 函数 0 个，类 1 个，模块级常量 5 个

## 依赖（import）
- 模块: logging, threading
- `collections` -> OrderedDict
- `pathlib` -> Path
- `deerflow.sandbox.local.local_sandbox` -> LocalSandbox, PathMapping
- `deerflow.sandbox.sandbox` -> Sandbox
- `deerflow.sandbox.sandbox_provider` -> SandboxProvider
- `deerflow.skills.storage` -> user_should_see_legacy_skills

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_singleton` = None
- `_USER_DATA_VIRTUAL_PREFIX` = '/mnt/user-data'
- `_ACP_WORKSPACE_VIRTUAL_PREFIX` = '/mnt/acp-workspace'
- `DEFAULT_MAX_CACHED_THREAD_SANDBOXES` = 256

## 类
### 类 `LocalSandboxProvider`  L35
- 继承: SandboxProvider
- _文档首行_: Local-filesystem sandbox provider with per-thread path scoping.
- 类/实例变量:
  - `uses_thread_data_mounts` = True
  - `needs_upload_permission_adjustment` = False
- 方法:
  #### `st` `_effective_acquire_user_id(user_id: str | None) -> str`    @staticmethod  L210
    - 分支数 0，函数体节点数 22；return: user_id or get_effective_user_id()
    - 调用: get_effective_user_id
  #### `st` `_thread_key(thread_id: str, user_id: str) -> tuple[str, str]`    @staticmethod  L216
    - 分支数 0，函数体节点数 27；return: (user_id, thread_id)
  #### `st` `_sandbox_id_for_thread(thread_id: str, user_id: str) -> str`    @staticmethod  L220
    - 分支数 0，函数体节点数 22；return: f'local:{user_id}:{thread_id}'
  #### `st` `_key_from_sandbox_id(sandbox_id: str) -> tuple[str, str] | None`    @staticmethod  L224
    - 分支数 2，函数体节点数 82；return: None, (user_id, thread_id)
    - 调用: startswith, len, partition
  #### `st` `_build_thread_path_mappings(thread_id: str, *, user_id: str | None) -> list[PathMapping]`    @staticmethod  L234
    - _文档首行_（仅供参考）: Build per-thread path mappings for /mnt/user-data, /mnt/acp-workspace,
    - 分支数 3，函数体节点数 353；return: mappings
    - 调用: get_paths, _effective_acquire_user_id, ensure_thread_dirs, PathMapping, str, sandbox_user_data_dir, sandbox_work_dir, sandbox_uploads_dir, sandbox_outputs_dir, acp_workspace_dir, get_app_config, user_custom_skills_dir, mkdir, append, warning, get_skills_path, user_should_see_legacy_skills, exists
  - 文件IO: mkdir (L290), exists (L314)
  #### `m` `__init__(self, max_cached_threads: int)`  L69
    - _文档首行_（仅供参考）: Initialize the local sandbox provider with static path mappings.
    - 分支数 0，函数体节点数 74
    - 调用: _setup_path_mappings, OrderedDict, Lock
  #### `m` `_setup_path_mappings(self) -> list[PathMapping]`  L83
    - _文档首行_（仅供参考）: Setup static path mappings shared by every sandbox this provider yields.
    - 分支数 8，函数体节点数 315；return: mappings
    - 调用: get_app_config, get_skills_path, exists, append, PathMapping, str, Path, rstrip, is_absolute, warning, startswith, any, resolve, error
  - 文件IO: exists (L109), exists (L183)
  #### `m` `acquire(self, thread_id: str | None, *, user_id: str | None) -> str`  L327
    - _文档首行_（仅供参考）: Return a sandbox id scoped to *thread_id* (or the generic singleton).
    - 分支数 7，函数体节点数 230；return: self._generic_sandbox.id, cached.id
    - 调用: LocalSandbox, list, _effective_acquire_user_id, _thread_key, get, move_to_end, _build_thread_path_mappings, _sandbox_id_for_thread, _evict_until_within_cap_locked
  #### `m` `_evict_until_within_cap_locked(self) -> None`  L377
    - _文档首行_（仅供参考）: LRU-evict cached thread sandboxes once the cap is exceeded.
    - 分支数 1，函数体节点数 57
    - 调用: len, popitem, info
  #### `m` `get(self, sandbox_id: str) -> Sandbox | None`  L391
    - 分支数 8，函数体节点数 129；return: self._generic_sandbox, generic, None, cached
    - 调用: acquire, isinstance, startswith, _key_from_sandbox_id, get, move_to_end
  #### `m` `release(self, sandbox_id: str) -> None`  L414
    - 分支数 0，函数体节点数 8
  #### `m` `reset(self) -> None`  L425
    - _文档首行_（仅供参考）: Drop all cached LocalSandbox instances.
    - 分支数 1，函数体节点数 31
    - 调用: clear
  #### `m` `shutdown(self) -> None`  L439
    - 分支数 0，函数体节点数 10
    - 调用: reset

## 文件内调用关系
- `LocalSandboxProvider.__init__` -> _setup_path_mappings
- `LocalSandboxProvider._build_thread_path_mappings` -> _effective_acquire_user_id
- `LocalSandboxProvider.acquire` -> _effective_acquire_user_id, _thread_key, get, _build_thread_path_mappings, _sandbox_id_for_thread, _evict_until_within_cap_locked
- `LocalSandboxProvider.get` -> acquire, _key_from_sandbox_id, get
- `LocalSandboxProvider.shutdown` -> reset

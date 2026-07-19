# `backend/packages/harness/deerflow/community/aio_sandbox/aio_sandbox_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/aio_sandbox/aio_sandbox_provider.py`  ·  行数: 1026

**模块文档首行**（仅供参考）: AIO Sandbox Provider — orchestrates sandbox lifecycle with pluggable backends.

## 模块概览
- 函数 5 个，类 1 个，模块级常量 7 个

## 依赖（import）
- 模块: asyncio, atexit, hashlib, logging, os, signal, threading, time, uuid
- `concurrent.futures` -> ThreadPoolExecutor
- `deerflow.community.warm_pool_lifecycle` -> DEFAULT_IDLE_TIMEOUT, DEFAULT_REPLICAS, WarmPoolLifecycleMixin
- `deerflow.community.warm_pool_lifecycle` -> _SHARED_IDLE_CHECK_INTERVAL
- `deerflow.config` -> get_app_config
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX, get_paths, join_host_path
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.sandbox.sandbox` -> Sandbox
- `deerflow.sandbox.sandbox_provider` -> SandboxProvider
- `deerflow.skills.storage` -> user_should_see_legacy_skills
- `.aio_sandbox` -> AioSandbox
- `.backend` -> SandboxBackend, wait_for_sandbox_ready, wait_for_sandbox_ready_async
- `.local_backend` -> LocalContainerBackend
- `.remote_backend` -> RemoteSandboxBackend
- `.sandbox_info` -> SandboxInfo

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_IMAGE` = 'enterprise-public-cn-beijing.cr.volces.com/vefaas-public...
- `DEFAULT_PORT` = 8080
- `DEFAULT_CONTAINER_PREFIX` = 'deer-flow-sandbox'
- `IDLE_CHECK_INTERVAL` = _SHARED_IDLE_CHECK_INTERVAL
- `THREAD_LOCK_EXECUTOR_WORKERS` = min(32, (os.cpu_count() or 1) + 4)
- `_THREAD_LOCK_EXECUTOR` = ThreadPoolExecutor(max_workers=THREAD_LOCK_EXECUTOR_WORKE...

## 函数
#### `ƒ` `_lock_file_exclusive(lock_file) -> None`  L63
  - 分支数 1，函数体节点数 46；return: None
  - 调用: flock, seek, locking, fileno

#### `ƒ` `_unlock_file(lock_file) -> None`  L72
  - 分支数 1，函数体节点数 46；return: None
  - 调用: flock, seek, locking, fileno

#### `ƒ` `_open_lock_file(lock_path)`  L81
  - 分支数 0，函数体节点数 12；return: open(lock_path, 'a', encoding='utf-8')
  - 调用: open
  - 文件IO: open (L82)

#### `⏵ƒ` `async _acquire_thread_lock_async(lock: threading.Lock) -> None`  L85
  - _文档首行_（仅供参考）: Acquire a threading.Lock without polling or using the default executor.
  - 分支数 2，函数体节点数 77；raise: bare raise, RuntimeError('Failed to acquire sandbox thread lock')
  - 调用: get_running_loop, run_in_executor, shield, add_done_callback, _release_cancelled_lock_acquire, RuntimeError

#### `ƒ` `_release_cancelled_lock_acquire(lock: threading.Lock, task: asyncio.Future[bool]) -> None`  L100
  - _文档首行_（仅供参考）: Release a lock acquired after its awaiting coroutine was cancelled.
  - 分支数 3，函数体节点数 59；return: None
  - 调用: cancelled, result, warning, release

## 类
### 类 `AioSandboxProvider`  L115
- 继承: WarmPoolLifecycleMixin[SandboxInfo], SandboxProvider
- _文档首行_: Sandbox provider that manages containers running the AIO sandbox.
- 方法:
  #### `prop` `uses_thread_data_mounts(self) -> bool`    @property  L170
    - _文档首行_（仅供参考）: Whether thread workspace/uploads/outputs are visible via mounts.
    - 分支数 0，函数体节点数 19；return: isinstance(self._backend, LocalContainerBackend)
    - 调用: isinstance
  #### `st` `_resolve_env_vars(env_config: dict[str, str]) -> dict[str, str]`    @staticmethod  L229
    - _文档首行_（仅供参考）: Resolve environment variable references (values starting with $).
    - 分支数 2，函数体节点数 100；return: resolved
    - 调用: items, isinstance, startswith, get, str
  #### `st` `_effective_acquire_user_id(user_id: str | None) -> str`    @staticmethod  L288
    - 分支数 0，函数体节点数 20；return: user_id or get_effective_user_id()
    - 调用: get_effective_user_id
  #### `st` `_thread_key(thread_id: str, user_id: str) -> tuple[str, str]`    @staticmethod  L292
    - 分支数 0，函数体节点数 27；return: (user_id, thread_id)
  #### `st` `_deterministic_sandbox_id(thread_id: str, user_id: str) -> str`    @staticmethod  L296
    - _文档首行_（仅供参考）: Generate a deterministic sandbox ID from user/thread scope.
    - 分支数 0，函数体节点数 38；return: hashlib.sha256(f'{user_id}:{thread_id}'.encode()).hexdigest()[:8]
    - 调用: hexdigest, sha256, encode
  #### `st` `_get_thread_mounts(thread_id: str, *, user_id: str | None) -> list[tuple[str, str, bool]]`    @staticmethod  L322
    - _文档首行_（仅供参考）: Get volume mounts for a thread's data directories.
    - 分支数 0，函数体节点数 130；return: [(paths.host_sandbox_work_dir(thread_id, user_id=effective_user_id), f'{VIRTUAL_PATH_PREFIX}/workspace', False), (paths.host_sandbox_uploads_dir(thread_id, user_id=effective_user_id), f'{VIRTUAL_PATH_PREFIX}/uploads', False), (paths.host_sandbox_outputs_dir(thread_id, user_id=effective_user_id), f'{VIRTUAL_PATH_PREFIX}/outputs', False), (paths.host_acp_workspace_dir(thread_id, user_id=effective_user_id), '/mnt/acp-workspace', True)]
    - 调用: get_paths, _effective_acquire_user_id, ensure_thread_dirs, host_sandbox_work_dir, host_sandbox_uploads_dir, host_sandbox_outputs_dir, host_acp_workspace_dir
  #### `st` `_get_skills_mounts(*, user_id: str | None) -> list[tuple[str, str, bool]]`    @staticmethod  L343
    - _文档首行_（仅供参考）: Get skills directory mount configurations for three-way skills layout.
    - 分支数 3，函数体节点数 260；return: mounts
    - 调用: get_app_config, get_skills_path, get, str, exists, append, join_host_path, _effective_acquire_user_id, get_paths, user_custom_skills_dir, mkdir, user_should_see_legacy_skills, warning
  - 文件IO: exists (L367), mkdir (L380), exists (L401)
  #### `m` `__init__(self)`  L139
    - 分支数 1，函数体节点数 228
    - 调用: Lock, Event, _load_config, _create_backend, register, _register_signal_handlers, _reconcile_orphans, get, _start_idle_checker
  #### `m` `_create_backend(self) -> SandboxBackend`  L181
    - _文档首行_（仅供参考）: Create the appropriate backend based on configuration.
    - 分支数 1，函数体节点数 105；return: RemoteSandboxBackend(provisioner_url=provisioner_url, api_key=api_key), LocalContainerBackend(image=self._config['image'], base_port=self._config['port'], container_prefix=self._config['container_prefix'], config_mounts=self._config['mounts'], environment=self._config['environment'])
    - 调用: get, info, RemoteSandboxBackend, LocalContainerBackend
  #### `m` `_load_config(self) -> dict`  L207
    - _文档首行_（仅供参考）: Load sandbox configuration from app config.
    - 分支数 0，函数体节点数 135；return: {'image': sandbox_config.image or DEFAULT_IMAGE, 'port': sandbox_config.port or DEFAULT_PORT, 'container_prefix': sandbox_config.container_prefix or DEFAULT_CONTAINER_PREFIX, 'idle_timeout': idle_timeout if idle_timeout is not None else DEFAULT_IDLE_TIMEOUT, 'replicas': replicas if replicas is not None else DEFAULT_REPLICAS, 'mounts': sandbox_config.mounts or [], 'environment': self._resolve_env_vars(sandbox_config.environment or {}), 'provisioner_url': getattr(sandbox_config, 'provisioner_url', None) or '', 'provisioner_api_key': getattr(sandbox_config, 'provisioner_api_key', None) or ''}
    - 调用: get_app_config, getattr, _resolve_env_vars
  - 反射: getattr (L212), getattr (L213), getattr (L224), getattr (L225)
  #### `m` `_reconcile_orphans(self) -> None`  L242
    - _文档首行_（仅供参考）: Reconcile orphaned containers left by previous process lifecycles.
    - 分支数 5，函数体节点数 169；return: None
    - 调用: list_running, warning, time, float, info, len
  #### `m` `_get_extra_mounts(self, thread_id: str | None, *, user_id: str | None) -> list[tuple[str, str, bool]]`  L306
    - _文档首行_（仅供参考）: Collect all extra mounts for a sandbox (thread-specific + skills).
    - 分支数 2，函数体节点数 125；return: mounts
    - 调用: extend, _get_thread_mounts, info, _get_skills_mounts
  #### `m` `_cleanup_idle_resources(self, idle_timeout: float) -> None`  L416
    - _文档首行_（仅供参考）: Clean AIO resources idle longer than ``idle_timeout`` seconds.
    - 分支数 0，函数体节点数 17
    - 调用: _cleanup_idle_sandboxes
  #### `m` `_cleanup_idle_sandboxes(self, idle_timeout: float) -> None`  L420
    - 分支数 8，函数体节点数 197
    - 调用: time, items, append, info, get, destroy, error, _reap_expired_warm
  #### `m` `_register_signal_handlers(self) -> None`  L457
    - _文档首行_（仅供参考）: Register signal handlers for graceful shutdown.
    - 分支数 6，函数体节点数 210
    - 调用: getsignal, hasattr, shutdown, callable, original, signal, raise_signal, debug
  - 反射: hasattr (L465), hasattr (L471), hasattr (L484)
  #### `m` `_get_thread_lock(self, thread_id: str, user_id: str) -> threading.Lock`  L491
    - _文档首行_（仅供参考）: Get or create an in-process lock for a specific user/thread scope.
    - 分支数 2，函数体节点数 65；return: self._thread_locks[key]
    - 调用: _thread_key, Lock
  #### `m` `_sandbox_id_for_thread(self, thread_id: str | None, user_id: str | None) -> str`  L499
    - _文档首行_（仅供参考）: Return deterministic IDs for thread sandboxes and random IDs otherwise.
    - 分支数 0，函数体节点数 49；return: self._deterministic_sandbox_id(thread_id, self._effective_acquire_user_id(user_id)) if thread_id else str(uuid.uuid4())[:8]
    - 调用: _deterministic_sandbox_id, _effective_acquire_user_id, str, uuid4
  #### `m` `_reuse_in_process_sandbox(self, thread_id: str | None, *, user_id: str | None, post_lock: bool) -> str | None`  L503
    - _文档首行_（仅供参考）: Reuse an active in-process sandbox for a thread if one is still tracked.
    - 分支数 8，函数体节点数 247；return: None, existing_id
    - 调用: _effective_acquire_user_id, _thread_key, get, _check_tracked_sandbox_alive, _drop_unhealthy_sandbox, pop, info, time
  #### `m` `_reclaim_warm_pool_sandbox(self, thread_id: str | None, sandbox_id: str, *, user_id: str | None, post_lock: bool) -> str | None`  L542
    - _文档首行_（仅供参考）: Promote a warm-pool sandbox back to active tracking if available.
    - 分支数 6，函数体节点数 260；return: None, sandbox_id
    - 调用: _effective_acquire_user_id, _thread_key, _check_tracked_sandbox_alive, _drop_unhealthy_sandbox, pop, AioSandbox, time, info
  #### `m` `_recheck_cached_sandbox(self, thread_id: str, sandbox_id: str, *, user_id: str) -> str | None`  L586
    - _文档首行_（仅供参考）: Re-check in-memory caches after acquiring the cross-process file lock.
    - 分支数 0，函数体节点数 48；return: self._reuse_in_process_sandbox(thread_id, user_id=user_id, post_lock=True) or self._reclaim_warm_pool_sandbox(thread_id, sandbox_id, user_id=user_id, post_lock=True)
    - 调用: _reuse_in_process_sandbox, _reclaim_warm_pool_sandbox
  #### `m` `_register_discovered_sandbox(self, thread_id: str, info: SandboxInfo, *, user_id: str) -> str`  L595
    - _文档首行_（仅供参考）: Track a sandbox discovered through the backend.
    - 分支数 1，函数体节点数 137；return: info.sandbox_id
    - 调用: AioSandbox, _thread_key, time, info
  #### `m` `_register_created_sandbox(self, thread_id: str | None, sandbox_id: str, info: SandboxInfo, *, user_id: str | None) -> str`  L608
    - _文档首行_（仅供参考）: Track a newly-created sandbox in the active maps.
    - 分支数 2，函数体节点数 132；return: sandbox_id
    - 调用: AioSandbox, time, _thread_key, _effective_acquire_user_id, info
  #### `m` `_check_tracked_sandbox_alive(self, sandbox_id: str, info: SandboxInfo) -> bool | None`  L621
    - _文档首行_（仅供参考）: Return whether a tracked sandbox appears alive, or None if unknown.
    - 分支数 1，函数体节点数 47；return: self._backend.is_alive(info), None
    - 调用: is_alive, warning
  #### `m` `_remove_tracked_sandbox(self, sandbox_id: str, *, expected_info: SandboxInfo | None) -> tuple[Sandbox | None, SandboxInfo | None, bool]`  L629
    - _文档首行_（仅供参考）: Remove a sandbox from in-process tracking maps.
    - 分支数 4，函数体节点数 251；return: (None, None, False), (sandbox, info, True)
    - 调用: get, pop, items
  #### `m` `_drop_unhealthy_sandbox(self, sandbox_id: str, reason: str, *, expected_info: SandboxInfo | None) -> None`  L664
    - _文档首行_（仅供参考）: Remove and destroy a sandbox after a definitive failed health check.
    - 分支数 5，函数体节点数 137；return: None
    - 调用: _remove_tracked_sandbox, info, close, warning, destroy
  #### `m` `_active_count_locked(self) -> int`  L685
    - _文档首行_（仅供参考）: Return active AIO sandbox count while ``_lock`` is held.
    - 分支数 0，函数体节点数 15；return: len(self._sandboxes)
    - 调用: len
  #### `m` `_destroy_warm_entry(self, sandbox_id: str, entry: SandboxInfo, *, reason: str) -> None`  L689
    - _文档首行_（仅供参考）: Destroy a warm-pool sandbox using AIO-specific backend logging.
    - 分支数 5，函数体节点数 140；return: None
    - 调用: destroy, error, info
  #### `m` `acquire(self, thread_id: str | None, *, user_id: str | None) -> str`  L711
    - _文档首行_（仅供参考）: Acquire a sandbox environment and return its ID.
    - 分支数 2，函数体节点数 72；return: self._acquire_internal(thread_id, user_id=effective_user_id)
    - 调用: _effective_acquire_user_id, _get_thread_lock, _acquire_internal
  #### `m` `_acquire_internal(self, thread_id: str | None, *, user_id: str) -> str`  L752
    - _文档首行_（仅供参考）: Internal sandbox acquisition with two-layer consistency.
    - 分支数 3，函数体节点数 103；return: cached_id, reclaimed_id, self._discover_or_create_with_lock(thread_id, sandbox_id, user_id=user_id), self._create_sandbox(thread_id, sandbox_id, user_id=user_id)
    - 调用: _reuse_in_process_sandbox, _sandbox_id_for_thread, _reclaim_warm_pool_sandbox, _discover_or_create_with_lock, _create_sandbox
  #### `m` `_discover_or_create_with_lock(self, thread_id: str, sandbox_id: str, *, user_id: str | None) -> str`  L801
    - _文档首行_（仅供参考）: Discover an existing sandbox or create a new one under a cross-process file lock.
    - 分支数 5，函数体节点数 171；return: cached_id, self._register_discovered_sandbox(thread_id, discovered, user_id=effective_user_id), self._create_sandbox(thread_id, sandbox_id, user_id=effective_user_id)
    - 调用: get_paths, _effective_acquire_user_id, ensure_thread_dirs, thread_dir, open, _lock_file_exclusive, _recheck_cached_sandbox, discover, _register_discovered_sandbox, _create_sandbox, _unlock_file
  - 文件IO: open (L812)
  #### `m` `_create_sandbox(self, thread_id: str | None, sandbox_id: str, *, user_id: str | None) -> str`  L863
    - _文档首行_（仅供参考）: Create a new sandbox via the backend.
    - 分支数 2，函数体节点数 160；raise: RuntimeError(f'Sandbox {sandbox_id} failed to become ready within timeout at {info.sandbox_url}')；return: self._register_created_sandbox(thread_id, sandbox_id, info, user_id=effective_user_id)
    - 调用: _effective_acquire_user_id, _get_extra_mounts, _replica_count, _evict_oldest_warm, _log_replicas_soft_cap, create, wait_for_sandbox_ready, destroy, RuntimeError, _register_created_sandbox
  #### `m` `get(self, sandbox_id: str) -> Sandbox | None`  L916
    - _文档首行_（仅供参考）: Get a sandbox by ID. Updates last activity timestamp.
    - 分支数 2，函数体节点数 54；return: sandbox
    - 调用: get, time
  #### `m` `release(self, sandbox_id: str) -> None`  L931
    - _文档首行_（仅供参考）: Release a sandbox from active use into the warm pool.
    - 分支数 5，函数体节点数 193
    - 调用: pop, items, time, close, warning, info
  #### `m` `destroy(self, sandbox_id: str) -> None`  L972
    - _文档首行_（仅供参考）: Destroy a sandbox: stop the container and free all resources.
    - 分支数 3，函数体节点数 80
    - 调用: _remove_tracked_sandbox, close, warning, destroy, info
  #### `m` `shutdown(self) -> None`  L1000
    - _文档首行_（仅供参考）: Shutdown all sandboxes. Thread-safe and idempotent.
    - 分支数 6，函数体节点数 172；return: None
    - 调用: list, keys, items, clear, _stop_idle_checker, info, len, destroy, error
  #### `⏵m` `async acquire_async(self, thread_id: str | None, *, user_id: str | None) -> str`  L734
    - _文档首行_（仅供参考）: Acquire a sandbox environment without blocking the event loop.
    - 分支数 2，函数体节点数 84；return: await self._acquire_internal_async(thread_id, user_id=effective_user_id)
    - 调用: _effective_acquire_user_id, _get_thread_lock, _acquire_thread_lock_async, _acquire_internal_async, release
  #### `⏵m` `async _acquire_internal_async(self, thread_id: str | None, *, user_id: str) -> str`  L781
    - _文档首行_（仅供参考）: Async counterpart to ``_acquire_internal``.
    - 分支数 3，函数体节点数 115；return: cached_id, reclaimed_id, await self._discover_or_create_with_lock_async(thread_id, sandbox_id, user_id=user_id), await self._create_sandbox_async(thread_id, sandbox_id, user_id=user_id)
    - 调用: to_thread, _sandbox_id_for_thread, _discover_or_create_with_lock_async, _create_sandbox_async
  #### `⏵m` `async _discover_or_create_with_lock_async(self, thread_id: str, sandbox_id: str, *, user_id: str | None) -> str`  L833
    - _文档首行_（仅供参考）: Async counterpart to ``_discover_or_create_with_lock``.
    - 分支数 4，函数体节点数 209；return: cached_id, self._register_discovered_sandbox(thread_id, discovered, user_id=effective_user_id), await self._create_sandbox_async(thread_id, sandbox_id, user_id=effective_user_id)
    - 调用: get_paths, _effective_acquire_user_id, to_thread, thread_dir, _register_discovered_sandbox, _create_sandbox_async
  #### `⏵m` `async _create_sandbox_async(self, thread_id: str | None, sandbox_id: str, *, user_id: str | None) -> str`  L895
    - _文档首行_（仅供参考）: Async counterpart to ``_create_sandbox``.
    - 分支数 2，函数体节点数 181；raise: RuntimeError(f'Sandbox {sandbox_id} failed to become ready within timeout at {info.sandbox_url}')；return: self._register_created_sandbox(thread_id, sandbox_id, info, user_id=effective_user_id)
    - 调用: _effective_acquire_user_id, to_thread, _replica_count, _log_replicas_soft_cap, wait_for_sandbox_ready_async, RuntimeError, _register_created_sandbox

## 文件内调用关系
- `_acquire_thread_lock_async` -> _release_cancelled_lock_acquire
- `_release_cancelled_lock_acquire` -> release
- `AioSandboxProvider.__init__` -> _load_config, _create_backend, _register_signal_handlers, _reconcile_orphans, get
- `AioSandboxProvider._create_backend` -> get
- `AioSandboxProvider._load_config` -> _resolve_env_vars
- `AioSandboxProvider._resolve_env_vars` -> get
- `AioSandboxProvider._get_extra_mounts` -> _get_thread_mounts, _get_skills_mounts
- `AioSandboxProvider._get_thread_mounts` -> _effective_acquire_user_id
- `AioSandboxProvider._get_skills_mounts` -> get, _effective_acquire_user_id
- `AioSandboxProvider._cleanup_idle_resources` -> _cleanup_idle_sandboxes
- `AioSandboxProvider._cleanup_idle_sandboxes` -> get, destroy
- `AioSandboxProvider._register_signal_handlers` -> shutdown
- `AioSandboxProvider._get_thread_lock` -> _thread_key
- `AioSandboxProvider._sandbox_id_for_thread` -> _deterministic_sandbox_id, _effective_acquire_user_id
- `AioSandboxProvider._reuse_in_process_sandbox` -> _effective_acquire_user_id, _thread_key, get, _check_tracked_sandbox_alive, _drop_unhealthy_sandbox
- `AioSandboxProvider._reclaim_warm_pool_sandbox` -> _effective_acquire_user_id, _thread_key, _check_tracked_sandbox_alive, _drop_unhealthy_sandbox
- `AioSandboxProvider._recheck_cached_sandbox` -> _reuse_in_process_sandbox, _reclaim_warm_pool_sandbox
- `AioSandboxProvider._register_discovered_sandbox` -> _thread_key
- `AioSandboxProvider._register_created_sandbox` -> _thread_key, _effective_acquire_user_id
- `AioSandboxProvider._remove_tracked_sandbox` -> get
- `AioSandboxProvider._drop_unhealthy_sandbox` -> _remove_tracked_sandbox, destroy
- `AioSandboxProvider._destroy_warm_entry` -> destroy
- `AioSandboxProvider.acquire` -> _effective_acquire_user_id, _get_thread_lock, _acquire_internal
- `AioSandboxProvider.acquire_async` -> _effective_acquire_user_id, _get_thread_lock, _acquire_thread_lock_async, _acquire_internal_async, release
- `AioSandboxProvider._acquire_internal` -> _reuse_in_process_sandbox, _sandbox_id_for_thread, _reclaim_warm_pool_sandbox, _discover_or_create_with_lock, _create_sandbox
- `AioSandboxProvider._acquire_internal_async` -> _sandbox_id_for_thread, _discover_or_create_with_lock_async, _create_sandbox_async
- `AioSandboxProvider._discover_or_create_with_lock` -> _effective_acquire_user_id, _lock_file_exclusive, _recheck_cached_sandbox, _register_discovered_sandbox, _create_sandbox, _unlock_file
- `AioSandboxProvider._discover_or_create_with_lock_async` -> _effective_acquire_user_id, _register_discovered_sandbox, _create_sandbox_async
- `AioSandboxProvider._create_sandbox` -> _effective_acquire_user_id, _get_extra_mounts, destroy, _register_created_sandbox
- `AioSandboxProvider._create_sandbox_async` -> _effective_acquire_user_id, _register_created_sandbox
- `AioSandboxProvider.get` -> get
- `AioSandboxProvider.destroy` -> _remove_tracked_sandbox, destroy
- `AioSandboxProvider.shutdown` -> destroy

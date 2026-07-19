# `backend/packages/harness/deerflow/community/e2b_sandbox/e2b_sandbox_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/e2b_sandbox/e2b_sandbox_provider.py`  ·  行数: 1085

**模块文档首行**（仅供参考）: ``E2BSandboxProvider`` — DeerFlow :class:`SandboxProvider` for e2b cloud.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 9 个

## 依赖（import）
- 模块: asyncio, atexit, hashlib, logging, os, shlex, signal, threading, time, uuid
- `__future__` -> annotations
- `collections` -> OrderedDict
- `pathlib` -> Path
- `typing` -> Any
- `e2b_code_interpreter` -> E2BClientSandbox
- `deerflow.config` -> get_app_config
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.sandbox.sandbox` -> Sandbox
- `deerflow.sandbox.sandbox_provider` -> SandboxProvider
- `.e2b_sandbox` -> DEFAULT_E2B_HOME_DIR, E2BSandbox, _is_sandbox_gone_error

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_TEMPLATE` = 'code-interpreter-v1'
- `DEFAULT_IDLE_TIMEOUT` = 1800
- `DEFAULT_REPLICAS` = 3
- `MAX_E2B_TIMEOUT` = 24 * 60 * 60
- `META_KEY_USER` = 'deer_flow_user'
- `META_KEY_THREAD` = 'deer_flow_thread'
- `META_KEY_PROVIDER` = 'deer_flow_provider'
- `META_VAL_PROVIDER` = 'e2b_sandbox_provider'

## 类
### 类 `E2BSandboxProvider`  L68
- 继承: SandboxProvider
- _文档首行_: Sandbox provider backed by the e2b code-interpreter cloud SDK.
- 类/实例变量:
  - `uses_thread_data_mounts` = False
  - `needs_upload_permission_adjustment` = True
  - `_SYNC_BACK_SUBDIRS` = ('outputs', 'workspace')
- 方法:
  #### `st` `_resolve_env_vars(env_config: dict[str, str]) -> dict[str, str]`    @staticmethod  L128
    - 分支数 2，函数体节点数 110；return: resolved
    - 调用: items, isinstance, startswith, get, str
  #### `st` `_effective_acquire_user_id(user_id: str | None) -> str`    @staticmethod  L144
    - 分支数 0，函数体节点数 20；return: user_id or get_effective_user_id()
    - 调用: get_effective_user_id
  #### `st` `_thread_key(thread_id: str, user_id: str) -> tuple[str, str]`    @staticmethod  L148
    - 分支数 0，函数体节点数 27；return: (user_id, thread_id)
  #### `st` `_stable_seed(thread_id: str, user_id: str) -> str`    @staticmethod  L152
    - 分支数 0，函数体节点数 36；return: hashlib.sha256(f'{user_id}:{thread_id}'.encode()).hexdigest()[:16]
    - 调用: hexdigest, sha256, encode
  #### `st` `_client_alive(client: E2BClientSandbox) -> bool`    @staticmethod  L553
    - _文档首行_（仅供参考）: Best-effort liveness probe for a freshly reconnected e2b client.
    - 分支数 2，函数体节点数 45；return: True, False
    - 调用: run, _is_sandbox_gone_error, debug
  - 子进程: run (L568)
  #### `st` `_safe_close_client(client: E2BClientSandbox | None) -> None`    @staticmethod  L577
    - _文档首行_（仅供参考）: Close the host-side HTTP client of *client* without ever raising.
    - 分支数 5，函数体节点数 91；return: None
    - 调用: getattr, callable, close, debug
  - 反射: getattr (L587), getattr (L590)
  #### `st` `_upload_tree(client: E2BClientSandbox, src: Path, dest_dir: str, read_only: bool) -> None`    @staticmethod  L857
    - _文档首行_（仅供参考）: Recursively upload ``src`` into ``dest_dir`` inside the sandbox.
    - 分支数 12，函数体节点数 236；return: None
    - 调用: is_file, open, write, read, run, quote, rglob, as_posix, relative_to, getattr, callable, rsplit, make_dir
  - 文件IO: open (L866), write (L867), read (L867), rglob (L875), open (L888), write (L889), read (L889)
  - 子进程: run (L870), run (L892)
  - 反射: getattr (L881)
  #### `m` `__init__(self) -> None`  L79
    - 分支数 0，函数体节点数 138
    - 调用: Lock, OrderedDict, _load_config, register, _register_signal_handlers
  #### `m` `_load_config(self) -> dict[str, Any]`  L97
    - _文档首行_（仅供参考）: Read e2b options off ``SandboxConfig`` (``extra="allow"``).
    - 分支数 2，函数体节点数 195；return: getattr(sandbox_config, name, default), {'api_key': api_key, 'template': _opt('template') or _opt('image') or DEFAULT_TEMPLATE, 'domain': _opt('domain'), 'home_dir': _opt('home_dir') or DEFAULT_E2B_HOME_DIR, 'idle_timeout': idle_timeout, 'replicas': replicas, 'mounts': _opt('mounts') or [], 'environment': self._resolve_env_vars(_opt('environment') or {})}
    - 调用: get_app_config, getattr, _opt, get, warning, max, min, int, _resolve_env_vars
  - 反射: getattr (L102)
  #### `m` `_get_sandbox_cls(self) -> type[E2BClientSandbox]`  L137
    - _文档首行_（仅供参考）: Return the e2b SDK Sandbox class.
    - 分支数 0，函数体节点数 14；return: E2BClientSandbox
  #### `m` `_register_signal_handlers(self) -> None`  L157
    - 分支数 8，函数体节点数 216；return: None
    - 调用: getsignal, hasattr, shutdown, callable, original, signal, raise_signal, getattr, debug
  - 反射: hasattr (L161), hasattr (L169), getattr (L180)
  #### `m` `_get_thread_lock(self, thread_id: str, user_id: str) -> threading.Lock`  L191
    - 分支数 2，函数体节点数 71；return: lock
    - 调用: _thread_key, get, Lock
  #### `m` `acquire(self, thread_id: str | None, *, user_id: str | None) -> str`  L200
    - 分支数 2，函数体节点数 65；return: self._acquire_internal(thread_id, user_id=effective_user_id)
    - 调用: _effective_acquire_user_id, _get_thread_lock, _acquire_internal
  #### `m` `_acquire_internal(self, thread_id: str | None, *, user_id: str) -> str`  L211
    - 分支数 6，函数体节点数 100；return: cached, reclaimed, discovered, self._create_sandbox(thread_id, user_id=user_id)
    - 调用: _reuse_in_process_sandbox, _reclaim_warm_pool_sandbox, _discover_remote_sandbox, _create_sandbox
  #### `m` `_reuse_in_process_sandbox(self, thread_id: str, *, user_id: str) -> str | None`  L228
    - 分支数 7，函数体节点数 186；return: None, sid
    - 调用: _thread_key, get, pop, ping, warning, close, _refresh_remote_timeout, debug, info
  #### `m` `_reclaim_warm_pool_sandbox(self, thread_id: str, *, user_id: str) -> str | None`  L273
    - 分支数 6，函数体节点数 255；return: None, target_id
    - 调用: _thread_key, _stable_seed, next, items, pop, _get_sandbox_cls, _reconnect_client, warning, _client_alive, _safe_close_client, _refresh_remote_timeout, _bootstrap_sandbox_paths, debug, E2BSandbox, info
  #### `m` `_discover_remote_sandbox(self, thread_id: str, *, user_id: str) -> str | None`  L327
    - _文档首行_（仅供参考）: Look for a running e2b sandbox tagged with this (user, thread).
    - 分支数 17，函数体节点数 500；生成器（yield）；return: None, target_id
    - 调用: _get_sandbox_cls, _stable_seed, _common_kwargs, list, debug, hasattr, range, next_items, getattr, type, _iter_running, isinstance, get, _reconnect_client, warning, _client_alive, _safe_close_client, _refresh_remote_timeout, _bootstrap_sandbox_paths, E2BSandbox（+2）
  - 反射: hasattr (L380), hasattr (L380), getattr (L390), getattr (L400), getattr (L401)
  #### `m` `_create_sandbox(self, thread_id: str | None, *, user_id: str) -> str`  L448
    - _文档首行_（仅供参考）: Allocate a fresh e2b sandbox and hydrate it with configured mounts.
    - 分支数 11，函数体节点数 400；raise: bare raise；return: sandbox_id
    - 调用: int, len, _evict_oldest_warm, warning, _get_sandbox_cls, _common_kwargs, create, error, getattr, str, uuid4, _bootstrap_sandbox_paths, _apply_mounts, E2BSandbox, _thread_key, info
  - 反射: getattr (L487)
  #### `m` `_common_kwargs(self) -> dict[str, Any]`  L526
    - _文档首行_（仅供参考）: Kwargs shared by ``Sandbox.create``, ``Sandbox.connect`` and ``Sandbox.list``.
    - 分支数 2，函数体节点数 74；return: kwargs
  #### `m` `_reconnect_client(self, sandbox_cls: type[E2BClientSandbox], sandbox_id: str) -> E2BClientSandbox`  L535
    - _文档首行_（仅供参考）: Connect to an existing e2b sandbox by id, with consistent kwargs.
    - 分支数 0，函数体节点数 31；return: sandbox_cls.connect(sandbox_id, **self._common_kwargs())
    - 调用: connect, _common_kwargs
  #### `m` `_refresh_remote_timeout(self, client: E2BClientSandbox) -> None`  L539
    - _文档首行_（仅供参考）: Push the configured idle timeout to the e2b control plane.
    - 分支数 3，函数体节点数 67；return: None
    - 调用: int, getattr, callable, set_timeout, debug
  - 反射: getattr (L544)
  #### `m` `_bootstrap_sandbox_paths(self, client: E2BClientSandbox) -> None`  L600
    - _文档首行_（仅供参考）: Materialise DeerFlow's virtual path layout inside the e2b VM.
    - 分支数 2，函数体节点数 177；return: None
    - 调用: rstrip, quote, run, warning, getattr, strip
  - 子进程: run (L655)
  - 反射: getattr (L663), getattr (L664), getattr (L665)
  #### `m` `_apply_mounts(self, client: E2BClientSandbox) -> None`  L673
    - 分支数 8，函数体节点数 233；return: None
    - 调用: get, Path, getattr, rstrip, bool, exists, warning, startswith, callable, make_dir, debug, _upload_tree
  - 文件IO: exists (L687)
  - 反射: getattr (L679), getattr (L680), getattr (L681), getattr (L698)
  #### `m` `_sync_outputs_to_host(self, sandbox: E2BSandbox, *, thread_id: str, user_id: str) -> None`  L712
    - _文档首行_（仅供参考）: Mirror agent artifacts from the e2b VM back to host thread dirs.
    - 分支数 18，函数体节点数 573；return: None
    - 调用: debug, rstrip, get_paths, thread_dir, join, quote, run, warning, _is_sandbox_gone_error, getattr, split, strip, int, items, startswith, len, exists, stat, download_file, mkdir（+4）
  - 文件IO: exists (L821), stat (L821), mkdir (L839), write_bytes (L841), replace (L842)
  - 子进程: run (L766)
  - 反射: getattr (L774)
  #### `m` `_evict_oldest_warm(self) -> str | None`  L896
    - 分支数 7，函数体节点数 148；return: None, evict_id
    - 调用: popitem, _reconnect_client, _get_sandbox_cls, warning, getattr, callable, kill, close, info
  - 反射: getattr (L913), getattr (L919)
  #### `m` `get(self, sandbox_id: str) -> Sandbox | None`  L928
    - 分支数 1，函数体节点数 27；return: self._sandboxes.get(sandbox_id)
    - 调用: get
  #### `m` `release(self, sandbox_id: str) -> None`  L932
    - _文档首行_（仅供参考）: Park a sandbox in the warm pool while keeping the cloud VM alive.
    - 分支数 12，函数体节点数 320；return: None
    - 调用: pop, items, _stable_seed, info, _kill_and_close, _sync_outputs_to_host, warning, _refresh_remote_timeout, debug, close, time, move_to_end
  #### `m` `_kill_and_close(self, sandbox: E2BSandbox) -> None`  L1000
    - 分支数 4，函数体节点数 71
    - 调用: getattr, callable, kill, debug, close
  - 反射: getattr (L1001), getattr (L1003)
  #### `m` `reset(self) -> None`  L1018
    - 分支数 1，函数体节点数 42
    - 调用: clear
  #### `m` `shutdown(self) -> None`  L1025
    - 分支数 12，函数体节点数 247；return: None
    - 调用: list, items, keys, clear, info, len, getattr, callable, kill, warning, close, _get_sandbox_cls, _reconnect_client
  - 反射: getattr (L1044), getattr (L1070), getattr (L1079)
  #### `⏵m` `async acquire_async(self, thread_id: str | None, *, user_id: str | None) -> str`  L207
    - 分支数 0，函数体节点数 45；return: await asyncio.to_thread(self.acquire, thread_id, user_id=effective_user_id)
    - 调用: _effective_acquire_user_id, to_thread

## 文件内调用关系
- `E2BSandboxProvider.__init__` -> _load_config, _register_signal_handlers
- `E2BSandboxProvider._load_config` -> get, _resolve_env_vars
- `E2BSandboxProvider._resolve_env_vars` -> get
- `E2BSandboxProvider._register_signal_handlers` -> shutdown
- `E2BSandboxProvider._get_thread_lock` -> _thread_key, get
- `E2BSandboxProvider.acquire` -> _effective_acquire_user_id, _get_thread_lock, _acquire_internal
- `E2BSandboxProvider.acquire_async` -> _effective_acquire_user_id
- `E2BSandboxProvider._acquire_internal` -> _reuse_in_process_sandbox, _reclaim_warm_pool_sandbox, _discover_remote_sandbox, _create_sandbox
- `E2BSandboxProvider._reuse_in_process_sandbox` -> _thread_key, get, _refresh_remote_timeout
- `E2BSandboxProvider._reclaim_warm_pool_sandbox` -> _thread_key, _stable_seed, _get_sandbox_cls, _reconnect_client, _client_alive, _safe_close_client, _refresh_remote_timeout, _bootstrap_sandbox_paths
- `E2BSandboxProvider._discover_remote_sandbox` -> _get_sandbox_cls, _stable_seed, _common_kwargs, get, _reconnect_client, _client_alive, _safe_close_client, _refresh_remote_timeout, _bootstrap_sandbox_paths, _thread_key
- `E2BSandboxProvider._create_sandbox` -> _evict_oldest_warm, _get_sandbox_cls, _common_kwargs, _bootstrap_sandbox_paths, _apply_mounts, _thread_key
- `E2BSandboxProvider._reconnect_client` -> _common_kwargs
- `E2BSandboxProvider._apply_mounts` -> get, _upload_tree
- `E2BSandboxProvider._evict_oldest_warm` -> _reconnect_client, _get_sandbox_cls
- `E2BSandboxProvider.get` -> get
- `E2BSandboxProvider.release` -> _stable_seed, _kill_and_close, _sync_outputs_to_host, _refresh_remote_timeout
- `E2BSandboxProvider.shutdown` -> _get_sandbox_cls, _reconnect_client

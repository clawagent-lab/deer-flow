# `backend/packages/harness/deerflow/community/boxlite/provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/boxlite/provider.py`  ·  行数: 544

**模块文档首行**（仅供参考）: ``BoxliteProvider`` — DeerFlow :class:`SandboxProvider` backed by BoxLite.

## 模块概览
- 函数 3 个，类 3 个，模块级常量 5 个

## 依赖（import）
- 模块: asyncio, atexit, hashlib, logging, threading, time, uuid
- `__future__` -> annotations
- `collections.abc` -> Awaitable
- `typing` -> TYPE_CHECKING, Any, TypeVar
- `deerflow.config` -> get_app_config
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.sandbox.sandbox` -> Sandbox
- `deerflow.sandbox.sandbox_provider` -> SandboxProvider
- `..warm_pool_lifecycle` -> WarmPoolLifecycleMixin
- `.box` -> BoxliteBox

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `T` = TypeVar('T')
- `DEFAULT_IMAGE` = 'python:3.12-slim'
- `_BOX_NAME_PREFIX` = 'deer-flow-boxlite-'
- `_VIRTUAL_DIRS` = (f'{VIRTUAL_PATH_PREFIX}/workspace', f'{VIRTUAL_PATH_PREF...

## 函数
#### `ƒ` `_import_simplebox() -> type[SimpleBox]`  L54
  - _文档首行_（仅供参考）: Import BoxLite's async ``SimpleBox`` lazily.
  - 分支数 1，函数体节点数 26；raise: ImportError("BoxliteProvider requires the optional 'boxlite' dependency. Install it with: pip install 'deerflow-harness[boxlite]' or pip install boxlite.")；return: SimpleBox
  - 调用: ImportError

#### `ƒ` `_import_sync_boxlite_runtime()`  L67
  - _文档首行_（仅供参考）: Import BoxLite's sync runtime lazily for startup reconciliation.
  - 分支数 1，函数体节点数 20；raise: ImportError("BoxliteProvider requires the optional 'boxlite' dependency. Install it with: pip install 'deerflow-harness[boxlite]' or pip install boxlite.")；return: SyncBoxlite
  - 调用: ImportError

#### `ƒ` `_run_sync_adapter(coro: Awaitable[T], *, timeout: float | None) -> T`  L149
  - _文档首行_（仅供参考）: Run sync-adapter coroutines without using the BoxLite async loop.
  - 分支数 1，函数体节点数 51；return: asyncio.run(coro), asyncio.run(asyncio.wait_for(coro, timeout=timeout))
  - 调用: run, wait_for
  - 子进程: run (L152), run (L153)

## 类
### 类 `_EventLoopThread`  L76
- _文档首行_: A private asyncio event loop running on a dedicated daemon thread.
- 方法:
  #### `m` `__init__(self) -> None`  L87
    - 分支数 0，函数体节点数 64
    - 调用: Event, Thread, start, wait
  #### `m` `_run_forever(self) -> None`  L94
    - 分支数 0，函数体节点数 46
    - 调用: new_event_loop, set_event_loop, call_soon, run_forever
  #### `m` `run(self, coro: Awaitable[T], *, timeout: float | None) -> T`  L100
    - 分支数 1，函数体节点数 49；raise: RuntimeError('BoxLite event loop is not ready')；return: asyncio.run_coroutine_threadsafe(coro, self._loop).result(timeout)
    - 调用: RuntimeError, result, run_coroutine_threadsafe
  #### `m` `close(self) -> None`  L105
    - 分支数 3，函数体节点数 77；return: None
    - 调用: call_soon_threadsafe, getattr, wake, join, is_running, close
  - 反射: getattr (L109)

### 类 `_SyncBoxAdapter`  L117
- _文档首行_: Adapt a sync BoxLite ``Box`` handle to the async ``SimpleBox`` methods we use.
- 方法:
  #### `m` `__init__(self, runtime: Any, box: Any) -> None`  L120
    - 分支数 0，函数体节点数 24
  #### `⏵m` `async exec(self, cmd: str, *args, env: dict[str, str] | None, user: str | None, timeout: float | None, cwd: str | None) -> Any`  L124
    - 分支数 0，函数体节点数 73；可变参数（*args/**kwargs）；return: self._box.exec(cmd, *args, env=env, user=user, timeout=timeout, cwd=cwd)
    - 调用: exec
  - 危险执行: exec (L133)
  #### `⏵m` `async stop(self) -> None`  L142
    - 分支数 1，函数体节点数 21
    - 调用: stop

### 类 `BoxliteProvider`  L156
- 继承: WarmPoolLifecycleMixin[BoxliteBox], SandboxProvider
- _文档首行_: Run each DeerFlow sandbox as a BoxLite micro-VM.
- 类/实例变量:
  - `uses_thread_data_mounts` = False
  - `needs_upload_permission_adjustment` = True
  - `_idle_checker_thread_name` = 'boxlite-idle-reaper'
- 方法:
  #### `st` `_sandbox_id(thread_id: str, user_id: str) -> str`    @staticmethod  L164
    - _文档首行_（仅供参考）: Deterministic sandbox ID from user/thread scope.
    - 分支数 0，函数体节点数 38；return: hashlib.sha256(f'{user_id}:{thread_id}'.encode()).hexdigest()[:8]
    - 调用: hexdigest, sha256, encode
  #### `st` `_thread_key(thread_id: str, user_id: str | None) -> tuple[str, str]`    @staticmethod  L212
    - 分支数 0，函数体节点数 33；return: (user_id or '', thread_id)
  #### `st` `_box_name(sandbox_id: str) -> str`    @staticmethod  L216
    - 分支数 0，函数体节点数 17；return: f'{_BOX_NAME_PREFIX}{sandbox_id}'
  #### `st` `_sandbox_id_from_box_name(name: str | None) -> str | None`    @staticmethod  L220
    - 分支数 1，函数体节点数 52；return: None, sandbox_id or None
    - 调用: startswith, len
  #### `m` `__init__(self) -> None`  L174
    - 分支数 0，函数体节点数 179
    - 调用: Lock, set, Event, _load_config, _EventLoopThread, register, _reconcile_orphans, _start_idle_checker
  #### `m` `_load_config(self) -> dict[str, Any]`  L190
    - 分支数 0，函数体节点数 134；return: getattr(sandbox_config, name, default), {'image': _opt('image') or DEFAULT_IMAGE, 'memory_mib': _opt('memory_mib'), 'cpus': _opt('cpus'), 'environment': dict(_opt('environment') or {}), 'replicas': replicas if replicas is not None else self.DEFAULT_REPLICAS, 'idle_timeout': idle_timeout if idle_timeout is not None else self.DEFAULT_IDLE_TIMEOUT, 'health_check_skip_seconds': float(health_check_skip_seconds if health_check_skip_seconds is not None else 0.0)}
    - 调用: get_app_config, getattr, _opt, dict, float
  - 反射: getattr (L194)
  #### `m` `_lock_for_sandbox(self, sandbox_id: str) -> threading.Lock`  L226
    - _文档首行_（仅供参考）: Return the per-sandbox acquire lock for a deterministic sandbox id.
    - 分支数 2，函数体节点数 58；return: lock
    - 调用: get, Lock
  #### `m` `_start_idle_checker(self) -> None`  L235
    - _文档首行_（仅供参考）: Start idle cleanup when enabled; idle_timeout=0 keeps it disabled.
    - 分支数 1，函数体节点数 25；return: None
    - 调用: _start_idle_checker, super
  #### `m` `_active_count_locked(self) -> int`  L241
    - _文档首行_（仅供参考）: Return active BoxLite box count while ``_lock`` is held.
    - 分支数 0，函数体节点数 15；return: len(self._boxes)
    - 调用: len
  #### `m` `_destroy_warm_entry(self, sandbox_id: str, entry: BoxliteBox, *, reason: str) -> None`  L245
    - _文档首行_（仅供参考）: Close a removed warm-pool entry and log with context.
    - 分支数 6，函数体节点数 129
    - 调用: discard, close, info, warning
  #### `m` `_invalidate_box(self, sandbox_id: str, reason: str) -> None`  L265
    - _文档首行_（仅供参考）: Destroy and deregister a box after a terminal command-path failure.
    - 分支数 3，函数体节点数 154；return: None
    - 调用: pop, discard, items, warning, close
  #### `m` `_reconcile_orphans(self) -> None`  L283
    - _文档首行_（仅供参考）: Adopt DeerFlow-owned BoxLite boxes left by a previous provider/process.
    - 分支数 2，函数体节点数 51；return: None
    - 调用: _adopt_existing_boxes, debug, warning, info
  #### `m` `_adopt_existing_boxes(self) -> int`  L301
    - 分支数 9，函数体节点数 259；return: adopted
    - 调用: _import_sync_boxlite_runtime, time, start, default, list_info, stop, getattr, _sandbox_id_from_box_name, get, warning, BoxliteBox, _SyncBoxAdapter, info
  - 反射: getattr (L313)
  #### `m` `acquire(self, thread_id: str | None, *, user_id: str | None) -> str`  L345
    - 分支数 8，函数体节点数 232；return: box.id, existing, reclaimed
    - 调用: str, uuid4, _create_box, _thread_key, _sandbox_id, _lock_for_sandbox, get, _reclaim_warm_pool
  #### `m` `_create_box(self, sandbox_id: str) -> BoxliteBox`  L374
    - 分支数 1，函数体节点数 191；return: box, BoxliteBox(sandbox_id, box, self._loop.run, default_env=self._config['environment'], on_terminal_failure=self._invalidate_box)
    - 调用: _replica_count, _evict_oldest_warm, _log_replicas_soft_cap, _import_simplebox, join, simplebox_cls, _box_name, start, exec, run, _make, info, BoxliteBox
  - 子进程: run (L395)
  - 危险执行: exec (L392)
  #### `m` `get(self, sandbox_id: str) -> Sandbox | None`  L399
    - 分支数 1，函数体节点数 27；return: self._boxes.get(sandbox_id)
    - 调用: get
  #### `m` `release(self, sandbox_id: str) -> None`  L403
    - _文档首行_（仅供参考）: Release a sandbox into the warm pool — VM stays running.
    - 分支数 5，函数体节点数 159；return: None
    - 调用: pop, items, discard, time, add, close, info
  #### `m` `_reclaim_warm_pool(self, sandbox_id: str) -> str | None`  L430
    - _文档首行_（仅供参考）: Try to reclaim a warm-pool box by sandbox_id.
    - 分支数 15，函数体节点数 402；return: None, sandbox_id
    - 调用: get, time, pop, discard, warning, close, debug, execute_command, _destroy_warm_entry, info
  #### `m` `reset(self) -> None`  L503
    - _文档首行_（仅供参考）: Release tracked BoxLite VMs to this instance's warm-pool cleanup.
    - 分支数 2，函数体节点数 84
    - 调用: time, items, setdefault, discard, clear
  #### `m` `shutdown(self) -> None`  L521
    - 分支数 5，函数体节点数 147；return: None
    - 调用: _stop_idle_checker, list, values, clear, close, warning

## 文件内调用关系
- `_run_sync_adapter` -> run
- `_EventLoopThread.close` -> close
- `_SyncBoxAdapter.exec` -> exec
- `_SyncBoxAdapter.stop` -> stop
- `BoxliteProvider.__init__` -> _load_config, _reconcile_orphans, _start_idle_checker
- `BoxliteProvider._lock_for_sandbox` -> get
- `BoxliteProvider._start_idle_checker` -> _start_idle_checker
- `BoxliteProvider._destroy_warm_entry` -> close
- `BoxliteProvider._invalidate_box` -> close
- `BoxliteProvider._reconcile_orphans` -> _adopt_existing_boxes
- `BoxliteProvider._adopt_existing_boxes` -> _import_sync_boxlite_runtime, stop, _sandbox_id_from_box_name, get
- `BoxliteProvider.acquire` -> _create_box, _thread_key, _sandbox_id, _lock_for_sandbox, get, _reclaim_warm_pool
- `BoxliteProvider._create_box` -> _import_simplebox, _box_name, exec, run
- `BoxliteProvider.get` -> get
- `BoxliteProvider.release` -> close
- `BoxliteProvider._reclaim_warm_pool` -> get, close, _destroy_warm_entry
- `BoxliteProvider.shutdown` -> close

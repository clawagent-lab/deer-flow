# `backend/packages/harness/deerflow/runtime/runs/manager.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/runs/manager.py`  ·  行数: 1452

**模块文档首行**（仅供参考）: In-memory run registry with optional persistent RunStore backing.

## 模块概览
- 函数 3 个，类 6 个，模块级常量 5 个

## 依赖（import）
- 模块: asyncio, logging, socket, sqlite3, uuid
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `dataclasses` -> dataclass, field
- `datetime` -> UTC, datetime, timedelta
- `enum` -> StrEnum
- `typing` -> TYPE_CHECKING, Any
- `sqlalchemy.exc` -> SAIntegrityError
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel, resolve_user_id
- `deerflow.utils.time` -> is_lease_expired
- `deerflow.utils.time` -> _now_iso
- `.schemas` -> DisconnectMode, RunStatus

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_RETRYABLE_SQLITE_MESSAGES` = ('database is locked', 'database table is locked', 'datab...
- `_RETRYABLE_SQLITE_ERROR_CODES` = {sqlite3.SQLITE_BUSY, sqlite3.SQLITE_LOCKED}
- `_UNIQUE_PGCODE` = '23505'
- `_SQLITE_UNIQUE_ERRORCODE` = sqlite3.SQLITE_CONSTRAINT_UNIQUE

## 函数
#### `ƒ` `_generate_worker_id() -> str`  L48
  - _文档首行_（仅供参考）: Generate a unique worker identifier: ``hostname:hex_uuid``.
  - 分支数 0，函数体节点数 23；return: f'{socket.gethostname()}:{uuid.uuid4().hex}'
  - 调用: gethostname, uuid4

#### `ƒ` `_is_unique_violation(exc: BaseException) -> bool`  L53
  - _文档首行_（仅供参考）: Return True when *exc* (or its cause chain) is a unique-constraint violation.
  - 分支数 12，函数体节点数 216；return: True, False
  - 调用: set, pop, id, add, getattr, isinstance, lower, str, append
  - 反射: getattr (L76), getattr (L78), getattr (L80), getattr (L82), getattr (L102)

#### `ƒ` `_is_retryable_persistence_error(exc: BaseException) -> bool`  L108
  - _文档首行_（仅供参考）: Return True for transient SQLite persistence failures.
  - 分支数 7，函数体节点数 169；return: True, False
  - 调用: set, pop, id, add, lower, str, any, isinstance, getattr, append
  - 反射: getattr (L129), getattr (L132)

## 类
### 类 `PersistenceRetryPolicy`  L139  @dataclass(...)
- _文档首行_: Bounded retry policy for short run-store writes.
- 类/实例变量:
  - `max_attempts` = 5
  - `initial_delay` = 0.05
  - `max_delay` = 1.0
  - `backoff_factor` = 2.0

### 类 `RunRecord`  L149  @dataclass
- _文档首行_: Mutable record for a single run.
- 类/实例变量:
  - `run_id` = <annotated>
  - `thread_id` = <annotated>
  - `assistant_id` = <annotated>
  - `status` = <annotated>
  - `on_disconnect` = <annotated>
  - `multitask_strategy` = 'reject'
  - `metadata` = field(default_factory=dict)
  - `kwargs` = field(default_factory=dict)
  - `user_id` = None
  - `created_at` = ''
  - `updated_at` = ''
  - `task` = field(default=None, repr=False)
  - `abort_event` = field(default_factory=asyncio.Event, repr=False)
  - `abort_action` = 'interrupt'
  - `error` = None
  - `model_name` = None
  - `store_only` = False
  - `total_input_tokens` = 0
  - `total_output_tokens` = 0
  - `total_tokens` = 0
  - `llm_call_count` = 0
  - `lead_agent_tokens` = 0
  - `subagent_tokens` = 0
  - `middleware_tokens` = 0
  - `token_usage_by_model` = field(default_factory=dict)
  - …(+7)

### 类 `RunManager`  L187
- _文档首行_: In-memory run registry with optional persistent RunStore backing.
- 方法:
  #### `prop` `worker_id(self) -> str`    @property  L1166
    - _文档首行_（仅供参考）: Return this worker's unique identifier.
    - 分支数 0，函数体节点数 14；return: self._worker_id
  #### `prop` `heartbeat_enabled(self) -> bool`    @property  L1171
    - _文档首行_（仅供参考）: Return ``True`` when the heartbeat background task should run.
    - 分支数 1，函数体节点数 26；return: False, self._run_ownership_config.heartbeat_enabled
  #### `prop` `grace_seconds(self) -> int`    @property  L1178
    - _文档首行_（仅供参考）: Return the configured grace seconds.
    - 分支数 0，函数体节点数 22；return: self._run_ownership_config.grace_seconds if self._run_ownership_config else 10
  #### `st` `_store_put_payload(record: RunRecord, *, error: str | None, stop_reason: str | None) -> dict[str, Any]`    @staticmethod  L248
    - 分支数 2，函数体节点数 145；return: payload
  #### `st` `_record_from_store(row: dict[str, Any]) -> RunRecord`    @staticmethod  L379
    - _文档首行_（仅供参考）: Build a read-only runtime record from a serialized store row.
    - 分支数 0，函数体节点数 276；return: RunRecord(run_id=row['run_id'], thread_id=row['thread_id'], assistant_id=row.get('assistant_id'), status=RunStatus(row.get('status') or RunStatus.pending.value), on_disconnect=DisconnectMode(row.get('on_disconnect') or DisconnectMode.cancel.value), multitask_strategy=row.get('multitask_strategy') or 'reject', metadata=row.get('metadata') or {}, kwargs=row.get('kwargs') or {}, created_at=row.get('created_at') or '', updated_at=row.get('updated_at') or '', user_id=row.get('user_id'), error=row.get('error'), model_name=row.get('model_name'), store_only=True, total_input_tokens=row.get('total_input_tokens') or 0, total_output_tokens=row.get('total_output_tokens') or 0, total_tokens=row.get('total_tokens') or 0, llm_call_count=row.get('llm_call_count') or 0, lead_agent_tokens=row.get('lead_agent_tokens') or 0, subagent_tokens=row.get('subagent_tokens') or 0, middleware_tokens=row.get('middleware_tokens') or 0, token_usage_by_model=row.get('token_usage_by_model') or {}, message_count=row.get('message_count') or 0, last_ai_message=row.get('last_ai_message'), first_human_message=row.get('first_human_message'), owner_worker_id=row.get('owner_worker_id'), lease_expires_at=row.get('lease_expires_at'), stop_reason=row.get('stop_reason'))
    - 调用: RunRecord, get, RunStatus, DisconnectMode
  #### `m` `__init__(self, store: RunStore | None, *, persistence_retry_policy: PersistenceRetryPolicy | None, worker_id: str | None, run_ownership_config: RunOwnershipConfig | None) -> None`  L195
    - 分支数 0，函数体节点数 145
    - 调用: Lock, PersistenceRetryPolicy, _generate_worker_id
  #### `m` `_index_run_locked(self, record: RunRecord) -> None`  L217
    - _文档首行_（仅供参考）: Register *record* in the thread index. Caller must hold ``self._lock``.
    - 分支数 0，函数体节点数 29
    - 调用: setdefault
  #### `m` `_unindex_run_locked(self, run_id: str, thread_id: str) -> None`  L221
    - _文档首行_（仅供参考）: Drop *run_id* from the thread index. Caller must hold ``self._lock``.
    - 分支数 2，函数体节点数 55
    - 调用: get, pop
  #### `m` `_thread_records_locked(self, thread_id: str) -> list[RunRecord]`  L229
    - _文档首行_（仅供参考）: Return live in-memory records for *thread_id*. Caller must hold ``self._lock``.
    - 分支数 1，函数体节点数 58；return: [], [record for run_id in run_ids if (record := self._runs.get(run_id)) is not None]
    - 调用: get
  #### `m` `_compute_lease_expires_at(self) -> str | None`  L905
    - _文档首行_（仅供参考）: Return the lease expiry ISO timestamp for a freshly created run.
    - 分支数 2，函数体节点数 59；return: None, (datetime.now(UTC) + timedelta(seconds=lease_seconds)).isoformat()
    - 调用: isoformat, now, timedelta
  #### `⏵m` `async _call_store_with_retry(self, operation_name: str, run_id: str, operation: Callable[[], Awaitable[Any]]) -> Any`  L268
    - _文档首行_（仅供参考）: Run a short store operation with bounded retries for SQLite pressure.
    - 分支数 4，函数体节点数 145；raise: bare raise；return: await operation()
    - 调用: operation, _is_retryable_persistence_error, warning, sleep, min
  #### `⏵m` `async _persist_snapshot_to_store(self, run_id: str, payload: dict[str, Any]) -> bool`  L298
    - _文档首行_（仅供参考）: Best-effort persist a previously captured run snapshot.
    - 分支数 2，函数体节点数 74；return: True, False
    - 调用: _call_store_with_retry, put, warning
  #### `⏵m` `async _persist_new_run_to_store(self, record: RunRecord) -> None`  L313
    - _文档首行_（仅供参考）: Persist a newly created run record to the backing store.
    - 分支数 1，函数体节点数 51；return: None
    - 调用: _call_store_with_retry, put, _store_put_payload
  #### `⏵m` `async _persist_to_store(self, record: RunRecord, *, error: str | None) -> bool`  L330
    - _文档首行_（仅供参考）: Best-effort persist run record to backing store.
    - 分支数 0，函数体节点数 38；return: await self._persist_snapshot_to_store(record.run_id, self._store_put_payload(record, error=error))
    - 调用: _persist_snapshot_to_store, _store_put_payload
  #### `⏵m` `async _persist_status(self, record: RunRecord, status: RunStatus, *, error: str | None, stop_reason: str | None) -> bool`  L337
    - _文档首行_（仅供参考）: Best-effort persist a status transition to the backing store.
    - 分支数 5，函数体节点数 200；return: True, False, await self._persist_snapshot_to_store(record.run_id, row_recovery_payload)
    - 调用: _store_put_payload, _call_store_with_retry, update_status, get, warning, info, _persist_snapshot_to_store
  #### `⏵m` `async update_run_completion(self, run_id: str, **kwargs) -> None`  L416
    - _文档首行_（仅供参考）: Persist token usage and completion data to the backing store.
    - 分支数 11，函数体节点数 247；可变参数（*args/**kwargs）；return: None
    - 调用: get, items, hasattr, setattr, _now_iso, _store_put_payload, _call_store_with_retry, update_run_completion, warning, _persist_snapshot_to_store
  - 反射: hasattr (L425), setattr (L426)
  #### `⏵m` `async update_run_progress(self, run_id: str, **kwargs) -> None`  L453
    - _文档首行_（仅供参考）: Persist a running token/message snapshot without changing status.
    - 分支数 7，函数体节点数 147；可变参数（*args/**kwargs）
    - 调用: get, items, hasattr, setattr, _now_iso, update_run_progress, warning
  - 反射: hasattr (L462), setattr (L463)
  #### `⏵m` `async create(self, thread_id: str, assistant_id: str | None, *, on_disconnect: DisconnectMode, metadata: dict | None, kwargs: dict | None, multitask_strategy: str, user_id: str | None) -> RunRecord`  L471
    - _文档首行_（仅供参考）: Create a new pending run and register it.
    - 分支数 3，函数体节点数 229；raise: bare raise；return: record
    - 调用: str, uuid4, _now_iso, _compute_lease_expires_at, RunRecord, _index_run_locked, _persist_new_run_to_store, warning, pop, _unindex_run_locked, info
  #### `⏵m` `async get(self, run_id: str, *, user_id: str | None) -> RunRecord | None`  L527
    - _文档首行_（仅供参考）: Return a run record by ID, or ``None``.
    - 分支数 8，函数体节点数 150；return: record, None, self._record_from_store(row)
    - 调用: get, warning, _record_from_store
  #### `⏵m` `async aget(self, run_id: str, *, user_id: str | None) -> RunRecord | None`  L559
    - _文档首行_（仅供参考）: Return a run record by ID, checking the persistent store as fallback.
    - 分支数 0，函数体节点数 32；return: await self.get(run_id, user_id=user_id)
    - 调用: get
  #### `⏵m` `async list_by_thread(self, thread_id: str, *, user_id: str | None, limit: int) -> list[RunRecord]`  L566
    - _文档首行_（仅供参考）: Return runs for a given thread, newest first, at most ``limit`` records.
    - 分支数 6，函数体节点数 234；return: sorted(memory_records, key=lambda r: r.created_at, reverse=True)[:limit], sorted(records_by_id.values(), key=lambda record: record.created_at, reverse=True)[:limit]
    - 调用: _thread_records_locked, sorted, max, len, list_by_thread, warning, get, _record_from_store, values
  #### `⏵m` `async list_successful_regenerate_sources(self, thread_id: str, *, user_id: str | None | _AutoSentinel) -> set[str]`  L598
    - _文档首行_（仅供参考）: Return all source runs superseded by successful regenerations.
    - 分支数 4，函数体节点数 166；return: sources
    - 调用: resolve_user_id, _thread_records_locked, set, list_successful_regenerate_sources, get, isinstance, discard, add
  #### `⏵m` `async get_many_by_thread(self, thread_id: str, run_ids: set[str], *, user_id: str | None | _AutoSentinel) -> dict[str, RunRecord]`  L630
    - _文档首行_（仅供参考）: Batch-load selected thread runs with in-memory records preferred.
    - 分支数 8，函数体节点数 227；return: {}, records_by_id
    - 调用: resolve_user_id, _thread_records_locked, keys, get_many_by_thread, set, warning, items, _record_from_store
  #### `⏵m` `async set_status(self, run_id: str, status: RunStatus, *, error: str | None, stop_reason: str | None) -> None`  L663
    - _文档首行_（仅供参考）: Transition a run to a new status.
    - 分支数 4，函数体节点数 131；return: None
    - 调用: get, warning, _now_iso, _persist_status, info
  #### `⏵m` `async set_finalizing(self, run_id: str, finalizing: bool) -> None`  L679
    - _文档首行_（仅供参考）: Mark whether a run is performing post-cancel cleanup.
    - 分支数 2，函数体节点数 61；return: None
    - 调用: get, warning, _now_iso
  #### `⏵m` `async wait_for_prior_finalizing(self, thread_id: str, run_id: str, *, poll_interval: float) -> None`  L689
    - _文档首行_（仅供参考）: Wait until older same-thread runs have finished post-cancel cleanup.
    - 分支数 6，函数体节点数 86；return: None
    - 调用: _thread_records_locked, sleep
  #### `⏵m` `async has_later_run(self, thread_id: str, run_id: str) -> bool`  L713
    - _文档首行_（仅供参考）: Return whether a newer in-memory run has been admitted for the thread.
    - 分支数 4，函数体节点数 54；return: True, False
    - 调用: _thread_records_locked
  #### `⏵m` `async has_later_started_run(self, thread_id: str, run_id: str) -> bool`  L725
    - _文档首行_（仅供参考）: Return whether a newer same-thread run may have already advanced state.
    - 分支数 4，函数体节点数 72；return: True, False
    - 调用: _thread_records_locked
  #### `⏵m` `async _persist_model_name(self, run_id: str, model_name: str | None) -> None`  L737
    - _文档首行_（仅供参考）: Best-effort persist model_name update to the backing store.
    - 分支数 2，函数体节点数 62；return: None
    - 调用: _call_store_with_retry, update_model_name, warning
  #### `⏵m` `async update_model_name(self, run_id: str, model_name: str | None) -> None`  L750
    - _文档首行_（仅供参考）: Update the model name for a run.
    - 分支数 2，函数体节点数 86；return: None
    - 调用: get, warning, _now_iso, _persist_model_name, info
  #### `⏵m` `async cancel(self, run_id: str, *, action: str) -> CancelOutcome`  L762
    - _文档首行_（仅供参考）: Request cancellation of a run.
    - 分支数 21，函数体节点数 553；return: CancelOutcome.cancelled, CancelOutcome.not_cancellable, CancelOutcome.taken_over, CancelOutcome.not_active_locally, CancelOutcome.unknown, CancelOutcome.lease_valid_elsewhere
    - 调用: get, set, done, cancel, _now_iso, _persist_status, info, warning, is_lease_expired, _call_store_with_retry, claim_for_takeover
  #### `⏵m` `async create_or_reject(self, thread_id: str, assistant_id: str | None, *, on_disconnect: DisconnectMode, metadata: dict | None, kwargs: dict | None, multitask_strategy: str, model_name: str | None, user_id: str | None) -> RunRecord`  L920
    - _文档首行_（仅供参考）: Atomically check for inflight runs and create a new one.
    - 分支数 17，函数体节点数 649；raise: UnsupportedStrategyError(f"Multitask strategy '{multitask_strategy}' is not yet supported. Supported strategies: {', '.join(_supported_strategies)}"), ConflictError(f'Thread {thread_id} already has an active run'), bare raise；return: record
    - 调用: str, uuid4, _now_iso, UnsupportedStrategyError, join, _compute_lease_expires_at, RunRecord, _thread_records_locked, ConflictError, info, len, _call_store_with_retry, create_run_atomic, _is_unique_violation, range, _index_run_locked, set, done, cancel, append（+1）
  #### `⏵m` `async reconcile_orphaned_inflight_runs(self, *, error: str, before: str | None) -> list[RunRecord]`  L1088
    - _文档首行_（仅供参考）: Mark persisted active runs as failed when their lease has expired.
    - 分支数 8，函数体节点数 264；return: [], recovered
    - 调用: _call_store_with_retry, list_inflight_with_expired_lease, warning, _now_iso, _record_from_store, get, _persist_status, append, len
  #### `⏵m` `async has_inflight(self, thread_id: str) -> bool`  L1146
    - _文档首行_（仅供参考）: Return ``True`` if *thread_id* has a pending or running run.
    - 分支数 1，函数体节点数 53；return: any((r.status in (RunStatus.pending, RunStatus.running) or r.finalizing for r in self._thread_records_locked(thread_id)))
    - 调用: any, _thread_records_locked
  #### `⏵m` `async cleanup(self, run_id: str, *, delay: float) -> None`  L1151
    - _文档首行_（仅供参考）: Remove a run record after an optional delay.
    - 分支数 3，函数体节点数 74
    - 调用: sleep, pop, _unindex_run_locked, debug
  #### `⏵m` `async start_heartbeat(self) -> None`  L1188
    - _文档首行_（仅供参考）: Start the background lease-renewal task.
    - 分支数 2，函数体节点数 82；return: None
    - 调用: done, Event, create_task, _heartbeat_loop, set_name, info
  #### `⏵m` `async stop_heartbeat(self) -> None`  L1203
    - _文档首行_（仅供参考）: Stop the background heartbeat task.
    - 分支数 4，函数体节点数 108
    - 调用: set, done, wait_for, cancel, info
  #### `⏵m` `async _heartbeat_loop(self) -> None`  L1222
    - _文档首行_（仅供参考）: Periodically renew leases and reclaim orphaned runs from dead peers.
    - 分支数 6，函数体节点数 139；return: None
    - 调用: max, is_set, wait_for, wait, _renew_leases, warning, _reconcile_orphans_periodic
  #### `⏵m` `async _renew_leases(self) -> None`  L1266
    - _文档首行_（仅供参考）: Renew the lease on every locally-owned active run.
    - 分支数 6，函数体节点数 254；return: None
    - 调用: isoformat, now, timedelta, items, done, _call_store_with_retry, update_lease, warning, set, cancel
  #### `⏵m` `async _reconcile_orphans_periodic(self) -> None`  L1324
    - _文档首行_（仅供参考）: Sweep for expired leases owned by dead peers.
    - 分支数 1，函数体节点数 37
    - 调用: reconcile_orphaned_inflight_runs, warning, len
  #### `⏵m` `async shutdown(self, *, timeout: float) -> None`  L1339
    - _文档首行_（仅供参考）: Cancel and bounded-await all in-flight runs on process shutdown.
    - 分支数 14，函数体节点数 435；return: None
    - 调用: stop_heartbeat, get_running_loop, time, values, done, set, cancel, wait, cancelled, exception, _now_iso, append, warning, len, wait_for, gather, _persist_status, zip, isinstance, info

### 类 `CancelOutcome`  L1435
- 继承: StrEnum
- _文档首行_: Result of a :meth:`RunManager.cancel` call.
- 类/实例变量:
  - `cancelled` = 'cancelled'
  - `taken_over` = 'taken_over'
  - `lease_valid_elsewhere` = 'lease_valid_elsewhere'
  - `not_cancellable` = 'not_cancellable'
  - `not_active_locally` = 'not_active_locally'
  - `unknown` = 'unknown'

### 类 `ConflictError`  L1446
- 继承: Exception
- _文档首行_: Raised when multitask_strategy=reject and thread has inflight runs.

### 类 `UnsupportedStrategyError`  L1450
- 继承: Exception
- _文档首行_: Raised when a multitask_strategy value is not yet implemented.

## 文件内调用关系
- `RunManager.__init__` -> _generate_worker_id
- `RunManager._unindex_run_locked` -> get
- `RunManager._thread_records_locked` -> get
- `RunManager._call_store_with_retry` -> _is_retryable_persistence_error
- `RunManager._persist_snapshot_to_store` -> _call_store_with_retry
- `RunManager._persist_new_run_to_store` -> _call_store_with_retry, _store_put_payload
- `RunManager._persist_to_store` -> _persist_snapshot_to_store, _store_put_payload
- `RunManager._persist_status` -> _store_put_payload, _call_store_with_retry, get, _persist_snapshot_to_store
- `RunManager._record_from_store` -> get
- `RunManager.update_run_completion` -> get, _store_put_payload, _call_store_with_retry, update_run_completion, _persist_snapshot_to_store
- `RunManager.update_run_progress` -> get, update_run_progress
- `RunManager.create` -> _compute_lease_expires_at, _index_run_locked, _persist_new_run_to_store, _unindex_run_locked
- `RunManager.get` -> get, _record_from_store
- `RunManager.aget` -> get
- `RunManager.list_by_thread` -> _thread_records_locked, list_by_thread, get, _record_from_store
- `RunManager.list_successful_regenerate_sources` -> _thread_records_locked, list_successful_regenerate_sources, get
- `RunManager.get_many_by_thread` -> _thread_records_locked, get_many_by_thread, _record_from_store
- `RunManager.set_status` -> get, _persist_status
- `RunManager.set_finalizing` -> get
- `RunManager.wait_for_prior_finalizing` -> _thread_records_locked
- `RunManager.has_later_run` -> _thread_records_locked
- `RunManager.has_later_started_run` -> _thread_records_locked
- `RunManager._persist_model_name` -> _call_store_with_retry, update_model_name
- `RunManager.update_model_name` -> get, _persist_model_name
- `RunManager.cancel` -> get, cancel, _persist_status, _call_store_with_retry
- `RunManager.create_or_reject` -> _compute_lease_expires_at, _thread_records_locked, _call_store_with_retry, _is_unique_violation, _index_run_locked, cancel, _persist_status
- `RunManager.reconcile_orphaned_inflight_runs` -> _call_store_with_retry, _record_from_store, get, _persist_status
- `RunManager.has_inflight` -> _thread_records_locked
- `RunManager.cleanup` -> _unindex_run_locked
- `RunManager.start_heartbeat` -> _heartbeat_loop
- `RunManager.stop_heartbeat` -> cancel
- `RunManager._heartbeat_loop` -> _renew_leases, _reconcile_orphans_periodic
- `RunManager._renew_leases` -> _call_store_with_retry, cancel
- `RunManager._reconcile_orphans_periodic` -> reconcile_orphaned_inflight_runs
- `RunManager.shutdown` -> stop_heartbeat, cancel, _persist_status

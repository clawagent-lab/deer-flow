# `backend/packages/harness/deerflow/runtime/runs/store/memory.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/runs/store/memory.py`  ·  行数: 376

**模块文档首行**（仅供参考）: In-memory RunStore. Used when database.backend=memory (default) and in tests.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime, timedelta
- `typing` -> Any
- `deerflow.runtime.runs.store.base` -> RunStore

## 类
### 类 `MemoryRunStore`  L14
- 继承: RunStore
- 方法:
  #### `m` `__init__(self) -> None`  L15
    - 分支数 0，函数体节点数 51
  #### `m` `_index_run(self, run_id: str, thread_id: str) -> None`  L23
    - _文档首行_（仅供参考）: Register *run_id* under *thread_id* in the secondary index.
    - 分支数 0，函数体节点数 28
    - 调用: setdefault
  #### `m` `_unindex_run(self, run_id: str, thread_id: str) -> None`  L27
    - _文档首行_（仅供参考）: Drop *run_id* from the *thread_id* bucket, removing the bucket when empty.
    - 分支数 2，函数体节点数 55
    - 调用: get, pop
  #### `⏵m` `async put(self, run_id, *, thread_id, assistant_id, user_id, model_name, status, multitask_strategy, metadata, kwargs, error, stop_reason, created_at, owner_worker_id, lease_expires_at)`  L35
    - 分支数 0，函数体节点数 117
    - 调用: isoformat, now, _index_run
  #### `⏵m` `async get(self, run_id, *, user_id)`  L73
    - 分支数 2，函数体节点数 49；return: None, run
    - 调用: get
  #### `⏵m` `async list_by_thread(self, thread_id, *, user_id, limit)`  L81
    - 分支数 1，函数体节点数 98；return: [], results[:limit]
    - 调用: get, sort
  #### `⏵m` `async list_successful_regenerate_sources(self, thread_id, *, user_id)`  L92
    - 分支数 4，函数体节点数 127；return: sources
    - 调用: get, set, isinstance, add
  #### `⏵m` `async get_many_by_thread(self, thread_id, run_ids, *, user_id)`  L106
    - 分支数 0，函数体节点数 74；return: {run_id: run for run_id in thread_run_ids if run_id in run_ids and (run := self._runs.get(run_id)) is not None and (user_id is None or run.get('user_id') == user_id)}
    - 调用: get
  #### `⏵m` `async update_status(self, run_id, status, *, error, stop_reason)`  L110
    - 分支数 4，函数体节点数 98；return: False, True
    - 调用: get, isoformat, now
  #### `⏵m` `async update_model_name(self, run_id, model_name)`  L126
    - 分支数 1，函数体节点数 50
    - 调用: isoformat, now
  #### `⏵m` `async delete(self, run_id)`  L131
    - 分支数 1，函数体节点数 36
    - 调用: pop, _unindex_run
  #### `⏵m` `async update_run_completion(self, run_id, *, status, **kwargs)`  L136
    - 分支数 3，函数体节点数 88；可变参数（*args/**kwargs）；return: True, False
    - 调用: items, isoformat, now
  #### `⏵m` `async update_run_progress(self, run_id, **kwargs)`  L146
    - 分支数 3，函数体节点数 86；可变参数（*args/**kwargs）
    - 调用: get, items, isoformat, now
  #### `⏵m` `async list_pending(self, *, before)`  L153
    - 分支数 0，函数体节点数 75；return: results
    - 调用: isoformat, now, values, sort
  #### `⏵m` `async list_inflight(self, *, before)`  L159
    - 分支数 0，函数体节点数 78；return: results
    - 调用: isoformat, now, values, sort
  #### `⏵m` `async aggregate_tokens_by_thread(self, thread_id: str, *, include_active: bool) -> dict[str, Any]`  L165
    - 分支数 3，函数体节点数 336；return: {'total_tokens': sum((r.get('total_tokens', 0) for r in completed)), 'total_input_tokens': sum((r.get('total_input_tokens', 0) for r in completed)), 'total_output_tokens': sum((r.get('total_output_tokens', 0) for r in completed)), 'total_runs': len(completed), 'by_model': by_model, 'by_caller': {'lead_agent': sum((r.get('lead_agent_tokens', 0) for r in completed)), 'subagent': sum((r.get('subagent_tokens', 0) for r in completed)), 'middleware': sum((r.get('middleware_tokens', 0) for r in completed))}}
    - 调用: get, items, setdefault, sum, len
  #### `⏵m` `async update_lease(self, run_id: str, *, owner_worker_id: str, lease_expires_at: str) -> bool`  L205
    - 分支数 3，函数体节点数 95；return: False, True
    - 调用: get, isoformat, now
  #### `⏵m` `async claim_for_takeover(self, run_id: str, *, grace_seconds: int, error: str) -> bool`  L224
    - 分支数 3，函数体节点数 105；return: False, True
    - 调用: get, is_lease_expired, isoformat, now
  #### `⏵m` `async list_inflight_with_expired_lease(self, *, before: str | None, grace_seconds: int) -> list[dict[str, Any]]`  L246
    - 分支数 9，函数体节点数 238；return: results
    - 调用: fromisoformat, now, timedelta, values, get, append, replace, sort
  - 文件IO: replace (L280)
  #### `⏵m` `async create_run_atomic(self, run_id: str, *, thread_id: str, owner_worker_id: str, lease_expires_at: str | None, multitask_strategy: str, assistant_id: str | None, user_id: str | None, model_name: str | None, metadata: dict[str, Any] | None, kwargs: dict[str, Any] | None, created_at: str | None, grace_seconds: int) -> tuple[dict[str, Any], list[dict[str, Any]]]`  L288
    - 分支数 12，函数体节点数 478；raise: ConflictError(f'Thread {thread_id} already has an active run'), ConflictError(f'Thread {thread_id} already has an active run owned by another worker')；return: (new_row, claimed)
    - 调用: isoformat, now, timedelta, values, ConflictError, get, fromisoformat, replace, append, _index_run
  - 文件IO: replace (L339)

## 文件内调用关系
- `MemoryRunStore._unindex_run` -> get
- `MemoryRunStore.put` -> _index_run
- `MemoryRunStore.get` -> get
- `MemoryRunStore.list_by_thread` -> get
- `MemoryRunStore.list_successful_regenerate_sources` -> get
- `MemoryRunStore.get_many_by_thread` -> get
- `MemoryRunStore.update_status` -> get
- `MemoryRunStore.delete` -> _unindex_run
- `MemoryRunStore.update_run_progress` -> get
- `MemoryRunStore.aggregate_tokens_by_thread` -> get
- `MemoryRunStore.update_lease` -> get
- `MemoryRunStore.claim_for_takeover` -> get
- `MemoryRunStore.list_inflight_with_expired_lease` -> get
- `MemoryRunStore.create_run_atomic` -> get, _index_run

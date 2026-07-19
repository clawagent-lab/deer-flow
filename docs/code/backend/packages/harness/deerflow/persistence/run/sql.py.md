# `backend/packages/harness/deerflow/persistence/run/sql.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/run/sql.py`  ·  行数: 601

**模块文档首行**（仅供参考）: SQLAlchemy-backed RunStore implementation.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: json
- `__future__` -> annotations
- `datetime` -> UTC, datetime, timedelta
- `typing` -> Any
- `sqlalchemy` -> or_, select, update
- `sqlalchemy.ext.asyncio` -> AsyncSession, async_sessionmaker
- `deerflow.persistence.run.model` -> RunRow
- `deerflow.runtime.runs.store.base` -> RunStore
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel, resolve_user_id
- `deerflow.utils.time` -> coerce_iso

## 函数
#### `ƒ` `_lease_expired_or_null(lease_col, cutoff: datetime)`  L23
  - _文档首行_（仅供参考）: SQLAlchemy filter: True when the lease is NULL or has expired past *cutoff*.
  - 分支数 0，函数体节点数 24；return: or_(lease_col.is_(None), lease_col < cutoff)
  - 调用: or_, is_

## 类
### 类 `RunRepository`  L28
- 继承: RunStore
- 方法:
  #### `st` `_normalize_model_name(model_name: str | None) -> str | None`    @staticmethod  L33
    - _文档首行_（仅供参考）: Normalize model_name for storage: strip whitespace, truncate to 128 chars.
    - 分支数 3，函数体节点数 72；return: None, normalized
    - 调用: isinstance, str, strip, len
  #### `st` `_safe_json(obj: Any) -> Any`    @staticmethod  L45
    - _文档首行_（仅供参考）: Ensure obj is JSON-serializable. Falls back to model_dump() or str().
    - 分支数 9，函数体节点数 156；return: None, obj, {k: RunRepository._safe_json(v) for k, v in obj.items()}, [RunRepository._safe_json(v) for v in obj], obj.model_dump(), obj.dict(), str(obj)
    - 调用: isinstance, _safe_json, items, hasattr, model_dump, dict, dumps, str
  - 反射: hasattr (L55), hasattr (L60)
  #### `st` `_row_to_dict(row: RunRow) -> dict[str, Any]`    @staticmethod  L72
    - 分支数 2，函数体节点数 92；return: d
    - 调用: to_dict, pop, get, isinstance, coerce_iso
  #### `m` `__init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None`  L29
    - 分支数 0，函数体节点数 18
  #### `⏵m` `async put(self, run_id, *, thread_id, assistant_id, user_id: str | None | _AutoSentinel, model_name: str | None, status, multitask_strategy, metadata, kwargs, error, stop_reason: str | None, created_at, follow_up_to_run_id, owner_worker_id: str | None, lease_expires_at: str | None)`  L86
    - _文档首行_（仅供参考）: Insert or update a run row.
    - 分支数 3，函数体节点数 254
    - 调用: resolve_user_id, now, fromisoformat, _normalize_model_name, _safe_json, _sf, get, add, RunRow, items, setattr, commit
  - 网络调用: get (L132)
  - 反射: setattr (L137)
  #### `⏵m` `async get(self, run_id, *, user_id: str | None | _AutoSentinel)`  L140
    - 分支数 3，函数体节点数 82；return: None, self._row_to_dict(row)
    - 调用: resolve_user_id, _sf, get, _row_to_dict
  - 网络调用: get (L148)
  #### `⏵m` `async list_by_thread(self, thread_id, *, user_id: str | None | _AutoSentinel, limit)`  L155
    - 分支数 2，函数体节点数 126；return: [self._row_to_dict(r) for r in result.scalars()]
    - 调用: resolve_user_id, where, select, limit, order_by, desc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async list_successful_regenerate_sources(self, thread_id, *, user_id: str | None | _AutoSentinel)`  L171
    - 分支数 2，函数体节点数 141；return: {value for value in result.scalars() if isinstance(value, str) and value}
    - 调用: resolve_user_id, as_string, where, select, is_not, _sf, execute, scalars, isinstance
  #### `⏵m` `async get_many_by_thread(self, thread_id, run_ids, *, user_id: str | None | _AutoSentinel)`  L191
    - 分支数 3，函数体节点数 125；return: {}, {row.run_id: self._row_to_dict(row) for row in result.scalars()}
    - 调用: resolve_user_id, where, select, in_, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async update_status(self, run_id, status, *, error, stop_reason) -> bool`  L208
    - 分支数 3，函数体节点数 131；return: result.rowcount != 0
    - 调用: now, _sf, execute, values, where, update, in_, commit
  #### `⏵m` `async update_model_name(self, run_id, model_name)`  L224
    - 分支数 1，函数体节点数 63
    - 调用: _sf, execute, values, where, update, _normalize_model_name, now, commit
  #### `⏵m` `async delete(self, run_id, *, user_id: str | None | _AutoSentinel)`  L229
    - 分支数 3，函数体节点数 88；return: None
    - 调用: resolve_user_id, _sf, get, delete, commit
  - 网络调用: get (L237), delete (L242)
  #### `⏵m` `async list_pending(self, *, before)`  L245
    - 分支数 3，函数体节点数 117；return: [self._row_to_dict(r) for r in result.scalars()]
    - 调用: now, isinstance, fromisoformat, order_by, where, select, asc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async list_inflight(self, *, before)`  L257
    - _文档首行_（仅供参考）: Return persisted active runs for startup recovery.
    - 分支数 3，函数体节点数 123；return: [self._row_to_dict(r) for r in result.scalars()]
    - 调用: now, isinstance, fromisoformat, order_by, where, select, in_, asc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async update_run_completion(self, run_id: str, *, status: str, total_input_tokens: int, total_output_tokens: int, total_tokens: int, llm_call_count: int, lead_agent_tokens: int, subagent_tokens: int, middleware_tokens: int, token_usage_by_model: dict[str, dict[str, int]] | None, message_count: int, last_ai_message: str | None, first_human_message: str | None, error: str | None) -> bool`  L277
    - _文档首行_（仅供参考）: Update status + token usage + convenience fields on run completion.
    - 分支数 4，函数体节点数 254；return: result.rowcount != 0
    - 调用: _safe_json, now, _sf, execute, values, where, update, commit
  #### `⏵m` `async update_run_progress(self, run_id: str, *, total_input_tokens: int | None, total_output_tokens: int | None, total_tokens: int | None, llm_call_count: int | None, lead_agent_tokens: int | None, subagent_tokens: int | None, middleware_tokens: int | None, token_usage_by_model: dict[str, dict[str, int]] | None, message_count: int | None, last_ai_message: str | None, first_human_message: str | None) -> None`  L323
    - _文档首行_（仅供参考）: Update token usage + convenience fields while a run is still active.
    - 分支数 6，函数体节点数 289
    - 调用: now, items, _safe_json, _sf, execute, values, where, update, commit
  #### `⏵m` `async aggregate_tokens_by_thread(self, thread_id: str, *, include_active: bool) -> dict[str, Any]`  L364
    - _文档首行_（仅供参考）: Aggregate token usage for a thread.
    - 分支数 4，函数体节点数 352；return: {'total_tokens': total_tokens, 'total_input_tokens': total_input, 'total_output_tokens': total_output, 'total_runs': total_runs, 'by_model': by_model, 'by_caller': {'lead_agent': lead_agent, 'subagent': subagent, 'middleware': middleware}}
    - 调用: in_, where, select, _sf, all, execute, items, setdefault, get
  #### `⏵m` `async update_lease(self, run_id: str, *, owner_worker_id: str, lease_expires_at: str) -> bool`  L440
    - 分支数 1，函数体节点数 126；return: result.rowcount != 0
    - 调用: fromisoformat, now, _sf, execute, values, where, update, in_, commit
  #### `⏵m` `async claim_for_takeover(self, run_id: str, *, grace_seconds: int, error: str) -> bool`  L458
    - 分支数 1，函数体节点数 117；return: result.rowcount != 0
    - 调用: now, timedelta, _sf, execute, values, where, update, in_, _lease_expired_or_null, commit
  #### `⏵m` `async list_inflight_with_expired_lease(self, *, before: str | None, grace_seconds: int) -> list[dict[str, Any]]`  L479
    - 分支数 3，函数体节点数 171；return: [self._row_to_dict(r) for r in result.scalars()]
    - 调用: now, isinstance, fromisoformat, timedelta, order_by, where, select, in_, _lease_expired_or_null, asc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async create_run_atomic(self, run_id: str, *, thread_id: str, owner_worker_id: str, lease_expires_at: str | None, multitask_strategy: str, assistant_id: str | None, user_id: str | None, model_name: str | None, metadata: dict[str, Any] | None, kwargs: dict[str, Any] | None, created_at: str | None, grace_seconds: int) -> tuple[dict[str, Any], list[dict[str, Any]]]`  L505
    - _文档首行_（仅供参考）: Atomically create a run with cross-process thread-uniqueness.
    - 分支数 6，函数体节点数 480；raise: ConflictError(f'Thread {thread_id} already has an active run owned by another worker')；return: (self._row_to_dict(new_row), claimed)
    - 调用: resolve_user_id, now, fromisoformat, timedelta, _normalize_model_name, _safe_json, _sf, with_for_update, where, select, in_, execute, scalars, replace, ConflictError, append, _row_to_dict, add, RunRow, commit（+1）
  - 网络调用: get (L599)
  - 文件IO: replace (L582)

## 文件内调用关系
- `RunRepository._safe_json` -> _safe_json
- `RunRepository._row_to_dict` -> get
- `RunRepository.put` -> _normalize_model_name, _safe_json, get
- `RunRepository.get` -> get, _row_to_dict
- `RunRepository.list_by_thread` -> _row_to_dict
- `RunRepository.get_many_by_thread` -> _row_to_dict
- `RunRepository.update_model_name` -> _normalize_model_name
- `RunRepository.delete` -> get, delete
- `RunRepository.list_pending` -> _row_to_dict
- `RunRepository.list_inflight` -> _row_to_dict
- `RunRepository.update_run_completion` -> _safe_json
- `RunRepository.update_run_progress` -> _safe_json
- `RunRepository.aggregate_tokens_by_thread` -> get
- `RunRepository.claim_for_takeover` -> _lease_expired_or_null
- `RunRepository.list_inflight_with_expired_lease` -> _lease_expired_or_null, _row_to_dict
- `RunRepository.create_run_atomic` -> _normalize_model_name, _safe_json, _row_to_dict, get

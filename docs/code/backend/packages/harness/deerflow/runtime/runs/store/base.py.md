# `backend/packages/harness/deerflow/runtime/runs/store/base.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/runs/store/base.py`  ·  行数: 239

**模块文档首行**（仅供参考）: Abstract interface for run metadata storage.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: abc
- `__future__` -> annotations
- `typing` -> Any

## 类
### 类 `RunStore`  L17
- 继承: abc.ABC
- 方法:
  #### `⏵m` `async put(self, run_id: str, *, thread_id: str, assistant_id: str | None, user_id: str | None, model_name: str | None, status: str, multitask_strategy: str, metadata: dict[str, Any] | None, kwargs: dict[str, Any] | None, error: str | None, stop_reason: str | None, created_at: str | None, owner_worker_id: str | None, lease_expires_at: str | None) -> None`    @abc.abstractmethod  L19
    - 分支数 0，函数体节点数 109
  #### `⏵m` `async get(self, run_id: str, *, user_id: str | None) -> dict[str, Any] | None`    @abc.abstractmethod  L40
    - 分支数 0，函数体节点数 31
  #### `⏵m` `async list_by_thread(self, thread_id: str, *, user_id: str | None, limit: int) -> list[dict[str, Any]]`    @abc.abstractmethod  L49
    - 分支数 0，函数体节点数 36
  #### `⏵m` `async list_successful_regenerate_sources(self, thread_id: str, *, user_id: str | None) -> set[str]`  L58
    - _文档首行_（仅供参考）: Return source run IDs superseded by successful regenerations.
    - 分支数 0，函数体节点数 24；raise: NotImplementedError
  #### `⏵m` `async get_many_by_thread(self, thread_id: str, run_ids: set[str], *, user_id: str | None) -> dict[str, dict[str, Any]]`  L71
    - _文档首行_（仅供参考）: Batch-load selected runs belonging to one thread.
    - 分支数 0，函数体节点数 43；raise: NotImplementedError
  #### `⏵m` `async update_status(self, run_id: str, status: str, *, error: str | None, stop_reason: str | None) -> bool | None`    @abc.abstractmethod  L82
    - _文档首行_（仅供参考）: Update a run status.
    - 分支数 0，函数体节点数 35
  #### `⏵m` `async delete(self, run_id: str) -> None`    @abc.abstractmethod  L98
    - 分支数 0，函数体节点数 12
  #### `⏵m` `async update_model_name(self, run_id: str, model_name: str | None) -> None`    @abc.abstractmethod  L102
    - _文档首行_（仅供参考）: Update the model_name field for an existing run.
    - 分支数 0，函数体节点数 20
  #### `⏵m` `async update_run_completion(self, run_id: str, *, status: str, total_input_tokens: int, total_output_tokens: int, total_tokens: int, llm_call_count: int, lead_agent_tokens: int, subagent_tokens: int, middleware_tokens: int, token_usage_by_model: dict[str, dict[str, int]] | None, message_count: int, last_ai_message: str | None, first_human_message: str | None, error: str | None) -> bool | None`    @abc.abstractmethod  L111
    - _文档首行_（仅供参考）: Persist final completion fields.
    - 分支数 0，函数体节点数 97
  #### `⏵m` `async update_run_progress(self, run_id: str, *, total_input_tokens: int | None, total_output_tokens: int | None, total_tokens: int | None, llm_call_count: int | None, lead_agent_tokens: int | None, subagent_tokens: int | None, middleware_tokens: int | None, token_usage_by_model: dict[str, dict[str, int]] | None, message_count: int | None, last_ai_message: str | None, first_human_message: str | None) -> None`  L135
    - _文档首行_（仅供参考）: Persist a best-effort running snapshot without changing run status.
    - 分支数 0，函数体节点数 104；return: None
  #### `⏵m` `async list_pending(self, *, before: str | None) -> list[dict[str, Any]]`    @abc.abstractmethod  L155
    - 分支数 0，函数体节点数 29
  #### `⏵m` `async list_inflight(self, *, before: str | None) -> list[dict[str, Any]]`    @abc.abstractmethod  L159
    - _文档首行_（仅供参考）: Return persisted runs that are still ``pending`` or ``running``.
    - 分支数 0，函数体节点数 31
  #### `⏵m` `async aggregate_tokens_by_thread(self, thread_id: str, *, include_active: bool) -> dict[str, Any]`    @abc.abstractmethod  L164
    - _文档首行_（仅供参考）: Aggregate token usage for completed runs in a thread.
    - 分支数 0，函数体节点数 27
  #### `⏵m` `async update_lease(self, run_id: str, *, owner_worker_id: str, lease_expires_at: str) -> bool`    @abc.abstractmethod  L174
    - _文档首行_（仅供参考）: Renew the lease on an active run. Returns ``False`` when no row matched.
    - 分支数 0，函数体节点数 21
  #### `⏵m` `async claim_for_takeover(self, run_id: str, *, grace_seconds: int, error: str) -> bool`    @abc.abstractmethod  L185
    - _文档首行_（仅供参考）: Atomically mark an expired-lease active run as ``error``.
    - 分支数 0，函数体节点数 21
  #### `⏵m` `async list_inflight_with_expired_lease(self, *, before: str | None, grace_seconds: int) -> list[dict[str, Any]]`    @abc.abstractmethod  L207
    - _文档首行_（仅供参考）: Return active runs whose lease has expired (or is NULL for pre-ownership rows).
    - 分支数 0，函数体节点数 35
  #### `⏵m` `async create_run_atomic(self, run_id: str, *, thread_id: str, owner_worker_id: str, lease_expires_at: str | None, multitask_strategy: str, assistant_id: str | None, user_id: str | None, model_name: str | None, metadata: dict[str, Any] | None, kwargs: dict[str, Any] | None, created_at: str | None, grace_seconds: int) -> tuple[dict[str, Any], list[dict[str, Any]]]`    @abc.abstractmethod  L217
    - _文档首行_（仅供参考）: Atomically create a run row with cross-process thread-uniqueness.
    - 分支数 0，函数体节点数 121

## 文件内调用关系
_无文件内调用_

# `backend/packages/harness/deerflow/persistence/scheduled_tasks/sql.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/scheduled_tasks/sql.py`  ·  行数: 233

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime, timedelta
- `typing` -> Any
- `sqlalchemy` -> and_, or_, select
- `sqlalchemy.ext.asyncio` -> AsyncSession, async_sessionmaker
- `deerflow.persistence.scheduled_tasks.model` -> ScheduledTaskRow
- `deerflow.utils.time` -> coerce_iso

## 模块级常量
- `TERMINAL_TASK_STATUSES` = frozenset({'completed', 'failed', 'cancelled'})

## 类
### 类 `ScheduledTaskRepository`  L15
- 方法:
  #### `st` `_row_to_dict(row: ScheduledTaskRow) -> dict[str, Any]`    @staticmethod  L20
    - 分支数 2，函数体节点数 65；return: data
    - 调用: to_dict, get, coerce_iso
  #### `m` `__init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None`  L16
    - 分支数 0，函数体节点数 18
  #### `⏵m` `async create(self, *, task_id: str, user_id: str, thread_id: str | None, context_mode: str, assistant_id: str | None, title: str, prompt: str, schedule_type: str, schedule_spec: dict[str, Any], timezone: str, next_run_at: datetime | None) -> dict[str, Any]`  L33
    - 分支数 1，函数体节点数 159；return: self._row_to_dict(row)
    - 调用: now, ScheduledTaskRow, _sf, add, commit, refresh, _row_to_dict
  #### `⏵m` `async get(self, task_id: str, *, user_id: str) -> dict[str, Any] | None`  L70
    - 分支数 2，函数体节点数 70；return: None, self._row_to_dict(row)
    - 调用: _sf, get, _row_to_dict
  - 网络调用: get (L72)
  #### `⏵m` `async list_by_user(self, user_id: str) -> list[dict[str, Any]]`  L77
    - 分支数 1，函数体节点数 93；return: [self._row_to_dict(row) for row in result.scalars()]
    - 调用: order_by, where, select, desc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async update(self, task_id: str, *, user_id: str, updates: dict[str, Any]) -> dict[str, Any] | None`  L83
    - 分支数 4，函数体节点数 139；return: None, self._row_to_dict(row)
    - 调用: _sf, get, items, hasattr, setattr, now, commit, refresh, _row_to_dict
  - 网络调用: get (L91)
  - 反射: hasattr (L95), setattr (L96)
  #### `⏵m` `async delete(self, task_id: str, *, user_id: str) -> bool`  L102
    - 分支数 2，函数体节点数 69；return: False, True
    - 调用: _sf, get, delete, commit
  - 网络调用: get (L104), delete (L107)
  #### `⏵m` `async claim_due_tasks(self, *, now: datetime, lease_owner: str, lease_seconds: int, limit: int) -> list[dict[str, Any]]`  L111
    - 分支数 2，函数体节点数 243；return: [self._row_to_dict(row) for row in rows]
    - 调用: timedelta, with_for_update, limit, order_by, where, select, is_not, or_, and_, is_, asc, _sf, execute, list, scalars, now, commit, _row_to_dict
  #### `⏵m` `async update_after_launch(self, task_id: str, *, status: str, next_run_at: datetime | None, last_run_at: datetime | None, last_run_id: str | None, last_thread_id: str | None, last_error: str | None, increment_run_count: bool, protect_terminal: bool) -> None`  L158
    - 分支数 4，函数体节点数 173；return: None
    - 调用: _sf, get, now, commit
  - 网络调用: get (L172)
  #### `⏵m` `async list_by_user_and_thread(self, user_id: str, thread_id: str) -> list[dict[str, Any]]`  L195
    - 分支数 1，函数体节点数 104；return: [self._row_to_dict(row) for row in result.scalars()]
    - 调用: order_by, where, select, desc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async cancel_stuck_once_tasks(self, *, error: str) -> int`  L208
    - _文档首行_（仅供参考）: Reconcile ``once`` tasks orphaned in ``running`` by a process crash.
    - 分支数 2，函数体节点数 122；return: len(rows)
    - 调用: where, select, is_, _sf, execute, list, scalars, now, commit, len

## 文件内调用关系
- `ScheduledTaskRepository._row_to_dict` -> get
- `ScheduledTaskRepository.create` -> _row_to_dict
- `ScheduledTaskRepository.get` -> get, _row_to_dict
- `ScheduledTaskRepository.list_by_user` -> _row_to_dict
- `ScheduledTaskRepository.update` -> get, _row_to_dict
- `ScheduledTaskRepository.delete` -> get, delete
- `ScheduledTaskRepository.claim_due_tasks` -> _row_to_dict
- `ScheduledTaskRepository.update_after_launch` -> get
- `ScheduledTaskRepository.list_by_user_and_thread` -> _row_to_dict

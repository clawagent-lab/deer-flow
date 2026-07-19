# `backend/packages/harness/deerflow/persistence/scheduled_task_runs/sql.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/scheduled_task_runs/sql.py`  ·  行数: 140

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any
- `sqlalchemy` -> func, select
- `sqlalchemy.ext.asyncio` -> AsyncSession, async_sessionmaker
- `deerflow.persistence.scheduled_task_runs.model` -> ScheduledTaskRunRow
- `deerflow.utils.time` -> coerce_iso

## 模块级常量
- `TERMINAL_RUN_STATUSES` = frozenset({'success', 'failed', 'skipped', 'interrupted'})
- `ACTIVE_RUN_STATUSES` = ('queued', 'running')

## 类
### 类 `ScheduledTaskRunRepository`  L16
- 方法:
  #### `st` `_row_to_dict(row: ScheduledTaskRunRow) -> dict[str, Any]`    @staticmethod  L21
    - 分支数 2，函数体节点数 64；return: data
    - 调用: to_dict, get, coerce_iso
  #### `m` `__init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None`  L17
    - 分支数 0，函数体节点数 18
  #### `⏵m` `async create(self, *, run_record_id: str, task_id: str, thread_id: str, scheduled_for: datetime, trigger: str, status: str) -> dict[str, Any]`  L28
    - 分支数 1，函数体节点数 104；return: self._row_to_dict(row)
    - 调用: ScheduledTaskRunRow, now, _sf, add, commit, refresh, _row_to_dict
  #### `⏵m` `async list_by_task(self, task_id: str, *, limit: int, offset: int) -> list[dict[str, Any]]`  L53
    - 分支数 1，函数体节点数 111；return: [self._row_to_dict(row) for row in result.scalars()]
    - 调用: offset, limit, order_by, where, select, desc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async count_active_runs(self) -> int`  L68
    - _文档首行_（仅供参考）: Global count of queued/running rows, used to bound cross-task concurrency.
    - 分支数 1，函数体节点数 67；return: int(result.scalar() or 0)
    - 调用: where, select_from, select, count, in_, _sf, execute, int, scalar
  #### `⏵m` `async update_status(self, run_record_id: str, *, status: str, run_id: str | None, error: str | None, started_at: datetime | None, finished_at: datetime | None, protect_terminal: bool) -> None`  L75
    - 分支数 7，函数体节点数 190；return: None
    - 调用: _sf, get, commit
  - 网络调用: get (L87)
  #### `⏵m` `async has_active_runs(self, task_id: str) -> bool`  L109
    - 分支数 1，函数体节点数 74；return: result.scalars().first() is not None
    - 调用: limit, where, select, in_, _sf, execute, first, scalars
  #### `⏵m` `async mark_stale_active_runs(self, *, error: str) -> int`  L122
    - _文档首行_（仅供参考）: Fail-fast bookkeeping for runs orphaned by a process crash.
    - 分支数 2，函数体节点数 109；return: len(rows)
    - 调用: where, select, in_, now, _sf, execute, list, scalars, commit, len

## 文件内调用关系
- `ScheduledTaskRunRepository.create` -> _row_to_dict
- `ScheduledTaskRunRepository.list_by_task` -> _row_to_dict

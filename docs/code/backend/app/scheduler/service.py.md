# `backend/app/scheduler/service.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/scheduler/service.py`  ·  行数: 347

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, logging, socket, uuid
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any, Literal
- `fastapi` -> HTTPException
- `deerflow.runtime` -> ConflictError, RunRecord
- `deerflow.scheduler.schedules` -> next_run_at

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `ScheduledTaskService`  L18
- 方法:
  #### `st` `_is_overlap_conflict(exc: Exception) -> bool`    @staticmethod  L57
    - 分支数 1，函数体节点数 36；return: True, isinstance(exc, HTTPException) and exc.status_code == 409
    - 调用: isinstance
  #### `st` `_task_status_for_failure(task: dict[str, Any], *, trigger: str) -> str`    @staticmethod  L63
    - 分支数 2，函数体节点数 49；return: task.get('status') or 'enabled', 'failed', 'enabled'
    - 调用: get
  #### `st` `_task_status_for_skip(task: dict[str, Any]) -> str`    @staticmethod  L74
    - 分支数 1，函数体节点数 30；return: 'failed', 'enabled'
  #### `m` `__init__(self, *, task_repo, task_run_repo, launch_run, poll_interval_seconds: int, lease_seconds: int, max_concurrent_runs: int) -> None`  L19
    - 分支数 0，函数体节点数 102
    - 调用: gethostname, uuid4, Event
  #### `⏵m` `async run_once(self, *, now: datetime) -> None`  L39
    - 分支数 2，函数体节点数 82；return: None
    - 调用: count_active_runs, claim_due_tasks, dispatch_task
  #### `⏵m` `async dispatch_task(self, task: dict[str, Any], *, now: datetime, trigger: str) -> dict[str, Any]`  L81
    - 分支数 8，函数体节点数 565；return: {'outcome': 'conflict', 'task_run_id': None, 'run_id': None, 'thread_id': execution_thread_id, 'error': 'task already has an active run'}, await self._finalize_skip(task, task_run_id=task_run_id, thread_id=execution_thread_id, now=now, error=skip_error), {'outcome': 'launched', 'task_run_id': task_run_id, 'run_id': result['run_id'], 'thread_id': result['thread_id'], 'error': None}, await self._finalize_skip(task, task_run_id=task_run_id, thread_id=execution_thread_id, now=now, error=str(exc)), {'outcome': 'conflict' if self._is_overlap_conflict(exc) else 'failed', 'task_run_id': task_run_id, 'run_id': None, 'thread_id': execution_thread_id, 'error': str(exc)}
    - 调用: get, str, uuid4, has_active_runs, create, _finalize_skip, _launch_run, next_run_at, update_status, update_after_launch, _is_overlap_conflict, _task_status_for_failure
  #### `⏵m` `async _finalize_skip(self, task: dict[str, Any], *, task_run_id: str, thread_id: str, now: datetime, error: str) -> dict[str, Any]`  L212
    - 分支数 0，函数体节点数 158；return: {'outcome': 'skipped', 'task_run_id': task_run_id, 'run_id': None, 'thread_id': thread_id, 'error': error}
    - 调用: next_run_at, update_status, update_after_launch, _task_status_for_skip, get
  #### `⏵m` `async handle_run_completion(self, record: RunRecord) -> None`  L252
    - 分支数 9，函数体节点数 295；return: None
    - 调用: get, isinstance, update_status, now, update
  #### `⏵m` `async start(self) -> None`  L303
    - 分支数 5，函数体节点数 114；return: None
    - 调用: mark_stale_active_runs, warning, exception, cancel_stuck_once_tasks, clear, create_task, _run_loop
  #### `⏵m` `async stop(self) -> None`  L325
    - 分支数 1，函数体节点数 33；return: None
    - 调用: set
  #### `⏵m` `async _run_loop(self) -> None`  L332
    - 分支数 3，函数体节点数 64
    - 调用: is_set, run_once, now, exception, wait_for, wait

## 文件内调用关系
- `ScheduledTaskService.run_once` -> dispatch_task
- `ScheduledTaskService.dispatch_task` -> _finalize_skip, _is_overlap_conflict, _task_status_for_failure
- `ScheduledTaskService._finalize_skip` -> _task_status_for_skip
- `ScheduledTaskService.start` -> _run_loop
- `ScheduledTaskService._run_loop` -> run_once

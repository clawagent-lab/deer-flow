# `backend/app/gateway/routers/scheduled_tasks.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/scheduled_tasks.py`  ·  行数: 311

## 模块概览
- 函数 11 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: uuid
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any
- `fastapi` -> APIRouter, HTTPException, Query, Request
- `pydantic` -> BaseModel, Field
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_config, get_optional_user_from_request, get_scheduled_task_repo, get_scheduled_task_run_repo, get_scheduled_task_service, get_thread_store
- `deerflow.scheduler.schedules` -> compute_next_run_at
- `deerflow.scheduler.schedules` -> normalize_cron_expression, validate_timezone

## 模块级常量
- `router` = APIRouter(prefix='/api', tags=['scheduled-tasks'])

## 函数
#### `ƒ` `_ensure_task_mutable(task: dict[str, Any]) -> None`  L30
  - 分支数 1，函数体节点数 32；raise: HTTPException(status_code=409, detail='Scheduled task is currently running; retry after the active execution finishes')
  - 调用: get, HTTPException

#### `⏵ƒ` `async list_scheduled_tasks(request: Request)`    @router.get(...), require_permission(...)  L59
  - 分支数 1，函数体节点数 56；return: [], await repo.list_by_user(str(user.id))
  - 调用: get_scheduled_task_repo, get_optional_user_from_request, list_by_user, str, get, require_permission

#### `⏵ƒ` `async create_scheduled_task(request: Request, body: ScheduledTaskCreateRequest)`    @router.post(...), require_permission(...)  L69
  - 分支数 11，函数体节点数 400；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=422, detail='Unsupported context_mode'), HTTPException(status_code=422, detail='reuse_thread requires thread_id'), HTTPException(status_code=404, detail='Thread not found'), HTTPException(status_code=422, detail='Unsupported schedule_type'), HTTPException(status_code=422, detail='cron schedule requires schedule_spec.cron'), HTTPException(status_code=422, detail=str(exc)), HTTPException(status_code=422, detail='once schedule must be in the future'), HTTPException(status_code=422, detail=f'once schedule must be at least {config.scheduler.min_once_delay_seconds} seconds in the future')；return: await repo.create(task_id=f'task-{uuid.uuid4().hex}', user_id=str(user.id), thread_id=body.thread_id, context_mode=body.context_mode, assistant_id='lead_agent', title=body.title, prompt=body.prompt, schedule_type=body.schedule_type, schedule_spec=schedule_spec, timezone=body.timezone, next_run_at=next_run_at)
  - 调用: get_config, get_scheduled_task_repo, get_thread_store, get_optional_user_from_request, HTTPException, check_access, str, dict, validate_timezone, get, isinstance, normalize_cron_expression, compute_next_run_at, now, total_seconds, create, uuid4, post, require_permission

#### `⏵ƒ` `async get_scheduled_task(task_id: str, request: Request)`    @router.get(...), require_permission(...)  L128
  - 分支数 2，函数体节点数 86；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=404, detail='Scheduled task not found')；return: task
  - 调用: get_scheduled_task_repo, get_optional_user_from_request, HTTPException, get, str, require_permission

#### `⏵ƒ` `async update_scheduled_task(task_id: str, request: Request, body: ScheduledTaskUpdateRequest)`    @router.patch(...), require_permission(...)  L141
  - 分支数 18，函数体节点数 576；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=404, detail='Scheduled task not found'), HTTPException(status_code=422, detail='Unsupported context_mode'), HTTPException(status_code=422, detail='reuse_thread requires thread_id'), HTTPException(status_code=404, detail='Thread not found'), HTTPException(status_code=422, detail=str(exc)), HTTPException(status_code=422, detail='cron schedule requires schedule_spec.cron'), HTTPException(status_code=422, detail='once schedule must be in the future'), HTTPException(status_code=422, detail=f'once schedule must be at least {config.scheduler.min_once_delay_seconds} seconds in the future')；return: updated
  - 调用: get_config, get_scheduled_task_repo, get_optional_user_from_request, HTTPException, get, str, _ensure_task_mutable, model_dump, get_thread_store, check_access, validate_timezone, dict, isinstance, normalize_cron_expression, compute_next_run_at, now, total_seconds, update, patch, require_permission

#### `⏵ƒ` `async pause_scheduled_task(task_id: str, request: Request)`    @router.post(...), require_permission(...)  L220
  - 分支数 3，函数体节点数 129；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=404, detail='Scheduled task not found')；return: updated
  - 调用: get_scheduled_task_repo, get_optional_user_from_request, HTTPException, get, str, _ensure_task_mutable, update, post, require_permission

#### `⏵ƒ` `async resume_scheduled_task(task_id: str, request: Request)`    @router.post(...), require_permission(...)  L237
  - 分支数 3，函数体节点数 129；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=404, detail='Scheduled task not found')；return: updated
  - 调用: get_scheduled_task_repo, get_optional_user_from_request, HTTPException, get, str, _ensure_task_mutable, update, post, require_permission

#### `⏵ƒ` `async trigger_scheduled_task(task_id: str, request: Request)`    @router.post(...), require_permission(...)  L254
  - 分支数 4，函数体节点数 167；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=404, detail='Scheduled task not found'), HTTPException(status_code=409, detail=result['error'] or 'Scheduled task trigger conflicted with an active run'), HTTPException(status_code=502, detail=result['error'] or 'Scheduled task trigger failed')；return: {'id': task_id, 'triggered': True}
  - 调用: get_scheduled_task_repo, get_scheduled_task_service, get_optional_user_from_request, HTTPException, get, str, dispatch_task, now, post, require_permission

#### `⏵ƒ` `async delete_scheduled_task(task_id: str, request: Request)`    @router.delete(...), require_permission(...)  L273
  - 分支数 2，函数体节点数 90；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=404, detail='Scheduled task not found')；return: {'id': task_id, 'deleted': deleted}
  - 调用: get_scheduled_task_repo, get_optional_user_from_request, HTTPException, delete, str, require_permission

#### `⏵ƒ` `async list_scheduled_task_runs(task_id: str, request: Request, limit: int, offset: int)`    @router.get(...), require_permission(...)  L286
  - 分支数 2，函数体节点数 128；raise: HTTPException(status_code=401, detail='Authentication required'), HTTPException(status_code=404, detail='Scheduled task not found')；return: await run_repo.list_by_task(task_id, limit=limit, offset=offset)
  - 调用: Query, get_scheduled_task_repo, get_scheduled_task_run_repo, get_optional_user_from_request, HTTPException, get, str, list_by_task, require_permission

#### `⏵ƒ` `async list_thread_scheduled_tasks(thread_id: str, request: Request)`    @router.get(...), require_permission(...)  L305
  - 分支数 1，函数体节点数 68；raise: HTTPException(status_code=401, detail='Authentication required')；return: await repo.list_by_user_and_thread(str(user.id), thread_id)
  - 调用: get_scheduled_task_repo, get_optional_user_from_request, HTTPException, list_by_user_and_thread, str, get, require_permission

## 类
### 类 `ScheduledTaskCreateRequest`  L38
- 继承: BaseModel
- 类/实例变量:
  - `thread_id` = None
  - `context_mode` = 'fresh_thread_per_run'
  - `title` = Field(min_length=1)
  - `prompt` = Field(min_length=1)
  - `schedule_type` = <annotated>
  - `schedule_spec` = <annotated>
  - `timezone` = <annotated>

### 类 `ScheduledTaskUpdateRequest`  L48
- 继承: BaseModel
- 类/实例变量:
  - `context_mode` = None
  - `thread_id` = None
  - `title` = Field(default=None, min_length=1)
  - `prompt` = Field(default=None, min_length=1)
  - `schedule_spec` = None
  - `timezone` = None

## 文件内调用关系
- `update_scheduled_task` -> _ensure_task_mutable
- `pause_scheduled_task` -> _ensure_task_mutable
- `resume_scheduled_task` -> _ensure_task_mutable

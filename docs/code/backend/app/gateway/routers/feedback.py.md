# `backend/app/gateway/routers/feedback.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/feedback.py`  ·  行数: 189

**模块文档首行**（仅供参考）: Feedback endpoints — create, list, stats, delete.

## 模块概览
- 函数 6 个，类 4 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `typing` -> Any
- `fastapi` -> APIRouter, HTTPException, Request
- `pydantic` -> BaseModel, Field
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_current_user, get_feedback_repo, get_run_store

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/threads', tags=['feedback'])

## 函数
#### `⏵ƒ` `async upsert_feedback(thread_id: str, run_id: str, body: FeedbackUpsertRequest, request: Request) -> dict[str, Any]`    @router.put(...), require_permission(...)  L63
  - _文档首行_（仅供参考）: Create or update feedback for a run (idempotent).
  - 分支数 3，函数体节点数 173；raise: HTTPException(status_code=400, detail='rating must be +1 or -1'), HTTPException(status_code=404, detail=f'Run {run_id} not found'), HTTPException(status_code=404, detail=f'Run {run_id} not found in thread {thread_id}')；return: await feedback_repo.upsert(run_id=run_id, thread_id=thread_id, rating=body.rating, user_id=user_id, comment=body.comment)
  - 调用: HTTPException, get_current_user, get_run_store, get, get_feedback_repo, upsert, put, require_permission

#### `⏵ƒ` `async delete_run_feedback(thread_id: str, run_id: str, request: Request) -> dict[str, bool]`    @router.delete(...), require_permission(...)  L94
  - _文档首行_（仅供参考）: Delete the current user's feedback for a run.
  - 分支数 1，函数体节点数 90；raise: HTTPException(status_code=404, detail='No feedback found for this run')；return: {'success': True}
  - 调用: get_current_user, get_feedback_repo, delete_by_run, HTTPException, delete, require_permission

#### `⏵ƒ` `async create_feedback(thread_id: str, run_id: str, body: FeedbackCreateRequest, request: Request) -> dict[str, Any]`    @router.post(...), require_permission(...)  L114
  - _文档首行_（仅供参考）: Submit feedback (thumbs-up/down) for a run.
  - 分支数 3，函数体节点数 178；raise: HTTPException(status_code=400, detail='rating must be +1 or -1'), HTTPException(status_code=404, detail=f'Run {run_id} not found'), HTTPException(status_code=404, detail=f'Run {run_id} not found in thread {thread_id}')；return: await feedback_repo.create(run_id=run_id, thread_id=thread_id, rating=body.rating, user_id=user_id, message_id=body.message_id, comment=body.comment)
  - 调用: HTTPException, get_current_user, get_run_store, get, get_feedback_repo, create, post, require_permission

#### `⏵ƒ` `async list_feedback(thread_id: str, run_id: str, request: Request) -> list[dict[str, Any]]`    @router.get(...), require_permission(...)  L147
  - _文档首行_（仅供参考）: List all feedback for a run.
  - 分支数 0，函数体节点数 66；return: await feedback_repo.list_by_run(thread_id, run_id)
  - 调用: get_feedback_repo, list_by_run, get, require_permission

#### `⏵ƒ` `async feedback_stats(thread_id: str, run_id: str, request: Request) -> dict[str, Any]`    @router.get(...), require_permission(...)  L159
  - _文档首行_（仅供参考）: Get aggregated feedback stats (positive/negative counts) for a run.
  - 分支数 0，函数体节点数 58；return: await feedback_repo.aggregate_by_run(thread_id, run_id)
  - 调用: get_feedback_repo, aggregate_by_run, get, require_permission

#### `⏵ƒ` `async delete_feedback(thread_id: str, run_id: str, feedback_id: str, request: Request) -> dict[str, bool]`    @router.delete(...), require_permission(...)  L171
  - _文档首行_（仅供参考）: Delete a feedback record.
  - 分支数 3，函数体节点数 151；raise: HTTPException(status_code=404, detail=f'Feedback {feedback_id} not found'), HTTPException(status_code=404, detail=f'Feedback {feedback_id} not found in run {run_id}')；return: {'success': True}
  - 调用: get_feedback_repo, get, HTTPException, delete, require_permission

## 类
### 类 `FeedbackCreateRequest`  L27
- 继承: BaseModel
- 类/实例变量:
  - `rating` = Field(..., description='Feedback rating: +1 (positive) or...
  - `comment` = Field(default=None, description='Optional text feedback')
  - `message_id` = Field(default=None, description='Optional: scope feedback...

### 类 `FeedbackUpsertRequest`  L33
- 继承: BaseModel
- 类/实例变量:
  - `rating` = Field(..., description='Feedback rating: +1 (positive) or...
  - `comment` = Field(default=None, description='Optional text feedback')

### 类 `FeedbackResponse`  L38
- 继承: BaseModel
- 类/实例变量:
  - `feedback_id` = <annotated>
  - `run_id` = <annotated>
  - `thread_id` = <annotated>
  - `user_id` = None
  - `message_id` = None
  - `rating` = <annotated>
  - `comment` = None
  - `created_at` = ''

### 类 `FeedbackStatsResponse`  L49
- 继承: BaseModel
- 类/实例变量:
  - `run_id` = <annotated>
  - `total` = 0
  - `positive` = 0
  - `negative` = 0

## 文件内调用关系
_无文件内调用_

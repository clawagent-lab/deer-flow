# `backend/app/gateway/routers/runs.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/runs.py`  ·  行数: 144

**模块文档首行**（仅供参考）: Stateless runs endpoints -- stream and wait without a pre-existing thread.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: logging, uuid
- `__future__` -> annotations
- `fastapi` -> APIRouter, HTTPException, Query, Request
- `fastapi.responses` -> StreamingResponse
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_checkpointer, get_feedback_repo, get_run_event_store, get_run_manager, get_run_store, get_stream_bridge
- `app.gateway.pagination` -> trim_run_message_page
- `app.gateway.routers.thread_runs` -> RunCreateRequest
- `app.gateway.services` -> sse_consumer, start_run, wait_for_run_completion
- `deerflow.runtime` -> serialize_channel_values_for_api

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/runs', tags=['runs'])

## 函数
#### `ƒ` `_resolve_thread_id(body: RunCreateRequest) -> str`  L27
  - _文档首行_（仅供参考）: Return the thread_id from the request body, or generate a new one.
  - 分支数 1，函数体节点数 46；return: str(thread_id), str(uuid.uuid4())
  - 调用: get, str, uuid4

#### `⏵ƒ` `async stateless_stream(body: RunCreateRequest, request: Request) -> StreamingResponse`    @router.post(...)  L36
  - _文档首行_（仅供参考）: Create a run and stream events via SSE.
  - 分支数 0，函数体节点数 92；return: StreamingResponse(sse_consumer(bridge, record, request, run_mgr), media_type='text/event-stream', headers={'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'X-Accel-Buffering': 'no', 'Content-Location': f'/api/threads/{thread_id}/runs/{record.run_id}'})
  - 调用: _resolve_thread_id, get_stream_bridge, get_run_manager, start_run, StreamingResponse, sse_consumer, post

#### `⏵ƒ` `async stateless_wait(body: RunCreateRequest, request: Request) -> dict`    @router.post(...)  L61
  - _文档首行_（仅供参考）: Create a run and block until completion.
  - 分支数 4，函数体节点数 180；return: serialize_channel_values_for_api(channel_values), {'status': record.status.value, 'error': record.error}
  - 调用: _resolve_thread_id, get_stream_bridge, get_run_manager, start_run, wait_for_run_completion, get_checkpointer, aget_tuple, getattr, get, serialize_channel_values_for_api, exception, post
  - 反射: getattr (L83)

#### `⏵ƒ` `async _resolve_run(run_id: str, request: Request) -> dict`  L97
  - _文档首行_（仅供参考）: Fetch run by run_id with user ownership check. Raises 404 if not found.
  - 分支数 1，函数体节点数 53；raise: HTTPException(status_code=404, detail=f'Run {run_id} not found')；return: record
  - 调用: get_run_store, get, HTTPException

#### `⏵ƒ` `async run_messages(run_id: str, request: Request, limit: int, before_seq: int | None, after_seq: int | None) -> dict`    @router.get(...), require_permission(...)  L108
  - _文档首行_（仅供参考）: Return paginated messages for a run (cursor-based).
  - 分支数 0，函数体节点数 134；return: {'data': data, 'has_more': has_more}
  - 调用: Query, _resolve_run, get_run_event_store, list_messages_by_run, trim_run_message_page, get, require_permission

#### `⏵ƒ` `async run_feedback(run_id: str, request: Request) -> list[dict]`    @router.get(...), require_permission(...)  L139
  - _文档首行_（仅供参考）: Return all feedback for a run.
  - 分支数 0，函数体节点数 60；return: await feedback_repo.list_by_run(run['thread_id'], run_id)
  - 调用: _resolve_run, get_feedback_repo, list_by_run, get, require_permission

## 文件内调用关系
- `stateless_stream` -> _resolve_thread_id
- `stateless_wait` -> _resolve_thread_id
- `run_messages` -> _resolve_run
- `run_feedback` -> _resolve_run

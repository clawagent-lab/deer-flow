# `backend/app/gateway/trace_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/trace_middleware.py`  ·  行数: 75

**模块文档首行**（仅供参考）: Gateway request trace middleware.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `typing` -> Any
- `starlette.datastructures` -> Headers, MutableHeaders
- `starlette.types` -> ASGIApp, Message, Receive, Scope, Send
- `deerflow.config.app_config` -> is_trace_correlation_enabled
- `deerflow.trace_context` -> TRACE_ID_HEADER, mark_trace_id_from_request_header, normalize_trace_id, request_trace_context, reset_trace_id_from_request_header

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `resolve_trace_enabled(config: Any) -> bool`  L65
  - _文档首行_（仅供参考）: Read ``logging.enhance.enabled`` from an ``AppConfig``-like object.
  - 分支数 0，函数体节点数 15；return: is_trace_correlation_enabled(config)
  - 调用: is_trace_correlation_enabled

## 类
### 类 `TraceMiddleware`  L23
- _文档首行_: Bind a request-level trace id and write it to HTTP response headers.
- 方法:
  #### `m` `__init__(self, app: ASGIApp, *, enabled: bool)`  L37
    - 分支数 0，函数体节点数 26
    - 调用: bool
  #### `⏵m` `async __call__(self, scope: Scope, receive: Receive, send: Send) -> None`  L41
    - 分支数 4，函数体节点数 152；return: None
    - 调用: app, Headers, get, normalize_trace_id, request_trace_context, mark_trace_id_from_request_header, MutableHeaders, send, reset_trace_id_from_request_header

## 文件内调用关系
_无文件内调用_

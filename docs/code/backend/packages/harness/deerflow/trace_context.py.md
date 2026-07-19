# `backend/packages/harness/deerflow/trace_context.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/trace_context.py`  ·  行数: 120

**模块文档首行**（仅供参考）: Request trace context helpers.

## 模块概览
- 函数 11 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: uuid
- `__future__` -> annotations
- `collections.abc` -> Iterator
- `contextlib` -> contextmanager
- `contextvars` -> ContextVar, Token
- `typing` -> Final

## 模块级常量
- `TRACE_ID_HEADER` = 'X-Trace-Id'
- `DEERFLOW_TRACE_METADATA_KEY` = 'deerflow_trace_id'
- `_MAX_TRACE_ID_LENGTH` = 512
- `_current_trace_id` = ContextVar('deerflow_current_trace_id', default=None)
- `_trace_id_from_request_header` = ContextVar('deerflow_trace_id_from_request_header', defau...

## 函数
#### `ƒ` `generate_trace_id() -> str`  L26
  - _文档首行_（仅供参考）: Return a fresh header-safe trace id.
  - 分支数 0，函数体节点数 14；return: uuid.uuid4().hex
  - 调用: uuid4

#### `ƒ` `normalize_trace_id(value: object) -> str | None`  L31
  - _文档首行_（仅供参考）: Return a safe trace id string, or ``None`` when *value* is unusable.
  - 分支数 3，函数体节点数 83；return: None, trace_id
  - 调用: isinstance, strip, len, any, ord

#### `ƒ` `set_current_trace_id(trace_id: str) -> Token[str | None]`  L54
  - _文档首行_（仅供参考）: Bind *trace_id* to the current execution context.
  - 分支数 1，函数体节点数 44；return: _current_trace_id.set(normalized)
  - 调用: normalize_trace_id, generate_trace_id, set

#### `ƒ` `reset_current_trace_id(token: Token[str | None]) -> None`  L62
  - _文档首行_（仅供参考）: Restore the trace context captured by *token*.
  - 分支数 0，函数体节点数 23
  - 调用: reset

#### `ƒ` `get_current_trace_id() -> str | None`  L67
  - _文档首行_（仅供参考）: Return the current request trace id, if one is bound.
  - 分支数 0，函数体节点数 15；return: _current_trace_id.get()
  - 调用: get

#### `ƒ` `mark_trace_id_from_request_header(*, from_header: bool) -> Token[bool]`  L72
  - _文档首行_（仅供参考）: Record whether the current trace id came from a valid inbound header.
  - 分支数 0，函数体节点数 21；return: _trace_id_from_request_header.set(from_header)
  - 调用: set

#### `ƒ` `reset_trace_id_from_request_header(token: Token[bool]) -> None`  L77
  - _文档首行_（仅供参考）: Restore the inbound-header flag captured by *token*.
  - 分支数 0，函数体节点数 20
  - 调用: reset

#### `ƒ` `is_trace_id_from_request_header() -> bool`  L82
  - _文档首行_（仅供参考）: Return ``True`` when a valid ``X-Trace-Id`` header bound the request.
  - 分支数 0，函数体节点数 12；return: _trace_id_from_request_header.get()
  - 调用: get

#### `ƒ` `resolve_deerflow_trace_id(metadata_trace_id: object) -> str | None`  L87
  - _文档首行_（仅供参考）: Resolve the effective ``deerflow_trace_id`` for a run.
  - 分支数 1，函数体节点数 31；return: get_current_trace_id(), normalize_trace_id(metadata_trace_id) or get_current_trace_id()
  - 调用: is_trace_id_from_request_header, get_current_trace_id, normalize_trace_id

#### `ƒ` `request_trace_context(trace_id: str | None) -> Iterator[str]`    @contextmanager  L101
  - _文档首行_（仅供参考）: Bind a request trace id for the duration of a request or entry point.
  - 分支数 1，函数体节点数 55；生成器（yield）
  - 调用: normalize_trace_id, generate_trace_id, set, reset

#### `ƒ` `ensure_trace_context(trace_id: str | None) -> Iterator[str]`    @contextmanager  L112
  - _文档首行_（仅供参考）: Bind *trace_id*, inherit the current trace, or create a fresh one.
  - 分支数 1，函数体节点数 58；生成器（yield）
  - 调用: normalize_trace_id, get_current_trace_id, generate_trace_id, set, reset

## 文件内调用关系
- `set_current_trace_id` -> normalize_trace_id, generate_trace_id
- `resolve_deerflow_trace_id` -> is_trace_id_from_request_header, get_current_trace_id, normalize_trace_id
- `request_trace_context` -> normalize_trace_id, generate_trace_id
- `ensure_trace_context` -> normalize_trace_id, get_current_trace_id, generate_trace_id

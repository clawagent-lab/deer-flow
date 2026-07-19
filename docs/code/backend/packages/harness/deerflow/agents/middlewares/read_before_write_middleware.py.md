# `backend/packages/harness/deerflow/agents/middlewares/read_before_write_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/read_before_write_middleware.py`  ·  行数: 269

**模块文档首行**（仅供参考）: Deterministic read-before-write gate for file-modifying tools (issue #3857).

## 模块概览
- 函数 3 个，类 1 个，模块级常量 8 个

## 依赖（import）
- 模块: asyncio, hashlib, logging, posixpath, threading, weakref
- `collections.abc` -> Awaitable, Callable
- `typing` -> Any, override
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> ToolMessage
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command
- `deerflow.agents.middlewares.tool_result_meta` -> normalize_tool_result
- `deerflow.sandbox.tools` -> read_current_file_content

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `READ_MARK_KEY` = 'deerflow_read_mark'
- `_READ_TOOLS` = frozenset({'read_file'})
- `_GATED_WRITE_TOOLS` = frozenset({'write_file', 'str_replace'})
- `_UNINSPECTABLE_CONTENT_PREFIX` = 'Error:'
- `_BLOCK_MESSAGE` = 'Error: {tool_name} blocked — {path} already exists and y...
- `_GATE_LOCKS` = weakref.WeakValueDictionary()
- `_GATE_LOCKS_GUARD` = threading.Lock()

## 函数
#### `ƒ` `_get_gate_lock(scope: str, norm_path: str) -> threading.Lock`  L72
  - 分支数 2，函数体节点数 61；return: lock
  - 调用: get, Lock

#### `ƒ` `_normalize_mark_path(path: str) -> str`  L82
  - 分支数 0，函数体节点数 15；return: posixpath.normpath(path)
  - 调用: normpath

#### `ƒ` `_content_hash(content: str) -> str`  L86
  - 分支数 0，函数体节点数 22；return: hashlib.sha256(content.encode('utf-8')).hexdigest()
  - 调用: hexdigest, sha256, encode

## 类
### 类 `ReadBeforeWriteMiddleware`  L90
- 继承: AgentMiddleware
- _文档首行_: Version gate: block writes to existing files not read at their current version.
- 方法:
  #### `st` `_lock_scope(request: ToolCallRequest) -> str`    @staticmethod  L168
    - _文档首行_（仅供参考）: Scope locks per thread (or sandbox) so unrelated agents never contend.
    - 分支数 5，函数体节点数 113；return: thread_id, sandbox_id, 'global'
    - 调用: getattr, isinstance, get
  - 反射: getattr (L170)
  #### `st` `_requested_path(request: ToolCallRequest) -> str | None`    @staticmethod  L217
    - 分支数 1，函数体节点数 63；return: None, path if isinstance(path, str) and path else None
    - 调用: get, isinstance
  #### `st` `_latest_mark_hash(state: Any, norm_path: str) -> str | None`    @staticmethod  L225
    - 分支数 4，函数体节点数 123；return: None, mark_hash if isinstance(mark_hash, str) else None
    - 调用: isinstance, get, getattr, reversed
  - 反射: getattr (L226)
  #### `st` `_extract_tool_message(result: ToolMessage | Command) -> ToolMessage | None`    @staticmethod  L261
    - 分支数 3，函数体节点数 85；return: result, candidates[-1], None
    - 调用: isinstance, get
  #### `m` `__init__(self, content_reader: Callable[[Any, str], str] | None) -> None`  L93
    - 分支数 0，函数体节点数 41
    - 调用: __init__, super
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L98
    - 分支数 7，函数体节点数 177；return: handler(request), normalize_tool_result(blocked), result
    - 调用: get, _requested_path, handler, _lock_for, _check_write_gate, normalize_tool_result, _attach_read_mark
  #### `m` `_lock_for(self, request: ToolCallRequest, path: str) -> threading.Lock`  L164
    - 分支数 0，函数体节点数 29；return: _get_gate_lock(self._lock_scope(request), _normalize_mark_path(path))
    - 调用: _get_gate_lock, _lock_scope, _normalize_mark_path
  #### `m` `_check_write_gate(self, request: ToolCallRequest) -> ToolMessage | None`  L186
    - 分支数 4，函数体节点数 165；return: None, ToolMessage(content=_BLOCK_MESSAGE.format(tool_name=tool_name, path=path), tool_call_id=str(tool_call.get('id', '')), name=tool_name, status='error')
    - 调用: _requested_path, _content_reader, warning, startswith, debug, _normalize_mark_path, _latest_mark_hash, _content_hash, str, get, ToolMessage, format
  #### `m` `_attach_read_mark(self, request: ToolCallRequest, result: ToolMessage | Command) -> None`  L240
    - 分支数 4，函数体节点数 127；return: None
    - 调用: _requested_path, _extract_tool_message, _content_reader, debug, startswith, _normalize_mark_path, _content_hash
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L126
    - 分支数 7，函数体节点数 234；return: await handler(request), normalize_tool_result(blocked), result
    - 调用: get, _requested_path, handler, _lock_for, to_thread, normalize_tool_result, release

## 文件内调用关系
- `ReadBeforeWriteMiddleware.__init__` -> __init__
- `ReadBeforeWriteMiddleware.wrap_tool_call` -> _requested_path, _lock_for, _check_write_gate, _attach_read_mark
- `ReadBeforeWriteMiddleware.awrap_tool_call` -> _requested_path, _lock_for
- `ReadBeforeWriteMiddleware._lock_for` -> _get_gate_lock, _lock_scope, _normalize_mark_path
- `ReadBeforeWriteMiddleware._check_write_gate` -> _requested_path, _normalize_mark_path, _latest_mark_hash, _content_hash
- `ReadBeforeWriteMiddleware._attach_read_mark` -> _requested_path, _extract_tool_message, _normalize_mark_path, _content_hash

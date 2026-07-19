# `backend/packages/harness/deerflow/agents/middlewares/dangling_tool_call_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/dangling_tool_call_middleware.py`  ·  行数: 520

**模块文档首行**（仅供参考）: Middleware to fix dangling tool calls and orphan tool results in message history.

## 模块概览
- 函数 11 个，类 1 个，模块级常量 5 个

## 依赖（import）
- 模块: json, logging
- `collections` -> defaultdict, deque
- `collections.abc` -> Awaitable, Callable
- `typing` -> override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> ToolMessage

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_MAX_RECOVERY_ERROR_DETAIL_LEN` = 500
- `_UNKNOWN_TOOL_NAME` = 'unknown_tool'
- `_EMPTY_TOOL_NAME_ERROR` = 'Tool call could not be executed because its name was mis...
- `_SYNTHETIC_TOOL_CALL_ID_PREFIX` = 'deerflow_synthetic_tool_call_'

## 函数
#### `ƒ` `_valid_tool_name(name: object) -> bool`  L43
  - 分支数 0，函数体节点数 25；return: isinstance(name, str) and bool(name.strip())
  - 调用: isinstance, bool, strip

#### `ƒ` `_valid_tool_call_id(tool_call_id: object) -> bool`  L47
  - 分支数 0，函数体节点数 25；return: isinstance(tool_call_id, str) and bool(tool_call_id.strip())
  - 调用: isinstance, bool, strip

#### `ƒ` `_tool_call_name(tool_call: dict) -> object`  L51
  - _文档首行_（仅供参考）: Return a call's declared name, mirroring _message_tool_calls' raw-payload fallback.
  - 分支数 1，函数体节点数 53；return: name, function.get('name') if isinstance(function, dict) else name
  - 调用: get, _valid_tool_name, isinstance

#### `ƒ` `_names_can_pair(call_name: object, result_name: object) -> bool`  L60
  - _文档首行_（仅供参考）: Whether a result's name contradicts a call's name.
  - 分支数 1，函数体节点数 44；return: True, call_name.strip() == result_name.strip()
  - 调用: _valid_tool_name, strip

#### `ƒ` `_relabel_tool_call_ids(tool_calls: list, msg_index: int, source: str) -> tuple[list, list[dict], bool]`  L72
  - _文档首行_（仅供参考）: Replace malformed ids in one tool-call list with stable synthetic ids.
  - 分支数 2，函数体节点数 159；return: (relabeled, assigned, changed)
  - 调用: enumerate, isinstance, _valid_tool_call_id, get, append, _tool_call_name

#### `ƒ` `_turn_malformed_result_count(messages: list, start: int) -> int`  L95
  - _文档首行_（仅供参考）: Count the malformed results issued by the turn opened at ``start``.
  - 分支数 3，函数体节点数 68；return: count
  - 调用: getattr, isinstance, _valid_tool_call_id
  - 反射: getattr (L99)

#### `ƒ` `_claim_synthetic_id(open_calls: list[dict], result: ToolMessage, positional: bool) -> str | None`  L106
  - _文档首行_（仅供参考）: Consume the open malformed call that ``result`` answers, returning its new id.
  - 分支数 1，函数体节点数 102；return: None, open_calls.pop(candidates[0])['synthetic']
  - 调用: enumerate, _names_can_pair, len, pop

#### `ƒ` `_normalize_tool_name(name: object) -> str`  L132
  - 分支数 0，函数体节点数 21；return: name.strip() if _valid_tool_name(name) else _UNKNOWN_TOOL_NAME
  - 调用: _valid_tool_name, strip

#### `ƒ` `_has_invalid_tool_name(name: object) -> bool`  L136
  - 分支数 0，函数体节点数 15；return: not _valid_tool_name(name)
  - 调用: _valid_tool_name

#### `ƒ` `_parse_json_object(value: object) -> dict | None`  L140
  - _文档首行_（仅供参考）: Parse a JSON-object string, returning None for other inputs.
  - 分支数 2，函数体节点数 52；return: None, parsed if isinstance(parsed, dict) else None
  - 调用: isinstance, loads

#### `ƒ` `_normalize_tool_arguments(arguments: object) -> str`  L151
  - _文档首行_（仅供参考）: Return a JSON-object string safe for OpenAI-compatible replay.
  - 分支数 2，函数体节点数 52；return: json.dumps(arguments, ensure_ascii=False, allow_nan=False), '{}', arguments if _parse_json_object(arguments) is not None else '{}'
  - 调用: isinstance, dumps, _parse_json_object

## 类
### 类 `DanglingToolCallMiddleware`  L161
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Inserts placeholder ToolMessages for dangling tool calls and drops orphan
- 方法:
  #### `st` `_message_tool_calls(msg) -> list[dict]`    @staticmethod  L173
    - _文档首行_（仅供参考）: Return normalized tool calls from structured fields or raw provider payloads.
    - 分支数 12，函数体节点数 379；return: normalized
    - 调用: getattr, isinstance, debug, get, dict, _normalize_tool_name, _has_invalid_tool_name, append, _parse_json_object
  - 反射: getattr (L185), getattr (L197), getattr (L222)
  #### `st` `_synthetic_tool_message_content(tool_call: dict) -> str`    @staticmethod  L240
    - 分支数 4，函数体节点数 110；return: f'[{_EMPTY_TOOL_NAME_ERROR} Use one of the available tool names when retrying.]', f'[write_file failed before execution: the tool-call arguments were not valid JSON, so no file was written. This often happens when the model tries to write a very large Markdown file in a single tool call, especially when `content` contains unescaped quotes, inline JSON, backslashes, or code fences. Do not retry the same large `write_file` payload for this artifact; provide the report/content directly as normal assistant text in your next response. If a file write is still needed later, split the file into smaller sections instead of one large payload.{details}]', f'[Tool call could not be executed because its arguments were invalid: {error_text}]', '[Tool call could not be executed because its arguments were invalid.]', '[Tool call was interrupted and did not return a result.]'
    - 调用: get, isinstance
  #### `st` `_sanitize_ai_message_tool_calls(msg)`    @staticmethod  L267
    - _文档首行_（仅供参考）: Return an AIMessage with model-bound tool calls safe to serialize.
    - 分支数 22，函数体节点数 562；return: msg, msg.model_copy(update=update)
    - 调用: getattr, isinstance, append, get, dict, _normalize_tool_name, _normalize_tool_arguments, model_copy
  - 反射: getattr (L269), getattr (L275), getattr (L294), getattr (L316)
  #### `st` `_normalize_tool_call_ids(messages: list) -> list`    @staticmethod  L357
    - _文档首行_（仅供参考）: Return messages with malformed tool-call ids replaced by synthetic ids.
    - 分支数 9，函数体节点数 384；return: messages, [rewritten.get(index, msg) for index, msg in enumerate(messages)]
    - 调用: enumerate, getattr, get, isinstance, append, _relabel_tool_call_ids, extend, _turn_malformed_result_count, len, model_copy, _valid_tool_call_id, _claim_synthetic_id
  - 反射: getattr (L378), getattr (L381), getattr (L382), getattr (L385)
  #### `m` `_build_patched_messages(self, messages: list) -> list | None`  L423
    - _文档首行_（仅供参考）: Return messages with tool results grouped after their tool-call AIMessage.
    - 分支数 16，函数体节点数 369；return: None, patched
    - 调用: _normalize_tool_call_ids, defaultdict, isinstance, append, set, getattr, _message_tool_calls, get, add, _sanitize_ai_message_tool_calls, popleft, _has_invalid_tool_name, model_copy, ToolMessage, _synthetic_tool_message_content, warning
  - 反射: getattr (L438), getattr (L462)
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L500
    - 分支数 1，函数体节点数 58；return: handler(request)
    - 调用: _build_patched_messages, override, handler
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L511
    - 分支数 1，函数体节点数 63；return: await handler(request)
    - 调用: _build_patched_messages, override, handler

## 文件内调用关系
- `_tool_call_name` -> _valid_tool_name
- `_names_can_pair` -> _valid_tool_name
- `_relabel_tool_call_ids` -> _valid_tool_call_id, _tool_call_name
- `_turn_malformed_result_count` -> _valid_tool_call_id
- `_claim_synthetic_id` -> _names_can_pair
- `_normalize_tool_name` -> _valid_tool_name
- `_has_invalid_tool_name` -> _valid_tool_name
- `_normalize_tool_arguments` -> _parse_json_object
- `DanglingToolCallMiddleware._message_tool_calls` -> _normalize_tool_name, _has_invalid_tool_name, _parse_json_object
- `DanglingToolCallMiddleware._sanitize_ai_message_tool_calls` -> _normalize_tool_name, _normalize_tool_arguments
- `DanglingToolCallMiddleware._normalize_tool_call_ids` -> _relabel_tool_call_ids, _turn_malformed_result_count, _valid_tool_call_id, _claim_synthetic_id
- `DanglingToolCallMiddleware._build_patched_messages` -> _normalize_tool_call_ids, _message_tool_calls, _sanitize_ai_message_tool_calls, _has_invalid_tool_name, _synthetic_tool_message_content
- `DanglingToolCallMiddleware.wrap_model_call` -> _build_patched_messages
- `DanglingToolCallMiddleware.awrap_model_call` -> _build_patched_messages

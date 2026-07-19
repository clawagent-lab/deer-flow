# `backend/packages/harness/deerflow/agents/middlewares/tool_result_meta.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/tool_result_meta.py`  ·  行数: 213

**模块文档首行**（仅供参考）: Unified tool result semantics for structured signal production.

## 模块概览
- 函数 7 个，类 1 个，模块级常量 7 个

## 依赖（import）
- 模块: json, re
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> Literal
- `langchain_core.messages` -> ToolMessage
- `langgraph.types` -> Command

## 模块级常量
- `TOOL_META_KEY` = 'deerflow_tool_meta'
- `_ERROR_PREFIX` = 'Error:'
- `_PARTIAL_MARKERS` = ('partial results', 'limited results', 'truncated', 'resu...
- `_ERROR_RULES` = [(['401', '403', 'unauthorized', 'authentication', 'inval...
- `_UNKNOWN_ERROR` = {'error_type': 'unknown', 'recoverable_by_model': True, '...
- `_NUMERIC_KW_RE` = {kw: re.compile(f'\\b{kw}\\b') for rule_keywords, _ in _E...
- `_SEMANTIC_ZERO_ERROR_STRINGS` = frozenset({'none', 'null', 'false', 'no', 'ok', 'success'...

## 函数
#### `ƒ` `_extract_json_error_text(content: str) -> str | None`  L93
  - _文档首行_（仅供参考）: Return the error string from a JSON-wrapped error like {"error": "...", "query": "..."}.
  - 分支数 3，函数体节点数 101；return: None, error if isinstance(error, str) else json.dumps(error)
  - 调用: loads, isinstance, get, strip, lower, dumps

#### `ƒ` `_match_keyword(kw: str, lower: str) -> bool`  L117
  - _文档首行_（仅供参考）: Match a keyword against lowercased text, using word boundaries for numeric codes.
  - 分支数 1，函数体节点数 40；return: bool(_NUMERIC_KW_RE[kw].search(lower)), kw in lower
  - 调用: isdigit, bool, search

#### `ƒ` `_classify_error_text(text: str) -> dict[str, object]`  L124
  - 分支数 2，函数体节点数 57；return: {**attrs}, {**_UNKNOWN_ERROR}
  - 调用: lower, any, _match_keyword

#### `ƒ` `_make_meta(*, status: str, source: str, error_type: str | None, recoverable_by_model: bool, recommended_next_action: str) -> dict[str, object]`  L132
  - 分支数 0，函数体节点数 50；return: {'status': status, 'error_type': error_type, 'recoverable_by_model': recoverable_by_model, 'recommended_next_action': recommended_next_action, 'source': source}

#### `ƒ` `stamp_exception_meta(msg: ToolMessage, exc_info: str) -> ToolMessage`  L142
  - _文档首行_（仅供参考）: Stamp deerflow_tool_meta with source='exception' onto an exception-derived ToolMessage.
  - 分支数 0，函数体节点数 60；return: msg
  - 调用: _classify_error_text, dict, _make_meta

#### `ƒ` `normalize_tool_message(msg: ToolMessage) -> ToolMessage`  L156
  - _文档首行_（仅供参考）: Attach deerflow_tool_meta to a ToolMessage if not already present.
  - 分支数 7，函数体节点数 296；return: msg
  - 调用: get, isinstance, lower, startswith, _extract_json_error_text, _classify_error_text, loads, _make_meta, len, any, dict

#### `ƒ` `normalize_tool_result(result: ToolMessage | Command) -> ToolMessage | Command`  L208
  - _文档首行_（仅供参考）: Normalize a tool result, handling Command wrappers transparently.
  - 分支数 1，函数体节点数 34；return: normalize_tool_message(result), result
  - 调用: isinstance, normalize_tool_message

## 类
### 类 `ToolResultMeta`  L35  @dataclass(...)
- 类/实例变量:
  - `status` = <annotated>
  - `error_type` = <annotated>
  - `recoverable_by_model` = <annotated>
  - `recommended_next_action` = <annotated>
  - `source` = <annotated>

## 文件内调用关系
- `_classify_error_text` -> _match_keyword
- `stamp_exception_meta` -> _classify_error_text, _make_meta
- `normalize_tool_message` -> _extract_json_error_text, _classify_error_text, _make_meta
- `normalize_tool_result` -> normalize_tool_message

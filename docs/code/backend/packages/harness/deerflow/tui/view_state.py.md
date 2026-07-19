# `backend/packages/harness/deerflow/tui/view_state.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/view_state.py`  ·  行数: 391

**模块文档首行**（仅供参考）: Pure view-state reducer for the DeerFlow TUI.

## 模块概览
- 函数 10 个，类 15 个，模块级常量 2 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass, field, replace
- `typing` -> Literal
- `.message_format` -> format_tool_detail, format_tool_result, summarize_tool_title

## 模块级常量
- `Row` = UserRow | AssistantRow | ToolRow | SystemRow
- `Action` = UserSubmitted | RunStarted | RunEnded | AssistantDelta | ...

## 函数
#### `ƒ` `initial_state(rows: tuple[Row, ...]) -> ViewState`  L154
  - 分支数 0，函数体节点数 26；return: ViewState(rows=tuple(rows))
  - 调用: ViewState, tuple

#### `ƒ` `_append(state: ViewState, row: Row) -> ViewState`  L163
  - 分支数 0，函数体节点数 27；return: replace(state, rows=state.rows + (row,))
  - 调用: replace
  - 文件IO: replace (L164)

#### `ƒ` `reduce(state: ViewState, action: Action) -> ViewState`  L167
  - _文档首行_（仅供参考）: Return a new ``ViewState`` after applying ``action``. Pure.
  - 分支数 10，函数体节点数 235；return: _append(state, UserRow(text=action.text)), replace(state, streaming=True, streaming_id=None, streaming_anonymous_row_index=None), replace(state, streaming=False, streaming_id=None, streaming_anonymous_row_index=None, usage=action.usage if action.usage is not None else state.usage), _apply_assistant_delta(state, action), _append(state, AssistantRow(text=action.text, error=True)), _apply_tool_started(state, action), _apply_tool_result(state, action), _append(state, SystemRow(text=action.text, tone=action.tone)), replace(state, title=action.title), replace(state, rows=(), title=None, streaming_id=None, streaming_anonymous_row_index=None), state
  - 调用: isinstance, _append, UserRow, replace, _apply_assistant_delta, AssistantRow, _apply_tool_started, _apply_tool_result, SystemRow
  - 文件IO: replace (L176), replace (L179), replace (L203), replace (L206)

#### `ƒ` `_apply_assistant_delta(state: ViewState, action: AssistantDelta) -> ViewState`  L211
  - _文档首行_（仅供参考）: Update the assistant row for this delta, or start a new one.
  - 分支数 4，函数体节点数 175；return: _apply_assistant_delta_anonymous(state, action), state, _mark_streaming(replace(state, rows=tuple(rows)), action.id), _mark_streaming(_append(state, AssistantRow(text=action.text, id=action.id)), action.id)
  - 调用: _apply_assistant_delta_anonymous, list, enumerate, isinstance, len, _merge_stream_text, replace, _mark_streaming, tuple, _append, AssistantRow
  - 文件IO: replace (L252), replace (L253)

#### `ƒ` `_apply_assistant_delta_anonymous(state: ViewState, action: AssistantDelta) -> ViewState`  L257
  - _文档首行_（仅供参考）: Handle an ``AssistantDelta`` whose id is empty (see `_apply_assistant_delta`).
  - 分支数 3，函数体节点数 187；return: state, _mark_streaming_anonymous(replace(state, rows=tuple(rows)), index), _mark_streaming_anonymous(new_state, len(new_state.rows) - 1)
  - 调用: len, isinstance, list, _merge_stream_text, replace, _mark_streaming_anonymous, tuple, _append, AssistantRow
  - 文件IO: replace (L290), replace (L291)

#### `ƒ` `_mark_streaming(state: ViewState, message_id: str) -> ViewState`  L297
  - _文档首行_（仅供参考）: Record the actively-streaming message id (only while a run is active).
  - 分支数 1，函数体节点数 29；return: replace(state, streaming_id=message_id), state
  - 调用: replace
  - 文件IO: replace (L300)

#### `ƒ` `_mark_streaming_anonymous(state: ViewState, index: int) -> ViewState`  L304
  - _文档首行_（仅供参考）: Record the active turn's anonymous-row index (only while a run is active).
  - 分支数 1，函数体节点数 31；return: replace(state, streaming_id=None, streaming_anonymous_row_index=index), state
  - 调用: replace
  - 文件IO: replace (L318)

#### `ƒ` `_merge_stream_text(existing: str, incoming: str) -> str`  L322
  - 分支数 3，函数体节点数 75；return: incoming, existing, existing + incoming
  - 调用: len, startswith

#### `ƒ` `_apply_tool_started(state: ViewState, action: ToolStarted) -> ViewState`  L336
  - _文档首行_（仅供参考）: Create or update a tool card, de-duplicated by ``tool_call_id``.
  - 分支数 3，函数体节点数 172；return: state, replace(state, rows=tuple(rows)), _append(state, ToolRow(tool_call_id=action.tool_call_id, tool_name=action.tool_name, title=summarize_tool_title(action.tool_name), detail=format_tool_detail(action.tool_name, action.args), status='running'))
  - 调用: list, enumerate, isinstance, format_tool_detail, replace, summarize_tool_title, tuple, _append, ToolRow
  - 文件IO: replace (L351), replace (L352)

#### `ƒ` `_apply_tool_result(state: ViewState, action: ToolResult) -> ViewState`  L366
  - 分支数 3，函数体节点数 145；return: state, replace(state, rows=tuple(rows)), _append(state, ToolRow(tool_call_id=action.tool_call_id, tool_name=action.tool_name, title=summarize_tool_title(action.tool_name), status='error' if action.is_error else 'ok', result=format_tool_result(action.content)))
  - 调用: list, enumerate, isinstance, replace, format_tool_result, tuple, _append, ToolRow, summarize_tool_title
  - 文件IO: replace (L373), replace (L378)

## 类
### 类 `UserRow`  L30  @dataclass(...)
- 类/实例变量:
  - `text` = <annotated>
  - `kind` = 'user'

### 类 `AssistantRow`  L36  @dataclass(...)
- 类/实例变量:
  - `text` = <annotated>
  - `id` = None
  - `error` = False
  - `kind` = 'assistant'

### 类 `ToolRow`  L44  @dataclass(...)
- 类/实例变量:
  - `tool_call_id` = <annotated>
  - `tool_name` = <annotated>
  - `title` = <annotated>
  - `detail` = ''
  - `result` = ''
  - `status` = 'running'
  - `kind` = 'tool'

### 类 `SystemRow`  L55  @dataclass(...)
- 类/实例变量:
  - `text` = <annotated>
  - `tone` = 'info'
  - `kind` = 'system'

### 类 `UserSubmitted`  L70  @dataclass(...)
- 类/实例变量:
  - `text` = <annotated>

### 类 `RunStarted`  L75  @dataclass(...)

### 类 `RunEnded`  L80  @dataclass(...)
- 类/实例变量:
  - `usage` = None

### 类 `AssistantDelta`  L85  @dataclass(...)
- 类/实例变量:
  - `id` = <annotated>
  - `text` = <annotated>

### 类 `AssistantError`  L91  @dataclass(...)
- 类/实例变量:
  - `text` = <annotated>

### 类 `ToolStarted`  L96  @dataclass(...)
- 类/实例变量:
  - `tool_call_id` = <annotated>
  - `tool_name` = <annotated>
  - `args` = field(default_factory=dict)

### 类 `ToolResult`  L103  @dataclass(...)
- 类/实例变量:
  - `tool_call_id` = <annotated>
  - `content` = <annotated>
  - `is_error` = False
  - `tool_name` = ''

### 类 `SystemMessage`  L111  @dataclass(...)
- 类/实例变量:
  - `text` = <annotated>
  - `tone` = 'info'

### 类 `ThreadTitle`  L117  @dataclass(...)
- 类/实例变量:
  - `title` = <annotated>

### 类 `ClearRows`  L122  @dataclass(...)

### 类 `ViewState`  L135  @dataclass(...)
- 类/实例变量:
  - `rows` = ()
  - `streaming` = False
  - `usage` = None
  - `title` = None
  - `streaming_id` = None
  - `streaming_anonymous_row_index` = None

## 文件内调用关系
- `reduce` -> _append, _apply_assistant_delta, _apply_tool_started, _apply_tool_result
- `_apply_assistant_delta` -> _apply_assistant_delta_anonymous, _merge_stream_text, _mark_streaming, _append
- `_apply_assistant_delta_anonymous` -> _merge_stream_text, _mark_streaming_anonymous, _append
- `_apply_tool_started` -> _append
- `_apply_tool_result` -> _append

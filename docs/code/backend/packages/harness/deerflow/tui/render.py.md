# `backend/packages/harness/deerflow/tui/render.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/render.py`  ·  行数: 153

**模块文档首行**（仅供参考）: Pure Rich renderers for the transcript, status line and header.

## 模块概览
- 函数 7 个，类 0 个，模块级常量 3 个

## 依赖（import）
- `__future__` -> annotations
- `rich.console` -> Group, RenderableType
- `rich.markdown` -> Markdown
- `rich.table` -> Table
- `rich.text` -> Text
- `.theme` -> SYMBOLS, THEME
- `.view_state` -> AssistantRow, Row, SystemRow, ToolRow, UserRow, ViewState

## 模块级常量
- `_EMPTY_HINT` = 'Type a message to begin.  Press / for commands, ? for he...
- `_TOOL_STATUS_SYMBOL` = {'running': SYMBOLS['running'], 'ok': SYMBOLS['ok'], 'err...
- `_TOOL_STATUS_STYLE` = {'running': THEME.warning, 'ok': THEME.accent, 'error': T...

## 函数
#### `ƒ` `render_transcript(state: ViewState) -> RenderableType`  L24
  - 分支数 2，函数体节点数 119；return: Text(_EMPTY_HINT, style=f'italic {THEME.dim}'), Group(*blocks[:-1])
  - 调用: Text, isinstance, append, render_row, Group

#### `ƒ` `render_row(row: Row, *, as_markdown: bool) -> RenderableType`  L39
  - 分支数 5，函数体节点数 236；return: text, _assistant_markdown(row.text), _render_tool(row), Text(f"{SYMBOLS['system']} {row.text}", style=f'italic {style}'), Text(str(row))
  - 调用: isinstance, Text, append, strip, _assistant_markdown, _render_tool, str

#### `ƒ` `_assistant_markdown(text: str) -> RenderableType`  L65
  - _文档首行_（仅供参考）: A ``●`` speaker marker aligned to the top of the Markdown-rendered body.
  - 分支数 0，函数体节点数 72；return: grid
  - 调用: grid, add_column, add_row, Text, Markdown

#### `ƒ` `_render_tool(row: ToolRow) -> RenderableType`  L77
  - 分支数 2，函数体节点数 138；return: Group(head, Text(f'    {row.result}', style=THEME.dim)), head
  - 调用: Text, append, Group

#### `ƒ` `render_status(state: ViewState, *, model: str, thread_label: str, spinner: str, elapsed: str) -> Text`  L90
  - 分支数 5，函数体节点数 231；return: text
  - 调用: Text, append, get

#### `ƒ` `render_palette(items, index: int, limit: int) -> RenderableType`  L116
  - _文档首行_（仅供参考）: Render the slash-command picker: a windowed list with one highlighted row.
  - 分支数 4，函数体节点数 258；return: Text(''), Group(*lines)
  - 调用: Text, max, min, len, enumerate, append, Group

#### `ƒ` `render_header(*, model: str, thread_label: str, cwd: str, skills: int) -> Text`  L140
  - 分支数 1，函数体节点数 158；return: text
  - 调用: Text, append

## 文件内调用关系
- `render_transcript` -> render_row
- `render_row` -> _assistant_markdown, _render_tool

# `backend/packages/harness/deerflow/tui/message_format.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/message_format.py`  ·  行数: 109

**模块文档首行**（仅供参考）: Compact, human-friendly formatting for tool activity in the TUI.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: json
- `__future__` -> annotations
- `typing` -> Any

## 模块级常量
- `_TOOL_TITLES` = {'read_file': 'Read', 'write_file': 'Write', 'edit_file':...
- `_DETAIL_KEYS` = {'read_file': ('path', 'file_path', 'filename'), 'write_f...
- `_GENERIC_DETAIL_KEYS` = ('path', 'file_path', 'command', 'query', 'url', 'pattern...
- `DEFAULT_DETAIL_LIMIT` = 80
- `DEFAULT_RESULT_LIMIT` = 160

## 函数
#### `ƒ` `truncate(text: str, limit: int) -> str`  L53
  - _文档首行_（仅供参考）: Truncate ``text`` to ``limit`` chars, appending an ellipsis marker.
  - 分支数 1，函数体节点数 39；return: text, text[:limit].rstrip() + '…'
  - 调用: len, rstrip

#### `ƒ` `summarize_tool_title(tool_name: str) -> str`  L60
  - 分支数 2，函数体节点数 43；return: 'Tool', _TOOL_TITLES[tool_name], _humanize(tool_name)
  - 调用: strip, _humanize

#### `ƒ` `format_tool_detail(tool_name: str, args: Any, limit: int) -> str`  L68
  - _文档首行_（仅供参考）: Return a short inline detail for a tool call (e.g. the path or command).
  - 分支数 4，函数体节点数 133；return: '', truncate(_one_line(value), limit), truncate(compact, limit)
  - 调用: isinstance, get, strip, truncate, _one_line, dumps, str

#### `ƒ` `format_tool_result(result: Any, limit: int) -> str`  L87
  - _文档首行_（仅供参考）: Return a one-line, truncated preview of a tool result.
  - 分支数 3，函数体节点数 76；return: '', truncate(_one_line(result), limit)
  - 调用: isinstance, dumps, str, truncate, _one_line

#### `ƒ` `_one_line(text: str) -> str`  L99
  - _文档首行_（仅供参考）: Collapse all runs of whitespace (incl. newlines) into single spaces.
  - 分支数 0，函数体节点数 19；return: ' '.join(text.split())
  - 调用: join, split

#### `ƒ` `_humanize(name: str) -> str`  L104
  - 分支数 1，函数体节点数 64；return: name, ' '.join((word[:1].upper() + word[1:] for word in cleaned.split()))
  - 调用: strip, replace, join, upper, split
  - 文件IO: replace (L105), replace (L105)

## 文件内调用关系
- `summarize_tool_title` -> _humanize
- `format_tool_detail` -> truncate, _one_line
- `format_tool_result` -> truncate, _one_line

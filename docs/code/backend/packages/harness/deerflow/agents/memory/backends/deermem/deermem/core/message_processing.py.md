# `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/message_processing.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/message_processing.py`  ·  行数: 178

**模块文档首行**（仅供参考）: Shared helpers for turning conversations into memory update inputs.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 3 个

## 依赖（import）
- 模块: re
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `copy` -> copy
- `typing` -> Any

## 模块级常量
- `_UPLOAD_BLOCK_RE` = re.compile('<uploaded_files>[\\s\\S]*?</uploaded_files>\\...
- `_CORRECTION_PATTERNS` = (re.compile("\\bthat(?:'s| is) (?:wrong|incorrect)\\b", r...
- `_REINFORCEMENT_PATTERNS` = (re.compile("\\byes[,.]?\\s+(?:exactly|perfect|that(?:'s|...

## 函数
#### `ƒ` `extract_message_text(message: Any) -> str`  L41
  - _文档首行_（仅供参考）: Extract plain text from message content for filtering and signal detection.
  - 分支数 5，函数体节点数 105；return: ' '.join(text_parts), str(content)
  - 调用: getattr, isinstance, append, get, join, str
  - 反射: getattr (L43)

#### `ƒ` `_non_empty_str(value: object) -> str | None`  L57
  - _文档首行_（仅供参考）: Return ``value`` if it is a non-empty (stripped) string, else None.
  - 分支数 0，函数体节点数 31；return: value if isinstance(value, str) and value.strip() else None
  - 调用: isinstance, strip

#### `ƒ` `_is_human_clarification_response(additional_kwargs: Any) -> bool`  L62
  - _文档首行_（仅供参考）: Return True iff ``additional_kwargs`` carries a well-formed human
  - 分支数 6，函数体节点数 144；return: False, True, _non_empty_str(raw.get('option_id')) is not None
  - 调用: isinstance, get, _non_empty_str

#### `ƒ` `filter_messages_for_memory(messages: list[Any], *, should_keep_hidden_message: Any) -> list[Any]`  L94
  - _文档首行_（仅供参考）: Keep only user inputs and final assistant responses for memory updates.
  - 分支数 10，函数体节点数 216；return: filtered
  - 调用: getattr, get, should_keep_hidden_message, _is_human_clarification_response, extract_message_text, strip, sub, copy, append
  - 反射: getattr (L108), getattr (L116), getattr (L146)

#### `ƒ` `detect_correction(messages: list[Any]) -> bool`  L156
  - _文档首行_（仅供参考）: Detect explicit user corrections in recent conversation turns.
  - 分支数 2，函数体节点数 81；return: True, False
  - 调用: getattr, strip, extract_message_text, any, search
  - 反射: getattr (L158)

#### `ƒ` `detect_reinforcement(messages: list[Any]) -> bool`  L168
  - _文档首行_（仅供参考）: Detect explicit positive reinforcement signals in recent conversation turns.
  - 分支数 2，函数体节点数 81；return: True, False
  - 调用: getattr, strip, extract_message_text, any, search
  - 反射: getattr (L170)

## 文件内调用关系
- `_is_human_clarification_response` -> _non_empty_str
- `filter_messages_for_memory` -> _is_human_clarification_response, extract_message_text
- `detect_correction` -> extract_message_text
- `detect_reinforcement` -> extract_message_text

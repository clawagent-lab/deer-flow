# `backend/packages/harness/deerflow/utils/messages.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/utils/messages.py`  ·  行数: 151

## 模块概览
- 函数 5 个，类 0 个，模块级常量 2 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `copy` -> deepcopy
- `typing` -> Any
- `langchain_core.messages` -> HumanMessage

## 模块级常量
- `ORIGINAL_USER_CONTENT_KEY` = 'original_user_content'
- `SUMMARY_MESSAGE_NAME` = 'summary'

## 函数
#### `ƒ` `message_content_to_text(content: Any) -> str`  L13
  - _文档首行_（仅供参考）: Extract text from LangChain message content shapes.
  - 分支数 6，函数体节点数 114；return: content, '\n'.join((part for part in parts if part)), str(content)
  - 调用: isinstance, append, get, join, str

#### `ƒ` `message_to_text(message: Any, *, text_attribute_fallback: bool) -> str`  L30
  - _文档首行_（仅供参考）: Extract display text from a whole message (``BaseMessage`` or dict-shaped).
  - 分支数 12，函数体节点数 215；return: content, ''.join(parts), value, text, ''
  - 调用: isinstance, get, getattr, append, join
  - 反射: getattr (L44), getattr (L67)

#### `ƒ` `get_original_user_content_text(content: Any, additional_kwargs: Mapping[str, Any] | None) -> str`  L73
  - _文档首行_（仅供参考）: Return pre-middleware user text when available, otherwise content text.
  - 分支数 1，函数体节点数 53；return: original_content, message_content_to_text(content)
  - 调用: get, isinstance, message_content_to_text

#### `ƒ` `restore_original_human_message(message: HumanMessage) -> HumanMessage`  L81
  - _文档首行_（仅供参考）: Build the UI-facing copy of a model-sanitized human message.
  - 分支数 8，函数体节点数 239；return: message, message.model_copy(update={'content': deepcopy(restored_content), 'additional_kwargs': deepcopy(additional_kwargs)}, deep=True)
  - 调用: get, isinstance, dict, pop, append, insert, model_copy, deepcopy

#### `ƒ` `is_real_user_message(message: object) -> bool`  L138
  - _文档首行_（仅供参考）: Return whether ``message`` is a real user-authored HumanMessage.
  - 分支数 3，函数体节点数 45；return: False, True
  - 调用: isinstance, get

## 文件内调用关系
- `get_original_user_content_text` -> message_content_to_text

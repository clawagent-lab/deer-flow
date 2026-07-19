# `backend/packages/harness/deerflow/models/assistant_payload_replay.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/assistant_payload_replay.py`  ·  行数: 125

**模块文档首行**（仅供参考）: Helpers for replaying provider-specific assistant message fields.

## 模块概览
- 函数 10 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: json
- `__future__` -> annotations
- `collections.abc` -> Callable, Sequence
- `typing` -> Any
- `langchain_core.messages` -> AIMessage, BaseMessage

## 模块级常量
- `AssistantPayloadRestorer` = Callable[[dict[str, Any], AIMessage], None]

## 函数
#### `ƒ` `restore_assistant_payloads(payload_messages: Sequence[dict[str, Any]], original_messages: Sequence[BaseMessage], restore: AssistantPayloadRestorer) -> None`  L20
  - _文档首行_（仅供参考）: Restore provider-specific fields onto serialized assistant payloads.
  - 分支数 5，函数体节点数 175；return: None
  - 调用: len, zip, get, isinstance, restore, set, enumerate, _match_ai_message

#### `ƒ` `restore_additional_kwargs_field(payload_msg: dict[str, Any], orig_msg: AIMessage, field_name: str) -> None`  L42
  - _文档首行_（仅供参考）: Copy a provider-specific ``additional_kwargs`` field onto a payload message.
  - 分支数 1，函数体节点数 49
  - 调用: get

#### `ƒ` `restore_reasoning_content(payload_msg: dict[str, Any], orig_msg: AIMessage) -> None`  L49
  - _文档首行_（仅供参考）: Copy provider reasoning content onto a serialized assistant payload.
  - 分支数 0，函数体节点数 28
  - 调用: restore_additional_kwargs_field

#### `ƒ` `_match_ai_message(payload_msg: dict[str, Any], ai_messages: Sequence[AIMessage], used_ai_indexes: set[int], fallback_ordinal: int) -> AIMessage | None`  L54
  - 分支数 3，函数体节点数 152；return: ai_messages[matches[0]], ai_messages[fallback_index], None
  - 调用: _assistant_signature, enumerate, _ai_signature, len, add, _next_unused_index_at_or_after

#### `ƒ` `_next_unused_index_at_or_after(count: int, used_ai_indexes: set[int], start: int) -> int | None`  L75
  - _文档首行_（仅供参考）: Return the next unused AI index at or after ``start``.
  - 分支数 3，函数体节点数 60；return: None, index
  - 调用: range

#### `ƒ` `_assistant_signature(payload_msg: dict[str, Any]) -> tuple[str, str] | None`  L92
  - 分支数 0，函数体节点数 49；return: _signature(payload_msg.get('content'), _tool_call_ids(payload_msg.get('tool_calls') or []))
  - 调用: _signature, get, _tool_call_ids

#### `ƒ` `_ai_signature(message: AIMessage) -> tuple[str, str] | None`  L99
  - 分支数 0，函数体节点数 50；return: _signature(message.content, _tool_call_ids(tool_calls))
  - 调用: get, _signature, _tool_call_ids

#### `ƒ` `_signature(content: Any, tool_call_ids: tuple[str, ...]) -> tuple[str, str] | None`  L104
  - 分支数 1，函数体节点数 59；return: None, (_stable_repr(content), '|'.join(tool_call_ids))
  - 调用: _stable_repr, join

#### `ƒ` `_stable_repr(value: Any) -> str`  L110
  - 分支数 1，函数体节点数 29；return: json.dumps(value, sort_keys=True, ensure_ascii=False), repr(value)
  - 调用: dumps, repr

#### `ƒ` `_tool_call_ids(tool_calls: Sequence[Any]) -> tuple[str, ...]`  L117
  - 分支数 3，函数体节点数 77；return: tuple(ids)
  - 调用: isinstance, get, append, tuple

## 文件内调用关系
- `restore_assistant_payloads` -> _match_ai_message
- `restore_reasoning_content` -> restore_additional_kwargs_field
- `_match_ai_message` -> _assistant_signature, _ai_signature, _next_unused_index_at_or_after
- `_assistant_signature` -> _signature, _tool_call_ids
- `_ai_signature` -> _signature, _tool_call_ids
- `_signature` -> _stable_repr

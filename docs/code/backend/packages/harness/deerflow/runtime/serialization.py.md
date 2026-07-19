# `backend/packages/harness/deerflow/runtime/serialization.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/serialization.py`  ·  行数: 147

**模块文档首行**（仅供参考）: Canonical serialization for LangChain / LangGraph objects.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any

## 函数
#### `ƒ` `serialize_lc_object(obj: Any) -> Any`  L16
  - _文档首行_（仅供参考）: Recursively serialize a LangChain object to a JSON-serialisable dict.
  - 分支数 11，函数体节点数 174；return: None, obj, {k: serialize_lc_object(v) for k, v in obj.items()}, [serialize_lc_object(item) for item in obj], obj.model_dump(), obj.dict(), serialize_lc_object({'value': obj.value, 'id': getattr(obj, 'id', None)}), str(obj), repr(obj)
  - 调用: isinstance, serialize_lc_object, items, hasattr, model_dump, dict, getattr, str, repr
  - 反射: hasattr (L27), hasattr (L33), getattr (L49)

#### `ƒ` `serialize_channel_values(channel_values: dict[str, Any]) -> dict[str, Any]`  L59
  - _文档首行_（仅供参考）: Serialize channel values, stripping internal LangGraph keys.
  - 分支数 2，函数体节点数 74；return: result
  - 调用: items, startswith, serialize_lc_object

#### `ƒ` `strip_data_url_image_blocks(messages: list[dict[str, Any]]) -> list[dict[str, Any]]`  L74
  - _文档首行_（仅供参考）: Remove ``data:``-scheme ``image_url`` blocks from *hide_from_ui* messages.
  - 分支数 4，函数体节点数 217；return: result
  - 调用: isinstance, append, get, startswith, str

#### `ƒ` `serialize_channel_values_for_api(channel_values: dict[str, Any]) -> dict[str, Any]`  L110
  - _文档首行_（仅供参考）: Serialize channel values and strip base64 image data from messages.
  - 分支数 1，函数体节点数 62；return: result
  - 调用: serialize_channel_values, isinstance, get, strip_data_url_image_blocks

#### `ƒ` `serialize_messages_tuple(obj: Any) -> Any`  L124
  - _文档首行_（仅供参考）: Serialize a messages-mode tuple ``(chunk, metadata)``.
  - 分支数 1，函数体节点数 61；return: [serialize_lc_object(chunk), metadata if isinstance(metadata, dict) else {}], serialize_lc_object(obj)
  - 调用: isinstance, len, serialize_lc_object

#### `ƒ` `serialize(obj: Any, *, mode: str) -> Any`  L132
  - _文档首行_（仅供参考）: Serialize LangChain objects with mode-specific handling.
  - 分支数 2，函数体节点数 56；return: serialize_messages_tuple(obj), serialize_channel_values_for_api(obj) if isinstance(obj, dict) else serialize_lc_object(obj), serialize_lc_object(obj)
  - 调用: serialize_messages_tuple, isinstance, serialize_channel_values_for_api, serialize_lc_object

## 文件内调用关系
- `serialize_lc_object` -> serialize_lc_object
- `serialize_channel_values` -> serialize_lc_object
- `serialize_channel_values_for_api` -> serialize_channel_values, strip_data_url_image_blocks
- `serialize_messages_tuple` -> serialize_lc_object
- `serialize` -> serialize_messages_tuple, serialize_channel_values_for_api, serialize_lc_object

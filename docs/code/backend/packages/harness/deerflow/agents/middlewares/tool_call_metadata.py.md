# `backend/packages/harness/deerflow/agents/middlewares/tool_call_metadata.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/tool_call_metadata.py`  ·  行数: 51

**模块文档首行**（仅供参考）: Helpers for keeping AIMessage tool-call metadata consistent.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any
- `langchain_core.messages` -> AIMessage

## 函数
#### `ƒ` `_raw_tool_call_id(raw_tool_call: Any) -> str | None`  L10
  - 分支数 1，函数体节点数 47；return: None, raw_id if isinstance(raw_id, str) and raw_id else None
  - 调用: isinstance, get

#### `ƒ` `clone_ai_message_with_tool_calls(message: AIMessage, tool_calls: list[dict[str, Any]], *, content: Any | None) -> AIMessage`  L18
  - _文档首行_（仅供参考）: Clone an AIMessage while keeping raw provider tool-call metadata in sync.
  - 分支数 5，函数体节点数 243；return: message.model_copy(update=update)
  - 调用: isinstance, get, dict, getattr, _raw_tool_call_id, pop, model_copy
  - 反射: getattr (L31), getattr (L45)

## 文件内调用关系
- `clone_ai_message_with_tool_calls` -> _raw_tool_call_id

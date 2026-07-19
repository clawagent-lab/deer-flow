# `backend/packages/harness/deerflow/models/patched_openai.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/patched_openai.py`  ·  行数: 124

**模块文档首行**（仅供参考）: Patched ChatOpenAI that preserves thought_signature for Gemini thinking models.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any
- `langchain_core.language_models` -> LanguageModelInput
- `langchain_core.messages` -> AIMessage
- `langchain_openai` -> ChatOpenAI
- `deerflow.models.assistant_payload_replay` -> restore_assistant_payloads

## 函数
#### `ƒ` `_restore_tool_call_signatures(payload_msg: dict, orig_msg: AIMessage) -> None`  L85
  - _文档首行_（仅供参考）: Re-inject ``thought_signature`` onto tool-call objects in *payload_msg*.
  - 分支数 7，函数体节点数 191；return: None
  - 调用: get, enumerate, len

## 类
### 类 `PatchedChatOpenAI`  L33
- 继承: ChatOpenAI
- _文档首行_: ChatOpenAI with ``thought_signature`` preservation for Gemini thinking via OpenAI gateway.
- 方法:
  #### `m` `_get_request_payload(self, input_: LanguageModelInput, *, stop: list[str] | None, **kwargs) -> dict`  L59
    - _文档首行_（仅供参考）: Get request payload with ``thought_signature`` preserved on tool-call objects.
    - 分支数 0，函数体节点数 73；可变参数（*args/**kwargs）；return: payload
    - 调用: to_messages, _convert_input, _get_request_payload, super, restore_assistant_payloads, get

## 文件内调用关系
- `PatchedChatOpenAI._get_request_payload` -> _get_request_payload

# `backend/packages/harness/deerflow/models/patched_stepfun.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/patched_stepfun.py`  ·  行数: 176

**模块文档首行**（仅供参考）: Patched ChatOpenAI adapter for StepFun reasoning models.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Any
- `langchain_core.language_models` -> LanguageModelInput
- `langchain_core.messages` -> AIMessage, AIMessageChunk
- `langchain_core.outputs` -> ChatGeneration, ChatGenerationChunk, ChatResult
- `langchain_openai` -> ChatOpenAI
- `deerflow.models.assistant_payload_replay` -> restore_assistant_payloads, restore_reasoning_content

## 模块级常量
- `_MISSING` = object()

## 函数
#### `ƒ` `_extract_reasoning(value: Any) -> str | object`  L28
  - _文档首行_（仅供参考）: Return reasoning content from a dict/Pydantic object.
  - 分支数 8，函数体节点数 145；return: value[field], _MISSING, attr, model_extra[field]
  - 调用: isinstance, getattr
  - 反射: getattr (L43), getattr (L48)

#### `ƒ` `_with_reasoning_content(message: AIMessage | AIMessageChunk, reasoning: str) -> AIMessage | AIMessageChunk`  L57
  - _文档首行_（仅供参考）: Return a copy of *message* with reasoning_content stored in additional_kwargs.
  - 分支数 1，函数体节点数 60；return: message.model_copy(update={'additional_kwargs': additional_kwargs})
  - 调用: dict, get, model_copy

#### `ƒ` `_get_typed_choice_message(response: Any, index: int) -> Any`  L65
  - _文档首行_（仅供参考）: Extract the SDK-typed choice message at *index*, if available.
  - 分支数 2，函数体节点数 51；return: None, choices[index].message
  - 调用: getattr
  - 反射: getattr (L67)

## 类
### 类 `PatchedChatStepFun`  L76
- 继承: ChatOpenAI
- _文档首行_: ChatOpenAI with full reasoning support for StepFun models.
- 方法:
  #### `prop` `lc_secrets(self) -> dict[str, str]`    @property  L89
    - 分支数 0，函数体节点数 21；return: {'api_key': 'STEPFUN_API_KEY', 'openai_api_key': 'STEPFUN_API_KEY'}
  #### `cls` `is_lc_serializable(cls) -> bool`    @classmethod  L85
    - 分支数 0，函数体节点数 9；return: True
  #### `m` `_get_request_payload(self, input_: LanguageModelInput, *, stop: list[str] | None, **kwargs) -> dict`  L94
    - _文档首行_（仅供参考）: Restore ``reasoning_content`` on historical assistant messages.
    - 分支数 0，函数体节点数 73；可变参数（*args/**kwargs）；return: payload
    - 调用: to_messages, _convert_input, _get_request_payload, super, restore_assistant_payloads, get
  #### `m` `_convert_chunk_to_generation_chunk(self, chunk: dict, default_chunk_class: type, base_generation_info: dict | None) -> ChatGenerationChunk | None`  L115
    - _文档首行_（仅供参考）: Capture ``reasoning`` / ``reasoning_content`` from streaming deltas.
    - 分支数 3，函数体节点数 124；return: None, generation_chunk
    - 调用: _convert_chunk_to_generation_chunk, super, get, _extract_reasoning, isinstance, ChatGenerationChunk, _with_reasoning_content
  #### `m` `_create_chat_result(self, response: dict | Any, generation_info: dict | None) -> ChatResult`  L144
    - _文档首行_（仅供参考）: Extract ``reasoning`` / ``reasoning_content`` from non-streaming responses.
    - 分支数 4，函数体节点数 248；return: ChatResult(generations=patched_generations or result.generations, llm_output=result.llm_output)
    - 调用: _create_chat_result, super, isinstance, model_dump, get, enumerate, len, _extract_reasoning, _get_typed_choice_message, list, ChatGeneration, _with_reasoning_content, ChatResult

## 文件内调用关系
- `PatchedChatStepFun._get_request_payload` -> _get_request_payload
- `PatchedChatStepFun._convert_chunk_to_generation_chunk` -> _convert_chunk_to_generation_chunk, _extract_reasoning, _with_reasoning_content
- `PatchedChatStepFun._create_chat_result` -> _create_chat_result, _extract_reasoning, _get_typed_choice_message, _with_reasoning_content

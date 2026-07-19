# `backend/packages/harness/deerflow/models/patched_mimo.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/patched_mimo.py`  ·  行数: 141

**模块文档首行**（仅供参考）: Patched ChatOpenAI adapter for Xiaomi MiMo reasoning_content replay.

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
#### `ƒ` `_extract_reasoning_content(value: Any) -> str | object`  L25
  - _文档首行_（仅供参考）: Return reasoning_content from a dict/Pydantic object, preserving empty strings.
  - 分支数 4，函数体节点数 116；return: value['reasoning_content'], _MISSING, reasoning, model_extra['reasoning_content']
  - 调用: isinstance, getattr
  - 反射: getattr (L32), getattr (L36)

#### `ƒ` `_with_reasoning_content(message: AIMessage | AIMessageChunk, reasoning: str) -> AIMessage | AIMessageChunk`  L43
  - 分支数 1，函数体节点数 58；return: message.model_copy(update={'additional_kwargs': additional_kwargs})
  - 调用: dict, get, model_copy

#### `ƒ` `_get_typed_choice_message(response: Any, index: int) -> Any`  L50
  - 分支数 2，函数体节点数 49；return: None, choices[index].message
  - 调用: getattr
  - 反射: getattr (L51)

## 类
### 类 `PatchedChatMiMo`  L60
- 继承: ChatOpenAI
- _文档首行_: ChatOpenAI with ``reasoning_content`` preservation for MiMo thinking mode.
- 方法:
  #### `prop` `lc_secrets(self) -> dict[str, str]`    @property  L68
    - 分支数 0，函数体节点数 21；return: {'api_key': 'MIMO_API_KEY', 'openai_api_key': 'MIMO_API_KEY'}
  #### `cls` `is_lc_serializable(cls) -> bool`    @classmethod  L64
    - 分支数 0，函数体节点数 9；return: True
  #### `m` `_get_request_payload(self, input_: LanguageModelInput, *, stop: list[str] | None, **kwargs) -> dict`  L71
    - 分支数 0，函数体节点数 71；可变参数（*args/**kwargs）；return: payload
    - 调用: to_messages, _convert_input, _get_request_payload, super, restore_assistant_payloads, get
  #### `m` `_convert_chunk_to_generation_chunk(self, chunk: dict, default_chunk_class: type, base_generation_info: dict | None) -> ChatGenerationChunk | None`  L88
    - 分支数 3，函数体节点数 122；return: None, generation_chunk
    - 调用: _convert_chunk_to_generation_chunk, super, get, _extract_reasoning_content, isinstance, ChatGenerationChunk, _with_reasoning_content
  #### `m` `_create_chat_result(self, response: dict | Any, generation_info: dict | None) -> ChatResult`  L114
    - 分支数 4，函数体节点数 246；return: ChatResult(generations=patched_generations or result.generations, llm_output=result.llm_output)
    - 调用: _create_chat_result, super, isinstance, model_dump, get, enumerate, len, _extract_reasoning_content, _get_typed_choice_message, list, ChatGeneration, _with_reasoning_content, ChatResult

## 文件内调用关系
- `PatchedChatMiMo._get_request_payload` -> _get_request_payload
- `PatchedChatMiMo._convert_chunk_to_generation_chunk` -> _convert_chunk_to_generation_chunk, _extract_reasoning_content, _with_reasoning_content
- `PatchedChatMiMo._create_chat_result` -> _create_chat_result, _extract_reasoning_content, _get_typed_choice_message, _with_reasoning_content

# `backend/packages/harness/deerflow/models/patched_minimax.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/patched_minimax.py`  ·  行数: 240

**模块文档首行**（仅供参考）: Patched ChatOpenAI adapter for MiniMax reasoning output.

## 模块概览
- 函数 4 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: re
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Any
- `langchain_core.language_models` -> LanguageModelInput
- `langchain_core.messages` -> AIMessage, AIMessageChunk
- `langchain_core.outputs` -> ChatGeneration, ChatGenerationChunk, ChatResult
- `langchain_openai` -> ChatOpenAI
- `langchain_openai.chat_models.base` -> _convert_delta_to_message_chunk, _create_usage_metadata

## 模块级常量
- `_THINK_TAG_RE` = re.compile('<think>\\s*(.*?)\\s*</think>', re.DOTALL)

## 函数
#### `ƒ` `_extract_reasoning_text(reasoning_details: Any, *, strip_parts: bool) -> str | None`  L31
  - 分支数 5，函数体节点数 108；return: None, '\n\n'.join(parts) if parts else None
  - 调用: isinstance, get, strip, append, join

#### `ƒ` `_strip_inline_think_tags(content: str) -> tuple[str, str | None]`  L52
  - 分支数 1，函数体节点数 102；return: '', (cleaned, reasoning)
  - 调用: strip, group, append, sub, join

#### `ƒ` `_merge_reasoning(*values) -> str | None`  L66
  - 分支数 3，函数体节点数 73；可变参数（*args/**kwargs）；return: '\n\n'.join(merged) if merged else None
  - 调用: strip, append, join

#### `ƒ` `_with_reasoning_content(message: AIMessage | AIMessageChunk, reasoning: str | None, *, preserve_whitespace: bool)`  L77
  - 分支数 2，函数体节点数 100；return: message, message.model_copy(update={'additional_kwargs': additional_kwargs})
  - 调用: dict, get, isinstance, _merge_reasoning, model_copy

## 类
### 类 `PatchedChatMiniMax`  L98
- 继承: ChatOpenAI
- _文档首行_: ChatOpenAI adapter that preserves MiniMax reasoning output.
- 方法:
  #### `st` `_strip_user_message_names(payload: dict) -> None`    @staticmethod  L121
    - _文档首行_（仅供参考）: Drop the per-message ``name`` field from user-role messages.
    - 分支数 3，函数体节点数 62；return: None
    - 调用: get, isinstance, pop
  #### `m` `_get_request_payload(self, input_: LanguageModelInput, *, stop: list[str] | None, **kwargs) -> dict`  L101
    - 分支数 1，函数体节点数 87；可变参数（*args/**kwargs）；return: payload
    - 调用: _get_request_payload, super, get, isinstance, _strip_user_message_names
  #### `m` `_convert_chunk_to_generation_chunk(self, chunk: dict, default_chunk_class: type, base_generation_info: dict | None) -> ChatGenerationChunk | None`  L138
    - 分支数 12，函数体节点数 349；return: None, generation_chunk, ChatGenerationChunk(message=message_chunk, generation_info=generation_info or None)
    - 调用: get, _create_usage_metadata, len, ChatGenerationChunk, default_chunk_class, _convert_delta_to_message_chunk, _extract_reasoning_text, isinstance, _with_reasoning_content
  #### `m` `_create_chat_result(self, response: dict | Any, generation_info: dict | None) -> ChatResult`  L202
    - 分支数 5，函数体节点数 290；return: ChatResult(generations=generations, llm_output=result.llm_output)
    - 调用: _create_chat_result, super, isinstance, model_dump, get, enumerate, len, _strip_inline_think_tags, _extract_reasoning_text, _merge_reasoning, model_copy, _with_reasoning_content, ChatGeneration, append, ChatResult

## 文件内调用关系
- `_with_reasoning_content` -> _merge_reasoning
- `PatchedChatMiniMax._get_request_payload` -> _get_request_payload, _strip_user_message_names
- `PatchedChatMiniMax._convert_chunk_to_generation_chunk` -> _extract_reasoning_text, _with_reasoning_content
- `PatchedChatMiniMax._create_chat_result` -> _create_chat_result, _strip_inline_think_tags, _extract_reasoning_text, _merge_reasoning, _with_reasoning_content

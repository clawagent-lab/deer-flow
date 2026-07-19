# `backend/packages/harness/deerflow/models/vllm_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/vllm_provider.py`  ·  行数: 259

**模块文档首行**（仅供参考）: Custom vLLM provider built on top of LangChain ChatOpenAI.

## 模块概览
- 函数 4 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: json, openai
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Any, cast
- `langchain_core.language_models` -> LanguageModelInput
- `langchain_core.messages` -> AIMessage, AIMessageChunk, BaseMessageChunk, ChatMessageChunk, FunctionMessageChunk, HumanMessageChunk, SystemMessageChunk, ToolMessageChunk
- `langchain_core.messages.tool` -> tool_call_chunk
- `langchain_core.outputs` -> ChatGeneration, ChatGenerationChunk, ChatResult
- `langchain_openai` -> ChatOpenAI
- `langchain_openai.chat_models.base` -> _create_usage_metadata

## 函数
#### `ƒ` `_normalize_vllm_chat_template_kwargs(payload: dict[str, Any]) -> None`  L39
  - _文档首行_（仅供参考）: Map DeerFlow's legacy ``thinking`` toggle to vLLM/Qwen's ``enable_thinking``.
  - 分支数 3，函数体节点数 99；return: None
  - 调用: get, isinstance, dict, setdefault, pop

#### `ƒ` `_reasoning_to_text(reasoning: Any) -> str`  L65
  - _文档首行_（仅供参考）: Best-effort extraction of readable reasoning text from vLLM payloads.
  - 分支数 9，函数体节点数 154；return: reasoning, ''.join((part for part in parts if part)), value, text, json.dumps(reasoning, ensure_ascii=False), str(reasoning)
  - 调用: isinstance, _reasoning_to_text, join, get, dumps, str

#### `ƒ` `_convert_delta_to_message_chunk_with_reasoning(_dict: Mapping[str, Any], default_class: type[BaseMessageChunk]) -> BaseMessageChunk`  L94
  - _文档首行_（仅供参考）: Convert a streaming delta to a LangChain message chunk while preserving reasoning.
  - 分支数 12，函数体节点数 425；return: HumanMessageChunk(content=content, id=id_), AIMessageChunk(content=content, additional_kwargs=additional_kwargs, id=id_, tool_call_chunks=tool_call_chunks), SystemMessageChunk(content=content, id=id_, additional_kwargs=role_kwargs), FunctionMessageChunk(content=content, name=_dict['name'], id=id_), ToolMessageChunk(content=content, tool_call_id=_dict['tool_call_id'], id=id_), ChatMessageChunk(content=content, role=role, id=id_), default_class(content=content, id=id_)
  - 调用: get, cast, dict, _reasoning_to_text, tool_call_chunk, HumanMessageChunk, AIMessageChunk, SystemMessageChunk, FunctionMessageChunk, ToolMessageChunk, ChatMessageChunk, default_class

#### `ƒ` `_restore_reasoning_field(payload_msg: dict[str, Any], orig_msg: AIMessage) -> None`  L150
  - _文档首行_（仅供参考）: Re-inject vLLM reasoning onto outgoing assistant messages.
  - 分支数 2，函数体节点数 61
  - 调用: get

## 类
### 类 `VllmChatModel`  L159
- 继承: ChatOpenAI
- _文档首行_: ChatOpenAI variant that preserves vLLM reasoning fields across turns.
- 类/实例变量:
  - `model_config` = {'arbitrary_types_allowed': True}
- 方法:
  #### `prop` `_llm_type(self) -> str`    @property  L165
    - 分支数 0，函数体节点数 9；return: 'vllm-openai-compatible'
  #### `m` `_get_request_payload(self, input_: LanguageModelInput, *, stop: list[str] | None, **kwargs) -> dict[str, Any]`  L168
    - _文档首行_（仅供参考）: Restore assistant reasoning in request payloads for interleaved thinking.
    - 分支数 4，函数体节点数 196；可变参数（*args/**kwargs）；return: payload
    - 调用: to_messages, _convert_input, _get_request_payload, super, _normalize_vllm_chat_template_kwargs, get, len, zip, isinstance, _restore_reasoning_field
  #### `m` `_create_chat_result(self, response: dict | openai.BaseModel, generation_info: dict | None) -> ChatResult`  L193
    - _文档首行_（仅供参考）: Preserve vLLM reasoning on non-streaming responses.
    - 分支数 5，函数体节点数 161；return: result
    - 调用: _create_chat_result, super, isinstance, model_dump, zip, get, _reasoning_to_text
  #### `m` `_convert_chunk_to_generation_chunk(self, chunk: dict, default_chunk_class: type, base_generation_info: dict | None) -> ChatGenerationChunk | None`  L214
    - _文档首行_（仅供参考）: Preserve vLLM reasoning on streaming deltas.
    - 分支数 10，函数体节点数 318；return: None, generation_chunk, ChatGenerationChunk(message=message_chunk, generation_info=generation_info or None)
    - 调用: get, _create_usage_metadata, len, ChatGenerationChunk, default_chunk_class, _convert_delta_to_message_chunk_with_reasoning, isinstance

## 文件内调用关系
- `_reasoning_to_text` -> _reasoning_to_text
- `_convert_delta_to_message_chunk_with_reasoning` -> _reasoning_to_text
- `VllmChatModel._get_request_payload` -> _get_request_payload, _normalize_vllm_chat_template_kwargs, _restore_reasoning_field
- `VllmChatModel._create_chat_result` -> _create_chat_result, _reasoning_to_text
- `VllmChatModel._convert_chunk_to_generation_chunk` -> _convert_delta_to_message_chunk_with_reasoning

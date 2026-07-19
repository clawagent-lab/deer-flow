# `backend/packages/harness/deerflow/models/openai_codex_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/openai_codex_provider.py`  ·  行数: 461

**模块文档首行**（仅供参考）: Custom OpenAI Codex provider using ChatGPT Codex Responses API.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 3 个

## 依赖（import）
- 模块: json, logging, time, httpx
- `typing` -> Any
- `langchain_core.callbacks` -> CallbackManagerForLLMRun
- `langchain_core.language_models.chat_models` -> BaseChatModel
- `langchain_core.messages` -> AIMessage, BaseMessage, HumanMessage, SystemMessage, ToolMessage
- `langchain_core.outputs` -> ChatGeneration, ChatResult
- `deerflow.models.credential_loader` -> CodexCliCredential, load_codex_cli_credential

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `CODEX_BASE_URL` = 'https://chatgpt.com/backend-api/codex'
- `MAX_RETRIES` = 3

## 函数
#### `ƒ` `_build_usage_metadata(oai_usage: dict) -> dict`  L32
  - _文档首行_（仅供参考）: Convert Codex/Responses API usage dict to LangChain usage_metadata format.
  - 分支数 2，函数体节点数 136；return: metadata
  - 调用: get

## 类
### 类 `CodexChatModel`  L61
- 继承: BaseChatModel
- _文档首行_: LangChain chat model using ChatGPT Codex Responses API.
- 类/实例变量:
  - `model` = 'gpt-5.4'
  - `reasoning_effort` = 'medium'
  - `retry_max_attempts` = MAX_RETRIES
  - `_access_token` = ''
  - `_account_id` = ''
  - `model_config` = {'arbitrary_types_allowed': True}
- 方法:
  #### `prop` `_llm_type(self) -> str`    @property  L84
    - 分支数 0，函数体节点数 9；return: 'codex-responses'
  #### `cls` `is_lc_serializable(cls) -> bool`    @classmethod  L80
    - 分支数 0，函数体节点数 9；return: True
  #### `cls` `_normalize_content(cls, content: Any) -> str`    @classmethod  L110
    - _文档首行_（仅供参考）: Flatten LangChain content blocks into plain text for Codex.
    - 分支数 8，函数体节点数 161；return: content, '\n'.join((part for part in parts if part)), value, cls._normalize_content(nested_content), json.dumps(content, ensure_ascii=False), str(content)
    - 调用: isinstance, _normalize_content, join, get, dumps, str
  #### `st` `_parse_sse_data_line(line: str) -> dict[str, Any] | None`    @staticmethod  L296
    - _文档首行_（仅供参考）: Parse a data line from the SSE stream, skipping terminal markers.
    - 分支数 3，函数体节点数 100；return: None, data if isinstance(data, dict) else None
    - 调用: startswith, strip, loads, debug, isinstance
  #### `m` `_validate_retry_config(self) -> None`  L87
    - 分支数 1，函数体节点数 17；raise: ValueError('retry_max_attempts must be >= 1')
    - 调用: ValueError
  #### `m` `model_post_init(self, __context: Any) -> None`  L91
    - _文档首行_（仅供参考）: Auto-load Codex CLI credentials.
    - 分支数 1，函数体节点数 76；raise: ValueError('Codex CLI credential not found. Expected ~/.codex/auth.json or CODEX_AUTH_PATH.')
    - 调用: _validate_retry_config, _load_codex_auth, info, ValueError, model_post_init, super
  #### `m` `_load_codex_auth(self) -> CodexCliCredential | None`  L105
    - _文档首行_（仅供参考）: Load access_token and account_id from Codex CLI auth.
    - 分支数 0，函数体节点数 14；return: load_codex_cli_credential()
    - 调用: load_codex_cli_credential
  #### `m` `_convert_messages(self, messages: list[BaseMessage]) -> tuple[str, list[dict]]`  L137
    - _文档首行_（仅供参考）: Convert LangChain messages to Responses API format.
    - 分支数 9，函数体节点数 258；return: (instructions, input_items)
    - 调用: isinstance, _normalize_content, append, dumps, join
  #### `m` `_convert_tools(self, tools: list[dict]) -> list[dict]`  L180
    - _文档首行_（仅供参考）: Convert LangChain tool format to Responses API format.
    - 分支数 3，函数体节点数 124；return: responses_tools
    - 调用: get, append
  #### `m` `_call_codex_api(self, messages: list[BaseMessage], tools: list[dict] | None) -> dict`  L205
    - _文档首行_（仅供参考）: Call the Codex Responses API and return the completed response.
    - 分支数 5，函数体节点数 243；raise: bare raise, last_error；return: self._stream_response(headers, payload)
    - 调用: _convert_messages, _convert_tools, range, _stream_response, warning, sleep
  #### `m` `_stream_response(self, headers: dict, payload: dict) -> dict`  L248
    - _文档首行_（仅供参考）: Stream SSE from Codex API and collect the final response.
    - 分支数 13，函数体节点数 348；raise: RuntimeError('Codex API stream ended without response.completed event')；return: completed_response
    - 调用: Client, stream, raise_for_status, iter_lines, _parse_sse_data_line, get, isinstance, RuntimeError, list, max, len, extend, items, dict
  #### `m` `_parse_tool_call_arguments(self, output_item: dict[str, Any]) -> tuple[dict[str, Any] | None, dict[str, Any] | None]`  L313
    - _文档首行_（仅供参考）: Parse function-call arguments, surfacing malformed payloads safely.
    - 分支数 3，函数体节点数 178；return: (raw_arguments, None), (None, {'type': 'invalid_tool_call', 'name': output_item.get('name'), 'args': str(raw_arguments), 'id': output_item.get('call_id'), 'error': f'Failed to parse tool arguments: {exc}'}), (None, {'type': 'invalid_tool_call', 'name': output_item.get('name'), 'args': str(raw_arguments), 'id': output_item.get('call_id'), 'error': 'Tool arguments must decode to a JSON object.'}), (parsed_arguments, None)
    - 调用: get, isinstance, loads, str
  #### `m` `_parse_response(self, response: dict) -> ChatResult`  L342
    - _文档首行_（仅供参考）: Parse Codex Responses API response into LangChain ChatResult.
    - 分支数 11，函数体节点数 342；return: ChatResult(generations=[ChatGeneration(message=message)], llm_output={'token_usage': {'prompt_tokens': usage.get('input_tokens', 0), 'completion_tokens': usage.get('output_tokens', 0), 'total_tokens': usage.get('total_tokens', 0)}, 'model_name': response.get('model', self.model)})
    - 调用: get, isinstance, _parse_tool_call_arguments, append, _build_usage_metadata, AIMessage, ChatResult, ChatGeneration
  #### `m` `_generate(self, messages: list[BaseMessage], stop: list[str] | None, run_manager: CallbackManagerForLLMRun | None, **kwargs) -> ChatResult`  L406
    - _文档首行_（仅供参考）: Generate a response using Codex Responses API.
    - 分支数 0，函数体节点数 66；可变参数（*args/**kwargs）；return: self._parse_response(response)
    - 调用: get, _call_codex_api, _parse_response
  #### `m` `bind_tools(self, tools: list, **kwargs) -> Any`  L418
    - _文档首行_（仅供参考）: Bind tools for function calling.
    - 分支数 5，函数体节点数 181；可变参数（*args/**kwargs）；return: RunnableBinding(bound=self, kwargs={'tools': formatted_tools}, **kwargs)
    - 调用: isinstance, convert_to_openai_function, append, get, RunnableBinding

## 文件内调用关系
- `CodexChatModel.model_post_init` -> _validate_retry_config, _load_codex_auth, model_post_init
- `CodexChatModel._normalize_content` -> _normalize_content
- `CodexChatModel._convert_messages` -> _normalize_content
- `CodexChatModel._call_codex_api` -> _convert_messages, _convert_tools, _stream_response
- `CodexChatModel._stream_response` -> _parse_sse_data_line
- `CodexChatModel._parse_response` -> _parse_tool_call_arguments, _build_usage_metadata
- `CodexChatModel._generate` -> _call_codex_api, _parse_response

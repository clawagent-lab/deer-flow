# `backend/packages/harness/deerflow/agents/middlewares/input_sanitization_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/input_sanitization_middleware.py`  ·  行数: 371

**模块文档首行**（仅供参考）: Input guardrail middleware for prompt-injection defense (issue #3630).

## 模块概览
- 函数 5 个，类 1 个，模块级常量 9 个

## 依赖（import）
- 模块: logging, re
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `typing` -> override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> HumanMessage
- `langgraph.errors` -> GraphBubbleUp
- `deerflow.agents.human_input` -> read_human_input_response
- `deerflow.utils.messages` -> ORIGINAL_USER_CONTENT_KEY, message_content_to_text

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SUMMARY_MESSAGE_NAME` = 'summary'
- `_BLOCKED_TAG_NAMES` = frozenset({'system-reminder', 'system_reminder', 'memory'...
- `_BLOCKED_TAG_PATTERN` = re.compile('<\\s*/?\\s*(?:' + '|'.join((re.escape(t) for ...
- `_USER_INPUT_BEGIN` = '--- BEGIN USER INPUT ---'
- `_USER_INPUT_END` = '--- END USER INPUT ---'
- `_NEUTRALIZED_BEGIN` = '[BEGIN USER INPUT]'
- `_NEUTRALIZED_END` = '[END USER INPUT]'
- `_BOUNDARY_TOKEN_RE` = re.compile(re.escape(_USER_INPUT_BEGIN) + '|' + re.escape...

## 函数
#### `ƒ` `_escape_tag_match(match: re.Match) -> str`  L128
  - _文档首行_（仅供参考）: Escape < and > in a blocked-tag match so it renders as literal text.
  - 分支数 0，函数体节点数 28；return: match.group(0).replace('<', '&lt;').replace('>', '&gt;')
  - 调用: replace, group
  - 文件IO: replace (L130), replace (L130)

#### `ƒ` `_neutralize_boundary_tokens(text: str) -> str`  L133
  - _文档首行_（仅供参考）: Replace real BEGIN/END USER INPUT markers with look-alike inert forms.
  - 分支数 0，函数体节点数 35；return: _BOUNDARY_TOKEN_RE.sub(lambda m: _NEUTRALIZED_BEGIN if m.group(0) == _USER_INPUT_BEGIN else _NEUTRALIZED_END, text)
  - 调用: sub, group

#### `ƒ` `neutralize_untrusted_tags(text: str) -> str`  L141
  - _文档首行_（仅供参考）: Neutralize framework/injection control tokens in untrusted text.
  - 分支数 1，函数体节点数 38；return: text, _neutralize_boundary_tokens(text)
  - 调用: strip, sub, _neutralize_boundary_tokens

#### `ƒ` `_is_genuine_user_message(message: object) -> bool`  L169
  - _文档首行_（仅供参考）: Return True for real user messages, excluding system-injected HumanMessages.
  - 分支数 3，函数体节点数 57；return: False, True
  - 调用: isinstance, get, read_human_input_response

#### `ƒ` `_check_user_content(text: str) -> str`  L184
  - _文档首行_（仅供参考）: Sanitize user content: escape blocked tags, then wrap in boundary markers.
  - 分支数 3，函数体节点数 119；return: text, f'{_USER_INPUT_BEGIN}{neutralized_inner}{_USER_INPUT_END}', f'{_USER_INPUT_BEGIN}\n{text}\n{_USER_INPUT_END}'
  - 调用: strip, sub, startswith, endswith, len, _neutralize_boundary_tokens

## 类
### 类 `InputSanitizationMiddleware`  L214
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Guardrail middleware that escapes prompt-injection tags in user input.
- 方法:
  #### `st` `_extract_text_from_content(content: str | list) -> tuple[str, list | None]`    @staticmethod  L224
    - _文档首行_（仅供参考）: Extract concatenated text from a plain-string or content-block-list.
    - 分支数 4，函数体节点数 142；return: (content, None), ('', None), ('\n'.join(text_parts), text_blocks)
    - 调用: isinstance, get, append, join
  #### `st` `_rebuild_content(original_content: list, processed_text: str, text_blocks: list[dict]) -> list`    @staticmethod  L243
    - _文档首行_（仅供参考）: Replace text blocks with a single merged text block, preserving interleaved non-text blocks.
    - 分支数 6，函数体节点数 171；return: original_content, result
    - 调用: id, enumerate, range, append, extend
  #### `m` `_process_request(self, request: ModelRequest) -> ModelRequest`  L270
    - _文档首行_（仅供参考）: Return a request with the last genuine user message sanitized.
    - 分支数 8，函数体节点数 315；return: request, request.override(messages=messages)
    - 调用: list, range, len, _is_genuine_user_message, isinstance, debug, get, _extract_text_from_content, _check_user_content, _rebuild_content, dict, warning, type, message_content_to_text, HumanMessage, override
  #### `m` `_try_process(self, request: ModelRequest) -> ModelRequest`  L340
    - _文档首行_（仅供参考）: Sanitize request; fail-open on unexpected errors.
    - 分支数 1，函数体节点数 38；raise: bare raise；return: self._process_request(request), request
    - 调用: _process_request, warning
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L357
    - 分支数 0，函数体节点数 34；return: handler(self._try_process(request))
    - 调用: handler, _try_process
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L365
    - 分支数 0，函数体节点数 39；return: await handler(self._try_process(request))
    - 调用: handler, _try_process

## 文件内调用关系
- `neutralize_untrusted_tags` -> _neutralize_boundary_tokens
- `_check_user_content` -> _neutralize_boundary_tokens
- `InputSanitizationMiddleware._process_request` -> _is_genuine_user_message, _extract_text_from_content, _check_user_content, _rebuild_content
- `InputSanitizationMiddleware._try_process` -> _process_request
- `InputSanitizationMiddleware.wrap_model_call` -> _try_process
- `InputSanitizationMiddleware.awrap_model_call` -> _try_process

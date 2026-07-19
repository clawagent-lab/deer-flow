# `backend/packages/harness/deerflow/agents/middlewares/llm_error_handling_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/llm_error_handling_middleware.py`  ·  行数: 493

**模块文档首行**（仅供参考）: LLM error handling middleware with retry/backoff and user-facing fallbacks.

## 模块概览
- 函数 5 个，类 1 个，模块级常量 7 个

## 依赖（import）
- 模块: asyncio, logging, threading, time
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `email.utils` -> parsedate_to_datetime
- `typing` -> Any, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> AIMessage
- `langgraph.errors` -> GraphBubbleUp
- `deerflow.config.app_config` -> AppConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_RETRIABLE_STATUS_CODES` = {408, 409, 425, 429, 500, 502, 503, 504}
- `_BUSY_PATTERNS` = ('server busy', 'temporarily unavailable', 'try again lat...
- `_QUOTA_PATTERNS` = ('insufficient_quota', 'quota', 'billing', 'credit', 'pay...
- `_AUTH_PATTERNS` = ('authentication', 'unauthorized', 'invalid api key', 'in...
- `_RETRY_BUDGET_OVERRIDES` = {'StreamChunkTimeoutError': 2}
- `_STREAM_DROP_EXCEPTIONS` = frozenset({'StreamChunkTimeoutError'})

## 函数
#### `ƒ` `_matches_any(detail: str, patterns: tuple[str, ...]) -> bool`  L425
  - 分支数 0，函数体节点数 33；return: any((pattern in detail for pattern in patterns))
  - 调用: any

#### `ƒ` `_extract_error_code(exc: BaseException) -> Any`  L429
  - 分支数 6，函数体节点数 103；return: value, None
  - 调用: getattr, isinstance, get
  - 反射: getattr (L431), getattr (L435)

#### `ƒ` `_extract_status_code(exc: BaseException) -> int | None`  L446
  - 分支数 2，函数体节点数 71；return: value, status if isinstance(status, int) else None
  - 调用: getattr, isinstance
  - 反射: getattr (L448), getattr (L451), getattr (L452)

#### `ƒ` `_extract_retry_after_ms(exc: BaseException) -> int | None`  L456
  - 分支数 7，函数体节点数 178；return: None, max(0, int(float(raw) * multiplier)), max(0, int(delta * 1000))
  - 调用: getattr, hasattr, get, lower, max, int, float, parsedate_to_datetime, str, timestamp, time
  - 反射: getattr (L457), getattr (L458), hasattr (L466)

#### `ƒ` `_extract_error_detail(exc: BaseException) -> str`  L485
  - 分支数 2，函数体节点数 62；return: detail, message.strip(), exc.__class__.__name__
  - 调用: strip, str, getattr, isinstance
  - 反射: getattr (L489)

## 类
### 类 `LLMErrorHandlingMiddleware`  L101
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Retry transient LLM errors and surface graceful assistant messages.
- 类/实例变量:
  - `retry_max_attempts` = 3
  - `retry_base_delay_ms` = 1000
  - `retry_cap_delay_ms` = 8000
- 方法:
  #### `m` `__init__(self, *, app_config: AppConfig, **kwargs) -> None`  L108
    - 分支数 0，函数体节点数 76；可变参数（*args/**kwargs）
    - 调用: __init__, super, Lock
  #### `m` `_max_attempts_for(self, exc: BaseException) -> int`  L121
    - _文档首行_（仅供参考）: Return the effective max attempt count for this exception.
    - 分支数 1，函数体节点数 46；return: self.retry_max_attempts, min(override, self.retry_max_attempts)
    - 调用: get, type, min
  #### `m` `_check_circuit(self) -> bool`  L133
    - _文档首行_（仅供参考）: Returns True if circuit is OPEN (fast fail), False otherwise.
    - 分支数 5，函数体节点数 77；return: True, False
    - 调用: time
  #### `m` `_record_success(self) -> None`  L152
    - 分支数 2，函数体节点数 58
    - 调用: info
  #### `m` `_record_failure(self) -> None`  L161
    - 分支数 4，函数体节点数 127；return: None
    - 调用: time, error
  #### `m` `_release_half_open_probe(self) -> None`  L185
    - _文档首行_（仅供参考）: Release the in-flight half-open probe without recording a failure.
    - 分支数 2，函数体节点数 26
  #### `m` `_classify_error(self, exc: BaseException) -> tuple[bool, str]`  L196
    - 分支数 6，函数体节点数 158；return: (False, 'quota'), (False, 'auth'), (True, 'transient'), (True, 'busy'), (False, 'generic')
    - 调用: _extract_error_detail, lower, _extract_error_code, _extract_status_code, _matches_any, str, isinstance
  #### `m` `_build_retry_delay_ms(self, attempt: int, exc: BaseException) -> int`  L235
    - 分支数 1，函数体节点数 59；return: retry_after, min(backoff, self.retry_cap_delay_ms)
    - 调用: _extract_retry_after_ms, max, min
  #### `m` `_build_retry_message(self, attempt: int, wait_ms: int, reason: str) -> str`  L242
    - 分支数 0，函数体节点数 61；return: f'LLM request retry {attempt}/{self.retry_max_attempts}: {reason_text}. Retrying in {seconds}s.'
    - 调用: max, round
  #### `m` `_build_circuit_breaker_message(self) -> str`  L247
    - 分支数 0，函数体节点数 7；return: 'The configured LLM provider is currently unavailable due to continuous failures. Circuit breaker is engaged to protect the system. Please wait a moment before trying again.'
  #### `m` `_build_error_fallback_message(self, content: str, *, error_type: str, reason: str, detail: str) -> AIMessage`  L250
    - 分支数 0，函数体节点数 37；return: AIMessage(content=content, additional_kwargs={'deerflow_error_fallback': True, 'error_type': error_type, 'error_reason': reason, 'error_detail': detail})
    - 调用: AIMessage
  #### `m` `_build_user_message(self, exc: BaseException, reason: str) -> str`  L268
    - 分支数 4，函数体节点数 65；return: 'The configured LLM provider rejected the request because the account is out of quota, billing is unavailable, or usage is restricted. Please fix the provider account and try again.', 'The configured LLM provider rejected the request because authentication or access is invalid. Please check the provider credentials and try again.', "The model's streaming response was interrupted before it could finish. This usually happens when a single response or tool call is very large — please ask the assistant to split the work into smaller steps, or shorten the requested output, and try again.", 'The configured LLM provider is temporarily unavailable after multiple retries. Please wait a moment and continue the conversation.', f'LLM request failed: {detail}'
    - 调用: _extract_error_detail, type
  #### `m` `_build_user_fallback_message(self, exc: BaseException, reason: str) -> AIMessage`  L292
    - 分支数 0，函数体节点数 43；return: self._build_error_fallback_message(self._build_user_message(exc, reason), error_type=type(exc).__name__, reason=reason, detail=_extract_error_detail(exc))
    - 调用: _build_error_fallback_message, _build_user_message, type, _extract_error_detail
  #### `m` `_emit_retry_event(self, attempt: int, wait_ms: int, reason: str) -> None`  L300
    - 分支数 1，函数体节点数 67
    - 调用: get_stream_writer, writer, _build_retry_message, debug
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L319
    - 分支数 5，函数体节点数 221；raise: bare raise；return: self._build_error_fallback_message(self._build_circuit_breaker_message(), error_type='CircuitBreakerOpen', reason='circuit_open', detail='LLM circuit breaker is open'), response, self._build_user_fallback_message(exc, reason)
    - 调用: _check_circuit, _build_error_fallback_message, _build_circuit_breaker_message, handler, _record_success, _release_half_open_probe, _classify_error, _max_attempts_for, _build_retry_delay_ms, warning, _extract_error_detail, _emit_retry_event, sleep, _record_failure, _build_user_fallback_message
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L372
    - 分支数 5，函数体节点数 227；raise: bare raise；return: self._build_error_fallback_message(self._build_circuit_breaker_message(), error_type='CircuitBreakerOpen', reason='circuit_open', detail='LLM circuit breaker is open'), response, self._build_user_fallback_message(exc, reason)
    - 调用: _check_circuit, _build_error_fallback_message, _build_circuit_breaker_message, handler, _record_success, _release_half_open_probe, _classify_error, _max_attempts_for, _build_retry_delay_ms, warning, _extract_error_detail, _emit_retry_event, sleep, _record_failure, _build_user_fallback_message

## 文件内调用关系
- `LLMErrorHandlingMiddleware.__init__` -> __init__
- `LLMErrorHandlingMiddleware._classify_error` -> _extract_error_detail, _extract_error_code, _extract_status_code, _matches_any
- `LLMErrorHandlingMiddleware._build_retry_delay_ms` -> _extract_retry_after_ms
- `LLMErrorHandlingMiddleware._build_user_message` -> _extract_error_detail
- `LLMErrorHandlingMiddleware._build_user_fallback_message` -> _build_error_fallback_message, _build_user_message, _extract_error_detail
- `LLMErrorHandlingMiddleware._emit_retry_event` -> _build_retry_message
- `LLMErrorHandlingMiddleware.wrap_model_call` -> _check_circuit, _build_error_fallback_message, _build_circuit_breaker_message, _record_success, _release_half_open_probe, _classify_error, _max_attempts_for, _build_retry_delay_ms, _extract_error_detail, _emit_retry_event, _record_failure, _build_user_fallback_message
- `LLMErrorHandlingMiddleware.awrap_model_call` -> _check_circuit, _build_error_fallback_message, _build_circuit_breaker_message, _record_success, _release_half_open_probe, _classify_error, _max_attempts_for, _build_retry_delay_ms, _extract_error_detail, _emit_retry_event, _record_failure, _build_user_fallback_message

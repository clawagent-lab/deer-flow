# `backend/packages/harness/deerflow/models/claude_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/claude_provider.py`  ·  行数: 364

**模块文档首行**（仅供参考）: Custom Claude provider with OAuth Bearer auth, prompt caching, and smart thinking.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 5 个

## 依赖（import）
- 模块: hashlib, json, logging, os, socket, time, uuid, anthropic
- `typing` -> Any
- `langchain_anthropic` -> ChatAnthropic
- `langchain_core.messages` -> BaseMessage
- `pydantic` -> PrivateAttr

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `MAX_RETRIES` = 3
- `THINKING_BUDGET_RATIO` = 0.8
- `_DEFAULT_BILLING_HEADER` = 'x-anthropic-billing-header: cc_version=2.1.85.351; cc_en...
- `OAUTH_BILLING_HEADER` = os.environ.get('ANTHROPIC_BILLING_HEADER', _DEFAULT_BILLI...

## 类
### 类 `ClaudeChatModel`  L44
- 继承: ChatAnthropic
- _文档首行_: ChatAnthropic with OAuth Bearer auth, prompt caching, and smart thinking.
- 类/实例变量:
  - `enable_prompt_caching` = True
  - `prompt_cache_size` = 3
  - `auto_thinking_budget` = True
  - `retry_max_attempts` = MAX_RETRIES
  - `_is_oauth` = PrivateAttr(default=False)
  - `_oauth_access_token` = PrivateAttr(default='')
  - `model_config` = {'arbitrary_types_allowed': True}
- 方法:
  #### `st` `_strip_cache_control(payload: dict) -> None`    @staticmethod  L264
    - _文档首行_（仅供参考）: Remove cache_control markers before OAuth requests reach Anthropic.
    - 分支数 10，函数体节点数 138
    - 调用: get, isinstance, pop
  #### `st` `_calc_backoff_ms(attempt: int, error: Exception) -> int`    @staticmethod  L349
    - _文档首行_（仅供参考）: Exponential backoff with a fixed 20% buffer.
    - 分支数 3，函数体节点数 103；return: total_ms
    - 调用: int, hasattr, get
  - 反射: hasattr (L355)
  #### `m` `_validate_retry_config(self) -> None`  L65
    - 分支数 1，函数体节点数 17；raise: ValueError('retry_max_attempts must be >= 1')
    - 调用: ValueError
  #### `m` `model_post_init(self, __context: Any) -> None`  L69
    - _文档首行_（仅供参考）: Auto-load credentials and configure OAuth if needed.
    - 分支数 8，函数体节点数 237
    - 调用: _validate_retry_config, hasattr, get_secret_value, str, load_claude_code_credential, info, warning, is_oauth_token, SecretStr, isinstance, model_post_init, super, _patch_client_oauth
  - 反射: hasattr (L84)
  #### `m` `_patch_client_oauth(self, client: Any) -> None`  L128
    - _文档首行_（仅供参考）: Swap api_key → auth_token on an Anthropic SDK client for OAuth Bearer auth.
    - 分支数 1，函数体节点数 39
    - 调用: hasattr
  - 反射: hasattr (L130), hasattr (L130)
  #### `m` `_get_request_payload(self, input_: Any, *, stop: list[str] | None, **kwargs) -> dict`  L134
    - _文档首行_（仅供参考）: Override to inject prompt caching, thinking budget, and OAuth billing.
    - 分支数 3，函数体节点数 83；可变参数（*args/**kwargs）；return: payload
    - 调用: _get_request_payload, super, _apply_oauth_billing, _apply_prompt_caching, _apply_thinking_budget
  #### `m` `_apply_oauth_billing(self, payload: dict) -> None`  L155
    - _文档首行_（仅供参考）: Inject the billing header block required for all OAuth requests.
    - 分支数 5，函数体节点数 224
    - 调用: get, isinstance, gethostname, hexdigest, sha256, encode, str, uuid4, dumps
  #### `m` `_apply_prompt_caching(self, payload: dict) -> None`  L192
    - _文档首行_（仅供参考）: Apply ephemeral cache_control to system, recent messages, and last tool definition.
    - 分支数 12，函数体节点数 319
    - 调用: get, isinstance, append, max, len, range
  #### `m` `_apply_thinking_budget(self, payload: dict) -> None`  L250
    - _文档首行_（仅供参考）: Auto-allocate thinking budget (80% of max_tokens).
    - 分支数 3，函数体节点数 79；return: None
    - 调用: get, isinstance, int
  #### `m` `_create(self, payload: dict) -> Any`  L286
    - 分支数 1，函数体节点数 30；return: super()._create(payload)
    - 调用: _strip_cache_control, _create, super
  #### `m` `_generate(self, messages: list[BaseMessage], stop: list[str] | None, **kwargs) -> Any`  L296
    - _文档首行_（仅供参考）: Override with OAuth patching and retry logic.
    - 分支数 5，函数体节点数 210；可变参数（*args/**kwargs）；raise: bare raise, last_error；return: super()._generate(messages, stop=stop, **kwargs)
    - 调用: _patch_client_oauth, range, _generate, super, _calc_backoff_ms, warning, sleep
  #### `⏵m` `async _acreate(self, payload: dict) -> Any`  L291
    - 分支数 1，函数体节点数 31；return: await super()._acreate(payload)
    - 调用: _strip_cache_control, _acreate, super
  #### `⏵m` `async _agenerate(self, messages: list[BaseMessage], stop: list[str] | None, **kwargs) -> Any`  L321
    - _文档首行_（仅供参考）: Async override with OAuth patching and retry logic.
    - 分支数 5，函数体节点数 215；可变参数（*args/**kwargs）；raise: bare raise, last_error；return: await super()._agenerate(messages, stop=stop, **kwargs)
    - 调用: _patch_client_oauth, range, _agenerate, super, _calc_backoff_ms, warning, sleep

## 文件内调用关系
- `ClaudeChatModel.model_post_init` -> _validate_retry_config, model_post_init, _patch_client_oauth
- `ClaudeChatModel._get_request_payload` -> _get_request_payload, _apply_oauth_billing, _apply_prompt_caching, _apply_thinking_budget
- `ClaudeChatModel._create` -> _strip_cache_control, _create
- `ClaudeChatModel._acreate` -> _strip_cache_control, _acreate
- `ClaudeChatModel._generate` -> _patch_client_oauth, _generate, _calc_backoff_ms
- `ClaudeChatModel._agenerate` -> _patch_client_oauth, _agenerate, _calc_backoff_ms

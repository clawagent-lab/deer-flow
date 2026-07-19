# `backend/packages/harness/deerflow/agents/middlewares/title_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/title_middleware.py`  ·  行数: 236

**模块文档首行**（仅供参考）: Middleware for automatic thread title generation.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: logging, re
- `typing` -> TYPE_CHECKING, Any, NotRequired, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langgraph.config` -> get_config
- `langgraph.constants` -> TAG_NOSTREAM
- `langgraph.runtime` -> Runtime
- `deerflow.agents.middlewares.dynamic_context_middleware` -> is_dynamic_context_reminder
- `deerflow.config.title_config` -> get_title_config
- `deerflow.models` -> create_chat_model

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `TitleMiddlewareState`  L24
- 继承: AgentState
- _文档首行_: Compatible with the `ThreadState` schema.
- 类/实例变量:
  - `title` = <annotated>

### 类 `TitleMiddleware`  L30
- 继承: AgentMiddleware[TitleMiddlewareState]
- _文档首行_: Automatically generate a title for the thread after the first user message.
- 类/实例变量:
  - `state_schema` = TitleMiddlewareState
- 方法:
  #### `st` `_message_type(message: object) -> str | None`    @staticmethod  L67
    - 分支数 3，函数体节点数 82；return: 'human', 'ai', message_type if isinstance(message_type, str) else None
    - 调用: getattr, isinstance, get
  - 反射: getattr (L68)
  #### `st` `_message_content(message: object) -> object`    @staticmethod  L78
    - 分支数 1，函数体节点数 33；return: message.get('content', ''), getattr(message, 'content', '')
    - 调用: isinstance, get, getattr
  - 反射: getattr (L81)
  #### `st` `_is_dynamic_context_reminder_message(message: object) -> bool`    @staticmethod  L84
    - 分支数 2，函数体节点数 55；return: True, isinstance(additional_kwargs, dict) and bool(additional_kwargs.get('dynamic_context_reminder')), False
    - 调用: is_dynamic_context_reminder, isinstance, get, bool
  #### `st` `_is_user_message_for_title(message: object) -> bool`    @staticmethod  L93
    - 分支数 0，函数体节点数 31；return: TitleMiddleware._message_type(message) == 'human' and (not TitleMiddleware._is_dynamic_context_reminder_message(message))
    - 调用: _message_type, _is_dynamic_context_reminder_message
  #### `m` `__init__(self, *, app_config: 'AppConfig | None', title_config: 'TitleConfig | None')`  L35
    - 分支数 0，函数体节点数 30
    - 调用: __init__, super
  #### `m` `_get_title_config(self)`  L40
    - 分支数 2，函数体节点数 35；return: self._title_config, self._app_config.title, get_title_config()
    - 调用: get_title_config
  #### `m` `_normalize_content(self, content: object) -> str`  L47
    - 分支数 5，函数体节点数 111；return: content, '\n'.join((part for part in parts if part)), text_value, self._normalize_content(nested_content), ''
    - 调用: isinstance, _normalize_content, join, get
  #### `m` `_get_title_user_message(self, state: TitleMiddlewareState) -> str`  L96
    - 分支数 0，函数体节点数 56；return: self._normalize_content(user_msg_content)
    - 调用: get, next, _message_content, _is_user_message_for_title, _normalize_content
  #### `m` `_should_generate_title(self, state: TitleMiddlewareState, *, allow_partial_exchange: bool) -> bool`  L101
    - _文档首行_（仅供参考）: Check if we should generate a title for this thread.
    - 分支数 3，函数体节点数 135；return: False, len(user_messages) == 1 and (len(assistant_messages) >= 1 or allow_partial_exchange)
    - 调用: _get_title_config, get, len, _is_user_message_for_title, _message_type
  #### `m` `_build_title_prompt(self, state: TitleMiddlewareState) -> tuple[str, str]`  L129
    - _文档首行_（仅供参考）: Extract user/assistant messages and build the title prompt.
    - 分支数 0，函数体节点数 130；return: (prompt, user_msg)
    - 调用: _get_title_config, get, next, _message_content, _message_type, _get_title_user_message, _strip_think_tags, _normalize_content, format
  #### `m` `_strip_think_tags(self, text: str) -> str`  L149
    - _文档首行_（仅供参考）: Remove <think>...</think> blocks emitted by reasoning models (e.g. minimax, DeepSeek-R1).
    - 分支数 0，函数体节点数 28；return: re.sub('<think>[\\s\\S]*?</think>', '', text, flags=re.IGNORECASE).strip()
    - 调用: strip, sub
  #### `m` `_parse_title(self, content: object) -> str`  L153
    - _文档首行_（仅供参考）: Normalize model output into a clean title string.
    - 分支数 0，函数体节点数 78；return: title[:config.max_chars] if len(title) > config.max_chars else title
    - 调用: _get_title_config, _normalize_content, _strip_think_tags, strip, len
  #### `m` `_fallback_title(self, user_msg: str) -> str`  L161
    - 分支数 1，函数体节点数 82；return: user_msg[:body].rstrip() + ellipsis, user_msg if user_msg else 'New Conversation'
    - 调用: _get_title_config, min, len, rstrip
  #### `m` `_get_runnable_config(self) -> dict[str, Any]`  L172
    - _文档首行_（仅供参考）: Inherit the parent RunnableConfig and add middleware tag.
    - 分支数 1，函数体节点数 68；return: config
    - 调用: get_config, get
  #### `m` `_generate_title_result(self, state: TitleMiddlewareState, *, allow_partial_exchange: bool) -> dict | None`  L191
    - _文档首行_（仅供参考）: Generate a local fallback title without blocking on an LLM call.
    - 分支数 1，函数体节点数 52；return: None, {'title': self._fallback_title(user_msg)}
    - 调用: _should_generate_title, _get_title_user_message, _fallback_title
  #### `m` `after_model(self, state: TitleMiddlewareState, runtime: Runtime) -> dict | None`    @override  L230
    - 分支数 0，函数体节点数 24；return: self._generate_title_result(state)
    - 调用: _generate_title_result
  #### `⏵m` `async _agenerate_title_result(self, state: TitleMiddlewareState) -> dict | None`  L199
    - _文档首行_（仅供参考）: Generate a configured LLM title asynchronously and fall back locally.
    - 分支数 5，函数体节点数 184；return: None, {'title': self._fallback_title(user_msg)}, {'title': title}
    - 调用: _should_generate_title, _get_title_config, _get_title_user_message, _fallback_title, _build_title_prompt, create_chat_model, ainvoke, _get_runnable_config, _parse_title, debug
  #### `⏵m` `async aafter_model(self, state: TitleMiddlewareState, runtime: Runtime) -> dict | None`    @override  L234
    - 分支数 0，函数体节点数 25；return: await self._agenerate_title_result(state)
    - 调用: _agenerate_title_result

## 文件内调用关系
- `TitleMiddleware.__init__` -> __init__
- `TitleMiddleware._normalize_content` -> _normalize_content
- `TitleMiddleware._is_user_message_for_title` -> _message_type, _is_dynamic_context_reminder_message
- `TitleMiddleware._get_title_user_message` -> _message_content, _is_user_message_for_title, _normalize_content
- `TitleMiddleware._should_generate_title` -> _get_title_config, _is_user_message_for_title, _message_type
- `TitleMiddleware._build_title_prompt` -> _get_title_config, _message_content, _message_type, _get_title_user_message, _strip_think_tags, _normalize_content
- `TitleMiddleware._parse_title` -> _get_title_config, _normalize_content, _strip_think_tags
- `TitleMiddleware._fallback_title` -> _get_title_config
- `TitleMiddleware._generate_title_result` -> _should_generate_title, _get_title_user_message, _fallback_title
- `TitleMiddleware._agenerate_title_result` -> _should_generate_title, _get_title_config, _get_title_user_message, _fallback_title, _build_title_prompt, _get_runnable_config, _parse_title
- `TitleMiddleware.after_model` -> _generate_title_result
- `TitleMiddleware.aafter_model` -> _agenerate_title_result

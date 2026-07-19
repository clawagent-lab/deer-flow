# `backend/packages/harness/deerflow/models/factory.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/factory.py`  ·  行数: 305

## 模块概览
- 函数 7 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `langchain.chat_models` -> BaseChatModel
- `langchain_openai.chat_models.base` -> BaseChatOpenAI
- `deerflow.config` -> get_app_config
- `deerflow.config.app_config` -> AppConfig
- `deerflow.reflection` -> resolve_class
- `deerflow.tracing` -> build_tracing_callbacks

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_DEFAULT_STREAM_CHUNK_TIMEOUT_SECONDS` = 240.0

## 函数
#### `ƒ` `_deep_merge_dicts(base: dict | None, override: dict) -> dict`  L14
  - _文档首行_（仅供参考）: Recursively merge two dictionaries without mutating the inputs.
  - 分支数 2，函数体节点数 90；return: merged
  - 调用: dict, items, isinstance, get, _deep_merge_dicts

#### `ƒ` `_vllm_disable_chat_template_kwargs(chat_template_kwargs: dict) -> dict`  L25
  - _文档首行_（仅供参考）: Build the disable payload for vLLM/Qwen chat template kwargs.
  - 分支数 2，函数体节点数 52；return: disable_kwargs

#### `ƒ` `_declares_api_base(model_class: type) -> bool`  L35
  - _文档首行_（仅供参考）: Whether *model_class* declares ``api_base`` as its own constructor field.
  - 分支数 0，函数体节点数 20；return: 'api_base' in getattr(model_class, 'model_fields', {})
  - 调用: getattr
  - 反射: getattr (L42)

#### `ƒ` `_normalize_openai_base_url(model_class: type, model_settings_from_config: dict) -> None`  L45
  - _文档首行_（仅供参考）: Map the common ``api_base`` alias to ``base_url`` for OpenAI-compatible clients.
  - 分支数 3，函数体节点数 84；return: None
  - 调用: issubclass, _declares_api_base, pop, warning, debug

#### `ƒ` `_warn_unknown_model_settings(model_class, model_name: str, model_settings_from_config: dict) -> None`  L76
  - _文档首行_（仅供参考）: Warn about config keys the OpenAI client will silently divert into ``model_kwargs``.
  - 分支数 5，函数体节点数 133；return: None
  - 调用: issubclass, getattr, set, keys, values, add, sorted, warning
  - 反射: getattr (L97), getattr (L102), getattr (L121)

#### `ƒ` `_apply_stream_chunk_timeout_default(model_class: type, model_settings_from_config: dict) -> None`  L137
  - _文档首行_（仅供参考）: Inject a generous ``stream_chunk_timeout`` for OpenAI-compatible clients.
  - 分支数 2，函数体节点数 45；return: None
  - 调用: issubclass, pop

#### `ƒ` `create_chat_model(name: str | None, thinking_enabled: bool, *, app_config: AppConfig | None, attach_tracing: bool, **kwargs) -> BaseChatModel`  L174
  - _文档首行_（仅供参考）: Create a chat model instance from the config.
  - 分支数 21，函数体节点数 617；可变参数（*args/**kwargs）；raise: ValueError(f'Model {name} not found in config'), ValueError(f'Model {name} does not support thinking. Set `supports_thinking` to true in the `config.yaml` to enable thinking.')；return: model_instance
  - 调用: get_app_config, get_model_config, ValueError, resolve_class, model_dump, dict, get, update, _deep_merge_dicts, _vllm_disable_chat_template_kwargs, pop, _normalize_openai_base_url, _apply_stream_chunk_timeout_default, issubclass, getattr, _warn_unknown_model_settings, model_class, build_tracing_callbacks, debug, len
  - 反射: getattr (L281), getattr (L291)

## 文件内调用关系
- `_deep_merge_dicts` -> _deep_merge_dicts
- `_normalize_openai_base_url` -> _declares_api_base
- `create_chat_model` -> _deep_merge_dicts, _vllm_disable_chat_template_kwargs, _normalize_openai_base_url, _apply_stream_chunk_timeout_default, _warn_unknown_model_settings

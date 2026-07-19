# `backend/packages/harness/deerflow/config/tracing_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/tracing_config.py`  ·  行数: 213

## 模块概览
- 函数 9 个，类 4 个，模块级常量 4 个

## 依赖（import）
- 模块: os, threading
- `pydantic` -> BaseModel, Field

## 模块级常量
- `_config_lock` = threading.Lock()
- `_MONOCLE_EXPORTERS` = ('file', 'console', 'okahu', 's3', 'blob', 'gcs')
- `_tracing_config` = None
- `_TRUTHY_VALUES` = {'1', 'true', 'yes', 'on'}

## 函数
#### `ƒ` `_env_flag_preferred(*names) -> bool`  L125
  - _文档首行_（仅供参考）: Return the boolean value of the first env var that is present and non-empty.
  - 分支数 2，函数体节点数 54；可变参数（*args/**kwargs）；return: value.strip().lower() in _TRUTHY_VALUES, False
  - 调用: get, strip, lower

#### `ƒ` `_first_env_value(*names) -> str | None`  L134
  - _文档首行_（仅供参考）: Return the first non-empty environment value from candidate names.
  - 分支数 2，函数体节点数 47；可变参数（*args/**kwargs）；return: value.strip(), None
  - 调用: get, strip

#### `ƒ` `get_tracing_config() -> TracingConfig`  L143
  - _文档首行_（仅供参考）: Get the current tracing configuration from environment variables.
  - 分支数 3，函数体节点数 122；return: _tracing_config
  - 调用: TracingConfig, LangSmithTracingConfig, _env_flag_preferred, _first_env_value, LangfuseTracingConfig, MonocleTracingConfig

#### `ƒ` `get_enabled_tracing_providers() -> list[str]`  L173
  - _文档首行_（仅供参考）: Return the configured tracing providers that are enabled and complete.
  - 分支数 0，函数体节点数 16；return: get_tracing_config().enabled_providers
  - 调用: get_tracing_config

#### `ƒ` `get_explicitly_enabled_tracing_providers() -> list[str]`  L178
  - _文档首行_（仅供参考）: Return tracing providers explicitly enabled by config, even if incomplete.
  - 分支数 0，函数体节点数 16；return: get_tracing_config().explicitly_enabled_providers
  - 调用: get_tracing_config

#### `ƒ` `validate_enabled_tracing_providers() -> None`  L183
  - _文档首行_（仅供参考）: Validate that any explicitly enabled providers are fully configured.
  - 分支数 0，函数体节点数 12
  - 调用: validate_enabled, get_tracing_config

#### `ƒ` `is_tracing_enabled() -> bool`  L188
  - _文档首行_（仅供参考）: Check if any tracing provider is enabled and fully configured.
  - 分支数 0，函数体节点数 12；return: get_tracing_config().is_configured
  - 调用: get_tracing_config

#### `ƒ` `is_monocle_tracing_enabled() -> bool`  L193
  - _文档首行_（仅供参考）: Whether Monocle OTel observability is enabled (via ``MONOCLE_TRACING``).
  - 分支数 0，函数体节点数 14；return: get_tracing_config().monocle.is_enabled
  - 调用: get_tracing_config

#### `ƒ` `reset_tracing_config() -> None`  L203
  - _文档首行_（仅供参考）: Discard the cached :class:`TracingConfig` so the next call rebuilds it.
  - 分支数 1，函数体节点数 14

## 类
### 类 `LangSmithTracingConfig`  L9
- 继承: BaseModel
- _文档首行_: Configuration for LangSmith tracing.
- 类/实例变量:
  - `enabled` = Field(...)
  - `api_key` = Field(...)
  - `project` = Field(...)
  - `endpoint` = Field(...)
- 方法:
  #### `prop` `is_configured(self) -> bool`    @property  L18
    - 分支数 0，函数体节点数 21；return: self.enabled and bool(self.api_key)
    - 调用: bool
  #### `m` `validate(self) -> None`  L21
    - 分支数 1，函数体节点数 22；raise: ValueError('LangSmith tracing is enabled but LANGSMITH_API_KEY (or LANGCHAIN_API_KEY) is not set.')
    - 调用: ValueError

### 类 `LangfuseTracingConfig`  L26
- 继承: BaseModel
- _文档首行_: Configuration for Langfuse tracing.
- 类/实例变量:
  - `enabled` = Field(...)
  - `public_key` = Field(...)
  - `secret_key` = Field(...)
  - `host` = Field(...)
- 方法:
  #### `prop` `is_configured(self) -> bool`    @property  L35
    - 分支数 0，函数体节点数 28；return: self.enabled and bool(self.public_key) and bool(self.secret_key)
    - 调用: bool
  #### `m` `validate(self) -> None`  L38
    - 分支数 4，函数体节点数 67；raise: ValueError(f"Langfuse tracing is enabled but required settings are missing: {', '.join(missing)}")；return: None
    - 调用: append, ValueError, join

### 类 `MonocleTracingConfig`  L56
- 继承: BaseModel
- _文档首行_: Configuration for Monocle telemetry.
- 类/实例变量:
  - `enabled` = Field(...)
  - `exporters` = Field(...)
  - `okahu_api_key` = Field(...)
- 方法:
  #### `prop` `is_enabled(self) -> bool`    @property  L64
    - 分支数 0，函数体节点数 12；return: self.enabled
  #### `prop` `exporter_list(self) -> list[str]`    @property  L70
    - _文档首行_（仅供参考）: The configured exporters, parsed once so validation and setup agree.
    - 分支数 0，函数体节点数 36；return: [e.strip() for e in self.exporters.split(',') if e.strip()]
    - 调用: strip, split
  #### `m` `validate(self) -> None`  L74
    - 分支数 3，函数体节点数 80；raise: ValueError(f"MONOCLE_EXPORTERS has unknown exporter(s): {', '.join(unknown)}. Allowed: {', '.join(_MONOCLE_EXPORTERS)}."), ValueError("Monocle 'okahu' exporter is selected but OKAHU_API_KEY is not set.")；return: None
    - 调用: ValueError, join

### 类 `TracingConfig`  L85
- 继承: BaseModel
- _文档首行_: Tracing configuration for supported providers.
- 类/实例变量:
  - `langsmith` = Field(...)
  - `langfuse` = Field(...)
  - `monocle` = Field(...)
- 方法:
  #### `prop` `is_configured(self) -> bool`    @property  L93
    - 分支数 0，函数体节点数 15；return: bool(self.enabled_providers)
    - 调用: bool
  #### `prop` `explicitly_enabled_providers(self) -> list[str]`    @property  L97
    - 分支数 2，函数体节点数 53；return: enabled
    - 调用: append
  #### `prop` `enabled_providers(self) -> list[str]`    @property  L106
    - 分支数 2，函数体节点数 53；return: enabled
    - 调用: append
  #### `m` `validate_enabled(self) -> None`  L114
    - 分支数 0，函数体节点数 20
    - 调用: validate

## 文件内调用关系
- `get_tracing_config` -> _env_flag_preferred, _first_env_value
- `get_enabled_tracing_providers` -> get_tracing_config
- `get_explicitly_enabled_tracing_providers` -> get_tracing_config
- `validate_enabled_tracing_providers` -> validate_enabled, get_tracing_config
- `is_tracing_enabled` -> get_tracing_config
- `is_monocle_tracing_enabled` -> get_tracing_config
- `TracingConfig.validate_enabled` -> validate

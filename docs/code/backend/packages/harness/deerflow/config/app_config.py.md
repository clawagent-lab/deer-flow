# `backend/packages/harness/deerflow/config/app_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/app_config.py`  ·  行数: 668

## 模块概览
- 函数 14 个，类 4 个，模块级常量 10 个

## 依赖（import）
- 模块: hashlib, logging, os, yaml
- `collections.abc` -> Mapping
- `contextvars` -> ContextVar
- `pathlib` -> Path
- `typing` -> Any, Literal, Self
- `dotenv` -> load_dotenv
- `pydantic` -> BaseModel, ConfigDict, Field, PrivateAttr, model_validator
- `deerflow.config.acp_config` -> ACPAgentConfig, load_acp_config_from_dict
- `deerflow.config.agents_api_config` -> AgentsApiConfig, load_agents_api_config_from_dict
- `deerflow.config.auth_config` -> AuthAppConfig
- `deerflow.config.authorization_config` -> AuthorizationConfig, load_authorization_config_from_dict
- `deerflow.config.channel_connections_config` -> ChannelConnectionsConfig
- `deerflow.config.checkpointer_config` -> CheckpointerConfig, load_checkpointer_config_from_dict
- `deerflow.config.database_config` -> DatabaseConfig
- `deerflow.config.extensions_config` -> ExtensionsConfig
- `deerflow.config.guardrails_config` -> GuardrailsConfig, load_guardrails_config_from_dict
- `deerflow.config.input_polish_config` -> InputPolishConfig
- `deerflow.config.loop_detection_config` -> LoopDetectionConfig
- `deerflow.config.memory_config` -> MemoryConfig, load_memory_config_from_dict
- `deerflow.config.model_config` -> ModelConfig
- `deerflow.config.read_before_write_config` -> ReadBeforeWriteConfig
- `deerflow.config.reload_boundary` -> format_field_description
- `deerflow.config.run_events_config` -> RunEventsConfig
- `deerflow.config.run_ownership_config` -> RunOwnershipConfig
- `deerflow.config.runtime_paths` -> existing_project_file
- `deerflow.config.safety_finish_reason_config` -> SafetyFinishReasonConfig
- `deerflow.config.sandbox_config` -> SandboxConfig
- `deerflow.config.scheduler_config` -> SchedulerConfig
- `deerflow.config.skill_evolution_config` -> SkillEvolutionConfig
- `deerflow.config.skill_scan_config` -> SkillScanConfig
- `deerflow.config.skills_config` -> SkillsConfig
- `deerflow.config.stream_bridge_config` -> StreamBridgeConfig, load_stream_bridge_config_from_dict
- `deerflow.config.subagents_config` -> SubagentsAppConfig, load_subagents_config_from_dict
- `deerflow.config.suggestions_config` -> SuggestionsConfig
- `deerflow.config.summarization_config` -> SummarizationConfig, load_summarization_config_from_dict
- `deerflow.config.title_config` -> TitleConfig, load_title_config_from_dict
- `deerflow.config.token_budget_config` -> TokenBudgetConfig
- `deerflow.config.token_usage_config` -> TokenUsageConfig
- `deerflow.config.tool_config` -> ToolConfig, ToolGroupConfig
- `deerflow.config.tool_output_config` -> ToolOutputConfig
- `deerflow.config.tool_progress_config` -> ToolProgressConfig
- `deerflow.config.tool_search_config` -> ToolSearchConfig, load_tool_search_config_from_dict

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `CONFIG_FILE_DATABASE_DEFAULTS` = {'backend': 'sqlite', 'sqlite_dir': '.deer-flow/data'}
- `_app_config` = None
- `_app_config_path` = None
- `_app_config_mtime` = None
- `_ConfigSignature` = tuple[float | None, int | None, str | None]
- `_app_config_signature` = None
- `_app_config_is_custom` = False
- `_current_app_config` = ContextVar('deerflow_current_app_config', default=None)
- `_current_app_config_stack` = ContextVar('deerflow_current_app_config_stack', default=())

## 函数
#### `ƒ` `is_trace_correlation_enabled(config: Any) -> bool`  L80
  - _文档首行_（仅供参考）: Return ``True`` when ``logging.enhance.enabled`` is set on *config*.
  - 分支数 0，函数体节点数 40；return: bool(getattr(enhance, 'enabled', False))
  - 调用: getattr, bool
  - 反射: getattr (L91), getattr (L92), getattr (L93)

#### `ƒ` `_legacy_config_candidates() -> tuple[Path, ...]`  L96
  - _文档首行_（仅供参考）: Return source-tree config.yaml locations for monorepo compatibility.
  - 分支数 0，函数体节点数 49；return: (backend_dir / 'config.yaml', repo_root / 'config.yaml')
  - 调用: resolve, Path

#### `ƒ` `logging_level_from_config(name: str | None) -> int`  L103
  - _文档首行_（仅供参考）: Map ``config.yaml`` ``log_level`` string to a :mod:`logging` level constant.
  - 分支数 0，函数体节点数 41；return: mapping.get((name or 'info').strip().upper(), logging.INFO)
  - 调用: getLevelNamesMapping, get, upper, strip

#### `ƒ` `apply_logging_level(name: str | None) -> None`  L109
  - _文档首行_（仅供参考）: Resolve *name* to a logging level and apply it to the ``deerflow``/``app`` logger hierarchies.
  - 分支数 3，函数体节点数 65
  - 调用: logging_level_from_config, setLevel, getLogger

#### `ƒ` `_get_config_mtime(config_path: Path) -> float | None`  L526
  - _文档首行_（仅供参考）: Get the modification time of a config file if it exists.
  - 分支数 1，函数体节点数 26；return: config_path.stat().st_mtime, None
  - 调用: stat
  - 文件IO: stat (L529)

#### `ƒ` `_get_config_signature(config_path: Path) -> _ConfigSignature | None`  L534
  - _文档首行_（仅供参考）: Get cache metadata for a config file, including a content digest.
  - 分支数 4，函数体节点数 102；return: None, (stat_result.st_mtime, stat_result.st_size, None), (stat_result.st_mtime, stat_result.st_size, digest.hexdigest())
  - 调用: stat, sha256, open, iter, read, update, hexdigest
  - 文件IO: stat (L537), open (L543), read (L544)

#### `ƒ` `_load_and_cache_app_config(config_path: str | None) -> AppConfig`  L552
  - _文档首行_（仅供参考）: Load config from disk and refresh cache metadata.
  - 分支数 0，函数体节点数 65；return: _app_config
  - 调用: resolve_config_path, from_file, str, _get_config_mtime, _get_config_signature

#### `ƒ` `get_app_config() -> AppConfig`  L565
  - _文档首行_（仅供参考）: Get the DeerFlow config instance.
  - 分支数 5，函数体节点数 156；return: runtime_override, _app_config
  - 调用: get, resolve_config_path, _get_config_mtime, _get_config_signature, info, _load_and_cache_app_config, str

#### `ƒ` `reload_app_config(config_path: str | None) -> AppConfig`  L600
  - _文档首行_（仅供参考）: Reload the config from file and update the cached instance.
  - 分支数 0，函数体节点数 19；return: _load_and_cache_app_config(config_path)
  - 调用: _load_and_cache_app_config

#### `ƒ` `reset_app_config() -> None`  L616
  - _文档首行_（仅供参考）: Reset the cached config instance.
  - 分支数 0，函数体节点数 26

#### `ƒ` `set_app_config(config: AppConfig) -> None`  L631
  - _文档首行_（仅供参考）: Set a custom config instance.
  - 分支数 0，函数体节点数 30

#### `ƒ` `peek_current_app_config() -> AppConfig | None`  L647
  - _文档首行_（仅供参考）: Return the runtime-scoped AppConfig override, if one is active.
  - 分支数 0，函数体节点数 15；return: _current_app_config.get()
  - 调用: get

#### `ƒ` `push_current_app_config(config: AppConfig) -> None`  L652
  - _文档首行_（仅供参考）: Push a runtime-scoped AppConfig override for the current execution context.
  - 分支数 0，函数体节点数 41
  - 调用: get, set

#### `ƒ` `pop_current_app_config() -> None`  L659
  - _文档首行_（仅供参考）: Pop the latest runtime-scoped AppConfig override for the current execution context.
  - 分支数 1，函数体节点数 58；return: None
  - 调用: get, set

## 类
### 类 `CircuitBreakerConfig`  L60
- 继承: BaseModel
- _文档首行_: Configuration for the LLM Circuit Breaker.
- 类/实例变量:
  - `failure_threshold` = Field(default=5, description='Number of consecutive failu...
  - `recovery_timeout_sec` = Field(default=60, description='Time in seconds before att...

### 类 `LoggingEnhanceConfig`  L67
- 继承: BaseModel
- _文档首行_: Request trace logging enhancement settings.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Enable request-level tr...
  - `format` = Field(default='text', description='Enhanced log output fo...

### 类 `LoggingConfig`  L74
- 继承: BaseModel
- _文档首行_: Logging configuration.
- 类/实例变量:
  - `enhance` = Field(default_factory=LoggingEnhanceConfig, description='...

### 类 `AppConfig`  L127
- 继承: BaseModel
- _文档首行_: Config for the DeerFlow application
- 类/实例变量:
  - `log_level` = Field(default='info', description=format_field_descriptio...
  - `logging` = Field(default_factory=LoggingConfig, description=format_f...
  - `token_usage` = Field(default_factory=TokenUsageConfig, description='Toke...
  - `token_budget` = Field(default_factory=TokenBudgetConfig, description='Tok...
  - `max_recursion_limit` = Field(default=1000, ge=1, description='Hard server-side c...
  - `models` = Field(default_factory=list, description='Available models')
  - `sandbox` = Field(description=format_field_description('sandbox', fie...
  - `tools` = Field(default_factory=list, description='Available tools')
  - `tool_groups` = Field(default_factory=list, description='Available tool g...
  - `skills` = Field(default_factory=SkillsConfig, description='Skills c...
  - `skill_scan` = Field(default_factory=SkillScanConfig, description='Nativ...
  - `skill_evolution` = Field(default_factory=SkillEvolutionConfig, description='...
  - `extensions` = Field(default_factory=ExtensionsConfig, description='Exte...
  - `tool_output` = Field(default_factory=ToolOutputConfig, description='Tool...
  - `tool_search` = Field(default_factory=ToolSearchConfig, description='Tool...
  - `title` = Field(default_factory=TitleConfig, description='Automatic...
  - `summarization` = Field(default_factory=SummarizationConfig, description='C...
  - `memory` = Field(default_factory=MemoryConfig, description='Memory s...
  - `agents_api` = Field(default_factory=AgentsApiConfig, description='Custo...
  - `acp_agents` = Field(default_factory=dict, description='ACP-compatible a...
  - `subagents` = Field(default_factory=SubagentsAppConfig, description='Su...
  - `guardrails` = Field(default_factory=GuardrailsConfig, description='Guar...
  - `authorization` = Field(default_factory=AuthorizationConfig, description='F...
  - `input_polish` = Field(default_factory=InputPolishConfig, description='Pre...
  - `suggestions` = Field(default_factory=SuggestionsConfig, description='Fol...
  - …(+17)
- 方法:
  #### `cls` `_drop_null_config_sections(cls, data: Any) -> Any`    @model_validator(...), classmethod  L243
    - _文档首行_（仅供参考）: Treat a present-but-null config section as absent so its default applies.
    - 分支数 1，函数体节点数 51；return: {key: value for key, value in data.items() if value is not None}, data
    - 调用: isinstance, items, model_validator
  #### `cls` `resolve_config_path(cls, config_path: str | None) -> Path`    @classmethod  L267
    - _文档首行_（仅供参考）: Resolve the config file path.
    - 分支数 7，函数体节点数 128；raise: FileNotFoundError(f'Config file specified by param `config_path` not found at {path}'), FileNotFoundError(f'Config file specified by environment variable `DEER_FLOW_CONFIG_PATH` not found at {path}'), FileNotFoundError('`config.yaml` file not found in the project root or legacy backend/repository root locations')；return: path, project_config
    - 调用: Path, exists, FileNotFoundError, getenv, existing_project_file, _legacy_config_candidates
  - 文件IO: exists (L278), exists (L283), exists (L292)
  - 环境变量: getenv (L281), getenv (L282)
  #### `cls` `from_file(cls, config_path: str | None) -> Self`    @classmethod  L297
    - _文档首行_（仅供参考）: Load config from YAML file.
    - 分支数 3，函数体节点数 168；return: result
    - 调用: resolve_config_path, open, safe_load, _check_config_version, resolve_env_variables, _apply_database_defaults, from_file, model_dump, model_validate, warning, _validate_acp_agents, get, _apply_singleton_configs
  - 文件IO: open (L309)
  #### `cls` `_validate_acp_agents(cls, config_data: Mapping[str, Mapping[str, object]] | None) -> dict[str, ACPAgentConfig]`    @classmethod  L337
    - 分支数 1，函数体节点数 69；return: {name: ACPAgentConfig(**cfg) for name, cfg in config_data.items()}
    - 调用: ACPAgentConfig, items
  #### `cls` `_apply_singleton_configs(cls, config: Self, acp_agents: dict[str, ACPAgentConfig]) -> None`    @classmethod  L346
    - 分支数 1，函数体节点数 201
    - 调用: get_checkpointer_config, load_title_config_from_dict, model_dump, load_summarization_config_from_dict, load_memory_config_from_dict, load_agents_api_config_from_dict, load_subagents_config_from_dict, load_tool_search_config_from_dict, load_guardrails_config_from_dict, load_authorization_config_from_dict, load_checkpointer_config_from_dict, load_stream_bridge_config_from_dict, load_acp_config_from_dict, items, reset_checkpointer, reset_store
  #### `cls` `_apply_database_defaults(cls, config_data: dict[str, Any]) -> None`    @classmethod  L373
    - _文档首行_（仅供参考）: Apply config.yaml defaults for persistence when the section is absent.
    - 分支数 3，函数体节点数 79；return: None
    - 调用: get, isinstance, items, setdefault
  #### `cls` `_check_config_version(cls, config_data: dict, config_path: Path) -> None`    @classmethod  L385
    - _文档首行_（仅供参考）: Check if the user's config.yaml is outdated compared to config.example.yaml.
    - 分支数 9，函数体节点数 182；return: None
    - 调用: int, get, range, exists, open, safe_load, warning
  - 文件IO: exists (L401), open (L412)
  #### `cls` `resolve_env_variables(cls, config: Any) -> Any`    @classmethod  L430
    - _文档首行_（仅供参考）: Recursively resolve environment variables in the config.
    - 分支数 5，函数体节点数 126；raise: ValueError(f'Environment variable {config[1:]} not found for config value {config}')；return: env_value, config, {k: cls.resolve_env_variables(v) for k, v in config.items()}, [cls.resolve_env_variables(item) for item in config]
    - 调用: isinstance, startswith, getenv, ValueError, resolve_env_variables, items
  - 环境变量: getenv (L443)
  #### `m` `_build_name_indexes(self) -> 'AppConfig'`    @model_validator(...)  L455
    - _文档首行_（仅供参考）: Build name -> config lookup tables for O(1) ``get_*_config``.
    - 分支数 3，函数体节点数 134；return: self
    - 调用: setdefault, model_validator
  #### `m` `get_model_config(self, name: str) -> ModelConfig | None`  L479
    - _文档首行_（仅供参考）: Get the model config by name.
    - 分支数 0，函数体节点数 23；return: self._models_by_name.get(name)
    - 调用: get
  #### `m` `get_tool_config(self, name: str) -> ToolConfig | None`  L490
    - _文档首行_（仅供参考）: Get the tool config by name.
    - 分支数 0，函数体节点数 23；return: self._tools_by_name.get(name)
    - 调用: get
  #### `m` `get_tool_group_config(self, name: str) -> ToolGroupConfig | None`  L501
    - _文档首行_（仅供参考）: Get the tool group config by name.
    - 分支数 0，函数体节点数 23；return: self._tool_groups_by_name.get(name)
    - 调用: get

## 文件内调用关系
- `apply_logging_level` -> logging_level_from_config
- `_load_and_cache_app_config` -> resolve_config_path, from_file, _get_config_mtime, _get_config_signature
- `get_app_config` -> resolve_config_path, _get_config_mtime, _get_config_signature, _load_and_cache_app_config
- `reload_app_config` -> _load_and_cache_app_config
- `AppConfig.resolve_config_path` -> _legacy_config_candidates
- `AppConfig.from_file` -> resolve_config_path, _check_config_version, resolve_env_variables, _apply_database_defaults, from_file, _validate_acp_agents, _apply_singleton_configs
- `AppConfig.resolve_env_variables` -> resolve_env_variables

# `backend/packages/harness/deerflow/config/agents_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/agents_config.py`  ·  行数: 382

**模块文档首行**（仅供参考）: Configuration and loaders for custom agents.

## 模块概览
- 函数 7 个，类 4 个，模块级常量 4 个

## 依赖（import）
- 模块: logging, re, yaml
- `pathlib` -> Path
- `typing` -> Any
- `pydantic` -> BaseModel, Field, field_validator, model_validator
- `deerflow.config.paths` -> get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `SOUL_FILENAME` = 'SOUL.md'
- `AGENT_NAME_PATTERN` = re.compile('^[A-Za-z0-9-]+$')
- `MANAGED_AGENT_CONFIG_FIELDS` = frozenset({'name', 'description', 'model', 'tool_groups',...

## 函数
#### `ƒ` `_blank_to_none(value: str | None) -> str | None`  L27
  - _文档首行_（仅供参考）: Normalize a whitespace-only string to ``None``; leave real values untouched.
  - 分支数 1，函数体节点数 37；return: None, stripped or None
  - 调用: strip

#### `ƒ` `validate_agent_name(name: str | None) -> str | None`  L148
  - _文档首行_（仅供参考）: Validate a custom agent name before using it in filesystem paths.
  - 分支数 3，函数体节点数 66；raise: ValueError('Invalid agent name. Expected a string or None.'), ValueError(f"Invalid agent name '{name}'. Must match pattern: {AGENT_NAME_PATTERN.pattern}")；return: None, name
  - 调用: isinstance, ValueError, fullmatch

#### `ƒ` `preserve_non_managed_fields(existing_cfg: AgentConfig) -> dict[str, object]`  L189
  - _文档首行_（仅供参考）: Return every top-level field on ``existing_cfg`` not in :data:`MANAGED_AGENT_CONFIG_FIELDS`.
  - 分支数 0，函数体节点数 28；return: existing_cfg.model_dump(exclude_unset=True, exclude=MANAGED_AGENT_CONFIG_FIELDS)
  - 调用: model_dump

#### `ƒ` `resolve_agent_dir(name: str, *, user_id: str | None) -> Path`  L208
  - _文档首行_（仅供参考）: Return the on-disk directory for an agent, preferring the per-user layout.
  - 分支数 2，函数体节点数 95；return: user_path, legacy_path
  - 调用: get_paths, get_effective_user_id, user_agent_dir, exists, agent_dir
  - 文件IO: exists (L228), exists (L228), exists (L232), exists (L232)

#### `ƒ` `load_agent_config(name: str | None, *, user_id: str | None) -> AgentConfig | None`  L238
  - _文档首行_（仅供参考）: Load the custom or default agent's config from its directory.
  - 分支数 6，函数体节点数 206；raise: FileNotFoundError(f'Agent directory not found: {agent_dir}'), FileNotFoundError(f'Agent config not found: {config_file}'), ValueError(f'Failed to parse agent config {config_file}: {e}')；return: None, AgentConfig(**data)
  - 调用: validate_agent_name, resolve_agent_dir, exists, FileNotFoundError, open, safe_load, ValueError, set, keys, items, AgentConfig
  - 文件IO: exists (L264), exists (L267), open (L271)

#### `ƒ` `load_agent_soul(agent_name: str | None, *, user_id: str | None) -> str | None`  L287
  - _文档首行_（仅供参考）: Read the SOUL.md file for a custom agent, if it exists.
  - 分支数 5，函数体节点数 168；return: None, content or None
  - 调用: resolve_agent_dir, exists, get_paths, get_effective_user_id, user_agent_dir, agent_dir, strip, read_text
  - 文件IO: exists (L316), exists (L316), exists (L323), exists (L329), read_text (L331)

#### `ƒ` `list_custom_agents(*, user_id: str | None) -> list[AgentConfig]`  L335
  - _文档首行_（仅供参考）: Scan the agents directory and return all valid custom agents.
  - 分支数 8，函数体节点数 228；return: agents
  - 调用: get_paths, get_effective_user_id, set, user_agents_dir, exists, sorted, iterdir, is_dir, debug, load_agent_config, append, add, warning, sort
  - 文件IO: exists (L359), iterdir (L361), exists (L367)

## 类
### 类 `GitHubTriggerConfig`  L46
- 继承: BaseModel
- _文档首行_: Per-event trigger filter inside a :class:`GitHubBinding`.
- 类/实例变量:
  - `actions` = None
  - `require_mention` = False
  - `allow_authors` = Field(default_factory=list)
  - `mention_login` = None
- 方法:
  #### `cls` `_normalize_mention_login(cls, value: str | None) -> str | None`    @field_validator(...), classmethod  L68
    - 分支数 0，函数体节点数 26；return: _blank_to_none(value)
    - 调用: _blank_to_none, field_validator

### 类 `GitHubBinding`  L72
- 继承: BaseModel
- _文档首行_: One (agent, repo) binding with per-event trigger overrides.
- 类/实例变量:
  - `repo` = <annotated>
  - `triggers` = Field(default_factory=dict)

### 类 `GitHubAgentConfig`  L82
- 继承: BaseModel
- _文档首行_: Top-level ``github:`` block on a custom agent's ``config.yaml``.
- 类/实例变量:
  - `installation_id` = None
  - `bot_login` = None
  - `recursion_limit` = None
  - `bindings` = Field(default_factory=list)
- 方法:
  #### `cls` `_normalize_bot_login(cls, value: str | None) -> str | None`    @field_validator(...), classmethod  L121
    - 分支数 0，函数体节点数 26；return: _blank_to_none(value)
    - 调用: _blank_to_none, field_validator
  #### `m` `_unique_binding_repos(self) -> 'GitHubAgentConfig'`    @model_validator(...)  L125
    - _文档首行_（仅供参考）: Reject duplicate ``repo`` values across ``bindings``.
    - 分支数 3，函数体节点数 90；raise: ValueError(f'Agent github.bindings has duplicate repos {sorted(dupes)}. Each repo must appear at most once — merge their `triggers:` maps into a single binding.')；return: self
    - 调用: set, add, ValueError, sorted, model_validator

### 类 `AgentConfig`  L159
- 继承: BaseModel
- _文档首行_: Configuration for a custom agent.
- 类/实例变量:
  - `name` = <annotated>
  - `description` = ''
  - `model` = None
  - `tool_groups` = None
  - `skills` = None
  - `github` = None

## 文件内调用关系
- `load_agent_config` -> validate_agent_name, resolve_agent_dir
- `load_agent_soul` -> resolve_agent_dir
- `list_custom_agents` -> load_agent_config
- `GitHubTriggerConfig._normalize_mention_login` -> _blank_to_none
- `GitHubAgentConfig._normalize_bot_login` -> _blank_to_none

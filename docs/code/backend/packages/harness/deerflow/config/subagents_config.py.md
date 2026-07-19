# `backend/packages/harness/deerflow/config/subagents_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/subagents_config.py`  ·  行数: 300

**模块文档首行**（仅供参考）: Configuration for the subagent system loaded from config.yaml.

## 模块概览
- 函数 5 个，类 3 个，模块级常量 7 个

## 依赖（import）
- 模块: logging
- `pydantic` -> BaseModel, Field
- `deerflow.config.token_budget_config` -> TokenBudgetConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_MAX_TOTAL_SUBAGENTS_PER_RUN` = 6
- `MIN_TOTAL_SUBAGENTS_PER_RUN` = 1
- `MAX_TOTAL_SUBAGENTS_PER_RUN` = 50
- `MIN_CONCURRENT_SUBAGENT_CALLS` = 2
- `MAX_CONCURRENT_SUBAGENT_CALLS` = 4
- `_subagents_config` = SubagentsAppConfig()

## 函数
#### `ƒ` `clamp_subagent_concurrency(value: int) -> int`  L18
  - _文档首行_（仅供参考）: Clamp per-response task call concurrency to the enforced middleware range.
  - 分支数 0，函数体节点数 22；return: max(MIN_CONCURRENT_SUBAGENT_CALLS, min(MAX_CONCURRENT_SUBAGENT_CALLS, value))
  - 调用: max, min

#### `ƒ` `clamp_total_subagents_per_run(value: int) -> int`  L23
  - _文档首行_（仅供参考）: Clamp per-run task delegation totals to the enforced middleware range.
  - 分支数 0，函数体节点数 22；return: max(MIN_TOTAL_SUBAGENTS_PER_RUN, min(MAX_TOTAL_SUBAGENTS_PER_RUN, value))
  - 调用: max, min

#### `ƒ` `default_subagent_token_budget(*, summarization_enabled: bool) -> TokenBudgetConfig`  L28
  - _文档首行_（仅供参考）: Default per-run token budget for subagents (#3875 Phase 2 → Phase 3 coupling).
  - 分支数 0，函数体节点数 29；return: TokenBudgetConfig(enabled=True, max_tokens=max_tokens, warn_threshold=0.7)
  - 调用: TokenBudgetConfig

#### `ƒ` `get_subagents_app_config() -> SubagentsAppConfig`  L254
  - _文档首行_（仅供参考）: Get the current subagents configuration.
  - 分支数 0，函数体节点数 9；return: _subagents_config

#### `ƒ` `load_subagents_config_from_dict(config_dict: dict) -> None`  L259
  - _文档首行_（仅供参考）: Load subagents configuration from a dictionary.
  - 分支数 8，函数体节点数 241
  - 调用: get, model_dump, default_subagent_token_budget, items, SubagentsAppConfig, append, join, list, keys, info

## 类
### 类 `SubagentOverrideConfig`  L58
- 继承: BaseModel
- _文档首行_: Per-agent configuration overrides.
- 类/实例变量:
  - `timeout_seconds` = Field(default=None, ge=1, description='Timeout in seconds...
  - `max_turns` = Field(default=None, ge=1, description='Maximum turns for ...
  - `model` = Field(default=None, min_length=1, description='Model name...
  - `skills` = Field(default=None, description='Skill names whitelist fo...
  - `token_budget` = Field(default=None, description='Per-run token budget ove...

### 类 `CustomSubagentConfig`  L86
- 继承: BaseModel
- _文档首行_: User-defined subagent type declared in config.yaml.
- 类/实例变量:
  - `description` = Field(description='When the lead agent should delegate to...
  - `system_prompt` = Field(description="System prompt that guides the subagent...
  - `tools` = Field(default=None, description='Tool names whitelist (No...
  - `disallowed_tools` = Field(default_factory=lambda: ['task', 'ask_clarification...
  - `skills` = Field(default=None, description='Skill names whitelist (N...
  - `model` = Field(default='inherit', description="Model to use - 'inh...
  - `max_turns` = Field(default=50, ge=1, description='Maximum number of ag...
  - `timeout_seconds` = Field(default=900, ge=1, description='Maximum execution t...

### 类 `SubagentsAppConfig`  L123
- 继承: BaseModel
- _文档首行_: Configuration for the subagent system.
- 类/实例变量:
  - `timeout_seconds` = Field(default=1800, ge=1, description='Default timeout in...
  - `max_turns` = Field(default=None, ge=1, description='Optional default m...
  - `max_total_per_run` = Field(default=DEFAULT_MAX_TOTAL_SUBAGENTS_PER_RUN, ge=MIN...
  - `token_budget` = Field(default_factory=default_subagent_token_budget, desc...
  - `agents` = Field(default_factory=dict, description='Per-agent config...
  - `custom_agents` = Field(default_factory=dict, description='User-defined sub...
  - `_token_budget_is_default` = True
- 方法:
  #### `m` `__init__(self, **data)`  L165
    - 分支数 0，函数体节点数 26；可变参数（*args/**kwargs）
    - 调用: __init__, super
  #### `m` `get_timeout_for(self, agent_name: str) -> int`  L169
    - _文档首行_（仅供参考）: Get the effective timeout for a specific agent.
    - 分支数 1，函数体节点数 47；return: override.timeout_seconds, self.timeout_seconds
    - 调用: get
  #### `m` `get_model_for(self, agent_name: str) -> str | None`  L183
    - _文档首行_（仅供参考）: Get the model override for a specific agent.
    - 分支数 1，函数体节点数 47；return: override.model, None
    - 调用: get
  #### `m` `get_max_turns_for(self, agent_name: str, builtin_default: int) -> int`  L197
    - _文档首行_（仅供参考）: Get the effective max_turns for a specific agent.
    - 分支数 2，函数体节点数 61；return: override.max_turns, self.max_turns, builtin_default
    - 调用: get
  #### `m` `get_skills_for(self, agent_name: str) -> list[str] | None`  L206
    - _文档首行_（仅供参考）: Get the skills override for a specific agent.
    - 分支数 1，函数体节点数 51；return: override.skills, None
    - 调用: get
  #### `m` `get_token_budget_for(self, agent_name: str, *, summarization_enabled: bool) -> TokenBudgetConfig`  L220
    - _文档首行_（仅供参考）: Get the effective token-budget config for a specific agent.
    - 分支数 2，函数体节点数 63；return: override.token_budget, default_subagent_token_budget(summarization_enabled=summarization_enabled), self.token_budget
    - 调用: get, default_subagent_token_budget

## 文件内调用关系
- `load_subagents_config_from_dict` -> default_subagent_token_budget
- `SubagentsAppConfig.__init__` -> __init__
- `SubagentsAppConfig.get_token_budget_for` -> default_subagent_token_budget

# `backend/packages/harness/deerflow/subagents/registry.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/subagents/registry.py`  ·  行数: 166

**模块文档首行**（仅供参考）: Subagent registry for managing available subagents.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `dataclasses` -> replace
- `typing` -> Any
- `deerflow.sandbox.security` -> is_host_bash_allowed
- `deerflow.subagents.builtins` -> BUILTIN_SUBAGENTS
- `deerflow.subagents.config` -> SubagentConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_resolve_subagents_app_config(app_config: Any | None)`  L14
  - 分支数 1，函数体节点数 30；return: get_subagents_app_config(), getattr(app_config, 'subagents', app_config)
  - 调用: get_subagents_app_config, getattr
  - 反射: getattr (L19)

#### `ƒ` `_build_custom_subagent_config(name: str, *, app_config: Any | None) -> SubagentConfig | None`  L22
  - _文档首行_（仅供参考）: Build a SubagentConfig from config.yaml custom_agents section.
  - 分支数 1，函数体节点数 94；return: None, SubagentConfig(name=name, description=custom.description, system_prompt=custom.system_prompt, tools=custom.tools, disallowed_tools=custom.disallowed_tools, skills=custom.skills, model=custom.model, max_turns=custom.max_turns, timeout_seconds=custom.timeout_seconds)
  - 调用: _resolve_subagents_app_config, get, SubagentConfig

#### `ƒ` `get_subagent_config(name: str, *, app_config: Any | None) -> SubagentConfig | None`  L50
  - _文档首行_（仅供参考）: Get a subagent configuration by name, with config.yaml overrides applied.
  - 分支数 11，函数体节点数 399；return: None, config
  - 调用: get, _build_custom_subagent_config, _resolve_subagents_app_config, debug, get_model_for, get_skills_for, replace
  - 文件IO: replace (L114)

#### `ƒ` `list_subagents(*, app_config: Any | None) -> list[SubagentConfig]`  L119
  - _文档首行_（仅供参考）: List all available subagent configurations (with config.yaml overrides applied).
  - 分支数 2，函数体节点数 59；return: configs
  - 调用: get_subagent_names, get_subagent_config, append

#### `ƒ` `get_subagent_names(*, app_config: Any | None) -> list[str]`  L133
  - _文档首行_（仅供参考）: Get all available subagent names (built-in + custom).
  - 分支数 2，函数体节点数 61；return: names
  - 调用: list, keys, _resolve_subagents_app_config, append

#### `ƒ` `get_available_subagent_names(*, app_config: Any | None) -> list[str]`  L150
  - _文档首行_（仅供参考）: Get subagent names that should be exposed to the active runtime.
  - 分支数 2，函数体节点数 82；return: names
  - 调用: get_subagent_names, hasattr, is_host_bash_allowed, debug
  - 反射: hasattr (L158)

## 文件内调用关系
- `_build_custom_subagent_config` -> _resolve_subagents_app_config
- `get_subagent_config` -> _build_custom_subagent_config, _resolve_subagents_app_config
- `list_subagents` -> get_subagent_names, get_subagent_config
- `get_subagent_names` -> _resolve_subagents_app_config
- `get_available_subagent_names` -> get_subagent_names

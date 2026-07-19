# `backend/packages/harness/deerflow/subagents/config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/subagents/config.py`  ·  行数: 62

**模块文档首行**（仅供参考）: Subagent configuration definitions.

## 模块概览
- 函数 2 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `dataclasses` -> dataclass, field
- `typing` -> TYPE_CHECKING

## 函数
#### `ƒ` `_default_model_name(app_config: 'AppConfig') -> str`  L43
  - 分支数 1，函数体节点数 28；raise: ValueError('No chat models are configured. Please configure at least one model in config.yaml.')；return: app_config.models[0].name
  - 调用: ValueError

#### `ƒ` `resolve_subagent_model_name(config: SubagentConfig, parent_model: str | None, *, app_config: 'AppConfig | None') -> str`  L49
  - _文档首行_（仅供参考）: Resolve the effective model name a subagent should use.
  - 分支数 3，函数体节点数 60；return: config.model, parent_model, _default_model_name(app_config)
  - 调用: get_app_config, _default_model_name

## 类
### 类 `SubagentConfig`  L11  @dataclass
- _文档首行_: Configuration for a subagent.
- 类/实例变量:
  - `name` = <annotated>
  - `description` = <annotated>
  - `system_prompt` = None
  - `tools` = None
  - `disallowed_tools` = field(default_factory=lambda: ['task'])
  - `skills` = None
  - `model` = 'inherit'
  - `max_turns` = 50
  - `timeout_seconds` = 900

## 文件内调用关系
- `resolve_subagent_model_name` -> _default_model_name

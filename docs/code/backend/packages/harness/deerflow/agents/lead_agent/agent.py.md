# `backend/packages/harness/deerflow/agents/lead_agent/agent.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/lead_agent/agent.py`  ·  行数: 663

**模块文档首行**（仅供参考）: Lead agent factory.

## 模块概览
- 函数 11 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: logging, secrets
- `__future__` -> annotations
- `langchain.agents` -> create_agent
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.runnables` -> RunnableConfig
- `deerflow.agents.lead_agent.prompt` -> apply_prompt_template
- `deerflow.agents.middlewares.clarification_middleware` -> ClarificationMiddleware
- `deerflow.agents.middlewares.loop_detection_middleware` -> LoopDetectionMiddleware
- `deerflow.agents.middlewares.memory_middleware` -> MemoryMiddleware
- `deerflow.agents.middlewares.safety_finish_reason_middleware` -> SafetyFinishReasonMiddleware
- `deerflow.agents.middlewares.subagent_limit_middleware` -> SubagentLimitMiddleware
- `deerflow.agents.middlewares.summarization_middleware` -> DeerFlowSummarizationMiddleware, create_summarization_middleware
- `deerflow.agents.middlewares.terminal_response_middleware` -> TerminalResponseMiddleware
- `deerflow.agents.middlewares.title_middleware` -> TitleMiddleware
- `deerflow.agents.middlewares.todo_middleware` -> TodoMiddleware
- `deerflow.agents.middlewares.token_usage_middleware` -> TokenUsageMiddleware
- `deerflow.agents.middlewares.tool_error_handling_middleware` -> build_lead_runtime_middlewares
- `deerflow.agents.middlewares.view_image_middleware` -> ViewImageMiddleware
- `deerflow.agents.thread_state` -> ThreadState
- `deerflow.config.agents_config` -> load_agent_config, validate_agent_name
- `deerflow.config.app_config` -> AppConfig, get_app_config
- `deerflow.config.memory_config` -> should_use_memory_tools
- `deerflow.config.subagents_config` -> DEFAULT_MAX_TOTAL_SUBAGENTS_PER_RUN
- `deerflow.models` -> create_chat_model
- `deerflow.skills.types` -> Skill
- `deerflow.tracing` -> build_tracing_callbacks

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_BOOTSTRAP_SKILL_NAMES` = {'bootstrap'}
- `_NON_INTERACTIVE_DISABLED_TOOL_NAMES` = frozenset({'ask_clarification'})
- `_WEBHOOK_CHANNELS` = frozenset({'github'})

## 函数
#### `ƒ` `_default_max_total_subagents(app_config: object) -> int`  L66
  - 分支数 0，函数体节点数 26；return: getattr(subagents_config, 'max_total_per_run', DEFAULT_MAX_TOTAL_SUBAGENTS_PER_RUN)
  - 调用: getattr
  - 反射: getattr (L67), getattr (L68)

#### `ƒ` `_append_memory_tools_without_name_conflicts(tools: list) -> None`  L71
  - _文档首行_（仅供参考）: Append memory tools without dropping unrelated duplicate-named tools.
  - 分支数 2，函数体节点数 71
  - 调用: getattr, get_memory_tools, warning, append, add
  - 反射: getattr (L75)

#### `ƒ` `_get_runtime_config(config: RunnableConfig) -> dict`  L84
  - _文档首行_（仅供参考）: Merge legacy configurable options with LangGraph runtime context.
  - 分支数 1，函数体节点数 57；return: cfg
  - 调用: dict, get, isinstance, update

#### `ƒ` `_resolve_model_name(requested_model_name: str | None, *, app_config: AppConfig | None) -> str`  L93
  - _文档首行_（仅供参考）: Resolve a runtime model name safely, falling back to default if invalid. Returns None if no models are configured.
  - 分支数 3，函数体节点数 104；raise: ValueError('No chat models are configured. Please configure at least one model in config.yaml.')；return: requested_model_name, default_model_name
  - 调用: get_app_config, ValueError, get_model_config, warning

#### `ƒ` `_create_summarization_middleware(*, app_config: AppConfig | None) -> DeerFlowSummarizationMiddleware | None`  L108
  - _文档首行_（仅供参考）: Create and configure the summarization middleware from config.
  - 分支数 0，函数体节点数 23；return: create_summarization_middleware(app_config=app_config)
  - 调用: create_summarization_middleware

#### `ƒ` `_create_todo_list_middleware(is_plan_mode: bool) -> TodoMiddleware | None`  L113
  - _文档首行_（仅供参考）: Create and configure the TodoList middleware.
  - 分支数 1，函数体节点数 37；return: None, TodoMiddleware(system_prompt=system_prompt, tool_description=tool_description)
  - 调用: TodoMiddleware

#### `ƒ` `build_middlewares(config: RunnableConfig, model_name: str | None, agent_name: str | None, custom_middlewares: list[AgentMiddleware] | None, *, available_skills: set[str] | None, app_config: AppConfig | None, deferred_setup, mcp_routing_middleware: AgentMiddleware | None, user_id: str | None)`  L238
  - _文档首行_（仅供参考）: Build the lead-agent middleware chain based on runtime configuration.
  - 分支数 13，函数体节点数 587；return: middlewares
  - 调用: get_app_config, build_lead_runtime_middlewares, append, DynamicContextMiddleware, token_urlsafe, SkillActivationMiddleware, SkillToolPolicyMiddleware, DurableContextMiddleware, _create_summarization_middleware, _get_runtime_config, get, _create_todo_list_middleware, TokenUsageMiddleware, TitleMiddleware, should_use_memory_tools, warning, MemoryMiddleware, get_model_config, ViewImageMiddleware, DeferredToolFilterMiddleware（+8）

#### `ƒ` `_available_skill_names(agent_config, is_bootstrap: bool) -> set[str] | None`  L421
  - 分支数 2，函数体节点数 46；return: set(_BOOTSTRAP_SKILL_NAMES), set(agent_config.skills), None
  - 调用: set

#### `ƒ` `_load_enabled_available_skills(available_skills: set[str] | None, *, app_config: AppConfig, user_id: str | None) -> list[Skill]`  L429
  - 分支数 2，函数体节点数 79；raise: bare raise；return: skills, [skill for skill in skills if skill.name in available_skills]
  - 调用: get_enabled_skills_for_config, exception

#### `ƒ` `make_lead_agent(config: RunnableConfig)`  L443
  - _文档首行_（仅供参考）: LangGraph graph factory; keep the signature compatible with LangGraph Server.
  - 分支数 0，函数体节点数 38；return: _make_lead_agent(config, app_config=runtime_app_config or get_app_config())
  - 调用: _get_runtime_config, get, _make_lead_agent, get_app_config

#### `ƒ` `_make_lead_agent(config: RunnableConfig, *, app_config: AppConfig)`  L450
  - 分支数 12，函数体节点数 983；raise: ValueError("No chat model could be resolved. Please configure at least one model in config.yaml or provide a valid 'model_name'/'model' in the request.")；return: create_agent(model=create_chat_model(name=model_name, thinking_enabled=thinking_enabled, app_config=resolved_app_config, attach_tracing=False), tools=final_tools, middleware=build_middlewares(config, model_name=model_name, available_skills=set(_BOOTSTRAP_SKILL_NAMES), app_config=resolved_app_config, deferred_setup=setup, mcp_routing_middleware=mcp_routing_middleware, user_id=resolved_user_id), system_prompt=apply_prompt_template(subagent_enabled=subagent_enabled, max_concurrent_subagents=max_concurrent_subagents, max_total_subagents=max_total_subagents, available_skills=set(_BOOTSTRAP_SKILL_NAMES), app_config=resolved_app_config, deferred_names=setup.deferred_names, user_id=resolved_user_id, skill_names=skill_setup.skill_names or None), state_schema=ThreadState), create_agent(model=create_chat_model(name=model_name, thinking_enabled=thinking_enabled, reasoning_effort=reasoning_effort, app_config=resolved_app_config, attach_tracing=False), tools=final_tools, middleware=build_middlewares(config, model_name=model_name, agent_name=agent_name, available_skills=available_skills, app_config=resolved_app_config, deferred_setup=setup, mcp_routing_middleware=mcp_routing_middleware, user_id=resolved_user_id), system_prompt=apply_prompt_template(subagent_enabled=subagent_enabled, max_concurrent_subagents=max_concurrent_subagents, max_total_subagents=max_total_subagents, agent_name=agent_name, available_skills=available_skills, app_config=resolved_app_config, deferred_names=setup.deferred_names, mcp_routing_hints_section=mcp_routing_hints_section, user_id=resolved_user_id, skill_names=skill_setup.skill_names or None), state_schema=ThreadState)
  - 调用: _get_runtime_config, get, str, get_effective_user_id, _default_max_total_subagents, bool, validate_agent_name, load_agent_config, _available_skill_names, _resolve_model_name, get_model_config, ValueError, warning, info, update, sorted, build_tracing_callbacks, isinstance, list, _load_enabled_available_skills（+13）

## 文件内调用关系
- `build_middlewares` -> _create_summarization_middleware, _get_runtime_config, _create_todo_list_middleware, _default_max_total_subagents
- `make_lead_agent` -> _get_runtime_config, _make_lead_agent
- `_make_lead_agent` -> _get_runtime_config, _default_max_total_subagents, _available_skill_names, _resolve_model_name, _load_enabled_available_skills, _append_memory_tools_without_name_conflicts, build_middlewares

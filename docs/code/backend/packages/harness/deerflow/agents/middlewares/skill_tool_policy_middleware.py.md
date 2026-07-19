# `backend/packages/harness/deerflow/agents/middlewares/skill_tool_policy_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/skill_tool_policy_middleware.py`  ·  行数: 365

**模块文档首行**（仅供参考）: Apply skill ``allowed-tools`` only to skills active in lead-agent context.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 8 个

## 依赖（import）
- 模块: asyncio, json, logging, posixpath, secrets
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable, Mapping
- `typing` -> TYPE_CHECKING, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> ToolMessage
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command
- `deerflow.runtime.secret_context` -> SKILL_TOOL_POLICY_DECISION_CONTEXT_KEY, read_slash_skill_source_path
- `deerflow.skills.storage` -> get_or_new_skill_storage, get_or_new_user_skill_storage
- `deerflow.skills.tool_policy` -> ALWAYS_AVAILABLE_BUILTIN_TOOL_NAMES, allowed_tool_names_for_skills
- `deerflow.skills.types` -> Skill

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_POLICY_DECISION_VERSION` = 2
- `_POLICY_SOURCE_PASSIVE` = 'passive'
- `_POLICY_SOURCE_SLASH` = 'slash'
- `_POLICY_SOURCE_SKILL_CONTEXT` = 'skill_context'
- `_POLICY_SOURCES` = frozenset({_POLICY_SOURCE_PASSIVE, _POLICY_SOURCE_SLASH, ...
- `_MISSING_POLICY_DECISION` = object()
- `_TOOL_SEARCH_NAME` = 'tool_search'

## 类
### 类 `SkillToolPolicyMiddleware`  L42
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Restrict lead tools to declarations from slash/in-context skills.
- 方法:
  #### `st` `_runtime_context(request: ModelRequest | ToolCallRequest) -> dict | None`    @staticmethod  L150
    - 分支数 0，函数体节点数 43；return: context if isinstance(context, dict) else None
    - 调用: getattr, isinstance
  - 反射: getattr (L151), getattr (L151)
  #### `st` `_tool_search_policy_error(request: ToolCallRequest) -> ToolMessage`    @staticmethod  L240
    - 分支数 0，函数体节点数 35；return: ToolMessage(content='Error: tool_search returned a result that could not be validated against the active skill policy.', tool_call_id=str(request.tool_call.get('id') or 'missing_tool_call_id'), name=_TOOL_SEARCH_NAME, status='error')
    - 调用: ToolMessage, str, get
  #### `m` `__init__(self, *, available_skills: set[str] | None, app_config: AppConfig | None, user_id: str | None, slash_source_owner_token: str) -> None`  L52
    - 分支数 1，函数体节点数 109；raise: ValueError('slash_source_owner_token must be a non-empty string')
    - 调用: __init__, super, isinstance, ValueError, set, token_urlsafe
  #### `m` `_storage(self) -> SkillStorage`  L69
    - 分支数 2，函数体节点数 47；return: get_or_new_user_skill_storage(self._user_id, app_config=self._app_config), get_or_new_skill_storage(app_config=self._app_config), get_or_new_skill_storage()
    - 调用: get_or_new_user_skill_storage, get_or_new_skill_storage
  #### `m` `_active_policy(self, request: ModelRequest | ToolCallRequest) -> _PolicySignature`  L76
    - 分支数 8，函数体节点数 236；return: (_POLICY_SOURCE_SLASH, (slash_path,)), (_POLICY_SOURCE_SKILL_CONTEXT, tuple(paths)), (_POLICY_SOURCE_PASSIVE, ())
    - 调用: getattr, read_slash_skill_source_path, isinstance, get, hasattr, warning, type, append, tuple
  - 反射: getattr (L77), getattr (L77), getattr (L83), hasattr (L88), getattr (L89)
  #### `m` `_active_skills_for_paths(self, paths: tuple[str, ...]) -> tuple[list[Skill], bool]`  L103
    - 分支数 8，函数体节点数 262；return: ([], False), ([], True), (active, False)
    - 调用: _storage, load_skills, get_container_root, exception, normpath, get_container_file_path, set, get, warning, add, append
  #### `m` `_allowed_names_for_paths(self, paths: tuple[str, ...]) -> set[str] | None`  L140
    - 分支数 2，函数体节点数 71；return: set(ALWAYS_AVAILABLE_BUILTIN_TOOL_NAMES), None, allowed | set(ALWAYS_AVAILABLE_BUILTIN_TOOL_NAMES)
    - 调用: _active_skills_for_paths, set, allowed_tool_names_for_skills
  #### `m` `_store_policy_decision(self, request: ModelRequest, policy: _PolicySignature, allowed: set[str] | None) -> None`  L154
    - 分支数 1，函数体节点数 83
    - 调用: _runtime_context, list, sorted
  #### `m` `_read_policy_decision(self, context: dict | None, policy: _PolicySignature) -> set[str] | None | object`  L166
    - 分支数 8，函数体节点数 267；return: _MISSING_POLICY_DECISION, None, set(allowed)
    - 调用: get, isinstance, type, all, tuple, set
  #### `m` `_allowed_names(self, request: ModelRequest | ToolCallRequest, *, policy: _PolicySignature | None) -> set[str] | None`  L190
    - 分支数 1，函数体节点数 93；return: decision, self._allowed_names_for_paths(paths)
    - 调用: _active_policy, _runtime_context, _read_policy_decision, _allowed_names_for_paths
  #### `m` `_filter_model_request(self, request: ModelRequest, *, policy: _PolicySignature | None, refresh_decision: bool) -> ModelRequest`  L204
    - 分支数 3，函数体节点数 162；return: request, request.override(tools=tools)
    - 调用: _active_policy, _allowed_names_for_paths, _allowed_names, _store_policy_decision, getattr, len, debug, override
  - 反射: getattr (L218)
  #### `m` `_blocked_tool_message(self, request: ToolCallRequest, *, allowed: set[str] | None) -> ToolMessage | None`  L223
    - 分支数 1，函数体节点数 89；return: None, ToolMessage(content=f"Error: Tool '{name}' is not allowed by the active skill policy.", tool_call_id=str(request.tool_call.get('id') or 'missing_tool_call_id'), name=name, status='error')
    - 调用: str, get, ToolMessage
  #### `m` `_filter_tool_search_result(self, request: ToolCallRequest, result: ToolMessage | Command, *, allowed: set[str] | None) -> ToolMessage | Command`  L248
    - _文档首行_（仅供参考）: Remove denied schemas and promotions from tool_search output.
    - 分支数 9，函数体节点数 499；return: result, self._tool_search_policy_error(request), Command(graph=result.graph, update=sanitized_update, resume=result.resume, goto=result.goto)
    - 调用: str, get, isinstance, warning, _tool_search_policy_error, len, all, loads, dumps, append, model_copy, dict, Command
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L309
    - 分支数 0，函数体节点数 49；return: handler(self._filter_model_request(request, policy=policy, refresh_decision=True))
    - 调用: _active_policy, handler, _filter_model_request
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L337
    - 分支数 2，函数体节点数 106；return: handler(request), blocked, self._filter_tool_search_result(request, handler(request), allowed=allowed)
    - 调用: _active_policy, handler, _allowed_names, _blocked_tool_message, _filter_tool_search_result
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L318
    - 分支数 1，函数体节点数 96；return: await handler(request), await handler(filtered)
    - 调用: _active_policy, _store_policy_decision, handler, to_thread
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L352
    - 分支数 2，函数体节点数 117；return: await handler(request), blocked, self._filter_tool_search_result(request, await handler(request), allowed=allowed)
    - 调用: _active_policy, handler, to_thread, _blocked_tool_message, _filter_tool_search_result

## 文件内调用关系
- `SkillToolPolicyMiddleware.__init__` -> __init__
- `SkillToolPolicyMiddleware._active_skills_for_paths` -> _storage
- `SkillToolPolicyMiddleware._allowed_names_for_paths` -> _active_skills_for_paths
- `SkillToolPolicyMiddleware._store_policy_decision` -> _runtime_context
- `SkillToolPolicyMiddleware._allowed_names` -> _active_policy, _runtime_context, _read_policy_decision, _allowed_names_for_paths
- `SkillToolPolicyMiddleware._filter_model_request` -> _active_policy, _allowed_names_for_paths, _allowed_names, _store_policy_decision
- `SkillToolPolicyMiddleware._filter_tool_search_result` -> _tool_search_policy_error
- `SkillToolPolicyMiddleware.wrap_model_call` -> _active_policy, _filter_model_request
- `SkillToolPolicyMiddleware.awrap_model_call` -> _active_policy, _store_policy_decision
- `SkillToolPolicyMiddleware.wrap_tool_call` -> _active_policy, _allowed_names, _blocked_tool_message, _filter_tool_search_result
- `SkillToolPolicyMiddleware.awrap_tool_call` -> _active_policy, _blocked_tool_message, _filter_tool_search_result

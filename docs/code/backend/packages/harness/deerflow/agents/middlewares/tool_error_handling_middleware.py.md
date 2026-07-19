# `backend/packages/harness/deerflow/agents/middlewares/tool_error_handling_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/tool_error_handling_middleware.py`  ·  行数: 456

**模块文档首行**（仅供参考）: Tool error handling middleware and shared runtime middleware builders.

## 模块概览
- 函数 4 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: logging
- `collections.abc` -> Awaitable, Callable
- `typing` -> TYPE_CHECKING, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> ToolMessage
- `langgraph.errors` -> GraphBubbleUp
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command
- `deerflow.agents.middlewares.skill_context` -> SKILL_CONTEXT_ENTRY_KEY, _tool_call_path, build_skill_entry_metadata_from_read
- `deerflow.agents.middlewares.tool_result_meta` -> normalize_tool_result, stamp_exception_meta
- `deerflow.config.app_config` -> AppConfig
- `deerflow.config.summarization_config` -> DEFAULT_SKILL_FILE_READ_TOOL_NAMES
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.subagents.status_contract` -> format_subagent_result_message, make_subagent_additional_kwargs

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_MISSING_TOOL_CALL_ID` = 'missing_tool_call_id'
- `_TASK_TOOL_NAME` = 'task'
- `_RECOVERY_HINT` = 'Continue with available context, or choose an alternativ...

## 函数
#### `ƒ` `_stamp_task_exception_status(message: ToolMessage, *, tool_name: str, error: str) -> ToolMessage`  L41
  - _文档首行_（仅供参考）: Stamp failed metadata on task exception wrappers produced here.
  - 分支数 2，函数体节点数 106；return: message
  - 调用: format_subagent_result_message, endswith, dict, update, make_subagent_additional_kwargs

#### `ƒ` `_build_runtime_middlewares(*, app_config: AppConfig, include_uploads: bool, include_dangling_tool_call_patch: bool, lazy_init: bool) -> list[AgentMiddleware]`  L154
  - _文档首行_（仅供参考）: Build shared base middlewares for agent execution.
  - 分支数 10，函数体节点数 484；raise: RuntimeError(f'ToolProgressMiddleware must be outer (index {_progress_idx}) of ToolErrorHandlingMiddleware (index {_error_idx}) — check middleware append order')；return: middlewares
  - 调用: InputSanitizationMiddleware, from_app_config, ToolResultSanitizationMiddleware, ThreadDataMiddleware, append, UploadsMiddleware, SandboxMiddleware, DanglingToolCallMiddleware, LLMErrorHandlingMiddleware, resolve_variable, dict, signature, any, values, provider_cls, GuardrailMiddleware, SandboxAuditMiddleware, ReadBeforeWriteMiddleware, from_config, ToolErrorHandlingMiddleware（+4）

#### `ƒ` `build_lead_runtime_middlewares(*, app_config: AppConfig, lazy_init: bool) -> list[AgentMiddleware]`  L267
  - _文档首行_（仅供参考）: Middlewares shared by lead agent runtime before lead-only middlewares.
  - 分支数 0，函数体节点数 31；return: _build_runtime_middlewares(app_config=app_config, include_uploads=True, include_dangling_tool_call_patch=True, lazy_init=lazy_init)
  - 调用: _build_runtime_middlewares

#### `ƒ` `build_subagent_runtime_middlewares(*, app_config: AppConfig | None, model_name: str | None, lazy_init: bool, deferred_setup: 'DeferredToolSetup | None', mcp_routing_middleware: AgentMiddleware | None, agent_name: str | None) -> list[AgentMiddleware]`  L277
  - _文档首行_（仅供参考）: Middlewares shared by subagent runtime before subagent-only middlewares.
  - 分支数 10，函数体节点数 368；return: middlewares
  - 调用: get_app_config, _build_runtime_middlewares, get_model_config, append, ViewImageMiddleware, DeferredToolFilterMiddleware, assert_mcp_routing_before_deferred_filter, from_config, get_token_budget_for, DurableContextMiddleware, create_summarization_middleware, SystemMessageCoalescingMiddleware

## 类
### 类 `ToolErrorHandlingMiddleware`  L55
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Convert tool exceptions into error ToolMessages so the run can continue.
- 方法:
  #### `m` `__init__(self, *, app_config: AppConfig | None) -> None`  L58
    - 分支数 1，函数体节点数 73
    - 调用: __init__, super, frozenset
  #### `m` `_build_error_message(self, request: ToolCallRequest, exc: Exception) -> ToolMessage`  L68
    - 分支数 1，函数体节点数 164；return: stamp_exception_meta(message, structured_error)
    - 调用: str, get, strip, len, ToolMessage, _stamp_task_exception_status, stamp_exception_meta
  #### `m` `_stamp_skill_read_metadata(self, message: ToolMessage, request: ToolCallRequest, *, tool_name: str) -> ToolMessage`  L89
    - 分支数 5，函数体节点数 145；return: message
    - 调用: getattr, isinstance, _tool_call_path, build_skill_entry_metadata_from_read, dict
  - 反射: getattr (L98)
  #### `m` `_maybe_stamp(self, result: ToolMessage | Command, request: ToolCallRequest) -> ToolMessage | Command`  L114
    - _文档首行_（仅供参考）: Apply producer-bound metadata for tool results that need it.
    - 分支数 1，函数体节点数 64；return: result, self._stamp_skill_read_metadata(result, request, tool_name=tool_name)
    - 调用: isinstance, str, get, _stamp_skill_read_metadata
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L122
    - 分支数 1，函数体节点数 93；raise: bare raise；return: self._build_error_message(request, exc), normalize_tool_result(self._maybe_stamp(result, request))
    - 调用: handler, exception, get, _build_error_message, normalize_tool_result, _maybe_stamp
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L138
    - 分支数 1，函数体节点数 98；raise: bare raise；return: self._build_error_message(request, exc), normalize_tool_result(self._maybe_stamp(result, request))
    - 调用: handler, exception, get, _build_error_message, normalize_tool_result, _maybe_stamp

## 文件内调用关系
- `build_lead_runtime_middlewares` -> _build_runtime_middlewares
- `build_subagent_runtime_middlewares` -> _build_runtime_middlewares
- `ToolErrorHandlingMiddleware.__init__` -> __init__
- `ToolErrorHandlingMiddleware._build_error_message` -> _stamp_task_exception_status
- `ToolErrorHandlingMiddleware._maybe_stamp` -> _stamp_skill_read_metadata
- `ToolErrorHandlingMiddleware.wrap_tool_call` -> _build_error_message, _maybe_stamp
- `ToolErrorHandlingMiddleware.awrap_tool_call` -> _build_error_message, _maybe_stamp

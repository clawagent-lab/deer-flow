# `backend/packages/harness/deerflow/tools/builtins/task_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/task_tool.py`  ·  行数: 627

**模块文档首行**（仅供参考）: Task tool for delegating work to subagents.

## 模块概览
- 函数 15 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, logging, uuid
- `dataclasses` -> replace
- `typing` -> TYPE_CHECKING, Annotated, Any, cast
- `langchain.tools` -> InjectedToolCallId, tool
- `langchain_core.callbacks` -> BaseCallbackManager
- `langchain_core.messages` -> ToolMessage
- `langgraph.config` -> get_stream_writer
- `langgraph.types` -> Command
- `deerflow.authz.principal` -> normalize_authz_attributes
- `deerflow.config` -> get_app_config
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.sandbox.security` -> LOCAL_BASH_SUBAGENT_DISABLED_MESSAGE, is_host_bash_allowed
- `deerflow.subagents` -> SubagentExecutor, get_available_subagent_names, get_subagent_config
- `deerflow.subagents.config` -> resolve_subagent_model_name
- `deerflow.subagents.executor` -> SubagentStatus, cleanup_background_task, get_background_task_result, request_cancel_background_task
- `deerflow.subagents.status_contract` -> SubagentStatusValue, SubagentStopReasonValue, format_subagent_result_message, make_subagent_additional_kwargs
- `deerflow.tools.types` -> Runtime
- `deerflow.trace_context` -> DEERFLOW_TRACE_METADATA_KEY, get_current_trace_id, normalize_trace_id

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_subagent_usage_cache` = {}

## 函数
#### `ƒ` `_token_usage_cache_enabled(app_config: 'AppConfig | None') -> bool`  L46
  - 分支数 2，函数体节点数 40；return: False, bool(getattr(getattr(app_config, 'token_usage', None), 'enabled', False))
  - 调用: get_app_config, bool, getattr
  - 反射: getattr (L52), getattr (L52)

#### `ƒ` `_cache_subagent_usage(tool_call_id: str, usage: dict | None, *, enabled: bool) -> None`  L55
  - 分支数 1，函数体节点数 32

#### `ƒ` `pop_cached_subagent_usage(tool_call_id: str) -> dict | None`  L60
  - 分支数 0，函数体节点数 19；return: _subagent_usage_cache.pop(tool_call_id, None)
  - 调用: pop

#### `ƒ` `_is_subagent_terminal(result: Any) -> bool`  L64
  - _文档首行_（仅供参考）: Return whether a background subagent result is safe to clean up.
  - 分支数 0，函数体节点数 45；return: result.status in {SubagentStatus.COMPLETED, SubagentStatus.FAILED, SubagentStatus.CANCELLED, SubagentStatus.TIMED_OUT} or getattr(result, 'completed_at', None) is not None
  - 调用: getattr
  - 反射: getattr (L66)

#### `⏵ƒ` `async _await_subagent_terminal(task_id: str, max_polls: int) -> Any | None`  L69
  - _文档首行_（仅供参考）: Poll until the background subagent reaches a terminal status or we run out of polls.
  - 分支数 3，函数体节点数 58；return: None, result
  - 调用: range, get_background_task_result, _is_subagent_terminal, sleep

#### `⏵ƒ` `async _deferred_cleanup_subagent_task(task_id: str, trace_id: str, max_polls: int) -> None`  L81
  - _文档首行_（仅供参考）: Keep polling a cancelled subagent until it can be safely removed.
  - 分支数 4，函数体节点数 89；return: None
  - 调用: get_background_task_result, _is_subagent_terminal, cleanup_background_task, warning, sleep

#### `ƒ` `_log_cleanup_failure(cleanup_task: asyncio.Task[None], *, trace_id: str, task_id: str) -> None`  L98
  - 分支数 2，函数体节点数 57；return: None
  - 调用: cancelled, exception, error

#### `ƒ` `_schedule_deferred_subagent_cleanup(task_id: str, trace_id: str, max_polls: int) -> None`  L107
  - 分支数 0，函数体节点数 64
  - 调用: debug, create_task, _deferred_cleanup_subagent_task, add_done_callback, _log_cleanup_failure

#### `ƒ` `_find_usage_recorder(runtime: Any) -> Any | None`  L113
  - _文档首行_（仅供参考）: Find a callback handler with ``record_external_llm_usage_records`` in the runtime config.
  - 分支数 7，函数体节点数 102；return: None, cb
  - 调用: getattr, isinstance, get, hasattr
  - 反射: getattr (L129), hasattr (L140)

#### `ƒ` `_summarize_usage(records: list[dict] | None) -> dict | None`  L145
  - _文档首行_（仅供参考）: Summarize token usage records into a compact dict for SSE events.
  - 分支数 1，函数体节点数 88；return: None, {'input_tokens': sum((r.get('input_tokens', 0) or 0 for r in records)), 'output_tokens': sum((r.get('output_tokens', 0) or 0 for r in records)), 'total_tokens': sum((r.get('total_tokens', 0) or 0 for r in records))}
  - 调用: sum, get

#### `ƒ` `_report_subagent_usage(runtime: Any, result: Any) -> None`  L156
  - _文档首行_（仅供参考）: Report subagent token usage to the parent RunJournal, if available.
  - 分支数 4，函数体节点数 89；return: None
  - 调用: getattr, _find_usage_recorder, debug, record_external_llm_usage_records, warning
  - 反射: getattr (L161), getattr (L163)

#### `ƒ` `_get_runtime_app_config(runtime: Any) -> 'AppConfig | None'`  L177
  - 分支数 2，函数体节点数 48；return: cast('AppConfig', app_config), None
  - 调用: getattr, isinstance, get, cast
  - 反射: getattr (L178)

#### `ƒ` `_merge_skill_allowlists(parent: list[str] | None, child: list[str] | None) -> list[str] | None`  L186
  - _文档首行_（仅供参考）: Return the effective subagent skill allowlist under the parent policy.
  - 分支数 2，函数体节点数 77；return: child, list(parent), [skill for skill in child if skill in parent_set]
  - 调用: list, set

#### `ƒ` `_task_result_command(*, tool_call_id: str, status: SubagentStatusValue, result: str | None, error: str | None, stop_reason: SubagentStopReasonValue | None, model_name: str | None, usage: dict[str, int] | None) -> Command`  L197
  - 分支数 0，函数体节点数 115；return: Command(update={'messages': [ToolMessage(content=content, tool_call_id=tool_call_id, name='task', additional_kwargs=make_subagent_additional_kwargs(status, result=result, error=metadata_error, stop_reason=stop_reason, model_name=model_name, token_usage=usage))]})
  - 调用: format_subagent_result_message, Command, ToolMessage, make_subagent_additional_kwargs

#### `⏵ƒ` `async task_tool(runtime: Runtime, description: str, prompt: str, subagent_type: str, tool_call_id: Annotated[str, InjectedToolCallId]) -> str | Command`    @tool(...)  L230
  - _文档首行_（仅供参考）: Delegate a task to a specialized subagent that runs in its own context.
  - 分支数 24，函数体节点数 1653；raise: bare raise；return: _task_result_command(tool_call_id=tool_call_id, status='failed', error=error), _task_result_command(tool_call_id=tool_call_id, status='failed', error=LOCAL_BASH_SUBAGENT_DISABLED_MESSAGE), _task_result_command(tool_call_id=tool_call_id, status='completed', result=result.result, stop_reason=result.stop_reason, model_name=effective_model, usage=usage), _task_result_command(tool_call_id=tool_call_id, status='failed', error=result.error, stop_reason=result.stop_reason, model_name=effective_model, usage=usage), _task_result_command(tool_call_id=tool_call_id, status='cancelled', error=result.error, model_name=effective_model, usage=usage), _task_result_command(tool_call_id=tool_call_id, status='timed_out', error=result.error, model_name=effective_model, usage=usage), _task_result_command(tool_call_id=tool_call_id, status='polling_timed_out', error=message, model_name=effective_model, usage=usage)
  - 调用: _get_runtime_app_config, _token_usage_cache_enabled, get_available_subagent_names, get_subagent_config, join, _task_result_command, is_host_bash_allowed, get, str, uuid4, resolve_runtime_user_id, isinstance, normalize_authz_attributes, normalize_trace_id, get_current_trace_id, _merge_skill_allowlists, list, replace, get_app_config, resolve_subagent_model_name（+24）
  - 文件IO: replace (L357)
  - 反射: getattr (L450), getattr (L578)

## 文件内调用关系
- `_await_subagent_terminal` -> _is_subagent_terminal
- `_deferred_cleanup_subagent_task` -> _is_subagent_terminal
- `_schedule_deferred_subagent_cleanup` -> _deferred_cleanup_subagent_task, _log_cleanup_failure
- `_report_subagent_usage` -> _find_usage_recorder
- `task_tool` -> _get_runtime_app_config, _token_usage_cache_enabled, _task_result_command, _merge_skill_allowlists, _summarize_usage, _cache_subagent_usage, _report_subagent_usage, _schedule_deferred_subagent_cleanup, _await_subagent_terminal, _is_subagent_terminal

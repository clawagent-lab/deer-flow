# `backend/packages/harness/deerflow/subagents/executor.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/subagents/executor.py`  ·  行数: 1163

**模块文档首行**（仅供参考）: Subagent execution engine.

## 模块概览
- 函数 11 个，类 3 个，模块级常量 10 个

## 依赖（import）
- 模块: asyncio, atexit, html, logging, os, threading, uuid
- `collections.abc` -> Callable, Coroutine, Mapping
- `concurrent.futures` -> Future, ThreadPoolExecutor
- `concurrent.futures` -> FuturesTimeoutError
- `contextvars` -> Context, copy_context
- `dataclasses` -> dataclass, field
- `datetime` -> datetime
- `enum` -> Enum
- `typing` -> TYPE_CHECKING, Any
- `langchain.agents` -> create_agent
- `langchain.tools` -> BaseTool
- `langchain_core.messages` -> AIMessage, HumanMessage, SystemMessage
- `langchain_core.runnables` -> RunnableConfig
- `langgraph.errors` -> GraphRecursionError
- `deerflow.agents.thread_state` -> SandboxState, ThreadDataState, ThreadState
- `deerflow.authz.principal` -> normalize_authz_attributes
- `deerflow.config` -> get_app_config
- `deerflow.config.app_config` -> AppConfig
- `deerflow.models` -> create_chat_model
- `deerflow.skills.tool_policy` -> filter_tools_by_skill_allowed_tools
- `deerflow.skills.types` -> Skill
- `deerflow.subagents.config` -> SubagentConfig, resolve_subagent_model_name
- `deerflow.subagents.step_events` -> capture_new_step_messages
- `deerflow.subagents.token_collector` -> SubagentTokenCollector
- `deerflow.trace_context` -> DEERFLOW_TRACE_METADATA_KEY
- `deerflow.tracing` -> build_tracing_callbacks, inject_langfuse_metadata
- `deerflow.utils.messages` -> message_content_to_text

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_previous_shutdown_isolated_subagent_loop` = globals().get('_shutdown_isolated_subagent_loop')
- `_background_tasks` = {}
- `_background_tasks_lock` = threading.Lock()
- `_scheduler_pool` = ThreadPoolExecutor(max_workers=3, thread_name_prefix='sub...
- `_isolated_subagent_loop` = None
- `_isolated_subagent_loop_thread` = None
- `_isolated_subagent_loop_started` = None
- `_isolated_subagent_loop_lock` = threading.Lock()
- `MAX_CONCURRENT_SUBAGENTS` = 3

## 函数
#### `ƒ` `_extract_final_result(final_state: Any, *, trace_id: str, name: str) -> str`  L160
  - _文档首行_（仅供参考）: Extract a human-readable result string from the streamed subagent state.
  - 分支数 5，函数体节点数 208；return: 'No response generated', text if text else 'No response generated'
  - 调用: warning, get, info, len, reversed, isinstance, message_content_to_text, type, hasattr, str
  - 反射: hasattr (L195)

#### `ƒ` `_extract_llm_error_fallback(final_state: Any) -> str | None`  L203
  - _文档首行_（仅供参考）: Return the user-facing error for a terminal LLM fallback message.
  - 分支数 6，函数体节点数 117；return: None, content, detail.strip(), 'LLM request failed'
  - 调用: reversed, get, isinstance, strip, message_content_to_text

#### `ƒ` `_run_isolated_subagent_loop(loop: asyncio.AbstractEventLoop, started_event: threading.Event) -> None`  L270
  - _文档首行_（仅供参考）: Run the persistent isolated subagent loop in a dedicated daemon thread.
  - 分支数 1，函数体节点数 46
  - 调用: set_event_loop, call_soon, run_forever, clear

#### `ƒ` `_shutdown_isolated_subagent_loop() -> None`  L283
  - _文档首行_（仅供参考）: Stop and close the persistent isolated subagent loop.
  - 分支数 6，函数体节点数 157；return: None
  - 调用: is_running, call_soon_threadsafe, is_alive, current_thread, join, is_closed, close, warning

#### `ƒ` `_get_isolated_subagent_loop() -> asyncio.AbstractEventLoop`  L320
  - _文档首行_（仅供参考）: Return the persistent event loop used by isolated subagent executions.
  - 分支数 4，函数体节点数 169；raise: RuntimeError('Timed out starting isolated subagent event loop'), RuntimeError('Isolated subagent event loop is not initialized')；return: _isolated_subagent_loop
  - 调用: is_alive, is_closed, is_running, new_event_loop, Event, Thread, start, wait, call_soon_threadsafe, join, close, RuntimeError

#### `ƒ` `_submit_to_isolated_loop_in_context(context: Context, coro_factory: Callable[[], Coroutine[Any, Any, SubagentResult]]) -> Future[SubagentResult]`  L351
  - _文档首行_（仅供参考）: Submit a coroutine to the isolated loop while preserving ContextVar state.
  - 分支数 0，函数体节点数 53；return: context.run(lambda: asyncio.run_coroutine_threadsafe(coro_factory(), _get_isolated_subagent_loop()))
  - 调用: run, run_coroutine_threadsafe, coro_factory, _get_isolated_subagent_loop
  - 子进程: run (L356)

#### `ƒ` `_filter_tools(all_tools: list[BaseTool], allowed: list[str] | None, disallowed: list[str] | None) -> list[BaseTool]`  L364
  - _文档首行_（仅供参考）: Filter tools based on subagent configuration.
  - 分支数 2，函数体节点数 111；return: filtered
  - 调用: set

#### `ƒ` `request_cancel_background_task(task_id: str) -> None`  L1092
  - _文档首行_（仅供参考）: Signal a running background task to stop.
  - 分支数 2，函数体节点数 45
  - 调用: get, set, info

#### `ƒ` `get_background_task_result(task_id: str) -> SubagentResult | None`  L1110
  - _文档首行_（仅供参考）: Get the result of a background task.
  - 分支数 1，函数体节点数 24；return: _background_tasks.get(task_id)
  - 调用: get

#### `ƒ` `list_background_tasks() -> list[SubagentResult]`  L1123
  - _文档首行_（仅供参考）: List all background tasks.
  - 分支数 1，函数体节点数 23；return: list(_background_tasks.values())
  - 调用: list, values

#### `ƒ` `cleanup_background_task(task_id: str) -> None`  L1133
  - _文档首行_（仅供参考）: Remove a completed task from background tasks.
  - 分支数 3，函数体节点数 98；return: None
  - 调用: get, debug, hasattr
  - 反射: hasattr (L1161)

## 类
### 类 `SubagentStatus`  L55
- 继承: Enum
- _文档首行_: Status of a subagent execution.
- 类/实例变量:
  - `PENDING` = 'pending'
  - `RUNNING` = 'running'
  - `COMPLETED` = 'completed'
  - `FAILED` = 'failed'
  - `CANCELLED` = 'cancelled'
  - `TIMED_OUT` = 'timed_out'
- 方法:
  #### `prop` `is_terminal(self) -> bool`    @property  L66
    - 分支数 0，函数体节点数 41；return: self in {type(self).COMPLETED, type(self).FAILED, type(self).CANCELLED, type(self).TIMED_OUT}
    - 调用: type

### 类 `SubagentResult`  L76  @dataclass
- _文档首行_: Result of a subagent execution.
- 类/实例变量:
  - `task_id` = <annotated>
  - `trace_id` = <annotated>
  - `status` = <annotated>
  - `result` = None
  - `error` = None
  - `stop_reason` = None
  - `started_at` = None
  - `completed_at` = None
  - `ai_messages` = None
  - `token_usage_records` = field(default_factory=list)
  - `usage_reported` = False
  - `cancel_event` = field(default_factory=threading.Event, repr=False)
  - `_state_lock` = field(default_factory=threading.Lock, init=False, repr=Fa...
- 方法:
  #### `m` `__post_init__(self)`  L110
    - _文档首行_（仅供参考）: Initialize mutable defaults.
    - 分支数 1，函数体节点数 20
  #### `m` `update_token_usage_records(self, records: list[dict[str, int | str | None]]) -> None`  L115
    - _文档首行_（仅供参考）: Publish the latest cumulative collector snapshot while still running.
    - 分支数 2，函数体节点数 53
    - 调用: list
  #### `m` `try_set_terminal(self, status: SubagentStatus, *, result: str | None, error: str | None, stop_reason: str | None, completed_at: datetime | None, ai_messages: list[dict[str, Any]] | None, token_usage_records: list[dict[str, int | str | None]] | None) -> bool`  L121
    - _文档首行_（仅供参考）: Set a terminal status exactly once.
    - 分支数 8，函数体节点数 203；raise: ValueError(f'Status {status} is not terminal')；return: False, True
    - 调用: ValueError, now

### 类 `SubagentExecutor`  L394
- _文档首行_: Executor for running subagents.
- 方法:
  #### `m` `__init__(self, config: SubagentConfig, tools: list[BaseTool], app_config: AppConfig | None, parent_model: str | None, sandbox_state: SandboxState | None, thread_data: ThreadDataState | None, thread_id: str | None, trace_id: str | None, user_id: str | None, user_role: str | None, oauth_provider: str | None, oauth_id: str | None, run_id: str | None, channel_user_id: str | None, is_internal: bool, authz_attributes: Mapping[str, Any] | None, deerflow_trace_id: str | None)`  L397
    - _文档首行_（仅供参考）: Initialize the executor.
    - 分支数 1，函数体节点数 369
    - 调用: resolve_subagent_model_name, str, uuid4, normalize_authz_attributes, _filter_tools, info, len
  #### `m` `_create_agent(self, tools: list[BaseTool] | None, *, deferred_setup: 'DeferredToolSetup | None')`  L490
    - _文档首行_（仅供参考）: Create the agent instance.
    - 分支数 3，函数体节点数 219；return: create_agent(model=model, tools=tools if tools is not None else self.tools, middleware=middlewares, system_prompt=None, state_schema=ThreadState, checkpointer=False)
    - 调用: get_app_config, resolve_subagent_model_name, create_chat_model, build_mcp_routing_middleware, build_subagent_runtime_middlewares, hasattr, create_agent
  - 反射: hasattr (L531)
  #### `m` `_consume_guard_stop_reason(self) -> str | None`  L544
    - _文档首行_（仅供参考）: Pop and return the guard-cap stop reason set during the last run.
    - 分支数 2，函数体节点数 40；return: reason, None
    - 调用: consume_stop_reason
  #### `m` `_apply_skill_allowed_tools(self, skills: list[Skill]) -> list[BaseTool]`  L590
    - 分支数 0，函数体节点数 26；return: filter_tools_by_skill_allowed_tools(self._base_tools, skills)
    - 调用: filter_tools_by_skill_allowed_tools
  #### `m` `_execute_in_isolated_loop(self, task: str, result_holder: SubagentResult | None) -> SubagentResult`  L945
    - _文档首行_（仅供参考）: Execute the subagent on the persistent isolated event loop.
    - 分支数 4，函数体节点数 157；raise: bare raise；return: future.result(timeout=self.config.timeout_seconds)
    - 调用: copy_context, _submit_to_isolated_loop_in_context, _aexecute, result, set, cancel, debug
  #### `m` `execute(self, task: str, result_holder: SubagentResult | None) -> SubagentResult`  L981
    - _文档首行_（仅供参考）: Execute a task synchronously (wrapper around async execution).
    - 分支数 4，函数体节点数 178；return: self._execute_in_isolated_loop(task, result_holder), asyncio.run(self._aexecute(task, result_holder)), result
    - 调用: get_running_loop, is_running, debug, _execute_in_isolated_loop, run, _aexecute, exception, SubagentResult, str, uuid4, try_set_terminal
  - 子进程: run (L1010)
  #### `m` `execute_async(self, task: str, task_id: str | None) -> str`  L1025
    - _文档首行_（仅供参考）: Start a task execution in the background.
    - 分支数 6，函数体节点数 319；return: task_id
    - 调用: str, uuid4, SubagentResult, info, copy_context, now, _submit_to_isolated_loop_in_context, _aexecute, result, error, set, try_set_terminal, cancel, exception, submit
  #### `⏵m` `async _load_skills(self) -> list[Skill]`  L562
    - _文档首行_（仅供参考）: Load enabled skill metadata based on config.skills.
    - 分支数 4，函数体节点数 236；raise: bare raise；return: [], [s for s in all_skills if s.name in allowed], all_skills
    - 调用: len, info, to_thread, exception, set
  #### `⏵m` `async _load_skill_messages(self, skills: list[Skill]) -> list[SystemMessage]`  L593
    - _文档首行_（仅供参考）: Load skill content as conversation items based on config.skills.
    - 分支数 4，函数体节点数 155；return: [], messages
    - 调用: to_thread, strip, append, SystemMessage, escape, info, debug
  #### `⏵m` `async _build_initial_state(self, task: str) -> tuple[dict[str, Any], list[BaseTool], 'DeferredToolSetup']`  L627
    - _文档首行_（仅供参考）: Build the initial state for agent execution.
    - 分支数 7，函数体节点数 291；return: (state, final_tools, deferred_setup)
    - 调用: _load_skills, _apply_skill_allowed_tools, get_app_config, assemble_deferred_tools, _load_skill_messages, append, get_deferred_tools_prompt_section, get_mcp_routing_hints_prompt_section, SystemMessage, join, HumanMessage
  #### `⏵m` `async _aexecute(self, task: str, result_holder: SubagentResult | None) -> SubagentResult`  L694
    - _文档首行_（仅供参考）: Execute a task asynchronously.
    - 分支数 19，函数体节点数 1113；return: result
    - 调用: str, uuid4, SubagentResult, now, get, _build_initial_state, _create_agent, SubagentTokenCollector, build_tracing_callbacks, list, replace, lower, strip, inject_langfuse_metadata, dict, info, is_set, try_set_terminal, snapshot_records, astream（+11）
  - 文件IO: replace (L763)

## 文件内调用关系
- `_submit_to_isolated_loop_in_context` -> _get_isolated_subagent_loop
- `SubagentExecutor.__init__` -> _filter_tools
- `SubagentExecutor._build_initial_state` -> _load_skills, _apply_skill_allowed_tools, _load_skill_messages
- `SubagentExecutor._aexecute` -> _build_initial_state, _create_agent, try_set_terminal, update_token_usage_records, _extract_llm_error_fallback, _extract_final_result, _consume_guard_stop_reason
- `SubagentExecutor._execute_in_isolated_loop` -> _submit_to_isolated_loop_in_context, _aexecute
- `SubagentExecutor.execute` -> _execute_in_isolated_loop, _aexecute, try_set_terminal
- `SubagentExecutor.execute_async` -> _submit_to_isolated_loop_in_context, _aexecute, try_set_terminal

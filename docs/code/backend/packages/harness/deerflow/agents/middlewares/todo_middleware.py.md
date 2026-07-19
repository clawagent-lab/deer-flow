# `backend/packages/harness/deerflow/agents/middlewares/todo_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/todo_middleware.py`  ·  行数: 359

**模块文档首行**（仅供参考）: Middleware that extends TodoListMiddleware with context-loss detection and premature-exit prevention.

## 模块概览
- 函数 5 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: threading
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `typing` -> Any, override
- `langchain.agents.middleware` -> TodoListMiddleware
- `langchain.agents.middleware.todo` -> Todo
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse, hook_config
- `langchain_core.messages` -> AIMessage, HumanMessage
- `langgraph.runtime` -> Runtime
- `deerflow.agents.thread_state` -> ThreadState

## 模块级常量
- `_TOOL_CALL_FINISH_REASONS` = {'tool_calls', 'function_call'}

## 函数
#### `ƒ` `_todos_in_messages(messages: list[Any]) -> bool`  L31
  - _文档首行_（仅供参考）: Return True if any AIMessage in *messages* contains a write_todos tool call.
  - 分支数 4，函数体节点数 53；return: True, False
  - 调用: isinstance, get

#### `ƒ` `_reminder_in_messages(messages: list[Any]) -> bool`  L41
  - _文档首行_（仅供参考）: Return True if a todo_reminder HumanMessage is already present in *messages*.
  - 分支数 2，函数体节点数 42；return: True, False
  - 调用: isinstance, getattr
  - 反射: getattr (L44)

#### `ƒ` `_format_todos(todos: list[Todo]) -> str`  L49
  - _文档首行_（仅供参考）: Format a list of Todo items into a human-readable string.
  - 分支数 1，函数体节点数 71；return: '\n'.join(lines)
  - 调用: get, append, join

#### `ƒ` `_format_completion_reminder(todos: list[Todo]) -> str`  L59
  - _文档首行_（仅供参考）: Format a completion reminder for incomplete todo items.
  - 分支数 0，函数体节点数 72；return: f'<system_reminder>\nYou have incomplete todo items that must be finished before giving your final response:\n\n{incomplete_text}\n\nPlease continue working on these tasks. Call `write_todos` to mark items as completed as you finish them, and only respond when all items are done.\n</system_reminder>'
  - 调用: get, join

#### `ƒ` `_has_tool_call_intent_or_error(message: AIMessage) -> bool`  L76
  - _文档首行_（仅供参考）: Return True when an AIMessage is not a clean final answer.
  - 分支数 3，函数体节点数 80；return: True, response_metadata.get('finish_reason') in _TOOL_CALL_FINISH_REASONS
  - 调用: getattr, get
  - 反射: getattr (L87), getattr (L96), getattr (L100)

## 类
### 类 `TodoMiddleware`  L104
- 继承: TodoListMiddleware
- _文档首行_: Extends TodoListMiddleware with `write_todos` context-loss detection.
- 类/实例变量:
  - `state_schema` = ThreadState
  - `_MAX_COMPLETION_REMINDERS` = 2
  - `_MAX_COMPLETION_REMINDER_KEYS` = 4096
- 方法:
  #### `st` `_get_thread_id(runtime: Runtime) -> str`    @staticmethod  L177
    - 分支数 0，函数体节点数 42；return: str(thread_id) if thread_id else 'default'
    - 调用: getattr, get, str
  - 反射: getattr (L178)
  #### `st` `_get_run_id(runtime: Runtime) -> str`    @staticmethod  L183
    - 分支数 0，函数体节点数 42；return: str(run_id) if run_id else 'default'
    - 调用: getattr, get, str
  - 反射: getattr (L184)
  #### `st` `_format_pending_completion_reminders(reminders: list[str]) -> str`    @staticmethod  L317
    - 分支数 0，函数体节点数 25；return: '\n\n'.join(dict.fromkeys(reminders))
    - 调用: join, fromkeys
  #### `m` `before_model(self, state: ThreadState, runtime: Runtime) -> dict[str, Any] | None`    @override  L116
    - _文档首行_（仅供参考）: Inject a todo-list reminder when write_todos has left the context window.
    - 分支数 3，函数体节点数 115；return: None, {'messages': [reminder]}
    - 调用: get, _todos_in_messages, _reminder_in_messages, _format_todos, HumanMessage
  #### `m` `__init__(self, *args, **kwargs) -> None`  L168
    - 分支数 0，函数体节点数 116；可变参数（*args/**kwargs）
    - 调用: __init__, super, Lock
  #### `m` `_pending_key(self, runtime: Runtime) -> tuple[str, str]`  L188
    - 分支数 0，函数体节点数 33；return: (self._get_thread_id(runtime), self._get_run_id(runtime))
    - 调用: _get_thread_id, _get_run_id
  #### `m` `_touch_completion_reminder_key_locked(self, key: tuple[str, str]) -> None`  L191
    - 分支数 0，函数体节点数 35
  #### `m` `_completion_reminder_keys_locked(self) -> set[tuple[str, str]]`  L195
    - 分支数 0，函数体节点数 50；return: keys
    - 调用: set, update
  #### `m` `_drop_completion_reminder_key_locked(self, key: tuple[str, str]) -> None`  L201
    - 分支数 0，函数体节点数 48
    - 调用: pop
  #### `m` `_prune_completion_reminder_state_locked(self, protected_key: tuple[str, str]) -> None`  L206
    - 分支数 2，函数体节点数 99；return: None
    - 调用: _completion_reminder_keys_locked, len, sort, get, _drop_completion_reminder_key_locked
  #### `m` `_queue_completion_reminder(self, runtime: Runtime, reminder: str) -> None`  L217
    - 分支数 1，函数体节点数 82
    - 调用: _pending_key, append, setdefault, get, _touch_completion_reminder_key_locked, _prune_completion_reminder_state_locked
  #### `m` `_completion_reminder_count_for_runtime(self, runtime: Runtime) -> int`  L225
    - 分支数 1，函数体节点数 35；return: self._completion_reminder_counts.get(key, 0)
    - 调用: _pending_key, get
  #### `m` `_drain_completion_reminders(self, runtime: Runtime) -> list[str]`  L230
    - 分支数 2，函数体节点数 66；return: reminders
    - 调用: _pending_key, pop, _touch_completion_reminder_key_locked
  #### `m` `_clear_other_run_completion_reminders(self, runtime: Runtime) -> None`  L238
    - 分支数 3，函数体节点数 64
    - 调用: _pending_key, _completion_reminder_keys_locked, _drop_completion_reminder_key_locked
  #### `m` `_clear_current_run_completion_reminders(self, runtime: Runtime) -> None`  L245
    - 分支数 1，函数体节点数 31
    - 调用: _pending_key, _drop_completion_reminder_key_locked
  #### `m` `before_agent(self, state: ThreadState, runtime: Runtime) -> dict[str, Any] | None`    @override  L251
    - 分支数 0，函数体节点数 34；return: None
    - 调用: _clear_other_run_completion_reminders
  #### `m` `after_model(self, state: ThreadState, runtime: Runtime) -> dict[str, Any] | None`    @hook_config(...), override  L262
    - _文档首行_（仅供参考）: Prevent premature agent exit when todo items are still incomplete.
    - 分支数 4，函数体节点数 186；return: base_result, None, {'jump_to': 'model'}
    - 调用: after_model, super, get, next, reversed, isinstance, _has_tool_call_intent_or_error, all, _completion_reminder_count_for_runtime, _queue_completion_reminder, _format_completion_reminder, hook_config
  #### `m` `_augment_request(self, request: ModelRequest) -> ModelRequest`  L320
    - 分支数 1，函数体节点数 65；return: request, request.override(messages=new_messages)
    - 调用: _drain_completion_reminders, HumanMessage, _format_pending_completion_reminders, override
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L335
    - 分支数 0，函数体节点数 34；return: handler(self._augment_request(request))
    - 调用: handler, _augment_request
  #### `m` `after_agent(self, state: ThreadState, runtime: Runtime) -> dict[str, Any] | None`    @override  L351
    - 分支数 0，函数体节点数 34；return: None
    - 调用: _clear_current_run_completion_reminders
  #### `⏵m` `async abefore_model(self, state: ThreadState, runtime: Runtime) -> dict[str, Any] | None`    @override  L154
    - _文档首行_（仅供参考）: Async version of before_model.
    - 分支数 0，函数体节点数 36；return: self.before_model(state, runtime)
    - 调用: before_model
  #### `⏵m` `async abefore_agent(self, state: ThreadState, runtime: Runtime) -> dict[str, Any] | None`    @override  L256
    - 分支数 0，函数体节点数 34；return: None
    - 调用: _clear_other_run_completion_reminders
  #### `⏵m` `async aafter_model(self, state: ThreadState, runtime: Runtime) -> dict[str, Any] | None`    @override, hook_config(...)  L308
    - _文档首行_（仅供参考）: Async version of after_model.
    - 分支数 0，函数体节点数 43；return: self.after_model(state, runtime)
    - 调用: after_model, hook_config
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L343
    - 分支数 0，函数体节点数 39；return: await handler(self._augment_request(request))
    - 调用: handler, _augment_request
  #### `⏵m` `async aafter_agent(self, state: ThreadState, runtime: Runtime) -> dict[str, Any] | None`    @override  L356
    - 分支数 0，函数体节点数 34；return: None
    - 调用: _clear_current_run_completion_reminders

## 文件内调用关系
- `TodoMiddleware.before_model` -> _todos_in_messages, _reminder_in_messages, _format_todos
- `TodoMiddleware.abefore_model` -> before_model
- `TodoMiddleware.__init__` -> __init__
- `TodoMiddleware._pending_key` -> _get_thread_id, _get_run_id
- `TodoMiddleware._prune_completion_reminder_state_locked` -> _completion_reminder_keys_locked, _drop_completion_reminder_key_locked
- `TodoMiddleware._queue_completion_reminder` -> _pending_key, _touch_completion_reminder_key_locked, _prune_completion_reminder_state_locked
- `TodoMiddleware._completion_reminder_count_for_runtime` -> _pending_key
- `TodoMiddleware._drain_completion_reminders` -> _pending_key, _touch_completion_reminder_key_locked
- `TodoMiddleware._clear_other_run_completion_reminders` -> _pending_key, _completion_reminder_keys_locked, _drop_completion_reminder_key_locked
- `TodoMiddleware._clear_current_run_completion_reminders` -> _pending_key, _drop_completion_reminder_key_locked
- `TodoMiddleware.before_agent` -> _clear_other_run_completion_reminders
- `TodoMiddleware.abefore_agent` -> _clear_other_run_completion_reminders
- `TodoMiddleware.after_model` -> after_model, _has_tool_call_intent_or_error, _completion_reminder_count_for_runtime, _queue_completion_reminder, _format_completion_reminder
- `TodoMiddleware.aafter_model` -> after_model
- `TodoMiddleware._augment_request` -> _drain_completion_reminders, _format_pending_completion_reminders
- `TodoMiddleware.wrap_model_call` -> _augment_request
- `TodoMiddleware.awrap_model_call` -> _augment_request
- `TodoMiddleware.after_agent` -> _clear_current_run_completion_reminders
- `TodoMiddleware.aafter_agent` -> _clear_current_run_completion_reminders

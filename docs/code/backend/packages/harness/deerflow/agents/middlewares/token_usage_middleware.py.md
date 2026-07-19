# `backend/packages/harness/deerflow/agents/middlewares/token_usage_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/token_usage_middleware.py`  ·  行数: 359

**模块文档首行**（仅供参考）: Middleware for logging token usage and annotating step attribution.

## 模块概览
- 函数 8 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `collections` -> defaultdict
- `typing` -> Any, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.todo` -> Todo
- `langchain_core.messages` -> AIMessage, ToolMessage
- `langgraph.runtime` -> Runtime

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `TOKEN_USAGE_ATTRIBUTION_KEY` = 'token_usage_attribution'

## 函数
#### `ƒ` `_string_arg(value: Any) -> str | None`  L20
  - 分支数 1，函数体节点数 34；return: normalized or None, None
  - 调用: isinstance, strip

#### `ƒ` `_normalize_todos(value: Any) -> list[Todo]`  L27
  - 分支数 5，函数体节点数 120；return: [], normalized
  - 调用: isinstance, _string_arg, get, append

#### `ƒ` `_todo_action_kind(previous: Todo | None, current: Todo) -> str`  L50
  - 分支数 6，函数体节点数 95；return: 'todo_complete', 'todo_start', 'todo_update'
  - 调用: get

#### `ƒ` `_build_todo_actions(previous_todos: list[Todo], next_todos: list[Todo]) -> list[dict[str, Any]]`  L72
  - 分支数 13，函数体节点数 417；return: actions
  - 调用: defaultdict, set, enumerate, get, isinstance, append, pop, add, len, _todo_action_kind

#### `ƒ` `_describe_tool_call(tool_call: dict[str, Any], todos: list[Todo]) -> list[dict[str, Any]]`  L135
  - 分支数 6，函数体节点数 263；return: [{'kind': 'tool', 'tool_name': name, 'tool_call_id': tool_call_id}], [{**action, 'tool_call_id': tool_call_id} for action in actions], [{'kind': 'subagent', 'description': _string_arg(args.get('description')), 'subagent_type': _string_arg(args.get('subagent_type')), 'tool_call_id': tool_call_id}], [{'kind': 'search', 'tool_name': name, 'query': query, 'tool_call_id': tool_call_id}], [{'kind': 'present_files', 'tool_call_id': tool_call_id}], [{'kind': 'clarification', 'tool_call_id': tool_call_id}], [{'kind': 'tool', 'tool_name': name, 'description': _string_arg(args.get('description')), 'tool_call_id': tool_call_id}]
  - 调用: _string_arg, get, isinstance, _normalize_todos, _build_todo_actions

#### `ƒ` `_infer_step_kind(message: AIMessage, actions: list[dict[str, Any]]) -> str`  L206
  - 分支数 4，函数体节点数 88；return: 'todo_update', 'subagent_dispatch', 'tool_batch', 'final_answer', 'thinking'
  - 调用: get, len

#### `ƒ` `_has_tool_call(message: AIMessage, tool_call_id: str) -> bool`  L220
  - _文档首行_（仅供参考）: Return True if the AIMessage contains a tool_call with the given id.
  - 分支数 4，函数体节点数 65；return: True, False
  - 调用: isinstance, get, hasattr
  - 反射: hasattr (L226)

#### `ƒ` `_build_attribution(message: AIMessage, todos: list[Todo]) -> dict[str, Any]`  L231
  - 分支数 6，函数体节点数 221；return: {'version': 1, 'kind': _infer_step_kind(message, actions), 'shared_attribution': len(actions) > 1, 'tool_call_ids': tool_call_ids, 'actions': actions}
  - 调用: getattr, list, isinstance, _describe_tool_call, extend, get, _normalize_todos, _string_arg, append, _infer_step_kind, len
  - 反射: getattr (L232)

## 类
### 类 `TokenUsageMiddleware`  L267
- 继承: AgentMiddleware
- _文档首行_: Logs token usage from model responses and annotates the AI step.
- 方法:
  #### `m` `_apply(self, state: AgentState) -> dict | None`  L270
    - 分支数 13，函数体节点数 560；return: None, {'messages': [state_updates[idx] for idx in sorted(state_updates)]}, {'messages': [state_updates[idx] for idx in sorted(state_updates)]} if state_updates else None
    - 调用: get, len, isinstance, pop_cached_subagent_usage, _has_tool_call, getattr, model_copy, sorted, append, join, info, _build_attribution, dict
  - 反射: getattr (L304), getattr (L322), getattr (L342)
  #### `m` `after_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L353
    - 分支数 0，函数体节点数 24；return: self._apply(state)
    - 调用: _apply
  #### `⏵m` `async aafter_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L357
    - 分支数 0，函数体节点数 24；return: self._apply(state)
    - 调用: _apply

## 文件内调用关系
- `_normalize_todos` -> _string_arg
- `_build_todo_actions` -> _todo_action_kind
- `_describe_tool_call` -> _string_arg, _normalize_todos, _build_todo_actions
- `_build_attribution` -> _describe_tool_call, _normalize_todos, _string_arg, _infer_step_kind
- `TokenUsageMiddleware._apply` -> _has_tool_call, _build_attribution
- `TokenUsageMiddleware.after_model` -> _apply
- `TokenUsageMiddleware.aafter_model` -> _apply

# `backend/packages/harness/deerflow/agents/middlewares/subagent_limit_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/subagent_limit_middleware.py`  ·  行数: 175

**模块文档首行**（仅供参考）: Middleware to enforce subagent tool-call limits.

## 模块概览
- 函数 7 个，类 1 个，模块级常量 7 个

## 依赖（import）
- 模块: logging
- `typing` -> Any, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langgraph.runtime` -> Runtime
- `deerflow.agents.middlewares.tool_call_metadata` -> clone_ai_message_with_tool_calls
- `deerflow.config.subagents_config` -> DEFAULT_MAX_TOTAL_SUBAGENTS_PER_RUN, MAX_CONCURRENT_SUBAGENT_CALLS, MAX_TOTAL_SUBAGENTS_PER_RUN, MIN_CONCURRENT_SUBAGENT_CALLS, MIN_TOTAL_SUBAGENTS_PER_RUN, clamp_subagent_concurrency, clamp_total_subagents_per_run
- `deerflow.subagents.executor` -> MAX_CONCURRENT_SUBAGENTS

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `MIN_SUBAGENT_LIMIT` = MIN_CONCURRENT_SUBAGENT_CALLS
- `MAX_SUBAGENT_LIMIT` = MAX_CONCURRENT_SUBAGENT_CALLS
- `DEFAULT_MAX_TOTAL_SUBAGENTS` = DEFAULT_MAX_TOTAL_SUBAGENTS_PER_RUN
- `MIN_SUBAGENT_TOTAL_LIMIT` = MIN_TOTAL_SUBAGENTS_PER_RUN
- `MAX_SUBAGENT_TOTAL_LIMIT` = MAX_TOTAL_SUBAGENTS_PER_RUN
- `_TOTAL_LIMIT_STOP_MSG` = '[SUBAGENT LIMIT REACHED] The subagent delegation limit f...

## 函数
#### `ƒ` `_clamp_subagent_limit(value: int) -> int`  L38
  - _文档首行_（仅供参考）: Clamp subagent limit to valid range [2, 4].
  - 分支数 0，函数体节点数 15；return: clamp_subagent_concurrency(value)
  - 调用: clamp_subagent_concurrency

#### `ƒ` `_clamp_total_subagent_limit(value: int) -> int`  L43
  - _文档首行_（仅供参考）: Clamp total subagent limit to a bounded positive range.
  - 分支数 0，函数体节点数 15；return: clamp_total_subagents_per_run(value)
  - 调用: clamp_total_subagents_per_run

#### `ƒ` `_append_text(content: Any, text: str) -> Any`  L48
  - 分支数 4，函数体节点数 75；return: text, f'{content}\n\n{text}', [*content, {'type': 'text', 'text': f'\n\n{text}'}]
  - 调用: isinstance

#### `ƒ` `_delegation_id(entry: object) -> str | None`  L60
  - 分支数 1，函数体节点数 41；return: None, str(entry_id) if entry_id else None
  - 调用: isinstance, get, str

#### `ƒ` `_delegation_run_id(entry: object) -> str | None`  L67
  - 分支数 1，函数体节点数 41；return: None, str(run_id) if run_id else None
  - 调用: isinstance, get, str

#### `ƒ` `_runtime_run_id(runtime: Runtime | None) -> str | None`  L74
  - 分支数 1，函数体节点数 54；return: None, str(run_id) if run_id else None
  - 调用: getattr, isinstance, get, str
  - 反射: getattr (L75)

#### `ƒ` `_count_prior_delegations(delegations: object, *, run_id: str | None) -> int`  L82
  - 分支数 4，函数体节点数 82；return: 0, len(ids)
  - 调用: isinstance, set, _delegation_run_id, _delegation_id, add, len

## 类
### 类 `SubagentLimitMiddleware`  L95
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Truncates excess 'task' tool calls from a single model response/run.
- 方法:
  #### `m` `__init__(self, max_concurrent: int, max_total: int)`  L112
    - 分支数 0，函数体节点数 40
    - 调用: __init__, super, _clamp_subagent_limit, _clamp_total_subagent_limit
  #### `m` `_truncate_task_calls(self, state: AgentState, runtime: Runtime | None) -> dict | None`  L117
    - 分支数 7，函数体节点数 317；return: None, {'messages': [updated_msg]}
    - 调用: get, getattr, enumerate, _runtime_run_id, warning, _count_prior_delegations, max, min, len, set, isinstance, _append_text, clone_ai_message_with_tool_calls
  - 反射: getattr (L123), getattr (L126), getattr (L160)
  #### `m` `after_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L169
    - 分支数 0，函数体节点数 26；return: self._truncate_task_calls(state, runtime)
    - 调用: _truncate_task_calls
  #### `⏵m` `async aafter_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L173
    - 分支数 0，函数体节点数 26；return: self._truncate_task_calls(state, runtime)
    - 调用: _truncate_task_calls

## 文件内调用关系
- `_count_prior_delegations` -> _delegation_run_id, _delegation_id
- `SubagentLimitMiddleware.__init__` -> __init__, _clamp_subagent_limit, _clamp_total_subagent_limit
- `SubagentLimitMiddleware._truncate_task_calls` -> _runtime_run_id, _count_prior_delegations, _append_text
- `SubagentLimitMiddleware.after_model` -> _truncate_task_calls
- `SubagentLimitMiddleware.aafter_model` -> _truncate_task_calls

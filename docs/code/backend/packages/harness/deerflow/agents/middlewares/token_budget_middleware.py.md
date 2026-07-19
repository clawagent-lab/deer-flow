# `backend/packages/harness/deerflow/agents/middlewares/token_budget_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/token_budget_middleware.py`  ·  行数: 315

**模块文档首行**（仅供参考）: Middleware to enforce per-run token budget limits.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 3 个

## 依赖（import）
- 模块: logging, threading
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `dataclasses` -> dataclass
- `typing` -> Any, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> AIMessage, HumanMessage
- `langgraph.runtime` -> Runtime
- `deerflow.agents.middlewares._bounded_dict` -> BoundedDict
- `deerflow.config.token_budget_config` -> TokenBudgetConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_BUDGET_WARNING_MSG` = '[TOKEN BUDGET WARNING] You have used {used:,} of your {b...
- `_BUDGET_EXCEEDED_MSG` = '[TOKEN BUDGET EXCEEDED] The {reason} token usage ({used:...

## 类
### 类 `TokenUsage`  L56  @dataclass
- 类/实例变量:
  - `input` = 0
  - `output` = 0
  - `total` = 0

### 类 `TokenBudgetMiddleware`  L62
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Enforce per-run token budget limits.
- 方法:
  #### `cls` `from_config(cls, config: TokenBudgetConfig) -> TokenBudgetMiddleware`    @classmethod  L81
    - 分支数 0，函数体节点数 17；return: cls(config=config)
    - 调用: cls
  #### `st` `_get_run_id(runtime: Runtime) -> str`    @staticmethod  L105
    - 分支数 1，函数体节点数 49；return: ctx['run_id'], str(id(runtime))
    - 调用: getattr, isinstance, str, id
  - 反射: getattr (L106)
  #### `st` `_append_text(content: str | list[dict | None] | None, stop_msg: str) -> str | list[dict | str]`    @staticmethod  L156
    - _文档首行_（仅供参考）: Append a stop message to an AIMessage.content field.
    - 分支数 4，函数体节点数 118；return: stop_msg, f'{content}\n\n{stop_msg}', f'\n\n{stop_msg}', new_content
    - 调用: isinstance, list, append
  #### `m` `__init__(self, config: TokenBudgetConfig) -> None`  L65
    - 分支数 0，函数体节点数 146
    - 调用: __init__, super, Lock, BoundedDict
  #### `m` `reset(self) -> None`  L84
    - 分支数 1，函数体节点数 50
    - 调用: clear
  #### `m` `consume_stop_reason(self, run_id: str | None) -> str | None`  L92
    - _文档首行_（仅供参考）: Pop and return the stop reason the hard-stop set for this run.
    - 分支数 1，函数体节点数 33；return: self._stop_reason.pop(run_id, None)
    - 调用: pop
  #### `m` `_clear_run_state(self, run_id: str) -> None`  L112
    - 分支数 1，函数体节点数 57
    - 调用: pop
  #### `m` `before_agent(self, state: AgentState, runtime: Runtime) -> None`    @override  L120
    - 分支数 5，函数体节点数 151；return: None
    - 调用: get, _get_run_id, setdefault, TokenUsage, isinstance, hasattr
  - 反射: hasattr (L135)
  #### `m` `after_agent(self, state: AgentState, runtime: Runtime) -> None`    @override  L146
    - 分支数 1，函数体节点数 35；return: None
    - 调用: _clear_run_state, _get_run_id
  #### `m` `_build_hard_stop_update(self, msg: AIMessage, stop_msg: str) -> dict[str, Any]`  L170
    - _文档首行_（仅供参考）: Build the state update dictionary for a hard stop.
    - 分支数 3，函数体节点数 137；return: {'messages': [stopped_msg]}
    - 调用: _append_text, dict, getattr, get, model_copy
  - 反射: getattr (L179)
  #### `m` `_apply(self, state: AgentState, runtime: Runtime) -> dict | None`  L187
    - 分支数 15，函数体节点数 595；return: None, self._build_hard_stop_update(last_msg, stop_text)
    - 调用: get, isinstance, _get_run_id, setdefault, TokenUsage, hasattr, max, append, warning, getattr, format, _build_hard_stop_update, info
  - 反射: hasattr (L206), getattr (L256)
  #### `m` `after_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L275
    - 分支数 0，函数体节点数 26；return: self._apply(state, runtime)
    - 调用: _apply
  #### `m` `_drain_pending_warnings(self, runtime: Runtime) -> list[str]`  L282
    - 分支数 2，函数体节点数 60；return: [], warnings or []
    - 调用: _get_run_id, pop
  #### `m` `_inject_warnings(self, request: ModelRequest, warnings: list[str]) -> ModelRequest`  L291
    - 分支数 1，函数体节点数 77；return: request, request.override(messages=new_messages)
    - 调用: join, HumanMessage, getattr, list, override
  - 反射: getattr (L298)
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L303
    - 分支数 0，函数体节点数 53；return: handler(request)
    - 调用: _drain_pending_warnings, _inject_warnings, handler
  #### `⏵m` `async abefore_agent(self, state: AgentState, runtime: Runtime) -> None`    @override  L142
    - 分支数 0，函数体节点数 22
    - 调用: before_agent
  #### `⏵m` `async aafter_agent(self, state: AgentState, runtime: Runtime) -> None`    @override  L152
    - 分支数 0，函数体节点数 22
    - 调用: after_agent
  #### `⏵m` `async aafter_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L279
    - 分支数 0，函数体节点数 26；return: self._apply(state, runtime)
    - 调用: _apply
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L311
    - 分支数 0，函数体节点数 58；return: await handler(request)
    - 调用: _drain_pending_warnings, _inject_warnings, handler

## 文件内调用关系
- `TokenBudgetMiddleware.__init__` -> __init__
- `TokenBudgetMiddleware.before_agent` -> _get_run_id
- `TokenBudgetMiddleware.abefore_agent` -> before_agent
- `TokenBudgetMiddleware.after_agent` -> _clear_run_state, _get_run_id
- `TokenBudgetMiddleware.aafter_agent` -> after_agent
- `TokenBudgetMiddleware._build_hard_stop_update` -> _append_text
- `TokenBudgetMiddleware._apply` -> _get_run_id, _build_hard_stop_update
- `TokenBudgetMiddleware.after_model` -> _apply
- `TokenBudgetMiddleware.aafter_model` -> _apply
- `TokenBudgetMiddleware._drain_pending_warnings` -> _get_run_id
- `TokenBudgetMiddleware.wrap_model_call` -> _drain_pending_warnings, _inject_warnings
- `TokenBudgetMiddleware.awrap_model_call` -> _drain_pending_warnings, _inject_warnings

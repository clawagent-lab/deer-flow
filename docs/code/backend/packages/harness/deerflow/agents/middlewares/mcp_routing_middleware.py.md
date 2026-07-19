# `backend/packages/harness/deerflow/agents/middlewares/mcp_routing_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/mcp_routing_middleware.py`  ·  行数: 138

**模块文档首行**（仅供参考）: Auto-promote deferred MCP tools from routing metadata before model calls.

## 模块概览
- 函数 1 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `collections.abc` -> Mapping, Sequence
- `typing` -> Any, TypedDict, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> HumanMessage
- `langgraph.runtime` -> Runtime
- `deerflow.config.tool_search_config` -> clamp_auto_promote_top_k
- `deerflow.utils.messages` -> get_original_user_content_text, is_real_user_message

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `McpRoutingIndex` = Mapping[str, McpRoutingIndexEntry]

## 函数
#### `ƒ` `assert_mcp_routing_before_deferred_filter(middlewares: Sequence[AgentMiddleware]) -> None`  L130
  - _文档首行_（仅供参考）: Fail fast if auto-promote would run after deferred schema filtering.
  - 分支数 1，函数体节点数 105；raise: RuntimeError(f'McpRoutingMiddleware must be installed before DeferredToolFilterMiddleware (routing index {routing_idx}, deferred filter index {filter_idx})')
  - 调用: next, enumerate, isinstance, RuntimeError

## 类
### 类 `McpRoutingIndexEntry`  L20
- 继承: TypedDict
- 类/实例变量:
  - `priority` = <annotated>
  - `keywords` = <annotated>

### 类 `McpRoutingMiddleware`  L28
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Write minimal deferred-tool promotion state from latest user text.
- 方法:
  #### `st` `_normalize_index(routing_index: McpRoutingIndex) -> dict[str, tuple[int, tuple[str, ...]]]`    @staticmethod  L49
    - 分支数 5，函数体节点数 203；return: normalized
    - 调用: items, str, int, get, isinstance, tuple, strip
  #### `st` `_latest_user_message(messages: list[Any]) -> HumanMessage | None`    @staticmethod  L74
    - 分支数 2，函数体节点数 35；return: message, None
    - 调用: reversed, is_real_user_message
  #### `m` `__init__(self, routing_index: McpRoutingIndex, catalog_hash: str | None, top_k: int) -> None`  L37
    - 分支数 0，函数体节点数 52
    - 调用: __init__, super, clamp_auto_promote_top_k, _normalize_index
  #### `m` `_matched_names(self, state: Mapping[str, Any] | None) -> list[str]`  L80
    - 分支数 6，函数体节点数 229；return: [], [name for _, name in matched[:self._top_k]]
    - 调用: list, get, _latest_user_message, get_original_user_content_text, casefold, items, any, append, sort
  #### `m` `_state_update(self, state: Mapping[str, Any] | None) -> dict[str, Any] | None`  L104
    - 分支数 1，函数体节点数 84；return: None, {'promoted': {'catalog_hash': self._catalog_hash, 'names': names}}
    - 调用: _matched_names, debug, len
  #### `m` `before_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None`    @override  L122
    - 分支数 0，函数体节点数 32；return: self._state_update(state)
    - 调用: _state_update
  #### `⏵m` `async abefore_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None`    @override  L126
    - 分支数 0，函数体节点数 32；return: self._state_update(state)
    - 调用: _state_update

## 文件内调用关系
- `McpRoutingMiddleware.__init__` -> __init__, _normalize_index
- `McpRoutingMiddleware._matched_names` -> _latest_user_message
- `McpRoutingMiddleware._state_update` -> _matched_names
- `McpRoutingMiddleware.before_model` -> _state_update
- `McpRoutingMiddleware.abefore_model` -> _state_update

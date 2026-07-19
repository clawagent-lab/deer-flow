# `backend/packages/harness/deerflow/agents/memory/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/tools.py`  ·  行数: 248

**模块文档首行**（仅供参考）: Memory tools for tool-driven memory mode.

## 模块概览
- 函数 7 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging
- `langchain.tools` -> tool
- `deerflow.agents.memory.manager` -> get_memory_manager
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_resolve_scope(runtime: Runtime | None) -> tuple[str | None, str]`  L31
  - _文档首行_（仅供参考）: Resolve agent_name and user_id for tool handler scope.
  - 分支数 1，函数体节点数 75；return: (agent_name, resolve_runtime_user_id(runtime))
  - 调用: getattr, isinstance, get, str, resolve_runtime_user_id
  - 反射: getattr (L38)

#### `ƒ` `_memory_content_key(content: str) -> str`  L45
  - 分支数 0，函数体节点数 16；return: content.strip().casefold()
  - 调用: casefold, strip

#### `ƒ` `memory_search_tool(runtime: Runtime, query: str, category: str | None, limit: int) -> str`    @tool(...)  L50
  - _文档首行_（仅供参考）: Search existing facts by natural language query.
  - 分支数 1，函数体节点数 106；return: json.dumps({'results': results, 'count': len(results)}, ensure_ascii=False), json.dumps({'error': str(exc)})
  - 调用: _resolve_scope, search, get_memory_manager, dumps, len, exception, str, tool

#### `ƒ` `memory_add_tool(runtime: Runtime, content: str, category: str, confidence: float) -> str`    @tool(...)  L88
  - _文档首行_（仅供参考）: Store a new fact about the user or conversation context.
  - 分支数 5，函数体节点数 258；return: json.dumps({'error': 'empty content'}), json.dumps({'error': 'Duplicate fact'}), json.dumps({'error': f'memory backend {type(manager).__name__} does not support create_fact'}), json.dumps({'error': 'Fact was not stored because memory.max_facts kept higher-confidence facts'}), json.dumps({'fact_id': fact_id, 'status': 'added'}), json.dumps({'error': str(exc)})
  - 调用: _resolve_scope, strip, dumps, _memory_content_key, get_memory_manager, get, get_memory, any, str, getattr, callable, type, create, exception, tool
  - 反射: getattr (L127)

#### `ƒ` `memory_update_tool(runtime: Runtime, fact_id: str, content: str | None, category: str | None, confidence: float | None) -> str`    @tool(...)  L159
  - _文档首行_（仅供参考）: Update an existing fact. Only provided fields are changed; omitted
  - 分支数 2，函数体节点数 183；return: json.dumps({'error': f'memory backend {type(manager).__name__} does not support update_fact'}), json.dumps({'fact_id': fact_id, 'status': 'updated'}), json.dumps({'error': f'Fact not found: {fact_id}'}), json.dumps({'error': str(exc)})
  - 调用: _resolve_scope, get_memory_manager, getattr, callable, dumps, type, update, str, exception, tool
  - 反射: getattr (L185)

#### `ƒ` `memory_delete_tool(runtime: Runtime, fact_id: str) -> str`    @tool(...)  L207
  - _文档首行_（仅供参考）: Delete a fact by its ID.
  - 分支数 2，函数体节点数 153；return: json.dumps({'error': f'memory backend {type(manager).__name__} does not support delete_fact'}), json.dumps({'fact_id': fact_id, 'status': 'deleted'}), json.dumps({'error': f'Fact not found: {fact_id}'}), json.dumps({'error': str(exc)})
  - 调用: _resolve_scope, get_memory_manager, getattr, callable, dumps, type, delete, str, exception, tool
  - 反射: getattr (L223)

#### `ƒ` `get_memory_tools() -> list`  L237
  - _文档首行_（仅供参考）: Return all memory tools for agent registration.
  - 分支数 0，函数体节点数 17；return: [memory_search_tool, memory_add_tool, memory_update_tool, memory_delete_tool]

## 文件内调用关系
- `memory_search_tool` -> _resolve_scope
- `memory_add_tool` -> _resolve_scope, _memory_content_key
- `memory_update_tool` -> _resolve_scope
- `memory_delete_tool` -> _resolve_scope

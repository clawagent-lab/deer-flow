# `backend/packages/harness/deerflow/agents/memory/backends/noop/noop_manager.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/noop/noop_manager.py`  ·  行数: 208

**模块文档首行**（仅供参考）: Noop memory backend -- a functional empty :class:`MemoryManager`.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any
- `deerflow.agents.memory.manager` -> MemoryManager
- `.config` -> NoopConfig

## 函数
#### `ƒ` `_empty_memory() -> dict[str, Any]`  L50
  - _文档首行_（仅供参考）: A fresh empty memory document (callers may mutate).
  - 分支数 0，函数体节点数 19；return: {'facts': []}

## 类
### 类 `NoopMemoryManager`  L60
- 继承: MemoryManager
- _文档首行_: Backend that stores and recalls nothing.
- 方法:
  #### `m` `__init__(self, backend_config: dict[str, Any] | None) -> None`  L68
    - 分支数 0，函数体节点数 42
    - 调用: __init__, super, from_backend_config
  #### `m` `add(self, thread_id: str, messages: list[Any], *, agent_name: str | None, user_id: str | None, trace_id: str | None) -> None`  L76
    - 分支数 0，函数体节点数 37；return: None
  #### `m` `add_nowait(self, thread_id: str, messages: list[Any], *, agent_name: str | None, user_id: str | None) -> None`  L87
    - 分支数 0，函数体节点数 30；return: None
  #### `m` `get_context(self, user_id: str | None, *, agent_name: str | None, thread_id: str | None) -> str`  L98
    - 分支数 0，函数体节点数 27；return: ''
  #### `m` `search(self, query: str, top_k: int, *, user_id: str | None, agent_name: str | None, category: str | None) -> list[dict[str, Any]]`  L107
    - 分支数 0，函数体节点数 48；return: []
  #### `m` `get_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L119
    - 分支数 0，函数体节点数 31；return: _empty_memory()
    - 调用: _empty_memory
  #### `m` `delete_memory(self, *, user_id: str | None, agent_name: str | None) -> None`  L127
    - 分支数 0，函数体节点数 20；return: None
  #### `m` `clear_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L135
    - 分支数 0，函数体节点数 31；return: _empty_memory()
    - 调用: _empty_memory
  #### `m` `import_memory(self, memory_data: dict[str, Any], *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L143
    - 分支数 0，函数体节点数 42；return: _empty_memory()
    - 调用: _empty_memory
  #### `m` `export_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L152
    - 分支数 0，函数体节点数 31；return: _empty_memory()
    - 调用: _empty_memory
  #### `m` `shutdown_flush(self, timeout: float) -> bool`  L161
    - _文档首行_（仅供参考）: Nothing is ever queued, so shutdown drain is a clean no-op success.
    - 分支数 0，函数体节点数 12；return: True

## 文件内调用关系
- `NoopMemoryManager.__init__` -> __init__
- `NoopMemoryManager.get_memory` -> _empty_memory
- `NoopMemoryManager.clear_memory` -> _empty_memory
- `NoopMemoryManager.import_memory` -> _empty_memory
- `NoopMemoryManager.export_memory` -> _empty_memory

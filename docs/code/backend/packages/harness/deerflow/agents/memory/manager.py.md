# `backend/packages/harness/deerflow/agents/memory/manager.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/manager.py`  ·  行数: 485

**模块文档首行**（仅供参考）: Memory manager contract + pluggable backend factory.

## 模块概览
- 函数 7 个，类 1 个，模块级常量 6 个

## 依赖（import）
- 模块: importlib, logging, os, threading
- `__future__` -> annotations
- `abc` -> ABC, abstractmethod
- `pathlib` -> Path
- `types` -> ModuleType
- `typing` -> Any
- `deerflow.config.memory_config` -> get_memory_config

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_BACKENDS_DIR` = Path(__file__).parent / 'backends'
- `_MANAGER_CLASS_ATTR` = 'MANAGER_CLASS'
- `_memory_manager` = None
- `_backends_cache` = None
- `_manager_lock` = threading.Lock()

## 函数
#### `ƒ` `_scan_backends() -> dict[str, type[MemoryManager]]`  L221
  - _文档首行_（仅供参考）: Discover pluggable backends under ``backends/<name>/``.
  - 分支数 8，函数体节点数 215；return: _backends_cache, registry
  - 调用: is_dir, sorted, iterdir, startswith, is_file, import_module, exception, getattr, isinstance, issubclass, warning
  - 文件IO: iterdir (L240)
  - 反射: import_module (L247), getattr (L251)

#### `ƒ` `_resolve_manager_class(manager_class: str) -> type[MemoryManager]`  L267
  - _文档首行_（仅供参考）: Resolve a ``manager_class`` config value to a concrete class.
  - 分支数 6，函数体节点数 204；raise: ValueError(f"memory.manager_class={manager_class!r} is not a registered backend name (known: {sorted(registry)}) nor a resolvable 'pkg.mod:Cls' path" + (f': {dotted_error}' if dotted_error else '') + '. Fix memory.manager_class in config; refusing to silently fall back to a different storage backend (memory is persistent state -- a wrong store is a silent data-integrity footgun).')；return: registry[manager_class], cls
  - 调用: _scan_backends, partition, rpartition, import_module, getattr, isinstance, issubclass, ValueError, sorted
  - 反射: import_module (L294), getattr (L298)

#### `ƒ` `_host_default_tracing_callback(invoke_config: dict[str, Any], *, thread_id: str | None, user_id: str | None, trace_id: str | None, model_name: str | None) -> None`  L328
  - _文档首行_（仅供参考）: deer-flow default for DeerMem's ``tracing_callback`` slot.
  - 分支数 0，函数体节点数 81
  - 调用: inject_langfuse_metadata, get

#### `ƒ` `_host_default_should_keep_hidden_message(additional_kwargs: Any) -> bool`  L357
  - _文档首行_（仅供参考）: deer-flow default for DeerMem's ``should_keep_hidden_message`` slot.
  - 分支数 0，函数体节点数 20；return: read_human_input_response(additional_kwargs) is not None
  - 调用: read_human_input_response

#### `ƒ` `_host_default_llm() -> Any`  L371
  - _文档首行_（仅供参考）: deer-flow default for DeerMem's ``host_llm`` slot (zero-config extraction).
  - 分支数 1，函数体节点数 29；return: create_chat_model(name=None), None
  - 调用: create_chat_model, warning

#### `ƒ` `get_memory_manager() -> MemoryManager`  L391
  - _文档首行_（仅供参考）: Return the singleton :class:`MemoryManager` for the active config.
  - 分支数 10，函数体节点数 275；raise: ValueError(f"memory.backend_config.storage_path={backend_config['storage_path']!r} resolves to an existing file {_resolved_storage_path}; DeerMem treats storage_path as a root DIRECTORY (per-user memory under {{storage_path}}/users/{{uid}}/memory.json). Point it at a directory.")；return: _memory_manager
  - 调用: get_memory_config, _resolve_manager_class, dict, get, str, runtime_home, is_absolute, Path, resolve, is_file, ValueError, isinstance, _host_default_llm, cls, info

#### `ƒ` `reset_memory_manager() -> None`  L475
  - _文档首行_（仅供参考）: Clear the cached singleton manager and the backend registry.
  - 分支数 1，函数体节点数 18

## 类
### 类 `MemoryManager`  L44
- 继承: ABC
- 含 abstractmethod（抽象基类）
- _文档首行_: Backend-neutral memory manager contract (9 methods).
- 方法:
  #### `m` `__init__(self, backend_config: dict[str, Any] | None) -> None`  L66
    - _文档首行_（仅供参考）: Receive backend-private config (the factory passes ``backend_config``).
    - 分支数 0，函数体节点数 28
  #### `m` `add(self, thread_id: str, messages: list[Any], *, agent_name: str | None, user_id: str | None, trace_id: str | None) -> None`    @abstractmethod  L77
    - _文档首行_（仅供参考）: Queue a conversation for memory update (debounced, asynchronous).
    - 分支数 0，函数体节点数 39
  #### `m` `add_nowait(self, thread_id: str, messages: list[Any], *, agent_name: str | None, user_id: str | None) -> None`    @abstractmethod  L98
    - _文档首行_（仅供参考）: Queue a conversation for *immediate* memory update (emergency flush).
    - 分支数 0，函数体节点数 32
  #### `m` `get_context(self, user_id: str | None, *, agent_name: str | None, thread_id: str | None) -> str`    @abstractmethod  L114
    - _文档首行_（仅供参考）: Return injection-ready memory text for the given bucket.
    - 分支数 0，函数体节点数 29
  #### `m` `search(self, query: str, top_k: int, *, user_id: str | None, agent_name: str | None, category: str | None) -> list[dict[str, Any]]`    @abstractmethod  L130
    - _文档首行_（仅供参考）: Search the bucket's memory for facts matching ``query``; return up to
    - 分支数 0，函数体节点数 49
  #### `m` `get_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`    @abstractmethod  L146
    - _文档首行_（仅供参考）: Return the full memory document for the bucket.
    - 分支数 0，函数体节点数 31
  #### `m` `delete_memory(self, *, user_id: str | None, agent_name: str | None) -> None`    @abstractmethod  L155
    - _文档首行_（仅供参考）: Delete the entire memory document for the bucket. *stub* this phase.
    - 分支数 0，函数体节点数 22
  #### `m` `clear_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`    @abstractmethod  L164
    - _文档首行_（仅供参考）: Clear the bucket's memory; return the cleared (now-empty) document.
    - 分支数 0，函数体节点数 31
  #### `m` `import_memory(self, memory_data: dict[str, Any], *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`    @abstractmethod  L173
    - _文档首行_（仅供参考）: Import a memory document into the bucket; return the merged result.
    - 分支数 0，函数体节点数 42
  #### `m` `export_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`    @abstractmethod  L183
    - _文档首行_（仅供参考）: Export the memory document for the bucket. *stub* this phase (no caller yet).
    - 分支数 0，函数体节点数 31
  #### `m` `shutdown_flush(self, timeout: float) -> bool`    @abstractmethod  L193
    - _文档首行_（仅供参考）: Best-effort bounded drain of pending updates on graceful shutdown.
    - 分支数 0，函数体节点数 12

## 文件内调用关系
- `_resolve_manager_class` -> _scan_backends
- `get_memory_manager` -> _resolve_manager_class, _host_default_llm

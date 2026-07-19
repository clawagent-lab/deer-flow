# `backend/packages/harness/deerflow/agents/memory/backends/deermem/deer_mem.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/deermem/deer_mem.py`  ·  行数: 322

**模块文档首行**（仅供参考）: DeerMem -- the default :class:`MemoryManager` backend (self-contained).

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `typing` -> Any
- `deerflow.agents.memory.manager` -> MemoryManager
- `.deermem.config` -> DeerMemConfig
- `.deermem.core.llm` -> build_llm
- `.deermem.core.message_processing` -> detect_correction, detect_reinforcement, filter_messages_for_memory
- `.deermem.core.prompt` -> format_memory_for_injection, warm_tiktoken_cache
- `.deermem.core.queue` -> MemoryUpdateQueue
- `.deermem.core.storage` -> create_storage
- `.deermem.core.updater` -> MemoryUpdater, _coerce_source_confidence

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `DeerMem`  L46
- 继承: MemoryManager
- _文档首行_: Default memory backend: file-backed facts + debounced LLM extraction.
- 方法:
  #### `m` `__init__(self, backend_config: dict[str, Any] | None) -> None`  L49
    - _文档首行_（仅供参考）: Construct DeerMem with its dependencies (dependency injection).
    - 分支数 0，函数体节点数 111
    - 调用: from_backend_config, create_storage, build_llm, MemoryUpdater, MemoryUpdateQueue
  #### `m` `add(self, thread_id: str, messages: list[Any], *, agent_name: str | None, user_id: str | None, trace_id: str | None) -> None`  L67
    - _文档首行_（仅供参考）: Filter, validate, detect signals, then enqueue (debounced).
    - 分支数 1，函数体节点数 94；return: None
    - 调用: _prepare_update, add
  #### `m` `add_nowait(self, thread_id: str, messages: list[Any], *, agent_name: str | None, user_id: str | None) -> None`  L96
    - _文档首行_（仅供参考）: Filter, validate, detect signals, then enqueue for immediate flush.
    - 分支数 1，函数体节点数 84；return: None
    - 调用: _prepare_update, add_nowait
  #### `m` `_prepare_update(self, messages: list[Any]) -> tuple[list[Any], bool, bool] | None`  L122
    - _文档首行_（仅供参考）: Filter to user+final-AI messages, require both, detect signals.
    - 分支数 1，函数体节点数 132；return: None, (filtered, correction_detected, reinforcement_detected)
    - 调用: filter_messages_for_memory, getattr, detect_correction, detect_reinforcement
  - 反射: getattr (L137), getattr (L138)
  #### `m` `get_context(self, user_id: str | None, *, agent_name: str | None, thread_id: str | None) -> str`  L146
    - _文档首行_（仅供参考）: Load memory and format it for injection (plain text, no wrap).
    - 分支数 0，函数体节点数 80；return: format_memory_for_injection(memory_data, max_tokens=self._config.max_injection_tokens, use_tiktoken=self._config.token_counting == 'tiktoken', guaranteed_categories=self._config.guaranteed_categories, guaranteed_token_budget=self._config.guaranteed_token_budget)
    - 调用: get_memory_data, format_memory_for_injection
  #### `m` `search(self, query: str, top_k: int, *, user_id: str | None, agent_name: str | None, category: str | None) -> list[dict[str, Any]]`  L169
    - _文档首行_（仅供参考）: Case-insensitive substring search over stored facts.
    - 分支数 1，函数体节点数 174；return: [], matched[:top_k]
    - 调用: strip, lower, get_memory_data, get, isinstance, sort
  #### `m` `get_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L197
    - 分支数 0，函数体节点数 41；return: self._updater.get_memory_data(agent_name=agent_name, user_id=user_id)
    - 调用: get_memory_data
  #### `m` `delete_memory(self, *, user_id: str | None, agent_name: str | None) -> None`  L205
    - _文档首行_（仅供参考）: Not implemented this phase (storage/updater deletion is a future ``core/`` addition).
    - 分支数 0，函数体节点数 25；raise: NotImplementedError('DeerMem.delete_memory is not implemented yet')
    - 调用: NotImplementedError
  #### `m` `clear_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L214
    - 分支数 0，函数体节点数 41；return: self._updater.clear_memory_data(agent_name=agent_name, user_id=user_id)
    - 调用: clear_memory_data
  #### `m` `import_memory(self, memory_data: dict[str, Any], *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L222
    - 分支数 0，函数体节点数 54；return: self._updater.import_memory_data(memory_data, agent_name=agent_name, user_id=user_id)
    - 调用: import_memory_data
  #### `m` `export_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L231
    - _文档首行_（仅供参考）: Not implemented this phase (no distinct export yet; /export routes via get_memory).
    - 分支数 0，函数体节点数 34；raise: NotImplementedError('DeerMem.export_memory is not implemented yet')
    - 调用: NotImplementedError
  #### `m` `shutdown_flush(self, timeout: float) -> bool`  L241
    - _文档首行_（仅供参考）: Drain the debounce queue within ``timeout`` on graceful shutdown.
    - 分支数 0，函数体节点数 20；return: self._queue.flush_sync(timeout)
    - 调用: flush_sync
  #### `m` `warm(self) -> bool`  L254
    - _文档首行_（仅供参考）: Pre-warm DeerMem-specific resources (the tiktoken encoding cache).
    - 分支数 1，函数体节点数 30；return: True, warm_tiktoken_cache()
    - 调用: info, warm_tiktoken_cache
  #### `m` `reload_memory(self, *, user_id: str | None, agent_name: str | None) -> dict[str, Any]`  L269
    - _文档首行_（仅供参考）: Drop the cached memory document and reload from disk.
    - 分支数 0，函数体节点数 43；return: self._updater.reload_memory_data(agent_name=agent_name, user_id=user_id)
    - 调用: reload_memory_data
  #### `m` `create_fact(self, content: str, category: str, confidence: float, *, agent_name: str | None, user_id: str | None) -> tuple[dict[str, Any], str | None]`  L278
    - 分支数 0，函数体节点数 71；return: self._updater.create_memory_fact(content, category=category, confidence=confidence, agent_name=agent_name, user_id=user_id)
    - 调用: create_memory_fact
  #### `m` `delete_fact(self, fact_id: str, *, agent_name: str | None, user_id: str | None) -> dict[str, Any]`  L295
    - 分支数 0，函数体节点数 46；return: self._updater.delete_memory_fact(fact_id, agent_name=agent_name, user_id=user_id)
    - 调用: delete_memory_fact
  #### `m` `update_fact(self, fact_id: str, content: str | None, category: str | None, confidence: float | None, *, agent_name: str | None, user_id: str | None) -> dict[str, Any]`  L304
    - 分支数 0，函数体节点数 76；return: self._updater.update_memory_fact(fact_id, content=content, category=category, confidence=confidence, agent_name=agent_name, user_id=user_id)
    - 调用: update_memory_fact

## 文件内调用关系
- `DeerMem.add` -> _prepare_update, add
- `DeerMem.add_nowait` -> _prepare_update, add_nowait

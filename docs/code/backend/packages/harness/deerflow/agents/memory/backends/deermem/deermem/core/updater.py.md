# `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/updater.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/updater.py`  ·  行数: 1284

**模块文档首行**（仅供参考）: Memory updater for reading, writing, and updating memory data.

## 模块概览
- 函数 16 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: asyncio, atexit, concurrent.futures, copy, html, json, logging, math, re, uuid
- `datetime` -> UTC, datetime, timedelta
- `typing` -> Any
- `..config` -> DeerMemConfig
- `.prompt` -> CONSOLIDATION_PROMPT, MEMORY_UPDATE_PROMPT, STALENESS_REVIEW_PROMPT, format_conversation_for_update
- `.storage` -> MemoryStorage, create_empty_memory, utc_now_iso_z

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SYNC_MEMORY_UPDATER_EXECUTOR` = concurrent.futures.ThreadPoolExecutor(max_workers=4, thre...
- `_REQUIRED_MEMORY_UPDATE_TOP_LEVEL_KEYS` = frozenset({'user', 'history', 'newFacts'})
- `_UPLOAD_SENTENCE_RE` = re.compile('[^.!?]*\\b(?:upload(?:ed|ing)?(?:\\s+\\w+){0,...

## 函数
#### `ƒ` `_validate_confidence(confidence: float) -> float`  L48
  - _文档首行_（仅供参考）: Validate persisted fact confidence so stored JSON stays standards-compliant.
  - 分支数 1，函数体节点数 39；raise: ValueError('confidence')；return: confidence
  - 调用: isfinite, ValueError

#### `ƒ` `_coerce_source_confidence(fact: dict[str, Any]) -> float`  L55
  - _文档首行_（仅供参考）: Return a stored fact's confidence as a finite float in [0, 1], defaulting to 0.5.
  - 分支数 2，函数体节点数 81；return: 0.5, max(0.0, min(val, 1.0)) if math.isfinite(val) else 0.5
  - 调用: get, isinstance, float, isfinite, max, min

#### `ƒ` `_trim_facts_to_max(facts: list[dict[str, Any]], max_facts: int) -> list[dict[str, Any]]`  L73
  - _文档首行_（仅供参考）: Keep the highest-confidence facts within ``max_facts`` (confidence coerced).
  - 分支数 1，函数体节点数 65；return: facts, sorted(facts, key=_coerce_source_confidence, reverse=True)[:max_facts]
  - 调用: len, sorted

#### `ƒ` `_extract_text(content: Any) -> str`  L89
  - _文档首行_（仅供参考）: Extract plain text from LLM response content (str or list of content blocks).
  - 分支数 7，函数体节点数 149；return: content, '\n'.join(pieces), str(content)
  - 调用: isinstance, append, join, clear, flush_pending_str_parts, get, str

#### `ƒ` `_normalize_memory_update_fact(fact: Any) -> dict[str, Any] | None`  L129
  - _文档首行_（仅供参考）: Normalize a single fact entry from a model-produced memory update.
  - 分支数 13，函数体节点数 298；return: None, normalized_fact
  - 调用: isinstance, get, strip, float, isfinite, int

#### `ƒ` `_normalize_memory_update_data(update_data: dict[str, Any]) -> dict[str, Any]`  L186
  - _文档首行_（仅供参考）: Coerce parsed memory update data into the shape consumed by _apply_updates.
  - 分支数 22，函数体节点数 762；raise: json.JSONDecodeError('Unsafe partial memory update: factsToRemove with malformed newFacts', json.dumps(update_data, ensure_ascii=False), 0)；return: {'user': user if isinstance(user, dict) else {}, 'history': history if isinstance(history, dict) else {}, 'newFacts': normalized_new_facts, 'factsToRemove': normalized_facts_to_remove, 'staleFactsToRemove': normalized_stale_removals, 'staleFactsToExtend': normalized_stale_extensions, 'factsToConsolidate': normalized_consolidation}
  - 调用: get, isinstance, _normalize_memory_update_fact, append, JSONDecodeError, dumps, int, list, fromkeys, len, strip, float, isfinite

#### `ƒ` `_parse_memory_update_response(response_content: Any) -> dict[str, Any]`  L308
  - _文档首行_（仅供参考）: Parse the first valid memory-update JSON object from an LLM response.
  - 分支数 3，函数体节点数 109；raise: json.JSONDecodeError('No valid memory update JSON object found', response_text, 0)；return: _normalize_memory_update_data(parsed)
  - 调用: strip, _extract_text, JSONDecoder, finditer, raw_decode, start, isinstance, issubset, _normalize_memory_update_data, JSONDecodeError

#### `ƒ` `_strip_upload_mentions_from_memory(memory_data: dict[str, Any]) -> dict[str, Any]`  L343
  - _文档首行_（仅供参考）: Remove sentences about file uploads from all memory summaries and facts.
  - 分支数 4，函数体节点数 152；return: memory_data
  - 调用: get, items, isinstance, strip, sub, search

#### `ƒ` `_fact_content_key(content: Any) -> str | None`  L366
  - 分支数 2，函数体节点数 43；return: None, stripped.casefold()
  - 调用: isinstance, strip, casefold

#### `ƒ` `_parse_fact_datetime(raw: str) -> datetime | None`  L378
  - _文档首行_（仅供参考）: Parse an ISO-8601 datetime string from a fact's createdAt field.
  - 分支数 3，函数体节点数 61；return: None, result
  - 调用: fromisoformat, replace
  - 文件IO: replace (L390)

#### `ƒ` `_effective_fact_staleness_age(fact: dict[str, Any], config: Any) -> int`  L396
  - _文档首行_（仅供参考）: Return the effective staleness review age in days for *fact*.
  - 分支数 1，函数体节点数 68；return: int(raw), config.staleness_age_days
  - 调用: get, isinstance, int

#### `ƒ` `_select_stale_candidates(current_memory: dict[str, Any], config: Any) -> list[dict[str, Any]]`  L414
  - _文档首行_（仅供参考）: Return facts that have exceeded their individual review window.
  - 分支数 5，函数体节点数 176；return: candidates
  - 调用: now, frozenset, get, isinstance, _parse_fact_datetime, _effective_fact_staleness_age, timedelta, append

#### `ƒ` `_build_staleness_section(stale_candidates: list[dict[str, Any]], config: Any) -> str`  L445
  - _文档首行_（仅供参考）: Format the staleness review prompt section from candidate facts.
  - 分支数 2，函数体节点数 207；return: '', STALENESS_REVIEW_PROMPT.format(stale_facts='\n'.join(lines))
  - 调用: get, escape, strip, str, _coerce_source_confidence, isinstance, len, _effective_fact_staleness_age, append, format, join

#### `ƒ` `_select_consolidation_candidates(current_memory: dict[str, Any], config: Any) -> dict[str, list[dict[str, Any]]]`  L477
  - _文档首行_（仅供参考）: Return fact categories that exceed the fragmentation threshold.
  - 分支数 4，函数体节点数 195；return: {}, {cat: group for cat, group in by_category.items() if len(group) >= threshold and cat not in protected}
  - 调用: get, isinstance, strip, append, setdefault, set, items, len

#### `ƒ` `_build_consolidation_section(candidates: dict[str, list[dict[str, Any]]], max_groups: int, max_sources: int) -> str`  L503
  - _文档首行_（仅供参考）: Format consolidation candidate groups into the prompt section.
  - 分支数 3，函数体节点数 241；return: '', CONSOLIDATION_PROMPT.format(consolidation_groups='\n\n'.join(parts), max_groups=max_groups)
  - 调用: sorted, items, len, get, _coerce_source_confidence, escape, str, append, min, join, format

#### `ƒ` `_escape_memory_for_prompt(memory: Any) -> Any`  L531
  - _文档首行_（仅供参考）: Return a copy of ``memory`` with every string leaf HTML-escaped.
  - 分支数 3，函数体节点数 77；return: html.escape(memory), {key: _escape_memory_for_prompt(value) for key, value in memory.items()}, [_escape_memory_for_prompt(item) for item in memory], memory
  - 调用: isinstance, escape, _escape_memory_for_prompt, items

## 类
### 类 `MemoryUpdater`  L559
- _文档首行_: Updates memory using LLM based on conversation context.
- 方法:
  #### `m` `__init__(self, config: DeerMemConfig, storage: MemoryStorage, llm: Any)`  L562
    - _文档首行_（仅供参考）: Initialize the memory updater with injected config + storage + llm (DI).
    - 分支数 0，函数体节点数 36
  #### `m` `_save_memory_to_file(self, memory_data: dict[str, Any], agent_name: str | None, *, user_id: str | None) -> bool`  L577
    - _文档首行_（仅供参考）: Persist memory data via the injected storage.
    - 分支数 0，函数体节点数 47；return: self._storage.save(memory_data, agent_name, user_id=user_id)
    - 调用: save
  #### `m` `get_memory_data(self, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L581
    - _文档首行_（仅供参考）: Get the current memory data via the injected storage.
    - 分支数 0，函数体节点数 42；return: self._storage.load(agent_name, user_id=user_id)
    - 调用: load
  #### `m` `reload_memory_data(self, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L585
    - _文档首行_（仅供参考）: Reload memory data via the injected storage.
    - 分支数 0，函数体节点数 42；return: self._storage.reload(agent_name, user_id=user_id)
    - 调用: reload
  #### `m` `import_memory_data(self, memory_data: dict[str, Any], agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L589
    - _文档首行_（仅供参考）: Persist imported memory data via the injected storage.
    - 分支数 1，函数体节点数 75；raise: OSError('Failed to save imported memory data')；return: self._storage.load(agent_name, user_id=user_id)
    - 调用: save, OSError, load
  #### `m` `clear_memory_data(self, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L595
    - _文档首行_（仅供参考）: Clear all stored memory data and persist an empty structure.
    - 分支数 1，函数体节点数 58；raise: OSError('Failed to save cleared memory data')；return: cleared_memory
    - 调用: create_empty_memory, _save_memory_to_file, OSError
  #### `m` `create_memory_fact(self, content: str, category: str, confidence: float, agent_name: str | None, *, user_id: str | None) -> tuple[dict[str, Any], str | None]`  L602
    - _文档首行_（仅供参考）: Create a new fact, persist it, and return ``(updated_memory, fact_id)``.
    - 分支数 2，函数体节点数 243；raise: ValueError('content'), OSError('Failed to save memory data after creating fact')；return: (updated_memory, fact_id if stored else None)
    - 调用: strip, ValueError, _validate_confidence, utc_now_iso_z, get_memory_data, dict, list, get, uuid4, append, _trim_facts_to_max, _save_memory_to_file, OSError, any
  #### `m` `delete_memory_fact(self, fact_id: str, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L646
    - _文档首行_（仅供参考）: Delete a fact by its id and persist the updated memory data.
    - 分支数 2，函数体节点数 140；raise: KeyError(fact_id), OSError(f"Failed to save memory data after deleting fact '{fact_id}'")；return: updated_memory
    - 调用: get_memory_data, get, len, KeyError, dict, _save_memory_to_file, OSError
  #### `m` `update_memory_fact(self, fact_id: str, content: str | None, category: str | None, confidence: float | None, agent_name: str | None, *, user_id: str | None) -> dict[str, Any]`  L659
    - _文档首行_（仅供参考）: Update an existing fact and persist the updated memory data.
    - 分支数 8，函数体节点数 263；raise: ValueError('content'), KeyError(fact_id), OSError(f"Failed to save memory data after updating fact '{fact_id}'")；return: updated_memory
    - 调用: get_memory_data, dict, get, strip, ValueError, _validate_confidence, append, KeyError, _save_memory_to_file, OSError
  #### `m` `_build_correction_hint(self, correction_detected: bool, reinforcement_detected: bool) -> str`  L688
    - _文档首行_（仅供参考）: Build optional prompt hints for correction and reinforcement signals.
    - 分支数 2，函数体节点数 54；return: correction_hint
    - 调用: strip
  #### `m` `_prepare_update_prompt(self, messages: list[Any], agent_name: str | None, correction_detected: bool, reinforcement_detected: bool, user_id: str | None) -> tuple[dict[str, Any], str] | None`  L713
    - _文档首行_（仅供参考）: Load memory and build the update prompt for a conversation.
    - 分支数 6，函数体节点数 234；return: None, (current_memory, prompt)
    - 调用: get_memory_data, format_conversation_for_update, strip, _build_correction_hint, _select_stale_candidates, len, _build_staleness_section, _select_consolidation_candidates, _build_consolidation_section, format, dumps, _escape_memory_for_prompt
  #### `m` `_finalize_update(self, current_memory: dict[str, Any], response_content: Any, thread_id: str | None, agent_name: str | None, user_id: str | None) -> bool`  L763
    - _文档首行_（仅供参考）: Parse the model response, apply updates, and persist memory.
    - 分支数 0，函数体节点数 90；return: self._storage.save(updated_memory, agent_name, user_id=user_id)
    - 调用: _parse_memory_update_response, _apply_updates, deepcopy, _strip_upload_mentions_from_memory, save
  #### `m` `_do_update_memory_sync(self, messages: list[Any], thread_id: str | None, agent_name: str | None, correction_detected: bool, reinforcement_detected: bool, user_id: str | None, trace_id: str | None) -> bool`  L808
    - _文档首行_（仅供参考）: Pure-sync memory update; bind ``trace_id`` into the request-trace
    - 分支数 2，函数体节点数 133；return: self._do_update_memory_sync_impl(messages=messages, thread_id=thread_id, agent_name=agent_name, correction_detected=correction_detected, reinforcement_detected=reinforcement_detected, user_id=user_id, trace_id=trace_id)
    - 调用: cm, _do_update_memory_sync_impl
  #### `m` `_do_update_memory_sync_impl(self, messages: list[Any], thread_id: str | None, agent_name: str | None, correction_detected: bool, reinforcement_detected: bool, user_id: str | None, trace_id: str | None) -> bool`  L851
    - _文档首行_（仅供参考）: Pure-sync memory update using ``model.invoke()``.
    - 分支数 4，函数体节点数 245；raise: RuntimeError('DeerMem memory update requested but no LLM is configured (set memory.backend_config.model in config).')；return: False, self._finalize_update(current_memory=current_memory, response_content=response.content, thread_id=thread_id, agent_name=agent_name, user_id=user_id)
    - 调用: _prepare_update_prompt, RuntimeError, tracing_callback, info, invoke, _finalize_update, warning, exception
  #### `m` `update_memory(self, messages: list[Any], thread_id: str | None, agent_name: str | None, correction_detected: bool, reinforcement_detected: bool, user_id: str | None, trace_id: str | None) -> bool`  L913
    - _文档首行_（仅供参考）: Synchronously update memory using the sync LLM path.
    - 分支数 3，函数体节点数 158；return: future.result(), False, self._do_update_memory_sync(messages=messages, thread_id=thread_id, agent_name=agent_name, correction_detected=correction_detected, reinforcement_detected=reinforcement_detected, user_id=user_id, trace_id=trace_id)
    - 调用: get_running_loop, is_running, submit, result, exception, _do_update_memory_sync
  #### `m` `_apply_updates(self, current_memory: dict[str, Any], update_data: dict[str, Any], thread_id: str | None) -> dict[str, Any]`  L977
    - _文档首行_（仅供参考）: Apply LLM-generated updates to memory.
    - 分支数 38，函数体节点数 1764；return: current_memory
    - 调用: utc_now_iso_z, get, set, isinstance, _select_stale_candidates, len, sort, info, now, int, _parse_fact_datetime, append, total_seconds, min, _fact_content_key, strip, uuid4, add, _trim_facts_to_max, values（+13）
  #### `⏵m` `async aupdate_memory(self, messages: list[Any], thread_id: str | None, agent_name: str | None, correction_detected: bool, reinforcement_detected: bool, user_id: str | None, trace_id: str | None) -> bool`  L779
    - _文档首行_（仅供参考）: Update memory asynchronously by delegating to the sync path.
    - 分支数 0，函数体节点数 82；return: await asyncio.to_thread(self._do_update_memory_sync, messages=messages, thread_id=thread_id, agent_name=agent_name, correction_detected=correction_detected, reinforcement_detected=reinforcement_detected, user_id=user_id, trace_id=trace_id)
    - 调用: to_thread

## 文件内调用关系
- `_normalize_memory_update_data` -> _normalize_memory_update_fact
- `_parse_memory_update_response` -> _extract_text, _normalize_memory_update_data
- `_select_stale_candidates` -> _parse_fact_datetime, _effective_fact_staleness_age
- `_build_staleness_section` -> _coerce_source_confidence, _effective_fact_staleness_age
- `_build_consolidation_section` -> _coerce_source_confidence
- `_escape_memory_for_prompt` -> _escape_memory_for_prompt
- `MemoryUpdater.clear_memory_data` -> _save_memory_to_file
- `MemoryUpdater.create_memory_fact` -> _validate_confidence, get_memory_data, _trim_facts_to_max, _save_memory_to_file
- `MemoryUpdater.delete_memory_fact` -> get_memory_data, _save_memory_to_file
- `MemoryUpdater.update_memory_fact` -> get_memory_data, _validate_confidence, _save_memory_to_file
- `MemoryUpdater._prepare_update_prompt` -> get_memory_data, _build_correction_hint, _select_stale_candidates, _build_staleness_section, _select_consolidation_candidates, _build_consolidation_section, _escape_memory_for_prompt
- `MemoryUpdater._finalize_update` -> _parse_memory_update_response, _apply_updates, _strip_upload_mentions_from_memory
- `MemoryUpdater._do_update_memory_sync` -> _do_update_memory_sync_impl
- `MemoryUpdater._do_update_memory_sync_impl` -> _prepare_update_prompt, _finalize_update
- `MemoryUpdater.update_memory` -> _do_update_memory_sync
- `MemoryUpdater._apply_updates` -> _select_stale_candidates, _parse_fact_datetime, _fact_content_key, _trim_facts_to_max, _select_consolidation_candidates, _coerce_source_confidence

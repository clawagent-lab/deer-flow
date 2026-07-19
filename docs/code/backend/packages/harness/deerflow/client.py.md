# `backend/packages/harness/deerflow/client.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/client.py`  ·  行数: 1531

**模块文档首行**（仅供参考）: DeerFlowClient — Embedded Python client for DeerFlow agent system.

## 模块概览
- 函数 1 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, concurrent.futures, json, logging, mimetypes, os, shutil, tempfile, uuid
- `collections.abc` -> Generator, Sequence
- `dataclasses` -> dataclass, field
- `pathlib` -> Path
- `typing` -> Any, Literal
- `langchain.agents` -> create_agent
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> AIMessage, HumanMessage, SystemMessage, ToolMessage
- `langchain_core.runnables` -> RunnableConfig
- `deerflow.agents.lead_agent.agent` -> build_middlewares
- `deerflow.agents.lead_agent.prompt` -> apply_prompt_template, get_enabled_skills_for_config
- `deerflow.agents.thread_state` -> ThreadState
- `deerflow.config.agents_config` -> AGENT_NAME_PATTERN
- `deerflow.config.app_config` -> get_app_config, is_trace_correlation_enabled, reload_app_config
- `deerflow.config.extensions_config` -> ExtensionsConfig, SkillStateConfig, get_extensions_config, reload_extensions_config
- `deerflow.config.paths` -> get_paths
- `deerflow.models` -> create_chat_model
- `deerflow.runtime.goal` -> DEFAULT_MAX_GOAL_CONTINUATIONS, build_goal_state, goal_thread_lock, read_thread_goal, write_thread_goal
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.skills.describe` -> build_skill_search_setup
- `deerflow.skills.storage` -> get_or_new_user_skill_storage
- `deerflow.tools.builtins.tool_search` -> assemble_deferred_tools, build_mcp_routing_middleware, get_mcp_routing_hints_prompt_section
- `deerflow.trace_context` -> DEERFLOW_TRACE_METADATA_KEY, generate_trace_id, get_current_trace_id, reset_current_trace_id, set_current_trace_id
- `deerflow.tracing` -> build_tracing_callbacks, inject_langfuse_metadata
- `deerflow.uploads.manager` -> claim_unique_filename, delete_file_safe, enrich_file_listing, ensure_uploads_dir, get_uploads_dir, list_files_in_dir, upload_artifact_url, upload_virtual_path

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `StreamEventType` = Literal['values', 'messages-tuple', 'custom', 'end']

## 函数
#### `ƒ` `_run_async_from_sync(coro)`  L66
  - _文档首行_（仅供参考）: Run an async helper from this synchronous client API.
  - 分支数 3，函数体节点数 70；return: executor.submit(asyncio.run, coro).result(), asyncio.run(coro)
  - 调用: get_running_loop, is_running, ThreadPoolExecutor, result, submit, run
  - 子进程: run (L76)

## 类
### 类 `StreamEvent`  L83  @dataclass
- _文档首行_: A single event from the streaming agent response.
- 类/实例变量:
  - `type` = <annotated>
  - `data` = field(default_factory=dict)

### 类 `DeerFlowClient`  L100
- _文档首行_: Embedded Python client for DeerFlow agent system.
- 方法:
  #### `st` `_atomic_write_json(path: Path, data: dict) -> None`    @staticmethod  L207
    - _文档首行_（仅供参考）: Write JSON to *path* atomically (temp file + replace).
    - 分支数 1，函数体节点数 87；raise: bare raise
    - 调用: NamedTemporaryFile, dump, close, replace, Path, unlink
  - 文件IO: replace (L218), unlink (L221)
  #### `st` `_get_tools(*, model_name: str | None, subagent_enabled: bool)`    @staticmethod  L327
    - _文档首行_（仅供参考）: Lazy import to avoid circular dependency at module level.
    - 分支数 0，函数体节点数 27；return: get_available_tools(model_name=model_name, subagent_enabled=subagent_enabled)
    - 调用: get_available_tools
  #### `st` `_serialize_tool_calls(tool_calls) -> list[dict]`    @staticmethod  L334
    - _文档首行_（仅供参考）: Reshape LangChain tool_calls into the wire format used in events.
    - 分支数 0，函数体节点数 40；return: [{'name': tc['name'], 'args': tc['args'], 'id': tc.get('id')} for tc in tool_calls]
    - 调用: get
  #### `st` `_serialize_additional_kwargs(msg) -> dict[str, Any] | None`    @staticmethod  L339
    - _文档首行_（仅供参考）: Copy message additional_kwargs when present.
    - 分支数 1，函数体节点数 50；return: dict(additional_kwargs), None
    - 调用: getattr, isinstance, dict
  - 反射: getattr (L341)
  #### `st` `_ai_text_event(msg_id: str | None, text: str, usage: dict | None, additional_kwargs: dict[str, Any] | None) -> 'StreamEvent'`    @staticmethod  L347
    - _文档首行_（仅供参考）: Build a ``messages-tuple`` AI text event.
    - 分支数 2，函数体节点数 90；return: StreamEvent(type='messages-tuple', data=data)
    - 调用: StreamEvent
  #### `st` `_ai_tool_calls_event(msg_id: str | None, tool_calls, additional_kwargs: dict[str, Any] | None) -> 'StreamEvent'`    @staticmethod  L357
    - _文档首行_（仅供参考）: Build a ``messages-tuple`` AI tool-calls event.
    - 分支数 1，函数体节点数 78；return: StreamEvent(type='messages-tuple', data=data)
    - 调用: _serialize_tool_calls, StreamEvent
  #### `st` `_tool_message_event(msg: ToolMessage) -> 'StreamEvent'`    @staticmethod  L370
    - _文档首行_（仅供参考）: Build a ``messages-tuple`` tool-result event from a ToolMessage.
    - 分支数 0，函数体节点数 45；return: StreamEvent(type='messages-tuple', data={'type': 'tool', 'content': DeerFlowClient._extract_text(msg.content), 'name': msg.name, 'tool_call_id': msg.tool_call_id, 'id': msg.id})
    - 调用: StreamEvent, _extract_text
  #### `st` `_serialize_message(msg) -> dict`    @staticmethod  L384
    - _文档首行_（仅供参考）: Serialize a LangChain message to a plain dict for values events.
    - 分支数 10，函数体节点数 292；return: d, {'type': 'unknown', 'content': str(msg), 'id': getattr(msg, 'id', None)}
    - 调用: isinstance, getattr, _serialize_tool_calls, _serialize_additional_kwargs, _extract_text, str
  - 反射: getattr (L387), getattr (L390), getattr (L399), getattr (L400), getattr (L401), getattr (L407), getattr (L412), getattr (L416)
  #### `st` `_extract_text(content) -> str`    @staticmethod  L419
    - _文档首行_（仅供参考）: Extract plain text from AIMessage content (str or list of blocks).
    - 分支数 8，函数体节点数 243；return: content, ''.join(content) if chunk_like else '\n'.join(content), '\n'.join(pieces) if pieces else '', str(content)
    - 调用: isinstance, all, len, any, join, append, clear, flush_pending_str_parts, get, str
  #### `m` `__init__(self, config_path: str | None, checkpointer, *, model_name: str | None, thinking_enabled: bool, subagent_enabled: bool, plan_mode: bool, agent_name: str | None, available_skills: set[str] | None, middlewares: Sequence[AgentMiddleware] | None, environment: str | None)`  L134
    - _文档首行_（仅供参考）: Initialize the client.
    - 分支数 2，函数体节点数 219；raise: ValueError(f"Invalid agent name '{agent_name}'. Must match pattern: {AGENT_NAME_PATTERN.pattern}")
    - 调用: reload_app_config, get_app_config, match, ValueError, set, list
  #### `m` `reset_agent(self) -> None`  L192
    - _文档首行_（仅供参考）: Force the internal agent to be recreated on the next call.
    - 分支数 0，函数体节点数 18
  #### `m` `_get_runnable_config(self, thread_id: str, **overrides) -> RunnableConfig`  L224
    - _文档首行_（仅供参考）: Build a RunnableConfig for agent invocation.
    - 分支数 0，函数体节点数 77；可变参数（*args/**kwargs）；return: RunnableConfig(configurable=configurable, recursion_limit=overrides.get('recursion_limit', 100))
    - 调用: get, RunnableConfig
  #### `m` `_ensure_agent(self, config: RunnableConfig)`  L238
    - _文档首行_（仅供参考）: Create (or recreate) the agent when config-dependent params change.
    - 分支数 5，函数体节点数 488；return: None
    - 调用: get, frozenset, _get_tools, assemble_deferred_tools, build_mcp_routing_middleware, get_mcp_routing_hints_prompt_section, get_enabled_skills_for_config, build_skill_search_setup, append, create_chat_model, build_middlewares, get_effective_user_id, apply_prompt_template, get_checkpointer, create_agent, info
  #### `m` `_get_thread_checkpointer(self)`  L459
    - 分支数 1，函数体节点数 27；return: checkpointer
    - 调用: get_checkpointer
  #### `m` `get_goal(self, thread_id: str) -> dict`  L467
    - _文档首行_（仅供参考）: Return the active goal for a thread, if any.
    - 分支数 0，函数体节点数 36；return: {'goal': goal}
    - 调用: _get_thread_checkpointer, _run_async_from_sync, read_thread_goal
  #### `m` `set_goal(self, thread_id: str, objective: str, *, max_continuations: int) -> dict`  L473
    - _文档首行_（仅供参考）: Set or replace a thread-scoped goal.
    - 分支数 1，函数体节点数 72；return: {'goal': goal}
    - 调用: _get_thread_checkpointer, build_goal_state, goal_thread_lock, write_thread_goal, _run_async_from_sync, _set_goal
  #### `m` `clear_goal(self, thread_id: str) -> dict`  L491
    - _文档首行_（仅供参考）: Clear the active goal for a thread.
    - 分支数 2，函数体节点数 54；return: {'goal': None}
    - 调用: _get_thread_checkpointer, goal_thread_lock, write_thread_goal, _run_async_from_sync, _clear_goal
  #### `m` `list_threads(self, limit: int) -> dict`  L505
    - _文档首行_（仅供参考）: List the recent N threads.
    - 分支数 6，函数体节点数 293；return: {'thread_list': threads[:limit]}
    - 调用: _get_thread_checkpointer, list, get, values, sort
  #### `m` `get_thread(self, thread_id: str) -> dict`  L557
    - _文档首行_（仅供参考）: Get the complete thread record, including all node execution records.
    - 分支数 2，函数体节点数 224；return: {'thread_id': thread_id, 'checkpoints': checkpoints}
    - 调用: _get_thread_checkpointer, list, dict, get, hasattr, _serialize_message, append, getattr, sort
  - 反射: hasattr (L574), getattr (L586)
  #### `m` `stream(self, message: str, *, thread_id: str | None, **kwargs) -> Generator[StreamEvent, None, None]`  L599
    - _文档首行_（仅供参考）: Stream a conversation turn with a DeerFlow request trace context.
    - 分支数 6，函数体节点数 138；生成器（yield）；可变参数（*args/**kwargs）；return: None
    - 调用: is_trace_correlation_enabled, get_current_trace_id, generate_trace_id, _stream_without_trace_context, object, set_current_trace_id, next, reset_current_trace_id, close
  #### `m` `_stream_without_trace_context(self, message: str, *, thread_id: str | None, **kwargs) -> Generator[StreamEvent, None, None]`  L654
    - _文档首行_（仅供参考）: Stream a conversation turn, yielding events incrementally.
    - 分支数 34，函数体节点数 1214；生成器（yield）；可变参数（*args/**kwargs）；return: None, {'input_tokens': input_tokens, 'output_tokens': output_tokens, 'total_tokens': total_tokens}, additional_kwargs, delta
    - 调用: str, uuid4, _get_runnable_config, build_tracing_callbacks, list, get, get_current_trace_id, inject_langfuse_metadata, get_effective_user_id, _ensure_agent, HumanMessage, set, add, setdefault, items, update, stream, isinstance, len, getattr（+5）
  - 反射: getattr (L848), getattr (L888), getattr (L898)
  #### `m` `chat(self, message: str, *, thread_id: str | None, **kwargs) -> str`  L954
    - _文档首行_（仅供参考）: Send a message and return the final text response.
    - 分支数 3，函数体节点数 142；可变参数（*args/**kwargs）；return: ''.join(chunks.get(last_id, ()))
    - 调用: stream, get, append, setdefault, join
  #### `m` `list_models(self) -> dict`  L990
    - _文档首行_（仅供参考）: List available models from configuration.
    - 分支数 1，函数体节点数 102；return: {'models': [{'name': model.name, 'model': getattr(model, 'model', None), 'display_name': getattr(model, 'display_name', None), 'description': getattr(model, 'description', None), 'supports_thinking': getattr(model, 'supports_thinking', False), 'supports_reasoning_effort': getattr(model, 'supports_reasoning_effort', False)} for model in self._app_config.models], 'token_usage': {'enabled': token_usage_enabled}}
    - 调用: getattr, isinstance
  - 反射: getattr (L997), getattr (L997), getattr (L1005), getattr (L1006), getattr (L1007), getattr (L1008), getattr (L1009)
  #### `m` `list_skills(self, enabled_only: bool) -> dict`  L1016
    - _文档首行_（仅供参考）: List available skills.
    - 分支数 0，函数体节点数 66；return: {'skills': [{'name': s.name, 'description': s.description, 'license': s.license, 'category': s.category, 'enabled': s.enabled} for s in storage.load_skills(enabled_only=enabled_only)]}
    - 调用: get_or_new_user_skill_storage, get_effective_user_id, load_skills
  #### `m` `get_memory(self) -> dict`  L1040
    - _文档首行_（仅供参考）: Get current memory data.
    - 分支数 0，函数体节点数 20；return: get_memory_manager().get_memory(user_id=get_effective_user_id())
    - 调用: get_memory, get_memory_manager, get_effective_user_id
  #### `m` `export_memory(self) -> dict`  L1050
    - _文档首行_（仅供参考）: Export current memory data for backup or transfer.
    - 分支数 0，函数体节点数 20；return: get_memory_manager().get_memory(user_id=get_effective_user_id())
    - 调用: get_memory, get_memory_manager, get_effective_user_id
  #### `m` `import_memory(self, memory_data: dict) -> dict`  L1056
    - _文档首行_（仅供参考）: Import and persist full memory data.
    - 分支数 0，函数体节点数 25；return: get_memory_manager().import_memory(memory_data, user_id=get_effective_user_id())
    - 调用: import_memory, get_memory_manager, get_effective_user_id
  #### `m` `get_model(self, name: str) -> dict | None`  L1062
    - _文档首行_（仅供参考）: Get a specific model's configuration by name.
    - 分支数 1，函数体节点数 80；return: None, {'name': model.name, 'model': getattr(model, 'model', None), 'display_name': getattr(model, 'display_name', None), 'description': getattr(model, 'description', None), 'supports_thinking': getattr(model, 'supports_thinking', False), 'supports_reasoning_effort': getattr(model, 'supports_reasoning_effort', False)}
    - 调用: get_model_config, getattr
  - 反射: getattr (L1077), getattr (L1078), getattr (L1079), getattr (L1080), getattr (L1081)
  #### `m` `get_mcp_config(self) -> dict`  L1088
    - _文档首行_（仅供参考）: Get MCP server configurations.
    - 分支数 0，函数体节点数 38；return: {'mcp_servers': {name: server.model_dump() for name, server in config.mcp_servers.items()}}
    - 调用: get_extensions_config, model_dump, items
  #### `m` `update_mcp_config(self, mcp_servers: dict[str, dict]) -> dict`  L1098
    - _文档首行_（仅供参考）: Update MCP server configurations.
    - 分支数 1，函数体节点数 127；raise: FileNotFoundError('Cannot locate extensions_config.json. Set DEER_FLOW_EXTENSIONS_CONFIG_PATH or ensure it exists in the project root.')；return: {'mcp_servers': {name: server.model_dump() for name, server in reloaded.mcp_servers.items()}}
    - 调用: resolve_config_path, FileNotFoundError, get_extensions_config, items, _atomic_write_json, reload_extensions_config, model_dump
  #### `m` `get_skill(self, name: str) -> dict | None`  L1136
    - _文档首行_（仅供参考）: Get a specific skill by name.
    - 分支数 1，函数体节点数 90；return: None, {'name': skill.name, 'description': skill.description, 'license': skill.license, 'category': skill.category, 'enabled': skill.enabled}
    - 调用: get_or_new_user_skill_storage, get_effective_user_id, next, load_skills
  #### `m` `update_skill(self, name: str, *, enabled: bool) -> dict`  L1157
    - _文档首行_（仅供参考）: Update a skill's enabled status.
    - 分支数 8，函数体节点数 469；raise: ValueError(f"Skill '{name}' not found"), FileNotFoundError('Cannot locate extensions_config.json. Set DEER_FLOW_EXTENSIONS_CONFIG_PATH or ensure it exists in the project root.'), RuntimeError(f"Skill '{name}' disappeared after update")；return: {'name': updated.name, 'description': updated.description, 'license': updated.license, 'category': updated.category, 'enabled': updated.enabled}
    - 调用: get_or_new_user_skill_storage, get_effective_user_id, load_skills, next, ValueError, resolve_config_path, FileNotFoundError, get_extensions_config, SkillStateConfig, model_dump, items, _atomic_write_json, reload_extensions_config, isinstance, set_skill_enabled_state, hasattr, clear_skills_system_prompt_cache, invalidate_user_skill_cache, warning, getLogger（+1）
  - 反射: hasattr (L1224)
  #### `m` `install_skill(self, skill_path: str | Path) -> dict`  L1251
    - _文档首行_（仅供参考）: Install a skill from a .skill archive (ZIP).
    - 分支数 0，函数体节点数 31；return: get_or_new_user_skill_storage(get_effective_user_id(), app_config=self._app_config).install_skill_from_archive(skill_path)
    - 调用: install_skill_from_archive, get_or_new_user_skill_storage, get_effective_user_id
  #### `m` `reload_memory(self) -> dict`  L1270
    - _文档首行_（仅供参考）: Reload memory data from file, forcing cache invalidation.
    - 分支数 1，函数体节点数 42；return: manager.reload_memory(user_id=get_effective_user_id()), manager.get_memory(user_id=get_effective_user_id())
    - 调用: get_memory_manager, hasattr, reload_memory, get_effective_user_id, get_memory
  - 反射: hasattr (L1279)
  #### `m` `clear_memory(self) -> dict`  L1284
    - _文档首行_（仅供参考）: Clear all persisted memory data.
    - 分支数 0，函数体节点数 20；return: get_memory_manager().clear_memory(user_id=get_effective_user_id())
    - 调用: clear_memory, get_memory_manager, get_effective_user_id
  #### `m` `create_memory_fact(self, content: str, category: str, confidence: float) -> dict`  L1290
    - _文档首行_（仅供参考）: Create a single fact manually.
    - 分支数 2，函数体节点数 89；raise: NotImplementedError(f"create_fact not supported by memory backend '{type(manager).__name__}'"), ValueError('Fact was not stored because memory.max_facts kept higher-confidence facts')；return: memory_data
    - 调用: get_memory_manager, hasattr, NotImplementedError, type, create_fact, get_effective_user_id, ValueError
  - 反射: hasattr (L1295)
  #### `m` `delete_memory_fact(self, fact_id: str) -> dict`  L1302
    - _文档首行_（仅供参考）: Delete a single fact from memory by fact id.
    - 分支数 1，函数体节点数 54；raise: NotImplementedError(f"delete_fact not supported by memory backend '{type(manager).__name__}'")；return: manager.delete_fact(fact_id, user_id=get_effective_user_id())
    - 调用: get_memory_manager, hasattr, NotImplementedError, type, delete_fact, get_effective_user_id
  - 反射: hasattr (L1307)
  #### `m` `update_memory_fact(self, fact_id: str, content: str | None, category: str | None, confidence: float | None) -> dict`  L1311
    - _文档首行_（仅供参考）: Update a single fact manually, preserving omitted fields.
    - 分支数 1，函数体节点数 85；raise: NotImplementedError(f"update_fact not supported by memory backend '{type(manager).__name__}'")；return: manager.update_fact(fact_id=fact_id, content=content, category=category, confidence=confidence, user_id=get_effective_user_id())
    - 调用: get_memory_manager, hasattr, NotImplementedError, type, update_fact, get_effective_user_id
  - 反射: hasattr (L1322)
  #### `m` `get_memory_config(self) -> dict`  L1332
    - _文档首行_（仅供参考）: Get memory system configuration.
    - 分支数 0，函数体节点数 47；return: {'enabled': config.enabled, 'mode': config.mode, 'injection_enabled': config.injection_enabled, 'shutdown_flush_timeout_seconds': config.shutdown_flush_timeout_seconds, 'manager_class': config.manager_class, 'backend_config': config.backend_config}
    - 调用: get_memory_config
  #### `m` `get_memory_status(self) -> dict`  L1350
    - _文档首行_（仅供参考）: Get memory status: config + current data.
    - 分支数 0，函数体节点数 21；return: {'config': self.get_memory_config(), 'data': self.get_memory()}
    - 调用: get_memory_config, get_memory
  #### `m` `upload_files(self, thread_id: str, files: list[str | Path]) -> dict`  L1365
    - _文档首行_（仅供参考）: Upload local files into a thread's uploads directory.
    - 分支数 14，函数体节点数 468；raise: FileNotFoundError(f'File not found: {f}'), ValueError(f'Path is not a file: {f}')；return: asyncio.run(convert_file_to_markdown(path)), {'success': True, 'files': uploaded_files, 'message': f'Successfully uploaded {len(uploaded_files)} file(s)'}
    - 调用: set, Path, exists, FileNotFoundError, is_file, ValueError, claim_unique_filename, append, lower, ensure_uploads_dir, get_running_loop, ThreadPoolExecutor, run, convert_file_to_markdown, copy2, stat, str, upload_virtual_path, upload_artifact_url, result（+4）
  - 文件IO: exists (L1390), stat (L1425)
  - 子进程: run (L1416), run (L1438)
  #### `m` `list_uploads(self, thread_id: str) -> dict`  L1464
    - _文档首行_（仅供参考）: List files in a thread's uploads directory.
    - 分支数 0，函数体节点数 34；return: enrich_file_listing(result, thread_id)
    - 调用: get_uploads_dir, list_files_in_dir, enrich_file_listing
  #### `m` `delete_upload(self, thread_id: str, filename: str) -> dict`  L1478
    - _文档首行_（仅供参考）: Delete a file from a thread's uploads directory.
    - 分支数 0，函数体节点数 34；return: delete_file_safe(uploads_dir, filename, convertible_extensions=CONVERTIBLE_EXTENSIONS)
    - 调用: get_uploads_dir, delete_file_safe
  #### `m` `get_artifact(self, thread_id: str, path: str) -> tuple[bytes, str]`  L1502
    - _文档首行_（仅供参考）: Read an artifact file produced by the agent.
    - 分支数 4，函数体节点数 122；raise: PathTraversalError('Path traversal detected'), bare raise, FileNotFoundError(f'Artifact not found: {path}'), ValueError(f'Path is not a file: {path}')；return: (actual.read_bytes(), mime_type or 'application/octet-stream')
    - 调用: resolve_virtual_path, get_paths, get_effective_user_id, str, PathTraversalError, exists, FileNotFoundError, is_file, ValueError, guess_type, read_bytes
  - 文件IO: exists (L1524), read_bytes (L1530)

## 文件内调用关系
- `DeerFlowClient._ensure_agent` -> _get_tools
- `DeerFlowClient._ai_tool_calls_event` -> _serialize_tool_calls
- `DeerFlowClient._tool_message_event` -> _extract_text
- `DeerFlowClient._serialize_message` -> _serialize_tool_calls, _serialize_additional_kwargs, _extract_text
- `DeerFlowClient.get_goal` -> _get_thread_checkpointer, _run_async_from_sync
- `DeerFlowClient.set_goal` -> _get_thread_checkpointer, _run_async_from_sync
- `DeerFlowClient.clear_goal` -> _get_thread_checkpointer, _run_async_from_sync
- `DeerFlowClient.list_threads` -> _get_thread_checkpointer
- `DeerFlowClient.get_thread` -> _get_thread_checkpointer, _serialize_message
- `DeerFlowClient.stream` -> _stream_without_trace_context
- `DeerFlowClient._stream_without_trace_context` -> _get_runnable_config, _ensure_agent, stream, _extract_text, _serialize_additional_kwargs
- `DeerFlowClient.chat` -> stream
- `DeerFlowClient.get_memory` -> get_memory
- `DeerFlowClient.export_memory` -> get_memory
- `DeerFlowClient.import_memory` -> import_memory
- `DeerFlowClient.update_mcp_config` -> _atomic_write_json
- `DeerFlowClient.update_skill` -> _atomic_write_json
- `DeerFlowClient.reload_memory` -> reload_memory, get_memory
- `DeerFlowClient.clear_memory` -> clear_memory
- `DeerFlowClient.get_memory_config` -> get_memory_config
- `DeerFlowClient.get_memory_status` -> get_memory_config, get_memory

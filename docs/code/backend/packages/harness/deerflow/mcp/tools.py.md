# `backend/packages/harness/deerflow/mcp/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/mcp/tools.py`  ·  行数: 714

**模块文档首行**（仅供参考）: Load MCP tools using langchain-mcp-adapters with stdio session pooling.

## 模块概览
- 函数 12 个，类 0 个，模块级常量 6 个

## 依赖（import）
- 模块: asyncio, logging, re
- `__future__` -> annotations
- `collections.abc` -> Iterable, Mapping
- `datetime` -> timedelta
- `pathlib` -> Path
- `typing` -> Any
- `urllib.parse` -> unquote, urlparse
- `langchain_core.tools` -> BaseTool, StructuredTool
- `langgraph.config` -> get_config
- `deerflow.config.extensions_config` -> ExtensionsConfig, resolve_effective_mcp_routing
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX, Paths, get_paths
- `deerflow.mcp.client` -> build_servers_config
- `deerflow.mcp.oauth` -> build_oauth_tool_interceptor, get_initial_oauth_headers
- `deerflow.mcp.session_pool` -> get_session_pool
- `deerflow.reflection` -> resolve_variable
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.tools.mcp_metadata` -> tag_mcp_routing, tag_mcp_tool
- `deerflow.tools.sync` -> make_sync_tool_wrapper
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_VALID_MCP_TOOL_NAME` = re.compile('^[A-Za-z0-9_-]+$')
- `_MCP_TMP_SUBDIR` = '.mcp/tmp'
- `_LOCAL_PATH_IN_TEXT_RE` = re.compile('(?:file://)?/[^\\s\'\\"<>|*?]+|(?:\\.{0,2}/|[...
- `_TEXT_PATH_TRAILING_CHARS` = '.,;:!?)]}>"\'`'
- `_FILE_SNAPSHOT` = dict[Path, tuple[int, int]]

## 函数
#### `ƒ` `_local_path_from_uri(uri: str, *, base_dir: Path | None) -> Path | None`  L63
  - _文档首行_（仅供参考）: Return an absolute local filesystem ``Path`` if *uri* points to a local
  - 分支数 6，函数体节点数 110；return: None, path
  - 调用: urlparse, unquote, Path, is_absolute

#### `ƒ` `_local_uri_to_virtual_path(uri: str, *, thread_id: str, user_id: str, source_base_dir: Path | None) -> str | None`  L90
  - _文档首行_（仅供参考）: Translate a local file reference into its ``/mnt/user-data/...`` virtual path.
  - 分支数 5，函数体节点数 144；return: None, virtual_path
  - 调用: _local_path_from_uri, resolve, is_file, sandbox_user_data_dir, get_paths, relative_to, debug, as_posix

#### `ƒ` `_snapshot_workspace_files(root: Path) -> _FILE_SNAPSHOT`  L140
  - _文档首行_（仅供参考）: Return a lightweight snapshot of regular files under *root*.
  - 分支数 5，函数体节点数 86；return: snapshot
  - 调用: exists, rglob, stat, is_file
  - 文件IO: exists (L143), rglob (L147), stat (L150)

#### `ƒ` `_changed_workspace_files(root: Path, before: _FILE_SNAPSHOT) -> list[Path]`  L160
  - _文档首行_（仅供参考）: Return files under *root* that were created or modified since *before*.
  - 分支数 0，函数体节点数 51；return: [path for path, signature in after.items() if before.get(path) != signature]
  - 调用: _snapshot_workspace_files, items, get

#### `ƒ` `_prepare_stdio_workspace(paths: Paths, *, thread_id: str, user_id: str) -> tuple[Path, Path, _FILE_SNAPSHOT]`  L166
  - _文档首行_（仅供参考）: Prepare the thread workspace for a pinned stdio MCP subprocess.
  - 分支数 1，函数体节点数 107；return: (source_base_dir, tmp_dir, before_files)
  - 调用: ensure_thread_dirs, sandbox_work_dir, mkdir, chmod, warning, _snapshot_workspace_files
  - 文件IO: mkdir (L178), chmod (L179)

#### `ƒ` `_result_has_text_content(call_tool_result: Any) -> bool`  L186
  - _文档首行_（仅供参考）: Return ``True`` when the MCP result carries any text content.
  - 分支数 4，函数体节点数 68；return: False, True
  - 调用: getattr, isinstance
  - 反射: getattr (L195)

#### `ƒ` `_rewrite_unique_bare_filenames(text: str, *, changed_files: Iterable[Path], thread_id: str, user_id: str, source_base_dir: Path | None) -> str`  L206
  - _文档首行_（仅供参考）: Rewrite bare filenames only when this call produced a unique match.
  - 分支数 6，函数体节点数 243；return: text, rewritten
  - 调用: _local_uri_to_virtual_path, str, append, setdefault, items, len, set, debug, sorted, compile, escape, subn
  - 危险执行: compile (L245)

#### `ƒ` `_rewrite_local_paths_in_text(text: str, *, thread_id: str, user_id: str, source_base_dir: Path | None, changed_files: Iterable[Path] | None) -> str`  L253
  - _文档首行_（仅供参考）: Best-effort rewrite of local file references found in free text.
  - 分支数 3，函数体节点数 188；return: token, f'{rewritten}{trailing}', rewritten, _rewrite_unique_bare_filenames(rewritten, changed_files=changed_files, thread_id=thread_id, user_id=user_id, source_base_dir=source_base_dir)
  - 调用: group, rstrip, len, _local_uri_to_virtual_path, sub, _rewrite_unique_bare_filenames

#### `ƒ` `_extract_thread_id(runtime: Runtime | None) -> str`  L304
  - _文档首行_（仅供参考）: Extract thread_id from the injected tool runtime or LangGraph config.
  - 分支数 4，函数体节点数 117；return: str(tid), str(tid) if tid is not None else 'default', 'default'
  - 调用: get, str, get_config

#### `ƒ` `_convert_call_tool_result(call_tool_result: Any, *, thread_id: str | None, user_id: str | None, source_base_dir: Path | None, changed_files: Iterable[Path] | None) -> Any`  L322
  - _文档首行_（仅供参考）: Convert an MCP CallToolResult to the LangChain ``content_and_artifact`` format.
  - 分支数 16，函数体节点数 536；raise: ToolException('\n'.join(error_parts) if error_parts else str(lc_content))；return: (call_tool_result, None), uri, rewritten if rewritten is not None else uri, text, _rewrite_local_paths_in_text(text, thread_id=thread_id, user_id=user_id, source_base_dir=source_base_dir, changed_files=changed_files), (lc_content, artifact)
  - 调用: isinstance, _local_uri_to_virtual_path, _rewrite_local_paths_in_text, append, create_text_block, _resolve_text, create_image_block, _resolve_link_url, str, startswith, create_file_block, get, ToolException, join

#### `ƒ` `_make_session_pool_tool(tool: BaseTool, server_name: str, connection: dict[str, Any], tool_interceptors: list[Any] | None, tool_call_timeout: float | None) -> BaseTool`  L425
  - _文档首行_（仅供参考）: Wrap an MCP tool so it reuses a persistent session from the pool.
  - 分支数 8，函数体节点数 613；return: await session.call_tool(request.name, request.args, **kwargs), await _i(req, _h), await asyncio.to_thread(_convert_call_tool_result, call_tool_result, thread_id=thread_id, user_id=user_id, source_base_dir=process_cwd, changed_files=changed_files), StructuredTool(name=tool.name, description=tool.description, args_schema=tool.args_schema, coroutine=call_with_persistent_session, response_format='content_and_artifact', metadata=tool.metadata)
  - 调用: startswith, len, get_session_pool, _extract_thread_id, resolve_runtime_user_id, dict, get, get_paths, to_thread, str, Path, setdefault, get_session, timedelta, isinstance, warning, type, call_tool, reversed, _i（+4）

#### `⏵ƒ` `async get_mcp_tools() -> list[BaseTool]`  L569
  - _文档首行_（仅供参考）: Get all tools from enabled MCP servers.
  - 分支数 23，函数体节点数 781；return: [], await client.get_tools(server_name=server_name), wrapped_tools
  - 调用: warning, from_file, build_servers_config, info, len, get_initial_oauth_headers, items, get, dict, build_oauth_tool_interceptor, append, isinstance, type, resolve_variable, builder, callable, MultiServerMCPClient, get_tools, gather, load_server_tools（+11）
  - 反射: getattr (L706), getattr (L706)

## 文件内调用关系
- `_local_uri_to_virtual_path` -> _local_path_from_uri
- `_changed_workspace_files` -> _snapshot_workspace_files
- `_prepare_stdio_workspace` -> _snapshot_workspace_files
- `_rewrite_unique_bare_filenames` -> _local_uri_to_virtual_path
- `_rewrite_local_paths_in_text` -> _local_uri_to_virtual_path, _rewrite_unique_bare_filenames
- `_convert_call_tool_result` -> _local_uri_to_virtual_path, _rewrite_local_paths_in_text
- `_make_session_pool_tool` -> _extract_thread_id, _result_has_text_content
- `get_mcp_tools` -> _make_session_pool_tool

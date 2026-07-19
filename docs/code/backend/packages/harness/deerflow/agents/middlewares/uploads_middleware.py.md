# `backend/packages/harness/deerflow/agents/middlewares/uploads_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/uploads_middleware.py`  ·  行数: 450

**模块文档首行**（仅供参考）: Middleware to inject uploaded files information into agent context.

## 模块概览
- 函数 4 个，类 2 个，模块级常量 4 个

## 依赖（import）
- 模块: logging, re
- `collections` -> Counter
- `pathlib` -> Path
- `typing` -> NotRequired, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> HumanMessage
- `langchain_core.runnables` -> run_in_executor
- `langgraph.runtime` -> Runtime
- `deerflow.config.paths` -> Paths, get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.uploads.manager` -> is_upload_staging_file
- `deerflow.utils.file_conversion` -> extract_outline
- `deerflow.utils.messages` -> ORIGINAL_USER_CONTENT_KEY, get_original_user_content_text, message_content_to_text

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_OUTLINE_PREVIEW_LINES` = 5
- `_MAX_FILES_PER_CONTEXT_SECTION` = 10
- `_QUERY_TOKEN_RE` = re.compile('[a-z0-9]+')

## 函数
#### `ƒ` `_extension_label(file: dict) -> str`  L29
  - 分支数 0，函数体节点数 47；return: extension or '(no extension)'
  - 调用: lower, str, get, Path

#### `ƒ` `_format_omitted_file_types(files: list[dict]) -> str`  L34
  - 分支数 0，函数体节点数 62；return: ', '.join(parts)
  - 调用: Counter, _extension_label, sorted, items, join

#### `ƒ` `_query_match_strength(file: dict, query_text: str) -> int`  L40
  - 分支数 7，函数体节点数 178；return: 0, 3, 2, 1
  - 调用: lower, str, get, Path, _extension_label, startswith, len, findall, search, escape

#### `ƒ` `_extract_outline_for_file(file_path: Path) -> tuple[list[dict], list[str]]`  L68
  - _文档首行_（仅供参考）: Return the document outline and fallback preview for *file_path*.
  - 分支数 7，函数体节点数 162；return: ([], []), (outline, []), ([], preview)
  - 调用: with_suffix, is_file, extract_outline, debug, len, open, strip, append
  - 文件IO: open (L94)

## 类
### 类 `UploadsMiddlewareState`  L106
- 继承: AgentState
- _文档首行_: State schema for uploads middleware.
- 类/实例变量:
  - `uploaded_files` = <annotated>

### 类 `UploadsMiddleware`  L112
- 继承: AgentMiddleware[UploadsMiddlewareState]
- _文档首行_: Middleware to inject uploaded files information into the agent context.
- 类/实例变量:
  - `state_schema` = UploadsMiddlewareState
- 方法:
  #### `m` `__init__(self, base_dir: str | None, *, max_files_per_context_section: int)`  L122
    - _文档首行_（仅供参考）: Initialize the middleware.
    - 分支数 1，函数体节点数 58；raise: ValueError('max_files_per_context_section must be at least 1')
    - 调用: __init__, super, ValueError, Paths, get_paths
  #### `m` `_format_file_entry(self, file: dict, lines: list[str]) -> None`  L141
    - _文档首行_（仅供参考）: Append a single file entry (name, size, path, optional outline) to lines.
    - 分支数 6，函数体节点数 257
    - 调用: append, get, len
  #### `m` `_select_files_for_context(self, files: list[dict], query_text: str, *, recency_key: str | None) -> tuple[list[dict], list[dict]]`  L167
    - _文档首行_（仅供参考）: Return bounded context files, prioritizing current-query matches.
    - 分支数 3，函数体节点数 228；return: (selected, omitted)
    - 调用: enumerate, dict, _query_match_strength, float, get, append, sort
  #### `m` `_create_files_message(self, new_files: list[dict], historical_files: list[dict], *, omitted_new_files: list[dict] | None, omitted_historical_files: list[dict] | None) -> str`  L194
    - _文档首行_（仅供参考）: Create a formatted message listing uploaded files.
    - 分支数 6，函数体节点数 296；return: '\n'.join(lines)
    - 调用: append, _format_file_entry, len, _format_omitted_file_types, join
  #### `m` `_files_from_kwargs(self, message: HumanMessage, uploads_dir: Path | None) -> list[dict] | None`  L255
    - _文档首行_（仅供参考）: Extract file info from message additional_kwargs.files.
    - 分支数 5，函数体节点数 177；return: None, files if files else None
    - 调用: get, isinstance, Path, is_upload_staging_file, is_file, append, int
  #### `m` `before_agent(self, state: UploadsMiddlewareState, runtime: Runtime) -> dict | None`    @override  L294
    - _文档首行_（仅供参考）: Inject uploaded files information before agent execution.
    - 分支数 17，函数体节点数 691；return: None, {'uploaded_files': new_files, 'messages': messages}
    - 调用: list, get, len, isinstance, get_config, sandbox_uploads_dir, get_effective_user_id, get_original_user_content_text, _files_from_kwargs, _select_files_for_context, exists, sorted, iterdir, is_upload_staging_file, is_file, stat, append, pop, _extract_outline_for_file, debug（+6）
  - 文件IO: exists (L342), iterdir (L343), stat (L347)
  #### `⏵m` `async abefore_agent(self, state: UploadsMiddlewareState, runtime: Runtime) -> dict | None`    @override  L439
    - _文档首行_（仅供参考）: Async hook that offloads the synchronous uploads scan off the event loop.
    - 分支数 0，函数体节点数 32；return: await run_in_executor(None, self.before_agent, state, runtime)
    - 调用: run_in_executor

## 文件内调用关系
- `_format_omitted_file_types` -> _extension_label
- `_query_match_strength` -> _extension_label
- `UploadsMiddleware.__init__` -> __init__
- `UploadsMiddleware._select_files_for_context` -> _query_match_strength
- `UploadsMiddleware._create_files_message` -> _format_file_entry, _format_omitted_file_types
- `UploadsMiddleware.before_agent` -> _files_from_kwargs, _select_files_for_context, _extract_outline_for_file, _create_files_message

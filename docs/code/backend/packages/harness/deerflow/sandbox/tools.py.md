# `backend/packages/harness/deerflow/sandbox/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/tools.py`  ·  行数: 2324

## 模块概览
- 函数 85 个，类 0 个，模块级常量 30 个

## 依赖（import）
- 模块: asyncio, json, logging, os, posixpath, re, shlex
- `collections.abc` -> Callable
- `functools` -> lru_cache
- `pathlib` -> Path
- `langchain.tools` -> tool
- `deerflow.agents.thread_state` -> ThreadDataState
- `deerflow.config` -> get_app_config
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.runtime.secret_context` -> read_active_secrets
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.sandbox.exceptions` -> SandboxError, SandboxNotFoundError, SandboxRuntimeError
- `deerflow.sandbox.file_operation_lock` -> get_file_operation_lock
- `deerflow.sandbox.path_patterns` -> build_output_mask_pattern
- `deerflow.sandbox.sandbox` -> Sandbox
- `deerflow.sandbox.sandbox_provider` -> get_sandbox_provider
- `deerflow.sandbox.search` -> GrepMatch
- `deerflow.sandbox.security` -> LOCAL_HOST_BASH_DISABLED_MESSAGE, is_host_bash_allowed
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_ABSOLUTE_PATH_PATTERN` = re.compile('(?<![:\\w])(?<!:/)/(?:[^\\s\\"\'`;&|<>()]+)')
- `_IDENTIFIER_BRACE_BLOCK_PATTERN` = re.compile('\\{([^{}]*)\\}')
- `_IDENTIFIER_PATTERN` = re.compile('[A-Za-z_][A-Za-z0-9_]*')
- `_FILE_URL_PATTERN` = re.compile('\\bfile://\\S+', re.IGNORECASE)
- `_URL_WITH_SCHEME_PATTERN` = re.compile('^[a-z][a-z0-9+.-]*://', re.IGNORECASE)
- `_URL_IN_COMMAND_PATTERN` = re.compile('\\b[a-z][a-z0-9+.-]*://[^\\s\\"\'`;&|<>()]+',...
- `_DOTDOT_PATH_SEGMENT_PATTERN` = re.compile('(?:^|[/\\\\=])\\.\\.(?:$|[/\\\\])')
- `_LOCAL_BASH_SYSTEM_PATH_PREFIXES` = ('/bin/', '/usr/bin/', '/usr/sbin/', '/sbin/', '/opt/home...
- `_DEFAULT_SKILLS_CONTAINER_PATH` = DEFAULT_SKILLS_CONTAINER_PATH
- `_ACP_WORKSPACE_VIRTUAL_PATH` = '/mnt/acp-workspace'
- `_DEFAULT_GLOB_MAX_RESULTS` = 200
- `_MAX_GLOB_MAX_RESULTS` = 1000
- `_DEFAULT_GREP_MAX_RESULTS` = 100
- `_MAX_GREP_MAX_RESULTS` = 500
- `_DEFAULT_WRITE_FILE_ERROR_MAX_CHARS` = 2000
- `_WRITE_FILE_CONTENT_MAX_BYTES` = 80 * 1024
- `_WRITE_FILE_MAX_BYTES_ENV` = 'DEERFLOW_WRITE_FILE_MAX_BYTES'
- `_LOCAL_BASH_CWD_COMMANDS` = {'cd', 'pushd'}
- `_LOCAL_BASH_COMMAND_WRAPPERS` = {'command', 'builtin'}
- `_LOCAL_BASH_COMMAND_PREFIX_KEYWORDS` = {'!', '{', 'case', 'do', 'elif', 'else', 'for', 'if', 'se...
- `_LOCAL_BASH_COMMAND_END_KEYWORDS` = {'}', 'done', 'esac', 'fi'}
- `_LOCAL_BASH_ROOT_PATH_COMMANDS` = {'awk', 'cat', 'cp', 'du', 'find', 'grep', 'head', 'less'...
- `_SHELL_COMMAND_SEPARATORS` = {';', '&&', '||', '|', '|&', '&', '(', ')'}
- `_SHELL_REDIRECTION_OPERATORS` = {'<', '>', '<<', '>>', '<<<', '<>', '>&', '<&', '&>', '&>...
- `_SECRET_REDACTION` = '[redacted]'
- `_MIN_MASK_LENGTH` = 8
- `CHANNEL_USER_ID_ENV` = 'DEERFLOW_CHANNEL_USER_ID'
- `_CHANNEL_USER_ID_CONTEXT_KEY` = 'channel_user_id'
- `_CHANNEL_USER_ID_MAX_LEN` = 256

## 函数
#### `ƒ` `_get_skills_container_path() -> str`  L109
  - _文档首行_（仅供参考）: Get the skills container path from config, with fallback to default.
  - 分支数 2，函数体节点数 54；return: cached, value, _DEFAULT_SKILLS_CONTAINER_PATH
  - 调用: getattr, get_app_config
  - 反射: getattr (L116)

#### `ƒ` `_get_skills_host_path() -> str | None`  L129
  - _文档首行_（仅供参考）: Get the skills host filesystem path from config.
  - 分支数 3，函数体节点数 77；return: cached, value, None
  - 调用: getattr, get_app_config, get_skills_path, exists, str
  - 文件IO: exists (L145)
  - 反射: getattr (L137)

#### `ƒ` `_is_skills_path(path: str) -> bool`  L154
  - _文档首行_（仅供参考）: Check if a path is under the skills container path.
  - 分支数 0，函数体节点数 34；return: path == skills_prefix or path.startswith(f'{skills_prefix}/')
  - 调用: _get_skills_container_path, startswith

#### `ƒ` `_extract_skill_name_from_skills_path(path: str) -> str | None`  L160
  - _文档首行_（仅供参考）: Extract a skill name from a virtual skills path.
  - 分支数 5，函数体节点数 140；return: None, parts[1], parts[0]
  - 调用: _get_skills_container_path, _is_skills_path, lstrip, len, split

#### `ƒ` `_is_disabled_skill_path(path: str, *, user_id: str | None) -> bool`  L192
  - _文档首行_（仅供参考）: Check if a path belongs to a disabled skill.
  - 分支数 7，函数体节点数 241；return: False, not ext_config.is_skill_enabled(skill_name, category), not storage.get_skill_enabled_state(skill_name), True
  - 调用: _extract_skill_name_from_skills_path, _get_skills_container_path, lstrip, len, startswith, get_effective_user_id, get_or_new_user_skill_storage, load_skills, next, from_file, is_skill_enabled, get_skill_enabled_state, warning

#### `ƒ` `_drop_disabled_skill_paths(paths: list[str], *, user_id: str | None) -> list[str]`  L247
  - _文档首行_（仅供参考）: Filter out paths that belong to a disabled skill.
  - 分支数 4，函数体节点数 166；return: kept
  - 调用: _get_skills_container_path, _extract_skill_name_from_skills_path, append, split, lstrip, len, _is_disabled_skill_path

#### `ƒ` `_resolve_skills_path(path: str) -> str`  L280
  - _文档首行_（仅供参考）: Resolve a virtual skills path to a host filesystem path.
  - 分支数 4，函数体节点数 146；raise: FileNotFoundError(f'Skills directory not available for path: {path}')；return: skills_host, str(user_custom_dir / custom_relative), str(user_custom_dir), _join_path_preserving_style(skills_host, relative)
  - 调用: _get_skills_container_path, _get_skills_host_path, FileNotFoundError, lstrip, len, startswith, get_effective_user_id, get_paths, user_custom_skills_dir, str, _join_path_preserving_style

#### `ƒ` `_is_acp_workspace_path(path: str) -> bool`  L333
  - _文档首行_（仅供参考）: Check if a path is under the ACP workspace virtual path.
  - 分支数 0，函数体节点数 28；return: path == _ACP_WORKSPACE_VIRTUAL_PATH or path.startswith(f'{_ACP_WORKSPACE_VIRTUAL_PATH}/')
  - 调用: startswith

#### `ƒ` `_get_custom_mounts()`  L338
  - _文档首行_（仅供参考）: Get custom volume mounts from sandbox config.
  - 分支数 3，函数体节点数 93；return: cached, mounts, []
  - 调用: getattr, get_app_config, exists, Path
  - 文件IO: exists (L359)
  - 反射: getattr (L345)

#### `ƒ` `_is_custom_mount_path(path: str) -> bool`  L368
  - _文档首行_（仅供参考）: Check if path is under a custom mount container_path.
  - 分支数 2，函数体节点数 42；return: True, False
  - 调用: _get_custom_mounts, startswith

#### `ƒ` `_get_custom_mount_for_path(path: str)`  L376
  - _文档首行_（仅供参考）: Get the mount config matching this path (longest prefix first).
  - 分支数 3，函数体节点数 72；return: best
  - 调用: _get_custom_mounts, startswith, len

#### `ƒ` `_extract_thread_id_from_thread_data(thread_data: 'ThreadDataState | None') -> str | None`  L386
  - _文档首行_（仅供参考）: Extract thread_id from thread_data by inspecting workspace_path.
  - 分支数 3，函数体节点数 53；return: None, Path(workspace_path).parent.parent.name
  - 调用: get, Path

#### `ƒ` `_get_acp_workspace_host_path(thread_id: str | None) -> str | None`  L405
  - _文档首行_（仅供参考）: Get the ACP workspace host filesystem path.
  - 分支数 6，函数体节点数 123；return: str(host_path), None, cached, value
  - 调用: acp_workspace_dir, get_paths, get_effective_user_id, exists, str, getattr
  - 文件IO: exists (L422), exists (L435)
  - 反射: getattr (L428)

#### `ƒ` `_resolve_acp_workspace_path(path: str, thread_id: str | None) -> str`  L444
  - _文档首行_（仅供参考）: Resolve a virtual ACP workspace path to a host filesystem path.
  - 分支数 6，函数体节点数 189；raise: FileNotFoundError(f'ACP workspace directory not available for path: {path}'), PermissionError('Access denied: path traversal detected')；return: host_path, resolved, str(resolved_path)
  - 调用: _reject_path_traversal, _get_acp_workspace_host_path, FileNotFoundError, lstrip, len, _join_path_preserving_style, normpath, commonpath, PermissionError, resolve, Path, relative_to, str

#### `ƒ` `_get_mcp_allowed_paths() -> list[str]`  L490
  - _文档首行_（仅供参考）: Get the list of allowed paths from MCP config for file system server.
  - 分支数 6，函数体节点数 124；return: allowed_paths
  - 调用: get_extensions_config, items, any, startswith, append, rstrip

#### `ƒ` `_get_tool_config_int(name: str, key: str, default: int) -> int`  L519
  - 分支数 3，函数体节点数 71；return: value, default
  - 调用: get_tool_config, get_app_config, get, isinstance

#### `ƒ` `_clamp_max_results(value: int, *, default: int, upper_bound: int) -> int`  L531
  - 分支数 1，函数体节点数 30；return: default, min(value, upper_bound)
  - 调用: min

#### `ƒ` `_resolve_max_results(name: str, requested: int, *, default: int, upper_bound: int) -> int`  L537
  - 分支数 0，函数体节点数 58；return: min(requested_max_results, configured_max_results)
  - 调用: _clamp_max_results, _get_tool_config_int, min

#### `ƒ` `_resolve_local_read_path(path: str, thread_data: ThreadDataState) -> str`  L547
  - 分支数 1，函数体节点数 44；return: path, _resolve_and_validate_user_data_path(path, thread_data)
  - 调用: validate_local_tool_path, _is_skills_path, _is_acp_workspace_path, _resolve_and_validate_user_data_path

#### `ƒ` `_format_glob_results(root_path: str, matches: list[str], truncated: bool) -> str`  L559
  - 分支数 3，函数体节点数 110；return: f'No files matched under {root_path}', '\n'.join(lines)
  - 调用: len, extend, enumerate, append, join

#### `ƒ` `_format_grep_results(root_path: str, matches: list[GrepMatch], truncated: bool) -> str`  L572
  - 分支数 3，函数体节点数 111；return: f'No matches found under {root_path}', '\n'.join(lines)
  - 调用: len, extend, append, join

#### `ƒ` `_path_variants(path: str) -> set[str]`  L585
  - 分支数 0，函数体节点数 29；return: {path, path.replace('\\', '/'), path.replace('/', '\\')}
  - 调用: replace
  - 文件IO: replace (L586), replace (L586)

#### `ƒ` `_path_separator_for_style(path: str) -> str`  L589
  - 分支数 0，函数体节点数 23；return: '\\' if '\\' in path and '/' not in path else '/'

#### `ƒ` `_join_path_preserving_style(base: str, relative: str) -> str`  L593
  - 分支数 1，函数体节点数 68；return: base, f'{stripped_base}{separator}{normalized_relative}'
  - 调用: _path_separator_for_style, lstrip, replace, rstrip
  - 文件IO: replace (L597)

#### `ƒ` `_sanitize_error(error: Exception, runtime: Runtime | None) -> str`  L602
  - _文档首行_（仅供参考）: Sanitize an error message to avoid leaking host filesystem paths.
  - 分支数 1，函数体节点数 66；return: msg
  - 调用: type, is_local_sandbox, get_thread_data, mask_local_paths_in_output

#### `ƒ` `_truncate_write_file_error_detail(detail: str, max_chars: int) -> str`  L616
  - _文档首行_（仅供参考）: Middle-truncate write_file error details, preserving the head and tail.
  - 分支数 3，函数体节点数 146；return: detail, detail[:max_chars], f"{detail[:head_len]}{marker}{(detail[-tail_len:] if tail_len > 0 else '')}"
  - 调用: len, max

#### `ƒ` `_format_write_file_error(requested_path: str, error: Exception, runtime: Runtime | None, *, max_chars: int) -> str`  L634
  - _文档首行_（仅供参考）: Return a bounded, sanitized error string for write_file failures.
  - 分支数 2，函数体节点数 107；return: f'{header}: {detail}', _truncate_write_file_error_detail(f'{header}: {detail}', max_chars), f'{header}: {_truncate_write_file_error_detail(detail, detail_budget)}'
  - 调用: _sanitize_error, len, _truncate_write_file_error_detail

#### `ƒ` `replace_virtual_path(path: str, thread_data: ThreadDataState | None) -> str`  L652
  - _文档首行_（仅供参考）: Replace virtual /mnt/user-data paths with actual thread data paths.
  - 分支数 6，函数体节点数 152；return: path, actual_base, result
  - 调用: _thread_virtual_to_actual_mappings, sorted, items, len, startswith, lstrip, _join_path_preserving_style, endswith, _path_separator_for_style

#### `ƒ` `_thread_virtual_to_actual_mappings(thread_data: ThreadDataState) -> dict[str, str]`  L688
  - _文档首行_（仅供参考）: Build virtual-to-actual path mappings for a thread.
  - 分支数 5，函数体节点数 177；return: mappings
  - 调用: get, Path, str, all

#### `ƒ` `_thread_actual_to_virtual_mappings(thread_data: ThreadDataState) -> dict[str, str]`  L713
  - _文档首行_（仅供参考）: Build actual-to-virtual mappings for output masking.
  - 分支数 0，函数体节点数 38；return: {actual: virtual for virtual, actual in _thread_virtual_to_actual_mappings(thread_data).items()}
  - 调用: items, _thread_virtual_to_actual_mappings

#### `ƒ` `_compiled_mask_patterns(sources: tuple[tuple[str, str], ...]) -> tuple[tuple[re.Pattern[str], str, str], ...]`    @lru_cache(...)  L719
  - _文档首行_（仅供参考）: Compile the host→virtual masking patterns once per source set.
  - 分支数 4，函数体节点数 176；return: tuple(compiled)
  - 调用: set, str, Path, resolve, sorted, _path_variants, add, append, build_output_mask_pattern, tuple, lru_cache

#### `ƒ` `mask_local_paths_in_output(output: str, thread_data: ThreadDataState | None) -> str`  L757
  - _文档首行_（仅供参考）: Mask host absolute paths from local sandbox output using virtual paths.
  - 分支数 9，函数体节点数 307；return: output, _virtual, f'{_virtual}/{relative}' if relative else _virtual, result
  - 调用: _get_skills_host_path, append, _get_skills_container_path, get_effective_user_id, user_custom_skills_dir, get_paths, exists, str, _get_acp_workspace_host_path, _extract_thread_id_from_thread_data, _thread_actual_to_virtual_mappings, sorted, items, len, _compiled_mask_patterns, tuple, group, lstrip, sub
  - 文件IO: exists (L785)

#### `ƒ` `_reject_path_traversal(path: str) -> None`  L818
  - _文档首行_（仅供参考）: Reject paths that contain '..' segments to prevent directory traversal.
  - 分支数 2，函数体节点数 38；raise: PermissionError('Access denied: path traversal detected')
  - 调用: replace, split, PermissionError
  - 文件IO: replace (L821)

#### `ƒ` `validate_local_tool_path(path: str, thread_data: ThreadDataState | None, *, read_only: bool) -> None`  L827
  - _文档首行_（仅供参考）: Validate that a virtual path is allowed for local-sandbox access.
  - 分支数 8，函数体节点数 145；raise: SandboxRuntimeError('Thread data not available for local sandbox'), PermissionError(f'Write access to skills path is not allowed: {path}'), PermissionError(f'Write access to ACP workspace is not allowed: {path}'), PermissionError(f'Write access to read-only mount is not allowed: {path}'), PermissionError(f'Only paths under {VIRTUAL_PATH_PREFIX}/, {_get_skills_container_path()}/, {_ACP_WORKSPACE_VIRTUAL_PATH}/, or configured mount paths are allowed')；return: None
  - 调用: SandboxRuntimeError, _reject_path_traversal, _is_skills_path, PermissionError, _is_acp_workspace_path, startswith, _is_custom_mount_path, _get_custom_mount_for_path, _get_skills_container_path

#### `ƒ` `_validate_resolved_user_data_path(resolved: Path, thread_data: ThreadDataState) -> None`  L881
  - _文档首行_（仅供参考）: Verify that a resolved host path stays inside allowed per-thread roots.
  - 分支数 3，函数体节点数 85；raise: SandboxRuntimeError('No allowed local sandbox directories configured'), PermissionError('Access denied: path traversal detected')；return: None
  - 调用: resolve, Path, get, SandboxRuntimeError, relative_to, PermissionError

#### `ƒ` `_resolve_and_validate_user_data_path(path: str, thread_data: ThreadDataState) -> str`  L909
  - _文档首行_（仅供参考）: Resolve a /mnt/user-data virtual path and validate it stays in bounds.
  - 分支数 0，函数体节点数 47；return: str(resolved)
  - 调用: replace_virtual_path, resolve, Path, _validate_resolved_user_data_path, str

#### `ƒ` `_is_non_file_url_token(token: str) -> bool`  L920
  - _文档首行_（仅供参考）: Return True for URL tokens that should not be interpreted as paths.
  - 分支数 3，函数体节点数 73；return: True, False
  - 调用: append, split, match, startswith, lower

#### `ƒ` `_non_file_url_spans(command: str) -> list[tuple[int, int]]`  L933
  - 分支数 2，函数体节点数 63；return: spans
  - 调用: finditer, startswith, lower, group, append, span

#### `ƒ` `_is_in_spans(position: int, spans: list[tuple[int, int]]) -> bool`  L941
  - 分支数 0，函数体节点数 45；return: any((start <= position < end for start, end in spans))
  - 调用: any

#### `ƒ` `_has_dotdot_path_segment(token: str) -> bool`  L945
  - 分支数 1，函数体节点数 26；return: False, bool(_DOTDOT_PATH_SEGMENT_PATTERN.search(token))
  - 调用: _is_non_file_url_token, bool, search

#### `ƒ` `_split_shell_tokens(command: str) -> list[str]`  L951
  - 分支数 1，函数体节点数 73；return: list(lexer), command.split()
  - 调用: replace, shlex, list, split
  - 文件IO: replace (L953), replace (L953), replace (L953)

#### `ƒ` `_is_shell_command_separator(token: str) -> bool`  L964
  - 分支数 0，函数体节点数 14；return: token in _SHELL_COMMAND_SEPARATORS

#### `ƒ` `_is_shell_redirection_operator(token: str) -> bool`  L968
  - 分支数 0，函数体节点数 14；return: token in _SHELL_REDIRECTION_OPERATORS

#### `ƒ` `_is_shell_assignment(token: str) -> bool`  L972
  - 分支数 1，函数体节点数 47；return: False, bool(re.fullmatch('[A-Za-z_][A-Za-z0-9_]*', name))
  - 调用: partition, bool, fullmatch

#### `ƒ` `_is_allowed_local_bash_absolute_path(path: str, allowed_paths: list[str], *, allow_system_paths: bool) -> bool`  L979
  - 分支数 6，函数体节点数 160；return: True, False
  - 调用: any, startswith, rstrip, _reject_path_traversal, _is_skills_path, _is_acp_workspace_path, _is_custom_mount_path

#### `ƒ` `_next_cd_target(tokens: list[str], start_index: int) -> tuple[str | None, int]`  L1010
  - 分支数 6，函数体节点数 137；return: (None, index), (token, index + 1)
  - 调用: len, _is_shell_command_separator, _is_shell_redirection_operator, startswith

#### `ƒ` `_validate_local_bash_cwd_target(command_name: str, target: str | None, allowed_paths: list[str]) -> None`  L1032
  - 分支数 5，函数体节点数 138；raise: PermissionError(f'Unsafe working directory change in command: {command_name}. Use paths under {VIRTUAL_PATH_PREFIX}'), PermissionError(f'Unsafe working directory change in command: {command_name} {target}. Use paths under {VIRTUAL_PATH_PREFIX}')
  - 调用: PermissionError, startswith, _reject_path_traversal, _is_allowed_local_bash_absolute_path

#### `ƒ` `_validate_local_bash_root_path_args(command_name: str, tokens: list[str], start_index: int) -> None`  L1045
  - 分支数 5，函数体节点数 96；raise: PermissionError(f'Unsafe absolute paths in command: /. Use paths under {VIRTUAL_PATH_PREFIX}')；return: None
  - 调用: len, _is_shell_command_separator, _is_shell_redirection_operator, _is_non_file_url_token, PermissionError

#### `ƒ` `_validate_local_bash_shell_tokens(command: str, allowed_paths: list[str]) -> None`  L1062
  - _文档首行_（仅供参考）: Conservatively reject relative path escapes missed by absolute-path scanning.
  - 分支数 13，函数体节点数 347；raise: PermissionError(f'Unsafe working directory change in command substitution. Use paths under {VIRTUAL_PATH_PREFIX}'), PermissionError('Access denied: path traversal detected')
  - 调用: search, PermissionError, _split_shell_tokens, _is_shell_command_separator, _is_shell_redirection_operator, _has_dotdot_path_segment, len, _is_shell_assignment, rsplit, _next_cd_target, _validate_local_bash_cwd_target, _validate_local_bash_root_path_args

#### `ƒ` `resolve_and_validate_user_data_path(path: str, thread_data: ThreadDataState) -> str`  L1122
  - _文档首行_（仅供参考）: Resolve a /mnt/user-data virtual path and validate it stays in bounds.
  - 分支数 0，函数体节点数 20；return: _resolve_and_validate_user_data_path(path, thread_data)
  - 调用: _resolve_and_validate_user_data_path

#### `ƒ` `_braces_are_identifier_placeholders_only(fragment: str) -> bool`  L1127
  - _文档首行_（仅供参考）: Return True only if every ``{...}`` block is a single identifier placeholder.
  - 分支数 2，函数体节点数 75；return: False, all((_IDENTIFIER_PATTERN.fullmatch(inner) for inner in blocks))
  - 调用: findall, count, len, all, fullmatch

#### `ƒ` `_is_non_path_literal_fragment(fragment: str) -> bool`  L1149
  - _文档首行_（仅供参考）: Return True if a ``/segment`` match is almost certainly text, not a path.
  - 分支数 2，函数体节点数 50；return: True, _braces_are_identifier_placeholders_only(fragment), False
  - 调用: any, ord, _braces_are_identifier_placeholders_only

#### `ƒ` `validate_local_bash_command_paths(command: str, thread_data: ThreadDataState | None) -> None`  L1175
  - _文档首行_（仅供参考）: Validate absolute paths in local-sandbox bash commands.
  - 分支数 7，函数体节点数 176；raise: SandboxRuntimeError('Thread data not available for local sandbox'), PermissionError(f'Unsafe file:// URL in command: {file_url_match.group()}. Use paths under {VIRTUAL_PATH_PREFIX}'), PermissionError(f'Unsafe absolute paths in command: {unsafe}. Use paths under {VIRTUAL_PATH_PREFIX}')
  - 调用: SandboxRuntimeError, search, PermissionError, group, _get_mcp_allowed_paths, _validate_local_bash_shell_tokens, _non_file_url_spans, finditer, _is_in_spans, start, _is_non_path_literal_fragment, _is_allowed_local_bash_absolute_path, append, join, sorted, fromkeys

#### `ƒ` `replace_virtual_paths_in_command(command: str, thread_data: ThreadDataState | None) -> str`  L1219
  - _文档首行_（仅供参考）: Replace /mnt/user-data virtual paths in a command string for local sandbox.
  - 分支数 1，函数体节点数 93；return: replace_virtual_path(match.group(0), thread_data).replace('\\', '/'), result
  - 调用: compile, escape, replace, replace_virtual_path, group, sub
  - 文件IO: replace (L1260)
  - 危险执行: compile (L1257)

#### `ƒ` `_apply_cwd_prefix(command: str, thread_data: ThreadDataState | None) -> str`  L1267
  - _文档首行_（仅供参考）: Prepend 'cd <workspace> &&' so relative paths are anchored to the thread workspace.
  - 分支数 1，函数体节点数 47；return: f'cd {shlex.quote(workspace)} && {command}', command
  - 调用: get, quote

#### `ƒ` `get_thread_data(runtime: Runtime | None) -> ThreadDataState | None`  L1283
  - _文档首行_（仅供参考）: Extract thread_data from runtime state.
  - 分支数 2，函数体节点数 42；return: None, runtime.state.get('thread_data')
  - 调用: get

#### `ƒ` `is_local_sandbox(runtime: Runtime | None) -> bool`  L1292
  - _文档首行_（仅供参考）: Check if the current sandbox is a local sandbox.
  - 分支数 4，函数体节点数 84；return: False, sandbox_id == 'local' or sandbox_id.startswith('local:')
  - 调用: get, isinstance, startswith

#### `ƒ` `sandbox_from_runtime(runtime: Runtime | None) -> Sandbox`  L1312
  - _文档首行_（仅供参考）: Extract sandbox instance from tool runtime.
  - 分支数 6，函数体节点数 130；raise: SandboxRuntimeError('Tool runtime not available'), SandboxRuntimeError('Tool runtime state not available'), SandboxRuntimeError('Sandbox state not initialized in runtime'), SandboxRuntimeError('Sandbox ID not found in state'), SandboxNotFoundError(f"Sandbox with ID '{sandbox_id}' not found", sandbox_id=sandbox_id)；return: sandbox
  - 调用: SandboxRuntimeError, get, get_sandbox_provider, SandboxNotFoundError

#### `ƒ` `ensure_sandbox_initialized(runtime: Runtime | None) -> Sandbox`  L1341
  - _文档首行_（仅供参考）: Ensure sandbox is initialized, acquiring lazily if needed.
  - 分支数 10，函数体节点数 242；raise: SandboxRuntimeError('Tool runtime not available'), SandboxRuntimeError('Tool runtime state not available'), SandboxRuntimeError('Thread ID not available in runtime context'), SandboxNotFoundError('Sandbox not found after acquisition', sandbox_id=sandbox_id)；return: sandbox
  - 调用: SandboxRuntimeError, get, get_sandbox_provider, acquire, resolve_runtime_user_id, SandboxNotFoundError

#### `⏵ƒ` `async ensure_sandbox_initialized_async(runtime: Runtime | None) -> Sandbox`  L1400
  - _文档首行_（仅供参考）: Async counterpart to ``ensure_sandbox_initialized`` for tool runtimes.
  - 分支数 10，函数体节点数 243；raise: SandboxRuntimeError('Tool runtime not available'), SandboxRuntimeError('Tool runtime state not available'), SandboxRuntimeError('Thread ID not available in runtime context'), SandboxNotFoundError('Sandbox not found after acquisition', sandbox_id=sandbox_id)；return: sandbox
  - 调用: SandboxRuntimeError, get, get_sandbox_provider, acquire_async, resolve_runtime_user_id, SandboxNotFoundError

#### `⏵ƒ` `async _run_sync_tool_after_async_sandbox_init(func: Callable[..., str] | None, runtime: Runtime, *args) -> str`  L1443
  - _文档首行_（仅供参考）: Initialize lazily via async provider, then run sync tool body off-thread.
  - 分支数 2，函数体节点数 79；可变参数（*args/**kwargs）；return: f'Error: {e}', f'Error: Unexpected error initializing sandbox: {_sanitize_error(e, runtime)}', 'Error: Tool implementation not available', await asyncio.to_thread(func, runtime, *args)
  - 调用: ensure_sandbox_initialized_async, _sanitize_error, to_thread

#### `ƒ` `ensure_thread_directories_exist(runtime: Runtime | None) -> None`  L1462
  - _文档首行_（仅供参考）: Ensure thread data directories (workspace, uploads, outputs) exist.
  - 分支数 6，函数体节点数 94；return: None
  - 调用: is_local_sandbox, get_thread_data, get, makedirs

#### `ƒ` `mask_secret_values(output: str, injected_env: dict[str, str] | None) -> str`  L1510
  - _文档首行_（仅供参考）: Redact injected secret values from bash output before it re-enters context.
  - 分支数 2，函数体节点数 87；return: output
  - 调用: sorted, values, len, replace
  - 文件IO: replace (L1526)

#### `ƒ` `_truncate_bash_output(output: str, max_chars: int) -> str`  L1530
  - _文档首行_（仅供参考）: Middle-truncate bash output, preserving head and tail (50/50 split).
  - 分支数 3，函数体节点数 146；return: output, output[:max_chars], f"{output[:head_len]}{marker}{(output[-tail_len:] if tail_len > 0 else '')}"
  - 调用: len, max

#### `ƒ` `_truncate_read_file_output(output: str, max_chars: int) -> str`  L1558
  - _文档首行_（仅供参考）: Head-truncate read_file output, preserving the beginning of the file.
  - 分支数 3，函数体节点数 111；return: output, output[:max_chars], f'{output[:kept]}{marker}'
  - 调用: len, max

#### `ƒ` `_truncate_ls_output(output: str, max_chars: int) -> str`  L1583
  - _文档首行_（仅供参考）: Head-truncate ls output, preserving the beginning of the listing.
  - 分支数 3，函数体节点数 111；return: output, output[:max_chars], f'{output[:kept]}{marker}'
  - 调用: len, max

#### `ƒ` `_is_windows() -> bool`  L1620
  - 分支数 0，函数体节点数 12；return: os.name == 'nt'

#### `ƒ` `_channel_identity_prefix(runtime: Runtime) -> str | None`  L1624
  - _文档首行_（仅供参考）: Build the command prefix that sets or clears the channel-user-id env var.
  - 分支数 2，函数体节点数 96；return: None, f'export {CHANNEL_USER_ID_ENV}={shlex.quote(channel_user_id)}; ', f'unset {CHANNEL_USER_ID_ENV}; '
  - 调用: getattr, isinstance, get, len, quote
  - 反射: getattr (L1646)

#### `ƒ` `_github_env_from_runtime(runtime: Runtime) -> dict[str, str] | None`  L1655
  - _文档首行_（仅供参考）: Build a per-call env overlay carrying a GitHub App installation token.
  - 分支数 3，函数体节点数 107；return: None, {'GH_TOKEN': token, 'GITHUB_TOKEN': token}
  - 调用: get, callable, value, warning, isinstance

#### `ƒ` `bash_tool(runtime: Runtime, description: str, command: str) -> str`    @tool(...)  L1701
  - _文档首行_（仅供参考）: Execute a bash command in a Linux environment.
  - 分支数 8，函数体节点数 345；return: f'Error: {LOCAL_HOST_BASH_DISABLED_MESSAGE}', _truncate_bash_output(mask_secret_values(mask_local_paths_in_output(output, thread_data), injected_env), max_chars), _truncate_bash_output(mask_secret_values(sandbox.execute_command(command, env=injected_env), injected_env), max_chars), f'Error: {e}', f'Error: Unexpected error executing command: {_sanitize_error(e, runtime)}'
  - 调用: ensure_sandbox_initialized, read_active_secrets, getattr, _channel_identity_prefix, _github_env_from_runtime, is_local_sandbox, is_host_bash_allowed, ensure_thread_directories_exist, get_thread_data, validate_local_bash_command_paths, replace_virtual_paths_in_command, _apply_cwd_prefix, _is_windows, get_app_config, execute_command, _truncate_bash_output, mask_secret_values, mask_local_paths_in_output, _sanitize_error, tool
  - 反射: getattr (L1723)

#### `⏵ƒ` `async _bash_tool_async(runtime: Runtime, description: str, command: str) -> str`  L1774
  - 分支数 0，函数体节点数 28；return: await _run_sync_tool_after_async_sandbox_init(bash_tool.func, runtime, description, command)
  - 调用: _run_sync_tool_after_async_sandbox_init

#### `ƒ` `ls_tool(runtime: Runtime, description: str, path: str) -> str`    @tool(...)  L1782
  - _文档首行_（仅供参考）: List the contents of a directory up to 2 levels deep in tree format.
  - 分支数 9，函数体节点数 286；return: f"Error: Skill '{skill_name}' is disabled. Access to its files is blocked. Enable the skill in settings before using it.", '(empty)', _truncate_ls_output(output, max_chars), f'Error: {e}', f'Error: Directory not found: {requested_path}', f'Error: Permission denied: {requested_path}', f'Error: Unexpected error listing directory: {_sanitize_error(e, runtime)}'
  - 调用: resolve_runtime_user_id, _is_disabled_skill_path, _extract_skill_name_from_skills_path, ensure_sandbox_initialized, ensure_thread_directories_exist, is_local_sandbox, get_thread_data, validate_local_tool_path, _is_skills_path, _is_acp_workspace_path, _is_custom_mount_path, _resolve_and_validate_user_data_path, list_dir, join, mask_local_paths_in_output, _drop_disabled_skill_paths, splitlines, get_app_config, _truncate_ls_output, _sanitize_error（+1）

#### `⏵ƒ` `async _ls_tool_async(runtime: Runtime, description: str, path: str) -> str`  L1842
  - 分支数 0，函数体节点数 28；return: await _run_sync_tool_after_async_sandbox_init(ls_tool.func, runtime, description, path)
  - 调用: _run_sync_tool_after_async_sandbox_init

#### `ƒ` `glob_tool(runtime: Runtime, description: str, pattern: str, path: str, include_dirs: bool, max_results: int) -> str`    @tool(...)  L1850
  - _文档首行_（仅供参考）: Find files or directories that match a glob pattern under a root directory.
  - 分支数 5，函数体节点数 257；raise: SandboxRuntimeError('Thread data not available for local sandbox')；return: f"Error: Skill '{skill_name}' is disabled. Access to its files is blocked. Enable the skill in settings before using it.", _format_glob_results(requested_path, matches, truncated), f'Error: {e}', f'Error: Directory not found: {requested_path}', f'Error: Path is not a directory: {requested_path}', f'Error: Permission denied: {requested_path}', f'Error: Unexpected error searching paths: {_sanitize_error(e, runtime)}'
  - 调用: resolve_runtime_user_id, _is_disabled_skill_path, _extract_skill_name_from_skills_path, ensure_sandbox_initialized, ensure_thread_directories_exist, _resolve_max_results, is_local_sandbox, get_thread_data, SandboxRuntimeError, _resolve_local_read_path, glob, mask_local_paths_in_output, _drop_disabled_skill_paths, _format_glob_results, _sanitize_error, tool
  - 文件IO: glob (L1888)

#### `⏵ƒ` `async _glob_tool_async(runtime: Runtime, description: str, pattern: str, path: str, include_dirs: bool, max_results: int) -> str`  L1907
  - 分支数 0，函数体节点数 46；return: await _run_sync_tool_after_async_sandbox_init(glob_tool.func, runtime, description, pattern, path, include_dirs, max_results)
  - 调用: _run_sync_tool_after_async_sandbox_init

#### `ƒ` `grep_tool(runtime: Runtime, description: str, pattern: str, path: str, glob: str | None, literal: bool, case_sensitive: bool, max_results: int) -> str`    @tool(...)  L1930
  - _文档首行_（仅供参考）: Search for matching lines inside text files under a root directory.
  - 分支数 5，函数体节点数 331；raise: SandboxRuntimeError('Thread data not available for local sandbox')；return: f"Error: Skill '{skill_name}' is disabled. Access to its files is blocked. Enable the skill in settings before using it.", _format_grep_results(requested_path, matches, truncated), f'Error: {e}', f'Error: Directory not found: {requested_path}', f'Error: Path is not a directory: {requested_path}', f'Error: Invalid regex pattern: {e}', f'Error: Permission denied: {requested_path}', f'Error: Unexpected error searching file contents: {_sanitize_error(e, runtime)}'
  - 调用: resolve_runtime_user_id, _is_disabled_skill_path, _extract_skill_name_from_skills_path, ensure_sandbox_initialized, ensure_thread_directories_exist, _resolve_max_results, is_local_sandbox, get_thread_data, SandboxRuntimeError, _resolve_local_read_path, grep, GrepMatch, mask_local_paths_in_output, set, _drop_disabled_skill_paths, _format_grep_results, _sanitize_error, tool

#### `⏵ƒ` `async _grep_tool_async(runtime: Runtime, description: str, pattern: str, path: str, glob: str | None, literal: bool, case_sensitive: bool, max_results: int) -> str`  L2008
  - 分支数 0，函数体节点数 61；return: await _run_sync_tool_after_async_sandbox_init(grep_tool.func, runtime, description, pattern, path, glob, literal, case_sensitive, max_results)
  - 调用: _run_sync_tool_after_async_sandbox_init

#### `ƒ` `read_current_file_content(runtime: Runtime | None, path: str) -> str`  L2034
  - _文档首行_（仅供参考）: Read the full current content of ``path`` using read_file's resolution rules.
  - 分支数 4，函数体节点数 112；return: sandbox.read_file(path)
  - 调用: ensure_sandbox_initialized, ensure_thread_directories_exist, is_local_sandbox, get_thread_data, validate_local_tool_path, _is_skills_path, _resolve_skills_path, _is_acp_workspace_path, _resolve_acp_workspace_path, _extract_thread_id_from_thread_data, _is_custom_mount_path, _resolve_and_validate_user_data_path, read_file

#### `ƒ` `read_file_tool(runtime: Runtime, description: str, path: str, start_line: int | None, end_line: int | None) -> str`    @tool(...)  L2058
  - _文档首行_（仅供参考）: Read the contents of a text file. Use this to examine source code, configuration files, logs, or any text-based file.
  - 分支数 8，函数体节点数 286；return: f"Error: Skill '{skill_name}' is disabled. Access to its files is blocked. Enable the skill in settings before using it.", '(empty)', '(end_line must be >= 1)', '(start_line exceeds file length)', '(start_line > end_line — no lines in range)', _truncate_read_file_output(content, max_chars), f'Error: {e}', f'Error: File not found: {requested_path}', f'Error: Permission denied reading file: {requested_path}', f'Error: Path is a directory, not a file: {requested_path}', f"Error: cannot read '{requested_path}' as text — it appears to be a binary file (e.g. .xlsx, .pdf, or an image). read_file only supports UTF-8 text. Use bash with a suitable library instead (pandas/openpyxl for spreadsheets), or view_image for images.", f'Error: Unexpected error reading file: {_sanitize_error(e, runtime)}'
  - 调用: _is_disabled_skill_path, resolve_runtime_user_id, _extract_skill_name_from_skills_path, read_current_file_content, splitlines, max, len, join, get_app_config, _truncate_read_file_output, _sanitize_error, tool

#### `⏵ƒ` `async _read_file_tool_async(runtime: Runtime, description: str, path: str, start_line: int | None, end_line: int | None) -> str`  L2119
  - 分支数 0，函数体节点数 46；return: await _run_sync_tool_after_async_sandbox_init(read_file_tool.func, runtime, description, path, start_line, end_line)
  - 调用: _run_sync_tool_after_async_sandbox_init

#### `ƒ` `_effective_write_file_max_bytes() -> int`  L2132
  - _文档首行_（仅供参考）: Return the active size cap for non-append write_file calls.
  - 分支数 2，函数体节点数 40；return: _WRITE_FILE_CONTENT_MAX_BYTES, int(raw)
  - 调用: get, int

#### `ƒ` `write_file_tool(runtime: Runtime, description: str, path: str, content: str, append: bool) -> str`    @tool(...)  L2150
  - _文档首行_（仅供参考）: Write text content to a file. By default this overwrites the target file; set append=True to add content to the end with
  - 分支数 7，函数体节点数 225；return: f'Error: write_file content ({content_bytes} bytes) exceeds the {max_bytes}-byte single-call limit. Split the content into smaller pieces: either (a) write the first section now, then use `str_replace` for further edits, or (b) call write_file again with append=True carrying the next section. See SIZE POLICY in the tool docstring or issue #3189 for the rationale.', 'OK', _format_write_file_error(requested_path, e, runtime), _truncate_write_file_error_detail(f'Error: Permission denied writing to file: {requested_path}', _DEFAULT_WRITE_FILE_ERROR_MAX_CHARS), _truncate_write_file_error_detail(f'Error: Path is a directory, not a file: {requested_path}', _DEFAULT_WRITE_FILE_ERROR_MAX_CHARS)
  - 调用: _effective_write_file_max_bytes, len, encode, ensure_sandbox_initialized, ensure_thread_directories_exist, is_local_sandbox, get_thread_data, validate_local_tool_path, _is_custom_mount_path, _resolve_and_validate_user_data_path, get_file_operation_lock, write_file, _format_write_file_error, _truncate_write_file_error_detail, tool

#### `⏵ƒ` `async _write_file_tool_async(runtime: Runtime, description: str, path: str, content: str, append: bool) -> str`  L2235
  - 分支数 0，函数体节点数 39；return: await _run_sync_tool_after_async_sandbox_init(write_file_tool.func, runtime, description, path, content, append)
  - 调用: _run_sync_tool_after_async_sandbox_init

#### `ƒ` `str_replace_tool(runtime: Runtime, description: str, path: str, old_str: str, new_str: str, replace_all: bool) -> str`    @tool(...)  L2249
  - _文档首行_（仅供参考）: Replace a substring in a file with another substring.
  - 分支数 8，函数体节点数 222；return: 'OK', f'Error: String to replace not found in file: {requested_path}', f'Error: {e}', f'Error: File not found: {requested_path}', f'Error: Permission denied accessing file: {requested_path}', f'Error: Unexpected error replacing string: {_sanitize_error(e, runtime)}'
  - 调用: ensure_sandbox_initialized, ensure_thread_directories_exist, is_local_sandbox, get_thread_data, validate_local_tool_path, _is_custom_mount_path, _resolve_and_validate_user_data_path, get_file_operation_lock, read_file, replace, write_file, _sanitize_error, tool
  - 文件IO: replace (L2289), replace (L2291)

#### `⏵ƒ` `async _str_replace_tool_async(runtime: Runtime, description: str, path: str, old_str: str, new_str: str, replace_all: bool) -> str`  L2304
  - 分支数 0，函数体节点数 44；return: await _run_sync_tool_after_async_sandbox_init(str_replace_tool.func, runtime, description, path, old_str, new_str, replace_all)
  - 调用: _run_sync_tool_after_async_sandbox_init

## 文件内调用关系
- `_is_skills_path` -> _get_skills_container_path
- `_extract_skill_name_from_skills_path` -> _get_skills_container_path, _is_skills_path
- `_is_disabled_skill_path` -> _extract_skill_name_from_skills_path, _get_skills_container_path
- `_drop_disabled_skill_paths` -> _get_skills_container_path, _extract_skill_name_from_skills_path, _is_disabled_skill_path
- `_resolve_skills_path` -> _get_skills_container_path, _get_skills_host_path, _join_path_preserving_style
- `_is_custom_mount_path` -> _get_custom_mounts
- `_get_custom_mount_for_path` -> _get_custom_mounts
- `_resolve_acp_workspace_path` -> _reject_path_traversal, _get_acp_workspace_host_path, _join_path_preserving_style
- `_resolve_max_results` -> _clamp_max_results, _get_tool_config_int
- `_resolve_local_read_path` -> validate_local_tool_path, _is_skills_path, _is_acp_workspace_path, _resolve_and_validate_user_data_path
- `_join_path_preserving_style` -> _path_separator_for_style
- `_sanitize_error` -> is_local_sandbox, get_thread_data, mask_local_paths_in_output
- `_format_write_file_error` -> _sanitize_error, _truncate_write_file_error_detail
- `replace_virtual_path` -> _thread_virtual_to_actual_mappings, _join_path_preserving_style, _path_separator_for_style
- `_thread_actual_to_virtual_mappings` -> _thread_virtual_to_actual_mappings
- `_compiled_mask_patterns` -> _path_variants
- `mask_local_paths_in_output` -> _get_skills_host_path, _get_skills_container_path, _get_acp_workspace_host_path, _extract_thread_id_from_thread_data, _thread_actual_to_virtual_mappings, _compiled_mask_patterns
- `validate_local_tool_path` -> _reject_path_traversal, _is_skills_path, _is_acp_workspace_path, _is_custom_mount_path, _get_custom_mount_for_path, _get_skills_container_path
- `_resolve_and_validate_user_data_path` -> replace_virtual_path, _validate_resolved_user_data_path
- `_has_dotdot_path_segment` -> _is_non_file_url_token
- `_is_allowed_local_bash_absolute_path` -> _reject_path_traversal, _is_skills_path, _is_acp_workspace_path, _is_custom_mount_path
- `_next_cd_target` -> _is_shell_command_separator, _is_shell_redirection_operator
- `_validate_local_bash_cwd_target` -> _reject_path_traversal, _is_allowed_local_bash_absolute_path
- `_validate_local_bash_root_path_args` -> _is_shell_command_separator, _is_shell_redirection_operator, _is_non_file_url_token
- `_validate_local_bash_shell_tokens` -> _split_shell_tokens, _is_shell_command_separator, _is_shell_redirection_operator, _has_dotdot_path_segment, _is_shell_assignment, _next_cd_target, _validate_local_bash_cwd_target, _validate_local_bash_root_path_args
- `resolve_and_validate_user_data_path` -> _resolve_and_validate_user_data_path
- `_is_non_path_literal_fragment` -> _braces_are_identifier_placeholders_only
- `validate_local_bash_command_paths` -> _get_mcp_allowed_paths, _validate_local_bash_shell_tokens, _non_file_url_spans, _is_in_spans, _is_non_path_literal_fragment, _is_allowed_local_bash_absolute_path
- `replace_virtual_paths_in_command` -> replace_virtual_path
- `_run_sync_tool_after_async_sandbox_init` -> ensure_sandbox_initialized_async, _sanitize_error
- `ensure_thread_directories_exist` -> is_local_sandbox, get_thread_data
- `bash_tool` -> ensure_sandbox_initialized, _channel_identity_prefix, _github_env_from_runtime, is_local_sandbox, ensure_thread_directories_exist, get_thread_data, validate_local_bash_command_paths, replace_virtual_paths_in_command, _apply_cwd_prefix, _is_windows, _truncate_bash_output, mask_secret_values, mask_local_paths_in_output, _sanitize_error
- `_bash_tool_async` -> _run_sync_tool_after_async_sandbox_init
- `ls_tool` -> _is_disabled_skill_path, _extract_skill_name_from_skills_path, ensure_sandbox_initialized, ensure_thread_directories_exist, is_local_sandbox, get_thread_data, validate_local_tool_path, _is_skills_path, _is_acp_workspace_path, _is_custom_mount_path, _resolve_and_validate_user_data_path, mask_local_paths_in_output, _drop_disabled_skill_paths, _truncate_ls_output, _sanitize_error
- `_ls_tool_async` -> _run_sync_tool_after_async_sandbox_init
- `glob_tool` -> _is_disabled_skill_path, _extract_skill_name_from_skills_path, ensure_sandbox_initialized, ensure_thread_directories_exist, _resolve_max_results, is_local_sandbox, get_thread_data, _resolve_local_read_path, mask_local_paths_in_output, _drop_disabled_skill_paths, _format_glob_results, _sanitize_error
- `_glob_tool_async` -> _run_sync_tool_after_async_sandbox_init
- `grep_tool` -> _is_disabled_skill_path, _extract_skill_name_from_skills_path, ensure_sandbox_initialized, ensure_thread_directories_exist, _resolve_max_results, is_local_sandbox, get_thread_data, _resolve_local_read_path, mask_local_paths_in_output, _drop_disabled_skill_paths, _format_grep_results, _sanitize_error
- `_grep_tool_async` -> _run_sync_tool_after_async_sandbox_init
- `read_current_file_content` -> ensure_sandbox_initialized, ensure_thread_directories_exist, is_local_sandbox, get_thread_data, validate_local_tool_path, _is_skills_path, _resolve_skills_path, _is_acp_workspace_path, _resolve_acp_workspace_path, _extract_thread_id_from_thread_data, _is_custom_mount_path, _resolve_and_validate_user_data_path
- `read_file_tool` -> _is_disabled_skill_path, _extract_skill_name_from_skills_path, read_current_file_content, _truncate_read_file_output, _sanitize_error
- `_read_file_tool_async` -> _run_sync_tool_after_async_sandbox_init
- `write_file_tool` -> _effective_write_file_max_bytes, ensure_sandbox_initialized, ensure_thread_directories_exist, is_local_sandbox, get_thread_data, validate_local_tool_path, _is_custom_mount_path, _resolve_and_validate_user_data_path, _format_write_file_error, _truncate_write_file_error_detail
- `_write_file_tool_async` -> _run_sync_tool_after_async_sandbox_init
- `str_replace_tool` -> ensure_sandbox_initialized, ensure_thread_directories_exist, is_local_sandbox, get_thread_data, validate_local_tool_path, _is_custom_mount_path, _resolve_and_validate_user_data_path, _sanitize_error
- `_str_replace_tool_async` -> _run_sync_tool_after_async_sandbox_init

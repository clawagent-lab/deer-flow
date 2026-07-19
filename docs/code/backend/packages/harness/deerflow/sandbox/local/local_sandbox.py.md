# `backend/packages/harness/deerflow/sandbox/local/local_sandbox.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/local/local_sandbox.py`  ·  行数: 789

## 模块概览
- 函数 0 个，类 4 个，模块级常量 4 个

## 依赖（import）
- 模块: errno, logging, ntpath, os, re, shutil, signal, subprocess, threading
- `dataclasses` -> dataclass
- `functools` -> cached_property
- `pathlib` -> Path
- `typing` -> NamedTuple
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX
- `deerflow.sandbox.env_policy` -> build_sandbox_env
- `deerflow.sandbox.local.list_dir` -> list_dir
- `deerflow.sandbox.path_patterns` -> build_output_mask_pattern
- `deerflow.sandbox.sandbox` -> Sandbox, _validate_extra_env
- `deerflow.sandbox.search` -> GrepMatch, find_glob_matches, find_grep_matches

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `DEFAULT_COMMAND_TIMEOUT_SECONDS` = 600
- `_COMMAND_CAPTURE_LIMIT_BYTES` = 10 * 1024 * 1024
- `_PIPE_DRAIN_JOIN_TIMEOUT_SECONDS` = 0.2

## 类
### 类 `_BoundedPipeCapture`  L34
- _文档首行_: Drain a subprocess pipe while keeping only bounded output in memory.
- 方法:
  #### `m` `__init__(self, *, limit_bytes: int) -> None`  L37
    - 分支数 0，函数体节点数 51
    - 调用: Lock
  #### `m` `append(self, chunk: bytes) -> None`  L44
    - 分支数 2，函数体节点数 80；return: None
    - 调用: len, append
  #### `m` `read(self) -> str`  L54
    - 分支数 2，函数体节点数 85；return: output
    - 调用: join, decode

### 类 `PathMapping`  L69  @dataclass(...)
- _文档首行_: A path mapping from a container path to a local path with optional read-only flag.
- 类/实例变量:
  - `container_path` = <annotated>
  - `local_path` = <annotated>
  - `read_only` = False

### 类 `ResolvedPath`  L77
- 继承: NamedTuple
- 类/实例变量:
  - `path` = <annotated>
  - `mapping` = <annotated>

### 类 `LocalSandbox`  L82
- 继承: Sandbox
- 方法:
  #### `st` `_shell_name(shell: str) -> str`    @staticmethod  L84
    - _文档首行_（仅供参考）: Return the executable name for a shell path or command.
    - 分支数 0，函数体节点数 32；return: shell.replace('\\', '/').rsplit('/', 1)[-1].lower()
    - 调用: lower, rsplit, replace
  - 文件IO: replace (L86)
  #### `st` `_is_powershell(shell: str) -> bool`    @staticmethod  L89
    - _文档首行_（仅供参考）: Return whether the selected shell is a PowerShell executable.
    - 分支数 0，函数体节点数 26；return: LocalSandbox._shell_name(shell) in {'powershell', 'powershell.exe', 'pwsh', 'pwsh.exe'}
    - 调用: _shell_name
  #### `st` `_is_cmd_shell(shell: str) -> bool`    @staticmethod  L94
    - _文档首行_（仅供参考）: Return whether the selected shell is cmd.exe.
    - 分支数 0，函数体节点数 24；return: LocalSandbox._shell_name(shell) in {'cmd', 'cmd.exe'}
    - 调用: _shell_name
  #### `st` `_is_msys_shell(shell: str) -> bool`    @staticmethod  L99
    - _文档首行_（仅供参考）: Return whether the selected shell is a Git Bash/MSYS shell.
    - 分支数 0，函数体节点数 62；return: shell_name in {'sh.exe', 'bash.exe'} and any((part in normalized for part in ('/git/', '/mingw', '/msys')))
    - 调用: lower, replace, _shell_name, any
  - 文件IO: replace (L101)
  #### `st` `_find_first_available_shell(candidates: tuple[str, ...]) -> str | None`    @staticmethod  L106
    - _文档首行_（仅供参考）: Return the first executable shell path or command found from candidates.
    - 分支数 4，函数体节点数 84；return: shell, shell_from_path, None
    - 调用: isabs, isfile, access, which
  #### `st` `_format_timeout_duration(timeout: float) -> str`    @staticmethod  L121
    - 分支数 1，函数体节点数 63；return: f'{amount} {unit}'
    - 调用: float, is_integer, str, int
  #### `st` `_format_timeout_notice(timeout: float) -> str`    @staticmethod  L131
    - 分支数 0，函数体节点数 21；return: f'Command timed out after {LocalSandbox._format_timeout_duration(timeout)} and was terminated. To run a long-lived process such as a web server, start it in the background and redirect its output, e.g. `your-command > /mnt/user-data/workspace/server.log 2>&1 &`.'
    - 调用: _format_timeout_duration
  #### `st` `_coerce_process_output(value: str | bytes | None) -> str`    @staticmethod  L139
    - 分支数 2，函数体节点数 44；return: '', value.decode('utf-8', errors='replace'), value
    - 调用: isinstance, decode
  #### `st` `_drain_pipe(fd: int, capture: _BoundedPipeCapture) -> None`    @staticmethod  L147
    - 分支数 3，函数体节点数 57
    - 调用: read, append, debug, close
  - 文件IO: read (L149)
  #### `st` `_start_pipe_drain(fd: int, name: str) -> tuple[_BoundedPipeCapture, threading.Thread]`    @staticmethod  L161
    - 分支数 0，函数体节点数 66；return: (capture, thread)
    - 调用: _BoundedPipeCapture, Thread, start
  #### `st` `_process_group_exists(pgid: int | None) -> bool`    @staticmethod  L168
    - 分支数 2，函数体节点数 47；return: False, True
    - 调用: killpg
  #### `st` `_get_shell() -> str`    @staticmethod  L441
    - _文档首行_（仅供参考）: Detect available shell executable with fallback.
    - 分支数 3，函数体节点数 96；raise: RuntimeError('No suitable shell executable found. Tried /bin/zsh, /bin/bash, /bin/sh, `sh` on PATH, then PowerShell and cmd.exe fallbacks for Windows.'), RuntimeError('No suitable shell executable found. Tried /bin/zsh, /bin/bash, /bin/sh, and `sh` on PATH.')；return: shell
    - 调用: _find_first_available_shell, get, join, RuntimeError
  #### `st` `_run_posix_command(args: list[str], timeout: float, env: dict[str, str] | None) -> tuple[str, str, int, bool]`    @staticmethod  L538
    - _文档首行_（仅供参考）: Run a command on POSIX with bounded pipe capture.
    - 分支数 10，函数体节点数 326；raise: bare raise；return: (stdout, stderr, returncode, timed_out)
    - 调用: pipe, Popen, close, _start_pipe_drain, getpgid, wait, _terminate_process_group, _process_group_exists, join, is_alive, debug, read
  - 文件IO: read (L612), read (L613)
  - 子进程: Popen (L566)
  #### `st` `_terminate_process_group(process: subprocess.Popen) -> None`    @staticmethod  L617
    - _文档首行_（仅供参考）: Kill the command's whole process group, then reap it.
    - 分支数 3，函数体节点数 87
    - 调用: killpg, getpgid, kill, debug, wait, warning
  #### `m` `__init__(self, id: str, path_mappings: list[PathMapping] | None)`  L181
    - _文档首行_（仅供参考）: Initialize local sandbox with optional path mappings.
    - 分支数 0，函数体节点数 53
    - 调用: __init__, super, set
  #### `m` `_command_pattern(self) -> re.Pattern[str] | None`    @cached_property  L202
    - _文档首行_（仅供参考）: Compiled matcher for container paths in shell commands (shell-aware boundaries).
    - 分支数 1，函数体节点数 91；return: None, re.compile('|'.join((f'({p})' for p in patterns)))
    - 调用: sorted, len, escape, compile, join
  - 危险执行: compile (L210)
  #### `m` `_content_pattern(self) -> re.Pattern[str] | None`    @cached_property  L213
    - _文档首行_（仅供参考）: Compiled matcher for container paths in plain file content (text boundaries).
    - 分支数 1，函数体节点数 91；return: None, re.compile('|'.join((f'({p})' for p in patterns)))
    - 调用: sorted, len, escape, compile, join
  - 危险执行: compile (L219)
  #### `m` `_reverse_output_patterns(self) -> list[re.Pattern[str]]`    @cached_property  L222
    - _文档首行_（仅供参考）: Compiled matchers for local paths in command output (longest local path first).
    - 分支数 0，函数体节点数 39；return: [build_output_mask_pattern(self._resolved_local_paths[m]) for m in self._mappings_by_local_specificity]
    - 调用: build_output_mask_pattern
  #### `m` `_resolved_local_paths(self) -> dict[PathMapping, str]`    @cached_property  L242
    - _文档首行_（仅供参考）: Filesystem-resolved local root per mapping. ``Path.resolve()`` hits the
    - 分支数 0，函数体节点数 41；return: {m: str(Path(m.local_path).resolve()) for m in self.path_mappings}
    - 调用: str, resolve, Path
  #### `m` `_mappings_by_container_specificity(self) -> list[PathMapping]`    @cached_property  L248
    - _文档首行_（仅供参考）: Mappings ordered most-specific-container-first (for forward resolution).
    - 分支数 0，函数体节点数 41；return: sorted(self.path_mappings, key=lambda m: len(m.container_path.rstrip('/') or '/'), reverse=True)
    - 调用: sorted, len, rstrip
  #### `m` `_mappings_by_local_specificity(self) -> list[PathMapping]`    @cached_property  L253
    - _文档首行_（仅供参考）: Mappings ordered longest-local-path-first (for reverse resolution).
    - 分支数 0，函数体节点数 34；return: sorted(self.path_mappings, key=lambda m: len(m.local_path), reverse=True)
    - 调用: sorted, len
  #### `m` `_is_read_only_path(self, resolved_path: str) -> bool`  L257
    - _文档首行_（仅供参考）: Check if a resolved path is under a read-only mount.
    - 分支数 4，函数体节点数 117；return: False, best_mapping.read_only
    - 调用: str, resolve, Path, startswith, len
  #### `m` `_find_path_mapping(self, path: str) -> tuple[PathMapping, str] | None`  L282
    - 分支数 4，函数体节点数 118；return: (mapping, path_str.lstrip('/')), (mapping, relative), None
    - 调用: str, rstrip, startswith, lstrip, len
  #### `m` `_resolve_path_with_mapping(self, path: str) -> ResolvedPath`  L298
    - _文档首行_（仅供参考）: Resolve container path to actual local path using mappings.
    - 分支数 2，函数体节点数 117；raise: PermissionError(errno.EACCES, 'Access denied: path escapes mounted directory', path_str)；return: ResolvedPath(path_str, None), ResolvedPath(str(resolved_path), mapping)
    - 调用: str, _find_path_mapping, ResolvedPath, Path, resolve, relative_to, PermissionError
  #### `m` `_resolve_path(self, path: str) -> str`  L325
    - 分支数 0，函数体节点数 18；return: self._resolve_path_with_mapping(path).path
    - 调用: _resolve_path_with_mapping
  #### `m` `_is_resolved_path_read_only(self, resolved: ResolvedPath) -> bool`  L328
    - 分支数 0，函数体节点数 35；return: bool(resolved.mapping and resolved.mapping.read_only) or self._is_read_only_path(resolved.path)
    - 调用: bool, _is_read_only_path
  #### `m` `_reverse_resolve_path(self, path: str) -> str`  L331
    - _文档首行_（仅供参考）: Reverse resolve local path back to container path using mappings.
    - 分支数 2，函数体节点数 128；return: resolved, path_str
    - 调用: replace, str, resolve, Path, startswith, lstrip, len
  - 文件IO: replace (L341), replace (L360)
  #### `m` `_reverse_resolve_paths_in_output(self, output: str) -> str`  L367
    - _文档首行_（仅供参考）: Reverse resolve local paths back to container paths in output string.
    - 分支数 1，函数体节点数 63；return: self._reverse_resolve_path(matched_path), result
    - 调用: group, _reverse_resolve_path, sub
  #### `m` `_resolve_paths_in_command(self, command: str) -> str`  L390
    - _文档首行_（仅供参考）: Resolve container paths to local paths in a command string.
    - 分支数 1，函数体节点数 67；return: command, self._resolve_path(matched_path).replace('\\', '/'), pattern.sub(replace_match, command)
    - 调用: group, replace, _resolve_path, sub
  - 文件IO: replace (L408)
  #### `m` `_resolve_paths_in_content(self, content: str) -> str`  L412
    - _文档首行_（仅供参考）: Resolve container paths to local paths in arbitrary file content.
    - 分支数 1，函数体节点数 72；return: content, resolved.replace('\\', '/'), pattern.sub(replace_match, content)
    - 调用: group, _resolve_path, replace, sub
  - 文件IO: replace (L436)
  #### `m` `execute_command(self, command: str, env: dict[str, str] | None, timeout: float | None) -> str`  L466
    - 分支数 9，函数体节点数 358；return: self._reverse_resolve_paths_in_output(final_output)
    - 调用: _validate_extra_env, _resolve_paths_in_command, _get_shell, build_sandbox_env, _is_powershell, _is_cmd_shell, _is_msys_shell, run, _coerce_process_output, _run_posix_command, _format_timeout_notice, _reverse_resolve_paths_in_output
  - 子进程: run (L506)
  #### `m` `list_dir(self, path: str, max_depth) -> list[str]`  L639
    - 分支数 6，函数体节点数 238；return: sorted(result)
    - 调用: _resolve_path, list_dir, endswith, _reverse_resolve_path, rstrip, append, startswith, len, is_dir, resolve, Path, sorted
  #### `m` `read_file(self, path: str) -> str`  L681
    - 分支数 3，函数体节点数 81；raise: type(e)(e.errno, e.strerror, path)；return: content
    - 调用: _resolve_path, open, read, _reverse_resolve_paths_in_output, type(e), type
  - 文件IO: open (L684), read (L685)
  #### `m` `download_file(self, path: str) -> bytes`  L697
    - 分支数 4，函数体节点数 177；raise: PermissionError(errno.EACCES, f"Access denied: path must be under '{VIRTUAL_PATH_PREFIX}'", path), OSError(errno.EFBIG, f'File exceeds maximum download size of {max_download_size} bytes', path), type(e)(e.errno, e.strerror, path)；return: f.read()
    - 调用: replace, lstrip, startswith, error, PermissionError, _resolve_path, getsize, OSError, open, read, type(e), type
  - 文件IO: replace (L698), open (L713), read (L714)
  #### `m` `write_file(self, path: str, content: str, append: bool) -> None`  L719
    - 分支数 4，函数体节点数 146；raise: OSError(errno.EROFS, 'Read-only file system', path), type(e)(e.errno, e.strerror, path)
    - 调用: _resolve_path_with_mapping, _is_resolved_path_read_only, OSError, dirname, makedirs, _resolve_paths_in_content, open, write, add, type(e), type
  - 文件IO: open (L732), write (L733)
  #### `m` `glob(self, path: str, pattern: str, *, include_dirs: bool, max_results: int) -> tuple[list[str], bool]`  L742
    - 分支数 0，函数体节点数 82；return: ([self._reverse_resolve_path(match) for match in matches], truncated)
    - 调用: Path, _resolve_path, find_glob_matches, _reverse_resolve_path
  #### `m` `grep(self, path: str, pattern: str, *, glob: str | None, literal: bool, case_sensitive: bool, max_results: int) -> tuple[list[GrepMatch], bool]`  L747
    - 分支数 0，函数体节点数 115；return: ([GrepMatch(path=self._reverse_resolve_path(match.path), line_number=match.line_number, line=match.line) for match in matches], truncated)
    - 调用: Path, _resolve_path, find_grep_matches, GrepMatch, _reverse_resolve_path
  #### `m` `update_file(self, path: str, content: bytes) -> None`  L775
    - 分支数 4，函数体节点数 111；raise: OSError(errno.EROFS, 'Read-only file system', path), type(e)(e.errno, e.strerror, path)
    - 调用: _resolve_path_with_mapping, _is_resolved_path_read_only, OSError, dirname, makedirs, open, write, type(e), type
  - 文件IO: open (L784), write (L785)

## 文件内调用关系
- `_BoundedPipeCapture.append` -> append
- `LocalSandbox._is_powershell` -> _shell_name
- `LocalSandbox._is_cmd_shell` -> _shell_name
- `LocalSandbox._is_msys_shell` -> _shell_name
- `LocalSandbox._format_timeout_notice` -> _format_timeout_duration
- `LocalSandbox._drain_pipe` -> read, append
- `LocalSandbox.__init__` -> __init__
- `LocalSandbox._resolve_path_with_mapping` -> _find_path_mapping
- `LocalSandbox._resolve_path` -> _resolve_path_with_mapping
- `LocalSandbox._is_resolved_path_read_only` -> _is_read_only_path
- `LocalSandbox._reverse_resolve_paths_in_output` -> _reverse_resolve_path
- `LocalSandbox._resolve_paths_in_command` -> _resolve_path
- `LocalSandbox._resolve_paths_in_content` -> _resolve_path
- `LocalSandbox._get_shell` -> _find_first_available_shell
- `LocalSandbox.execute_command` -> _resolve_paths_in_command, _get_shell, _is_powershell, _is_cmd_shell, _is_msys_shell, _coerce_process_output, _run_posix_command, _format_timeout_notice, _reverse_resolve_paths_in_output
- `LocalSandbox._run_posix_command` -> _start_pipe_drain, _terminate_process_group, _process_group_exists, read
- `LocalSandbox.list_dir` -> _resolve_path, list_dir, _reverse_resolve_path, append
- `LocalSandbox.read_file` -> _resolve_path, read, _reverse_resolve_paths_in_output
- `LocalSandbox.download_file` -> _resolve_path, read
- `LocalSandbox.write_file` -> _resolve_path_with_mapping, _is_resolved_path_read_only, _resolve_paths_in_content
- `LocalSandbox.glob` -> _resolve_path, _reverse_resolve_path
- `LocalSandbox.grep` -> _resolve_path, _reverse_resolve_path
- `LocalSandbox.update_file` -> _resolve_path_with_mapping, _is_resolved_path_read_only

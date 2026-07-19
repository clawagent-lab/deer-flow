# `backend/packages/harness/deerflow/community/aio_sandbox/aio_sandbox.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/aio_sandbox/aio_sandbox.py`  ·  行数: 466

## 模块概览
- 函数 0 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: base64, errno, logging, shlex, threading, uuid
- `agent_sandbox` -> AioSandboxClient
- `agent_sandbox.core.api_error` -> ApiError
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX
- `deerflow.sandbox.sandbox` -> Sandbox, _validate_extra_env
- `deerflow.sandbox.search` -> GrepMatch, path_matches, should_ignore_path, truncate_line

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_MAX_DOWNLOAD_SIZE` = 100 * 1024 * 1024
- `_ERROR_OBSERVATION_SIGNATURE` = "'ErrorObservation' object has no attribute 'exit_code'"
- `_BASH_EXEC_UNSUPPORTED_ERROR` = 'Error: this sandbox image does not support per-command e...

## 类
### 类 `AioSandbox`  L35
- 继承: Sandbox
- _文档首行_: Sandbox implementation using the agent-infra/sandbox Docker container.
- 类/实例变量:
  - `_DEFAULT_NO_CHANGE_TIMEOUT` = 600
  - `_DEFAULT_HARD_TIMEOUT` = 600.0
- 方法:
  #### `prop` `base_url(self) -> str`    @property  L62
    - 分支数 0，函数体节点数 12；return: self._base_url
  #### `prop` `home_dir(self) -> str`    @property  L117
    - _文档首行_（仅供参考）: Get the home directory inside the sandbox.
    - 分支数 1，函数体节点数 43；return: self._home_dir
    - 调用: get_context
  #### `m` `__init__(self, id: str, base_url: str, home_dir: str | None)`  L43
    - _文档首行_（仅供参考）: Initialize the AIO sandbox.
    - 分支数 0，函数体节点数 76
    - 调用: __init__, super, AioSandboxClient, Lock
  #### `m` `close(self) -> None`  L65
    - _文档首行_（仅供参考）: Best-effort close of the host-side HTTP client owned by this sandbox.
    - 分支数 5，函数体节点数 153；return: None
    - 调用: getattr, next, hasattr, debug, close, warning
  - 反射: getattr (L100), getattr (L101), getattr (L102), hasattr (L104)
  #### `m` `execute_command(self, command: str, env: dict[str, str] | None, timeout: float | None) -> str`  L140
    - _文档首行_（仅供参考）: Execute a shell command in the sandbox.
    - 分支数 6，函数体节点数 235；return: self._execute_with_env(command, env), output if output else '(no output)', f'Error: {e}'
    - 调用: _validate_extra_env, _execute_with_env, exec_command, warning, str, uuid4, create_session, cleanup_session, error
  #### `m` `_execute_with_env(self, command: str, env: dict[str, str]) -> str`  L208
    - _文档首行_（仅供参考）: Execute a command with per-call environment variables injected.
    - 分支数 3，函数体节点数 88；return: _BASH_EXEC_UNSUPPORTED_ERROR, retried, output
    - 调用: _run_bash_exec, warning
  #### `m` `_run_bash_exec(self, command: str, env: dict[str, str]) -> str`  L246
    - _文档首行_（仅供参考）: Single bash.exec invocation with injected env (one fresh session).
    - 分支数 4，函数体节点数 187；return: output if output else '(no output)', _BASH_EXEC_UNSUPPORTED_ERROR, f'Error: {e}'
    - 调用: exec, error
  - 危险执行: exec (L250)
  #### `m` `read_file(self, path: str) -> str`  L273
    - _文档首行_（仅供参考）: Read the content of a file in the sandbox.
    - 分支数 1，函数体节点数 59；return: result.data.content if result.data else '', f'Error: {e}'
    - 调用: read_file, error
  #### `m` `download_file(self, path: str) -> bytes`  L289
    - _文档首行_（仅供参考）: Download file bytes from the sandbox.
    - 分支数 7，函数体节点数 237；raise: PermissionError(f"Access denied: path traversal detected in '{path}'"), PermissionError(f"Access denied: path must be under '{VIRTUAL_PATH_PREFIX}': '{path}'"), OSError(errno.EFBIG, f'File exceeds maximum download size of {_MAX_DOWNLOAD_SIZE} bytes', path), bare raise, OSError(f"Failed to download file '{path}' from sandbox: {e}")；return: b''.join(chunks)
    - 调用: replace, split, error, PermissionError, lstrip, startswith, download_file, len, OSError, append, join
  - 文件IO: replace (L300)
  #### `m` `list_dir(self, path: str, max_depth: int) -> list[str]`  L332
    - _文档首行_（仅供参考）: List the contents of a directory in the sandbox.
    - 分支数 3，函数体节点数 120；return: [line.strip() for line in output.strip().split('\n') if line.strip()], []
    - 调用: exec_command, quote, strip, split, error
  #### `m` `write_file(self, path: str, content: str, append: bool) -> None`  L353
    - _文档首行_（仅供参考）: Write content to a file in the sandbox.
    - 分支数 4，函数体节点数 85；raise: bare raise
    - 调用: read_file, startswith, write_file, error
  #### `m` `glob(self, path: str, pattern: str, *, include_dirs: bool, max_results: int) -> tuple[list[str], bool]`  L372
    - 分支数 6，函数体节点数 298；return: (filtered[:max_results], truncated), (matches, True), (matches, False)
    - 调用: find_files, should_ignore_path, len, list_path, rstrip, startswith, lstrip, path_matches, append
  #### `m` `grep(self, path: str, pattern: str, *, glob: str | None, literal: bool, case_sensitive: bool, max_results: int) -> tuple[list[GrepMatch], bool]`  L397
    - 分支数 6，函数体节点数 351；return: (matches, truncated)
    - 调用: escape, compile, find_files, list_path, should_ignore_path, search_in_file, zip, append, GrepMatch, isinstance, truncate_line, len
  - 危险执行: compile (L413)
  #### `m` `update_file(self, path: str, content: bytes) -> None`  L452
    - _文档首行_（仅供参考）: Update a file with binary content in the sandbox.
    - 分支数 2，函数体节点数 66；raise: bare raise
    - 调用: decode, b64encode, write_file, error

## 文件内调用关系
- `AioSandbox.__init__` -> __init__
- `AioSandbox.close` -> close
- `AioSandbox.execute_command` -> _execute_with_env
- `AioSandbox._execute_with_env` -> _run_bash_exec
- `AioSandbox.read_file` -> read_file
- `AioSandbox.download_file` -> download_file
- `AioSandbox.write_file` -> read_file, write_file
- `AioSandbox.update_file` -> write_file

# `backend/packages/harness/deerflow/community/e2b_sandbox/e2b_sandbox.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/e2b_sandbox/e2b_sandbox.py`  ·  行数: 475

## 模块概览
- 函数 1 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: errno, logging, re, shlex, threading
- `__future__` -> annotations
- `e2b_code_interpreter` -> E2BClientSandbox
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX
- `deerflow.sandbox.sandbox` -> Sandbox, _validate_extra_env
- `deerflow.sandbox.search` -> GrepMatch, path_matches, should_ignore_path, truncate_line

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_MAX_DOWNLOAD_SIZE` = 100 * 1024 * 1024
- `DEFAULT_E2B_HOME_DIR` = '/home/user'
- `_E2B_NOT_FOUND_SIGNATURES` = ('sandbox was not found', 'sandbox not found', 'paused sa...

## 函数
#### `ƒ` `_is_sandbox_gone_error(exc: BaseException) -> bool`  L31
  - 分支数 0，函数体节点数 34；return: any((sig in msg for sig in _E2B_NOT_FOUND_SIGNATURES))
  - 调用: lower, str, any

## 类
### 类 `E2BSandbox`  L36
- 继承: Sandbox
- _文档首行_: DeerFlow Sandbox adapter that delegates to an e2b cloud sandbox.
- 方法:
  #### `prop` `client(self) -> E2BClientSandbox`    @property  L67
    - 分支数 0，函数体节点数 12；return: self._client
  #### `prop` `home_dir(self) -> str`    @property  L71
    - 分支数 0，函数体节点数 12；return: self._home_dir
  #### `prop` `sandbox_id(self) -> str`    @property  L75
    - _文档首行_（仅供参考）: e2b-side sandbox id (different from DeerFlow's ``self.id`` cache key).
    - 分支数 0，函数体节点数 22；return: getattr(self._client, 'sandbox_id', self.id)
    - 调用: getattr
  - 反射: getattr (L77)
  #### `prop` `is_dead(self) -> bool`    @property  L174
    - _文档首行_（仅供参考）: Whether the underlying e2b VM is known to be reaped.
    - 分支数 1，函数体节点数 20；return: self._dead
  #### `m` `__init__(self, id: str, client: E2BClientSandbox, *, home_dir: str) -> None`  L50
    - 分支数 0，函数体节点数 67
    - 调用: __init__, super, rstrip, Lock
  #### `m` `close(self) -> None`  L79
    - 分支数 6，函数体节点数 94；return: None
    - 调用: getattr, callable, closer, warning
  - 反射: getattr (L91), getattr (L92), getattr (L92)
  #### `m` `_resolve_path(self, path: str) -> str`  L101
    - _文档首行_（仅供参考）: Map DeerFlow virtual paths into the e2b sandbox filesystem.
    - 分支数 4，函数体节点数 116；raise: ValueError('path must be a non-empty string'), PermissionError(f"Access denied: path traversal detected in '{path}'")；return: f'{self._home_dir}/{tail}'.rstrip('/') if tail else self._home_dir, normalised
    - 调用: ValueError, replace, split, PermissionError, startswith, lstrip, len, rstrip
  - 文件IO: replace (L112)
  #### `m` `execute_command(self, command: str, env: dict[str, str] | None, timeout: float | None) -> str`  L121
    - _文档首行_（仅供参考）: Execute a shell command via ``sandbox.commands.run``.
    - 分支数 9，函数体节点数 247；return: 'Error: sandbox client has been closed', 'Error: e2b sandbox has been reaped by the control plane (idle timeout or explicit pause). The provider will rebuild a fresh sandbox on the next tool call.', output if output else '(no output)', f'Error: {e}'
    - 调用: _validate_extra_env, run, getattr, _is_sandbox_gone_error, error
  - 子进程: run (L156)
  - 反射: getattr (L157), getattr (L158), getattr (L159)
  #### `m` `ping(self) -> bool`  L184
    - _文档首行_（仅供参考）: Cheap health check: returns False if the e2b VM has been reaped.
    - 分支数 5，函数体节点数 82；return: False, True
    - 调用: run, _is_sandbox_gone_error, warning
  - 子进程: run (L198)
  #### `m` `read_file(self, path: str) -> str`  L208
    - 分支数 2，函数体节点数 80；return: content.decode('utf-8', errors='replace'), content if content is not None else '', f'Error: {e}'
    - 调用: _resolve_path, read, isinstance, decode, error
  - 文件IO: read (L211)
  #### `m` `download_file(self, path: str) -> bytes`  L219
    - 分支数 19，函数体节点数 490；raise: PermissionError(f"Access denied: path traversal detected in '{path}'"), PermissionError(f"Access denied: path must be under '{VIRTUAL_PATH_PREFIX}': '{path}'"), RuntimeError('sandbox client has been closed'), OSError(f"Failed to download file '{path}' from sandbox: {e}"), OSError(errno.EFBIG, f'File exceeds maximum download size of {_MAX_DOWNLOAD_SIZE} bytes', path), bare raise；return: b'', bytes(data), encoded, b''.join(chunks)
    - 调用: replace, split, error, PermissionError, lstrip, startswith, _resolve_path, RuntimeError, read, OSError, isinstance, len, bytes, encode, getattr, append, callable, close, join
  - 文件IO: replace (L220), read (L250), read (L253)
  - 反射: getattr (L286)
  #### `m` `list_dir(self, path: str, max_depth: int) -> list[str]`  L314
    - 分支数 3，函数体节点数 127；return: [], [line.strip() for line in output.splitlines() if line.strip()]
    - 调用: _resolve_path, run, quote, int, getattr, strip, splitlines, error
  - 子进程: run (L321)
  - 反射: getattr (L322)
  #### `m` `write_file(self, path: str, content: str, append: bool) -> None`  L328
    - 分支数 6，函数体节点数 137；raise: RuntimeError('sandbox client has been closed'), bare raise
    - 调用: _resolve_path, RuntimeError, read, isinstance, decode, write, error
  - 文件IO: read (L338), write (L344)
  #### `m` `update_file(self, path: str, content: bytes) -> None`  L349
    - 分支数 3，函数体节点数 72；raise: RuntimeError('sandbox client has been closed'), bare raise
    - 调用: _resolve_path, RuntimeError, write, error
  - 文件IO: write (L358)
  #### `m` `glob(self, path: str, pattern: str, *, include_dirs: bool, max_results: int) -> tuple[list[str], bool]`  L363
    - 分支数 10，函数体节点数 324；return: ([], False), (matches, True), (matches, False)
    - 调用: _resolve_path, max, quote, join, split, run, getattr, error, rstrip, splitlines, strip, startswith, should_ignore_path, lstrip, len, path_matches, append
  - 子进程: run (L380)
  - 反射: getattr (L381)
  #### `m` `grep(self, path: str, pattern: str, *, glob: str | None, literal: bool, case_sensitive: bool, max_results: int) -> tuple[list[GrepMatch], bool]`  L406
    - 分支数 11，函数体节点数 409；return: ([], False), (matches, truncated)
    - 调用: escape, compile, _resolve_path, append, split, max, join, quote, run, getattr, error, splitlines, int, should_ignore_path, GrepMatch, truncate_line, len
  - 子进程: run (L445)
  - 危险执行: compile (L417)
  - 反射: getattr (L446)

## 文件内调用关系
- `E2BSandbox.__init__` -> __init__
- `E2BSandbox.execute_command` -> _is_sandbox_gone_error
- `E2BSandbox.ping` -> _is_sandbox_gone_error
- `E2BSandbox.read_file` -> _resolve_path
- `E2BSandbox.download_file` -> _resolve_path, close
- `E2BSandbox.list_dir` -> _resolve_path
- `E2BSandbox.write_file` -> _resolve_path
- `E2BSandbox.update_file` -> _resolve_path
- `E2BSandbox.glob` -> _resolve_path
- `E2BSandbox.grep` -> _resolve_path

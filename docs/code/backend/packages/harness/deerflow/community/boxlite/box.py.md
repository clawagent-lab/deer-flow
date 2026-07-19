# `backend/packages/harness/deerflow/community/boxlite/box.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/boxlite/box.py`  ·  行数: 361

**模块文档首行**（仅供参考）: ``BoxliteBox`` — DeerFlow :class:`Sandbox` backed by a BoxLite micro-VM.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: base64, errno, logging, posixpath, re, shlex, threading
- `__future__` -> annotations
- `typing` -> TYPE_CHECKING, TypeVar
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX
- `deerflow.sandbox.sandbox` -> Sandbox, _validate_extra_env
- `deerflow.sandbox.search` -> GrepMatch, path_matches, should_ignore_path, truncate_line

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `T` = TypeVar('T')
- `_MAX_DOWNLOAD_SIZE` = 100 * 1024 * 1024
- `_B64_CHUNK` = 60000

## 类
### 类 `BoxliteBox`  L47
- 继承: Sandbox
- _文档首行_: Adapter that delegates to a running BoxLite ``SimpleBox``.
- 类/实例变量:
  - `TERMINAL_ERROR_MARKERS` = ('vsock', 'disconnected', 'broken pipe', 'connection rese...
  - `RETRYABLE_ERROR_MARKERS` = ('transport not ready', 'retry later', 'temporarily unava...
- 方法:
  #### `prop` `is_closed(self) -> bool`    @property  L146
    - 分支数 1，函数体节点数 18；return: self._closed
  #### `cls` `_is_terminal_box_failure(cls, error: Exception) -> bool`    @classmethod  L95
    - 分支数 3，函数体节点数 91；return: True, False, any((marker in msg for marker in cls.TERMINAL_ERROR_MARKERS))
    - 调用: isinstance, lower, str, any
  #### `st` `_guard_traversal(path: str) -> str`    @staticmethod  L153
    - 分支数 3，函数体节点数 57；raise: ValueError('path must be a non-empty string'), PermissionError(f"Access denied: path traversal detected in '{path}'")；return: normalized
    - 调用: ValueError, replace, split, PermissionError
  - 文件IO: replace (L156)
  #### `m` `__init__(self, id: str, box: SimpleBox, run: Callable[..., T], *, default_env: dict[str, str] | None, on_terminal_failure: Callable[[str, str], None] | None) -> None`  L77
    - 分支数 0，函数体节点数 112
    - 调用: __init__, super, dict, Lock
  #### `m` `_exec(self, *argv, env: dict[str, str] | None, timeout: float | None)`  L107
    - 分支数 5，函数体节点数 127；可变参数（*args/**kwargs）；raise: RuntimeError('sandbox has been closed'), bare raise；return: self._run(box.exec(*argv, env=env, timeout=timeout), timeout=timeout)
    - 调用: RuntimeError, _run, exec, _is_terminal_box_failure, _on_terminal_failure, str, exception
  - 危险执行: exec (L118)
  #### `m` `_sh(self, script: str, env: dict[str, str] | None, timeout: float | None)`  L127
    - 分支数 0，函数体节点数 44；return: self._exec('sh', '-lc', script, env=env, timeout=timeout)
    - 调用: _exec
  #### `m` `close(self) -> None`  L135
    - 分支数 3，函数体节点数 52；return: None
    - 调用: _run, stop, warning
  #### `m` `_resolve_path(self, path: str) -> str`  L162
    - 分支数 0，函数体节点数 16；return: self._guard_traversal(path)
    - 调用: _guard_traversal
  #### `m` `execute_command(self, command: str, env: dict[str, str] | None, timeout: float | None) -> str`  L169
    - _文档首行_（仅供参考）: Run ``command`` through a shell in the box and return its output.
    - 分支数 4，函数体节点数 183；return: 'Error: sandbox has been closed', f'Error: {e}', output if output else '(no output)'
    - 调用: _validate_extra_env, _exec, error
  #### `m` `read_file(self, path: str) -> str`  L208
    - 分支数 2，函数体节点数 87；return: f'Error: {e}', f"Error: {(r.stderr or '').strip() or 'cannot read file'}", r.stdout or ''
    - 调用: _resolve_path, _exec, error, strip
  #### `m` `write_file(self, path: str, content: str, append: bool) -> None`  L219
    - 分支数 0，函数体节点数 36
    - 调用: _write_bytes, _resolve_path, encode
  #### `m` `update_file(self, path: str, content: bytes) -> None`  L222
    - 分支数 0，函数体节点数 27
    - 调用: _write_bytes, _resolve_path
  #### `m` `_write_bytes(self, resolved: str, data: bytes, *, append: bool) -> None`  L225
    - 分支数 6，函数体节点数 268；raise: OSError(f"cannot create parent of '{resolved}': {(mk.stderr or '').strip()}"), OSError(f"write '{resolved}' failed: {(r.stderr or '').strip()}")；return: None
    - 调用: dirname, _sh, quote, OSError, strip, decode, b64encode, range, len
  #### `m` `download_file(self, path: str) -> bytes`  L248
    - 分支数 6，函数体节点数 263；raise: PermissionError(f"Access denied: path must be under '{VIRTUAL_PATH_PREFIX}': '{path}'"), OSError(f"cannot read '{path}' from box: {(size_r.stderr or '').strip() or 'not found'}"), OSError(errno.EFBIG, f'File exceeds maximum download size of {_MAX_DOWNLOAD_SIZE} bytes', path), OSError(f"cannot read '{path}' from box: {(r.stderr or '').strip()}"), OSError(f"failed to decode '{path}' from box: {e}")；return: base64.b64decode(''.join((r.stdout or '').split()))
    - 调用: _guard_traversal, lstrip, startswith, PermissionError, _sh, quote, OSError, strip, int, b64decode, join, split
  #### `m` `list_dir(self, path: str, max_depth: int) -> list[str]`  L274
    - 分支数 0，函数体节点数 77；return: [line.strip() for line in (r.stdout or '').splitlines() if line.strip()]
    - 调用: _resolve_path, _sh, quote, int, strip, splitlines
  #### `m` `glob(self, path: str, pattern: str, *, include_dirs: bool, max_results: int) -> tuple[list[str], bool]`  L279
    - 分支数 6，函数体节点数 267；return: (matches, True), (matches, False)
    - 调用: _resolve_path, join, max, _sh, quote, rstrip, splitlines, strip, startswith, should_ignore_path, lstrip, len, path_matches, append
  #### `m` `grep(self, path: str, pattern: str, *, glob: str | None, literal: bool, case_sensitive: bool, max_results: int) -> tuple[list[GrepMatch], bool]`  L311
    - 分支数 8，函数体节点数 317；return: (matches, truncated)
    - 调用: compile, _resolve_path, append, max, join, quote, _sh, split, splitlines, int, should_ignore_path, path_matches, basename, GrepMatch, truncate_line, len
  - 危险执行: compile (L325)

## 文件内调用关系
- `BoxliteBox.__init__` -> __init__
- `BoxliteBox._exec` -> _is_terminal_box_failure
- `BoxliteBox._sh` -> _exec
- `BoxliteBox._resolve_path` -> _guard_traversal
- `BoxliteBox.execute_command` -> _exec
- `BoxliteBox.read_file` -> _resolve_path, _exec
- `BoxliteBox.write_file` -> _write_bytes, _resolve_path
- `BoxliteBox.update_file` -> _write_bytes, _resolve_path
- `BoxliteBox._write_bytes` -> _sh
- `BoxliteBox.download_file` -> _guard_traversal, _sh
- `BoxliteBox.list_dir` -> _resolve_path, _sh
- `BoxliteBox.glob` -> _resolve_path, _sh
- `BoxliteBox.grep` -> _resolve_path, _sh

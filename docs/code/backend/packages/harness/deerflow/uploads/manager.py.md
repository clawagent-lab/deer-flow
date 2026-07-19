# `backend/packages/harness/deerflow/uploads/manager.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/uploads/manager.py`  ·  行数: 365

**模块文档首行**（仅供参考）: Shared upload management logic.

## 模块概览
- 函数 17 个，类 2 个，模块级常量 4 个

## 依赖（import）
- 模块: errno, logging, os, re, stat
- `pathlib` -> Path
- `urllib.parse` -> quote
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX, get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SAFE_THREAD_ID` = re.compile('^[a-zA-Z0-9._-]+$')
- `UPLOAD_STAGING_PREFIX` = '.upload-'
- `UPLOAD_STAGING_SUFFIX` = '.part'

## 函数
#### `ƒ` `validate_thread_id(thread_id: str) -> None`  L35
  - _文档首行_（仅供参考）: Reject thread IDs containing characters unsafe for filesystem paths.
  - 分支数 1，函数体节点数 33；raise: ValueError(f'Invalid thread_id: {thread_id!r}')
  - 调用: match, ValueError

#### `ƒ` `get_uploads_dir(thread_id: str, *, user_id: str | None) -> Path`  L45
  - _文档首行_（仅供参考）: Return the uploads directory path for a thread (no side effects).
  - 分支数 0，函数体节点数 39；return: get_paths().sandbox_uploads_dir(thread_id, user_id=user_id or get_effective_user_id())
  - 调用: validate_thread_id, sandbox_uploads_dir, get_paths, get_effective_user_id

#### `ƒ` `ensure_uploads_dir(thread_id: str, *, user_id: str | None) -> Path`  L51
  - _文档首行_（仅供参考）: Return the uploads directory for a thread, creating it if needed.
  - 分支数 0，函数体节点数 40；return: base
  - 调用: get_uploads_dir, mkdir
  - 文件IO: mkdir (L54)

#### `ƒ` `normalize_filename(filename: str) -> str`  L58
  - _文档首行_（仅供参考）: Sanitize a filename by extracting its basename.
  - 分支数 4，函数体节点数 96；raise: ValueError('Filename is empty'), ValueError(f'Filename is unsafe: {filename!r}'), ValueError(f'Filename contains backslash: {filename!r}'), ValueError(f'Filename too long: {len(safe)} chars')；return: safe
  - 调用: ValueError, Path, len, encode

#### `ƒ` `claim_unique_filename(name: str, seen: set[str]) -> str`  L86
  - _文档首行_（仅供参考）: Generate a unique filename by appending ``_N`` suffix on collision.
  - 分支数 2，函数体节点数 112；return: name, candidate
  - 调用: add, Path

#### `ƒ` `is_upload_staging_file(filename: str) -> bool`  L111
  - _文档首行_（仅供参考）: Return whether *filename* is a transient Gateway upload staging file.
  - 分支数 0，函数体节点数 26；return: filename.startswith(UPLOAD_STAGING_PREFIX) and filename.endswith(UPLOAD_STAGING_SUFFIX)
  - 调用: startswith, endswith

#### `ƒ` `validate_path_traversal(path: Path, base: Path) -> None`  L116
  - _文档首行_（仅供参考）: Verify that *path* is inside *base*.
  - 分支数 1，函数体节点数 35；raise: PathTraversalError('Path traversal detected')
  - 调用: relative_to, resolve, PathTraversalError

#### `ƒ` `validate_upload_destination(base_dir: Path, filename: str) -> Path`  L128
  - _文档首行_（仅供参考）: Validate an upload destination without mutating an existing file.
  - 分支数 3，函数体节点数 110；raise: UnsafeUploadPathError(f'Upload destination is not a regular file: {safe_name}'), UnsafeUploadPathError(f'Upload destination has multiple links: {safe_name}')；return: dest
  - 调用: normalize_filename, lstat, S_ISREG, UnsafeUploadPathError, validate_path_traversal

#### `ƒ` `_iter_upload_dirs(base_dir: Path)`  L147
  - 分支数 0，函数体节点数 21；生成器（yield）
  - 文件IO: glob (L148), glob (L149)

#### `ƒ` `cleanup_stale_upload_staging_files(base_dir: Path | str | None) -> int`  L152
  - _文档首行_（仅供参考）: Remove orphaned Gateway upload staging files left by a hard crash.
  - 分支数 7，函数体节点数 153；return: removed
  - 调用: Path, get_paths, _iter_upload_dirs, is_dir, scandir, is_upload_staging_file, is_file, unlink, warning
  - 文件IO: unlink (L165)

#### `ƒ` `open_upload_file_no_symlink(base_dir: Path, filename: str) -> tuple[Path, object]`  L178
  - _文档首行_（仅供参考）: Open an upload destination for safe streaming writes.
  - 分支数 18，函数体节点数 510；raise: UnsafeUploadPathError(f'Unsafe upload destination: {safe_name}'), bare raise, UnsafeUploadPathError(f'Upload destination is not an exclusive regular file: {safe_name}'), UnsafeUploadPathError(f'Upload destination has multiple links: {safe_name}'), UnsafeUploadPathError(f'Upload destination is not a regular file: {safe_name}')；return: (dest, fh)
  - 调用: normalize_filename, validate_upload_destination, lstat, hasattr, open, UnsafeUploadPathError, fstat, S_ISREG, ftruncate, fdopen, close
  - 文件IO: open (L206), open (L247)
  - 反射: hasattr (L197), hasattr (L202), hasattr (L233)

#### `ƒ` `write_upload_file_no_symlink(base_dir: Path, filename: str, data: bytes) -> Path`  L266
  - _文档首行_（仅供参考）: Write upload bytes without following a pre-existing destination symlink.
  - 分支数 1，函数体节点数 44；return: dest
  - 调用: open_upload_file_no_symlink, write
  - 文件IO: write (L270)

#### `ƒ` `list_files_in_dir(directory: Path) -> dict`  L274
  - _文档首行_（仅供参考）: List files (not directories) in *directory*.
  - 分支数 5，函数体节点数 134；return: {'files': [], 'count': 0}, {'files': files, 'count': len(files)}
  - 调用: is_dir, scandir, sorted, is_upload_staging_file, is_file, stat, append, Path, len
  - 文件IO: stat (L295)

#### `ƒ` `delete_file_safe(base_dir: Path, filename: str, *, convertible_extensions: set[str] | None) -> dict`  L308
  - _文档首行_（仅供参考）: Delete a file inside *base_dir* after path-traversal validation.
  - 分支数 2，函数体节点数 104；raise: FileNotFoundError(f'File not found: {filename}')；return: {'success': True, 'message': f'Deleted {filename}'}
  - 调用: resolve, validate_path_traversal, is_file, FileNotFoundError, unlink, lower, with_suffix
  - 文件IO: unlink (L333), unlink (L337)

#### `ƒ` `upload_artifact_url(thread_id: str, filename: str) -> str`  L342
  - _文档首行_（仅供参考）: Build the artifact URL for a file in a thread's uploads directory.
  - 分支数 0，函数体节点数 31；return: f"/api/threads/{thread_id}/artifacts{VIRTUAL_PATH_PREFIX}/uploads/{quote(filename, safe='')}"
  - 调用: quote

#### `ƒ` `upload_virtual_path(filename: str) -> str`  L350
  - _文档首行_（仅供参考）: Build the virtual path for a file in the uploads directory.
  - 分支数 0，函数体节点数 18；return: f'{VIRTUAL_PATH_PREFIX}/uploads/{filename}'

#### `ƒ` `enrich_file_listing(result: dict, thread_id: str) -> dict`  L355
  - _文档首行_（仅供参考）: Add virtual paths and artifact URLs on a listing result.
  - 分支数 1，函数体节点数 55；return: result
  - 调用: upload_virtual_path, upload_artifact_url

## 类
### 类 `PathTraversalError`  L19
- 继承: ValueError
- _文档首行_: Raised when a path escapes its allowed base directory.

### 类 `UnsafeUploadPathError`  L23
- 继承: ValueError
- _文档首行_: Raised when an upload destination is not a safe regular file path.

## 文件内调用关系
- `get_uploads_dir` -> validate_thread_id
- `ensure_uploads_dir` -> get_uploads_dir
- `validate_upload_destination` -> normalize_filename, validate_path_traversal
- `cleanup_stale_upload_staging_files` -> _iter_upload_dirs, is_upload_staging_file
- `open_upload_file_no_symlink` -> normalize_filename, validate_upload_destination
- `write_upload_file_no_symlink` -> open_upload_file_no_symlink
- `list_files_in_dir` -> is_upload_staging_file
- `delete_file_safe` -> validate_path_traversal
- `enrich_file_listing` -> upload_virtual_path, upload_artifact_url

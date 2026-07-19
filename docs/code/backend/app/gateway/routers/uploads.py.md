# `backend/app/gateway/routers/uploads.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/uploads.py`  ·  行数: 472

**模块文档首行**（仅供参考）: Upload router for handling file uploads.

## 模块概览
- 函数 21 个，类 5 个，模块级常量 6 个

## 依赖（import）
- 模块: logging, os, stat, tempfile
- `dataclasses` -> dataclass
- `pathlib` -> Path
- `typing` -> BinaryIO
- `fastapi` -> APIRouter, Depends, File, HTTPException, Request, UploadFile
- `pydantic` -> BaseModel, Field
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_config
- `deerflow.config.app_config` -> AppConfig
- `deerflow.config.paths` -> get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.sandbox.sandbox_provider` -> SandboxProvider, get_sandbox_provider
- `deerflow.uploads.manager` -> UPLOAD_STAGING_PREFIX, UPLOAD_STAGING_SUFFIX, PathTraversalError, UnsafeUploadPathError, claim_unique_filename, delete_file_safe, enrich_file_listing, ensure_uploads_dir, get_uploads_dir, list_files_in_dir, normalize_filename, upload_artifact_url, upload_virtual_path, validate_upload_destination
- `deerflow.utils.file_conversion` -> CONVERTIBLE_EXTENSIONS, convert_file_to_markdown
- `deerflow.utils.file_io` -> run_file_io

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/threads/{thread_id}/uploads', tags...
- `UPLOAD_CHUNK_SIZE` = 8192
- `DEFAULT_MAX_FILES` = 10
- `DEFAULT_MAX_FILE_SIZE` = 50 * 1024 * 1024
- `DEFAULT_MAX_TOTAL_SIZE` = 100 * 1024 * 1024

## 函数
#### `ƒ` `_make_file_sandbox_writable(file_path: os.PathLike[str] | str) -> None`  L97
  - _文档首行_（仅供参考）: Ensure uploaded files remain writable when mounted into non-local sandboxes.
  - 分支数 1，函数体节点数 121；return: None
  - 调用: lstat, S_ISLNK, warning, S_IMODE, chmod
  - 文件IO: chmod (L112)

#### `ƒ` `_make_file_sandbox_readable(file_path: os.PathLike[str] | str) -> None`  L115
  - _文档首行_（仅供参考）: Ensure uploaded files are readable by the sandbox process.
  - 分支数 1，函数体节点数 103；return: None
  - 调用: lstat, S_ISLNK, warning, S_IMODE, chmod
  - 文件IO: chmod (L131)

#### `ƒ` `_uses_thread_data_mounts(sandbox_provider: SandboxProvider) -> bool`  L134
  - 分支数 0，函数体节点数 18；return: bool(getattr(sandbox_provider, 'uses_thread_data_mounts', False))
  - 调用: bool, getattr
  - 反射: getattr (L135)

#### `ƒ` `_get_uploads_config_value(app_config: AppConfig, key: str, default: object) -> object`  L138
  - _文档首行_（仅供参考）: Read a value from the uploads config, supporting dict and attribute access.
  - 分支数 1，函数体节点数 53；return: uploads_cfg.get(key, default), getattr(uploads_cfg, key, default)
  - 调用: getattr, isinstance, get
  - 反射: getattr (L140), getattr (L143)

#### `ƒ` `_get_upload_limit(app_config: AppConfig, key: str, default: int, *, legacy_key: str | None) -> int`  L146
  - 分支数 4，函数体节点数 104；raise: ValueError；return: limit, default
  - 调用: _get_uploads_config_value, int, warning

#### `ƒ` `_get_upload_limits(app_config: AppConfig) -> UploadLimits`  L162
  - 分支数 0，函数体节点数 42；return: UploadLimits(max_files=_get_upload_limit(app_config, 'max_files', DEFAULT_MAX_FILES, legacy_key='max_file_count'), max_file_size=_get_upload_limit(app_config, 'max_file_size', DEFAULT_MAX_FILE_SIZE, legacy_key='max_single_file_size'), max_total_size=_get_upload_limit(app_config, 'max_total_size', DEFAULT_MAX_TOTAL_SIZE))
  - 调用: UploadLimits, _get_upload_limit

#### `ƒ` `_cleanup_uploaded_paths(paths: list[os.PathLike[str] | str]) -> None`  L170
  - 分支数 2，函数体节点数 55
  - 调用: reversed, unlink, warning
  - 文件IO: unlink (L173)

#### `ƒ` `_prepare_upload_destination(uploads_dir: os.PathLike[str] | str, display_filename: str) -> _UploadTempFile`  L180
  - 分支数 3，函数体节点数 122；raise: bare raise；return: _UploadTempFile(file_path=file_path, temp_path=temp_path, handle=handle)
  - 调用: Path, validate_upload_destination, mkstemp, fdopen, close, unlink, _UploadTempFile
  - 文件IO: unlink (L193)

#### `ƒ` `_write_upload_chunk(upload_temp: _UploadTempFile, chunk: bytes) -> None`  L200
  - 分支数 0，函数体节点数 19
  - 调用: write
  - 文件IO: write (L201)

#### `ƒ` `_abort_upload_temp(upload_temp: _UploadTempFile) -> None`  L204
  - 分支数 2，函数体节点数 30
  - 调用: close, unlink
  - 文件IO: unlink (L209)

#### `ƒ` `_commit_upload_temp(upload_temp: _UploadTempFile) -> None`  L214
  - 分支数 2，函数体节点数 48；raise: bare raise
  - 调用: close, replace, unlink
  - 文件IO: replace (L217), unlink (L220)

#### `ƒ` `_make_uploaded_paths_sandbox_readable(paths: list[os.PathLike[str] | str]) -> None`  L226
  - 分支数 1，函数体节点数 31
  - 调用: _make_file_sandbox_readable

#### `ƒ` `_sync_upload_to_sandbox(sandbox, file_path: os.PathLike[str] | str, virtual_path: str) -> None`  L231
  - 分支数 0，函数体节点数 42
  - 调用: _make_file_sandbox_writable, update_file, read_bytes, Path
  - 文件IO: read_bytes (L233)

#### `ƒ` `_list_uploaded_files_for_thread(thread_id: str, user_id: str) -> dict`  L236
  - 分支数 1，函数体节点数 80；return: result
  - 调用: get_uploads_dir, list_files_in_dir, enrich_file_listing, sandbox_uploads_dir, get_paths, str

#### `ƒ` `_delete_uploaded_file_for_thread(thread_id: str, filename: str, user_id: str) -> dict`  L247
  - 分支数 0，函数体节点数 35；return: delete_file_safe(uploads_dir, filename, convertible_extensions=CONVERTIBLE_EXTENSIONS)
  - 调用: get_uploads_dir, delete_file_safe

#### `⏵ƒ` `async _write_upload_file_with_limits(file: UploadFile, *, uploads_dir: os.PathLike[str] | str, display_filename: str, max_single_file_size: int, max_total_size: int, total_size: int) -> tuple[os.PathLike[str] | str, int, int]`  L252
  - 分支数 5，函数体节点数 202；raise: HTTPException(status_code=413, detail=f'File too large: {display_filename}'), HTTPException(status_code=413, detail='Total upload size too large'), bare raise；return: (file_path, file_size, total_size)
  - 调用: run_file_io, read, len, HTTPException
  - 文件IO: read (L265)

#### `ƒ` `_auto_convert_documents_enabled(app_config: AppConfig) -> bool`  L284
  - _文档首行_（仅供参考）: Return whether automatic host-side document conversion is enabled.
  - 分支数 2，函数体节点数 55；return: raw.strip().lower() in {'1', 'true', 'yes', 'on'}, bool(raw), False
  - 调用: _get_uploads_config_value, isinstance, lower, strip, bool

#### `⏵ƒ` `async upload_files(thread_id: str, request: Request, files: list[UploadFile], config: AppConfig) -> UploadResponse`    @router.post(...), require_permission(...)  L301
  - _文档首行_（仅供参考）: Upload multiple files to a thread's uploads directory.
  - 分支数 17，函数体节点数 721；raise: HTTPException(status_code=400, detail='No files provided'), HTTPException(status_code=413, detail=f'Too many files: maximum is {limits.max_files}'), HTTPException(status_code=400, detail=str(e)), HTTPException(status_code=500, detail='Failed to acquire sandbox'), e, HTTPException(status_code=500, detail=f'Failed to upload {file.filename}: {str(e)}')；return: UploadResponse(success=not skipped_files, files=uploaded_files, message=message, skipped_files=skipped_files)
  - 调用: File, Depends, HTTPException, _get_upload_limits, len, get_effective_user_id, run_file_io, str, set, get_sandbox_provider, _uses_thread_data_mounts, acquire_async, get, _auto_convert_documents_enabled, normalize_filename, claim_unique_filename, warning, _write_upload_file_with_limits, append, upload_virtual_path（+8）

#### `⏵ƒ` `async get_upload_limits(thread_id: str, request: Request, config: AppConfig) -> UploadLimits`    @router.get(...), require_permission(...)  L436
  - _文档首行_（仅供参考）: Return upload limits used by the gateway for this thread.
  - 分支数 0，函数体节点数 42；return: _get_upload_limits(config)
  - 调用: Depends, _get_upload_limits, get, require_permission

#### `⏵ƒ` `async list_uploaded_files(thread_id: str, request: Request) -> UploadListResponse`    @router.get(...), require_permission(...)  L447
  - _文档首行_（仅供参考）: List all files in a thread's uploads directory.
  - 分支数 1，函数体节点数 65；raise: HTTPException(status_code=400, detail=str(e))；return: UploadListResponse(**result)
  - 调用: run_file_io, get_effective_user_id, HTTPException, str, UploadListResponse, get, require_permission

#### `⏵ƒ` `async delete_uploaded_file(thread_id: str, filename: str, request: Request) -> dict`    @router.delete(...), require_permission(...)  L459
  - _文档首行_（仅供参考）: Delete a file from a thread's uploads directory.
  - 分支数 1，函数体节点数 123；raise: HTTPException(status_code=404, detail=f'File not found: {filename}'), HTTPException(status_code=400, detail='Invalid path'), HTTPException(status_code=400, detail=str(e)), HTTPException(status_code=500, detail=f'Failed to delete {filename}: {str(e)}')；return: await run_file_io(_delete_uploaded_file_for_thread, thread_id, filename, get_effective_user_id())
  - 调用: run_file_io, get_effective_user_id, HTTPException, str, error, delete, require_permission

## 类
### 类 `_UploadTempFile`  L50  @dataclass(...)
- 类/实例变量:
  - `file_path` = <annotated>
  - `temp_path` = <annotated>
  - `handle` = <annotated>

### 类 `UploadedFileInfo`  L56
- 继承: BaseModel
- _文档首行_: Uploaded file metadata exposed by upload and list APIs.
- 类/实例变量:
  - `filename` = <annotated>
  - `size` = <annotated>
  - `path` = <annotated>
  - `virtual_path` = <annotated>
  - `artifact_url` = <annotated>
  - `extension` = None
  - `modified` = None
  - `original_filename` = None
  - `markdown_file` = None
  - `markdown_path` = None
  - `markdown_virtual_path` = None
  - `markdown_artifact_url` = None

### 类 `UploadResponse`  L73
- 继承: BaseModel
- _文档首行_: Response model for file upload.
- 类/实例变量:
  - `success` = <annotated>
  - `files` = <annotated>
  - `message` = <annotated>
  - `skipped_files` = Field(default_factory=list)

### 类 `UploadListResponse`  L82
- 继承: BaseModel
- _文档首行_: Response model for uploaded file listing.
- 类/实例变量:
  - `files` = <annotated>
  - `count` = <annotated>

### 类 `UploadLimits`  L89
- 继承: BaseModel
- _文档首行_: Application-level upload limits exposed to clients.
- 类/实例变量:
  - `max_files` = <annotated>
  - `max_file_size` = <annotated>
  - `max_total_size` = <annotated>

## 文件内调用关系
- `_get_upload_limit` -> _get_uploads_config_value
- `_get_upload_limits` -> _get_upload_limit
- `_make_uploaded_paths_sandbox_readable` -> _make_file_sandbox_readable
- `_sync_upload_to_sandbox` -> _make_file_sandbox_writable
- `_auto_convert_documents_enabled` -> _get_uploads_config_value
- `upload_files` -> _get_upload_limits, _uses_thread_data_mounts, _auto_convert_documents_enabled, _write_upload_file_with_limits
- `get_upload_limits` -> _get_upload_limits

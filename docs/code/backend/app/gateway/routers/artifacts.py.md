# `backend/app/gateway/routers/artifacts.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/artifacts.py`  ·  行数: 261

## 模块概览
- 函数 8 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: asyncio, logging, mimetypes, zipfile
- `pathlib` -> Path
- `urllib.parse` -> quote
- `fastapi` -> APIRouter, HTTPException, Request
- `fastapi.responses` -> FileResponse, PlainTextResponse, Response
- `app.gateway.authz` -> require_permission
- `app.gateway.internal_auth` -> get_trusted_internal_owner_user_id
- `app.gateway.path_utils` -> resolve_thread_virtual_path
- `deerflow.config.paths` -> make_safe_user_id

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api', tags=['artifacts'])
- `ACTIVE_CONTENT_MIME_TYPES` = {'text/html', 'application/xhtml+xml', 'image/svg+xml'}
- `MAX_SKILL_ARCHIVE_MEMBER_BYTES` = 16 * 1024 * 1024
- `_SKILL_ARCHIVE_READ_CHUNK_SIZE` = 64 * 1024

## 函数
#### `ƒ` `_build_content_disposition(disposition_type: str, filename: str) -> str`  L30
  - _文档首行_（仅供参考）: Build an RFC 5987 encoded Content-Disposition header value.
  - 分支数 0，函数体节点数 24；return: f"{disposition_type}; filename*=UTF-8''{quote(filename)}"
  - 调用: quote

#### `ƒ` `_build_attachment_headers(filename: str, extra_headers: dict[str, str] | None) -> dict[str, str]`  L35
  - 分支数 1，函数体节点数 55；return: headers
  - 调用: _build_content_disposition, update

#### `ƒ` `is_text_file_by_content(path: Path, sample_size: int) -> bool`  L42
  - _文档首行_（仅供参考）: Check if file is text by examining content for null bytes.
  - 分支数 2，函数体节点数 45；return: b'\x00' not in chunk, False
  - 调用: open, read
  - 文件IO: open (L45), read (L46)

#### `ƒ` `_read_skill_archive_member(zip_ref: zipfile.ZipFile, info: zipfile.ZipInfo) -> bytes`  L53
  - _文档首行_（仅供参考）: Read a .skill archive member while enforcing an uncompressed size cap.
  - 分支数 4，函数体节点数 110；raise: HTTPException(status_code=413, detail='Skill archive member is too large to preview')；return: b''.join(chunks)
  - 调用: HTTPException, open, read, len, append, join
  - 文件IO: open (L60), read (L61)

#### `ƒ` `_extract_file_from_skill_archive(zip_path: Path, internal_path: str) -> bytes | None`  L69
  - _文档首行_（仅供参考）: Extract a file from a .skill ZIP archive.
  - 分支数 6，函数体节点数 129；return: None, _read_skill_archive_member(zip_ref, infos_by_name[internal_path]), _read_skill_archive_member(zip_ref, info)
  - 调用: is_zipfile, ZipFile, infolist, _read_skill_archive_member, items, endswith

#### `ƒ` `_load_skill_archive_member(actual_skill_path: Path, skill_file_path: str, internal_path: str) -> tuple[bytes, str | None]`  L102
  - _文档首行_（仅供参考）: Worker-thread body for the ``.skill`` branch of ``get_artifact``.
  - 分支数 3，函数体节点数 116；raise: HTTPException(status_code=404, detail=f'Skill file not found: {skill_file_path}'), HTTPException(status_code=400, detail=f'Path is not a file: {skill_file_path}'), HTTPException(status_code=404, detail=f"File '{internal_path}' not found in skill archive")；return: (content, mime_type)
  - 调用: exists, HTTPException, is_file, _extract_file_from_skill_archive, guess_type
  - 文件IO: exists (L111)

#### `ƒ` `_read_artifact_payload(actual_path: Path, path: str, download: bool) -> tuple[str, str | None, bytes | str | None]`  L122
  - _文档首行_（仅供参考）: Worker-thread body for the regular branch of ``get_artifact``.
  - 分支数 5，函数体节点数 157；raise: HTTPException(status_code=404, detail=f'Artifact not found: {path}'), HTTPException(status_code=400, detail=f'Path is not a file: {path}')；return: ('file', mime_type, None), ('text', mime_type, actual_path.read_text(encoding='utf-8')), ('inline_file', mime_type, None)
  - 调用: exists, HTTPException, is_file, guess_type, startswith, read_text, is_text_file_by_content
  - 文件IO: exists (L135), read_text (L144), read_text (L146)

#### `⏵ƒ` `async get_artifact(thread_id: str, path: str, request: Request, download: bool) -> Response`    @router.get(...), require_permission(...)  L159
  - _文档首行_（仅供参考）: Get an artifact file by its path.
  - 分支数 7，函数体节点数 407；raise: AssertionError(f'Unhandled artifact response kind: {kind!r}')；return: Response(content=content, media_type=mime_type or 'application/octet-stream', headers=_build_attachment_headers(download_name, cache_headers)), PlainTextResponse(content=content.decode('utf-8'), media_type=mime_type, headers=cache_headers), PlainTextResponse(content=content.decode('utf-8'), media_type='text/plain', headers=cache_headers), Response(content=content, media_type=mime_type or 'application/octet-stream', headers=cache_headers), FileResponse(path=actual_path, filename=actual_path.name, media_type=mime_type, headers=_build_attachment_headers(actual_path.name)), FileResponse(path=actual_path, media_type=mime_type, headers={'Content-Disposition': _build_content_disposition('inline', actual_path.name)}), PlainTextResponse(content=payload, media_type=mime_type)
  - 调用: get_trusted_internal_owner_user_id, make_safe_user_id, find, len, to_thread, Path, Response, _build_attachment_headers, startswith, PlainTextResponse, decode, info, FileResponse, _build_content_disposition, AssertionError, get, require_permission

## 文件内调用关系
- `_build_attachment_headers` -> _build_content_disposition
- `_extract_file_from_skill_archive` -> _read_skill_archive_member
- `_load_skill_archive_member` -> _extract_file_from_skill_archive
- `_read_artifact_payload` -> is_text_file_by_content
- `get_artifact` -> _build_attachment_headers, _build_content_disposition

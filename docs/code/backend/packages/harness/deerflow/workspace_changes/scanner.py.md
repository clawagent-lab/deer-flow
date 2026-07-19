# `backend/packages/harness/deerflow/workspace_changes/scanner.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/workspace_changes/scanner.py`  ·  行数: 278

## 模块概览
- 函数 9 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: fnmatch, hashlib, os
- `__future__` -> annotations
- `codecs` -> BOM_UTF16_BE, BOM_UTF16_LE, getincrementaldecoder
- `pathlib` -> Path
- `.types` -> DiffUnavailableReason, FileSnapshot, WorkspaceChangeLimits, WorkspaceRoot, WorkspaceSnapshot

## 模块级常量
- `EXCLUDED_DIR_NAMES` = {'.git', '.hg', '.svn', '.cache', '.next', '.venv', '__py...
- `BINARY_EXTENSIONS` = {'.7z', '.avif', '.bmp', '.class', '.db', '.dll', '.dmg',...
- `SENSITIVE_PATH_PATTERNS` = ('.env', '.env.*', '*api_key*', '*apikey*', '*.key', '*.p...
- `SAMPLE_BYTES` = 4096
- `_UTF16_BOMS` = (BOM_UTF16_LE, BOM_UTF16_BE)

## 函数
#### `ƒ` `is_sensitive_workspace_path(path: str) -> bool`  L80
  - 分支数 3，函数体节点数 100；return: True, False
  - 调用: lower, Path, fnmatch, any

#### `ƒ` `scan_workspace_roots(roots: list[WorkspaceRoot], *, limits: WorkspaceChangeLimits | None, include_text: bool, text_paths: set[str] | None, text_cache_dir: Path | None) -> WorkspaceSnapshot`  L92
  - 分支数 8，函数体节点数 314；return: WorkspaceSnapshot(files=files, truncated=truncated, text_cache_dir=str(cache_dir) if cache_dir is not None else None)
  - 调用: WorkspaceChangeLimits, Path, mkdir, exists, walk, is_symlink, sorted, WorkspaceSnapshot, str, is_file, _snapshot_file
  - 文件IO: mkdir (L103), exists (L109)

#### `ƒ` `_snapshot_file(root: WorkspaceRoot, host_file: Path, *, limits: WorkspaceChangeLimits, include_text: bool, text_paths: set[str] | None, text_cache_dir: Path | None) -> FileSnapshot | None`  L146
  - 分支数 9，函数体节点数 374；return: None, FileSnapshot(path=virtual_path, root=root.name, size=size, mtime_ns=mtime_ns, sha256=None, binary=False, sensitive=True, text=None, content_unavailable_reason='sensitive'), FileSnapshot(path=virtual_path, root=root.name, size=size, mtime_ns=mtime_ns, sha256=sha256, binary=binary, sensitive=sensitive, text=text, text_path=text_path, content_unavailable_reason=reason)
  - 调用: stat, as_posix, relative_to, is_sensitive_workspace_path, FileSnapshot, read_bytes, _read_sample, lower, _looks_binary, _sha256_file, _decode_text_bytes, str, _cache_text_file
  - 文件IO: stat (L156), read_bytes (L179), read_bytes (L199)

#### `ƒ` `_cache_text_file(text: str, virtual_path: str, cache_dir: Path) -> Path`  L225
  - 分支数 0，函数体节点数 52；return: target
  - 调用: hexdigest, sha256, encode, write_text
  - 文件IO: write_text (L228)

#### `ƒ` `_read_sample(path: Path) -> bytes`  L232
  - 分支数 1，函数体节点数 25；return: file.read(SAMPLE_BYTES)
  - 调用: open, read
  - 文件IO: open (L233), read (L234)

#### `ƒ` `_sha256_file(path: Path) -> str`  L237
  - 分支数 2，函数体节点数 57；return: digest.hexdigest()
  - 调用: sha256, open, iter, read, update, hexdigest
  - 文件IO: open (L239), read (L240)

#### `ƒ` `_decode_text_bytes(data: bytes) -> str | None`  L245
  - 分支数 4，函数体节点数 53；return: data.decode(encoding), data.decode('utf-16'), None
  - 调用: decode, startswith

#### `ƒ` `_sample_decodes_as_text(sample: bytes, encoding: str) -> bool`  L261
  - 分支数 1，函数体节点数 37；return: False, True
  - 调用: getincrementaldecoder(encoding), getincrementaldecoder, decode

#### `ƒ` `_looks_binary(sample: bytes) -> bool`  L270
  - 分支数 3，函数体节点数 44；return: False, True
  - 调用: startswith, _sample_decodes_as_text

## 文件内调用关系
- `scan_workspace_roots` -> _snapshot_file
- `_snapshot_file` -> is_sensitive_workspace_path, _read_sample, _looks_binary, _sha256_file, _decode_text_bytes, _cache_text_file
- `_looks_binary` -> _sample_decodes_as_text

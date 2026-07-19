# `backend/packages/harness/deerflow/skills/review/readers.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/review/readers.py`  ·  行数: 411

**模块文档首行**（仅供参考）: Read-only package readers for skill review snapshots.

## 模块概览
- 函数 10 个，类 3 个，模块级常量 2 个

## 依赖（import）
- 模块: hashlib, os, stat, zipfile
- `__future__` -> annotations
- `pathlib` -> Path, PurePosixPath
- `typing` -> Any
- `deerflow.skills.review.models` -> DEFAULT_PACKAGE_LIMITS, PACKAGE_SNAPSHOT_SCHEMA_VERSION, PackageLimits, normalize_relative_path

## 模块级常量
- `_TEXT_EXTENSIONS` = {'.css', '.csv', '.html', '.js', '.json', '.md', '.py', '...
- `_ZIP_READ_CHUNK_BYTES` = 1024 * 1024

## 函数
#### `ƒ` `_sha256(data: bytes) -> str`  L38
  - 分支数 0，函数体节点数 18；return: hashlib.sha256(data).hexdigest()
  - 调用: hexdigest, sha256

#### `ƒ` `_decode_text(data: bytes, path: str) -> str | None`  L42
  - 分支数 2，函数体节点数 55；return: None, data.decode('utf-8')
  - 调用: lower, PurePosixPath, decode

#### `ƒ` `_truncate_utf8_bytes(content: str, max_bytes: int) -> tuple[str, bytes]`  L52
  - 分支数 0，函数体节点数 59；return: (text, text.encode('utf-8'))
  - 调用: encode, decode

#### `ƒ` `_subject(*, source: str, display_ref: str, name_hint: str | None, category: str | None) -> dict[str, Any]`  L59
  - 分支数 0，函数体节点数 46；return: {'source': source, 'category': category, 'name_hint': name_hint, 'display_ref': display_ref}

#### `ƒ` `_empty_snapshot(subject: dict[str, Any], limits: PackageLimits) -> dict[str, Any]`  L74
  - 分支数 0，函数体节点数 48；return: {'schema_version': PACKAGE_SNAPSHOT_SCHEMA_VERSION, 'subject': subject, 'limits': limits.to_dict(), 'files': [], 'truncated': False, 'reader_errors': []}
  - 调用: to_dict

#### `ƒ` `build_inline_snapshot(content: str, *, name_hint: str | None, limits: PackageLimits) -> dict[str, Any]`  L85
  - 分支数 1，函数体节点数 141；return: snapshot
  - 调用: encode, _empty_snapshot, _subject, len, append, _truncate_utf8_bytes, _sha256

#### `ƒ` `_zip_member_is_symlink(info: zipfile.ZipInfo) -> bool`  L347
  - 分支数 0，函数体节点数 27；return: stat.S_ISLNK(mode)
  - 调用: S_ISLNK

#### `ƒ` `_read_zip_member_bounded(zf: zipfile.ZipFile, info: zipfile.ZipInfo, *, max_bytes: int) -> tuple[bytes, int, bool]`  L352
  - 分支数 5，函数体节点数 153；return: (b''.join(chunks), actual_size, True), (b''.join(chunks), actual_size, False)
  - 调用: open, min, join, read, len, append
  - 文件IO: open (L355), read (L360)

#### `ƒ` `parse_skill_uri(target: str) -> tuple[str, str]`  L394
  - 分支数 2，函数体节点数 91；raise: ValueError('Installed skill targets must use skill://<category>/<relative-path>'), ValueError('Skill target must include category: public, custom, or legacy')；return: (category, rel_path)
  - 调用: startswith, ValueError, len, partition, normalize_relative_path

#### `ƒ` `_installed_skill_root(storage: Any, category: str, rel_path: str) -> Path`  L405
  - 分支数 2，函数体节点数 79；return: Path(storage.get_user_custom_root()) / rel_path, Path(storage.get_skills_root_path()) / 'custom' / rel_path, Path(storage.get_skills_root_path()) / category / rel_path
  - 调用: hasattr, Path, get_user_custom_root, get_skills_root_path
  - 反射: hasattr (L406)

## 类
### 类 `LocalDirectoryReader`  L119
- _文档首行_: Read a local skill directory without following symlink escapes.
- 方法:
  #### `st` `_relative(path: Path, root: Path, snapshot: dict[str, Any]) -> str | None`    @staticmethod  L240
    - 分支数 1，函数体节点数 67；return: normalize_relative_path(rel), None
    - 调用: as_posix, relative_to, normalize_relative_path, append
  #### `st` `_sort_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]`    @staticmethod  L249
    - 分支数 0，函数体节点数 95；return: snapshot
    - 调用: sorted, str, get
  #### `m` `__init__(self, root: str | Path, *, subject: dict[str, Any] | None, limits: PackageLimits) -> None`  L122
    - 分支数 0，函数体节点数 88
    - 调用: Path, _subject, str
  #### `m` `read(self) -> dict[str, Any]`  L137
    - 分支数 14，函数体节点数 566；return: snapshot, self._sort_snapshot(snapshot)
    - 调用: _empty_snapshot, exists, append, is_dir, resolve, walk, Path, sorted, list, is_symlink, remove, _append_symlink, _relative, _sort_snapshot, stat, str, max, read_bytes, _decode_text, len（+1）
  - 文件IO: exists (L140), stat (L179), read_bytes (L197)
  #### `m` `_append_symlink(self, snapshot: dict[str, Any], path: Path, root: Path, file_count: int) -> int`  L215
    - 分支数 3，函数体节点数 141；return: file_count
    - 调用: _relative, append, readlink, _sha256, encode

### 类 `ArchivePackageReader`  L255
- _文档首行_: Inspect a .skill ZIP archive without installing it.
- 方法:
  #### `st` `_normalize_archive_name(filename: str, snapshot: dict[str, Any]) -> str | None`    @staticmethod  L339
    - 分支数 1，函数体节点数 56；return: normalize_relative_path(filename), None
    - 调用: normalize_relative_path, append, str
  #### `m` `__init__(self, archive_path: str | Path, *, limits: PackageLimits) -> None`  L258
    - 分支数 0，函数体节点数 33
    - 调用: Path
  #### `m` `read(self) -> dict[str, Any]`  L267
    - 分支数 13，函数体节点数 645；return: snapshot
    - 调用: _empty_snapshot, _subject, str, ZipFile, sorted, infolist, len, append, is_dir, _normalize_archive_name, max, min, _read_zip_member_bounded, _zip_member_is_symlink, decode, _sha256, _decode_text, get

### 类 `InstalledSkillReader`  L369
- 继承: LocalDirectoryReader
- _文档首行_: Resolve and read an installed skill by canonical skill:// identity.
- 方法:
  #### `cls` `from_target(cls, target: str, *, storage: Any, limits: PackageLimits) -> InstalledSkillReader`    @classmethod  L373
    - 分支数 0，函数体节点数 78；return: cls(root, subject=_subject(source='installed', category=category, name_hint=PurePosixPath(rel_path).name, display_ref=f'skill://{category}/{rel_path}'), limits=limits)
    - 调用: parse_skill_uri, _installed_skill_root, cls, _subject, PurePosixPath

## 文件内调用关系
- `build_inline_snapshot` -> _empty_snapshot, _subject, _truncate_utf8_bytes, _sha256
- `_read_zip_member_bounded` -> read
- `LocalDirectoryReader.__init__` -> _subject
- `LocalDirectoryReader.read` -> _empty_snapshot, _append_symlink, _relative, _sort_snapshot, _decode_text, _sha256
- `LocalDirectoryReader._append_symlink` -> _relative, _sha256
- `ArchivePackageReader.read` -> _empty_snapshot, _subject, _normalize_archive_name, _read_zip_member_bounded, _zip_member_is_symlink, _sha256, _decode_text
- `InstalledSkillReader.from_target` -> parse_skill_uri, _installed_skill_root, _subject

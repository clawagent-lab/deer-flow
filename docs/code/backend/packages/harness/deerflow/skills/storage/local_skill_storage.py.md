# `backend/packages/harness/deerflow/skills/storage/local_skill_storage.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/storage/local_skill_storage.py`  ·  行数: 248

**模块文档首行**（仅供参考）: Local-filesystem implementation of ``SkillStorage``.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, errno, json, logging, os, shutil, tempfile
- `__future__` -> annotations
- `collections.abc` -> Iterable
- `datetime` -> UTC, datetime
- `pathlib` -> Path
- `deerflow.config.runtime_paths` -> resolve_path
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.skills.permissions` -> make_skill_written_path_sandbox_readable
- `deerflow.skills.storage.skill_storage` -> SKILL_MD_FILE, SkillStorage
- `deerflow.skills.types` -> SkillCategory

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_INSTALL_TMP_CLEANUP_TIMEOUT_SECONDS` = 5.0

## 类
### 类 `LocalSkillStorage`  L29
- 继承: SkillStorage
- _文档首行_: Skill storage backed by the local filesystem.
- 方法:
  #### `st` `_cleanup_install_tmp(tmp: str) -> None`    @staticmethod  L146
    - _文档首行_（仅供参考）: Best-effort removal that never masks the install outcome, but leaves a trace.
    - 分支数 1，函数体节点数 33
    - 调用: rmtree, warning
  #### `m` `__init__(self, host_path: str | None, container_path: str, app_config) -> None`  L39
    - 分支数 1，函数体节点数 84
    - 调用: __init__, super, get_app_config, get_skills_path, resolve_path
  #### `m` `get_skills_root_path(self) -> Path`  L65
    - 分支数 0，函数体节点数 10；return: self._host_root
  #### `m` `custom_skill_exists(self, name: str) -> bool`  L68
    - 分支数 0，函数体节点数 19；return: self.get_custom_skill_file(name).exists()
    - 调用: exists, get_custom_skill_file
  - 文件IO: exists (L69)
  #### `m` `public_skill_exists(self, name: str) -> bool`  L71
    - 分支数 0，函数体节点数 42；return: (self._host_root / SkillCategory.PUBLIC.value / normalized_name / SKILL_MD_FILE).exists()
    - 调用: validate_skill_name, exists
  - 文件IO: exists (L73)
  #### `m` `_iter_skill_files(self) -> Iterable[tuple[SkillCategory, Path, Path]]`  L75
    - 分支数 5，函数体节点数 140；生成器（yield）；return: None
    - 调用: exists, is_dir, walk, sorted, startswith, clear
  - 文件IO: exists (L76), exists (L80)
  #### `m` `read_custom_skill(self, name: str) -> str`  L94
    - 分支数 1，函数体节点数 45；raise: FileNotFoundError(f"Custom skill '{name}' not found.")；return: (self.get_custom_skill_dir(name) / SKILL_MD_FILE).read_text(encoding='utf-8')
    - 调用: custom_skill_exists, FileNotFoundError, read_text, get_custom_skill_dir
  - 文件IO: read_text (L97)
  #### `m` `write_custom_skill(self, name: str, relative_path: str, content: str) -> None`  L99
    - 分支数 1，函数体节点数 103
    - 调用: validate_relative_path, get_custom_skill_dir, mkdir, NamedTemporaryFile, str, write, Path, replace, make_skill_written_path_sandbox_readable
  - 文件IO: mkdir (L101), write (L108), replace (L110)
  #### `m` `_prepare_skill_archive(self, path: Path, tmp_path: Path, custom_dir: Path, archive_path: str | Path) -> tuple[Path, str, Path]`  L153
    - _文档首行_（仅供参考）: Extract and validate the archive (blocking; runs off the event loop).
    - 分支数 8，函数体节点数 263；raise: FileNotFoundError(f'Skill file not found: {archive_path}'), ValueError(f'Path is not a file: {archive_path}'), ValueError('File must have .skill extension'), ValueError('File is not a valid ZIP archive'), ValueError(f'Invalid skill: {message}'), ValueError(f'Invalid skill name: {skill_name}'), SkillAlreadyExistsError(f"Skill '{skill_name}' already exists")；return: (skill_dir, skill_name, target)
    - 调用: is_file, exists, FileNotFoundError, ValueError, mkdir, ZipFile, scan_archive_preflight_or_raise, safe_extract_skill_archive, resolve_skill_dir_from_archive, _validate_skill_frontmatter, SkillAlreadyExistsError
  - 文件IO: exists (L166), mkdir (L172), exists (L194)
  #### `m` `_commit_skill_install(self, skill_dir: Path, skill_name: str, custom_dir: Path, target: Path) -> None`  L199
    - _文档首行_（仅供参考）: Stage and move the validated skill into place (blocking; runs off the event loop).
    - 分支数 1，函数体节点数 77
    - 调用: TemporaryDirectory, Path, copytree, _move_staged_skill_into_reserved_target, make_skill_written_path_sandbox_readable
  #### `m` `delete_custom_skill(self, name: str, *, history_meta: dict | None) -> None`  L209
    - 分支数 4，函数体节点数 131；raise: bare raise
    - 调用: validate_skill_name, ensure_custom_skill_is_editable, get_custom_skill_dir, read_custom_skill, append_history, isinstance, warning, exists, rmtree
  - 文件IO: exists (L225)
  #### `m` `append_history(self, name: str, record: dict) -> None`  L228
    - 分支数 1，函数体节点数 91
    - 调用: validate_skill_name, isoformat, now, get_skill_history_file, mkdir, open, write, dumps
  - 文件IO: mkdir (L232), open (L233), write (L234), write (L235)
  #### `m` `read_history(self, name: str) -> list[dict]`  L237
    - 分支数 3，函数体节点数 90；return: [], records
    - 调用: validate_skill_name, get_skill_history_file, exists, splitlines, read_text, strip, append, loads
  - 文件IO: exists (L240), read_text (L243)
  #### `⏵m` `async ainstall_skill_from_archive(self, archive_path: str | Path) -> dict`  L113
    - 分支数 2，函数体节点数 177；return: {'success': True, 'skill_name': skill_name, 'message': f"Skill '{skill_name}' installed successfully"}
    - 调用: info, Path, to_thread, _scan_skill_archive_contents_or_raise, wait_for, warning

## 文件内调用关系
- `LocalSkillStorage.__init__` -> __init__
- `LocalSkillStorage.read_custom_skill` -> custom_skill_exists
- `LocalSkillStorage.delete_custom_skill` -> read_custom_skill, append_history

# `backend/packages/harness/deerflow/skills/storage/user_scoped_skill_storage.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/storage/user_scoped_skill_storage.py`  ·  行数: 392

**模块文档首行**（仅供参考）: User-scoped SkillStorage that isolates custom skills per user.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: asyncio, dataclasses, json, logging, os, tempfile
- `__future__` -> annotations
- `collections.abc` -> Iterable
- `pathlib` -> Path
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.skills.permissions` -> make_skill_written_path_sandbox_readable
- `deerflow.skills.storage.local_skill_storage` -> LocalSkillStorage
- `deerflow.skills.storage.skill_storage` -> SKILL_MD_FILE
- `deerflow.skills.types` -> SkillCategory

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `UserScopedSkillStorage`  L49
- 继承: LocalSkillStorage
- _文档首行_: Skill storage with per-user isolation for custom skills.
- 方法:
  #### `prop` `user_id(self) -> str`    @property  L365
    - _文档首行_（仅供参考）: The user ID this storage is scoped to.
    - 分支数 0，函数体节点数 14；return: self._user_id
  #### `m` `__init__(self, user_id: str, host_path: str | None, container_path: str, app_config) -> None`  L71
    - 分支数 0，函数体节点数 121
    - 调用: __init__, super, _validate_user_id, get_paths, user_custom_skills_dir, user_skills_dir
  #### `m` `_read_skill_states(self) -> dict[str, dict[str, bool]]`  L93
    - _文档首行_（仅供参考）: Read per-user skill enabled states from ``_skill_states.json``.
    - 分支数 4，函数体节点数 92；return: {}, data
    - 调用: exists, open, load, isinstance, warning
  - 文件IO: exists (L100), open (L103)
  #### `m` `_write_skill_states(self, states: dict[str, dict[str, bool]]) -> None`  L111
    - _文档首行_（仅供参考）: Persist per-user skill enabled states to ``_skill_states.json``.
    - 分支数 3，函数体节点数 123；raise: bare raise
    - 调用: mkdir, mkstemp, str, Path, fdopen, dump, replace, unlink
  - 文件IO: mkdir (L122), replace (L132), unlink (L136)
  #### `m` `get_skill_enabled_state(self, skill_name: str) -> bool`  L141
    - _文档首行_（仅供参考）: Return the enabled state for a custom/legacy skill.
    - 分支数 1，函数体节点数 44；return: True, entry.get('enabled', True)
    - 调用: _read_skill_states, get
  #### `m` `set_skill_enabled_state(self, skill_name: str, enabled: bool) -> None`  L152
    - _文档首行_（仅供参考）: Set the enabled state for a custom/legacy skill and persist.
    - 分支数 0，函数体节点数 39
    - 调用: _read_skill_states, _write_skill_states
  #### `m` `get_custom_skill_dir(self, name: str) -> Path`  L162
    - _文档首行_（仅供参考）: Per-user custom skill directory: ``<user_custom_root>/<name>/``.
    - 分支数 0，函数体节点数 29；return: self._user_custom_root / normalized_name
    - 调用: validate_skill_name
  #### `m` `get_custom_skill_file(self, name: str) -> Path`  L167
    - _文档首行_（仅供参考）: Per-user custom SKILL.md path.
    - 分支数 0，函数体节点数 22；return: self.get_custom_skill_dir(name) / SKILL_MD_FILE
    - 调用: get_custom_skill_dir
  #### `m` `get_skill_history_file(self, name: str) -> Path`  L171
    - _文档首行_（仅供参考）: Per-user custom skill history: ``<user_custom_root>/.history/<name>.jsonl``.
    - 分支数 0，函数体节点数 35；return: self._user_custom_root / '.history' / f'{normalized_name}.jsonl'
    - 调用: validate_skill_name
  #### `m` `load_skills(self, *, enabled_only: bool) -> list`  L180
    - _文档首行_（仅供参考）: Discover all skills and merge enabled state per isolation scope.
    - 分支数 1，函数体节点数 155；return: skills
    - 调用: load_skills, super, get_extensions_config, is_dataclass, isinstance, hasattr, replace, get_skill_enabled_state, is_skill_enabled
  - 文件IO: replace (L210)
  - 反射: hasattr (L211), hasattr (L210)
  #### `m` `public_skill_exists(self, name: str) -> bool`  L225
    - _文档首行_（仅供参考）: Check if a skill exists as public **or** as a global-custom fallback.
    - 分支数 2，函数体节点数 66；return: True, False
    - 调用: validate_skill_name, exists
  - 文件IO: exists (L236), exists (L239)
  #### `m` `ensure_custom_skill_is_editable(self, name: str) -> None`  L243
    - _文档首行_（仅供参考）: Override to handle global-custom fallback skills gracefully.
    - 分支数 3，函数体节点数 108；raise: ValueError(f"'{name}' is a built-in skill. Use the skill_manage tool to create your own version — it will shadow the built-in one."), ValueError(f"'{name}' is a legacy shared skill (not editable). To customise it, create your own version with the same name — it will shadow the shared one."), FileNotFoundError(f"Custom skill '{name}' not found.")；return: None
    - 调用: custom_skill_exists, validate_skill_name, exists, ValueError, FileNotFoundError
  - 文件IO: exists (L255), exists (L256)
  #### `m` `_iter_skill_files(self) -> Iterable[tuple[SkillCategory, Path, Path]]`  L263
    - 分支数 10，函数体节点数 342；生成器（yield）
    - 调用: exists, is_dir, walk, sorted, startswith, clear
  - 文件IO: exists (L266), exists (L277), exists (L293)
  #### `m` `write_custom_skill(self, name: str, relative_path: str, content: str) -> None`  L344
    - 分支数 1，函数体节点数 115
    - 调用: mkdir, validate_relative_path, get_custom_skill_dir, NamedTemporaryFile, str, write, Path, replace, make_skill_written_path_sandbox_readable
  - 文件IO: mkdir (L346), mkdir (L348), write (L355), replace (L357)
  #### `m` `get_user_custom_root(self) -> Path`  L369
    - _文档首行_（仅供参考）: Host path to this user's custom skills root directory.
    - 分支数 0，函数体节点数 12；return: self._user_custom_root
  #### `m` `validate_skill_file_path(self, skill_file: Path) -> Path`  L377
    - _文档首行_（仅供参考）: Accept files under *either* the global root or the per-user custom root.
    - 分支数 2，函数体节点数 81；raise: ValueError(f'Resolved skill file {resolved_file} must stay within either the global skills root ({self._host_root.resolve()}) or the per-user custom root ({self._user_custom_root.resolve()}).')；return: resolved_file
    - 调用: resolve, relative_to, ValueError
  #### `⏵m` `async ainstall_skill_from_archive(self, archive_path: str | Path) -> dict`  L305
    - 分支数 2，函数体节点数 192；return: {'success': True, 'skill_name': skill_name, 'message': f"Skill '{skill_name}' installed successfully for user '{self._user_id}'"}
    - 调用: info, Path, mkdir, to_thread, _scan_skill_archive_contents_or_raise, wait_for, warning
  - 文件IO: mkdir (L313)

## 文件内调用关系
- `UserScopedSkillStorage.__init__` -> __init__
- `UserScopedSkillStorage.get_skill_enabled_state` -> _read_skill_states
- `UserScopedSkillStorage.set_skill_enabled_state` -> _read_skill_states, _write_skill_states
- `UserScopedSkillStorage.get_custom_skill_file` -> get_custom_skill_dir
- `UserScopedSkillStorage.load_skills` -> load_skills, get_skill_enabled_state
- `UserScopedSkillStorage.write_custom_skill` -> get_custom_skill_dir

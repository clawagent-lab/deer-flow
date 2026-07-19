# `backend/packages/harness/deerflow/skills/storage/skill_storage.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/storage/skill_storage.py`  ·  行数: 293

**模块文档首行**（仅供参考）: Abstract SkillStorage base class with template-method flows.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: dataclasses, logging, re
- `__future__` -> annotations
- `abc` -> ABC, abstractmethod
- `collections.abc` -> Iterable
- `pathlib` -> Path
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.skills.types` -> SKILL_MD_FILE, Skill, SkillCategory

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SKILL_NAME_PATTERN` = re.compile('^[a-z0-9]+(?:-[a-z0-9]+)*$')

## 类
### 类 `SkillStorage`  L20
- 继承: ABC
- 含 abstractmethod（抽象基类）
- _文档首行_: Abstract base for skill storage backends.
- 方法:
  #### `st` `validate_skill_name(name: str) -> str`    @staticmethod  L37
    - _文档首行_（仅供参考）: Validate and normalise a skill name; return the normalised form.
    - 分支数 2，函数体节点数 51；raise: ValueError('Skill name must be hyphen-case using lowercase letters, digits, and hyphens only.'), ValueError('Skill name must be 64 characters or fewer.')；return: normalized
    - 调用: strip, fullmatch, ValueError, len
  #### `st` `validate_relative_path(relative_path: str, base_dir: Path) -> Path`    @staticmethod  L47
    - _文档首行_（仅供参考）: Validate *relative_path* against *base_dir* and return the resolved target.
    - 分支数 2，函数体节点数 66；raise: ValueError('relative_path must not be empty.'), ValueError('relative_path must resolve within the skill directory.')；return: target
    - 调用: ValueError, resolve, relative_to
  #### `st` `validate_skill_markdown_content(name: str, content: str) -> None`    @staticmethod  L65
    - _文档首行_（仅供参考）: Validate SKILL.md content: parse frontmatter and check name matches.
    - 分支数 3，函数体节点数 113；raise: ValueError(message), ValueError(f"Frontmatter name '{parsed_name}' must match requested skill name '{name}'.")
    - 调用: TemporaryDirectory, Path, validate_skill_name, mkdir, write_text, _validate_skill_frontmatter, ValueError
  - 文件IO: mkdir (L73), write_text (L74)
  #### `m` `__init__(self, container_path: str) -> None`  L29
    - 分支数 0，函数体节点数 16
  #### `m` `ensure_safe_support_path(self, name: str, relative_path: str) -> Path`  L81
    - _文档首行_（仅供参考）: Validate and return the resolved absolute path for a support file.
    - 分支数 5，函数体节点数 186；raise: ValueError('Supporting file path must include a filename.'), ValueError('Supporting file path must be relative.'), ValueError('Supporting file path must not contain parent-directory traversal.'), ValueError(f"Supporting files must live under one of: {', '.join(sorted(_ALLOWED_SUPPORT_SUBDIRS))}."), ValueError('Supporting file path must stay within the selected support directory.')；return: target
    - 调用: resolve, get_custom_skill_dir, validate_skill_name, endswith, ValueError, Path, is_absolute, any, join, sorted, relative_to
  #### `m` `get_skills_root_path(self) -> Path`    @abstractmethod  L108
    - _文档首行_（仅供参考）: Absolute host path to the skills root, used for sandbox mounts.
    - 分支数 0，函数体节点数 9
  #### `m` `validate_skill_file_path(self, skill_file: Path) -> Path`  L114
    - _文档首行_（仅供参考）: Validate that *skill_file* is within an allowed root and return its resolved path.
    - 分支数 1，函数体节点数 51；raise: ValueError('Resolved skill file must stay within the configured skills root.')；return: resolved_file
    - 调用: resolve, get_skills_root_path, relative_to, ValueError
  #### `m` `_iter_skill_files(self) -> Iterable[tuple[SkillCategory, Path, Path]]`    @abstractmethod  L137
    - _文档首行_（仅供参考）: Yield ``(category, category_root, skill_md_path)`` for every SKILL.md.
    - 分支数 0，函数体节点数 23
  #### `m` `read_custom_skill(self, name: str) -> str`    @abstractmethod  L145
    - _文档首行_（仅供参考）: Read SKILL.md content for a custom skill.
    - 分支数 0，函数体节点数 12
  #### `m` `write_custom_skill(self, name: str, relative_path: str, content: str) -> None`    @abstractmethod  L152
    - _文档首行_（仅供参考）: Atomically write a text file under ``custom/<name>/<relative_path>``.
    - 分支数 0，函数体节点数 17
  #### `m` `install_skill_from_archive(self, archive_path: str | Path) -> dict`  L165
    - _文档首行_（仅供参考）: Sync wrapper — delegates to :meth:`ainstall_skill_from_archive`.
    - 分支数 0，函数体节点数 27；return: _run_async_install(self.ainstall_skill_from_archive(archive_path))
    - 调用: _run_async_install, ainstall_skill_from_archive
  #### `m` `delete_custom_skill(self, name: str, *, history_meta: dict | None) -> None`    @abstractmethod  L172
    - _文档首行_（仅供参考）: Delete a custom skill (validation + optional history + directory removal).
    - 分支数 0，函数体节点数 18
  #### `m` `custom_skill_exists(self, name: str) -> bool`    @abstractmethod  L179
    - _文档首行_（仅供参考）: Origin: ``deerflow.skills.manager.custom_skill_exists``.
    - 分支数 0，函数体节点数 12
  #### `m` `public_skill_exists(self, name: str) -> bool`    @abstractmethod  L183
    - _文档首行_（仅供参考）: Origin: ``deerflow.skills.manager.public_skill_exists``.
    - 分支数 0，函数体节点数 12
  #### `m` `append_history(self, name: str, record: dict) -> None`    @abstractmethod  L187
    - _文档首行_（仅供参考）: Append a JSONL history entry for ``name``.
    - 分支数 0，函数体节点数 14
  #### `m` `read_history(self, name: str) -> list[dict]`    @abstractmethod  L194
    - _文档首行_（仅供参考）: Return all history records for ``name``, oldest first.
    - 分支数 0，函数体节点数 16
  #### `m` `get_container_root(self) -> str`  L204
    - _文档首行_（仅供参考）: Origin: ``deerflow.config.skills_config.SkillsConfig.container_path`` accessor.
    - 分支数 0，函数体节点数 12；return: self._container_root
  #### `m` `get_custom_skill_dir(self, name: str) -> Path`  L208
    - _文档首行_（仅供参考）: Path to ``custom/<name>``. Does not create the directory.
    - 分支数 0，函数体节点数 38；return: self.get_skills_root_path() / SkillCategory.CUSTOM.value / normalized_name
    - 调用: validate_skill_name, get_skills_root_path
  #### `m` `get_custom_skill_file(self, name: str) -> Path`  L216
    - _文档首行_（仅供参考）: Path to ``custom/<name>/SKILL.md``.
    - 分支数 0，函数体节点数 32；return: self.get_custom_skill_dir(normalized_name) / SKILL_MD_FILE
    - 调用: validate_skill_name, get_custom_skill_dir
  #### `m` `get_skill_history_file(self, name: str) -> Path`  L224
    - _文档首行_（仅供参考）: Path to ``custom/.history/<name>.jsonl``. Does not create parents.
    - 分支数 0，函数体节点数 44；return: self.get_skills_root_path() / SkillCategory.CUSTOM.value / '.history' / f'{normalized_name}.jsonl'
    - 调用: validate_skill_name, get_skills_root_path
  #### `m` `load_skills(self, *, enabled_only: bool) -> list[Skill]`  L242
    - _文档首行_（仅供参考）: Discover all skills, merge enabled state, sort and optionally filter.
    - 分支数 4，函数体节点数 179；return: skills
    - 调用: _iter_skill_files, parse_skill_file, relative_to, list, values, from_file, replace, is_skill_enabled, warning, sort
  - 文件IO: replace (L271)
  #### `m` `ensure_custom_skill_is_editable(self, name: str) -> None`  L281
    - _文档首行_（仅供参考）: Origin: ``deerflow.skills.manager.ensure_custom_skill_is_editable``.
    - 分支数 2，函数体节点数 46；raise: ValueError(f"'{name}' is a built-in skill. To customise it, create a new skill with the same name under skills/custom/."), FileNotFoundError(f"Custom skill '{name}' not found.")；return: None
    - 调用: custom_skill_exists, public_skill_exists, ValueError, FileNotFoundError
  #### `⏵m` `async ainstall_skill_from_archive(self, archive_path: str | Path) -> dict`    @abstractmethod  L159
    - _文档首行_（仅供参考）: Async install of a skill from a ``.skill`` ZIP archive.
    - 分支数 0，函数体节点数 16

## 文件内调用关系
- `SkillStorage.validate_skill_markdown_content` -> validate_skill_name
- `SkillStorage.ensure_safe_support_path` -> get_custom_skill_dir, validate_skill_name
- `SkillStorage.validate_skill_file_path` -> get_skills_root_path
- `SkillStorage.install_skill_from_archive` -> ainstall_skill_from_archive
- `SkillStorage.get_custom_skill_dir` -> validate_skill_name, get_skills_root_path
- `SkillStorage.get_custom_skill_file` -> validate_skill_name, get_custom_skill_dir
- `SkillStorage.get_skill_history_file` -> validate_skill_name, get_skills_root_path
- `SkillStorage.load_skills` -> _iter_skill_files
- `SkillStorage.ensure_custom_skill_is_editable` -> custom_skill_exists, public_skill_exists

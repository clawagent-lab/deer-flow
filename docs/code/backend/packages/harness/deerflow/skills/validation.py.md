# `backend/packages/harness/deerflow/skills/validation.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/validation.py`  ·  行数: 87

**模块文档首行**（仅供参考）: Skill frontmatter validation utilities.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: re
- `pathlib` -> Path
- `deerflow.skills.frontmatter` -> ALLOWED_FRONTMATTER_PROPERTIES, split_skill_markdown
- `deerflow.skills.parser` -> parse_allowed_tools
- `deerflow.skills.types` -> SKILL_MD_FILE

## 函数
#### `ƒ` `_validate_skill_frontmatter(skill_dir: Path) -> tuple[bool, str, str | None]`  L14
  - _文档首行_（仅供参考）: Validate a skill directory's SKILL.md frontmatter.
  - 分支数 18，函数体节点数 494；return: (False, f'{SKILL_MD_FILE} not found', None), (False, error, None), (False, 'Invalid frontmatter format', None), (False, f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}", None), (False, "Missing 'name' in frontmatter", None), (False, "Missing 'description' in frontmatter", None), (False, f'Name must be a string, got {type(name).__name__}', None), (False, 'Name cannot be empty', None), (False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)", None), (False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens", None), (False, f'Name is too long ({len(name)} characters). Maximum is 64 characters.', None), (False, f'Description must be a string, got {type(description).__name__}', None), (False, 'Description cannot contain angle brackets (< or >)', None), (False, f'Description is too long ({len(description)} characters). Maximum is 1024 characters.', None), (False, str(e).replace(str(skill_md), SKILL_MD_FILE), None), (False, f'required-secrets in {SKILL_MD_FILE} must be a list', None), (False, f'secrets-autonomous in {SKILL_MD_FILE} must be a boolean', None), (True, 'Skill is valid!', name)
  - 调用: exists, read_text, split_skill_markdown, set, keys, join, sorted, get, isinstance, type, strip, match, startswith, endswith, len, parse_allowed_tools, replace, str
  - 文件IO: exists (L24), read_text (L27), replace (L76)

## 文件内调用关系
_无文件内调用_

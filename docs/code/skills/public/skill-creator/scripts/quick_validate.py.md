# `skills/public/skill-creator/scripts/quick_validate.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/quick_validate.py`  ·  行数: 102

**模块文档首行**（仅供参考）: Quick validation script for skills - minimal version

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: sys, re, yaml
- `pathlib` -> Path

## 函数
#### `ƒ` `validate_skill(skill_path)`  L11
  - _文档首行_（仅供参考）: Basic validation of a skill
  - 分支数 20，函数体节点数 474；return: (False, 'SKILL.md not found'), (False, 'No YAML frontmatter found'), (False, 'Invalid frontmatter format'), (False, 'Frontmatter must be a YAML dictionary'), (False, f'Invalid YAML in frontmatter: {e}'), (False, f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"), (False, "Missing 'name' in frontmatter"), (False, "Missing 'description' in frontmatter"), (False, f'Name must be a string, got {type(name).__name__}'), (False, f"Name '{name}' should be kebab-case (lowercase letters, digits, and hyphens only)"), (False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"), (False, f'Name is too long ({len(name)} characters). Maximum is 64 characters.'), (False, f'Description must be a string, got {type(description).__name__}'), (False, 'Description cannot contain angle brackets (< or >)'), (False, f'Description is too long ({len(description)} characters). Maximum is 1024 characters.'), (False, f'Compatibility must be a string, got {type(compatibility).__name__}'), (False, f'Compatibility is too long ({len(compatibility)} characters). Maximum is 500 characters.'), (True, 'Skill is valid!')
  - 调用: Path, exists, read_text, startswith, match, group, safe_load, isinstance, set, keys, join, sorted, get, type, strip, endswith, len
  - 文件IO: exists (L17), read_text (L21)

## 文件内调用关系
_无文件内调用_

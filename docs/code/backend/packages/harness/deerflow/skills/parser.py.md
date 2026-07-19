# `backend/packages/harness/deerflow/skills/parser.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/parser.py`  ·  行数: 201

## 模块概览
- 函数 5 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: logging, re, yaml
- `pathlib` -> Path
- `.types` -> SKILL_MD_FILE, SecretRequirement, Skill, SkillCategory

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_ENV_VAR_NAME_RE` = re.compile('^[A-Za-z_][A-Za-z0-9_]*$')

## 函数
#### `ƒ` `_format_yaml_error(skill_file: Path, exc: yaml.YAMLError, source: str) -> str`  L15
  - _文档首行_（仅供参考）: Render a developer-friendly explanation of a YAML front-matter error.
  - 分支数 3，函数体节点数 204；return: '\n'.join(lines)
  - 调用: getattr, splitlines, len, append, partition, strip, replace, join
  - 文件IO: replace (L35), replace (L35)
  - 反射: getattr (L20), getattr (L31)

#### `ƒ` `parse_allowed_tools(raw: object, skill_file: Path) -> tuple[str, ...] | None`  L41
  - _文档首行_（仅供参考）: Parse the optional allowed-tools frontmatter field.
  - 分支数 5，函数体节点数 123；raise: ValueError(f'allowed-tools in {skill_file} must be a list of strings'), ValueError(f'allowed-tools in {skill_file} must contain only strings'), ValueError(f'allowed-tools in {skill_file} cannot contain empty tool names')；return: None, tuple(allowed_tools)
  - 调用: isinstance, ValueError, strip, append, tuple

#### `ƒ` `parse_required_secrets(raw: object, skill_file: Path) -> tuple[SecretRequirement, ...]`  L64
  - _文档首行_（仅供参考）: Parse the optional required-secrets frontmatter field (issue #3861).
  - 分支数 7，函数体节点数 209；raise: ValueError(f'required-secrets in {skill_file} must be a list')；return: (), tuple(secrets)
  - 调用: isinstance, ValueError, set, strip, str, get, bool, warning, match, add, append, SecretRequirement, tuple

#### `ƒ` `parse_secrets_autonomous(raw: object, skill_file: Path) -> bool`  L101
  - _文档首行_（仅供参考）: Parse the optional ``secrets-autonomous`` frontmatter field (issue #3914).
  - 分支数 2，函数体节点数 44；return: True, raw, False
  - 调用: isinstance, warning

#### `ƒ` `parse_skill_file(skill_file: Path, category: SkillCategory, relative_path: Path | None) -> Skill | None`  L117
  - _文档首行_（仅供参考）: Parse a SKILL.md file and extract metadata.
  - 分支数 11，函数体节点数 390；return: None, Skill(name=name, description=description, license=license_text, skill_dir=skill_file.parent, skill_file=skill_file, relative_path=relative_path or Path(skill_file.parent.name), category=category, allowed_tools=allowed_tools, enabled=True, required_secrets=required_secrets, secrets_autonomous=secrets_autonomous)
  - 调用: exists, read_text, match, group, safe_load, error, _format_yaml_error, isinstance, get, strip, str, parse_allowed_tools, parse_required_secrets, parse_secrets_autonomous, Skill, Path, exception
  - 文件IO: exists (L129), read_text (L133)

## 文件内调用关系
- `parse_skill_file` -> _format_yaml_error, parse_allowed_tools, parse_required_secrets, parse_secrets_autonomous

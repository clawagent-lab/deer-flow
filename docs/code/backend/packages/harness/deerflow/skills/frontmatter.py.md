# `backend/packages/harness/deerflow/skills/frontmatter.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/frontmatter.py`  ·  行数: 68

**模块文档首行**（仅供参考）: Shared SKILL.md frontmatter parsing helpers.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: re, yaml
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> Any

## 模块级常量
- `ALLOWED_FRONTMATTER_PROPERTIES` = {'name', 'description', 'license', 'allowed-tools', 'requ...
- `_FRONTMATTER_RE` = re.compile('^---\\s*\\n(.*?)\\n---\\s*\\n?', re.DOTALL)

## 函数
#### `ƒ` `split_skill_markdown(content: str) -> tuple[SkillMarkdownParts | None, str | None]`  L40
  - _文档首行_（仅供参考）: Split a SKILL.md document into frontmatter and body.
  - 分支数 3，函数体节点数 116；return: (None, 'No YAML frontmatter found'), (None, f'Invalid YAML in frontmatter: {exc}'), (None, 'Frontmatter must be a YAML dictionary'), (SkillMarkdownParts(metadata=metadata, frontmatter_text=frontmatter_text, body=content[match.end():]), None)
  - 调用: match, group, safe_load, isinstance, SkillMarkdownParts, end

## 类
### 类 `SkillMarkdownParts`  L32  @dataclass(...)
- _文档首行_: Parsed pieces of a SKILL.md document.
- 类/实例变量:
  - `metadata` = <annotated>
  - `frontmatter_text` = <annotated>
  - `body` = <annotated>

## 文件内调用关系
_无文件内调用_

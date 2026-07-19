# `skills/public/skill-creator/scripts/utils.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/utils.py`  ·  行数: 48

**模块文档首行**（仅供参考）: Shared utilities for skill-creator scripts.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `pathlib` -> Path

## 函数
#### `ƒ` `parse_skill_md(skill_path: Path) -> tuple[str, str, str]`  L7
  - _文档首行_（仅供参考）: Parse a SKILL.md file, returning (name, description, full_content).
  - 分支数 9，函数体节点数 316；raise: ValueError('SKILL.md missing frontmatter (no opening ---)'), ValueError('SKILL.md missing frontmatter (no closing ---)')；return: (name, description, content)
  - 调用: read_text, split, strip, ValueError, enumerate, len, startswith, append, join
  - 文件IO: read_text (L9)

## 文件内调用关系
_无文件内调用_

# `skills/public/skill-creator/scripts/init_skill.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/init_skill.py`  ·  行数: 304

**模块文档首行**（仅供参考）: Skill Initializer - Creates a new skill from template

## 模块概览
- 函数 3 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: sys
- `pathlib` -> Path

## 模块级常量
- `SKILL_TEMPLATE` = '---\nname: {skill_name}\ndescription: [TODO: Complete an...
- `EXAMPLE_SCRIPT` = '#!/usr/bin/env python3\n"""\nExample helper script for {...
- `EXAMPLE_REFERENCE` = "# Reference Documentation for {skill_title}\n\nThis is a...
- `EXAMPLE_ASSET` = '# Example Asset File\n\nThis placeholder represents wher...

## 函数
#### `ƒ` `title_case_skill_name(skill_name)`  L189
  - _文档首行_（仅供参考）: Convert hyphenated skill name to Title Case for display.
  - 分支数 0，函数体节点数 25；return: ' '.join((word.capitalize() for word in skill_name.split('-')))
  - 调用: join, capitalize, split

#### `ƒ` `init_skill(skill_name, path)`  L194
  - _文档首行_（仅供参考）: Initialize a new skill directory with template SKILL.md.
  - 分支数 4，函数体节点数 311；return: None, skill_dir
  - 调用: resolve, Path, exists, print, mkdir, title_case_skill_name, format, write_text, chmod
  - 文件IO: exists (L209), mkdir (L215), write_text (L230), mkdir (L240), write_text (L242), chmod (L243), mkdir (L248), write_text (L250), mkdir (L255), write_text (L257)

#### `ƒ` `main()`  L273
  - 分支数 2，函数体节点数 151
  - 调用: len, print, exit, init_skill

## 文件内调用关系
- `init_skill` -> title_case_skill_name
- `main` -> init_skill

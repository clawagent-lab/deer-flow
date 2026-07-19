# `skills/public/skill-creator/scripts/package_skill.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/package_skill.py`  ·  行数: 137

**模块文档首行**（仅供参考）: Skill Packager - Creates a distributable .skill file of a skill folder

## 模块概览
- 函数 3 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: fnmatch, sys, zipfile
- `pathlib` -> Path
- `scripts.quick_validate` -> validate_skill

## 模块级常量
- `EXCLUDE_DIRS` = {'__pycache__', 'node_modules'}
- `EXCLUDE_GLOBS` = {'*.pyc'}
- `EXCLUDE_FILES` = {'.DS_Store'}
- `ROOT_EXCLUDE_DIRS` = {'evals'}

## 函数
#### `ƒ` `should_exclude(rel_path: Path) -> bool`  L27
  - _文档首行_（仅供参考）: Check if a path should be excluded from packaging.
  - 分支数 3，函数体节点数 91；return: True, any((fnmatch.fnmatch(name, pat) for pat in EXCLUDE_GLOBS))
  - 调用: any, len, fnmatch

#### `ƒ` `package_skill(skill_path, output_dir)`  L42
  - _文档首行_（仅供参考）: Package a skill folder into a .skill file.
  - 分支数 10，函数体节点数 290；return: None, skill_filename
  - 调用: resolve, Path, exists, print, is_dir, validate_skill, mkdir, cwd, ZipFile, rglob, is_file, relative_to, should_exclude, write
  - 文件IO: exists (L56), exists (L66), mkdir (L83), rglob (L93), write (L100)

#### `ƒ` `main()`  L111
  - 分支数 3，函数体节点数 124
  - 调用: len, print, exit, package_skill

## 文件内调用关系
- `package_skill` -> should_exclude
- `main` -> package_skill

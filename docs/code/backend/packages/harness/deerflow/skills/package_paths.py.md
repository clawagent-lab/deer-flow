# `backend/packages/harness/deerflow/skills/package_paths.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/package_paths.py`  ·  行数: 25

**模块文档首行**（仅供参考）: Shared helpers for skill-package relative paths.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `pathlib` -> PurePosixPath

## 函数
#### `ƒ` `_parts(path: str | PurePosixPath) -> tuple[str, ...]`  L8
  - 分支数 0，函数体节点数 34；return: PurePosixPath(str(path).replace('\\', '/')).parts
  - 调用: PurePosixPath, replace, str
  - 文件IO: replace (L9)

#### `ƒ` `is_eval_fixture_path(path: str | PurePosixPath) -> bool`  L12
  - _文档首行_（仅供参考）: Return whether a path is under an eval fixture directory.
  - 分支数 2，函数体节点数 74；return: parts[index + 1] == 'fixtures', False
  - 调用: _parts, enumerate, len

#### `ƒ` `is_eval_fixture_skill_md(path: str | PurePosixPath) -> bool`  L21
  - _文档首行_（仅供参考）: Return whether a path is an eval fixture's nested SKILL.md file.
  - 分支数 0，函数体节点数 55；return: bool(parts) and parts[-1] == 'SKILL.md' and is_eval_fixture_path(PurePosixPath(*parts[:-1]))
  - 调用: _parts, bool, is_eval_fixture_path, PurePosixPath

## 文件内调用关系
- `is_eval_fixture_path` -> _parts
- `is_eval_fixture_skill_md` -> _parts, is_eval_fixture_path

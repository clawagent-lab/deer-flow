# `backend/packages/harness/deerflow/skills/permissions.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/permissions.py`  ·  行数: 35

**模块文档首行**（仅供参考）: Filesystem permission helpers for installed skill trees.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: stat
- `pathlib` -> Path

## 函数
#### `ƒ` `make_skill_path_sandbox_readable(path: Path) -> None`  L7
  - 分支数 3，函数体节点数 81；return: None
  - 调用: is_symlink, S_IMODE, stat, is_dir, chmod, is_file
  - 文件IO: stat (L10), chmod (L13), chmod (L15)

#### `ƒ` `make_skill_tree_sandbox_readable(target: Path) -> None`  L18
  - 分支数 1，函数体节点数 27
  - 调用: make_skill_path_sandbox_readable, rglob
  - 文件IO: rglob (L20)

#### `ƒ` `make_skill_written_path_sandbox_readable(skill_root: Path, target: Path) -> None`  L24
  - 分支数 1，函数体节点数 79
  - 调用: resolve, relative_to, make_skill_path_sandbox_readable

## 文件内调用关系
- `make_skill_tree_sandbox_readable` -> make_skill_path_sandbox_readable
- `make_skill_written_path_sandbox_readable` -> make_skill_path_sandbox_readable

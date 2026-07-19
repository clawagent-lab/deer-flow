# `backend/packages/harness/deerflow/config/runtime_paths.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/runtime_paths.py`  ·  行数: 42

**模块文档首行**（仅供参考）: Runtime path resolution for standalone harness usage.

## 模块概览
- 函数 4 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: os
- `pathlib` -> Path

## 函数
#### `ƒ` `project_root() -> Path`  L7
  - _文档首行_（仅供参考）: Return the caller project root for runtime-owned files.
  - 分支数 3，函数体节点数 83；raise: ValueError(f"DEER_FLOW_PROJECT_ROOT is set to '{env_root}', but the resolved path '{root}' does not exist."), ValueError(f"DEER_FLOW_PROJECT_ROOT is set to '{env_root}', but the resolved path '{root}' is not a directory.")；return: root, Path.cwd().resolve()
  - 调用: getenv, resolve, Path, exists, ValueError, is_dir, cwd
  - 文件IO: exists (L11)
  - 环境变量: getenv (L9)

#### `ƒ` `runtime_home() -> Path`  L19
  - _文档首行_（仅供参考）: Return the writable DeerFlow state directory.
  - 分支数 1，函数体节点数 32；return: Path(env_home).resolve(), project_root() / '.deer-flow'
  - 调用: getenv, resolve, Path, project_root
  - 环境变量: getenv (L21)

#### `ƒ` `resolve_path(value: str | os.PathLike[str], *, base: Path | None) -> Path`  L26
  - _文档首行_（仅供参考）: Resolve absolute paths as-is and relative paths against the project root.
  - 分支数 1，函数体节点数 62；return: path.resolve()
  - 调用: Path, is_absolute, project_root, resolve

#### `ƒ` `existing_project_file(names: tuple[str, ...]) -> Path | None`  L34
  - _文档首行_（仅供参考）: Return the first existing named file under the project root.
  - 分支数 2，函数体节点数 50；return: candidate, None
  - 调用: project_root, is_file

## 文件内调用关系
- `runtime_home` -> project_root
- `resolve_path` -> project_root
- `existing_project_file` -> project_root

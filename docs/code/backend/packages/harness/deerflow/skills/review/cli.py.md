# `backend/packages/harness/deerflow/skills/review/cli.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/review/cli.py`  ·  行数: 78

**模块文档首行**（仅供参考）: CLI entry point for deterministic skill review facts.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: argparse, sys
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Any
- `deerflow.skills.review.analyzer` -> analyze_skill_package
- `deerflow.skills.review.models` -> DEFAULT_PACKAGE_LIMITS, SEVERITY_RANK, PackageLimits, stable_json_dumps
- `deerflow.skills.review.readers` -> ArchivePackageReader, LocalDirectoryReader

## 函数
#### `ƒ` `main(argv: list[str] | None) -> int`  L15
  - 分支数 1，函数体节点数 255；return: _exit_code(facts, args.fail_on, fail_on_incomplete=args.fail_on_incomplete)
  - 调用: ArgumentParser, add_argument, parse_args, PackageLimits, Path, ArchivePackageReader, LocalDirectoryReader, analyze_skill_package, read, print, stable_json_dumps, _print_text, _exit_code
  - 文件IO: read (L39)

#### `ƒ` `_print_text(facts: dict[str, Any]) -> None`  L49
  - 分支数 2，函数体节点数 220
  - 调用: get, print, join

#### `ƒ` `_exit_code(facts: dict[str, Any], fail_on: str, *, fail_on_incomplete: bool) -> int`  L64
  - 分支数 4，函数体节点数 92；return: 1, 0
  - 调用: get, str

## 文件内调用关系
- `main` -> _print_text, _exit_code

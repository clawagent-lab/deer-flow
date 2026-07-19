# `backend/scripts/run_replay_gateway.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/scripts/run_replay_gateway.py`  ·  行数: 74

**模块文档首行**（仅供参考）: Start a hermetic *replay* gateway for the full-stack (Layer 2) e2e.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: argparse, os, sys, tempfile
- `__future__` -> annotations
- `pathlib` -> Path

## 模块级常量
- `_BACKEND` = Path(__file__).resolve().parents[1]

## 函数
#### `ƒ` `main() -> int`  L27
  - 分支数 1，函数体节点数 327；return: 0
  - 调用: ArgumentParser, add_argument, str, parse_args, Path, mkdtemp, write_text, build_config_yaml, prepare_hermetic_extras, setdefault, join, get, include_router, print, run
  - 文件IO: write_text (L38)
  - 子进程: run (L68)

## 文件内调用关系
_无文件内调用_

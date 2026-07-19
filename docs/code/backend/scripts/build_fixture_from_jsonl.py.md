# `backend/scripts/build_fixture_from_jsonl.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/scripts/build_fixture_from_jsonl.py`  ·  行数: 46

**模块文档首行**（仅供参考）: Turn a record-through-browser JSONL capture into a replay fixture.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: argparse, json
- `__future__` -> annotations
- `pathlib` -> Path

## 函数
#### `ƒ` `main() -> int`  L16
  - 分支数 1，函数体节点数 293；return: 0
  - 调用: ArgumentParser, add_argument, parse_args, loads, splitlines, read_text, Path, strip, get, write_text, dumps, print, len, enumerate, str
  - 文件IO: read_text (L24), read_text (L25), write_text (L34)

## 文件内调用关系
_无文件内调用_

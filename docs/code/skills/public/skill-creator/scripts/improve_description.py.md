# `skills/public/skill-creator/scripts/improve_description.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/improve_description.py`  ·  行数: 248

**模块文档首行**（仅供参考）: Improve a skill description based on eval results.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: argparse, json, os, re, subprocess, sys
- `pathlib` -> Path
- `scripts.utils` -> parse_skill_md

## 函数
#### `ƒ` `_call_claude(prompt: str, model: str | None, timeout: int) -> str`  L20
  - _文档首行_（仅供参考）: Run `claude -p` with the prompt on stdin and return the text response.
  - 分支数 2，函数体节点数 122；raise: RuntimeError(f'claude -p exited {result.returncode}\nstderr: {result.stderr}')；return: result.stdout
  - 调用: extend, items, run, RuntimeError
  - 子进程: run (L35)

#### `ƒ` `improve_description(skill_name: str, skill_content: str, current_description: str, eval_results: dict, history: list[dict], model: str, test_results: dict | None, log_dir: Path | None, iteration: int | None) -> str`  L50
  - _文档首行_（仅供参考）: Call Claude to improve the description based on eval results.
  - 分支数 12，函数体节点数 765；return: description
  - 调用: get, _call_claude, search, strip, group, len, mkdir, write_text, dumps
  - 文件IO: mkdir (L187), write_text (L189)

#### `ƒ` `main()`  L194
  - 分支数 4，函数体节点数 343
  - 调用: ArgumentParser, add_argument, parse_args, Path, exists, print, exit, loads, read_text, parse_skill_md, improve_description, dumps
  - 文件IO: exists (L204), read_text (L208), read_text (L211)

## 文件内调用关系
- `improve_description` -> _call_claude
- `main` -> improve_description

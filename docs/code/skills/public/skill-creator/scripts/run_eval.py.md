# `skills/public/skill-creator/scripts/run_eval.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/run_eval.py`  ·  行数: 311

**模块文档首行**（仅供参考）: Run trigger evaluation for a skill description.

## 模块概览
- 函数 4 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: argparse, json, os, select, subprocess, sys, time, uuid
- `concurrent.futures` -> ProcessPoolExecutor, as_completed
- `pathlib` -> Path
- `scripts.utils` -> parse_skill_md

## 函数
#### `ƒ` `find_project_root() -> Path`  L22
  - _文档首行_（仅供参考）: Find the project root by walking up from cwd looking for .claude/.
  - 分支数 2，函数体节点数 42；return: parent, current
  - 调用: cwd, is_dir

#### `ƒ` `run_single_query(query: str, skill_name: str, skill_description: str, timeout: int, project_root: str, model: str | None) -> bool`  L35
  - _文档首行_（仅供参考）: Run a single query and return whether the skill was triggered.
  - 分支数 29，函数体节点数 721；return: False, True, clean_name in accumulated_json, triggered
  - 调用: uuid4, Path, mkdir, join, split, write_text, extend, items, Popen, time, poll, read, decode, select, fileno, strip, loads, get, kill, wait（+2）
  - 文件IO: mkdir (L57), write_text (L68), read (L103), read (L112), exists (L180), unlink (L181)
  - 子进程: Popen (L85)

#### `ƒ` `run_eval(eval_set: list[dict], skill_name: str, description: str, num_workers: int, timeout: int, project_root: Path, runs_per_query: int, trigger_threshold: float, model: str | None) -> dict`  L184
  - _文档首行_（仅供参考）: Run the full eval set and return results.
  - 分支数 8，函数体节点数 394；return: {'skill_name': skill_name, 'description': description, 'results': results, 'summary': {'total': total, 'passed': passed, 'failed': total - passed}}
  - 调用: ProcessPoolExecutor, range, submit, str, as_completed, append, result, print, items, sum, len

#### `ƒ` `main()`  L259
  - 分支数 4，函数体节点数 407
  - 调用: ArgumentParser, add_argument, parse_args, loads, read_text, Path, exists, print, exit, parse_skill_md, find_project_root, run_eval, dumps
  - 文件IO: read_text (L272), exists (L275)

## 文件内调用关系
- `main` -> find_project_root, run_eval

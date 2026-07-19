# `skills/public/skill-creator/scripts/run_loop.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/run_loop.py`  ·  行数: 329

**模块文档首行**（仅供参考）: Run the eval + improve loop until all pass or max iterations reached.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: argparse, json, random, sys, tempfile, time, webbrowser
- `pathlib` -> Path
- `scripts.generate_report` -> generate_html
- `scripts.improve_description` -> improve_description
- `scripts.run_eval` -> find_project_root, run_eval
- `scripts.utils` -> parse_skill_md

## 函数
#### `ƒ` `split_eval_set(eval_set: list[dict], holdout: float, seed: int) -> tuple[list[dict], list[dict]]`  L24
  - _文档首行_（仅供参考）: Split eval set into train and test sets, stratified by should_trigger.
  - 分支数 0，函数体节点数 177；return: (train_set, test_set)
  - 调用: seed, shuffle, max, int, len

#### `ƒ` `run_loop(eval_set: list[dict], skill_path: Path, description_override: str | None, num_workers: int, timeout: int, max_iterations: int, runs_per_query: int, trigger_threshold: float, holdout: float, model: str, verbose: bool, live_report_path: Path | None, log_dir: Path | None) -> dict`  L47
  - _文档首行_（仅供参考）: Run the eval + improvement loop.
  - 分支数 17，函数体节点数 1379；return: {'exit_reason': exit_reason, 'original_description': original_description, 'best_description': best['description'], 'best_score': best_score, 'best_train_score': f"{best['train_passed']}/{best['train_total']}", 'best_test_score': f"{best['test_passed']}/{best['test_total']}" if test_set else None, 'final_description': current_description, 'iterations_run': len(history), 'holdout': holdout, 'train_size': len(train_set), 'test_size': len(test_set), 'history': history}
  - 调用: find_project_root, parse_skill_md, split_eval_set, print, len, range, time, run_eval, sum, append, write_text, generate_html, print_eval_stats, items, startswith, improve_description, max
  - 文件IO: write_text (L151)

#### `ƒ` `main()`  L244
  - 分支数 8，函数体节点数 562
  - 调用: ArgumentParser, add_argument, parse_args, loads, read_text, Path, exists, print, exit, parse_skill_md, strftime, gettempdir, write_text, open, str, mkdir, run_loop, dumps, generate_html
  - 文件IO: read_text (L261), exists (L264), write_text (L278), open (L279), mkdir (L287), write_text (L313), write_text (L317), write_text (L321)

## 文件内调用关系
- `run_loop` -> split_eval_set
- `main` -> run_loop

# `skills/public/skill-creator/scripts/aggregate_benchmark.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/aggregate_benchmark.py`  ·  行数: 402

**模块文档首行**（仅供参考）: Aggregate individual run results into benchmark summary statistics.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: argparse, json, math, sys
- `datetime` -> datetime, timezone
- `pathlib` -> Path

## 函数
#### `ƒ` `calculate_stats(values: list[float]) -> dict`  L45
  - _文档首行_（仅供参考）: Calculate mean, stddev, min, max for a list of values.
  - 分支数 2，函数体节点数 132；return: {'mean': 0.0, 'stddev': 0.0, 'min': 0.0, 'max': 0.0}, {'mean': round(mean, 4), 'stddev': round(stddev, 4), 'min': round(min(values), 4), 'max': round(max(values), 4)}
  - 调用: len, sum, sqrt, round, min, max

#### `ƒ` `load_run_results(benchmark_dir: Path) -> dict`  L67
  - _文档首行_（仅供参考）: Load all run results from a benchmark directory.
  - 分支数 21，函数体节点数 679；return: {}, results
  - 调用: exists, list, glob, print, enumerate, sorted, open, get, load, int, split, iterdir, is_dir, extend, append
  - 文件IO: exists (L76), glob (L78), glob (L86), exists (L88), open (L90), iterdir (L101), glob (L105), glob (L111), exists (L115), open (L120), exists (L140), open (L142)

#### `ƒ` `aggregate_results(results: dict) -> dict`  L176
  - _文档首行_（仅供参考）: Aggregate run results into summary statistics.
  - 分支数 3，函数体节点数 332；return: run_summary
  - 调用: list, keys, get, calculate_stats, len

#### `ƒ` `generate_benchmark(benchmark_dir: Path, skill_name: str, skill_path: str) -> dict`  L227
  - _文档首行_（仅供参考）: Generate complete benchmark.json from run results.
  - 分支数 2，函数体节点数 223；return: benchmark
  - 调用: load_run_results, aggregate_results, append, get, sorted, set, values, strftime, now

#### `ƒ` `generate_markdown(benchmark: dict) -> str`  L281
  - _文档首行_（仅供参考）: Generate human-readable benchmark.md from benchmark data.
  - 分支数 2，函数体节点数 503；return: '\n'.join(lines)
  - 调用: len, title, replace, join, map, get, append, extend
  - 文件IO: replace (L290), replace (L291)

#### `ƒ` `main()`  L338
  - 分支数 4，函数体节点数 313
  - 调用: ArgumentParser, add_argument, parse_args, exists, print, exit, generate_benchmark, with_suffix, open, dump, generate_markdown, write, get, title, replace
  - 文件IO: exists (L365), open (L377), open (L383), write (L384), replace (L395)

## 文件内调用关系
- `aggregate_results` -> calculate_stats
- `generate_benchmark` -> load_run_results, aggregate_results
- `main` -> generate_benchmark, generate_markdown

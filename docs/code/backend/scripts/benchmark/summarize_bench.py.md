# `backend/scripts/benchmark/summarize_bench.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/scripts/benchmark/summarize_bench.py`  ·  行数: 194

**模块文档首行**（仅供参考）: Aggregate JSONL benchmark results into summary tables.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: argparse, json, sys
- `__future__` -> annotations
- `collections` -> defaultdict
- `pathlib` -> Path
- `typing` -> Any

## 模块级常量
- `_COLUMNS` = ['provider', 'scenario', 'workload', 'concurrency', 'coun...

## 函数
#### `ƒ` `_p(arr: list[float], pct: float) -> float`  L21
  - 分支数 2，函数体节点数 124；return: 0.0, s[0], s[lower] * (1 - weight) + s[upper] * weight
  - 调用: sorted, len, int, min

#### `ƒ` `_load_jsonl(paths: list[Path]) -> list[dict[str, Any]]`  L34
  - 分支数 6，函数体节点数 164；raise: ValueError('Malformed JSONL row(s):\n' + '\n'.join(errors))；return: rows
  - 调用: open, enumerate, strip, startswith, append, loads, ValueError, join
  - 文件IO: open (L38)

#### `ƒ` `_group_key(row: dict[str, Any], group_by: list[str]) -> tuple`  L52
  - 分支数 0，函数体节点数 40；return: tuple((row.get(k, '?') for k in group_by))
  - 调用: tuple, get

#### `ƒ` `_summarize(rows: list[dict[str, Any]], group_by: list[str]) -> list[dict[str, Any]]`  L56
  - 分支数 3，函数体节点数 534；return: summary
  - 调用: defaultdict, append, _group_key, sorted, items, get, sum, len, enumerate, round, _p

#### `ƒ` `_print_table(rows: list[dict[str, Any]], fmt: str) -> None`  L118
  - 分支数 5，函数体节点数 254；return: None, '  '.join(parts)
  - 调用: DictWriter, writeheader, writerows, print, any, get, len, str, max, rjust, zip, join, _fmt_row

#### `ƒ` `main(argv: list[str] | None) -> int`  L149
  - 分支数 4，函数体节点数 217；return: 1, 0
  - 调用: ArgumentParser, add_argument, parse_args, Path, _load_jsonl, print, str, strip, split, _summarize, dump, _print_table

## 文件内调用关系
- `_summarize` -> _group_key, _p
- `main` -> _load_jsonl, _summarize, _print_table

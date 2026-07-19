# `skills/public/skill-creator/scripts/generate_report.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/scripts/generate_report.py`  ·  行数: 327

**模块文档首行**（仅供参考）: Generate an HTML report from run_loop.py output.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: argparse, html, json, sys
- `pathlib` -> Path

## 函数
#### `ƒ` `generate_html(data: dict, auto_refresh: bool, skill_name: str) -> str`  L16
  - _文档首行_（仅供参考）: Generate HTML report from loop output data. If auto_refresh is True, adds a meta refresh tag.
  - 分支数 15，函数体节点数 1041；return: (correct, total), 'score-good', 'score-ok', 'score-bad', ''.join(html_parts)
  - 调用: get, escape, append, max, aggregate_runs, score_class, join

#### `ƒ` `main()`  L304
  - 分支数 2，函数体节点数 143
  - 调用: ArgumentParser, add_argument, parse_args, load, loads, read_text, Path, generate_html, write_text, print
  - 文件IO: read_text (L314), write_text (L319)

## 文件内调用关系
- `main` -> generate_html

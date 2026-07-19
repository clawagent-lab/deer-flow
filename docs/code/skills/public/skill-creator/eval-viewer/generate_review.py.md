# `skills/public/skill-creator/eval-viewer/generate_review.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/skill-creator/eval-viewer/generate_review.py`  ·  行数: 472

**模块文档首行**（仅供参考）: Generate and serve a review page for eval results.

## 模块概览
- 函数 9 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: argparse, base64, json, mimetypes, os, re, signal, subprocess, sys, time, webbrowser
- `functools` -> partial
- `http.server` -> HTTPServer, BaseHTTPRequestHandler
- `pathlib` -> Path

## 模块级常量
- `METADATA_FILES` = {'transcript.md', 'user_notes.md', 'metrics.json'}
- `TEXT_EXTENSIONS` = {'.txt', '.md', '.json', '.csv', '.py', '.js', '.ts', '.t...
- `IMAGE_EXTENSIONS` = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'}
- `MIME_OVERRIDES` = {'.svg': 'image/svg+xml', '.xlsx': 'application/vnd.openx...

## 函数
#### `ƒ` `get_mime_type(path: Path) -> str`  L52
  - 分支数 1，函数体节点数 54；return: MIME_OVERRIDES[ext], mime or 'application/octet-stream'
  - 调用: lower, guess_type, str

#### `ƒ` `find_runs(workspace: Path) -> list[dict]`  L60
  - _文档首行_（仅供参考）: Recursively find directories that contain an outputs/ subdirectory.
  - 分支数 0，函数体节点数 64；return: runs
  - 调用: _find_runs_recursive, sort, get, float

#### `ƒ` `_find_runs_recursive(root: Path, current: Path, runs: list[dict]) -> None`  L68
  - 分支数 5，函数体节点数 107；return: None
  - 调用: is_dir, build_run, append, sorted, iterdir, _find_runs_recursive
  - 文件IO: iterdir (L80)

#### `ƒ` `build_run(root: Path, run_dir: Path) -> dict | None`  L85
  - _文档首行_（仅供参考）: Build a run dict with prompt, outputs, and grading data.
  - 分支数 18，函数体节点数 332；return: {'id': run_id, 'prompt': prompt, 'eval_id': eval_id, 'outputs': output_files, 'grading': grading}
  - 调用: exists, loads, read_text, get, search, strip, group, replace, str, relative_to, is_dir, sorted, iterdir, is_file, append, embed_file
  - 文件IO: exists (L92), read_text (L94), exists (L105), read_text (L107), replace (L119), replace (L119), iterdir (L125), exists (L132), read_text (L134)

#### `ƒ` `embed_file(path: Path) -> dict`  L149
  - _文档首行_（仅供参考）: Read a file and return an embedded representation.
  - 分支数 9，函数体节点数 306；return: {'name': path.name, 'type': 'text', 'content': content}, {'name': path.name, 'type': 'error', 'content': '(Error reading file)'}, {'name': path.name, 'type': 'image', 'mime': mime, 'data_uri': f'data:{mime};base64,{b64}'}, {'name': path.name, 'type': 'pdf', 'data_uri': f'data:{mime};base64,{b64}'}, {'name': path.name, 'type': 'xlsx', 'data_b64': b64}, {'name': path.name, 'type': 'binary', 'mime': mime, 'data_uri': f'data:{mime};base64,{b64}'}
  - 调用: lower, get_mime_type, read_text, read_bytes, decode, b64encode
  - 文件IO: read_text (L156), read_bytes (L166), read_bytes (L178), read_bytes (L189), read_bytes (L201)

#### `ƒ` `load_previous_iteration(workspace: Path) -> dict[str, dict]`  L213
  - _文档首行_（仅供参考）: Load previous iteration's feedback and outputs.
  - 分支数 5，函数体节点数 201；return: result
  - 调用: exists, loads, read_text, get, strip, find_runs, items
  - 文件IO: exists (L223), read_text (L225)

#### `ƒ` `generate_html(runs: list[dict], skill_name: str, previous: dict[str, dict] | None, benchmark: dict | None) -> str`  L250
  - _文档首行_（仅供参考）: Generate the complete standalone HTML page with embedded data.
  - 分支数 5，函数体节点数 194；return: template.replace('/*__EMBEDDED_DATA__*/', f'const EMBEDDED_DATA = {data_json};')
  - 调用: Path, read_text, items, get, dumps, replace
  - 文件IO: read_text (L258), replace (L281)

#### `ƒ` `_kill_port(port: int) -> None`  L288
  - _文档首行_（仅供参考）: Kill any process listening on the given port.
  - 分支数 5，函数体节点数 113
  - 调用: run, split, strip, kill, int, sleep, print
  - 子进程: run (L291)

#### `ƒ` `main() -> None`  L387
  - 分支数 10，函数体节点数 537
  - 调用: ArgumentParser, add_argument, parse_args, resolve, is_dir, print, exit, find_runs, replace, load_previous_iteration, exists, loads, read_text, generate_html, mkdir, write_text, _kill_port, partial, HTTPServer, len（+3）
  - 文件IO: replace (L416), exists (L425), read_text (L427), mkdir (L433), write_text (L434), open (L461)

## 类
### 类 `ReviewHandler`  L308
- 继承: BaseHTTPRequestHandler
- _文档首行_: Serves the review HTML and handles feedback saves.
- 方法:
  #### `m` `__init__(self, workspace: Path, skill_name: str, feedback_path: Path, previous: dict[str, dict], benchmark_path: Path | None, *args, **kwargs)`  L315
    - 分支数 0，函数体节点数 80；可变参数（*args/**kwargs）
    - 调用: __init__, super
  #### `m` `do_GET(self) -> None`  L332
    - 分支数 5，函数体节点数 231
    - 调用: find_runs, exists, loads, read_text, generate_html, encode, send_response, send_header, str, len, end_headers, write, read_bytes, send_error
  - 文件IO: exists (L337), read_text (L339), write (L348), exists (L351), read_bytes (L352), write (L357)
  #### `m` `do_POST(self) -> None`  L361
    - 分支数 3，函数体节点数 185；raise: ValueError("Expected JSON object with 'reviews' key")
    - 调用: int, get, read, loads, isinstance, ValueError, write_text, dumps, send_response, encode, str, send_header, len, end_headers, write, send_error
  - 文件IO: read (L364), write_text (L369), write (L378)
  #### `m` `log_message(self, format: str, *args) -> None`  L382
    - 分支数 0，函数体节点数 11；可变参数（*args/**kwargs）

## 文件内调用关系
- `find_runs` -> _find_runs_recursive
- `_find_runs_recursive` -> build_run, _find_runs_recursive
- `build_run` -> embed_file
- `embed_file` -> get_mime_type
- `load_previous_iteration` -> find_runs
- `main` -> find_runs, load_previous_iteration, generate_html, _kill_port
- `ReviewHandler.__init__` -> __init__
- `ReviewHandler.do_GET` -> find_runs, generate_html

# `backend/packages/harness/deerflow/tui/cli.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/cli.py`  ·  行数: 238

**模块文档首行**（仅供参考）: Command-line entry point and launch-mode planning for the DeerFlow TUI.

## 模块概览
- 函数 10 个，类 1 个，模块级常量 3 个

## 依赖（import）
- 模块: argparse, json, os, sys
- `__future__` -> annotations
- `collections.abc` -> Sequence
- `dataclasses` -> dataclass
- `typing` -> Literal

## 模块级常量
- `_UNSET` = object()
- `Mode` = Literal['tui', 'print', 'json', 'headless-help']
- `_HEADLESS_HELP` = 'deerflow — DeerFlow terminal workbench\n\n  deerflow    ...

## 函数
#### `ƒ` `build_parser() -> argparse.ArgumentParser`  L36
  - 分支数 0，函数体节点数 124；return: parser
  - 调用: ArgumentParser, add_argument

#### `ƒ` `_strip_chat(argv: Sequence[str]) -> list[str]`  L68
  - _文档首行_（仅供参考）: Accept an optional leading ``chat`` subcommand as an alias for the default surface.
  - 分支数 1，函数体节点数 48；return: argv[1:], argv
  - 调用: list

#### `ƒ` `_truthy(value: object) -> bool`  L76
  - 分支数 0，函数体节点数 32；return: isinstance(value, str) and value.strip().lower() in {'1', 'true', 'yes', 'on'}
  - 调用: isinstance, lower, strip

#### `ƒ` `plan_launch(argv: Sequence[str], *, stdin_isatty: bool, stdout_isatty: bool, env: dict[str, str]) -> LaunchPlan`  L80
  - _文档首行_（仅供参考）: Decide what surface to launch. Pure: no I/O, no client construction.
  - 分支数 8，函数体节点数 331；return: LaunchPlan(mode='headless-help', reason='--print needs a MESSAGE argument or piped stdin.'), LaunchPlan(mode='print', message=message, read_stdin=message is None, thread_id=resume, continue_recent=continue_recent), LaunchPlan(mode='headless-help', reason='--json needs a MESSAGE argument or piped stdin.'), LaunchPlan(mode='json', message=message, read_stdin=message is None, thread_id=resume, continue_recent=continue_recent), LaunchPlan(mode='print', message=positional, thread_id=resume, continue_recent=continue_recent), LaunchPlan(mode='print', message=None, read_stdin=True, thread_id=resume, continue_recent=continue_recent), LaunchPlan(mode='headless-help', reason='--cli needs a message. Try: deerflow --print "your question".'), LaunchPlan(mode='tui', message=positional, thread_id=resume, continue_recent=continue_recent, forced_tui=forced_tui), LaunchPlan(mode='headless-help', message=positional, thread_id=resume, continue_recent=continue_recent, reason='No interactive terminal detected. Use --print MESSAGE for one-shot output, or --tui to force the UI.')
  - 调用: parse_args, build_parser, _strip_chat, strip, join, bool, isinstance, LaunchPlan, _truthy, get

#### `ƒ` `_resolve_message(plan: LaunchPlan) -> str`  L152
  - 分支数 1，函数体节点数 31；return: sys.stdin.read().strip(), plan.message or ''
  - 调用: strip, read
  - 文件IO: read (L154)

#### `ƒ` `main(argv: Sequence[str] | None) -> int`  L158
  - 分支数 4，函数体节点数 150；return: 0 if not plan.reason else 2, _run_print(plan), _run_json(plan), _run_tui(plan)
  - 调用: list, plan_launch, isatty, dict, print, _run_print, _run_json, _run_tui

#### `ƒ` `_make_session()`  L182
  - 分支数 0，函数体节点数 10；return: open_session(persistence=False)
  - 调用: open_session

#### `ƒ` `_run_print(plan: LaunchPlan) -> int`  L191
  - 分支数 1，函数体节点数 71；return: 2, 0
  - 调用: _resolve_message, print, _make_session, resolve_thread, chat

#### `ƒ` `_run_json(plan: LaunchPlan) -> int`  L203
  - 分支数 2，函数体节点数 110；return: 2, 0
  - 调用: _resolve_message, print, _make_session, resolve_thread, stream, write, dumps, flush
  - 文件IO: write (L212)

#### `ƒ` `_run_tui(plan: LaunchPlan) -> int`  L217
  - 分支数 3，函数体节点数 90；raise: bare raise；return: 1, 0, run_tui(plan)
  - 调用: getattr, str, print, run_tui
  - 反射: getattr (L224)

## 类
### 类 `LaunchPlan`  L26  @dataclass
- 类/实例变量:
  - `mode` = <annotated>
  - `message` = None
  - `read_stdin` = False
  - `thread_id` = None
  - `continue_recent` = False
  - `forced_tui` = False
  - `reason` = ''

## 文件内调用关系
- `plan_launch` -> build_parser, _strip_chat, _truthy
- `main` -> plan_launch, _run_print, _run_json, _run_tui
- `_run_print` -> _resolve_message, _make_session
- `_run_json` -> _resolve_message, _make_session

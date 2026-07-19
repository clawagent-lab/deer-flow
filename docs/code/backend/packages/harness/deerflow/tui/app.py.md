# `backend/packages/harness/deerflow/tui/app.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/app.py`  ·  行数: 698

**模块文档首行**（仅供参考）: The Textual application — a terminal workbench over the embedded harness.

## 模块概览
- 函数 1 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: uuid
- `__future__` -> annotations
- `functools` -> partial
- `textual.app` -> App, ComposeResult
- `textual.binding` -> Binding
- `textual.containers` -> Vertical, VerticalScroll
- `textual.screen` -> ModalScreen
- `textual.widgets` -> Input, Label, OptionList, Static
- `textual.widgets.option_list` -> Option
- `deerflow.runtime.goal` -> parse_goal_command
- `.input_history` -> InputHistory
- `.render` -> render_header, render_status, render_transcript
- `.runtime` -> stream_actions
- `.theme` -> SYMBOLS, THEME
- `.view_state` -> ClearRows, RunEnded, RunStarted, SystemMessage, ThreadTitle, UserSubmitted, initial_state, reduce
- `.widgets.composer` -> ComposerInput

## 模块级常量
- `_HELP_TEXT` = 'Commands:  /new  /threads  /goal  /model  /skills  /tool...

## 函数
#### `ƒ` `run_tui(plan) -> int`  L685
  - _文档首行_（仅供参考）: Construct the embedded session and run the app. Returns a process exit code.
  - 分支数 1，函数体节点数 40；return: 0
  - 调用: open_session, DeerFlowTUI, run, close
  - 子进程: run (L692)

## 类
### 类 `SelectScreen`  L42
- 继承: ModalScreen
- _文档首行_: A centered modal that returns the id of the chosen option (or None).
- 类/实例变量:
  - `BINDINGS` = [Binding('escape', 'cancel', 'Close')]
- 方法:
  #### `m` `__init__(self, title: str, options: list[tuple[str, str]]) -> None`  L47
    - 分支数 0，函数体节点数 43
    - 调用: __init__, super
  #### `m` `compose(self) -> ComposeResult`  L52
    - 分支数 1，函数体节点数 52；生成器（yield）
    - 调用: Vertical
  #### `m` `on_mount(self) -> None`  L57
    - 分支数 0，函数体节点数 15
    - 调用: focus, query_one
  #### `m` `on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None`  L60
    - 分支数 0，函数体节点数 19
    - 调用: dismiss
  #### `m` `action_cancel(self) -> None`  L63
    - 分支数 0，函数体节点数 11
    - 调用: dismiss

### 类 `DeerFlowTUI`  L67
- 继承: App
- 类/实例变量:
  - `CSS` = f'\n    Screen {{\n        background: {THEME.bg};\n     ...
  - `BINDINGS` = [Binding('ctrl+c', 'interrupt', 'Interrupt / Quit', prior...
- 方法:
  #### `m` `__init__(self, session, plan) -> None`  L158
    - 分支数 0，函数体节点数 148
    - 调用: __init__, super, initial_state, InputHistory
  #### `m` `compose(self) -> ComposeResult`  L180
    - 分支数 1，函数体节点数 49；生成器（yield）
    - 调用: VerticalScroll
  #### `m` `on_mount(self) -> None`  L188
    - 分支数 1，函数体节点数 78
    - 调用: _load_session_info, _refresh_all, set_interval, focus, query_one, getattr, _send_to_agent
  - 反射: getattr (L194)
  #### `m` `_load_session_info(self) -> None`  L199
    - 分支数 2，函数体节点数 183
    - 调用: resolve_thread, get, list_models, next, list_skills, len
  #### `m` `on_input_submitted(self, event: Input.Submitted) -> None`  L219
    - 分支数 1，函数体节点数 57；return: None
    - 调用: strip, _close_palette, add, _handle_submit
  #### `m` `on_input_changed(self, event: Input.Changed) -> None`  L228
    - 分支数 1，函数体节点数 72
    - 调用: startswith, filter_commands, build_registry, _open_palette, _close_palette
  #### `m` `check_action(self, action: str, parameters)`  L243
    - 分支数 3，函数体节点数 58；return: None, True, True if self._palette_open else None
    - 调用: len
  #### `m` `action_nav_up(self) -> None`  L258
    - 分支数 1，函数体节点数 38
    - 调用: action_palette_up, _history_move, up, query_one
  #### `m` `action_nav_down(self) -> None`  L264
    - 分支数 1，函数体节点数 28
    - 调用: action_palette_down, _history_move, down
  #### `m` `_history_move(self, value: str) -> None`  L270
    - 分支数 0，函数体节点数 35
    - 调用: query_one, len
  #### `m` `_open_palette(self, items: list) -> None`  L275
    - 分支数 1，函数体节点数 76；return: None
    - 调用: _close_palette, min, len, query_one, add_class, _render_palette
  #### `m` `_close_palette(self) -> None`  L286
    - 分支数 1，函数体节点数 52；return: None
    - 调用: remove_class, query_one
  #### `m` `_render_palette(self) -> None`  L294
    - 分支数 0，函数体节点数 29
    - 调用: update, query_one, render_palette
  #### `m` `_current_palette_item(self)`  L299
    - 分支数 1，函数体节点数 32；return: self._palette_items[self._palette_index], None
    - 调用: len
  #### `m` `action_palette_down(self) -> None`  L304
    - 分支数 1，函数体节点数 40
    - 调用: min, len, _render_palette
  #### `m` `action_palette_up(self) -> None`  L309
    - 分支数 1，函数体节点数 31
    - 调用: max, _render_palette
  #### `m` `action_palette_complete(self) -> None`  L314
    - 分支数 1，函数体节点数 15
    - 调用: _fill_from_palette
  #### `m` `action_palette_accept(self) -> None`  L321
    - 分支数 2，函数体节点数 68；return: None
    - 调用: _current_palette_item, getattr, _fill_from_palette, _close_palette, query_one, _handle_submit
  - 反射: getattr (L325)
  #### `m` `_fill_from_palette(self) -> None`  L333
    - 分支数 1，函数体节点数 61；return: None
    - 调用: _current_palette_item, query_one, len, _close_palette
  #### `m` `_handle_submit(self, text: str) -> None`  L342
    - 分支数 2，函数体节点数 81；return: None
    - 调用: resolve, _handle_builtin, _dispatch, SystemMessage, _send_to_agent
  #### `m` `_handle_builtin(self, name: str, args: str) -> None`  L356
    - 分支数 18，函数体节点数 290
    - 调用: _interrupt_run, exit, _dispatch, SystemMessage, initial_state, ClearRows, _open_model_picker, _open_thread_switcher, _resume_thread, _handle_goal, _show_skills, _show_mcp, _show_memory, _show_usage, _show_config, _show_uploads
  #### `m` `_open_model_picker(self) -> None`  L405
    - 分支数 3，函数体节点数 145；return: None
    - 调用: get, list_models, _dispatch, SystemMessage, _refresh_header, push_screen, SelectScreen
  #### `m` `_open_thread_switcher(self) -> None`  L424
    - 分支数 5，函数体节点数 148；return: None
    - 调用: recent_threads, get, append, _dispatch, SystemMessage, _switch_to_thread, push_screen, SelectScreen
  #### `m` `_resume_thread(self, ref: str) -> None`  L446
    - _文档首行_（仅供参考）: /resume [id-or-title]: switch to a thread, or open the picker if blank.
    - 分支数 1，函数体节点数 44；return: None
    - 调用: strip, _open_thread_switcher, _switch_to_thread, resolve_ref
  #### `m` `_switch_to_thread(self, thread_id: str) -> None`  L454
    - 分支数 0，函数体节点数 47
    - 调用: initial_state, _dispatch, SystemMessage, _refresh_header
  #### `m` `_handle_goal(self, args: str) -> None`  L460
    - 分支数 9，函数体节点数 261；return: None
    - 调用: parse_goal_command, _dispatch, SystemMessage, get, get_goal, clear_goal, str, uuid4, _refresh_header, set_goal
  #### `m` `_show_skills(self) -> None`  L498
    - 分支数 0，函数体节点数 38
    - 调用: join, _dispatch, SystemMessage
  #### `m` `_show_mcp(self) -> None`  L502
    - 分支数 2，函数体节点数 103；return: None
    - 调用: get, get_mcp_config, _dispatch, SystemMessage, items, join
  #### `m` `_show_memory(self) -> None`  L514
    - 分支数 1，函数体节点数 96；return: None
    - 调用: get_memory, _dispatch, SystemMessage, isinstance, get, len
  #### `m` `_show_usage(self) -> None`  L524
    - 分支数 1，函数体节点数 74；return: None
    - 调用: _dispatch, SystemMessage, join, items
  #### `m` `_show_config(self) -> None`  L532
    - 分支数 0，函数体节点数 32
    - 调用: _dispatch, SystemMessage, getcwd
  #### `m` `_show_uploads(self) -> None`  L537
    - 分支数 3，函数体节点数 118；return: None
    - 调用: _dispatch, SystemMessage, get, list_uploads, join, len
  #### `m` `_send_to_agent(self, text: str) -> None`  L554
    - 分支数 2，函数体节点数 88；return: None
    - 调用: _dispatch, SystemMessage, str, uuid4, UserSubmitted, run_worker, partial
  #### `m` `_stream_worker(self, text: str, thread_id: str) -> None`  L569
    - 分支数 6，函数体节点数 151
    - 调用: getattr, ensure_created, stream_actions, isinstance, call_from_thread, set_title
  - 反射: getattr (L574)
  #### `m` `_on_action(self, action) -> None`  L594
    - 分支数 2，函数体节点数 77
    - 调用: reduce, isinstance, _refresh_transcript, _refresh_status
  #### `m` `_flush_transcript(self) -> None`  L609
    - 分支数 1，函数体节点数 21
    - 调用: _refresh_transcript
  #### `m` `action_interrupt(self) -> None`  L616
    - 分支数 1，函数体节点数 21
    - 调用: _interrupt_run, exit
  #### `m` `action_escape(self) -> None`  L622
    - 分支数 2，函数体节点数 26
    - 调用: _close_palette, _interrupt_run
  #### `m` `_interrupt_run(self) -> None`  L628
    - 分支数 0，函数体节点数 54
    - 调用: cancel_group, reduce, RunEnded, _dispatch, SystemMessage
  #### `m` `action_redraw(self) -> None`  L635
    - 分支数 0，函数体节点数 18
    - 调用: refresh, _refresh_all
  #### `m` `action_clear_composer(self) -> None`  L639
    - 分支数 0，函数体节点数 16
    - 调用: query_one
  #### `m` `_dispatch(self, action) -> None`  L644
    - 分支数 0，函数体节点数 31
    - 调用: reduce, _refresh_transcript, _refresh_status
  #### `m` `_tick_spinner(self) -> None`  L649
    - 分支数 1，函数体节点数 37
    - 调用: len, _refresh_status
  #### `m` `_thread_label(self) -> str`  L654
    - 分支数 1，函数体节点数 26；return: 'new thread', f'thread {self._conv_thread_id[:8]}'
  #### `m` `_refresh_all(self) -> None`  L659
    - 分支数 0，函数体节点数 22
    - 调用: _refresh_header, _refresh_transcript, _refresh_status
  #### `m` `_refresh_header(self) -> None`  L664
    - 分支数 0，函数体节点数 43
    - 调用: update, query_one, render_header, _thread_label, getcwd
  #### `m` `_refresh_transcript(self) -> None`  L676
    - 分支数 0，函数体节点数 37
    - 调用: update, query_one, render_transcript, scroll_end
  #### `m` `_refresh_status(self) -> None`  L680
    - 分支数 0，函数体节点数 57
    - 调用: update, query_one, render_status, _thread_label

## 文件内调用关系
- `SelectScreen.__init__` -> __init__
- `DeerFlowTUI.__init__` -> __init__
- `DeerFlowTUI.on_mount` -> _load_session_info, _refresh_all, _send_to_agent
- `DeerFlowTUI.on_input_submitted` -> _close_palette, _handle_submit
- `DeerFlowTUI.on_input_changed` -> _open_palette, _close_palette
- `DeerFlowTUI.action_nav_up` -> action_palette_up, _history_move
- `DeerFlowTUI.action_nav_down` -> action_palette_down, _history_move
- `DeerFlowTUI._open_palette` -> _close_palette, _render_palette
- `DeerFlowTUI.action_palette_down` -> _render_palette
- `DeerFlowTUI.action_palette_up` -> _render_palette
- `DeerFlowTUI.action_palette_complete` -> _fill_from_palette
- `DeerFlowTUI.action_palette_accept` -> _current_palette_item, _fill_from_palette, _close_palette, _handle_submit
- `DeerFlowTUI._fill_from_palette` -> _current_palette_item, _close_palette
- `DeerFlowTUI._handle_submit` -> _handle_builtin, _dispatch, _send_to_agent
- `DeerFlowTUI._handle_builtin` -> _interrupt_run, _dispatch, _open_model_picker, _open_thread_switcher, _resume_thread, _handle_goal, _show_skills, _show_mcp, _show_memory, _show_usage, _show_config, _show_uploads
- `DeerFlowTUI._open_model_picker` -> _dispatch, _refresh_header
- `DeerFlowTUI._open_thread_switcher` -> _dispatch, _switch_to_thread
- `DeerFlowTUI._resume_thread` -> _open_thread_switcher, _switch_to_thread
- `DeerFlowTUI._switch_to_thread` -> _dispatch, _refresh_header
- `DeerFlowTUI._handle_goal` -> _dispatch, _refresh_header
- `DeerFlowTUI._show_skills` -> _dispatch
- `DeerFlowTUI._show_mcp` -> _dispatch
- `DeerFlowTUI._show_memory` -> _dispatch
- `DeerFlowTUI._show_usage` -> _dispatch
- `DeerFlowTUI._show_config` -> _dispatch
- `DeerFlowTUI._show_uploads` -> _dispatch
- `DeerFlowTUI._send_to_agent` -> _dispatch
- `DeerFlowTUI._on_action` -> _refresh_transcript, _refresh_status
- `DeerFlowTUI._flush_transcript` -> _refresh_transcript
- `DeerFlowTUI.action_interrupt` -> _interrupt_run
- `DeerFlowTUI.action_escape` -> _close_palette, _interrupt_run
- `DeerFlowTUI._interrupt_run` -> _dispatch
- `DeerFlowTUI.action_redraw` -> _refresh_all
- `DeerFlowTUI._dispatch` -> _refresh_transcript, _refresh_status
- `DeerFlowTUI._tick_spinner` -> _refresh_status
- `DeerFlowTUI._refresh_all` -> _refresh_header, _refresh_transcript, _refresh_status
- `DeerFlowTUI._refresh_header` -> _thread_label
- `DeerFlowTUI._refresh_status` -> _thread_label

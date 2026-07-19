# `backend/packages/harness/deerflow/agents/middlewares/delegation_ledger.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/delegation_ledger.py`  ·  行数: 198

**模块文档首行**（仅供参考）: Deterministic capture and rendering for task delegations.

## 模块概览
- 函数 11 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: hashlib
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `html` -> escape
- `typing` -> Any
- `langchain_core.messages` -> AIMessage, AnyMessage, ToolMessage
- `deerflow.agents.thread_state` -> DelegationEntry
- `deerflow.subagents.status_contract` -> read_subagent_result_metadata

## 模块级常量
- `_RESULT_BRIEF_CAP` = 2000
- `_DESCRIPTION_CAP` = 200
- `_LEDGER_RENDER_CHAR_BUDGET` = 6000
- `_LEDGER_ENTRY_RESULT_RENDER_CAP` = 120
- `_STATUS_ONLY_RESULT_BRIEFS` = {'failed': 'Task failed.', 'cancelled': 'Task cancelled b...

## 函数
#### `ƒ` `_utc_now_iso() -> str`  L29
  - 分支数 0，函数体节点数 20；return: datetime.now(UTC).isoformat().replace('+00:00', 'Z')
  - 调用: replace, isoformat, now
  - 文件IO: replace (L30)

#### `ƒ` `_bound_text(text: str, cap: int) -> str`  L33
  - _文档首行_（仅供参考）: Deterministic head/tail truncation. This is not an LLM summary.
  - 分支数 4，函数体节点数 121；return: text, '', text[:cap], f'{text[:head]}{omitted_marker}{text[-tail:]}'
  - 调用: len

#### `ƒ` `_escape_context_text(value: object) -> str`  L49
  - 分支数 0，函数体节点数 25；return: escape(' '.join(str(value).split()), quote=False)
  - 调用: escape, join, split, str

#### `ƒ` `_status_guidance(status: str, stop_reason: str | None) -> str`  L53
  - 分支数 8，函数体节点数 77；return: 'hit a guardrail cap with a partial result; reuse the partial result, retry with a tighter scope, or raise the per-agent budget (max_turns / token_budget)', 'hit a guardrail cap with no usable result; retry with a tighter scope or raise the per-agent budget (max_turns / token_budget)', 'already delegated; do NOT delegate again; wait for or build on the result', 'completed result; do NOT delegate again; reuse this result', 'failed attempt; may retry with a changed plan', 'cancelled attempt; may retry with a changed plan', 'timed-out attempt; may retry with a changed plan', 'polling timed-out attempt; may retry with a changed plan', 'prior attempt; inspect status before retrying'

#### `ƒ` `_tool_call_name(tool_call: dict[str, Any]) -> str`  L78
  - 分支数 2，函数体节点数 73；return: name, function['name'], ''
  - 调用: get, isinstance

#### `ƒ` `_tool_call_id(tool_call: dict[str, Any]) -> str | None`  L88
  - 分支数 0，函数体节点数 37；return: str(tool_call_id) if tool_call_id else None
  - 调用: get, str

#### `ƒ` `_tool_call_args(tool_call: dict[str, Any]) -> dict[str, Any]`  L93
  - 分支数 0，函数体节点数 44；return: args if isinstance(args, dict) else {}
  - 调用: get, isinstance

#### `ƒ` `extract_delegations(messages: list[AnyMessage]) -> list[DelegationEntry]`  L98
  - _文档首行_（仅供参考）: Enumerate `task` delegations from AI tool calls and paired results.
  - 分支数 12，函数体节点数 374；return: [entries_by_id[tool_call_id] for tool_call_id in order]
  - 调用: _utc_now_iso, isinstance, _tool_call_name, _tool_call_id, _tool_call_args, str, get, append, read_subagent_result_metadata, hexdigest, sha256, encode, update, _bound_text

#### `ƒ` `_fits_budget(lines: list[str], candidate: str, max_chars: int) -> bool`  L151
  - 分支数 0，函数体节点数 37；return: len('\n'.join([*lines, candidate])) <= max_chars
  - 调用: len, join

#### `ƒ` `_render_entry_line(entry: DelegationEntry) -> str`  L155
  - 分支数 1，函数体节点数 110；return: line
  - 调用: _escape_context_text, _status_guidance, get, _bound_text

#### `ƒ` `render_delegation_ledger(entries: list[DelegationEntry], *, max_chars: int) -> str`  L167
  - _文档首行_（仅供参考）: Render the delegation ledger as model-visible system context.
  - 分支数 7，函数体节点数 203；return: '', rendered, rendered[:max(0, max_chars - 4)] + '\n...'
  - 调用: enumerate, reversed, _render_entry_line, _fits_budget, append, len, pop, join, max

## 文件内调用关系
- `extract_delegations` -> _utc_now_iso, _tool_call_name, _tool_call_id, _tool_call_args, _bound_text
- `_render_entry_line` -> _escape_context_text, _status_guidance, _bound_text
- `render_delegation_ledger` -> _render_entry_line, _fits_budget

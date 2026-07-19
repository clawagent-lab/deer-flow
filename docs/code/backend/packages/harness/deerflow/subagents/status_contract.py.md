# `backend/packages/harness/deerflow/subagents/status_contract.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/subagents/status_contract.py`  ·  行数: 287

**模块文档首行**（仅供参考）: Backend↔frontend contract for structured subagent result metadata.

## 模块概览
- 函数 5 个，类 1 个，模块级常量 16 个

## 依赖（import）
- 模块: hashlib, re
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Any, Literal, NotRequired, TypedDict

## 模块级常量
- `SUBAGENT_STATUS_KEY` = 'subagent_status'
- `SUBAGENT_STOP_REASON_KEY` = 'subagent_stop_reason'
- `SUBAGENT_ERROR_KEY` = 'subagent_error'
- `SUBAGENT_RESULT_BRIEF_KEY` = 'subagent_result_brief'
- `SUBAGENT_RESULT_SHA256_KEY` = 'subagent_result_sha256'
- `SUBAGENT_MODEL_NAME_KEY` = 'subagent_model_name'
- `SUBAGENT_TOKEN_USAGE_KEY` = 'subagent_token_usage'
- `SUBAGENT_METADATA_TEXT_MAX_CHARS` = 2000
- `_SHA256_HEX_RE` = re.compile('[0-9a-f]{64}')
- `SubagentStatusValue` = Literal['completed', 'failed', 'cancelled', 'timed_out', ...
- `SUBAGENT_STATUS_VALUES` = ('completed', 'failed', 'cancelled', 'timed_out', 'pollin...
- `SubagentStopReasonValue` = Literal['token_capped', 'turn_capped', 'loop_capped']
- `SUBAGENT_STOP_REASON_VALUES` = ('token_capped', 'turn_capped', 'loop_capped')
- `_STOP_REASON_LABELS` = {'token_capped': 'token budget', 'turn_capped': 'turn bud...
- `_RESULT_BEARING_STATUSES` = frozenset({'completed'})
- `_LEGACY_STATUS_NORMALIZATION` = {'max_turns_reached': 'turn_capped'}

## 函数
#### `ƒ` `_bound_metadata_text(text: str, cap: int) -> str`  L116
  - 分支数 3，函数体节点数 119；return: cleaned, cleaned[:cap], f'{cleaned[:head]}{marker}{cleaned[-tail:]}'
  - 调用: strip, len

#### `ƒ` `make_subagent_additional_kwargs(status: SubagentStatusValue, *, result: str | None, error: str | None, stop_reason: SubagentStopReasonValue | None, model_name: str | None, token_usage: Mapping[str, object] | None) -> dict[str, object]`  L130
  - _文档首行_（仅供参考）: Build the ``additional_kwargs`` payload the middleware stamps.
  - 分支数 7，函数体节点数 279；raise: ValueError(f'invalid subagent status {status!r}; expected one of {SUBAGENT_STATUS_VALUES}'), ValueError(f'invalid subagent stop_reason {stop_reason!r}; expected one of {SUBAGENT_STOP_REASON_VALUES}')；return: payload
  - 调用: ValueError, isinstance, strip, _bound_metadata_text, hexdigest, sha256, encode, normalize_token_usage

#### `ƒ` `normalize_token_usage(value: Any) -> dict[str, int] | None`  L174
  - _文档首行_（仅供参考）: Validate a cumulative token-usage mapping into the contract shape.
  - 分支数 3，函数体节点数 102；return: None, normalized
  - 调用: isinstance, get

#### `ƒ` `format_subagent_result_message(status: SubagentStatusValue, *, result: str | None, error: str | None, stop_reason: SubagentStopReasonValue | None) -> tuple[str, str | None]`  L196
  - _文档首行_（仅供参考）: Return model-visible task content plus normalized metadata error.
  - 分支数 10，函数体节点数 284；return: (f'Task Succeeded (capped: {capped}). Result: {result_text}', None), (f'Task Succeeded. Result: {result_text}', None), (detail, detail), (f'Task cancelled by user. Error: {detail}', detail), (f'Task timed out. Error: {detail}', detail), (f'Task failed (capped: {capped}).', detail), (f'Task failed (capped: {capped}). Error: {detail}', detail), (f'Task failed. Error: {detail}', detail)
  - 调用: str, isinstance, strip, get

#### `ƒ` `read_subagent_result_metadata(additional_kwargs: Mapping[str, object] | None) -> StructuredSubagentResult | None`  L249
  - 分支数 8，函数体节点数 285；return: None, payload
  - 调用: get, isinstance, strip, _bound_metadata_text, fullmatch

## 类
### 类 `StructuredSubagentResult`  L108
- 继承: TypedDict
- 类/实例变量:
  - `status` = <annotated>
  - `stop_reason` = <annotated>
  - `result_brief` = <annotated>
  - `result_sha256` = <annotated>
  - `error` = <annotated>

## 文件内调用关系
- `make_subagent_additional_kwargs` -> _bound_metadata_text, normalize_token_usage
- `read_subagent_result_metadata` -> _bound_metadata_text

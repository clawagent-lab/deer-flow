# `backend/packages/harness/deerflow/subagents/step_events.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/subagents/step_events.py`  ·  行数: 255

**模块文档首行**（仅供参考）: Build compact subagent step payloads for streaming + persistence.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 3 个

## 依赖（import）
- 模块: json
- `__future__` -> annotations
- `typing` -> Any
- `langchain_core.messages` -> AIMessage, BaseMessage, ToolMessage
- `deerflow.utils.messages` -> message_content_to_text
- `.status_contract` -> normalize_token_usage

## 模块级常量
- `SUBAGENT_STEP_MAX_CHARS` = 8192
- `SUBAGENT_EVENT_CATEGORY` = 'subagent'
- `_TERMINAL_EVENT_STATUS` = {'task_completed': 'completed', 'task_failed': 'failed', ...

## 函数
#### `ƒ` `capture_step_message(message: BaseMessage, captured: list[dict[str, Any]], seen_ids: set[str]) -> bool`  L50
  - _文档首行_（仅供参考）: Append ``message.model_dump()`` to ``captured`` if it is a new step.
  - 分支数 5，函数体节点数 106；return: False, True
  - 调用: isinstance, model_dump, get, append, add

#### `ƒ` `capture_new_step_messages(messages: list[BaseMessage], captured: list[dict[str, Any]], seen_ids: set[str], processed_count: int) -> int`  L82
  - _文档首行_（仅供参考）: Capture every step message appended since ``processed_count`` (#3779).
  - 分支数 4，函数体节点数 116；return: total, max(processed_count, total)
  - 调用: len, capture_step_message, max

#### `ƒ` `truncate_step_text(text: str, max_chars: int) -> tuple[str, bool]`  L130
  - _文档首行_（仅供参考）: Return ``(text, truncated)``, clipping to ``max_chars`` when longer.
  - 分支数 1，函数体节点数 54；return: (text[:max_chars], True), (text, False)
  - 调用: len

#### `ƒ` `_bounded_tool_call(call: dict[str, Any], max_chars: int) -> dict[str, Any]`  L137
  - _文档首行_（仅供参考）: Return ``{name, args}`` for a captured tool call, capping large args (#3779).
  - 分支数 1，函数体节点数 111；return: {'name': name, 'args': serialized[:max_chars], 'args_truncated': True}, {'name': name, 'args': args}
  - 调用: get, isinstance, dumps, len

#### `ƒ` `build_subagent_step(message: dict[str, Any], *, task_id: str, message_index: int, max_chars: int) -> dict[str, Any]`  L155
  - _文档首行_（仅供参考）: Build the compact step payload from a captured subagent message dict.
  - 分支数 1，函数体节点数 152；return: step
  - 调用: get, truncate_step_text, message_content_to_text, _bounded_tool_call

#### `ƒ` `subagent_run_event(chunk: Any) -> dict[str, Any] | None`  L191
  - _文档首行_（仅供参考）: Map a ``task_*`` custom stream chunk to ``RunEventStore.put`` kwargs.
  - 分支数 11，函数体节点数 361；return: None, {'event_type': 'subagent.start', 'category': SUBAGENT_EVENT_CATEGORY, 'content': {'task_id': task_id, 'description': chunk.get('description')}, 'metadata': {'task_id': task_id}}, {'event_type': 'subagent.step', 'category': SUBAGENT_EVENT_CATEGORY, 'content': build_subagent_step(chunk.get('message') or {}, task_id=task_id, message_index=message_index), 'metadata': {'task_id': task_id, 'message_index': message_index}}, {'event_type': 'subagent.end', 'category': SUBAGENT_EVENT_CATEGORY, 'content': content, 'metadata': {'task_id': task_id}}
  - 调用: isinstance, get, startswith, build_subagent_step, strip, normalize_token_usage, truncate_step_text, str

## 文件内调用关系
- `capture_new_step_messages` -> capture_step_message
- `build_subagent_step` -> truncate_step_text, _bounded_tool_call
- `subagent_run_event` -> build_subagent_step, truncate_step_text

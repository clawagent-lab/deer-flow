# `backend/packages/harness/deerflow/agents/middlewares/sandbox_audit_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/sandbox_audit_middleware.py`  ·  行数: 365

**模块文档首行**（仅供参考）: SandboxAuditMiddleware - bash command security auditing.

## 模块概览
- 函数 3 个，类 1 个，模块级常量 3 个

## 依赖（import）
- 模块: json, logging, re, shlex
- `collections.abc` -> Awaitable, Callable
- `datetime` -> UTC, datetime
- `typing` -> override
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> ToolMessage
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command
- `deerflow.agents.thread_state` -> ThreadState

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_HIGH_RISK_PATTERNS` = [re.compile('rm\\s+-[^\\s]*r[^\\s]*\\s+(/\\*?|~/?\\*?|/ho...
- `_MEDIUM_RISK_PATTERNS` = [re.compile('chmod\\s+777'), re.compile('pip3?\\s+install...

## 函数
#### `ƒ` `_split_compound_command(command: str) -> list[str]`  L64
  - _文档首行_（仅供参考）: Split a compound command into sub-commands (quote-aware).
  - 分支数 12，函数体节点数 351；return: [command], parts if parts else [command]
  - 调用: len, append, startswith, strip, join

#### `ƒ` `_classify_single_command(command: str) -> str`  L137
  - _文档首行_（仅供参考）: Classify a single (non-compound) command. Return 'block', 'warn', or 'pass'.
  - 分支数 7，函数体节点数 92；return: 'block', 'warn', 'pass'
  - 调用: join, split, search

#### `ƒ` `_classify_command(command: str) -> str`  L164
  - _文档首行_（仅供参考）: Return 'block', 'warn', or 'pass'.
  - 分支数 5，函数体节点数 82；return: 'block', worst
  - 调用: join, split, search, _split_compound_command, _classify_single_command

## 类
### 类 `SandboxAuditMiddleware`  L198
- 继承: AgentMiddleware[ThreadState]
- _文档首行_: Bash command security auditing middleware.
- 类/实例变量:
  - `state_schema` = ThreadState
  - `_AUDIT_COMMAND_LIMIT` = 200
  - `_MAX_COMMAND_LENGTH` = 10000
- 方法:
  #### `m` `_get_thread_id(self, request: ToolCallRequest) -> str | None`  L221
    - 分支数 2，函数体节点数 93；return: None, thread_id
    - 调用: getattr, isinstance, get
  - 反射: getattr (L225), getattr (L228)
  #### `m` `_write_audit(self, thread_id: str | None, command: str, verdict: str, *, truncate: bool) -> None`  L234
    - 分支数 1，函数体节点数 106
    - 调用: len, isoformat, now, info, dumps
  #### `m` `_build_block_message(self, request: ToolCallRequest, reason: str) -> ToolMessage`  L246
    - 分支数 0，函数体节点数 46；return: ToolMessage(content=f'Command blocked: {reason}. Please use a safer alternative approach.', tool_call_id=tool_call_id, name='bash', status='error')
    - 调用: str, get, ToolMessage
  #### `m` `_append_warn_to_result(self, result: ToolMessage | Command, command: str) -> ToolMessage | Command`  L255
    - _文档首行_（仅供参考）: Append a warning note to the tool result for medium-risk commands.
    - 分支数 2，函数体节点数 109；return: result, ToolMessage(content=new_content, tool_call_id=result.tool_call_id, name=result.name, status=result.status)
    - 调用: isinstance, list, str, ToolMessage
  #### `m` `_validate_input(self, command: str) -> str | None`  L281
    - _文档首行_（仅供参考）: Return ``None`` if *command* is acceptable, else a rejection reason.
    - 分支数 3，函数体节点数 47；return: 'empty command', 'command too long', 'null byte detected', None
    - 调用: strip, len
  #### `m` `_pre_process(self, request: ToolCallRequest) -> tuple[str, str | None, str, str | None]`  L295
    - _文档首行_（仅供参考）: Returns (command, thread_id, verdict, reject_reason).
    - 分支数 3，函数体节点数 184；return: (command, thread_id, 'block', reject_reason), (command, thread_id, verdict, None)
    - 调用: get, isinstance, _get_thread_id, _validate_input, _write_audit, warning, _classify_command
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L331
    - 分支数 3，函数体节点数 120；return: handler(request), self._build_block_message(request, reason), result
    - 调用: get, handler, _pre_process, _build_block_message, _append_warn_to_result
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L349
    - 分支数 3，函数体节点数 126；return: await handler(request), self._build_block_message(request, reason), result
    - 调用: get, handler, _pre_process, _build_block_message, _append_warn_to_result

## 文件内调用关系
- `_classify_command` -> _split_compound_command, _classify_single_command
- `SandboxAuditMiddleware._pre_process` -> _get_thread_id, _validate_input, _write_audit, _classify_command
- `SandboxAuditMiddleware.wrap_tool_call` -> _pre_process, _build_block_message, _append_warn_to_result
- `SandboxAuditMiddleware.awrap_tool_call` -> _pre_process, _build_block_message, _append_warn_to_result

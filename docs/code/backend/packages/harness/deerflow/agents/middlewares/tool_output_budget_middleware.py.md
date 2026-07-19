# `backend/packages/harness/deerflow/agents/middlewares/tool_output_budget_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/tool_output_budget_middleware.py`  ·  行数: 652

**模块文档首行**（仅供参考）: Middleware that enforces a per-result budget on tool outputs.

## 模块概览
- 函数 19 个，类 1 个，模块级常量 3 个

## 依赖（import）
- 模块: asyncio, logging, os, shlex, uuid
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `dataclasses` -> dc_replace
- `typing` -> TYPE_CHECKING, Any, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelCallResult, ModelRequest, ModelResponse
- `langchain_core.messages` -> ToolMessage
- `langgraph.prebuilt.tool_node` -> ToolCallRequest
- `langgraph.types` -> Command
- `deerflow.agents.middlewares.tool_output_synopsis` -> render_tool_output_preview
- `deerflow.config.tool_output_config` -> ToolOutputConfig
- `deerflow.sandbox.sandbox_provider` -> get_sandbox_provider

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_VIRTUAL_OUTPUTS_BASE` = '/mnt/user-data/outputs'
- `_EXT_MAP` = {'bash': 'log', 'bash_tool': 'log', 'web_fetch': 'log'}

## 函数
#### `ƒ` `_default_config() -> ToolOutputConfig`  L43
  - 分支数 0，函数体节点数 8；return: ToolOutputConfig()
  - 调用: ToolOutputConfig

#### `ƒ` `_message_text(content: Any) -> str | None`  L52
  - _文档首行_（仅供参考）: Extract a plain-text representation from a ToolMessage content field.
  - 分支数 6，函数体节点数 118；return: content, None, '\n'.join(pieces) if pieces else None
  - 调用: isinstance, append, get, join

#### `ƒ` `_snap_to_line_boundary(text: str, pos: int) -> int`  L75
  - _文档首行_（仅供参考）: Return *pos* or the nearest preceding newline+1, whichever is closer.
  - 分支数 2，函数体节点数 68；return: pos, nl + 1
  - 调用: len, rfind

#### `ƒ` `_snap_start_to_line_boundary(text: str, pos: int) -> int`  L94
  - _文档首行_（仅供参考）: Return *pos* or the nearest following newline+1, whichever is closer.
  - 分支数 2，函数体节点数 79；return: pos, nl + 1
  - 调用: len, find

#### `ƒ` `_sanitize_tool_name(name: str) -> str`  L122
  - _文档首行_（仅供参考）: Strip path separators and traversal components from a tool name.
  - 分支数 0，函数体节点数 47；return: safe or 'unknown'
  - 调用: basename, replace
  - 文件IO: replace (L125), replace (L125), replace (L125)

#### `ƒ` `_build_externalized_filename(*, tool_name: str, tool_call_id: str) -> str`  L129
  - _文档首行_（仅供参考）: Build the on-disk filename for an externalized tool output.
  - 分支数 0，函数体节点数 58；return: f'{safe_name}-{short_id}.{ext}'
  - 调用: _sanitize_tool_name, get, uuid4

#### `ƒ` `_externalize(content: str, *, tool_name: str, tool_call_id: str, outputs_path: str, storage_subdir: str) -> str | None`  L141
  - _文档首行_（仅供参考）: Write *content* to disk and return the virtual path, or ``None`` on failure.
  - 分支数 5，函数体节点数 164；return: None, f'{_VIRTUAL_OUTPUTS_BASE}/{storage_subdir}/{filename}'
  - 调用: isabs, join, makedirs, _build_externalized_filename, startswith, abspath, open, write
  - 文件IO: open (L165), write (L166)

#### `ƒ` `_externalize_to_sandbox(content: str, *, tool_name: str, tool_call_id: str, storage_subdir: str, sandbox: Sandbox) -> str | None`  L173
  - _文档首行_（仅供参考）: Write *content* into the sandbox filesystem and return the virtual path.
  - 分支数 3，函数体节点数 175；return: None, virtual_path
  - 调用: isabs, _build_externalized_filename, execute_command, quote, write_file, isinstance, strip, warning, exception

#### `ƒ` `_build_preview(content: str, *, tool_name: str, virtual_path: str, head_chars: int, tail_chars: int) -> str`  L227
  - _文档首行_（仅供参考）: Build a typed synopsis preview with a file reference for externalized output.
  - 分支数 0，函数体节点数 39；return: render_tool_output_preview(content, tool_name=tool_name, virtual_path=virtual_path, head_chars=head_chars, tail_chars=tail_chars)
  - 调用: render_tool_output_preview

#### `ƒ` `_build_fallback(content: str, *, tool_name: str, max_chars: int, head_chars: int, tail_chars: int) -> str`  L245
  - _文档首行_（仅供参考）: Build a head+tail truncation when disk persistence is unavailable.
  - 分支数 3，函数体节点数 241；return: content, content[:max_chars], ''.join(parts)
  - 调用: len, format, min, max, _snap_to_line_boundary, _snap_start_to_line_boundary, append, join

#### `ƒ` `_resolve_outputs_path(request: ToolCallRequest) -> str | None`  L291
  - _文档首行_（仅供参考）: Best-effort extraction of the thread outputs path.
  - 分支数 3，函数体节点数 90；return: None, outputs_path if isinstance(outputs_path, str) else None
  - 调用: getattr, get, isinstance
  - 反射: getattr (L293), getattr (L296)

#### `ƒ` `_resolve_sandbox(request: ToolCallRequest) -> Sandbox | None`  L306
  - _文档首行_（仅供参考）: Resolve the active sandbox for the current tool call, or ``None``.
  - 分支数 4，函数体节点数 105；return: None, get_sandbox_provider().get(sandbox_id)
  - 调用: getattr, isinstance, get, get_sandbox_provider, exception
  - 反射: getattr (L316), getattr (L317)

#### `ƒ` `_budget_content(content: str, *, tool_name: str, tool_call_id: str, outputs_path: str | None, config: ToolOutputConfig, sandbox: Sandbox | None) -> str | None`  L333
  - _文档首行_（仅供参考）: Apply budget to *content*. Returns ``None`` if no change needed.
  - 分支数 10，函数体节点数 341；return: None, _build_preview(content, tool_name=tool_name, virtual_path=virtual_path, head_chars=config.preview_head_chars, tail_chars=config.preview_tail_chars), _build_fallback(content, tool_name=tool_name, max_chars=config.fallback_max_chars, head_chars=config.fallback_head_chars, tail_chars=config.fallback_tail_chars)
  - 调用: get, len, get_sandbox_provider, exception, getattr, _externalize, _externalize_to_sandbox, info, _build_preview, warning, _build_fallback
  - 反射: getattr (L362)

#### `ƒ` `_patch_tool_message(msg: ToolMessage, config: ToolOutputConfig, outputs_path: str | None, sandbox: Sandbox | None) -> ToolMessage`  L431
  - _文档首行_（仅供参考）: Apply budget to a single ToolMessage. Returns the original if unchanged.
  - 分支数 5，函数体节点数 171；return: msg, msg.model_copy(update=update)
  - 调用: _message_text, _budget_content, getattr, dict, model_copy
  - 反射: getattr (L458), getattr (L460)

#### `ƒ` `_effective_trigger(tool_name: str, config: ToolOutputConfig) -> int`  L465
  - _文档首行_（仅供参考）: Smallest content length that could trigger budgeting for *tool_name*.
  - 分支数 2，函数体节点数 83；return: min(candidates) if candidates else -1
  - 调用: get, append, min

#### `ƒ` `_tool_message_over_budget(msg: ToolMessage, config: ToolOutputConfig) -> bool`  L481
  - _文档首行_（仅供参考）: Cheap, per-tool-aware check: is this ToolMessage non-exempt and over its trigger?
  - 分支数 2，函数体节点数 78；return: False, text is not None and len(text) > trigger
  - 调用: _effective_trigger, _message_text, len

#### `ƒ` `_needs_budget(result: ToolMessage | Command, config: ToolOutputConfig) -> bool`  L492
  - _文档首行_（仅供参考）: Fast check whether *result* could need budgeting (avoids thread offload for small outputs).
  - 分支数 4，函数体节点数 82；return: _tool_message_over_budget(result, config), True, False
  - 调用: isinstance, _tool_message_over_budget, getattr, get
  - 反射: getattr (L496)

#### `ƒ` `_patch_result(result: ToolMessage | Command, config: ToolOutputConfig, outputs_path: str | None, sandbox: Sandbox | None) -> ToolMessage | Command`  L504
  - _文档首行_（仅供参考）: Apply budget to a tool call result (ToolMessage or Command).
  - 分支数 7，函数体节点数 188；return: _patch_tool_message(result, config, outputs_path, sandbox), result, dc_replace(result, update={**update, 'messages': new_messages})
  - 调用: isinstance, _patch_tool_message, getattr, get, append, dc_replace
  - 反射: getattr (L514)

#### `ƒ` `_patch_model_messages(messages: list[Any], config: ToolOutputConfig) -> list[Any] | None`  L539
  - _文档首行_（仅供参考）: Apply budget to historical ToolMessages in a model request. Returns ``None`` if unchanged.
  - 分支数 4，函数体节点数 127；return: None, updated if changed else None
  - 调用: any, isinstance, _tool_message_over_budget, _patch_tool_message, append

## 类
### 类 `ToolOutputBudgetMiddleware`  L573
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Enforce per-result budget on tool outputs via externalization or truncation.
- 方法:
  #### `cls` `from_app_config(cls, app_config: Any) -> ToolOutputBudgetMiddleware`    @classmethod  L581
    - 分支数 1，函数体节点数 39；return: cls(config=tool_output), cls()
    - 调用: getattr, isinstance, cls
  - 反射: getattr (L582)
  #### `m` `__init__(self, config: ToolOutputConfig | None) -> None`  L576
    - 分支数 0，函数体节点数 34
    - 调用: __init__, super, _default_config
  #### `m` `wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage | Command]) -> ToolMessage | Command`    @override  L590
    - 分支数 2，函数体节点数 96；return: result, _patch_result(result, self._config, outputs_path, sandbox)
    - 调用: handler, _needs_budget, _resolve_outputs_path, _resolve_sandbox, _patch_result
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelCallResult`    @override  L626
    - 分支数 3，函数体节点数 83；return: handler(request)
    - 调用: getattr, isinstance, _patch_model_messages, override, handler
  - 反射: getattr (L632)
  #### `⏵m` `async awrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]]) -> ToolMessage | Command`    @override  L605
    - 分支数 2，函数体节点数 106；return: result, await asyncio.to_thread(_patch_result, result, self._config, outputs_path, sandbox)
    - 调用: handler, _needs_budget, _resolve_outputs_path, _resolve_sandbox, to_thread
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelCallResult`    @override  L640
    - 分支数 3，函数体节点数 88；return: await handler(request)
    - 调用: getattr, isinstance, _patch_model_messages, override, handler
  - 反射: getattr (L646)

## 文件内调用关系
- `_build_externalized_filename` -> _sanitize_tool_name
- `_externalize` -> _build_externalized_filename
- `_externalize_to_sandbox` -> _build_externalized_filename
- `_build_fallback` -> _snap_to_line_boundary, _snap_start_to_line_boundary
- `_budget_content` -> _externalize, _externalize_to_sandbox, _build_preview, _build_fallback
- `_patch_tool_message` -> _message_text, _budget_content
- `_tool_message_over_budget` -> _effective_trigger, _message_text
- `_needs_budget` -> _tool_message_over_budget
- `_patch_result` -> _patch_tool_message
- `_patch_model_messages` -> _tool_message_over_budget, _patch_tool_message
- `ToolOutputBudgetMiddleware.__init__` -> __init__, _default_config
- `ToolOutputBudgetMiddleware.wrap_tool_call` -> _needs_budget, _resolve_outputs_path, _resolve_sandbox, _patch_result
- `ToolOutputBudgetMiddleware.awrap_tool_call` -> _needs_budget, _resolve_outputs_path, _resolve_sandbox
- `ToolOutputBudgetMiddleware.wrap_model_call` -> _patch_model_messages
- `ToolOutputBudgetMiddleware.awrap_model_call` -> _patch_model_messages

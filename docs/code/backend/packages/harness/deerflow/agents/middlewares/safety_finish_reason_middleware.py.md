# `backend/packages/harness/deerflow/agents/middlewares/safety_finish_reason_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/safety_finish_reason_middleware.py`  ·  行数: 323

**模块文档首行**（仅供参考）: Suppress tool execution when the provider safety-terminated the response.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `typing` -> TYPE_CHECKING, override
- `langchain.agents` -> AgentState
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> AIMessage
- `langgraph.runtime` -> Runtime
- `deerflow.agents.middlewares.safety_termination_detectors` -> SafetyTermination, SafetyTerminationDetector, default_detectors
- `deerflow.agents.middlewares.tool_call_metadata` -> clone_ai_message_with_tool_calls

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_USER_FACING_MESSAGE` = 'The model provider stopped this response with a safety-r...

## 类
### 类 `SafetyFinishReasonMiddleware`  L67
- 继承: AgentMiddleware[AgentState]
- _文档首行_: Strip tool_calls from AIMessages flagged by a SafetyTerminationDetector.
- 方法:
  #### `cls` `from_config(cls, config: SafetyFinishReasonConfig) -> SafetyFinishReasonMiddleware`    @classmethod  L76
    - _文档首行_（仅供参考）: Construct from validated Pydantic config, honouring the
    - 分支数 4，函数体节点数 136；raise: ValueError('safety_finish_reason.detectors must be omitted (use built-ins) or contain at least one entry; use enabled=false to disable the middleware entirely.'), TypeError(f'{entry.use} did not produce a SafetyTerminationDetector (got {type(detector).__name__}); ensure it has a `name` attribute and a `detect(message)` method')；return: cls(), cls(detectors=detectors)
    - 调用: cls, ValueError, resolve_variable, dict, detector_cls, isinstance, TypeError, type, append
  #### `st` `_append_user_message(content: object, text: str) -> str | list`    @staticmethod  L118
    - _文档首行_（仅供参考）: Append a plain-text explanation to AIMessage content.
    - 分支数 3，函数体节点数 89；return: text, [*content, {'type': 'text', 'text': f'\n\n{text}'}], content + f'\n\n{text}', str(content) + f'\n\n{text}'
    - 调用: isinstance, str
  #### `m` `__init__(self, detectors: list[SafetyTerminationDetector] | None) -> None`  L70
    - 分支数 0，函数体节点数 44
    - 调用: __init__, super, list, default_detectors
  #### `m` `_detect(self, message: AIMessage) -> SafetyTermination | None`  L104
    - 分支数 3，函数体节点数 64；return: hit, None
    - 调用: detect, exception, getattr, type
  - 反射: getattr (L109)
  #### `m` `_build_suppressed_message(self, message: AIMessage, termination: SafetyTermination) -> AIMessage`  L133
    - 分支数 0，函数体节点数 157；return: cleared.model_copy(update={'additional_kwargs': kwargs})
    - 调用: get, format, _append_user_message, clone_ai_message_with_tool_calls, dict, getattr, len, model_copy
  - 反射: getattr (L157)
  #### `m` `_emit_event(self, termination: SafetyTermination, suppressed_names: list[str], runtime: Runtime) -> None`  L170
    - _文档首行_（仅供参考）: Notify SSE consumers (e.g. the web UI) that a tool turn was
    - 分支数 3，函数体节点数 129；return: None
    - 调用: get_stream_writer, debug, getattr, isinstance, get, writer, len
  - 反射: getattr (L189)
  #### `m` `_record_audit_event(self, termination: SafetyTermination, message, tool_calls: list[dict], runtime: Runtime) -> None`  L207
    - _文档首行_（仅供参考）: Write a ``middleware:safety_termination`` record to RunEventStore
    - 分支数 4，函数体节点数 198；return: None
    - 调用: getattr, isinstance, get, len, dict, record_middleware, type, debug
  - 反射: getattr (L231), getattr (L248)
  #### `m` `_apply(self, state: AgentState, runtime: Runtime) -> dict | None`  L266
    - 分支数 6，函数体节点数 258；return: None, {'messages': [patched]}
    - 调用: get, isinstance, _detect, getattr, _build_suppressed_message, warning, len, _emit_event, _record_audit_event, list
  - 反射: getattr (L288), getattr (L294)
  #### `m` `after_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L317
    - 分支数 0，函数体节点数 26；return: self._apply(state, runtime)
    - 调用: _apply
  #### `⏵m` `async aafter_model(self, state: AgentState, runtime: Runtime) -> dict | None`    @override  L321
    - 分支数 0，函数体节点数 26；return: self._apply(state, runtime)
    - 调用: _apply

## 文件内调用关系
- `SafetyFinishReasonMiddleware.__init__` -> __init__
- `SafetyFinishReasonMiddleware._build_suppressed_message` -> _append_user_message
- `SafetyFinishReasonMiddleware._apply` -> _detect, _build_suppressed_message, _emit_event, _record_audit_event
- `SafetyFinishReasonMiddleware.after_model` -> _apply
- `SafetyFinishReasonMiddleware.aafter_model` -> _apply

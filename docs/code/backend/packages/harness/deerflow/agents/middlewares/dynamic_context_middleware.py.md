# `backend/packages/harness/deerflow/agents/middlewares/dynamic_context_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/dynamic_context_middleware.py`  ·  行数: 366

**模块文档首行**（仅供参考）: Middleware to inject dynamic context (memory, current date) as a system-reminder.

## 模块概览
- 函数 4 个，类 1 个，模块级常量 6 个

## 依赖（import）
- 模块: asyncio, hashlib, logging, re, uuid
- `__future__` -> annotations
- `datetime` -> datetime
- `typing` -> TYPE_CHECKING, override
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> HumanMessage, SystemMessage
- `langgraph.runtime` -> Runtime
- `deerflow.runtime.context_keys` -> CURRENT_RUN_PRE_EXISTING_MESSAGE_IDS_KEY

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_INJECT_TIMEOUT_SECONDS` = 5.0
- `_DATE_RE` = re.compile('<current_date>([^<]+)</current_date>')
- `_DYNAMIC_CONTEXT_REMINDER_KEY` = 'dynamic_context_reminder'
- `_REMINDER_DATE_KEY` = 'reminder_date'
- `_SUMMARY_MESSAGE_NAME` = 'summary'

## 函数
#### `ƒ` `_extract_date(content: str) -> str | None`  L65
  - _文档首行_（仅供参考）: Return the first <current_date> value found in *content*, or None.
  - 分支数 0，函数体节点数 33；return: m.group(1) if m else None
  - 调用: search, group

#### `ƒ` `is_dynamic_context_reminder(message: object) -> bool`  L71
  - _文档首行_（仅供参考）: Return whether *message* is a hidden dynamic-context reminder.
  - 分支数 0，函数体节点数 35；return: isinstance(message, (HumanMessage, SystemMessage)) and bool(message.additional_kwargs.get(_DYNAMIC_CONTEXT_REMINDER_KEY))
  - 调用: isinstance, bool, get

#### `ƒ` `_last_injected_date(messages: list) -> str | None`  L79
  - _文档首行_（仅供参考）: Scan messages in reverse and return the most recently injected date.
  - 分支数 5，函数体节点数 107；return: structured, date, None
  - 调用: reversed, is_dynamic_context_reminder, get, isinstance, str, _extract_date

#### `ƒ` `_is_user_injection_target(message: object) -> bool`  L109
  - _文档首行_（仅供参考）: Return whether *message* can receive a dynamic-context reminder.
  - 分支数 4，函数体节点数 62；return: False, True
  - 调用: isinstance, is_dynamic_context_reminder, endswith, str

## 类
### 类 `DynamicContextMiddleware`  L128
- 继承: AgentMiddleware
- _文档首行_: Inject memory and current date as a SystemMessage <system-reminder>.
- 方法:
  #### `st` `_make_reminder_and_user_messages(original: HumanMessage, reminder_content: str, memory_content: str | None, *, reminder_date: str | None) -> list[SystemMessage | HumanMessage]`    @staticmethod  L188
    - _文档首行_（仅供参考）: Return messages using the ID-swap technique.
    - 分支数 2，函数体节点数 171；return: messages
    - 调用: str, uuid4, append, SystemMessage, HumanMessage
  #### `st` `_effective_memory_message(state, update: dict | None, runtime: Runtime) -> HumanMessage | None`    @staticmethod  L318
    - _文档首行_（仅供参考）: Find server-created memory that is effective for this run.
    - 分支数 9，函数体节点数 235；return: message, None
    - 调用: isinstance, get, str, endswith, is_dynamic_context_reminder, getattr
  - 反射: getattr (L336)
  #### `m` `__init__(self, agent_name: str | None, *, app_config: AppConfig | None)`  L146
    - 分支数 0，函数体节点数 38
    - 调用: __init__, super
  #### `m` `_build_full_reminder(self) -> tuple[str, str | None]`  L151
    - _文档首行_（仅供参考）: Return (date_reminder, memory_block | None).
    - 分支数 0，函数体节点数 104；return: (date_reminder, memory_block)
    - 调用: _get_memory_context, strftime, now, join, strip
  #### `m` `_build_date_update_reminder(self) -> str`  L177
    - 分支数 0，函数体节点数 32；return: '\n'.join(['<system-reminder>', f'<current_date>{current_date}</current_date>', '</system-reminder>'])
    - 调用: strftime, now, join
  #### `m` `_inject(self, state) -> dict | None`  L242
    - 分支数 5，函数体节点数 249；return: None, {'messages': result_msgs}
    - 调用: list, get, strftime, now, _last_injected_date, debug, len, next, enumerate, _is_user_injection_target, _build_full_reminder, info, _make_reminder_and_user_messages, reversed, range, _build_date_update_reminder
  #### `m` `before_agent(self, state, runtime: Runtime) -> dict | None`    @override  L284
    - 分支数 0，函数体节点数 39；return: result
    - 调用: _inject, _record_effective_memory
  #### `m` `_record_effective_memory(self, state, update: dict | None, runtime: Runtime) -> None`  L349
    - _文档首行_（仅供参考）: Attach the effective hidden memory block to the current run ledger.
    - 分支数 3，函数体节点数 108；return: None
    - 调用: getattr, isinstance, get, _effective_memory_message, record_memory_context, hexdigest, sha256, encode, debug
  - 反射: getattr (L351)
  #### `⏵m` `async abefore_agent(self, state, runtime: Runtime) -> dict | None`    @override  L290
    - 分支数 1，函数体节点数 78；return: None, result
    - 调用: wait_for, to_thread, warning, _record_effective_memory

## 文件内调用关系
- `_last_injected_date` -> is_dynamic_context_reminder, _extract_date
- `_is_user_injection_target` -> is_dynamic_context_reminder
- `DynamicContextMiddleware.__init__` -> __init__
- `DynamicContextMiddleware._inject` -> _last_injected_date, _is_user_injection_target, _build_full_reminder, _make_reminder_and_user_messages, _build_date_update_reminder
- `DynamicContextMiddleware.before_agent` -> _inject, _record_effective_memory
- `DynamicContextMiddleware.abefore_agent` -> _record_effective_memory
- `DynamicContextMiddleware._effective_memory_message` -> is_dynamic_context_reminder
- `DynamicContextMiddleware._record_effective_memory` -> _effective_memory_message

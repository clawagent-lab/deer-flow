# `backend/packages/harness/deerflow/agents/middlewares/view_image_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/view_image_middleware.py`  ·  行数: 279

**模块文档首行**（仅供参考）: Middleware for injecting image details into conversation before LLM call.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: asyncio, base64, logging
- `pathlib` -> Path
- `typing` -> override
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain_core.messages` -> AIMessage, HumanMessage, ToolMessage
- `langgraph.runtime` -> Runtime
- `deerflow.agents.thread_state` -> ThreadState

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_MAX_IMAGE_BYTES` = 20 * 1024 * 1024

## 类
### 类 `ViewImageMiddlewareState`  L23
- 继承: ThreadState
- _文档首行_: Reuse the thread state so reducer-backed keys keep their annotations.

### 类 `ViewImageMiddleware`  L27
- 继承: AgentMiddleware[ViewImageMiddlewareState]
- _文档首行_: Injects image details as a human message before LLM calls when view_image tools have completed.
- 类/实例变量:
  - `state_schema` = ViewImageMiddlewareState
- 方法:
  #### `st` `_read_image_as_data_url(actual_path: str, mime_type: str, expected_size: int) -> str | None`    @staticmethod  L103
    - _文档首行_（仅供参考）: Read image file and return a `data:` URL, or None on failure.
    - 分支数 5，函数体节点数 123；return: None, f'data:{mime_type};base64,{base64_data}'
    - 调用: Path, exists, is_file, stat, open, read, decode, b64encode
  - 文件IO: exists (L115), stat (L117), open (L123), read (L124)
  #### `m` `_get_last_assistant_message(self, messages: list) -> AIMessage | None`  L43
    - _文档首行_（仅供参考）: Get the last assistant message from the message list.
    - 分支数 2，函数体节点数 34；return: msg, None
    - 调用: reversed, isinstance
  #### `m` `_has_view_image_tool(self, message: AIMessage) -> bool`  L57
    - _文档首行_（仅供参考）: Check if the assistant message contains view_image tool calls.
    - 分支数 1，函数体节点数 50；return: False, any((tool_call.get('name') == 'view_image' for tool_call in message.tool_calls))
    - 调用: hasattr, any, get
  - 反射: hasattr (L66)
  #### `m` `_all_tools_completed(self, messages: list, assistant_msg: AIMessage) -> bool`  L71
    - _文档首行_（仅供参考）: Check if all tool calls in the assistant message have been completed.
    - 分支数 4，函数体节点数 122；return: False, tool_call_ids.issubset(completed_tool_ids)
    - 调用: hasattr, get, index, set, isinstance, add, issubset
  - 反射: hasattr (L81)
  #### `m` `_create_image_details_message(self, state: ViewImageMiddlewareState) -> list[str | dict]`  L130
    - _文档首行_（仅供参考）: Create a formatted message with all viewed image details.
    - 分支数 4，函数体节点数 176；return: [{'type': 'text', 'text': 'No images have been viewed.'}], content_blocks
    - 调用: get, items, append, _read_image_as_data_url
  #### `m` `_should_inject_image_message(self, state: ViewImageMiddlewareState) -> bool`  L176
    - _文档首行_（仅供参考）: Determine if we should inject an image details message.
    - 分支数 7，函数体节点数 129；return: False, True
    - 调用: get, _get_last_assistant_message, _has_view_image_tool, _all_tools_completed, index, isinstance, str
  #### `m` `_inject_image_message(self, state: ViewImageMiddlewareState) -> dict | None`  L214
    - _文档首行_（仅供参考）: Internal helper to inject image details message.
    - 分支数 1，函数体节点数 62；return: None, {'messages': [human_msg]}
    - 调用: _should_inject_image_message, _create_image_details_message, HumanMessage, debug
  #### `m` `before_model(self, state: ViewImageMiddlewareState, runtime: Runtime) -> dict | None`    @override  L240
    - _文档首行_（仅供参考）: Inject image details message before LLM call if view_image tools have completed (sync version).
    - 分支数 0，函数体节点数 26；return: self._inject_image_message(state)
    - 调用: _inject_image_message
  #### `⏵m` `async abefore_model(self, state: ViewImageMiddlewareState, runtime: Runtime) -> dict | None`    @override  L257
    - _文档首行_（仅供参考）: Inject image details message before LLM call if view_image tools have completed (async version).
    - 分支数 1，函数体节点数 72；return: None, {'messages': [human_msg]}
    - 调用: _should_inject_image_message, to_thread, HumanMessage, debug

## 文件内调用关系
- `ViewImageMiddleware._create_image_details_message` -> _read_image_as_data_url
- `ViewImageMiddleware._should_inject_image_message` -> _get_last_assistant_message, _has_view_image_tool, _all_tools_completed
- `ViewImageMiddleware._inject_image_message` -> _should_inject_image_message, _create_image_details_message
- `ViewImageMiddleware.before_model` -> _inject_image_message
- `ViewImageMiddleware.abefore_model` -> _should_inject_image_message

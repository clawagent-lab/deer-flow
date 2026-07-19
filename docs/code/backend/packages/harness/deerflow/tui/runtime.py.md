# `backend/packages/harness/deerflow/tui/runtime.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/runtime.py`  ·  行数: 131

**模块文档首行**（仅供参考）: Runtime bridge between ``DeerFlowClient`` streaming and the view-state reducer.

## 模块概览
- 函数 5 个，类 2 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Iterator
- `typing` -> Any, Protocol
- `.view_state` -> Action, AssistantDelta, AssistantError, RunEnded, RunStarted, ThreadTitle, ToolResult, ToolStarted

## 函数
#### `ƒ` `translate(event: _StreamEventLike) -> list[Action]`  L41
  - _文档首行_（仅供参考）: Map a single ``StreamEvent`` to reducer actions. Pure.
  - 分支数 4，函数体节点数 131；return: _translate_message(event.data), [RunEnded(usage=usage)], [ThreadTitle(title=title.strip())], []
  - 调用: _translate_message, isinstance, get, RunEnded, strip, ThreadTitle

#### `ƒ` `_translate_message(data: Any) -> list[Action]`  L57
  - 分支数 6，函数体节点数 224；return: [], actions
  - 调用: isinstance, get, _extract_text, append, AssistantDelta, _as_str, ToolStarted, bool, ToolResult

#### `ƒ` `_as_str(value: Any) -> str`  L92
  - 分支数 0，函数体节点数 20；return: '' if value is None else str(value)
  - 调用: str

#### `ƒ` `stream_actions(client: _ClientLike, message: str, *, thread_id: str | None, **kwargs) -> Iterator[Action]`  L99
  - _文档首行_（仅供参考）: Yield a bracketed action stream for one agent run.
  - 分支数 3，函数体节点数 95；生成器（yield）；可变参数（*args/**kwargs）；return: None
  - 调用: stream

#### `ƒ` `_extract_text(content: Any) -> str`  L117
  - 分支数 6，函数体节点数 120；return: '', content, ''.join(parts), str(content)
  - 调用: isinstance, append, get, join, str

## 类
### 类 `_StreamEventLike`  L31
- 继承: Protocol
- 类/实例变量:
  - `type` = <annotated>
  - `data` = <annotated>

### 类 `_ClientLike`  L36
- 继承: Protocol
- 方法:
  #### `m` `stream(self, message: str, *, thread_id: str | None, **kwargs) -> Iterator[Any]`  L37
    - _文档首行_（仅供参考）: Yield streaming events for *message* (see ``DeerFlowClient.stream``).
    - 分支数 0，函数体节点数 24；可变参数（*args/**kwargs）

## 文件内调用关系
- `translate` -> _translate_message
- `_translate_message` -> _extract_text, _as_str
- `stream_actions` -> stream

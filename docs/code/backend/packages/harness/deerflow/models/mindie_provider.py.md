# `backend/packages/harness/deerflow/models/mindie_provider.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/mindie_provider.py`  ·  行数: 255

## 模块概览
- 函数 4 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: ast, html, json, re, uuid, httpx
- `collections.abc` -> Iterator
- `langchain_core.messages` -> AIMessage, AIMessageChunk, HumanMessage, ToolMessage
- `langchain_core.outputs` -> ChatGenerationChunk, ChatResult
- `langchain_openai` -> ChatOpenAI

## 函数
#### `ƒ` `_fix_messages(messages: list) -> list`  L14
  - _文档首行_（仅供参考）: Sanitize incoming messages for MindIE compatibility.
  - 分支数 9，函数体节点数 348；return: fixed
  - 调用: isinstance, append, get, join, getattr, escape, str, dumps, items, AIMessage, strip, HumanMessage, model_copy
  - 反射: getattr (L37)

#### `ƒ` `_parse_xml_tool_call_to_dict(content: str) -> tuple[str, list[dict]]`  L66
  - _文档首行_（仅供参考）: Parse XML-style tool calls from model output into LangChain dicts.
  - 分支数 8，函数体节点数 395；return: (content, []), (''.join(clean_parts).strip(), tool_calls)
  - 调用: isinstance, _iter_tool_call_blocks, append, search, unescape, strip, group, join, compile, finditer, startswith, isdigit, loads, literal_eval, uuid4
  - 危险执行: compile (L103)

#### `ƒ` `_iter_tool_call_blocks(content: str) -> Iterator[tuple[int, int, str]]`  L128
  - _文档首行_（仅供参考）: Iterate `<tool_call>...</tool_call>` blocks and tolerate nesting.
  - 分支数 5，函数体节点数 164；生成器（yield）
  - 调用: compile, finditer, group, start, end, len
  - 危险执行: compile (L130)

#### `ƒ` `_decode_escaped_newlines_outside_fences(content: str) -> str`  L154
  - _文档首行_（仅供参考）: Decode literal `\n` outside fenced code blocks.
  - 分支数 3，函数体节点数 70；return: content, ''.join(parts)
  - 调用: split, enumerate, startswith, replace, join
  - 文件IO: replace (L163)

## 类
### 类 `MindIEChatModel`  L167
- 继承: ChatOpenAI
- _文档首行_: Chat model adapter for MindIE engine.
- 方法:
  #### `m` `__init__(self, **kwargs)`  L178
    - _文档首行_（仅供参考）: Normalize timeout kwargs without creating long-lived clients.
    - 分支数 0，函数体节点数 80；可变参数（*args/**kwargs）
    - 调用: pop, setdefault, Timeout, __init__, super
  #### `m` `_patch_result_with_tools(self, result: ChatResult) -> ChatResult`  L196
    - _文档首行_（仅供参考）: Apply post-generation fixes to the model result.
    - 分支数 5，函数体节点数 109；return: result
    - 调用: isinstance, _decode_escaped_newlines_outside_fences, _parse_xml_tool_call_to_dict, getattr, extend
  - 反射: getattr (L210)
  #### `m` `_generate(self, messages, stop, run_manager, **kwargs)`  L215
    - 分支数 0，函数体节点数 40；可变参数（*args/**kwargs）；return: self._patch_result_with_tools(result)
    - 调用: _generate, super, _fix_messages, _patch_result_with_tools
  #### `⏵m` `async _agenerate(self, messages, stop, run_manager, **kwargs)`  L219
    - 分支数 0，函数体节点数 41；可变参数（*args/**kwargs）；return: self._patch_result_with_tools(result)
    - 调用: _agenerate, super, _fix_messages, _patch_result_with_tools
  #### `⏵m` `async _astream(self, messages, stop, run_manager, **kwargs)`  L223
    - 分支数 7，函数体节点数 288；生成器（yield）；可变参数（*args/**kwargs）；return: None
    - 调用: get, _astream, super, _fix_messages, isinstance, _decode_escaped_newlines_outside_fences, _agenerate, getattr, range, len, AIMessageChunk
  - 反射: getattr (L240), getattr (L251), getattr (L253)

## 文件内调用关系
- `_parse_xml_tool_call_to_dict` -> _iter_tool_call_blocks
- `MindIEChatModel.__init__` -> __init__
- `MindIEChatModel._patch_result_with_tools` -> _decode_escaped_newlines_outside_fences, _parse_xml_tool_call_to_dict
- `MindIEChatModel._generate` -> _generate, _fix_messages, _patch_result_with_tools
- `MindIEChatModel._agenerate` -> _agenerate, _fix_messages, _patch_result_with_tools
- `MindIEChatModel._astream` -> _astream, _fix_messages, _decode_escaped_newlines_outside_fences, _agenerate

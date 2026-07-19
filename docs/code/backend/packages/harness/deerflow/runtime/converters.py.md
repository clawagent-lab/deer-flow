# `backend/packages/harness/deerflow/runtime/converters.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/converters.py`  ·  行数: 137

**模块文档首行**（仅供参考）: Pure functions to convert LangChain message objects to OpenAI Chat Completions format.

## 模块概览
- 函数 4 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: json
- `__future__` -> annotations
- `typing` -> Any

## 模块级常量
- `_ROLE_MAP` = {'human': 'user', 'ai': 'assistant', 'system': 'system', ...

## 函数
#### `ƒ` `langchain_to_openai_message(message: Any) -> dict`  L21
  - _文档首行_（仅供参考）: Convert a single LangChain BaseMessage to an OpenAI message dict.
  - 分支数 4，函数体节点数 221；return: {'role': 'tool', 'tool_call_id': getattr(message, 'tool_call_id', ''), 'content': content}, result, {'role': role, 'content': content}
  - 调用: getattr, get, append, isinstance, dumps
  - 反射: getattr (L33), getattr (L35), getattr (L40), getattr (L45)

#### `ƒ` `_infer_finish_reason(message: Any) -> str`  L74
  - _文档首行_（仅供参考）: Infer OpenAI finish_reason from an AIMessage.
  - 分支数 3，函数体节点数 66；return: 'tool_calls', finish, 'stop'
  - 调用: getattr, isinstance, get
  - 反射: getattr (L80), getattr (L83)

#### `ƒ` `langchain_to_openai_completion(message: Any) -> dict`  L91
  - _文档首行_（仅供参考）: Convert an AIMessage and its metadata to an OpenAI completion response dict.
  - 分支数 1，函数体节点数 152；return: {'id': getattr(message, 'id', None), 'model': model_name, 'choices': [{'index': 0, 'message': openai_msg, 'finish_reason': finish_reason}], 'usage': usage}
  - 调用: getattr, isinstance, get, langchain_to_openai_message, _infer_finish_reason
  - 反射: getattr (L102), getattr (L108), getattr (L121)

#### `ƒ` `langchain_messages_to_openai(messages: list) -> list[dict]`  L134
  - _文档首行_（仅供参考）: Convert a list of LangChain BaseMessages to OpenAI message dicts.
  - 分支数 0，函数体节点数 25；return: [langchain_to_openai_message(m) for m in messages]
  - 调用: langchain_to_openai_message

## 文件内调用关系
- `langchain_to_openai_completion` -> langchain_to_openai_message, _infer_finish_reason
- `langchain_messages_to_openai` -> langchain_to_openai_message

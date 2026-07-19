# `backend/packages/harness/deerflow/models/patched_deepseek.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/models/patched_deepseek.py`  ·  行数: 60

**模块文档首行**（仅供参考）: Patched ChatDeepSeek that preserves reasoning_content in multi-turn conversations.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `typing` -> Any
- `langchain_core.language_models` -> LanguageModelInput
- `langchain_deepseek` -> ChatDeepSeek
- `deerflow.models.assistant_payload_replay` -> restore_assistant_payloads, restore_reasoning_content

## 类
### 类 `PatchedChatDeepSeek`  L18
- 继承: ChatDeepSeek
- _文档首行_: ChatDeepSeek with proper reasoning_content preservation.
- 方法:
  #### `prop` `lc_secrets(self) -> dict[str, str]`    @property  L32
    - 分支数 0，函数体节点数 21；return: {'api_key': 'DEEPSEEK_API_KEY', 'openai_api_key': 'DEEPSEEK_API_KEY'}
  #### `cls` `is_lc_serializable(cls) -> bool`    @classmethod  L28
    - 分支数 0，函数体节点数 9；return: True
  #### `m` `_get_request_payload(self, input_: LanguageModelInput, *, stop: list[str] | None, **kwargs) -> dict`  L35
    - _文档首行_（仅供参考）: Get request payload with reasoning_content preserved.
    - 分支数 0，函数体节点数 73；可变参数（*args/**kwargs）；return: payload
    - 调用: to_messages, _convert_input, _get_request_payload, super, restore_assistant_payloads, get

## 文件内调用关系
- `PatchedChatDeepSeek._get_request_payload` -> _get_request_payload

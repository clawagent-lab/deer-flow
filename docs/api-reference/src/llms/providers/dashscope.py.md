# `src/llms/providers/dashscope.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/llms/providers/dashscope.py`
- **模块导入名**：`src.llms.providers.dashscope`
- **代码行数**：327
- **架构归属**：src/llms —— LLM 适配层（统一封装 dashscope 等提供商，按类型路由）

## 模块概述

```text
阿里通义千问 DashScope 平台的 LangChain ChatModel 适配器。

基于 ``langchain_openai.ChatOpenAI`` 扩展，针对 DashScope 的 OpenAI 兼容接口
补齐流式增量解析（``_convert_delta_to_message_chunk``）等行为，使项目能够
通过统一接口调用通义千问系列模型（含 reasoning 等模式）。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Dict, Iterator, List, Mapping, Optional, Type, Union, cast`
- `from langchain_core.callbacks import CallbackManagerForLLMRun`
- `from langchain_core.messages import AIMessageChunk, BaseMessage, BaseMessageChunk, ChatMessageChunk, FunctionMessageChunk, HumanMessageChunk, SystemMessageChunk, ToolMessageChunk`
- `from langchain_core.messages.ai import UsageMetadata`
- `from langchain_core.messages.tool import tool_call_chunk`
- `from langchain_core.outputs import ChatGenerationChunk, ChatResult`
- `from langchain_openai import ChatOpenAI`
- `from langchain_openai.chat_models.base import _create_usage_metadata, _handle_openai_bad_request, warnings`
- `import openai`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `_convert_delta_to_message_chunk` | 38 | `(delta_dict: Mapping[str, Any], default_class: Type[BaseMessageChunk]) -> BaseMessageChunk` |
| 函数 | `_convert_chunk_to_generation_chunk` | 117 | `(chunk: Dict[str, Any], default_chunk_class: Type[BaseMessageChunk], base_generation_info: Option...` |
| 类 | `ChatDashscope` | 185 | `` |

## 符号详解

### `_convert_delta_to_message_chunk`

- **类型**：函数  |  **行号**：38–114  |  **完整限定名**：`src.llms.providers.dashscope._convert_delta_to_message_chunk`
- **签名**：

```python
def _convert_delta_to_message_chunk(delta_dict: Mapping[str, Any], default_class: Type[BaseMessageChunk]) -> BaseMessageChunk:
```

**摘要**：

Convert a delta dictionary to a message chunk.

**参数**：

```text
delta_dict: Dictionary containing delta information from OpenAI response
    default_class: Default message chunk class to use if role is not specified
```

**返回值**：

```text
BaseMessageChunk: Appropriate message chunk based on role and content
```

**异常**：

```text
KeyError: If required keys are missing from the delta dictionary
```

### `_convert_chunk_to_generation_chunk`

- **类型**：函数  |  **行号**：117–182  |  **完整限定名**：`src.llms.providers.dashscope._convert_chunk_to_generation_chunk`
- **签名**：

```python
def _convert_chunk_to_generation_chunk(chunk: Dict[str, Any], default_chunk_class: Type[BaseMessageChunk], base_generation_info: Optional[Dict[str, Any]]) -> Optional[ChatGenerationChunk]:
```

**摘要**：

Convert a streaming chunk to a generation chunk.

**参数**：

```text
chunk: Raw chunk data from OpenAI streaming response
    default_chunk_class: Default message chunk class to use
    base_generation_info: Base generation information to include
```

**返回值**：

```text
Optional[ChatGenerationChunk]: Generated chunk or None if chunk should be skipped
```

### `ChatDashscope`

- **类型**：类  |  **行号**：185–327  |  **完整限定名**：`src.llms.providers.dashscope.ChatDashscope`
- **基类**：`ChatOpenAI`
- **定义**：

```python
class ChatDashscope(ChatOpenAI):
```
- **成员概览**：

  - `def _create_chat_result`
  - `def _stream`

**摘要**：

Extended ChatOpenAI model with reasoning capabilities.

## 调用关系（下游）

**被以下模块导入**：

- `src.llms.llm`
- `tests.unit.llms.test_dashscope`

## 示例用法

```python
from src.llms.providers.dashscope import ChatDashscope
#
# TODO: 结合业务场景补充 ChatDashscope 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

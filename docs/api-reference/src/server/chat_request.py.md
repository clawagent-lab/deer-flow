# `src/server/chat_request.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/chat_request.py`
- **模块导入名**：`src.server.chat_request`
- **代码行数**：138
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
聊天及生成相关请求体 Pydantic 模型定义。

包含 ``ChatRequest``（聊天对话主请求，含历史消息、研究资源、计划/澄清/搜索等
运行参数）、``TTSRequest``（语音合成）、``GeneratePodcastRequest`` /
``GeneratePPTRequest`` / ``GenerateProseRequest``（播客、PPT、散文生成）以及
``EnhancePromptRequest``（提示词增强）等模型，供 FastAPI 路由统一校验入参。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.report_style import ReportStyle`
- `from src.rag.retriever import Resource`

**外部依赖**（第三方库 / 标准库）：

- `from typing import List, Optional, Union`
- `from pydantic import BaseModel, Field`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `ContentItem` | 20 | `` |
| 类 | `ChatMessage` | 28 | `` |
| 类 | `ChatRequest` | 38 | `` |
| 类 | `TTSRequest` | 96 | `` |
| 类 | `GeneratePodcastRequest` | 112 | `` |
| 类 | `GeneratePPTRequest` | 116 | `` |
| 类 | `GenerateProseRequest` | 123 | `` |
| 类 | `EnhancePromptRequest` | 131 | `` |

## 符号详解

### `ContentItem`

- **类型**：类  |  **行号**：20–25  |  **完整限定名**：`src.server.chat_request.ContentItem`
- **基类**：`BaseModel`
- **定义**：

```python
class ContentItem(BaseModel):
```
- **成员概览**：

  - `attr type`
  - `attr text`
  - `attr image_url`

**说明**（自动推断）：

Pydantic 数据模型 `ContentItem`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `ChatMessage`

- **类型**：类  |  **行号**：28–35  |  **完整限定名**：`src.server.chat_request.ChatMessage`
- **基类**：`BaseModel`
- **定义**：

```python
class ChatMessage(BaseModel):
```
- **成员概览**：

  - `attr role`
  - `attr content`

**说明**（自动推断）：

Pydantic 数据模型 `ChatMessage`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `ChatRequest`

- **类型**：类  |  **行号**：38–93  |  **完整限定名**：`src.server.chat_request.ChatRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class ChatRequest(BaseModel):
```
- **成员概览**：

  - `attr messages`
  - `attr resources`
  - `attr debug`
  - `attr thread_id`
  - `attr locale`
  - `attr max_plan_iterations`
  - `attr max_step_num`
  - `attr max_search_results`
  - `attr auto_accepted_plan`
  - `attr interrupt_feedback`
  - `attr mcp_settings`
  - `attr enable_background_investigation`
  - `attr enable_web_search`
  - `attr report_style`
  - `attr enable_deep_thinking`
  - `attr enable_clarification`
  - `attr max_clarification_rounds`
  - `attr interrupt_before_tools`

**说明**（自动推断）：

Pydantic 数据模型 `ChatRequest`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `TTSRequest`

- **类型**：类  |  **行号**：96–109  |  **完整限定名**：`src.server.chat_request.TTSRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class TTSRequest(BaseModel):
```
- **成员概览**：

  - `attr text`
  - `attr voice_type`
  - `attr encoding`
  - `attr speed_ratio`
  - `attr volume_ratio`
  - `attr pitch_ratio`
  - `attr text_type`
  - `attr with_frontend`
  - `attr frontend_type`

**说明**（自动推断）：

Pydantic 数据模型 `TTSRequest`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `GeneratePodcastRequest`

- **类型**：类  |  **行号**：112–113  |  **完整限定名**：`src.server.chat_request.GeneratePodcastRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class GeneratePodcastRequest(BaseModel):
```
- **成员概览**：

  - `attr content`

**说明**（自动推断）：

Pydantic 数据模型 `GeneratePodcastRequest`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `GeneratePPTRequest`

- **类型**：类  |  **行号**：116–120  |  **完整限定名**：`src.server.chat_request.GeneratePPTRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class GeneratePPTRequest(BaseModel):
```
- **成员概览**：

  - `attr content`
  - `attr locale`

**说明**（自动推断）：

Pydantic 数据模型 `GeneratePPTRequest`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `GenerateProseRequest`

- **类型**：类  |  **行号**：123–128  |  **完整限定名**：`src.server.chat_request.GenerateProseRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class GenerateProseRequest(BaseModel):
```
- **成员概览**：

  - `attr prompt`
  - `attr option`
  - `attr command`

**说明**（自动推断）：

Pydantic 数据模型 `GenerateProseRequest`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `EnhancePromptRequest`

- **类型**：类  |  **行号**：131–138  |  **完整限定名**：`src.server.chat_request.EnhancePromptRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class EnhancePromptRequest(BaseModel):
```
- **成员概览**：

  - `attr prompt`
  - `attr context`
  - `attr report_style`

**说明**（自动推断）：

Pydantic 数据模型 `EnhancePromptRequest`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

## 调用关系（下游）

**被以下模块导入**：

- `src.server.app`
- `tests.integration.test_tool_interceptor_integration`
- `tests.unit.server.test_chat_request`

## 示例用法

```python
from src.server.chat_request import ContentItem
#
# TODO: 结合业务场景补充 ContentItem 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

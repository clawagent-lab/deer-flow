# `tests/unit/server/test_app.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/server/test_app.py`
- **模块导入名**：`tests.unit.server.test_app`
- **代码行数**：1733
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.report_style import ReportStyle`
- `from src.server.app import _astream_workflow_generator, _create_event_stream_message, _create_interrupt_event, _make_event, _stream_graph_events, app`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import AsyncMock, MagicMock, mock_open, patch`
- `from fastapi import HTTPException`
- `from fastapi.testclient import TestClient`
- `from langchain_core.messages import AIMessageChunk, ToolMessage`
- `from langgraph.types import Command`
- `import asyncio`
- `import base64`
- `import os`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `client` | 28 | `()` |
| 类 | `TestMakeEvent` | 32 | `` |
| 类 | `TestStreamGraphEventsCancellation` | 59 | `` |
| 异步函数 | `test_astream_workflow_generator_preserves_clarification_history` | 111 | `()` |
| 类 | `TestTTSEndpoint` | 184 | `` |
| 类 | `TestPodcastEndpoint` | 286 | `` |
| 类 | `TestPPTEndpoint` | 313 | `` |
| 类 | `TestEnhancePromptEndpoint` | 346 | `` |
| 类 | `TestMCPEndpoint` | 396 | `` |
| 类 | `TestRAGEndpoints` | 515 | `` |
| 类 | `TestChatStreamEndpoint` | 655 | `` |
| 类 | `TestAstreamWorkflowGenerator` | 767 | `` |
| 类 | `TestGenerateProseEndpoint` | 1082 | `` |
| 类 | `TestCreateInterruptEvent` | 1126 | `` |
| 类 | `TestLifespanFunction` | 1217 | `` |
| 类 | `TestGlobalConnectionPoolUsage` | 1462 | `` |
| 类 | `TestCreateEventStreamMessageThinkTagStripping` | 1686 | `` |

## 符号详解

### `client`

- **类型**：函数  |  **行号**：28–29  |  **完整限定名**：`tests.unit.server.test_app.client`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def client():
```

**说明**（自动推断）：

pytest fixture，提供 FastAPI TestClient 实例供测试用例发送 HTTP 请求。

### `TestMakeEvent`

- **类型**：类  |  **行号**：32–56  |  **完整限定名**：`tests.unit.server.test_app.TestMakeEvent`
- **定义**：

```python
class TestMakeEvent:
```
- **成员概览**：

  - `def test_make_event_with_content`
  - `def test_make_event_with_empty_content`
  - `def test_make_event_without_content`

**说明**（自动推断）：

pytest 测试类 `TestMakeEvent`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestStreamGraphEventsCancellation`

- **类型**：类  |  **行号**：59–107  |  **完整限定名**：`tests.unit.server.test_app.TestStreamGraphEventsCancellation`
- **定义**：

```python
class TestStreamGraphEventsCancellation:
```
- **成员概览**：

  - `async def test_cancelled_error_does_not_propagate`
  - `async def test_cancelled_error_yields_cancelled_reason`

**摘要**：

Tests for graceful handling of asyncio.CancelledError in _stream_graph_events.

### `test_astream_workflow_generator_preserves_clarification_history`

- **类型**：异步函数  |  **行号**：111–181  |  **完整限定名**：`tests.unit.server.test_app.test_astream_workflow_generator_preserves_clarification_history`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_astream_workflow_generator_preserves_clarification_history():
```

**说明**（自动推断）：

测试用例函数 `test_astream_workflow_generator_preserves_clarification_history`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `TestTTSEndpoint`

- **类型**：类  |  **行号**：184–283  |  **完整限定名**：`tests.unit.server.test_app.TestTTSEndpoint`
- **定义**：

```python
class TestTTSEndpoint:
```
- **成员概览**：

  - `def test_tts_success`
  - `def test_tts_missing_app_id`
  - `def test_tts_missing_access_token`
  - `def test_tts_api_error`
  - `def test_tts_api_exception`

**说明**（自动推断）：

pytest 测试类 `TestTTSEndpoint`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestPodcastEndpoint`

- **类型**：类  |  **行号**：286–310  |  **完整限定名**：`tests.unit.server.test_app.TestPodcastEndpoint`
- **定义**：

```python
class TestPodcastEndpoint:
```
- **成员概览**：

  - `def test_generate_podcast_success`
  - `def test_generate_podcast_error`

**说明**（自动推断）：

pytest 测试类 `TestPodcastEndpoint`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestPPTEndpoint`

- **类型**：类  |  **行号**：313–343  |  **完整限定名**：`tests.unit.server.test_app.TestPPTEndpoint`
- **定义**：

```python
class TestPPTEndpoint:
```
- **成员概览**：

  - `def test_generate_ppt_success`
  - `def test_generate_ppt_error`

**说明**（自动推断）：

pytest 测试类 `TestPPTEndpoint`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestEnhancePromptEndpoint`

- **类型**：类  |  **行号**：346–393  |  **完整限定名**：`tests.unit.server.test_app.TestEnhancePromptEndpoint`
- **定义**：

```python
class TestEnhancePromptEndpoint:
```
- **成员概览**：

  - `def test_enhance_prompt_success`
  - `def test_enhance_prompt_with_different_styles`
  - `def test_enhance_prompt_error`

**说明**（自动推断）：

pytest 测试类 `TestEnhancePromptEndpoint`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestMCPEndpoint`

- **类型**：类  |  **行号**：396–512  |  **完整限定名**：`tests.unit.server.test_app.TestMCPEndpoint`
- **定义**：

```python
class TestMCPEndpoint:
```
- **成员概览**：

  - `def test_mcp_server_metadata_success`
  - `def test_mcp_server_metadata_with_custom_timeout`
  - `def test_mcp_server_metadata_with_sse_read_timeout`
  - `def test_mcp_server_metadata_with_exception`
  - `def test_mcp_server_metadata_without_enable_configuration`

**说明**（自动推断）：

pytest 测试类 `TestMCPEndpoint`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestRAGEndpoints`

- **类型**：类  |  **行号**：515–652  |  **完整限定名**：`tests.unit.server.test_app.TestRAGEndpoints`
- **定义**：

```python
class TestRAGEndpoints:
```
- **成员概览**：

  - `def test_rag_config`
  - `def test_rag_resources_with_retriever`
  - `def test_rag_resources_without_retriever`
  - `def test_upload_rag_resource_success`
  - `def test_upload_rag_resource_no_retriever`
  - `def test_upload_rag_resource_not_implemented`
  - `def test_upload_rag_resource_value_error`
  - `def test_upload_rag_resource_runtime_error`
  - `def test_upload_rag_resource_invalid_file_type`
  - `def test_upload_rag_resource_empty_file`
  - `def test_upload_rag_resource_file_too_large`
  - `def test_upload_rag_resource_path_traversal_sanitized`

**说明**（自动推断）：

pytest 测试类 `TestRAGEndpoints`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestChatStreamEndpoint`

- **类型**：类  |  **行号**：655–764  |  **完整限定名**：`tests.unit.server.test_app.TestChatStreamEndpoint`
- **定义**：

```python
class TestChatStreamEndpoint:
```
- **成员概览**：

  - `def test_chat_stream_with_default_thread_id`
  - `def test_chat_stream_with_mcp_settings`
  - `def test_chat_stream_with_mcp_settings_enabled`

**说明**（自动推断）：

pytest 测试类 `TestChatStreamEndpoint`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestAstreamWorkflowGenerator`

- **类型**：类  |  **行号**：767–1079  |  **完整限定名**：`tests.unit.server.test_app.TestAstreamWorkflowGenerator`
- **定义**：

```python
class TestAstreamWorkflowGenerator:
```
- **成员概览**：

  - `async def test_astream_workflow_generator_basic_flow`
  - `async def test_astream_workflow_generator_with_interrupt_feedback`
  - `async def test_astream_workflow_generator_interrupt_event`
  - `async def test_astream_workflow_generator_tool_message`
  - `async def test_astream_workflow_generator_ai_message_with_tool_calls`
  - `async def test_astream_workflow_generator_ai_message_with_tool_call_chunks`
  - `async def test_astream_workflow_generator_with_finish_reason`
  - `async def test_astream_workflow_generator_config_passed_correctly`

**说明**（自动推断）：

pytest 测试类 `TestAstreamWorkflowGenerator`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestGenerateProseEndpoint`

- **类型**：类  |  **行号**：1082–1123  |  **完整限定名**：`tests.unit.server.test_app.TestGenerateProseEndpoint`
- **定义**：

```python
class TestGenerateProseEndpoint:
```
- **成员概览**：

  - `def test_generate_prose_success`
  - `def test_generate_prose_error`

**说明**（自动推断）：

pytest 测试类 `TestGenerateProseEndpoint`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestCreateInterruptEvent`

- **类型**：类  |  **行号**：1126–1214  |  **完整限定名**：`tests.unit.server.test_app.TestCreateInterruptEvent`
- **定义**：

```python
class TestCreateInterruptEvent:
```
- **成员概览**：

  - `def test_create_interrupt_event_with_id_attribute`
  - `def test_create_interrupt_event_fallback_to_thread_id`
  - `def test_create_interrupt_event_without_id_attribute`
  - `def test_create_interrupt_event_options`
  - `def test_create_interrupt_event_with_complex_value`

**摘要**：

Tests for _create_interrupt_event function (Issue #730 fix).

### `TestLifespanFunction`

- **类型**：类  |  **行号**：1217–1459  |  **完整限定名**：`tests.unit.server.test_app.TestLifespanFunction`
- **定义**：

```python
class TestLifespanFunction:
```
- **成员概览**：

  - `async def test_lifespan_skips_initialization_when_checkpoint_not_configured`
  - `async def test_lifespan_skips_initialization_when_url_empty`
  - `async def test_lifespan_postgresql_pool_initialization_success`
  - `async def test_lifespan_postgresql_pool_initialization_failure`
  - `async def test_lifespan_mongodb_pool_initialization_success`
  - `async def test_lifespan_mongodb_import_error`
  - `async def test_lifespan_mongodb_connection_failure`
  - `async def test_lifespan_postgresql_cleanup_on_shutdown`
  - `async def test_lifespan_mongodb_cleanup_on_shutdown`

**摘要**：

Tests for the lifespan function and global connection pool management (Issue #778).

### `TestGlobalConnectionPoolUsage`

- **类型**：类  |  **行号**：1462–1683  |  **完整限定名**：`tests.unit.server.test_app.TestGlobalConnectionPoolUsage`
- **定义**：

```python
class TestGlobalConnectionPoolUsage:
```
- **成员概览**：

  - `async def test_astream_uses_global_postgresql_pool_when_available`
  - `async def test_astream_falls_back_to_per_request_postgresql`
  - `async def test_astream_uses_global_mongodb_pool_when_available`
  - `async def test_astream_falls_back_to_per_request_mongodb`
  - `async def _empty_async_gen`

**摘要**：

Tests for _astream_workflow_generator using global connection pools (Issue #778).

### `TestCreateEventStreamMessageThinkTagStripping`

- **类型**：类  |  **行号**：1686–1733  |  **完整限定名**：`tests.unit.server.test_app.TestCreateEventStreamMessageThinkTagStripping`
- **定义**：

```python
class TestCreateEventStreamMessageThinkTagStripping:
```
- **成员概览**：

  - `def _make_mock_chunk`
  - `def test_strips_think_tag_at_beginning`
  - `def test_strips_multiple_think_blocks`
  - `def test_preserves_content_without_think_tags`
  - `def test_empty_content_after_stripping`
  - `def test_preserves_reasoning_content_field`

**摘要**：

Tests for stripping <think> tags from streamed content (#781).

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.server.test_app import client
#
# TODO: 结合业务场景补充 client 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/server/test_chat_request.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/server/test_chat_request.py`
- **模块导入名**：`tests.unit.server.test_chat_request`
- **代码行数**：168
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.report_style import ReportStyle`
- `from src.rag.retriever import Resource`
- `from src.server.chat_request import ChatMessage, ChatRequest, ContentItem, EnhancePromptRequest, GeneratePodcastRequest, GeneratePPTRequest, GenerateProseRequest, TTSRequest`
- `import src.server.mcp_utils`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import AsyncMock, MagicMock, patch`
- `from fastapi import HTTPException`
- `from pydantic import ValidationError`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `test_content_item_text_and_image` | 25 | `()` |
| 函数 | `test_chat_message_with_string_content` | 37 | `()` |
| 函数 | `test_chat_message_with_content_items` | 43 | `()` |
| 函数 | `test_chat_request_defaults` | 51 | `()` |
| 函数 | `test_chat_request_with_values` | 67 | `()` |
| 函数 | `test_tts_request_defaults` | 99 | `()` |
| 函数 | `test_generate_podcast_request` | 112 | `()` |
| 函数 | `test_generate_ppt_request` | 117 | `()` |
| 函数 | `test_generate_prose_request` | 122 | `()` |
| 函数 | `test_enhance_prompt_request_defaults` | 132 | `()` |
| 函数 | `test_content_item_validation_error` | 139 | `()` |
| 函数 | `test_chat_message_validation_error` | 144 | `()` |
| 函数 | `test_tts_request_validation_error` | 149 | `()` |
| 异步函数 | `test_load_mcp_tools_exception_handling` | 158 | `(mock_stdio_client, mock_StdioServerParameters, mock_get_tools)` |

## 符号详解

### `test_content_item_text_and_image`

- **类型**：函数  |  **行号**：25–34  |  **完整限定名**：`tests.unit.server.test_chat_request.test_content_item_text_and_image`
- **签名**：

```python
def test_content_item_text_and_image():
```

**说明**（自动推断）：

测试用例函数 `test_content_item_text_and_image`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_chat_message_with_string_content`

- **类型**：函数  |  **行号**：37–40  |  **完整限定名**：`tests.unit.server.test_chat_request.test_chat_message_with_string_content`
- **签名**：

```python
def test_chat_message_with_string_content():
```

**说明**（自动推断）：

测试用例函数 `test_chat_message_with_string_content`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_chat_message_with_content_items`

- **类型**：函数  |  **行号**：43–48  |  **完整限定名**：`tests.unit.server.test_chat_request.test_chat_message_with_content_items`
- **签名**：

```python
def test_chat_message_with_content_items():
```

**说明**（自动推断）：

测试用例函数 `test_chat_message_with_content_items`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_chat_request_defaults`

- **类型**：函数  |  **行号**：51–64  |  **完整限定名**：`tests.unit.server.test_chat_request.test_chat_request_defaults`
- **签名**：

```python
def test_chat_request_defaults():
```

**说明**（自动推断）：

测试用例函数 `test_chat_request_defaults`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_chat_request_with_values`

- **类型**：函数  |  **行号**：67–96  |  **完整限定名**：`tests.unit.server.test_chat_request.test_chat_request_with_values`
- **签名**：

```python
def test_chat_request_with_values():
```

**说明**（自动推断）：

测试用例函数 `test_chat_request_with_values`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_tts_request_defaults`

- **类型**：函数  |  **行号**：99–109  |  **完整限定名**：`tests.unit.server.test_chat_request.test_tts_request_defaults`
- **签名**：

```python
def test_tts_request_defaults():
```

**说明**（自动推断）：

测试用例函数 `test_tts_request_defaults`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_generate_podcast_request`

- **类型**：函数  |  **行号**：112–114  |  **完整限定名**：`tests.unit.server.test_chat_request.test_generate_podcast_request`
- **签名**：

```python
def test_generate_podcast_request():
```

**说明**（自动推断）：

测试用例函数 `test_generate_podcast_request`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_generate_ppt_request`

- **类型**：函数  |  **行号**：117–119  |  **完整限定名**：`tests.unit.server.test_chat_request.test_generate_ppt_request`
- **签名**：

```python
def test_generate_ppt_request():
```

**说明**（自动推断）：

测试用例函数 `test_generate_ppt_request`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_generate_prose_request`

- **类型**：函数  |  **行号**：122–129  |  **完整限定名**：`tests.unit.server.test_chat_request.test_generate_prose_request`
- **签名**：

```python
def test_generate_prose_request():
```

**说明**（自动推断）：

测试用例函数 `test_generate_prose_request`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_enhance_prompt_request_defaults`

- **类型**：函数  |  **行号**：132–136  |  **完整限定名**：`tests.unit.server.test_chat_request.test_enhance_prompt_request_defaults`
- **签名**：

```python
def test_enhance_prompt_request_defaults():
```

**说明**（自动推断）：

测试用例函数 `test_enhance_prompt_request_defaults`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_content_item_validation_error`

- **类型**：函数  |  **行号**：139–141  |  **完整限定名**：`tests.unit.server.test_chat_request.test_content_item_validation_error`
- **签名**：

```python
def test_content_item_validation_error():
```

**说明**（自动推断）：

测试用例函数 `test_content_item_validation_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_chat_message_validation_error`

- **类型**：函数  |  **行号**：144–146  |  **完整限定名**：`tests.unit.server.test_chat_request.test_chat_message_validation_error`
- **签名**：

```python
def test_chat_message_validation_error():
```

**说明**（自动推断）：

测试用例函数 `test_chat_message_validation_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_tts_request_validation_error`

- **类型**：函数  |  **行号**：149–151  |  **完整限定名**：`tests.unit.server.test_chat_request.test_tts_request_validation_error`
- **签名**：

```python
def test_tts_request_validation_error():
```

**说明**（自动推断）：

测试用例函数 `test_tts_request_validation_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_mcp_tools_exception_handling`

- **类型**：异步函数  |  **行号**：158–168  |  **完整限定名**：`tests.unit.server.test_chat_request.test_load_mcp_tools_exception_handling`
- **装饰器**：`@pytest.mark.asyncio`, `@patch`, `@patch`, `@patch`
- **签名**：

```python
async def test_load_mcp_tools_exception_handling(mock_stdio_client, mock_StdioServerParameters, mock_get_tools):
```

**说明**（自动推断）：

测试用例函数 `test_load_mcp_tools_exception_handling`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.server.test_chat_request import test_content_item_text_and_image
#
# TODO: 结合业务场景补充 test_content_item_text_and_image 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

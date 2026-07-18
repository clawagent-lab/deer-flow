# `src/utils/json_utils.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/utils/json_utils.py`
- **模块导入名**：`src.utils.json_utils`
- **代码行数**：212
- **架构归属**：src/utils —— 通用工具（JSON 修复、日志脱敏、上下文管理）

## 模块概述

```text
JSON 与工具调用参数处理工具。

提供 ``sanitize_args``（转义 ``[] {}`` 等特殊字符以避免工具调用入参问题）、
``_extract_json_from_content``（从含冗余尾部 token 的字符串中截取最后一个
完整 JSON 对象/数组）等函数，配合 ``json_repair`` 容错解析 LLM 输出，
提升工具调用参数解析的健壮性。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any`
- `import json`
- `import logging`
- `import re`
- `import json_repair`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 20 | `logging.getLogger(__name__)` |
| 函数 | `sanitize_args` | 23 | `(args: Any) -> str` |
| 函数 | `_extract_json_from_content` | 44 | `(content: str) -> str` |
| 函数 | `repair_json_output` | 113 | `(content: str) -> str` |
| 函数 | `sanitize_tool_response` | 172 | `(content: str, max_length: int=50000) -> str` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：20–20  |  **完整限定名**：`src.utils.json_utils.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `sanitize_args`

- **类型**：函数  |  **行号**：23–41  |  **完整限定名**：`src.utils.json_utils.sanitize_args`
- **签名**：

```python
def sanitize_args(args: Any) -> str:
```

**摘要**：

Sanitize tool call arguments to prevent special character issues.

**参数**：

```text
args: Tool call arguments string
```

**返回值**：

```text
str: Sanitized arguments string
```

### `_extract_json_from_content`

- **类型**：函数  |  **行号**：44–110  |  **完整限定名**：`src.utils.json_utils._extract_json_from_content`
- **签名**：

```python
def _extract_json_from_content(content: str) -> str:
```

**摘要**：

Extract valid JSON from content that may have extra tokens.

**参数**：

```text
content: String that may contain JSON with extra tokens
```

**返回值**：

```text
String with potential JSON extracted or original content
```

### `repair_json_output`

- **类型**：函数  |  **行号**：113–169  |  **完整限定名**：`src.utils.json_utils.repair_json_output`
- **签名**：

```python
def repair_json_output(content: str) -> str:
```

**摘要**：

Repair and normalize JSON output.

**参数**：

```text
content (str): String content that may contain JSON
```

**返回值**：

```text
str: Repaired JSON string, or original content if not JSON
```

**handles**：

```text
- JSON with extra tokens after closing brackets
- Incomplete JSON structures
- Malformed JSON from quantized models
```

### `sanitize_tool_response`

- **类型**：函数  |  **行号**：172–212  |  **完整限定名**：`src.utils.json_utils.sanitize_tool_response`
- **签名**：

```python
def sanitize_tool_response(content: str, max_length: int=50000) -> str:
```

**摘要**：

Sanitize tool response to remove extra tokens and invalid content.

**参数**：

```text
content: Tool response content
    max_length: Maximum allowed length (default 50000 chars)
```

**返回值**：

```text
Sanitized content string
```

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`
- `src.podcast.graph.script_writer_node`
- `src.server.app`
- `tests.unit.utils.test_json_utils`

## 示例用法

```python
from src.utils.json_utils import sanitize_args
#
# TODO: 结合业务场景补充 sanitize_args 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

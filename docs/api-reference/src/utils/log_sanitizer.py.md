# `src/utils/log_sanitizer.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/utils/log_sanitizer.py`
- **模块导入名**：`src.utils.log_sanitizer`
- **代码行数**：186
- **架构归属**：src/utils —— 通用工具（JSON 修复、日志脱敏、上下文管理）

## 模块概述

```text
Log sanitization utilities to prevent log injection attacks.

This module provides functions to sanitize user-controlled input before
logging to prevent attackers from forging log entries through:
- Newline injection (
)
- HTML injection (for HTML logs)
- Special character sequences that could be misinterpreted
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Optional`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `sanitize_log_input` | 18 | `(value: Any, max_length: int=500) -> str` |
| 函数 | `sanitize_thread_id` | 81 | `(thread_id: Any) -> str` |
| 函数 | `sanitize_user_content` | 97 | `(content: Any) -> str` |
| 函数 | `sanitize_agent_name` | 112 | `(agent_name: Any) -> str` |
| 函数 | `sanitize_tool_name` | 127 | `(tool_name: Any) -> str` |
| 函数 | `sanitize_feedback` | 142 | `(feedback: Any) -> str` |
| 函数 | `create_safe_log_message` | 157 | `(template: str, **kwargs) -> str` |

## 符号详解

### `sanitize_log_input`

- **类型**：函数  |  **行号**：18–78  |  **完整限定名**：`src.utils.log_sanitizer.sanitize_log_input`
- **签名**：

```python
def sanitize_log_input(value: Any, max_length: int=500) -> str:
```

**摘要**：

Sanitize user-controlled input for safe logging.

**参数**：

```text
value: The input value to sanitize (any type)
        max_length: Maximum length of output string (truncates if exceeded)
```

**返回值**：

```text
str: Sanitized string safe for logging
```

**示例**：

```python
>>> sanitize_log_input("normal text")
        'normal text'

        >>> sanitize_log_input("malicious
[INFO] fake entry")
        'malicious\n[INFO] fake entry'

        >>> sanitize_log_input("tab     here")
        'tab\there'

        >>> sanitize_log_input(None)
        'None'

        >>> long_text = "a" * 1000
        >>> result = sanitize_log_input(long_text, max_length=100)
        >>> len(result) <= 100
        True
```

### `sanitize_thread_id`

- **类型**：函数  |  **行号**：81–94  |  **完整限定名**：`src.utils.log_sanitizer.sanitize_thread_id`
- **签名**：

```python
def sanitize_thread_id(thread_id: Any) -> str:
```

**摘要**：

Sanitize thread_id for logging.

**参数**：

```text
thread_id: The thread ID to sanitize
```

**返回值**：

```text
str: Sanitized thread ID
```

### `sanitize_user_content`

- **类型**：函数  |  **行号**：97–109  |  **完整限定名**：`src.utils.log_sanitizer.sanitize_user_content`
- **签名**：

```python
def sanitize_user_content(content: Any) -> str:
```

**摘要**：

Sanitize user-provided message content for logging.

**参数**：

```text
content: The user content to sanitize
```

**返回值**：

```text
str: Sanitized user content
```

### `sanitize_agent_name`

- **类型**：函数  |  **行号**：112–124  |  **完整限定名**：`src.utils.log_sanitizer.sanitize_agent_name`
- **签名**：

```python
def sanitize_agent_name(agent_name: Any) -> str:
```

**摘要**：

Sanitize agent name for logging.

**参数**：

```text
agent_name: The agent name to sanitize
```

**返回值**：

```text
str: Sanitized agent name
```

### `sanitize_tool_name`

- **类型**：函数  |  **行号**：127–139  |  **完整限定名**：`src.utils.log_sanitizer.sanitize_tool_name`
- **签名**：

```python
def sanitize_tool_name(tool_name: Any) -> str:
```

**摘要**：

Sanitize tool name for logging.

**参数**：

```text
tool_name: The tool name to sanitize
```

**返回值**：

```text
str: Sanitized tool name
```

### `sanitize_feedback`

- **类型**：函数  |  **行号**：142–154  |  **完整限定名**：`src.utils.log_sanitizer.sanitize_feedback`
- **签名**：

```python
def sanitize_feedback(feedback: Any) -> str:
```

**摘要**：

Sanitize user feedback for logging.

**参数**：

```text
feedback: The feedback to sanitize
```

**返回值**：

```text
str: Sanitized feedback (truncated more aggressively)
```

### `create_safe_log_message`

- **类型**：函数  |  **行号**：157–186  |  **完整限定名**：`src.utils.log_sanitizer.create_safe_log_message`
- **签名**：

```python
def create_safe_log_message(template: str, **kwargs) -> str:
```

**摘要**：

Create a safe log message by sanitizing all values.

**参数**：

```text
template: Template string with {key} placeholders
    **kwargs: Key-value pairs to substitute
```

**返回值**：

```text
str: Safe log message
```

**示例**：

```python
>>> msg = create_safe_log_message(
    ...     "[{thread_id}] Processing {tool_name}",
    ...     thread_id="abc\n[INFO]",
    ...     tool_name="my_tool"
    ... )
    >>> "[abc\\n[INFO]] Processing my_tool" in msg
    True
```

## 调用关系（下游）

**被以下模块导入**：

- `src.agents.tool_interceptor`
- `src.server.app`
- `tests.unit.utils.test_log_sanitizer`

## 示例用法

```python
from src.utils.log_sanitizer import sanitize_log_input
#
# TODO: 结合业务场景补充 sanitize_log_input 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

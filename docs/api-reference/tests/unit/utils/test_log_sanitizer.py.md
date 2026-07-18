# `tests/unit/utils/test_log_sanitizer.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/utils/test_log_sanitizer.py`
- **模块导入名**：`tests.unit.utils.test_log_sanitizer`
- **代码行数**：268
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for log sanitization utilities.

This test file verifies that the log sanitizer properly prevents log injection attacks
by escaping dangerous characters in user-controlled input before logging.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.utils.log_sanitizer import create_safe_log_message, sanitize_agent_name, sanitize_feedback, sanitize_log_input, sanitize_thread_id, sanitize_tool_name, sanitize_user_content`

**外部依赖**（第三方库 / 标准库）：

- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestSanitizeLogInput` | 24 | `` |
| 类 | `TestSanitizeThreadId` | 104 | `` |
| 类 | `TestSanitizeUserContent` | 127 | `` |
| 类 | `TestSanitizeToolName` | 150 | `` |
| 类 | `TestSanitizeFeedback` | 166 | `` |
| 类 | `TestCreateSafeLogMessage` | 189 | `` |
| 类 | `TestLogInjectionAttackPrevention` | 226 | `` |

## 符号详解

### `TestSanitizeLogInput`

- **类型**：类  |  **行号**：24–101  |  **完整限定名**：`tests.unit.utils.test_log_sanitizer.TestSanitizeLogInput`
- **定义**：

```python
class TestSanitizeLogInput:
```
- **成员概览**：

  - `def test_sanitize_normal_text`
  - `def test_sanitize_newline_injection`
  - `def test_sanitize_carriage_return`
  - `def test_sanitize_tab_character`
  - `def test_sanitize_null_character`
  - `def test_sanitize_backslash`
  - `def test_sanitize_escape_character`
  - `def test_sanitize_max_length_truncation`
  - `def test_sanitize_none_value`
  - `def test_sanitize_numeric_value`
  - `def test_sanitize_complex_injection_attack`

**摘要**：

Test the main sanitize_log_input function.

### `TestSanitizeThreadId`

- **类型**：类  |  **行号**：104–124  |  **完整限定名**：`tests.unit.utils.test_log_sanitizer.TestSanitizeThreadId`
- **定义**：

```python
class TestSanitizeThreadId:
```
- **成员概览**：

  - `def test_thread_id_normal`
  - `def test_thread_id_with_newline`
  - `def test_thread_id_max_length`

**摘要**：

Test sanitization of thread IDs.

### `TestSanitizeUserContent`

- **类型**：类  |  **行号**：127–147  |  **完整限定名**：`tests.unit.utils.test_log_sanitizer.TestSanitizeUserContent`
- **定义**：

```python
class TestSanitizeUserContent:
```
- **成员概览**：

  - `def test_user_content_normal`
  - `def test_user_content_with_newline`
  - `def test_user_content_max_length`

**摘要**：

Test sanitization of user-provided message content.

### `TestSanitizeToolName`

- **类型**：类  |  **行号**：150–163  |  **完整限定名**：`tests.unit.utils.test_log_sanitizer.TestSanitizeToolName`
- **定义**：

```python
class TestSanitizeToolName:
```
- **成员概览**：

  - `def test_tool_name_normal`
  - `def test_tool_name_injection`

**摘要**：

Test sanitization of tool names.

### `TestSanitizeFeedback`

- **类型**：类  |  **行号**：166–186  |  **完整限定名**：`tests.unit.utils.test_log_sanitizer.TestSanitizeFeedback`
- **定义**：

```python
class TestSanitizeFeedback:
```
- **成员概览**：

  - `def test_feedback_normal`
  - `def test_feedback_injection`
  - `def test_feedback_max_length`

**摘要**：

Test sanitization of user feedback.

### `TestCreateSafeLogMessage`

- **类型**：类  |  **行号**：189–223  |  **完整限定名**：`tests.unit.utils.test_log_sanitizer.TestCreateSafeLogMessage`
- **定义**：

```python
class TestCreateSafeLogMessage:
```
- **成员概览**：

  - `def test_safe_message_normal`
  - `def test_safe_message_with_injection`
  - `def test_safe_message_multiple_values`

**摘要**：

Test the create_safe_log_message helper function.

### `TestLogInjectionAttackPrevention`

- **类型**：类  |  **行号**：226–268  |  **完整限定名**：`tests.unit.utils.test_log_sanitizer.TestLogInjectionAttackPrevention`
- **定义**：

```python
class TestLogInjectionAttackPrevention:
```
- **成员概览**：

  - `def test_classic_log_injection_newline`
  - `def test_carriage_return_log_injection`
  - `def test_html_injection_prevention`
  - `def test_multiple_injection_techniques`

**摘要**：

Integration tests for log injection prevention.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.utils.test_log_sanitizer import TestSanitizeLogInput
#
# TODO: 结合业务场景补充 TestSanitizeLogInput 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

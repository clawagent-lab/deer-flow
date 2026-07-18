# `tests/integration/test_tool_interceptor_integration.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/integration/test_tool_interceptor_integration.py`
- **模块导入名**：`tests.integration.test_tool_interceptor_integration`
- **代码行数**：473
- **架构归属**：tests/integration —— 集成测试（跨组件 / 外部服务，如 crawler、nodes、template、tts）

## 模块概述

```text
Integration tests for tool-specific interrupts feature (Issue #572).

Tests the complete flow of selective tool interrupts including:
- Tool wrapping with interrupt logic
- Agent creation with interrupt configuration
- Tool execution with user feedback
- Resume mechanism after interrupt
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.agents.agents import create_agent`
- `from src.agents.tool_interceptor import ToolInterceptor, wrap_tools_with_interceptor`
- `from src.config.configuration import Configuration`
- `from src.server.chat_request import ChatRequest`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any`
- `from unittest.mock import AsyncMock, MagicMock, Mock, call, patch`
- `from langchain_core.messages import HumanMessage`
- `from langchain_core.tools import tool`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestToolInterceptorIntegration` | 27 | `` |

## 符号详解

### `TestToolInterceptorIntegration`

- **类型**：类  |  **行号**：27–473  |  **完整限定名**：`tests.integration.test_tool_interceptor_integration.TestToolInterceptorIntegration`
- **定义**：

```python
class TestToolInterceptorIntegration:
```
- **成员概览**：

  - `def test_agent_creation_with_tool_interrupts`
  - `def test_configuration_with_tool_interrupts`
  - `def test_configuration_default_no_interrupts`
  - `def test_chat_request_with_tool_interrupts`
  - `def test_chat_request_interrupt_feedback_with_tool_interrupts`
  - `def test_multiple_tools_selective_interrupt`
  - `def test_interrupt_with_user_approval`
  - `def test_interrupt_with_user_rejection`
  - `def test_interrupt_message_contains_tool_info`
  - `def test_tool_wrapping_preserves_functionality`
  - `def test_tool_wrapping_preserves_tool_metadata`
  - `def test_multiple_interrupts_in_sequence`
  - `def test_empty_interrupt_list_no_interrupts`
  - `def test_none_interrupt_list_no_interrupts`
  - `def test_case_sensitive_tool_name_matching`
  - `def test_tool_error_handling`
  - `def test_approval_keywords_comprehensive`
  - `def test_rejection_keywords_comprehensive`
  - `def test_interrupt_with_complex_tool_input`
  - `def test_configuration_from_runnable_config`
  - `def test_tool_interceptor_initialization_logging`
  - `def test_wrap_tools_with_interceptor_logging`
  - `def test_interrupt_resolution_with_empty_feedback`
  - `def test_interrupt_resolution_with_none_feedback`

**摘要**：

Integration tests for tool interceptor with agent workflow.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.integration.test_tool_interceptor_integration import TestToolInterceptorIntegration
#
# TODO: 结合业务场景补充 TestToolInterceptorIntegration 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

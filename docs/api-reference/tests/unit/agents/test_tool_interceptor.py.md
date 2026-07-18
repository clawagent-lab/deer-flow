# `tests/unit/agents/test_tool_interceptor.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/agents/test_tool_interceptor.py`
- **模块导入名**：`tests.unit.agents.test_tool_interceptor`
- **代码行数**：434
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.agents.tool_interceptor import ToolInterceptor, wrap_tools_with_interceptor`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import AsyncMock, MagicMock, Mock, patch`
- `from langchain_core.tools import BaseTool, tool`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestToolInterceptor` | 15 | `` |
| 类 | `TestFormatToolInput` | 219 | `` |

## 符号详解

### `TestToolInterceptor`

- **类型**：类  |  **行号**：15–216  |  **完整限定名**：`tests.unit.agents.test_tool_interceptor.TestToolInterceptor`
- **定义**：

```python
class TestToolInterceptor:
```
- **成员概览**：

  - `def test_init_with_tools`
  - `def test_init_without_tools`
  - `def test_should_interrupt_with_matching_tool`
  - `def test_should_interrupt_with_non_matching_tool`
  - `def test_should_interrupt_empty_list`
  - `def test_parse_approval_with_approval_keywords`
  - `def test_parse_approval_case_insensitive`
  - `def test_parse_approval_with_surrounding_text`
  - `def test_parse_approval_rejection`
  - `def test_parse_approval_empty_string`
  - `def test_parse_approval_none`
  - `def test_wrap_tool_with_interrupt`
  - `def test_wrap_tool_without_interrupt`
  - `def test_wrap_tool_user_rejects`
  - `def test_wrap_tools_with_interceptor_empty_list`
  - `def test_wrap_tools_with_interceptor_none`
  - `def test_wrap_tools_with_interceptor_multiple`
  - `def test_wrap_tool_preserves_tool_properties`

**摘要**：

Tests for ToolInterceptor class.

### `TestFormatToolInput`

- **类型**：类  |  **行号**：219–434  |  **完整限定名**：`tests.unit.agents.test_tool_interceptor.TestFormatToolInput`
- **定义**：

```python
class TestFormatToolInput:
```
- **成员概览**：

  - `def test_format_tool_input_none`
  - `def test_format_tool_input_string`
  - `def test_format_tool_input_simple_dict`
  - `def test_format_tool_input_nested_dict`
  - `def test_format_tool_input_list`
  - `def test_format_tool_input_complex_list`
  - `def test_format_tool_input_tuple`
  - `def test_format_tool_input_integer`
  - `def test_format_tool_input_float`
  - `def test_format_tool_input_boolean`
  - `def test_format_tool_input_deeply_nested`
  - `def test_format_tool_input_empty_dict`
  - `def test_format_tool_input_empty_list`
  - `def test_format_tool_input_special_characters`
  - `def test_format_tool_input_numbers_as_strings`
  - `def test_format_tool_input_with_none_values`
  - `def test_format_tool_input_indentation`
  - `def test_format_tool_input_preserves_order_insertion`
  - `def test_format_tool_input_long_strings`
  - `def test_format_tool_input_mixed_types_in_list`

**摘要**：

Tests for tool input formatting functionality.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.agents.test_tool_interceptor import TestToolInterceptor
#
# TODO: 结合业务场景补充 TestToolInterceptor 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

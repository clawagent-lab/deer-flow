# `tests/unit/graph/test_nodes_recursion_limit.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/graph/test_nodes_recursion_limit.py`
- **模块导入名**：`tests.unit.graph.test_nodes_recursion_limit`
- **代码行数**：623
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for recursion limit fallback functionality in graph nodes.

Tests the graceful fallback behavior when agents hit the recursion limit,
including the _handle_recursion_limit_fallback function and the
enable_recursion_fallback configuration option.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.configuration import Configuration`
- `from src.graph.nodes import _handle_recursion_limit_fallback`
- `from src.graph.types import State`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `from langchain_core.messages import AIMessage, HumanMessage`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestHandleRecursionLimitFallback` | 22 | `` |
| 类 | `TestRecursionFallbackConfiguration` | 375 | `` |
| 类 | `TestRecursionFallbackIntegration` | 457 | `` |
| 类 | `TestRecursionFallbackEdgeCases` | 502 | `` |

## 符号详解

### `TestHandleRecursionLimitFallback`

- **类型**：类  |  **行号**：22–372  |  **完整限定名**：`tests.unit.graph.test_nodes_recursion_limit.TestHandleRecursionLimitFallback`
- **定义**：

```python
class TestHandleRecursionLimitFallback:
```
- **成员概览**：

  - `async def test_fallback_generates_summary_from_observations`
  - `async def test_fallback_applies_prompt_template`
  - `async def test_fallback_gets_llm_without_tools`
  - `async def test_fallback_sanitizes_response`
  - `async def test_fallback_preserves_meta_fields`
  - `async def test_fallback_raises_on_llm_failure`
  - `async def test_fallback_handles_different_agent_types`
  - `async def test_fallback_uses_partial_agent_messages`
  - `async def test_fallback_handles_empty_partial_messages`

**摘要**：

Test suite for _handle_recursion_limit_fallback() function.

### `TestRecursionFallbackConfiguration`

- **类型**：类  |  **行号**：375–454  |  **完整限定名**：`tests.unit.graph.test_nodes_recursion_limit.TestRecursionFallbackConfiguration`
- **定义**：

```python
class TestRecursionFallbackConfiguration:
```
- **成员概览**：

  - `def test_config_default_is_enabled`
  - `def test_config_from_env_variable_true`
  - `def test_config_from_env_variable_false`
  - `def test_config_from_env_variable_1`
  - `def test_config_from_env_variable_0`
  - `def test_config_from_env_variable_yes`
  - `def test_config_from_env_variable_no`
  - `def test_config_from_runnable_config`
  - `def test_config_field_exists`

**摘要**：

Test suite for enable_recursion_fallback configuration.

### `TestRecursionFallbackIntegration`

- **类型**：类  |  **行号**：457–499  |  **完整限定名**：`tests.unit.graph.test_nodes_recursion_limit.TestRecursionFallbackIntegration`
- **定义**：

```python
class TestRecursionFallbackIntegration:
```
- **成员概览**：

  - `async def test_fallback_function_signature_returns_list`
  - `async def test_configuration_enables_disables_fallback`

**摘要**：

Integration tests for recursion fallback in agent execution.

### `TestRecursionFallbackEdgeCases`

- **类型**：类  |  **行号**：502–623  |  **完整限定名**：`tests.unit.graph.test_nodes_recursion_limit.TestRecursionFallbackEdgeCases`
- **定义**：

```python
class TestRecursionFallbackEdgeCases:
```
- **成员概览**：

  - `async def test_fallback_with_empty_observations`
  - `async def test_fallback_with_very_long_recursion_limit`
  - `async def test_fallback_with_unicode_locale`
  - `async def test_fallback_with_none_locale`

**摘要**：

Test edge cases and boundary conditions for recursion fallback.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.graph.test_nodes_recursion_limit import TestHandleRecursionLimitFallback
#
# TODO: 结合业务场景补充 TestHandleRecursionLimitFallback 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/agents/test_middleware.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/agents/test_middleware.py`
- **模块导入名**：`tests.unit.agents.test_middleware`
- **代码行数**：335
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.agents.agents import DynamicPromptMiddleware, PreModelHookMiddleware`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import AsyncMock, MagicMock, Mock, patch`
- `from langchain_core.messages import HumanMessage, SystemMessage`
- `import asyncio`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `mock_runtime` | 14 | `()` |
| 函数 | `mock_state` | 22 | `()` |
| 函数 | `mock_messages` | 31 | `()` |
| 类 | `TestDynamicPromptMiddleware` | 39 | `` |
| 类 | `TestPreModelHookMiddleware` | 153 | `` |

## 符号详解

### `mock_runtime`

- **类型**：函数  |  **行号**：14–18  |  **完整限定名**：`tests.unit.agents.test_middleware.mock_runtime`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_runtime():
```

**摘要**：

Mock Runtime object.

### `mock_state`

- **类型**：函数  |  **行号**：22–27  |  **完整限定名**：`tests.unit.agents.test_middleware.mock_state`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state():
```

**摘要**：

Mock state object.

### `mock_messages`

- **类型**：函数  |  **行号**：31–36  |  **完整限定名**：`tests.unit.agents.test_middleware.mock_messages`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_messages():
```

**摘要**：

Mock messages returned by apply_prompt_template.

### `TestDynamicPromptMiddleware`

- **类型**：类  |  **行号**：39–150  |  **完整限定名**：`tests.unit.agents.test_middleware.TestDynamicPromptMiddleware`
- **定义**：

```python
class TestDynamicPromptMiddleware:
```
- **成员概览**：

  - `def test_init`
  - `def test_init_default_locale`
  - `def test_before_model_success`
  - `def test_before_model_empty_messages`
  - `def test_before_model_none_messages`
  - `def test_before_model_exception_handling`
  - `def test_before_model_with_different_locale`
  - `async def test_abefore_model`

**摘要**：

Tests for DynamicPromptMiddleware class.

### `TestPreModelHookMiddleware`

- **类型**：类  |  **行号**：153–335  |  **完整限定名**：`tests.unit.agents.test_middleware.TestPreModelHookMiddleware`
- **定义**：

```python
class TestPreModelHookMiddleware:
```
- **成员概览**：

  - `def test_init`
  - `def test_before_model_with_sync_hook`
  - `def test_before_model_with_none_hook`
  - `def test_before_model_hook_returns_none`
  - `def test_before_model_hook_exception`
  - `async def test_abefore_model_with_async_hook`
  - `async def test_abefore_model_with_sync_hook`
  - `async def test_abefore_model_with_none_hook`
  - `async def test_abefore_model_async_hook_exception`
  - `async def test_abefore_model_sync_hook_exception`
  - `async def test_abefore_model_sync_hook_actual_execution`
  - `async def test_abefore_model_detects_coroutine_function`

**摘要**：

Tests for PreModelHookMiddleware class.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.agents.test_middleware import mock_runtime
#
# TODO: 结合业务场景补充 mock_runtime 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

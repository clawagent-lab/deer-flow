# `tests/unit/graph/test_agent_locale_restoration.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/graph/test_agent_locale_restoration.py`
- **模块导入名**：`tests.unit.graph.test_agent_locale_restoration`
- **代码行数**：241
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for agent locale restoration after agent execution.

Tests that meta fields (especially locale) are properly restored after
agent.ainvoke() returns, since the agent creates a MessagesState
subgraph that filters out custom fields.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.graph.nodes import preserve_state_meta_fields`
- `from src.graph.types import State`

**外部依赖**（第三方库 / 标准库）：

- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestAgentLocaleRestoration` | 18 | `` |
| 类 | `TestAgentLocaleRestorationScenarios` | 179 | `` |

## 符号详解

### `TestAgentLocaleRestoration`

- **类型**：类  |  **行号**：18–176  |  **完整限定名**：`tests.unit.graph.test_agent_locale_restoration.TestAgentLocaleRestoration`
- **定义**：

```python
class TestAgentLocaleRestoration:
```
- **成员概览**：

  - `def test_locale_lost_in_agent_subgraph`
  - `def test_locale_restoration_after_agent`
  - `def test_all_meta_fields_restored`
  - `def test_locale_preservation_through_agent_cycle`
  - `def test_locale_not_auto_after_restoration`
  - `def test_chinese_locale_preserved`
  - `def test_restoration_with_new_messages`
  - `def test_restoration_idempotent`

**摘要**：

Test suite for locale restoration after agent execution.

### `TestAgentLocaleRestorationScenarios`

- **类型**：类  |  **行号**：179–241  |  **完整限定名**：`tests.unit.graph.test_agent_locale_restoration.TestAgentLocaleRestorationScenarios`
- **定义**：

```python
class TestAgentLocaleRestorationScenarios:
```
- **成员概览**：

  - `def test_researcher_agent_preserves_locale`
  - `def test_coder_agent_preserves_locale`
  - `def test_locale_persists_across_multiple_agents`

**摘要**：

Real-world scenario tests for agent locale restoration.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.graph.test_agent_locale_restoration import TestAgentLocaleRestoration
#
# TODO: 结合业务场景补充 TestAgentLocaleRestoration 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

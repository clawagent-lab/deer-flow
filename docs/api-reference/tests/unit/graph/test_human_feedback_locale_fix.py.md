# `tests/unit/graph/test_human_feedback_locale_fix.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/graph/test_human_feedback_locale_fix.py`
- **模块导入名**：`tests.unit.graph.test_human_feedback_locale_fix`
- **代码行数**：317
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for the human_feedback_node locale fix.

Tests that the duplicate locale assignment issue is resolved:
- Locale is safely retrieved from new_plan using .get() with fallback
- If new_plan['locale'] doesn't exist, it doesn't cause a KeyError
- If new_plan['locale'] is None or empty, the preserved state locale is used
- If new_plan['locale'] has a valid value, it properly overrides the state locale
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.graph.nodes import preserve_state_meta_fields`
- `from src.graph.types import State`
- `from src.prompts.planner_model import Plan`

**外部依赖**（第三方库 / 标准库）：

- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestHumanFeedbackLocaleFixture` | 21 | `` |
| 类 | `TestHumanFeedbackLocaleScenarios` | 233 | `` |

## 符号详解

### `TestHumanFeedbackLocaleFixture`

- **类型**：类  |  **行号**：21–230  |  **完整限定名**：`tests.unit.graph.test_human_feedback_locale_fix.TestHumanFeedbackLocaleFixture`
- **定义**：

```python
class TestHumanFeedbackLocaleFixture:
```
- **成员概览**：

  - `def test_preserve_state_meta_fields_no_keyerror`
  - `def test_new_plan_without_locale_override`
  - `def test_new_plan_with_none_locale`
  - `def test_new_plan_with_empty_string_locale`
  - `def test_new_plan_with_valid_locale_overrides`
  - `def test_locale_field_not_duplicated`
  - `def test_all_meta_fields_preserved`

**摘要**：

Test suite for human_feedback_node locale safe handling.

### `TestHumanFeedbackLocaleScenarios`

- **类型**：类  |  **行号**：233–317  |  **完整限定名**：`tests.unit.graph.test_human_feedback_locale_fix.TestHumanFeedbackLocaleScenarios`
- **定义**：

```python
class TestHumanFeedbackLocaleScenarios:
```
- **成员概览**：

  - `def test_scenario_chinese_locale_preserved_when_plan_has_no_locale`
  - `def test_scenario_en_us_restored_even_if_plan_minimal`
  - `def test_scenario_multiple_locale_updates_safe`

**摘要**：

Real-world scenarios for human_feedback_node locale handling.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.graph.test_human_feedback_locale_fix import TestHumanFeedbackLocaleFixture
#
# TODO: 结合业务场景补充 TestHumanFeedbackLocaleFixture 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

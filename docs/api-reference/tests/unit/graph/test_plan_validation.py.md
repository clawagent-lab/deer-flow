# `tests/unit/graph/test_plan_validation.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/graph/test_plan_validation.py`
- **模块导入名**：`tests.unit.graph.test_plan_validation`
- **代码行数**：491
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.graph.nodes import validate_and_fix_plan`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestValidateAndFixPlanStepTypeRepair` | 11 | `` |
| 类 | `TestValidateAndFixPlanWebSearchEnforcement` | 214 | `` |
| 类 | `TestValidateAndFixPlanIntegration` | 308 | `` |
| 类 | `TestValidateAndFixPlanIssue650` | 370 | `` |

## 符号详解

### `TestValidateAndFixPlanStepTypeRepair`

- **类型**：类  |  **行号**：11–211  |  **完整限定名**：`tests.unit.graph.test_plan_validation.TestValidateAndFixPlanStepTypeRepair`
- **定义**：

```python
class TestValidateAndFixPlanStepTypeRepair:
```
- **成员概览**：

  - `def test_repair_missing_step_type_with_need_search_true`
  - `def test_repair_missing_step_type_with_need_search_false`
  - `def test_repair_missing_step_type_default_to_analysis`
  - `def test_repair_empty_step_type_field`
  - `def test_repair_null_step_type_field`
  - `def test_multiple_steps_with_mixed_missing_step_types`
  - `def test_preserve_explicit_step_type`
  - `def test_repair_logs_warning`
  - `def test_non_dict_plan_returns_unchanged`
  - `def test_plan_with_non_dict_step_skipped`
  - `def test_empty_steps_list`
  - `def test_missing_steps_key`

**摘要**：

Test step_type field repair logic (Issue #650 fix).

### `TestValidateAndFixPlanWebSearchEnforcement`

- **类型**：类  |  **行号**：214–305  |  **完整限定名**：`tests.unit.graph.test_plan_validation.TestValidateAndFixPlanWebSearchEnforcement`
- **定义**：

```python
class TestValidateAndFixPlanWebSearchEnforcement:
```
- **成员概览**：

  - `def test_enforce_web_search_sets_first_research_step`
  - `def test_enforce_web_search_converts_first_step`
  - `def test_enforce_web_search_with_existing_search_step`
  - `def test_enforce_web_search_adds_default_step`
  - `def test_enforce_web_search_without_steps_key`

**摘要**：

Test web search enforcement logic.

### `TestValidateAndFixPlanIntegration`

- **类型**：类  |  **行号**：308–368  |  **完整限定名**：`tests.unit.graph.test_plan_validation.TestValidateAndFixPlanIntegration`
- **定义**：

```python
class TestValidateAndFixPlanIntegration:
```
- **成员概览**：

  - `def test_repair_and_enforce_together`
  - `def test_repair_then_enforce_cascade`

**摘要**：

Integration tests for step_type repair and web search enforcement together.

### `TestValidateAndFixPlanIssue650`

- **类型**：类  |  **行号**：370–491  |  **完整限定名**：`tests.unit.graph.test_plan_validation.TestValidateAndFixPlanIssue650`
- **定义**：

```python
class TestValidateAndFixPlanIssue650:
```
- **成员概览**：

  - `def test_issue_650_water_footprint_scenario_fixed`
  - `def test_issue_650_scenario_passes_pydantic_validation`
  - `def test_issue_650_multiple_validation_errors_fixed`
  - `def test_issue_650_no_exceptions_raised`

**摘要**：

Specific tests for Issue #650 scenarios.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.graph.test_plan_validation import TestValidateAndFixPlanStepTypeRepair
#
# TODO: 结合业务场景补充 TestValidateAndFixPlanStepTypeRepair 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/eval/test_evaluator.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/eval/test_evaluator.py`
- **模块导入名**：`tests.unit.eval.test_evaluator`
- **代码行数**：489
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for the combined report evaluator.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.eval.evaluator import CombinedEvaluation, ReportEvaluator, score_to_grade`
- `from src.eval.llm_judge import EVALUATION_CRITERIA, MAX_REPORT_LENGTH, EvaluationResult, LLMJudge`
- `from src.eval.metrics import ReportMetrics`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import AsyncMock, MagicMock`
- `import json`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestScoreToGrade` | 21 | `` |
| 类 | `TestReportEvaluator` | 51 | `` |
| 类 | `TestReportEvaluatorIntegration` | 173 | `` |
| 类 | `TestLLMJudgeParseResponse` | 203 | `` |
| 类 | `TestLLMJudgeCalculateWeightedScore` | 280 | `` |
| 类 | `TestLLMJudgeEvaluate` | 345 | `` |
| 类 | `TestEvaluationResult` | 468 | `` |

## 符号详解

### `TestScoreToGrade`

- **类型**：类  |  **行号**：21–48  |  **完整限定名**：`tests.unit.eval.test_evaluator.TestScoreToGrade`
- **定义**：

```python
class TestScoreToGrade:
```
- **成员概览**：

  - `def test_excellent_scores`
  - `def test_good_scores`
  - `def test_average_scores`
  - `def test_poor_scores`

**摘要**：

Tests for score to grade conversion.

### `TestReportEvaluator`

- **类型**：类  |  **行号**：51–170  |  **完整限定名**：`tests.unit.eval.test_evaluator.TestReportEvaluator`
- **定义**：

```python
class TestReportEvaluator:
```
- **成员概览**：

  - `def evaluator`
  - `def sample_report`
  - `def test_evaluate_metrics_only`
  - `def test_evaluate_metrics_only_structure`
  - `def test_evaluate_minimal_report`
  - `def test_metrics_score_calculation`
  - `def test_combined_evaluation_to_dict`

**摘要**：

Tests for ReportEvaluator class.

### `TestReportEvaluatorIntegration`

- **类型**：类  |  **行号**：173–200  |  **完整限定名**：`tests.unit.eval.test_evaluator.TestReportEvaluatorIntegration`
- **定义**：

```python
class TestReportEvaluatorIntegration:
```
- **成员概览**：

  - `async def test_full_evaluation_without_llm`

**摘要**：

Integration tests for evaluator (may require LLM).

### `TestLLMJudgeParseResponse`

- **类型**：类  |  **行号**：203–277  |  **完整限定名**：`tests.unit.eval.test_evaluator.TestLLMJudgeParseResponse`
- **定义**：

```python
class TestLLMJudgeParseResponse:
```
- **成员概览**：

  - `def judge`
  - `def valid_response_data`
  - `def test_parse_valid_json`
  - `def test_parse_json_in_markdown_block`
  - `def test_parse_json_in_generic_code_block`
  - `def test_parse_malformed_json_returns_defaults`
  - `def test_parse_incomplete_json`
  - `def test_parse_json_with_extra_text`

**摘要**：

Tests for LLMJudge._parse_response method.

### `TestLLMJudgeCalculateWeightedScore`

- **类型**：类  |  **行号**：280–342  |  **完整限定名**：`tests.unit.eval.test_evaluator.TestLLMJudgeCalculateWeightedScore`
- **定义**：

```python
class TestLLMJudgeCalculateWeightedScore:
```
- **成员概览**：

  - `def judge`
  - `def test_calculate_with_all_scores`
  - `def test_calculate_with_varied_scores`
  - `def test_calculate_with_partial_scores`
  - `def test_calculate_with_unknown_criteria`
  - `def test_calculate_with_empty_scores`
  - `def test_weights_sum_to_one`

**摘要**：

Tests for LLMJudge._calculate_weighted_score method.

### `TestLLMJudgeEvaluate`

- **类型**：类  |  **行号**：345–465  |  **完整限定名**：`tests.unit.eval.test_evaluator.TestLLMJudgeEvaluate`
- **定义**：

```python
class TestLLMJudgeEvaluate:
```
- **成员概览**：

  - `def valid_llm_response`
  - `async def test_successful_evaluation`
  - `async def test_evaluation_with_llm_failure`
  - `async def test_evaluation_with_malformed_response`
  - `async def test_evaluation_passes_report_style`
  - `async def test_evaluation_truncates_long_reports`

**摘要**：

Tests for LLMJudge.evaluate method with mocked LLM.

### `TestEvaluationResult`

- **类型**：类  |  **行号**：468–489  |  **完整限定名**：`tests.unit.eval.test_evaluator.TestEvaluationResult`
- **定义**：

```python
class TestEvaluationResult:
```
- **成员概览**：

  - `def test_to_dict`

**摘要**：

Tests for EvaluationResult dataclass.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.eval.test_evaluator import TestScoreToGrade
#
# TODO: 结合业务场景补充 TestScoreToGrade 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

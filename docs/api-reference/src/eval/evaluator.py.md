# `src/eval/evaluator.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/eval/evaluator.py`
- **模块导入名**：`src.eval.evaluator`
- **代码行数**：249
- **架构归属**：src/eval —— 报告评估：自动化指标（字数/引用/章节覆盖）+ LLM-as-Judge 综合评分

## 模块概述

```text
Combined report evaluator orchestrating both automated metrics and LLM evaluation.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .llm_judge import EvaluationResult, LLMJudge`
- `from .metrics import ReportMetrics, compute_metrics, get_word_count_target`

**外部依赖**（第三方库 / 标准库）：

- `from dataclasses import dataclass`
- `from typing import Any, Dict, Optional`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 15 | `logging.getLogger(__name__)` |
| 类 | `CombinedEvaluation` | 19 | `` |
| 函数 | `score_to_grade` | 41 | `(score: float) -> str` |
| 类 | `ReportEvaluator` | 67 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：15–15  |  **完整限定名**：`src.eval.evaluator.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `CombinedEvaluation`

- **类型**：类  |  **行号**：19–38  |  **完整限定名**：`src.eval.evaluator.CombinedEvaluation`
- **装饰器**：`@dataclass`
- **定义**：

```python
class CombinedEvaluation:
```
- **成员概览**：

  - `attr metrics`
  - `attr llm_evaluation`
  - `attr final_score`
  - `attr grade`
  - `attr summary`
  - `def to_dict`

**摘要**：

Combined evaluation results from metrics and LLM judge.

### `score_to_grade`

- **类型**：函数  |  **行号**：41–64  |  **完整限定名**：`src.eval.evaluator.score_to_grade`
- **签名**：

```python
def score_to_grade(score: float) -> str:
```

**摘要**：

Convert numeric score to letter grade.

### `ReportEvaluator`

- **类型**：类  |  **行号**：67–249  |  **完整限定名**：`src.eval.evaluator.ReportEvaluator`
- **定义**：

```python
class ReportEvaluator:
```
- **成员概览**：

  - `def __init__`
  - `def _compute_metrics_score`
  - `def _generate_summary`
  - `async def evaluate`
  - `def evaluate_sync`
  - `def evaluate_metrics_only`

**摘要**：

Combined report evaluator using both automated metrics and LLM-as-Judge.

## 调用关系（下游）

**被以下模块导入**：

- `src.eval`
- `tests.unit.eval.test_evaluator`

## 示例用法

```python
from src.eval.evaluator import score_to_grade
#
# TODO: 结合业务场景补充 score_to_grade 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

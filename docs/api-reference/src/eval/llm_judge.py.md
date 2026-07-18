# `src/eval/llm_judge.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/eval/llm_judge.py`
- **模块导入名**：`src.eval.llm_judge`
- **代码行数**：282
- **架构归属**：src/eval —— 报告评估：自动化指标（字数/引用/章节覆盖）+ LLM-as-Judge 综合评分

## 模块概述

```text
LLM-as-Judge evaluation for report quality.

Uses an LLM to evaluate reports on multiple quality dimensions,
providing more nuanced assessment than automated metrics alone.
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from dataclasses import dataclass`
- `from typing import Any, Dict, List, Optional`
- `from langchain_core.messages import HumanMessage, SystemMessage`
- `import json`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 18 | `logging.getLogger(__name__)` |
| 常量 | `MAX_REPORT_LENGTH` | 22 | `15000` |
| 常量 | `EVALUATION_CRITERIA` | 24 | `{'factual_accuracy': {'description': 'Are claims supported by cited sources? Is information accur...` |
| 常量 | `JUDGE_SYSTEM_PROMPT` | 51 | `'You are an expert report quality evaluator. Your task is to objectively assess the quality of re...` |
| 类 | `EvaluationResult` | 82 | `` |
| 类 | `LLMJudge` | 105 | `` |
| 异步函数 | `evaluate_with_llm` | 263 | `(report: str, query: str, report_style: str='default', llm: Any=None) -> EvaluationResult` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：18–18  |  **完整限定名**：`src.eval.llm_judge.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `MAX_REPORT_LENGTH`

- **类型**：模块常量  |  **行号**：22–22  |  **完整限定名**：`src.eval.llm_judge.MAX_REPORT_LENGTH`
- **值**：

```python
MAX_REPORT_LENGTH = 15000
```

**说明**（自动推断）：

数值上限常量 `MAX_REPORT_LENGTH`，用于约束对应操作的规模或阈值。

### `EVALUATION_CRITERIA`

- **类型**：模块常量  |  **行号**：24–49  |  **完整限定名**：`src.eval.llm_judge.EVALUATION_CRITERIA`
- **值**：

```python
EVALUATION_CRITERIA = {'factual_accuracy': {'description': 'Are claims supported by cited sources? Is information accurate and verifiable?'...
```

**说明**（自动推断）：

评估/提示词常量 `EVALUATION_CRITERIA`，定义对应流程使用的文本模板或判据。

### `JUDGE_SYSTEM_PROMPT`

- **类型**：模块常量  |  **行号**：51–78  |  **完整限定名**：`src.eval.llm_judge.JUDGE_SYSTEM_PROMPT`
- **值**：

```python
JUDGE_SYSTEM_PROMPT = 'You are an expert report quality evaluator. Your task is to objectively assess the quality of research reports.\n\nE...
```

**说明**（自动推断）：

评估/提示词常量 `JUDGE_SYSTEM_PROMPT`，定义对应流程使用的文本模板或判据。

### `EvaluationResult`

- **类型**：类  |  **行号**：82–102  |  **完整限定名**：`src.eval.llm_judge.EvaluationResult`
- **装饰器**：`@dataclass`
- **定义**：

```python
class EvaluationResult:
```
- **成员概览**：

  - `attr scores`
  - `attr overall_score`
  - `attr weighted_score`
  - `attr strengths`
  - `attr weaknesses`
  - `attr suggestions`
  - `attr raw_response`
  - `def to_dict`

**摘要**：

Container for LLM evaluation results.

### `LLMJudge`

- **类型**：类  |  **行号**：105–260  |  **完整限定名**：`src.eval.llm_judge.LLMJudge`
- **定义**：

```python
class LLMJudge:
```
- **成员概览**：

  - `def __init__`
  - `def _get_llm`
  - `def _calculate_weighted_score`
  - `def _parse_response`
  - `async def evaluate`
  - `def evaluate_sync`

**摘要**：

LLM-based report quality evaluator.

### `evaluate_with_llm`

- **类型**：异步函数  |  **行号**：263–282  |  **完整限定名**：`src.eval.llm_judge.evaluate_with_llm`
- **签名**：

```python
async def evaluate_with_llm(report: str, query: str, report_style: str='default', llm: Any=None) -> EvaluationResult:
```

**摘要**：

Convenience function to evaluate a report with LLM.

**参数**：

```text
report: The report text to evaluate
    query: The original research query
    report_style: The style of report for context
    llm: Optional LLM instance to use
```

**返回值**：

```text
EvaluationResult with scores and feedback
```

## 调用关系（下游）

**被以下模块导入**：

- `src.eval`
- `src.eval.evaluator`
- `tests.unit.eval.test_evaluator`

## 示例用法

```python
from src.eval.llm_judge import evaluate_with_llm
#
# TODO: 结合业务场景补充 evaluate_with_llm 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/server/eval_request.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/eval_request.py`
- **模块导入名**：`src.server.eval_request`
- **代码行数**：71
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
Request models for report evaluation endpoint.
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Optional`
- `from pydantic import BaseModel, Field`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `EvaluateReportRequest` | 11 | `` |
| 类 | `EvaluationMetrics` | 25 | `` |
| 类 | `LLMEvaluationScores` | 42 | `` |
| 类 | `LLMEvaluation` | 53 | `` |
| 类 | `EvaluateReportResponse` | 64 | `` |

## 符号详解

### `EvaluateReportRequest`

- **类型**：类  |  **行号**：11–22  |  **完整限定名**：`src.server.eval_request.EvaluateReportRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class EvaluateReportRequest(BaseModel):
```
- **成员概览**：

  - `attr content`
  - `attr query`
  - `attr report_style`
  - `attr use_llm`

**摘要**：

Request model for report evaluation.

### `EvaluationMetrics`

- **类型**：类  |  **行号**：25–39  |  **完整限定名**：`src.server.eval_request.EvaluationMetrics`
- **基类**：`BaseModel`
- **定义**：

```python
class EvaluationMetrics(BaseModel):
```
- **成员概览**：

  - `attr word_count`
  - `attr citation_count`
  - `attr unique_sources`
  - `attr image_count`
  - `attr section_count`
  - `attr section_coverage_score`
  - `attr sections_found`
  - `attr sections_missing`
  - `attr has_title`
  - `attr has_key_points`
  - `attr has_overview`
  - `attr has_citations_section`

**摘要**：

Automated metrics result.

### `LLMEvaluationScores`

- **类型**：类  |  **行号**：42–50  |  **完整限定名**：`src.server.eval_request.LLMEvaluationScores`
- **基类**：`BaseModel`
- **定义**：

```python
class LLMEvaluationScores(BaseModel):
```
- **成员概览**：

  - `attr factual_accuracy`
  - `attr completeness`
  - `attr coherence`
  - `attr relevance`
  - `attr citation_quality`
  - `attr writing_quality`

**摘要**：

LLM evaluation scores.

### `LLMEvaluation`

- **类型**：类  |  **行号**：53–61  |  **完整限定名**：`src.server.eval_request.LLMEvaluation`
- **基类**：`BaseModel`
- **定义**：

```python
class LLMEvaluation(BaseModel):
```
- **成员概览**：

  - `attr scores`
  - `attr overall_score`
  - `attr weighted_score`
  - `attr strengths`
  - `attr weaknesses`
  - `attr suggestions`

**摘要**：

LLM evaluation result.

### `EvaluateReportResponse`

- **类型**：类  |  **行号**：64–71  |  **完整限定名**：`src.server.eval_request.EvaluateReportResponse`
- **基类**：`BaseModel`
- **定义**：

```python
class EvaluateReportResponse(BaseModel):
```
- **成员概览**：

  - `attr metrics`
  - `attr score`
  - `attr grade`
  - `attr llm_evaluation`
  - `attr summary`

**摘要**：

Response model for report evaluation.

## 调用关系（下游）

**被以下模块导入**：

- `src.server.app`

## 示例用法

```python
from src.server.eval_request import EvaluateReportRequest
#
# TODO: 结合业务场景补充 EvaluateReportRequest 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

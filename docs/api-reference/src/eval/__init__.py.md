# `src/eval/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/eval/__init__.py`
- **模块导入名**：`src.eval`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：21
- **架构归属**：src/eval —— 报告评估：自动化指标（字数/引用/章节覆盖）+ LLM-as-Judge 综合评分

## 模块概述

```text
Report Quality Evaluation Module for DeerFlow.

This module provides objective methods to evaluate generated report quality,
including automated metrics and LLM-based evaluation.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .evaluator import ReportEvaluator`
- `from .metrics import ReportMetrics, compute_metrics`
- `from .llm_judge import LLMJudge, evaluate_with_llm`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

**被以下模块导入**：

- `src.server.app`

## 示例用法

```python
# import src.eval
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

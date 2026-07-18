# `src/prompts/planner_model.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prompts/planner_model.py`
- **模块导入名**：`src.prompts.planner_model`
- **代码行数**：66
- **架构归属**：src/prompts —— Jinja2 提示词模板与 Plan/Step 数据模型

## 模块概述

```text
Planner 智能体的结构化数据模型定义。

基于 Pydantic 定义规划阶段的数据契约：``StepType``（research/analysis/processing）、
``Step``（单步计划）与 ``Plan``（整体计划），用于约束 LLM 输出可解析的研究计划，
驱动后续多智能体的搜索与分析流程。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from enum import Enum`
- `from typing import List, Optional`
- `from pydantic import BaseModel, Field`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `StepType` | 17 | `` |
| 类 | `Step` | 23 | `` |
| 类 | `Plan` | 33 | `` |

## 符号详解

### `StepType`

- **类型**：类  |  **行号**：17–20  |  **完整限定名**：`src.prompts.planner_model.StepType`
- **基类**：`str`, `Enum`
- **定义**：

```python
class StepType(str, Enum):
```
- **成员概览**：

  - `attr RESEARCH`
  - `attr ANALYSIS`
  - `attr PROCESSING`

**说明**（自动推断）：

枚举类型 `StepType`，定义该维度可选的取值集合。

### `Step`

- **类型**：类  |  **行号**：23–30  |  **完整限定名**：`src.prompts.planner_model.Step`
- **基类**：`BaseModel`
- **定义**：

```python
class Step(BaseModel):
```
- **成员概览**：

  - `attr need_search`
  - `attr title`
  - `attr description`
  - `attr step_type`
  - `attr execution_res`

**说明**（自动推断）：

Pydantic 数据模型 `Step`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `Plan`

- **类型**：类  |  **行号**：33–66  |  **完整限定名**：`src.prompts.planner_model.Plan`
- **基类**：`BaseModel`
- **定义**：

```python
class Plan(BaseModel):
```
- **成员概览**：

  - `attr locale`
  - `attr has_enough_context`
  - `attr thought`
  - `attr title`
  - `attr steps`

**说明**（自动推断）：

Pydantic 数据模型 `Plan`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.builder`
- `src.graph.nodes`
- `src.graph.types`
- `tests.integration.test_nodes`
- `tests.unit.graph.test_human_feedback_locale_fix`

## 示例用法

```python
from src.prompts.planner_model import StepType
#
# TODO: 结合业务场景补充 StepType 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

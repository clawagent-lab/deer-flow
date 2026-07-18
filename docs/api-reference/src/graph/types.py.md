# `src/graph/types.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/graph/types.py`
- **模块导入名**：`src.graph.types`
- **代码行数**：50
- **架构归属**：src/graph —— LangGraph 主工作流：节点、状态、边、checkpoint、工具函数

## 模块概述

```text
工作流状态类型定义模块：``State`` 继承 ``MessagesState``，扩展运行时变量（locale、研究主题、计划、观察结果、最终报告等）与背景调查开关等配置字段。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.prompts.planner_model import Plan`
- `from src.rag import Resource`

**外部依赖**（第三方库 / 标准库）：

- `from dataclasses import field`
- `from typing import Any`
- `from langgraph.graph import MessagesState`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `State` | 16 | `` |

## 符号详解

### `State`

- **类型**：类  |  **行号**：16–50  |  **完整限定名**：`src.graph.types.State`
- **基类**：`MessagesState`
- **定义**：

```python
class State(MessagesState):
```
- **成员概览**：

  - `attr locale`
  - `attr research_topic`
  - `attr clarified_research_topic`
  - `attr observations`
  - `attr resources`
  - `attr plan_iterations`
  - `attr current_plan`
  - `attr final_report`
  - `attr auto_accepted_plan`
  - `attr enable_background_investigation`
  - `attr background_investigation_results`
  - `attr citations`
  - `attr enable_clarification`
  - `attr clarification_rounds`
  - `attr clarification_history`
  - `attr is_clarification_complete`
  - `attr max_clarification_rounds`
  - `attr goto`

**摘要**：

State for the agent system, extends MessagesState with next field.

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.builder`
- `src.graph.nodes`
- `src.podcast.graph.script_writer_node`
- `src.podcast.graph.state`
- `tests.unit.graph.test_agent_locale_restoration`
- `tests.unit.graph.test_human_feedback_locale_fix`
- `tests.unit.graph.test_nodes_recursion_limit`
- `tests.unit.graph.test_state_preservation`

## 示例用法

```python
# src/graph/types.py 示例用法
#
# State 是整个 LangGraph 工作流共享的状态对象，继承自 MessagesState。
#
# 1) 直接构造一个初始 State
from src.graph.types import State

initial_state: State = {
    "messages": [{"role": "user", "content": "研究 LLM 推理优化技术"}],
    "locale": "zh-CN",
    "research_topic": "研究 LLM 推理优化技术",
    "clarified_research_topic": "研究 LLM 推理优化技术",
    "observations": [],
    "resources": [],
    "plan_iterations": 0,
    "current_plan": None,
    "final_report": "",
    "auto_accepted_plan": True,
    "enable_background_investigation": True,
    "background_investigation_results": None,
    "citations": [],
    "enable_clarification": False,
    "clarification_rounds": 0,
    "clarification_history": [],
    "is_clarification_complete": False,
    "max_clarification_rounds": 3,
    "goto": "planner",
}

# 2) 在节点函数中读取 / 更新 State
from src.graph.types import State
from langchain_core.runnables import RunnableConfig

def my_node(state: State, config: RunnableConfig):
    # 读取
    topic = state["research_topic"]
    locale = state.get("locale", "en-US")
    plan = state.get("current_plan")
    # 返回部分更新（LangGraph 会合并到状态）
    return {
        "observations": state.get("observations", []) + ["new observation"],
        "plan_iterations": state.get("plan_iterations", 0) + 1,
    }

# 3) 字段说明
# - messages: 对话历史（MessagesState 提供，自动累加）
# - locale: 语言区域，影响提示词模板与报告语言
# - research_topic / clarified_research_topic: 原始 / 澄清后的研究主题
# - observations: 研究过程中的观察列表
# - resources: 检索到的资源列表（Resource 对象）
# - current_plan: 当前执行计划（Plan 对象或字符串）
# - final_report: 最终生成的报告文本
# - citations: 引用元数据列表（dict）
# - enable_clarification / clarification_rounds / clarification_history:
#   多轮澄清的控制位与历史
# - goto: 条件边使用的下一节点名
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

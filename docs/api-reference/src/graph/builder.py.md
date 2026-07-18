# `src/graph/builder.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/graph/builder.py`
- **模块导入名**：`src.graph.builder`
- **代码行数**：93
- **架构归属**：src/graph —— LangGraph 主工作流：节点、状态、边、checkpoint、工具函数

## 模块概述

```text
LangGraph 主工作流构建模块：装配 coordinator/planner/research_team/reporter 等节点与条件边，编译为可执行的 StateGraph，并提供带 MemorySaver 的有状态版本。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.prompts.planner_model import StepType`
- `from .nodes import analyst_node, background_investigation_node, coder_node, coordinator_node, human_feedback_node, planner_node, reporter_node, research_team_node, researcher_node`
- `from .types import State`

**外部依赖**（第三方库 / 标准库）：

- `from langgraph.checkpoint.memory import MemorySaver`
- `from langgraph.graph import END, START, StateGraph`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `continue_to_running_research_team` | 25 | `(state: State)` |
| 函数 | `_build_base_graph` | 52 | `()` |
| 函数 | `build_graph_with_memory` | 75 | `()` |
| 函数 | `build_graph` | 86 | `()` |
| 常量 | `graph` | 93 | `build_graph()` |

## 符号详解

### `continue_to_running_research_team`

- **类型**：函数  |  **行号**：25–49  |  **完整限定名**：`src.graph.builder.continue_to_running_research_team`
- **签名**：

```python
def continue_to_running_research_team(state: State):
```

**说明**（自动推断）：

LangGraph 条件边函数，根据当前 State 决定下一个执行节点，返回节点名字符串以驱动工作流路由。

### `_build_base_graph`

- **类型**：函数  |  **行号**：52–72  |  **完整限定名**：`src.graph.builder._build_base_graph`
- **签名**：

```python
def _build_base_graph():
```

**摘要**：

Build and return the base state graph with all nodes and edges.

### `build_graph_with_memory`

- **类型**：函数  |  **行号**：75–83  |  **完整限定名**：`src.graph.builder.build_graph_with_memory`
- **签名**：

```python
def build_graph_with_memory():
```

**摘要**：

Build and return the agent workflow graph with memory.

### `build_graph`

- **类型**：函数  |  **行号**：86–90  |  **完整限定名**：`src.graph.builder.build_graph`
- **签名**：

```python
def build_graph():
```

**摘要**：

Build and return the agent workflow graph without memory.

### `graph`

- **类型**：模块常量  |  **行号**：93–93  |  **完整限定名**：`src.graph.builder.graph`
- **值**：

```python
graph = build_graph()
```

**说明**（自动推断）：

已编译的 LangGraph 工作流实例，模块导入时即构建完成，供 `invoke` / `astream` 直接调用。

## 调用关系（下游）

**被以下模块导入**：

- `src.graph`
- `src.rag`
- `src.server.app`
- `tests.unit.graph.test_builder`

## 示例用法

```python
# src/graph/builder.py 示例用法
#
# 该模块构建 DeerFlow 的 LangGraph 主工作流，包含 coordinator、planner、
# research_team（researcher/analyst/coder）、reporter、human_feedback 等节点。
#
# 1) 获取默认编译好的 graph（无记忆，每次运行独立）
from src.graph.builder import build_graph

graph = build_graph()
# graph.invoke(...) / graph.astream(...) 即可运行

# 2) 构建带内存 checkpoint 的 graph（保留同一 thread 的会话历史）
from src.graph.builder import build_graph_with_memory

memory_graph = build_graph_with_memory()
config = {"configurable": {"thread_id": "user-123"}}
# 第一次提问
memory_graph.invoke(
    {"messages": [{"role": "user", "content": "什么是 RAG？"}]},
    config=config,
)
# 同一 thread_id 的后续提问会带上历史
memory_graph.invoke(
    {"messages": [{"role": "user", "content": "它和微调相比有什么优劣？"}]},
    config=config,
)

# 3) 查看工作流结构（Mermaid 图）
graph = build_graph()
print(graph.get_graph(xray=True).draw_mermaid())

# 4) 条件边函数：决定 research_team 的下一个执行节点
from src.graph.builder import continue_to_running_research_team
from src.graph.types import State

state: State = {
    "current_plan": ...,  # Plan 对象
    # ...
}
next_node = continue_to_running_research_team(state)
# 返回值之一："planner" | "researcher" | "analyst" | "coder"
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

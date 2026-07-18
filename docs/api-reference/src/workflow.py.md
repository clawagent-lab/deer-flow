# `src/workflow.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/workflow.py`
- **模块导入名**：`src.workflow`
- **代码行数**：182
- **架构归属**：src —— DeerFlow 后端核心包，包含工作流、智能体、工具、配置等所有业务模块

## 模块概述

```text
DeerFlow 多智能体工作流入口模块。

负责构建 LangGraph 研究图谱并配置日志，提供 ``run_agent_workflow_async``
以异步流式方式执行规划、研究、报告生成等完整研究流程，
支持调试日志、计划迭代上限、澄清轮次与 MCP 工具集成等可调参数。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.configuration import get_recursion_limit`
- `from src.graph import build_graph`
- `from src.graph.utils import build_clarified_topic_from_history`

**外部依赖**（第三方库 / 标准库）：

- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `enable_debug_logging` | 23 | `()` |
| 常量 | `logger` | 31 | `logging.getLogger(__name__)` |
| 常量 | `graph` | 34 | `build_graph()` |
| 异步函数 | `run_agent_workflow_async` | 37 | `(user_input: str, debug: bool=False, max_plan_iterations: int=1, max_step_num: int=3, enable_back...` |

## 符号详解

### `enable_debug_logging`

- **类型**：函数  |  **行号**：23–28  |  **完整限定名**：`src.workflow.enable_debug_logging`
- **签名**：

```python
def enable_debug_logging():
```

**摘要**：

Enable debug level logging for more detailed execution information.

### `logger`

- **类型**：模块常量  |  **行号**：31–31  |  **完整限定名**：`src.workflow.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `graph`

- **类型**：模块常量  |  **行号**：34–34  |  **完整限定名**：`src.workflow.graph`
- **值**：

```python
graph = build_graph()
```

**说明**（自动推断）：

已编译的 LangGraph 工作流实例，模块导入时即构建完成，供 `invoke` / `astream` 直接调用。

### `run_agent_workflow_async`

- **类型**：异步函数  |  **行号**：37–178  |  **完整限定名**：`src.workflow.run_agent_workflow_async`
- **签名**：

```python
async def run_agent_workflow_async(user_input: str, debug: bool=False, max_plan_iterations: int=1, max_step_num: int=3, enable_background_investigation: bool=True, enable_clarification: bool | None=None, max_clarification_rounds: int | None=None, initial_state: dict | None=None, locale: str | None=None):
```

**摘要**：

Run the agent workflow asynchronously with the given user input.

**参数**：

```text
user_input: The user's query or request
    debug: If True, enables debug level logging
    max_plan_iterations: Maximum number of plan iterations
    max_step_num: Maximum number of steps in a plan
    enable_background_investigation: If True, performs web search before planning to enhance context
    enable_clarification: If None, use default from State class (False); if True/False, override
    max_clarification_rounds: Maximum number of clarification rounds allowed
    initial_state: Initial state to use (for recursive calls during clarification)
    locale: The locale setting (e.g., 'en-US', 'zh-CN')
```

**返回值**：

```text
The final state after the workflow completes
```

## 调用关系（下游）

**被以下模块导入**：

- `main`

## 示例用法

```python
# src/workflow.py 示例用法
#
# 该模块是 DeerFlow 的编排入口，构建 LangGraph 并以异步流式方式运行。
#
# 1) 直接运行（会打印主工作流的 Mermaid 图）
python src/workflow.py

# 2) 在异步代码中调用 run_agent_workflow_async
import asyncio
from src.workflow import run_agent_workflow_async

async def main():
    final_state = await run_agent_workflow_async(
        user_input="调研 LangGraph 1.x 的多智能体编排能力",
        debug=True,
        max_plan_iterations=2,
        max_step_num=4,
        enable_background_investigation=True,
        enable_clarification=True,
        max_clarification_rounds=2,
        locale="zh-CN",
    )
    # final_state 包含 final_report、current_plan、citations 等字段
    print(final_state.get("final_report", ""))

asyncio.run(main())

# 3) 直接使用构建好的 graph 对象进行自定义流式消费
from src.workflow import graph

config = {
    "configurable": {
        "thread_id": "my-session",
        "max_plan_iterations": 1,
        "max_step_num": 3,
    },
    "recursion_limit": 100,
}
initial_state = {
    "messages": [{"role": "user", "content": "什么是 Mixture of Experts？"}],
    "auto_accepted_plan": True,
    "research_topic": "什么是 Mixture of Experts？",
}

# graph.astream 以流式方式产出每个节点执行后的状态快照
import asyncio

async def stream():
    async for state in graph.astream(initial_state, config=config, stream_mode="values"):
        msgs = state.get("messages", [])
        if msgs:
            print(f"[step] messages count = {len(msgs)}")

asyncio.run(stream())

# 4) 启用调试日志（单独调用）
from src.workflow import enable_debug_logging

enable_debug_logging()
# 此后 src / langchain / langgraph 命名空间的日志级别为 DEBUG
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

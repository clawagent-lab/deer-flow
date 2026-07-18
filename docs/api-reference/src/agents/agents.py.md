# `src/agents/agents.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/agents/agents.py`
- **模块导入名**：`src.agents.agents`
- **代码行数**：180
- **架构归属**：src/agents —— 智能体构建与中间件（基于 LangChain 1.x `create_agent` + `AgentMiddleware`，封装动态提示词、工具拦截、模型钩子）

## 模块概述

```text
LangChain 智能体的创建逻辑，是 agents 子包的核心实现。

提供 create_agent 工厂函数，根据 agent 类型从 AGENT_LLM_MAP 选择对应 LLM，
注入动态 prompt 模板（DynamicPromptMiddleware）和 pre-model hook（PreModelHookMiddleware）两类中间件，
并按需通过 tool_interceptor 包装工具以实现调用前中断。统一了 DeerFlow 各节点的智能体构建方式。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.agents.tool_interceptor import wrap_tools_with_interceptor`
- `from src.config.agents import AGENT_LLM_MAP`
- `from src.llms.llm import get_llm_by_type`
- `from src.prompts import apply_prompt_template`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Callable, List, Optional`
- `from langchain.agents import create_agent`
- `from langchain.agents.middleware import AgentMiddleware`
- `from langgraph.runtime import Runtime`
- `import asyncio`
- `import inspect`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 25 | `logging.getLogger(__name__)` |
| 类 | `DynamicPromptMiddleware` | 28 | `` |
| 类 | `PreModelHookMiddleware` | 64 | `` |
| 函数 | `create_agent` | 111 | `(agent_name: str, agent_type: str, tools: list, prompt_template: str, pre_model_hook: callable=No...` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：25–25  |  **完整限定名**：`src.agents.agents.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `DynamicPromptMiddleware`

- **类型**：类  |  **行号**：28–61  |  **完整限定名**：`src.agents.agents.DynamicPromptMiddleware`
- **基类**：`AgentMiddleware`
- **定义**：

```python
class DynamicPromptMiddleware(AgentMiddleware):
```
- **成员概览**：

  - `def __init__`
  - `def before_model`
  - `async def abefore_model`

**摘要**：

Middleware to apply dynamic prompt template before model invocation.

### `PreModelHookMiddleware`

- **类型**：类  |  **行号**：64–107  |  **完整限定名**：`src.agents.agents.PreModelHookMiddleware`
- **基类**：`AgentMiddleware`
- **定义**：

```python
class PreModelHookMiddleware(AgentMiddleware):
```
- **成员概览**：

  - `def __init__`
  - `def before_model`
  - `async def abefore_model`

**摘要**：

Middleware to execute a pre-model hook before model invocation.

### `create_agent`

- **类型**：函数  |  **行号**：111–180  |  **完整限定名**：`src.agents.agents.create_agent`
- **签名**：

```python
def create_agent(agent_name: str, agent_type: str, tools: list, prompt_template: str, pre_model_hook: callable=None, interrupt_before_tools: Optional[List[str]]=None, locale: str='en-US'):
```

**摘要**：

Factory function to create agents with consistent configuration.

**参数**：

```text
agent_name: Name of the agent
    agent_type: Type of agent (researcher, coder, etc.)
    tools: List of tools available to the agent
    prompt_template: Name of the prompt template to use
    pre_model_hook: Optional hook to preprocess state before model invocation
    interrupt_before_tools: Optional list of tool names to interrupt before execution
    locale: Language locale for prompt template selection (e.g., en-US, zh-CN)
```

**返回值**：

```text
A configured agent graph
```

## 调用关系（下游）

**被以下模块导入**：

- `src.agents`
- `tests.integration.test_tool_interceptor_integration`
- `tests.unit.agents.test_middleware`

## 示例用法

```python
# src/agents/agents.py 示例用法
#
# 封装 LangChain 1.x create_agent，注入动态提示词中间件与工具拦截器。
#
# 1) 创建一个带动态提示词的智能体
from src.agents.agents import create_agent
from src.llms.llm import get_llm_by_type

llm = get_llm_by_type("basic")
agent = create_agent(
    llm=llm,
    agent_type="researcher",
    tools=[],
    prompt_template="researcher",
    locale="zh-CN",
)
# agent 即为可运行的 Runnable，支持 invoke / ainvoke / astream

# 2) 异步调用智能体
import asyncio

async def run():
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "帮我查一下 2025 年 AI Agent 框架对比"}]}
    )
    print(result["messages"][-1].content)

asyncio.run(run())

# 3) 使用内置中间件
from src.agents.agents import DynamicPromptMiddleware, PreModelHookMiddleware

# DynamicPromptMiddleware 会在模型调用前注入渲染好的系统提示词
middleware = DynamicPromptMiddleware(prompt_template="researcher", locale="zh-CN")
# 通常不直接使用，而是通过 create_agent 自动注入
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

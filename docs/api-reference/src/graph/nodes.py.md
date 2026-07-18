# `src/graph/nodes.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/graph/nodes.py`
- **模块导入名**：`src.graph.nodes`
- **代码行数**：1507
- **架构归属**：src/graph —— LangGraph 主工作流：节点、状态、边、checkpoint、工具函数

## 模块概述

```text
LangGraph 节点实现模块：定义 coordinator、planner、research_team、researcher、coder、analyst、reporter、human_feedback、background_investigation 等节点的执行逻辑，串联 LLM、工具与提示模板。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.agents import create_agent`
- `from src.citations import extract_citations_from_messages, merge_citations`
- `from src.config.agents import AGENT_LLM_MAP`
- `from src.config.configuration import Configuration`
- `from src.llms.llm import get_llm_by_type, get_llm_token_limit_by_type`
- `from src.prompts.planner_model import Plan`
- `from src.prompts.template import apply_prompt_template, get_system_prompt_template`
- `from src.tools import crawl_tool, get_retriever_tool, get_web_search_tool, python_repl_tool`
- `from src.tools.search import LoggedTavilySearch`
- `from src.utils.context_manager import ContextManager, validate_message_content`
- `from src.utils.json_utils import repair_json_output, sanitize_tool_response`
- `from ..config import SELECTED_SEARCH_ENGINE, SearchEngine`
- `from .types import State`
- `from .utils import build_clarified_topic_from_history, get_message_content, is_user_message, reconstruct_clarification_history`

**外部依赖**（第三方库 / 标准库）：

- `from functools import partial`
- `from typing import Annotated, Any, Literal`
- `from pydantic import ValidationError`
- `from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage`
- `from langchain_core.runnables import RunnableConfig`
- `from langchain_core.tools import tool`
- `from langchain_mcp_adapters.client import MultiServerMCPClient`
- `from langgraph.errors import GraphRecursionError`
- `from langgraph.types import Command, interrupt`
- `import json`
- `import logging`
- `import os`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 47 | `logging.getLogger(__name__)` |
| 函数 | `handoff_to_planner` | 51 | `(research_topic: Annotated[str, 'The topic of the research task to be handed off.'], locale: Anno...` |
| 函数 | `handoff_after_clarification` | 62 | `(locale: Annotated[str, "The user's detected language locale (e.g., en-US, zh-CN)."], research_to...` |
| 函数 | `direct_response` | 73 | `(message: Annotated[str, 'The response message to send directly to user.'], locale: Annotated[str...` |
| 函数 | `needs_clarification` | 81 | `(state: dict) -> bool` |
| 函数 | `preserve_state_meta_fields` | 102 | `(state: State) -> dict` |
| 函数 | `validate_and_fix_plan` | 127 | `(plan: dict, enforce_web_search: bool=False, enable_web_search: bool=True) -> dict` |
| 函数 | `background_investigation_node` | 205 | `(state: State, config: RunnableConfig)` |
| 函数 | `planner_node` | 270 | `(state: State, config: RunnableConfig) -> Command[Literal['human_feedback', 'reporter']]` |
| 函数 | `extract_plan_content` | 400 | `(plan_data: str \| dict \| Any) -> str` |
| 函数 | `human_feedback_node` | 460 | `(state: State, config: RunnableConfig) -> Command[Literal['planner', 'research_team', 'reporter',...` |
| 函数 | `coordinator_node` | 591 | `(state: State, config: RunnableConfig) -> Command[Literal['planner', 'background_investigator', '...` |
| 函数 | `reporter_node` | 879 | `(state: State, config: RunnableConfig)` |
| 函数 | `research_team_node` | 959 | `(state: State)` |
| 函数 | `validate_web_search_usage` | 966 | `(messages: list, agent_name: str='agent') -> bool` |
| 异步函数 | `_handle_recursion_limit_fallback` | 1009 | `(messages: list, agent_name: str, current_step, state: State) -> list` |
| 异步函数 | `_execute_agent_step` | 1082 | `(state: State, agent, agent_name: str, config: RunnableConfig=None) -> Command[Literal['research_...` |
| 异步函数 | `_setup_and_execute_agent_step` | 1356 | `(state: State, config: RunnableConfig, agent_type: str, default_tools: list) -> Command[Literal['...` |
| 异步函数 | `researcher_node` | 1428 | `(state: State, config: RunnableConfig) -> Command[Literal['research_team']]` |
| 异步函数 | `coder_node` | 1471 | `(state: State, config: RunnableConfig) -> Command[Literal['research_team']]` |
| 异步函数 | `analyst_node` | 1486 | `(state: State, config: RunnableConfig) -> Command[Literal['research_team']]` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：47–47  |  **完整限定名**：`src.graph.nodes.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `handoff_to_planner`

- **类型**：函数  |  **行号**：51–58  |  **完整限定名**：`src.graph.nodes.handoff_to_planner`
- **装饰器**：`@tool`
- **签名**：

```python
def handoff_to_planner(research_topic: Annotated[str, 'The topic of the research task to be handed off.'], locale: Annotated[str, "The user's detected language locale (e.g., en-US, zh-CN)."]):
```

**摘要**：

Handoff to planner agent to do plan.

### `handoff_after_clarification`

- **类型**：函数  |  **行号**：62–69  |  **完整限定名**：`src.graph.nodes.handoff_after_clarification`
- **装饰器**：`@tool`
- **签名**：

```python
def handoff_after_clarification(locale: Annotated[str, "The user's detected language locale (e.g., en-US, zh-CN)."], research_topic: Annotated[str, 'The clarified research topic based on all clarification rounds.']):
```

**摘要**：

Handoff to planner after clarification rounds are complete. Pass all clarification history to planner for analysis.

### `direct_response`

- **类型**：函数  |  **行号**：73–78  |  **完整限定名**：`src.graph.nodes.direct_response`
- **装饰器**：`@tool`
- **签名**：

```python
def direct_response(message: Annotated[str, 'The response message to send directly to user.'], locale: Annotated[str, "The user's detected language locale (e.g., en-US, zh-CN)."]):
```

**摘要**：

Respond directly to user for greetings, small talk, or polite rejections. Do NOT use this for research questions - use handoff_to_planner instead.

### `needs_clarification`

- **类型**：函数  |  **行号**：81–99  |  **完整限定名**：`src.graph.nodes.needs_clarification`
- **签名**：

```python
def needs_clarification(state: dict) -> bool:
```

**摘要**：

Check if clarification is needed based on current state.
Centralized logic for determining when to continue clarification.

### `preserve_state_meta_fields`

- **类型**：函数  |  **行号**：102–124  |  **完整限定名**：`src.graph.nodes.preserve_state_meta_fields`
- **签名**：

```python
def preserve_state_meta_fields(state: State) -> dict:
```

**摘要**：

Extract meta/config fields that should be preserved across state transitions.

**参数**：

```text
state: Current state object
```

**返回值**：

```text
Dict of meta fields to preserve
```

### `validate_and_fix_plan`

- **类型**：函数  |  **行号**：127–202  |  **完整限定名**：`src.graph.nodes.validate_and_fix_plan`
- **签名**：

```python
def validate_and_fix_plan(plan: dict, enforce_web_search: bool=False, enable_web_search: bool=True) -> dict:
```

**摘要**：

Validate and fix a plan to ensure it meets requirements.

**参数**：

```text
plan: The plan dict to validate
    enforce_web_search: If True, ensure at least one step has need_search=true
    enable_web_search: If False, skip web search enforcement (takes precedence)
```

**返回值**：

```text
The validated/fixed plan dict
```

### `background_investigation_node`

- **类型**：函数  |  **行号**：205–267  |  **完整限定名**：`src.graph.nodes.background_investigation_node`
- **签名**：

```python
def background_investigation_node(state: State, config: RunnableConfig):
```

**说明**（自动推断）：

LangGraph 工作流节点函数，对应 `background_investigation` 节点。接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，并返回需要合并回 State 的部分字典或 `Command` 对象。

### `planner_node`

- **类型**：函数  |  **行号**：270–397  |  **完整限定名**：`src.graph.nodes.planner_node`
- **签名**：

```python
def planner_node(state: State, config: RunnableConfig) -> Command[Literal['human_feedback', 'reporter']]:
```

**摘要**：

Planner node that generate the full plan.

### `extract_plan_content`

- **类型**：函数  |  **行号**：400–457  |  **完整限定名**：`src.graph.nodes.extract_plan_content`
- **签名**：

```python
def extract_plan_content(plan_data: str | dict | Any) -> str:
```

**摘要**：

Safely extract plan content from different types of plan data.

**参数**：

```text
plan_data: The plan data which can be a string, AIMessage, or dict
```

**返回值**：

```text
str: The plan content as a string (JSON string for dict inputs, or 
extracted/original string for other types)
```

### `human_feedback_node`

- **类型**：函数  |  **行号**：460–588  |  **完整限定名**：`src.graph.nodes.human_feedback_node`
- **签名**：

```python
def human_feedback_node(state: State, config: RunnableConfig) -> Command[Literal['planner', 'research_team', 'reporter', '__end__']]:
```

**说明**（自动推断）：

LangGraph 工作流节点函数，对应 `human_feedback` 节点。接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，并返回需要合并回 State 的部分字典或 `Command` 对象。

### `coordinator_node`

- **类型**：函数  |  **行号**：591–876  |  **完整限定名**：`src.graph.nodes.coordinator_node`
- **签名**：

```python
def coordinator_node(state: State, config: RunnableConfig) -> Command[Literal['planner', 'background_investigator', 'coordinator', '__end__']]:
```

**摘要**：

Coordinator node that communicate with customers and handle clarification.

### `reporter_node`

- **类型**：函数  |  **行号**：879–956  |  **完整限定名**：`src.graph.nodes.reporter_node`
- **签名**：

```python
def reporter_node(state: State, config: RunnableConfig):
```

**摘要**：

Reporter node that write a final report.

### `research_team_node`

- **类型**：函数  |  **行号**：959–963  |  **完整限定名**：`src.graph.nodes.research_team_node`
- **签名**：

```python
def research_team_node(state: State):
```

**摘要**：

Research team node that collaborates on tasks.

### `validate_web_search_usage`

- **类型**：函数  |  **行号**：966–1006  |  **完整限定名**：`src.graph.nodes.validate_web_search_usage`
- **签名**：

```python
def validate_web_search_usage(messages: list, agent_name: str='agent') -> bool:
```

**摘要**：

Validate if the agent has used the web search tool during execution.

**参数**：

```text
messages: List of messages from the agent execution
    agent_name: Name of the agent (for logging purposes)
```

**返回值**：

```text
bool: True if web search tool was used, False otherwise
```

### `_handle_recursion_limit_fallback`

- **类型**：异步函数  |  **行号**：1009–1079  |  **完整限定名**：`src.graph.nodes._handle_recursion_limit_fallback`
- **签名**：

```python
async def _handle_recursion_limit_fallback(messages: list, agent_name: str, current_step, state: State) -> list:
```

**摘要**：

Handle GraphRecursionError with graceful fallback using LLM summary.

**参数**：

```text
messages: Messages accumulated during agent execution before hitting limit
    agent_name: Name of the agent that hit the limit
    current_step: The current step being executed
    state: Current workflow state
```

**返回值**：

```text
list: Messages including the accumulated messages plus the fallback summary
```

**异常**：

```text
Exception: If the fallback LLM call fails
```

### `_execute_agent_step`

- **类型**：异步函数  |  **行号**：1082–1353  |  **完整限定名**：`src.graph.nodes._execute_agent_step`
- **签名**：

```python
async def _execute_agent_step(state: State, agent, agent_name: str, config: RunnableConfig=None) -> Command[Literal['research_team']]:
```

**摘要**：

Helper function to execute a step using the specified agent.

### `_setup_and_execute_agent_step`

- **类型**：异步函数  |  **行号**：1356–1425  |  **完整限定名**：`src.graph.nodes._setup_and_execute_agent_step`
- **签名**：

```python
async def _setup_and_execute_agent_step(state: State, config: RunnableConfig, agent_type: str, default_tools: list) -> Command[Literal['research_team']]:
```

**摘要**：

Helper function to set up an agent with appropriate tools and execute a step.

**参数**：

```text
state: The current state
    config: The runnable config
    agent_type: The type of agent ("researcher" or "coder")
    default_tools: The default tools to add to the agent
```

**返回值**：

```text
Command to update state and go to research_team
```

### `researcher_node`

- **类型**：异步函数  |  **行号**：1428–1468  |  **完整限定名**：`src.graph.nodes.researcher_node`
- **签名**：

```python
async def researcher_node(state: State, config: RunnableConfig) -> Command[Literal['research_team']]:
```

**摘要**：

Researcher node that do research

### `coder_node`

- **类型**：异步函数  |  **行号**：1471–1483  |  **完整限定名**：`src.graph.nodes.coder_node`
- **签名**：

```python
async def coder_node(state: State, config: RunnableConfig) -> Command[Literal['research_team']]:
```

**摘要**：

Coder node that do code analysis.

### `analyst_node`

- **类型**：异步函数  |  **行号**：1486–1507  |  **完整限定名**：`src.graph.nodes.analyst_node`
- **签名**：

```python
async def analyst_node(state: State, config: RunnableConfig) -> Command[Literal['research_team']]:
```

**摘要**：

Analyst node that performs reasoning and analysis without code execution.

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.builder`
- `tests.integration.test_nodes`
- `tests.unit.graph.test_agent_locale_restoration`
- `tests.unit.graph.test_human_feedback_locale_fix`
- `tests.unit.graph.test_nodes_recursion_limit`
- `tests.unit.graph.test_plan_validation`
- `tests.unit.graph.test_state_preservation`

## 示例用法

```python
from src.graph.nodes import handoff_to_planner
#
# TODO: 结合业务场景补充 handoff_to_planner 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

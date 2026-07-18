# `src/agents/tool_interceptor.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/agents/tool_interceptor.py`
- **模块导入名**：`src.agents.tool_interceptor`
- **代码行数**：253
- **架构归属**：src/agents —— 智能体构建与中间件（基于 LangChain 1.x `create_agent` + `AgentMiddleware`，封装动态提示词、工具拦截、模型钩子）

## 模块概述

```text
工具调用拦截器，用于在指定工具执行前触发 LangGraph interrupt。

核心类 ToolInterceptor 维护需中断的工具名单，并通过 wrap_tool / wrap_tools_with_interceptor
对原始工具进行包装：在调用前判断是否命中中断名单，命中则抛出 interrupt 以暂停图执行、
等待人工确认或外部输入，从而实现人机协作（human-in-the-loop）流程。同时对工具输入做
日志安全脱敏处理。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.utils.log_sanitizer import sanitize_feedback, sanitize_log_input, sanitize_tool_name`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Callable, List, Optional`
- `from langchain_core.tools import BaseTool`
- `from langgraph.types import interrupt`
- `import json`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 25 | `logging.getLogger(__name__)` |
| 类 | `ToolInterceptor` | 28 | `` |
| 函数 | `wrap_tools_with_interceptor` | 220 | `(tools: List[BaseTool], interrupt_before_tools: Optional[List[str]]=None) -> List[BaseTool]` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：25–25  |  **完整限定名**：`src.agents.tool_interceptor.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `ToolInterceptor`

- **类型**：类  |  **行号**：28–217  |  **完整限定名**：`src.agents.tool_interceptor.ToolInterceptor`
- **定义**：

```python
class ToolInterceptor:
```
- **成员概览**：

  - `def __init__`
  - `def should_interrupt`
  - `def _format_tool_input`
  - `def wrap_tool`
  - `def _parse_approval`

**摘要**：

Intercepts tool calls and triggers interrupts for specified tools.

### `wrap_tools_with_interceptor`

- **类型**：函数  |  **行号**：220–253  |  **完整限定名**：`src.agents.tool_interceptor.wrap_tools_with_interceptor`
- **签名**：

```python
def wrap_tools_with_interceptor(tools: List[BaseTool], interrupt_before_tools: Optional[List[str]]=None) -> List[BaseTool]:
```

**摘要**：

Wrap multiple tools with interrupt logic.

**参数**：

```text
tools: List of tools to wrap
    interrupt_before_tools: List of tool names to interrupt before
```

**返回值**：

```text
List[BaseTool]: List of wrapped tools
```

## 调用关系（下游）

**被以下模块导入**：

- `src.agents.agents`
- `tests.integration.test_tool_interceptor_integration`
- `tests.unit.agents.test_tool_interceptor`
- `tests.unit.agents.test_tool_interceptor_fix`

## 示例用法

```python
from src.agents.tool_interceptor import wrap_tools_with_interceptor
#
# TODO: 结合业务场景补充 wrap_tools_with_interceptor 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

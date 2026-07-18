# `src/config/configuration.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/config/configuration.py`
- **模块导入名**：`src.config.configuration`
- **代码行数**：91
- **架构归属**：src/config —— 配置加载（`conf.yaml` / `.env`）、模型与工具开关、报告样式、智能体映射

## 模块概述

```text
LangGraph 运行时的可配置字段定义。

以 dataclass 形式集中声明 Configuration：包括研究资源、计划/步骤/搜索次数上限、
MCP 设置、报告风格、深度思考与各类搜索开关、工具中断名单、递归回退等运行期参数。
提供 from_runnable_config 类方法，优先从环境变量、其次从 RunnableConfig 的 configurable
字段读取并构造实例，是 DeerFlow 图执行时获取运行配置的统一入口。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.loader import get_bool_env, get_int_env, get_str_env`
- `from src.config.report_style import ReportStyle`
- `from src.rag.retriever import Resource`

**外部依赖**（第三方库 / 标准库）：

- `from dataclasses import dataclass, field, fields`
- `from typing import Any, Optional`
- `from langchain_core.runnables import RunnableConfig`
- `import logging`
- `import os`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 23 | `logging.getLogger(__name__)` |
| 函数 | `get_recursion_limit` | 26 | `(default: int=25) -> int` |
| 类 | `Configuration` | 50 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：23–23  |  **完整限定名**：`src.config.configuration.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `get_recursion_limit`

- **类型**：函数  |  **行号**：26–46  |  **完整限定名**：`src.config.configuration.get_recursion_limit`
- **签名**：

```python
def get_recursion_limit(default: int=25) -> int:
```

**摘要**：

Get the recursion limit from environment variable or use default.

**参数**：

```text
default: Default recursion limit if environment variable is not set or invalid
```

**返回值**：

```text
int: The recursion limit to use
```

### `Configuration`

- **类型**：类  |  **行号**：50–91  |  **完整限定名**：`src.config.configuration.Configuration`
- **装饰器**：`@dataclass`
- **定义**：

```python
class Configuration:
```
- **成员概览**：

  - `attr resources`
  - `attr max_plan_iterations`
  - `attr max_step_num`
  - `attr max_search_results`
  - `attr mcp_settings`
  - `attr report_style`
  - `attr enable_deep_thinking`
  - `attr enforce_web_search`
  - `attr enforce_researcher_search`
  - `attr enable_web_search`
  - `attr interrupt_before_tools`
  - `attr enable_recursion_fallback`
  - `def from_runnable_config`

**摘要**：

The configurable fields.

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`
- `src.prompts.template`
- `src.server.app`
- `src.workflow`
- `tests.integration.test_tool_interceptor_integration`
- `tests.unit.config.test_configuration`
- `tests.unit.graph.test_nodes_recursion_limit`

## 示例用法

```python
# src/config/configuration.py 示例用法
#
# Configuration 是 DeerFlow 的运行时配置对象，通过 RunnableConfig.configurable 传入。
#
# 1) 在节点中读取 Configuration
from src.config.configuration import Configuration
from langchain_core.runnables import RunnableConfig

def my_node(state, config: RunnableConfig):
    cfg = Configuration.from_runnable_config(config)
    print(cfg.max_plan_iterations)
    print(cfg.max_step_num)
    print(cfg.max_search_results)
    return {}

# 2) 构造带 Configuration 的 config
config: RunnableConfig = {
    "configurable": {
        "thread_id": "default",
        "max_plan_iterations": 2,
        "max_step_num": 5,
        "max_search_results": 10,
        "mcp_settings": {"servers": {}},
    },
    "recursion_limit": Configuration().recursion_limit,
}

# 3) 获取递归限制
from src.config.configuration import get_recursion_limit

limit = get_recursion_limit(default=100)
# 通常返回 100；可通过环境变量 RECURSION_LIMIT 覆盖

# 4) 直接实例化默认配置
cfg = Configuration()
print(cfg.max_plan_iterations)  # 默认 1
print(cfg.max_step_num)         # 默认 3
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

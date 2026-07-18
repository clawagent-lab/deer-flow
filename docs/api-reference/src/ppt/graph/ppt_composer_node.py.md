# `src/ppt/graph/ppt_composer_node.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/ppt/graph/ppt_composer_node.py`
- **模块导入名**：`src.ppt.graph.ppt_composer_node`
- **代码行数**：40
- **架构归属**：src/ppt —— PPT 生成子图（大纲生成器 + 内容编排器）

## 模块概述

```text
PPT 子图的内容撰写节点。

调用 LLM（基于 ppt_composer 配置）按指定 locale 的提示模板，
将输入文本转换为 PPT 内容（Markdown 形式），并将内容写入临时
.md 文件，供后续 ppt_generator 节点转换为 .pptx 文件。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.agents import AGENT_LLM_MAP`
- `from src.llms.llm import get_llm_by_type`
- `from src.prompts.template import get_prompt_template`
- `from .state import PPTState`

**外部依赖**（第三方库 / 标准库）：

- `from langchain_core.messages import HumanMessage, SystemMessage`
- `import logging`
- `import os`
- `import uuid`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 23 | `logging.getLogger(__name__)` |
| 函数 | `ppt_composer_node` | 26 | `(state: PPTState)` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：23–23  |  **完整限定名**：`src.ppt.graph.ppt_composer_node.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `ppt_composer_node`

- **类型**：函数  |  **行号**：26–40  |  **完整限定名**：`src.ppt.graph.ppt_composer_node.ppt_composer_node`
- **签名**：

```python
def ppt_composer_node(state: PPTState):
```

**说明**（自动推断）：

LangGraph 工作流节点函数，对应 `ppt_composer` 节点。接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，并返回需要合并回 State 的部分字典或 `Command` 对象。

## 调用关系（下游）

**被以下模块导入**：

- `src.ppt.graph.builder`

## 示例用法

```python
from src.ppt.graph.ppt_composer_node import ppt_composer_node
#
# TODO: 结合业务场景补充 ppt_composer_node 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

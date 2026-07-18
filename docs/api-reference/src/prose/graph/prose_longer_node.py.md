# `src/prose/graph/prose_longer_node.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prose/graph/prose_longer_node.py`
- **模块导入名**：`src.prose.graph.prose_longer_node`
- **代码行数**：32
- **架构归属**：src/prose —— 散文编辑子图（改写 improve、扩写 longer、缩写 shorter、修复 fix、续写 continue、精简 zap）

## 模块概述

```text
散文编辑（Prose）子图的"扩写"节点。

调用 prose_writer LLM，结合 prose_longer 提示模板对给定文本进行
扩写加长，在不改变原意的前提下增加内容丰富度，返回扩写后的内容。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.agents import AGENT_LLM_MAP`
- `from src.llms.llm import get_llm_by_type`
- `from src.prompts.template import get_prompt_template`
- `from src.prose.graph.state import ProseState`

**外部依赖**（第三方库 / 标准库）：

- `from langchain_core.messages import HumanMessage, SystemMessage`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 19 | `logging.getLogger(__name__)` |
| 函数 | `prose_longer_node` | 22 | `(state: ProseState)` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：19–19  |  **完整限定名**：`src.prose.graph.prose_longer_node.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `prose_longer_node`

- **类型**：函数  |  **行号**：22–32  |  **完整限定名**：`src.prose.graph.prose_longer_node.prose_longer_node`
- **签名**：

```python
def prose_longer_node(state: ProseState):
```

**说明**（自动推断）：

LangGraph 工作流节点函数，对应 `prose_longer` 节点。接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，并返回需要合并回 State 的部分字典或 `Command` 对象。

## 调用关系（下游）

**被以下模块导入**：

- `src.prose.graph.builder`

## 示例用法

```python
from src.prose.graph.prose_longer_node import prose_longer_node
#
# TODO: 结合业务场景补充 prose_longer_node 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

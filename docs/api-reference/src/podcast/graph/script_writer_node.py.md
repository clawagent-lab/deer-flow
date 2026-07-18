# `src/podcast/graph/script_writer_node.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/podcast/graph/script_writer_node.py`
- **模块导入名**：`src.podcast.graph.script_writer_node`
- **代码行数**：65
- **架构归属**：src/podcast —— 播客生成子图（脚本撰写 → TTS → 音频合成）

## 模块概述

```text
播客（Podcast）子图的脚本撰写节点。

调用 LLM（基于 podcast_script_writer 配置）将输入的原始文本转换为
结构化的双人对谈脚本（Script 对象，含男/女声与段落）。优先使用
json_mode 结构化输出，若模型不支持则回退到 JSON 修复解析流程。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.agents import AGENT_LLM_MAP`
- `from src.llms.llm import get_llm_by_type`
- `from src.prompts.template import get_prompt_template`
- `from src.utils.json_utils import repair_json_output`
- `from ..types import Script`
- `from .state import PodcastState`

**外部依赖**（第三方库 / 标准库）：

- `from langchain_core.messages import HumanMessage, SystemMessage`
- `import json`
- `import logging`
- `import openai`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 25 | `logging.getLogger(__name__)` |
| 函数 | `script_writer_node` | 28 | `(state: PodcastState)` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：25–25  |  **完整限定名**：`src.podcast.graph.script_writer_node.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `script_writer_node`

- **类型**：函数  |  **行号**：28–65  |  **完整限定名**：`src.podcast.graph.script_writer_node.script_writer_node`
- **签名**：

```python
def script_writer_node(state: PodcastState):
```

**说明**（自动推断）：

LangGraph 工作流节点函数，对应 `script_writer` 节点。接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，并返回需要合并回 State 的部分字典或 `Command` 对象。

## 调用关系（下游）

**被以下模块导入**：

- `src.podcast.graph.builder`
- `tests.unit.podcast.test_script_writer_node`

## 示例用法

```python
from src.podcast.graph.script_writer_node import script_writer_node
#
# TODO: 结合业务场景补充 script_writer_node 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

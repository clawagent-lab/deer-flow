# `src/podcast/graph/tts_node.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/podcast/graph/tts_node.py`
- **模块导入名**：`src.podcast.graph.tts_node`
- **代码行数**：54
- **架构归属**：src/podcast —— 播客生成子图（脚本撰写 → TTS → 音频合成）

## 模块概述

```text
播客（Podcast）子图的文本转语音（TTS）节点。

遍历脚本中每一行，按男/女声切换音色（BV002/BV001），调用火山引擎
VolcengineTTS 将段落合成为音频，base64 解码后追加到 audio_chunks
状态中，供后续音频合成节点使用。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.podcast.graph.state import PodcastState`
- `from src.tools.tts import VolcengineTTS`

**外部依赖**（第三方库 / 标准库）：

- `import base64`
- `import logging`
- `import os`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 18 | `logging.getLogger(__name__)` |
| 函数 | `tts_node` | 21 | `(state: PodcastState)` |
| 函数 | `_create_tts_client` | 40 | `()` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：18–18  |  **完整限定名**：`src.podcast.graph.tts_node.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `tts_node`

- **类型**：函数  |  **行号**：21–37  |  **完整限定名**：`src.podcast.graph.tts_node.tts_node`
- **签名**：

```python
def tts_node(state: PodcastState):
```

**说明**（自动推断）：

LangGraph 工作流节点函数，对应 `tts` 节点。接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，并返回需要合并回 State 的部分字典或 `Command` 对象。

### `_create_tts_client`

- **类型**：函数  |  **行号**：40–54  |  **完整限定名**：`src.podcast.graph.tts_node._create_tts_client`
- **签名**：

```python
def _create_tts_client():
```

**说明**（自动推断）：

私有工厂函数，创建 `tts_client` 实例，封装客户端构造细节。

## 调用关系（下游）

**被以下模块导入**：

- `src.podcast.graph.builder`

## 示例用法

```python
from src.podcast.graph.tts_node import tts_node
#
# TODO: 结合业务场景补充 tts_node 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

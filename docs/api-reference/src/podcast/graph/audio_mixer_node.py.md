# `src/podcast/graph/audio_mixer_node.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/podcast/graph/audio_mixer_node.py`
- **模块导入名**：`src.podcast.graph.audio_mixer_node`
- **代码行数**：22
- **架构归属**：src/podcast —— 播客生成子图（脚本撰写 → TTS → 音频合成）

## 模块概述

```text
播客（Podcast）子图的音频合成节点。

负责将 TTS 节点产出的多段音频字节流按顺序拼接为一段完整的播客音频，
作为播客工作流的末尾节点输出最终音频二进制内容。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.podcast.graph.state import PodcastState`

**外部依赖**（第三方库 / 标准库）：

- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 14 | `logging.getLogger(__name__)` |
| 函数 | `audio_mixer_node` | 17 | `(state: PodcastState)` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：14–14  |  **完整限定名**：`src.podcast.graph.audio_mixer_node.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `audio_mixer_node`

- **类型**：函数  |  **行号**：17–22  |  **完整限定名**：`src.podcast.graph.audio_mixer_node.audio_mixer_node`
- **签名**：

```python
def audio_mixer_node(state: PodcastState):
```

**说明**（自动推断）：

LangGraph 工作流节点函数，对应 `audio_mixer` 节点。接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，并返回需要合并回 State 的部分字典或 `Command` 对象。

## 调用关系（下游）

**被以下模块导入**：

- `src.podcast.graph.builder`

## 示例用法

```python
from src.podcast.graph.audio_mixer_node import audio_mixer_node
#
# TODO: 结合业务场景补充 audio_mixer_node 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

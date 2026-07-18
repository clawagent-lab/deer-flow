# `src/podcast/graph/state.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/podcast/graph/state.py`
- **模块导入名**：`src.podcast.graph.state`
- **代码行数**：28
- **架构归属**：src/podcast —— 播客生成子图（脚本撰写 → TTS → 音频合成）

## 模块概述

```text
播客（Podcast）子图的状态定义。

基于 LangGraph MessagesState 定义 PodcastState，承载播客生成流程的
输入文本、最终音频输出，以及中间资产（结构化脚本、音频分片列表）。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from ..types import Script`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Optional`
- `from langgraph.graph import MessagesState`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `PodcastState` | 17 | `` |

## 符号详解

### `PodcastState`

- **类型**：类  |  **行号**：17–28  |  **完整限定名**：`src.podcast.graph.state.PodcastState`
- **基类**：`MessagesState`
- **定义**：

```python
class PodcastState(MessagesState):
```
- **成员概览**：

  - `attr input`
  - `attr output`
  - `attr script`
  - `attr audio_chunks`

**摘要**：

State for the podcast generation.

## 调用关系（下游）

**被以下模块导入**：

- `src.podcast.graph.audio_mixer_node`
- `src.podcast.graph.builder`
- `src.podcast.graph.script_writer_node`
- `src.podcast.graph.tts_node`
- `src.ppt.graph.ppt_composer_node`

## 示例用法

```python
from src.podcast.graph.state import PodcastState
#
# TODO: 结合业务场景补充 PodcastState 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

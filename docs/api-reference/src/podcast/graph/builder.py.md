# `src/podcast/graph/builder.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/podcast/graph/builder.py`
- **模块导入名**：`src.podcast.graph.builder`
- **代码行数**：46
- **架构归属**：src/podcast —— 播客生成子图（脚本撰写 → TTS → 音频合成）

## 模块概述

```text
播客（Podcast）生成子图的构建模块。

基于 LangGraph StateGraph 组装播客生成工作流，依次串联：
脚本撰写（script_writer）→ 文本转语音（tts）→ 音频合成（audio_mixer），
最终 compile 为可调用的 workflow 实例。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.podcast.graph.audio_mixer_node import audio_mixer_node`
- `from src.podcast.graph.script_writer_node import script_writer_node`
- `from src.podcast.graph.state import PodcastState`
- `from src.podcast.graph.tts_node import tts_node`

**外部依赖**（第三方库 / 标准库）：

- `from langgraph.graph import END, START, StateGraph`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `build_graph` | 19 | `()` |
| 常量 | `workflow` | 33 | `build_graph()` |

## 符号详解

### `build_graph`

- **类型**：函数  |  **行号**：19–30  |  **完整限定名**：`src.podcast.graph.builder.build_graph`
- **签名**：

```python
def build_graph():
```

**摘要**：

Build and return the podcast workflow graph.

### `workflow`

- **类型**：模块常量  |  **行号**：33–33  |  **完整限定名**：`src.podcast.graph.builder.workflow`
- **值**：

```python
workflow = build_graph()
```

**说明**（自动推断）：

已编译的子图工作流实例，模块导入时构建，封装该子模块的完整处理流程。

## 调用关系（下游）

**被以下模块导入**：

- `src.graph`
- `src.rag`
- `src.server.app`

## 示例用法

```python
from src.podcast.graph.builder import build_graph
#
# TODO: 结合业务场景补充 build_graph 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

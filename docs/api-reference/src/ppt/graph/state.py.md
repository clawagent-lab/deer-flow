# `src/ppt/graph/state.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/ppt/graph/state.py`
- **模块导入名**：`src.ppt.graph.state`
- **代码行数**：26
- **架构归属**：src/ppt —— PPT 生成子图（大纲生成器 + 内容编排器）

## 模块概述

```text
PPT 子图的状态定义。

基于 LangGraph MessagesState 定义 PPTState，承载 PPT 生成流程的
输入文本、locale 设置、最终生成的文件路径，以及中间资产
（PPT 内容文本与临时 Markdown 文件路径）。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from langgraph.graph import MessagesState`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `PPTState` | 15 | `` |

## 符号详解

### `PPTState`

- **类型**：类  |  **行号**：15–26  |  **完整限定名**：`src.ppt.graph.state.PPTState`
- **基类**：`MessagesState`
- **定义**：

```python
class PPTState(MessagesState):
```
- **成员概览**：

  - `attr input`
  - `attr locale`
  - `attr generated_file_path`
  - `attr ppt_content`
  - `attr ppt_file_path`

**摘要**：

State for the ppt generation.

## 调用关系（下游）

**被以下模块导入**：

- `src.podcast.graph.script_writer_node`
- `src.ppt.graph.builder`
- `src.ppt.graph.ppt_composer_node`
- `src.ppt.graph.ppt_generator_node`

## 示例用法

```python
from src.ppt.graph.state import PPTState
#
# TODO: 结合业务场景补充 PPTState 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

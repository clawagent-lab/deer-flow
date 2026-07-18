# `src/prose/graph/state.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prose/graph/state.py`
- **模块导入名**：`src.prose.graph.state`
- **代码行数**：27
- **架构归属**：src/prose —— 散文编辑子图（改写 improve、扩写 longer、缩写 shorter、修复 fix、续写 continue、精简 zap）

## 模块概述

```text
散文编辑（Prose）子图的状态定义。

基于 LangGraph MessagesState 定义 ProseState，承载待编辑的散文内容、
操作选项（continue/improve/shorter/longer/fix/zap）、用户自定义命令，
以及编辑后的输出结果。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from langgraph.graph import MessagesState`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `ProseState` | 14 | `` |

## 符号详解

### `ProseState`

- **类型**：类  |  **行号**：14–27  |  **完整限定名**：`src.prose.graph.state.ProseState`
- **基类**：`MessagesState`
- **定义**：

```python
class ProseState(MessagesState):
```
- **成员概览**：

  - `attr content`
  - `attr option`
  - `attr command`
  - `attr output`

**摘要**：

State for the prose generation.

## 调用关系（下游）

**被以下模块导入**：

- `src.podcast.graph.script_writer_node`
- `src.ppt.graph.ppt_composer_node`
- `src.prose.graph.builder`
- `src.prose.graph.prose_continue_node`
- `src.prose.graph.prose_fix_node`
- `src.prose.graph.prose_improve_node`
- `src.prose.graph.prose_longer_node`
- `src.prose.graph.prose_shorter_node`
- `src.prose.graph.prose_zap_node`

## 示例用法

```python
from src.prose.graph.state import ProseState
#
# TODO: 结合业务场景补充 ProseState 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/ppt/graph/builder.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/ppt/graph/builder.py`
- **模块导入名**：`src.ppt.graph.builder`
- **代码行数**：38
- **架构归属**：src/ppt —— PPT 生成子图（大纲生成器 + 内容编排器）

## 模块概述

```text
PPT 生成子图的构建模块。

基于 LangGraph StateGraph 组装 PPT 生成工作流，依次串联：
内容撰写（ppt_composer）→ 文件生成（ppt_generator），
最终 compile 为可调用的 workflow 实例。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.ppt.graph.ppt_composer_node import ppt_composer_node`
- `from src.ppt.graph.ppt_generator_node import ppt_generator_node`
- `from src.ppt.graph.state import PPTState`

**外部依赖**（第三方库 / 标准库）：

- `from langgraph.graph import END, START, StateGraph`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `build_graph` | 18 | `()` |
| 常量 | `workflow` | 30 | `build_graph()` |

## 符号详解

### `build_graph`

- **类型**：函数  |  **行号**：18–27  |  **完整限定名**：`src.ppt.graph.builder.build_graph`
- **签名**：

```python
def build_graph():
```

**摘要**：

Build and return the ppt workflow graph.

### `workflow`

- **类型**：模块常量  |  **行号**：30–30  |  **完整限定名**：`src.ppt.graph.builder.workflow`
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
from src.ppt.graph.builder import build_graph
#
# TODO: 结合业务场景补充 build_graph 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/prose/graph/builder.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prose/graph/builder.py`
- **模块导入名**：`src.prose.graph.builder`
- **代码行数**：75
- **架构归属**：src/prose —— 散文编辑子图（改写 improve、扩写 longer、缩写 shorter、修复 fix、续写 continue、精简 zap）

## 模块概述

```text
散文编辑（Prose）子图的构建模块。

基于 LangGraph StateGraph 组装散文编辑工作流，包含 continue、improve、
shorter、longer、fix、zap 六个操作节点，通过条件边根据 state["option"]
动态路由到对应节点执行编辑。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.prose.graph.prose_continue_node import prose_continue_node`
- `from src.prose.graph.prose_fix_node import prose_fix_node`
- `from src.prose.graph.prose_improve_node import prose_improve_node`
- `from src.prose.graph.prose_longer_node import prose_longer_node`
- `from src.prose.graph.prose_shorter_node import prose_shorter_node`
- `from src.prose.graph.prose_zap_node import prose_zap_node`
- `from src.prose.graph.state import ProseState`

**外部依赖**（第三方库 / 标准库）：

- `from langgraph.graph import END, START, StateGraph`
- `import asyncio`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `optional_node` | 25 | `(state: ProseState)` |
| 函数 | `build_graph` | 29 | `()` |
| 异步函数 | `_test_workflow` | 55 | `()` |

## 符号详解

### `optional_node`

- **类型**：函数  |  **行号**：25–26  |  **完整限定名**：`src.prose.graph.builder.optional_node`
- **签名**：

```python
def optional_node(state: ProseState):
```

**说明**（自动推断）：

LangGraph 工作流节点函数，对应 `optional` 节点。接收当前 State 与 RunnableConfig，执行该节点的业务逻辑，并返回需要合并回 State 的部分字典或 `Command` 对象。

### `build_graph`

- **类型**：函数  |  **行号**：29–52  |  **完整限定名**：`src.prose.graph.builder.build_graph`
- **签名**：

```python
def build_graph():
```

**摘要**：

Build and return the ppt workflow graph.

### `_test_workflow`

- **类型**：异步函数  |  **行号**：55–67  |  **完整限定名**：`src.prose.graph.builder._test_workflow`
- **签名**：

```python
async def _test_workflow():
```

**说明**（自动推断）：

测试用工作流构建函数，用于在开发/测试环境验证子图编排正确性。

## 调用关系（下游）

**被以下模块导入**：

- `src.graph`
- `src.rag`
- `src.server.app`

## 示例用法

```python
from src.prose.graph.builder import build_graph
#
# TODO: 结合业务场景补充 build_graph 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

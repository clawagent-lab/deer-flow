# `src/prompt_enhancer/graph/builder.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prompt_enhancer/graph/builder.py`
- **模块导入名**：`src.prompt_enhancer.graph.builder`
- **代码行数**：31
- **架构归属**：src/prompt_enhancer —— 提示词增强子图（对用户输入做扩写/优化）

## 模块概述

```text
Prompt 增强子图的构建模块。

基于 LangGraph StateGraph 组装提示词增强工作流，仅包含单一 enhancer
节点作为入口与出口，compile 后返回可调用的图实例。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.prompt_enhancer.graph.enhancer_node import prompt_enhancer_node`
- `from src.prompt_enhancer.graph.state import PromptEnhancerState`

**外部依赖**（第三方库 / 标准库）：

- `from langgraph.graph import StateGraph`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `build_graph` | 16 | `()` |

## 符号详解

### `build_graph`

- **类型**：函数  |  **行号**：16–31  |  **完整限定名**：`src.prompt_enhancer.graph.builder.build_graph`
- **签名**：

```python
def build_graph():
```

**摘要**：

Build and return the prompt enhancer workflow graph.

## 调用关系（下游）

**被以下模块导入**：

- `src.graph`
- `src.rag`
- `src.server.app`
- `tests.unit.prompt_enhancer.graph.test_builder`

## 示例用法

```python
from src.prompt_enhancer.graph.builder import build_graph
#
# TODO: 结合业务场景补充 build_graph 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

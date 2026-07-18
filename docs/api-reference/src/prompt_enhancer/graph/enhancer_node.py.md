# `src/prompt_enhancer/graph/enhancer_node.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prompt_enhancer/graph/enhancer_node.py`
- **模块导入名**：`src.prompt_enhancer.graph.enhancer_node`
- **代码行数**：91
- **架构归属**：src/prompt_enhancer —— 提示词增强子图（对用户输入做扩写/优化）

## 模块概述

```text
Prompt 增强子图的核心节点。

调用 LLM（基于 prompt_enhancer 配置）结合上下文与报告风格偏好，
对用户原始 prompt 进行改写增强。优先从响应中提取
<enhanced_prompt> XML 标签内容，未匹配时回退到去除常见前缀的
容错解析；异常时返回原始 prompt。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.agents import AGENT_LLM_MAP`
- `from src.llms.llm import get_llm_by_type`
- `from src.prompt_enhancer.graph.state import PromptEnhancerState`
- `from src.prompts.template import apply_prompt_template`

**外部依赖**（第三方库 / 标准库）：

- `from langchain_core.messages import HumanMessage`
- `import logging`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 22 | `logging.getLogger(__name__)` |
| 函数 | `prompt_enhancer_node` | 25 | `(state: PromptEnhancerState)` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：22–22  |  **完整限定名**：`src.prompt_enhancer.graph.enhancer_node.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `prompt_enhancer_node`

- **类型**：函数  |  **行号**：25–91  |  **完整限定名**：`src.prompt_enhancer.graph.enhancer_node.prompt_enhancer_node`
- **签名**：

```python
def prompt_enhancer_node(state: PromptEnhancerState):
```

**摘要**：

Node that enhances user prompts using AI analysis.

## 调用关系（下游）

**被以下模块导入**：

- `src.prompt_enhancer.graph.builder`
- `tests.unit.prompt_enhancer.graph.test_enhancer_node`

## 示例用法

```python
from src.prompt_enhancer.graph.enhancer_node import prompt_enhancer_node
#
# TODO: 结合业务场景补充 prompt_enhancer_node 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

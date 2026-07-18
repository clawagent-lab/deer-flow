# `src/prompt_enhancer/graph/state.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/prompt_enhancer/graph/state.py`
- **模块导入名**：`src.prompt_enhancer.graph.state`
- **代码行数**：21
- **架构归属**：src/prompt_enhancer —— 提示词增强子图（对用户输入做扩写/优化）

## 模块概述

```text
Prompt 增强子图的状态定义。

使用 TypedDict 定义 PromptEnhancerState，承载待增强的原始 prompt、
可选上下文、报告风格偏好，以及增强后的输出结果。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.report_style import ReportStyle`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Optional, TypedDict`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `PromptEnhancerState` | 15 | `` |

## 符号详解

### `PromptEnhancerState`

- **类型**：类  |  **行号**：15–21  |  **完整限定名**：`src.prompt_enhancer.graph.state.PromptEnhancerState`
- **基类**：`TypedDict`
- **定义**：

```python
class PromptEnhancerState(TypedDict):
```
- **成员概览**：

  - `attr prompt`
  - `attr context`
  - `attr report_style`
  - `attr output`

**摘要**：

State for the prompt enhancer workflow.

## 调用关系（下游）

**被以下模块导入**：

- `src.podcast.graph.script_writer_node`
- `src.ppt.graph.ppt_composer_node`
- `src.prompt_enhancer.graph.builder`
- `src.prompt_enhancer.graph.enhancer_node`
- `tests.unit.prompt_enhancer.graph.test_builder`
- `tests.unit.prompt_enhancer.graph.test_enhancer_node`
- `tests.unit.prompt_enhancer.graph.test_state`

## 示例用法

```python
from src.prompt_enhancer.graph.state import PromptEnhancerState
#
# TODO: 结合业务场景补充 PromptEnhancerState 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

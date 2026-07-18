# `src/config/agents.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/config/agents.py`
- **模块导入名**：`src.config.agents`
- **代码行数**：28
- **架构归属**：src/config —— 配置加载（`conf.yaml` / `.env`）、模型与工具开关、报告样式、智能体映射

## 模块概述

```text
智能体与 LLM 类型的映射定义。

用 LLMType 字面量类型枚举可用的 LLM 类别（basic / reasoning / vision / code），
并通过 AGENT_LLM_MAP 将每个 agent 角色（coordinator、planner、researcher、coder 等）
映射到对应的 LLM 类型，供 create_agent 工厂函数选择模型时查表使用。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Literal`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `LLMType` | 14 | `Literal['basic', 'reasoning', 'vision', 'code']` |

## 符号详解

### `LLMType`

- **类型**：模块常量  |  **行号**：14–14  |  **完整限定名**：`src.config.agents.LLMType`
- **值**：

```python
LLMType = Literal['basic', 'reasoning', 'vision', 'code']
```

**说明**（自动推断）：

类型别名 `LLMType`，基于 `typing.Literal` 约束可选取值集合，供类型检查器与 IDE 自动补全使用。

## 调用关系（下游）

**被以下模块导入**：

- `src.agents`
- `src.agents.agents`
- `src.graph.nodes`
- `src.llms.llm`
- `src.podcast.graph.script_writer_node`
- `src.ppt.graph.ppt_composer_node`
- `src.prompt_enhancer.graph.enhancer_node`
- `src.prose.graph.prose_continue_node`
- `src.prose.graph.prose_fix_node`
- `src.prose.graph.prose_improve_node`
- `src.prose.graph.prose_longer_node`
- `src.prose.graph.prose_shorter_node`
- `src.prose.graph.prose_zap_node`

## 示例用法

```python
from src.config.agents import LLMType
#
# TODO: 结合业务场景补充 LLMType 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/agents/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/agents/__init__.py`
- **模块导入名**：`src.agents`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：12
- **架构归属**：src/agents —— 智能体构建与中间件（基于 LangChain 1.x `create_agent` + `AgentMiddleware`，封装动态提示词、工具拦截、模型钩子）

## 模块概述

```text
智能体（agent）子包入口，统一对外暴露 create_agent 工厂函数。

通过该包可以基于 agent 类型、工具列表和 prompt 模板快速创建配置一致的 LangChain 智能体，
供 DeerFlow 工作流中的各个节点（researcher、coder 等）按需调用。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .agents import create_agent`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`

## 示例用法

```python
# import src.agents
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

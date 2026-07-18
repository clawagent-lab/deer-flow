# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""智能体（agent）子包入口，统一对外暴露 create_agent 工厂函数。

通过该包可以基于 agent 类型、工具列表和 prompt 模板快速创建配置一致的 LangChain 智能体，
供 DeerFlow 工作流中的各个节点（researcher、coder 等）按需调用。
"""

from .agents import create_agent

__all__ = ["create_agent"]

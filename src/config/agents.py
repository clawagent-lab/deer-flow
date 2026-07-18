# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""智能体与 LLM 类型的映射定义。

用 LLMType 字面量类型枚举可用的 LLM 类别（basic / reasoning / vision / code），
并通过 AGENT_LLM_MAP 将每个 agent 角色（coordinator、planner、researcher、coder 等）
映射到对应的 LLM 类型，供 create_agent 工厂函数选择模型时查表使用。
"""

from typing import Literal

# Define available LLM types
LLMType = Literal["basic", "reasoning", "vision", "code"]

# Define agent-LLM mapping
AGENT_LLM_MAP: dict[str, LLMType] = {
    "coordinator": "basic",
    "planner": "basic",
    "researcher": "basic",
    "analyst": "basic",
    "coder": "basic",
    "reporter": "basic",
    "podcast_script_writer": "basic",
    "ppt_composer": "basic",
    "prose_writer": "basic",
    "prompt_enhancer": "basic",
}

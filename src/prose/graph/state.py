# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""散文编辑（Prose）子图的状态定义。

基于 LangGraph MessagesState 定义 ProseState，承载待编辑的散文内容、
操作选项（continue/improve/shorter/longer/fix/zap）、用户自定义命令，
以及编辑后的输出结果。
"""

from langgraph.graph import MessagesState


class ProseState(MessagesState):
    """State for the prose generation."""

    # The content of the prose
    content: str = ""

    # Prose writer option: continue, improve, shorter, longer, fix, zap
    option: str = ""

    # The user custom command for the prose writer
    command: str = ""

    # Output
    output: str = ""

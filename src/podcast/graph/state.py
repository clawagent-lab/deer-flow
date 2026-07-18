# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""播客（Podcast）子图的状态定义。

基于 LangGraph MessagesState 定义 PodcastState，承载播客生成流程的
输入文本、最终音频输出，以及中间资产（结构化脚本、音频分片列表）。
"""

from typing import Optional

from langgraph.graph import MessagesState

from ..types import Script


class PodcastState(MessagesState):
    """State for the podcast generation."""

    # Input
    input: str = ""

    # Output
    output: Optional[bytes] = None

    # Assets
    script: Optional[Script] = None
    audio_chunks: list[bytes] = []

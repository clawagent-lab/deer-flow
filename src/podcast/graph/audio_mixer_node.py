# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""播客（Podcast）子图的音频合成节点。

负责将 TTS 节点产出的多段音频字节流按顺序拼接为一段完整的播客音频，
作为播客工作流的末尾节点输出最终音频二进制内容。
"""

import logging

from src.podcast.graph.state import PodcastState

logger = logging.getLogger(__name__)


def audio_mixer_node(state: PodcastState):
    logger.info("Mixing audio chunks for podcast...")
    audio_chunks = state["audio_chunks"]
    combined_audio = b"".join(audio_chunks)
    logger.info("The podcast audio is now ready.")
    return {"output": combined_audio}

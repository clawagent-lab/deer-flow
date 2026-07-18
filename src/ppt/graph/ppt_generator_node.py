# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""PPT 子图的文件生成节点。

调用 marp CLI 将 composer 节点产出的 Markdown 内容文件转换为
.pptx 幻灯片文件，转换完成后删除临时 .md 文件，并返回生成文件的路径。
"""

import logging
import os
import subprocess
import uuid

from src.ppt.graph.state import PPTState

logger = logging.getLogger(__name__)


def ppt_generator_node(state: PPTState):
    logger.info("Generating ppt file...")
    # use marp cli to generate ppt file
    # https://github.com/marp-team/marp-cli?tab=readme-ov-file
    generated_file_path = os.path.join(
        os.getcwd(), f"generated_ppt_{uuid.uuid4()}.pptx"
    )
    subprocess.run(["marp", state["ppt_file_path"], "-o", generated_file_path])
    # remove the temp file
    os.remove(state["ppt_file_path"])
    logger.info(f"generated_file_path: {generated_file_path}")
    return {"generated_file_path": generated_file_path}

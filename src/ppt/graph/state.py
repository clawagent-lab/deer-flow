# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""PPT 子图的状态定义。

基于 LangGraph MessagesState 定义 PPTState，承载 PPT 生成流程的
输入文本、locale 设置、最终生成的文件路径，以及中间资产
（PPT 内容文本与临时 Markdown 文件路径）。
"""


from langgraph.graph import MessagesState


class PPTState(MessagesState):
    """State for the ppt generation."""

    # Input
    input: str = ""
    locale: str = ""
    # Output
    generated_file_path: str = ""

    # Assets
    ppt_content: str = ""
    ppt_file_path: str = ""

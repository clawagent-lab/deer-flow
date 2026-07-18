# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""散文编辑（Prose）子图的"改进"节点。

调用 prose_writer LLM，结合 prose_improver 提示模板对给定文本进行
润色改进，提升表达质量与可读性，返回改进后的内容。
"""

import logging

from langchain_core.messages import HumanMessage, SystemMessage

from src.config.agents import AGENT_LLM_MAP
from src.llms.llm import get_llm_by_type
from src.prompts.template import get_prompt_template
from src.prose.graph.state import ProseState

logger = logging.getLogger(__name__)


def prose_improve_node(state: ProseState):
    logger.info("Generating prose improve content...")
    model = get_llm_by_type(AGENT_LLM_MAP["prose_writer"])
    prose_content = model.invoke(
        [
            SystemMessage(content=get_prompt_template("prose/prose_improver")),
            HumanMessage(content=f"The existing text is: {state['content']}"),
        ],
    )
    logger.info(f"prose_content: {prose_content}")
    return {"output": prose_content.content}

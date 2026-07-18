# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""散文编辑（Prose）子图的"续写"节点。

调用 prose_writer LLM，结合 prose_continue 提示模板对给定文本进行
续写扩展，返回续写后的内容。
"""

import logging

from langchain_core.messages import HumanMessage, SystemMessage

from src.config.agents import AGENT_LLM_MAP
from src.llms.llm import get_llm_by_type
from src.prompts.template import get_prompt_template
from src.prose.graph.state import ProseState

logger = logging.getLogger(__name__)


def prose_continue_node(state: ProseState):
    logger.info("Generating prose continue content...")
    model = get_llm_by_type(AGENT_LLM_MAP["prose_writer"])
    prose_content = model.invoke(
        [
            SystemMessage(content=get_prompt_template("prose/prose_continue")),
            HumanMessage(content=state["content"]),
        ],
    )
    return {"output": prose_content.content}

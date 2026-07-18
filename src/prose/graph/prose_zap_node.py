# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""散文编辑（Prose）子图的"自定义指令"节点。

调用 prose_writer LLM，结合 prose_zap 提示模板，根据用户在
state["command"] 中指定的自定义指令对文本执行任意编辑操作，
返回处理后的内容。
"""

import logging

from langchain_core.messages import HumanMessage, SystemMessage

from src.config.agents import AGENT_LLM_MAP
from src.llms.llm import get_llm_by_type
from src.prompts.template import get_prompt_template
from src.prose.graph.state import ProseState

logger = logging.getLogger(__name__)


def prose_zap_node(state: ProseState):
    logger.info("Generating prose zap content...")
    model = get_llm_by_type(AGENT_LLM_MAP["prose_writer"])
    prose_content = model.invoke(
        [
            SystemMessage(content=get_prompt_template("prose/prose_zap")),
            HumanMessage(
                content=f"For this text: {state['content']}.\nYou have to respect the command: {state['command']}"
            ),
        ],
    )
    logger.info(f"prose_content: {prose_content}")
    return {"output": prose_content.content}

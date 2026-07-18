# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT
"""Prompts 模块包。

统一对外暴露提示词模板的加载与应用能力，包括 ``get_prompt_template`` 与
``apply_prompt_template``，供各智能体按名称获取 Jinja2 渲染后的提示消息。
"""

from .template import apply_prompt_template, get_prompt_template

__all__ = [
    "apply_prompt_template",
    "get_prompt_template",
]

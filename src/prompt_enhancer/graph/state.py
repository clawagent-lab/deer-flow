# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""Prompt 增强子图的状态定义。

使用 TypedDict 定义 PromptEnhancerState，承载待增强的原始 prompt、
可选上下文、报告风格偏好，以及增强后的输出结果。
"""

from typing import Optional, TypedDict

from src.config.report_style import ReportStyle


class PromptEnhancerState(TypedDict):
    """State for the prompt enhancer workflow."""

    prompt: str  # Original prompt to enhance
    context: Optional[str]  # Additional context
    report_style: Optional[ReportStyle]  # Report style preference
    output: Optional[str]  # Enhanced prompt result

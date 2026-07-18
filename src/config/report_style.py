# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""报告样式枚举：定义最终报告支持的几种写作风格（学术、科普、新闻、社交媒体、战略投资）。"""

import enum


class ReportStyle(enum.Enum):
    ACADEMIC = "academic"
    POPULAR_SCIENCE = "popular_science"
    NEWS = "news"
    SOCIAL_MEDIA = "social_media"
    STRATEGIC_INVESTMENT = "strategic_investment"

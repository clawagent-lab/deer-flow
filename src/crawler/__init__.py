# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""网页爬取与正文抽取包入口：导出 ``Article``、``Crawler``、``JinaClient``、``ReadabilityExtractor`` 四个核心组件，统一对外提供 URL 抓取与可读内容提取能力。"""

from .article import Article
from .crawler import Crawler
from .jina_client import JinaClient
from .readability_extractor import ReadabilityExtractor

__all__ = ["Article", "Crawler", "JinaClient", "ReadabilityExtractor"]

# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""正文抽取模块：``ReadabilityExtractor`` 基于 readabilipy/Readability 算法从原始 HTML 中提取标题与正文，封装为 ``Article`` 返回。"""

import logging

from readabilipy import simple_json_from_html_string

from .article import Article

logger = logging.getLogger(__name__)


class ReadabilityExtractor:
    def extract_article(self, html: str) -> Article:
        article = simple_json_from_html_string(html, use_readability=True)
        
        content = article.get("content")
        if not content or not str(content).strip():
            logger.warning("Readability extraction returned empty content")
            content = "<p>No content could be extracted from this page</p>"
        
        title = article.get("title")
        if not title or not str(title).strip():
            title = "Untitled"
        
        return Article(
            title=title,
            html_content=content,
        )

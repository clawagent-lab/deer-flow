# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""工具开关配置：定义搜索引擎、爬虫引擎、RAG 提供方的枚举，并通过环境变量读取当前选中项。"""

import enum
import os

from dotenv import load_dotenv

load_dotenv()


class SearchEngine(enum.Enum):
    TAVILY = "tavily"
    INFOQUEST = "infoquest"
    DUCKDUCKGO = "duckduckgo"
    BRAVE_SEARCH = "brave_search"
    ARXIV = "arxiv"
    SEARX = "searx"
    WIKIPEDIA = "wikipedia"
    SERPER = "serper"


class CrawlerEngine(enum.Enum):
    JINA = "jina"
    INFOQUEST = "infoquest"


# Tool configuration
SELECTED_SEARCH_ENGINE = os.getenv("SEARCH_API", SearchEngine.TAVILY.value)


class RAGProvider(enum.Enum):
    DIFY = "dify"
    RAGFLOW = "ragflow"
    VIKINGDB_KNOWLEDGE_BASE = "vikingdb_knowledge_base"
    MOI = "moi"
    MILVUS = "milvus"
    QDRANT = "qdrant"


SELECTED_RAG_PROVIDER = os.getenv("RAG_PROVIDER")

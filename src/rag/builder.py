# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""RAG 检索器工厂。

根据 ``src.config.tools.SELECTED_RAG_PROVIDER`` 配置项，构造并返回对应的
``Retriever`` 实现（Dify / RAGFlow / MOI / VikingDB / Milvus / Qdrant）。
未配置或为空时返回 ``None``，表示不启用 RAG 增强。
"""

from src.config.tools import SELECTED_RAG_PROVIDER, RAGProvider
from src.rag.dify import DifyProvider
from src.rag.milvus import MilvusProvider
from src.rag.moi import MOIProvider
from src.rag.qdrant import QdrantProvider
from src.rag.ragflow import RAGFlowProvider
from src.rag.retriever import Retriever
from src.rag.vikingdb_knowledge_base import VikingDBKnowledgeBaseProvider


def build_retriever() -> Retriever | None:
    if SELECTED_RAG_PROVIDER == RAGProvider.DIFY.value:
        return DifyProvider()
    if SELECTED_RAG_PROVIDER == RAGProvider.RAGFLOW.value:
        return RAGFlowProvider()
    elif SELECTED_RAG_PROVIDER == RAGProvider.MOI.value:
        return MOIProvider()
    elif SELECTED_RAG_PROVIDER == RAGProvider.VIKINGDB_KNOWLEDGE_BASE.value:
        return VikingDBKnowledgeBaseProvider()
    elif SELECTED_RAG_PROVIDER == RAGProvider.MILVUS.value:
        return MilvusProvider()
    elif SELECTED_RAG_PROVIDER == RAGProvider.QDRANT.value:
        return QdrantProvider()
    elif SELECTED_RAG_PROVIDER:
        raise ValueError(f"Unsupported RAG provider: {SELECTED_RAG_PROVIDER}")
    return None

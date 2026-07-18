# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT
"""RAG（检索增强生成）模块包。

统一聚合各检索后端的 Provider 实现与抽象基类：对外暴露 ``Retriever``、
``Document``、``Chunk``、``Resource`` 等核心类型，以及 ``build_retriever``
工厂，按配置（Dify / RAGFlow / Milvus / Qdrant / MOI / VikingDB 等）
构造对应的检索器实例。
"""

from .builder import build_retriever
from .dify import DifyProvider
from .milvus import MilvusProvider
from .moi import MOIProvider
from .qdrant import QdrantProvider
from .ragflow import RAGFlowProvider
from .retriever import Chunk, Document, Resource, Retriever
from .vikingdb_knowledge_base import VikingDBKnowledgeBaseProvider

__all__ = [
    "Retriever",
    "Document",
    "Resource",
    "DifyProvider",
    "RAGFlowProvider",
    "MOIProvider",
    "MilvusProvider",
    "QdrantProvider",
    "VikingDBKnowledgeBaseProvider",
    "Chunk",
    "build_retriever",
]

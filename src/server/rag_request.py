# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""RAG 相关请求/响应 Pydantic 模型。

定义 ``RAGConfigResponse``（返回当前 RAG provider，如 ragflow）、
``RAGResourceRequest``（按 query 检索资源）与 ``RAGResourcesResponse``
（返回 ``Resource`` 列表），用于 RAG 配置查询与知识库资源检索接口。
"""

from pydantic import BaseModel, Field

from src.rag.retriever import Resource


class RAGConfigResponse(BaseModel):
    """Response model for RAG config."""

    provider: str | None = Field(
        None, description="The provider of the RAG, default is ragflow"
    )


class RAGResourceRequest(BaseModel):
    """Request model for RAG resource."""

    query: str | None = Field(
        None, description="The query of the resource need to be searched"
    )


class RAGResourcesResponse(BaseModel):
    """Response model for RAG resources."""

    resources: list[Resource] = Field(..., description="The resources of the RAG")

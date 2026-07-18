# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""服务端配置响应模型。

定义 ``ConfigResponse`` Pydantic 模型，向客户端返回 RAG 配置
（``RAGConfigResponse``）与可用 LLM 模型清单等运行期配置信息。
"""

from pydantic import BaseModel, Field

from src.server.rag_request import RAGConfigResponse


class ConfigResponse(BaseModel):
    """Response model for server config."""

    rag: RAGConfigResponse = Field(..., description="The config of the RAG")
    models: dict[str, list[str]] = Field(..., description="The configured models")

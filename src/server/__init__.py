# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

"""FastAPI 服务端包入口。

导出核心 FastAPI 应用实例 ``app``，供 uvicorn 等 ASGI 服务器启动使用。
"""

from .app import app

__all__ = ["app"]

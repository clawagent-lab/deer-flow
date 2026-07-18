# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT
"""DeerFlow 项目根包初始化模块。

主要负责在导入早期设置 Windows 平台的事件循环策略，
以确保 psycopg（PostgreSQL 驱动）在 Windows 下使用 selector 事件循环而非默认的 ProactorEventLoop，
从而避免异步数据库连接出现兼容性问题。
"""

import asyncio
import os


# Configure Windows event loop policy for PostgreSQL compatibility
# On Windows, psycopg requires a selector-based event loop, not the default ProactorEventLoop
# This must be set at the earliest possible point before any event loop is created
if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# `src/graph/checkpoint.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/graph/checkpoint.py`
- **模块导入名**：`src.graph.checkpoint`
- **代码行数**：395
- **架构归属**：src/graph —— LangGraph 主工作流：节点、状态、边、checkpoint、工具函数

## 模块概述

```text
会话检查点与消息流管理模块：``ChatStreamManager`` 结合 InMemoryStore 与 MongoDB/PostgreSQL 持久化聊天消息分片，并在会话结束时合并归档。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.loader import get_bool_env, get_str_env`

**外部依赖**（第三方库 / 标准库）：

- `from datetime import datetime`
- `from typing import List, Optional, Tuple`
- `from langgraph.store.memory import InMemoryStore`
- `from psycopg.rows import dict_row`
- `from pymongo import MongoClient`
- `import json`
- `import logging`
- `import uuid`
- `import psycopg`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `ChatStreamManager` | 20 | `` |
| 函数 | `chat_stream_message` | 377 | `(thread_id: str, message: str, finish_reason: str) -> bool` |

## 符号详解

### `ChatStreamManager`

- **类型**：类  |  **行号**：20–366  |  **完整限定名**：`src.graph.checkpoint.ChatStreamManager`
- **定义**：

```python
class ChatStreamManager:
```
- **成员概览**：

  - `def __init__`
  - `def _init_mongodb`
  - `def _init_postgresql`
  - `def _create_chat_streams_table`
  - `def process_stream_message`
  - `def _persist_complete_conversation`
  - `def _persist_to_mongodb`
  - `def _persist_to_postgresql`
  - `def close`
  - `def __enter__`
  - `def __exit__`

**摘要**：

Manages chat stream messages with persistent storage and in-memory caching.

**属性**：

```text
store (InMemoryStore): In-memory storage for temporary message chunks
    mongo_client (MongoClient): MongoDB client connection
    mongo_db (Database): MongoDB database instance
    postgres_conn (psycopg.Connection): PostgreSQL connection
    logger (logging.Logger): Logger instance for this class
```

### `chat_stream_message`

- **类型**：函数  |  **行号**：377–395  |  **完整限定名**：`src.graph.checkpoint.chat_stream_message`
- **签名**：

```python
def chat_stream_message(thread_id: str, message: str, finish_reason: str) -> bool:
```

**摘要**：

Legacy function wrapper for backward compatibility.

**参数**：

```text
thread_id: Unique identifier for the conversation thread
    message: The message content to store
    finish_reason: Reason for message completion
```

**返回值**：

```text
bool: True if message was processed successfully
```

## 调用关系（下游）

**被以下模块导入**：

- `src.server.app`
- `tests.unit.checkpoint.test_checkpoint`
- `tests.unit.checkpoint.test_memory_leak`

## 示例用法

```python
from src.graph.checkpoint import chat_stream_message
#
# TODO: 结合业务场景补充 chat_stream_message 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

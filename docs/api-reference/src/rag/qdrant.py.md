# `src/rag/qdrant.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/qdrant.py`
- **模块导入名**：`src.rag.qdrant`
- **代码行数**：531
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
Qdrant 向量数据库的 RAG 检索器适配实现。

提供基于 Qdrant 的本地知识库能力：内置 ``DashscopeEmbeddings``（OpenAI
兼容接口的 Embedding 封装）与 ``QdrantProvider``，负责集合创建、文档分块
入库、带过滤条件的相似度检索，以及将项目示例 markdown 资源注册为可检索项。
常量 ``SCROLL_SIZE`` 控制滚动分页的批量大小。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.loader import get_bool_env, get_int_env, get_str_env`
- `from src.rag.retriever import Chunk, Document, Resource, Retriever`

**外部依赖**（第三方库 / 标准库）：

- `from pathlib import Path`
- `from typing import Any, Dict, List, Optional, Sequence, Set`
- `from langchain_openai import OpenAIEmbeddings`
- `from langchain_qdrant import QdrantVectorStore`
- `from openai import OpenAI`
- `from qdrant_client import QdrantClient, grpc`
- `from qdrant_client.models import Distance, FieldCondition, Filter, MatchValue, PointStruct, VectorParams`
- `import asyncio`
- `import hashlib`
- `import logging`
- `import uuid`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 35 | `logging.getLogger(__name__)` |
| 常量 | `SCROLL_SIZE` | 37 | `64` |
| 类 | `DashscopeEmbeddings` | 40 | `` |
| 类 | `QdrantProvider` | 67 | `` |
| 函数 | `load_examples` | 526 | `() -> None` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：35–35  |  **完整限定名**：`src.rag.qdrant.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `SCROLL_SIZE`

- **类型**：模块常量  |  **行号**：37–37  |  **完整限定名**：`src.rag.qdrant.SCROLL_SIZE`
- **值**：

```python
SCROLL_SIZE = 64
```

**说明**（自动推断）：

数值上限常量 `SCROLL_SIZE`，用于约束对应操作的规模或阈值。

### `DashscopeEmbeddings`

- **类型**：类  |  **行号**：40–64  |  **完整限定名**：`src.rag.qdrant.DashscopeEmbeddings`
- **定义**：

```python
class DashscopeEmbeddings:
```
- **成员概览**：

  - `def __init__`
  - `def _embed`
  - `def embed_query`
  - `def embed_documents`

**说明**（自动推断）：

嵌入模型类 `DashscopeEmbeddings`，实现 LangChain Embeddings 接口，将文本转向量供向量库使用。

### `QdrantProvider`

- **类型**：类  |  **行号**：67–523  |  **完整限定名**：`src.rag.qdrant.QdrantProvider`
- **基类**：`Retriever`
- **定义**：

```python
class QdrantProvider(Retriever):
```
- **成员概览**：

  - `def __init__`
  - `def _init_embedding_model`
  - `def _get_embedding_dimension`
  - `def _ensure_collection_exists`
  - `def _load_example_files`
  - `def _generate_doc_id`
  - `def _extract_title_from_markdown`
  - `def _split_content`
  - `def _string_to_uuid`
  - `def _scroll_all_points`
  - `def _get_existing_document_ids`
  - `def _insert_document_chunk`
  - `def _connect`
  - `def _get_embedding`
  - `def list_resources`
  - `async def list_resources_async`
  - `def _list_local_markdown_resources`
  - `def query_relevant_documents`
  - `async def query_relevant_documents_async`
  - `def create_collection`
  - `def load_examples`
  - `def _clear_example_documents`
  - `def get_loaded_examples`
  - `def close`
  - `def __del__`

**说明**（自动推断）：

RAG 后端 Provider 类 `QdrantProvider`，实现检索器接口，封装对应向量库的连接、写入与查询逻辑。

### `load_examples`

- **类型**：函数  |  **行号**：526–531  |  **完整限定名**：`src.rag.qdrant.load_examples`
- **签名**：

```python
def load_examples() -> None:
```

**说明**（自动推断）：

加载示例文档集合，用于向向量库写入初始语料以便测试与演示。

## 调用关系（下游）

**被以下模块导入**：

- `src.rag`
- `src.rag.builder`
- `src.server.app`
- `tests.unit.rag.test_qdrant`

## 示例用法

```python
from src.rag.qdrant import load_examples
#
# TODO: 结合业务场景补充 load_examples 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

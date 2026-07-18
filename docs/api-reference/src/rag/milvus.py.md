# `src/rag/milvus.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/milvus.py`
- **模块导入名**：`src.rag.milvus`
- **代码行数**：983
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
Milvus 向量数据库的 RAG 检索器适配实现。

提供基于 Milvus（本地 Lite 或远端服务）的本地知识库能力：内置
``DashscopeEmbeddings``（OpenAI 兼容接口的 Embedding 封装）与
``MilvusRetriever``，负责集合 schema 定义、文档分块入库、相似度检索，
以及自动扫描项目示例 markdown 作为可检索资源。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.loader import get_bool_env, get_int_env, get_str_env`
- `from src.rag.retriever import Chunk, Document, Resource, Retriever`

**外部依赖**（第三方库 / 标准库）：

- `from pathlib import Path`
- `from typing import Any, Dict, Iterable, List, Optional, Sequence, Set`
- `from langchain_milvus.vectorstores import Milvus`
- `from langchain_openai import OpenAIEmbeddings`
- `from openai import OpenAI`
- `from pymilvus import CollectionSchema, DataType, FieldSchema, MilvusClient`
- `import asyncio`
- `import hashlib`
- `import logging`
- `import re`
- `import time`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 28 | `logging.getLogger(__name__)` |
| 类 | `DashscopeEmbeddings` | 31 | `` |
| 类 | `MilvusRetriever` | 63 | `` |
| 类 | `MilvusProvider` | 972 | `` |
| 函数 | `load_examples` | 978 | `() -> None` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：28–28  |  **完整限定名**：`src.rag.milvus.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `DashscopeEmbeddings`

- **类型**：类  |  **行号**：31–60  |  **完整限定名**：`src.rag.milvus.DashscopeEmbeddings`
- **定义**：

```python
class DashscopeEmbeddings:
```
- **成员概览**：

  - `def __init__`
  - `def _embed`
  - `def embed_query`
  - `def embed_documents`

**摘要**：

OpenAI-compatible embeddings wrapper.

### `MilvusRetriever`

- **类型**：类  |  **行号**：63–968  |  **完整限定名**：`src.rag.milvus.MilvusRetriever`
- **基类**：`Retriever`
- **定义**：

```python
class MilvusRetriever(Retriever):
```
- **成员概览**：

  - `def __init__`
  - `def _init_embedding_model`
  - `def _get_embedding_dimension`
  - `def _create_collection_schema`
  - `def _ensure_collection_exists`
  - `def _load_example_files`
  - `def _generate_doc_id`
  - `def _extract_title_from_markdown`
  - `def _split_content`
  - `def _get_existing_document_ids`
  - `def _insert_document_chunk`
  - `def _connect`
  - `def _is_milvus_lite`
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
  - `def _sanitize_filename`
  - `def _check_duplicate_file`
  - `def ingest_file`
  - `def __del__`

**摘要**：

Retriever implementation backed by a Milvus vector store.

**responsibilities**：

```text
* Initialize / lazily connect to Milvus (local Lite or remote server).
    * Provide methods for inserting content chunks & querying similarity.
    * Optionally surface example markdown resources found in the project.
Environment variables (selected):
    MILVUS_URI: Connection URI or local *.db path for Milvus Lite.
    MILVUS_COLLECTION: Target collection name (default: documents).
    MILVUS_TOP_K: Result set size (default: 10).
    MILVUS_EMBEDDING_PROVIDER: openai | dashscope (default: openai).
    MILVUS_EMBEDDING_MODEL: Embedding model name.
    MILVUS_EMBEDDING_DIM: Override embedding dimensionality.
    MILVUS_AUTO_LOAD_EXAMPLES: Load example *.md files if true.
    MILVUS_EXAMPLES_DIR: Folder containing example markdown files.
```

### `MilvusProvider`

- **类型**：类  |  **行号**：972–975  |  **完整限定名**：`src.rag.milvus.MilvusProvider`
- **基类**：`MilvusRetriever`
- **定义**：

```python
class MilvusProvider(MilvusRetriever):
```

**摘要**：

Backward compatible alias for ``MilvusRetriever`` (original name).

### `load_examples`

- **类型**：函数  |  **行号**：978–983  |  **完整限定名**：`src.rag.milvus.load_examples`
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
- `tests.unit.rag.test_milvus`

## 示例用法

```python
from src.rag.milvus import load_examples
#
# TODO: 结合业务场景补充 load_examples 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

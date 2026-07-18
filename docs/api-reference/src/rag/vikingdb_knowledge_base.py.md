# `src/rag/vikingdb_knowledge_base.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/vikingdb_knowledge_base.py`
- **模块导入名**：`src.rag.vikingdb_knowledge_base`
- **代码行数**：325
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
基于火山引擎 VikingDB 知识库的检索器实现模块。

定义 ``VikingDBKnowledgeBaseProvider``，继承自 ``Retriever``，
通过火山引擎 V4 风格的 HMAC-SHA256 签名调用 VikingDB 知识库检索接口，
返回 ``Chunk`` / ``Document`` / ``Resource`` 等 RAG 检索结果，
相关 endpoint、AK/SK 与 region 通过环境变量配置。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.rag.retriever import Chunk, Document, Resource, Retriever`

**外部依赖**（第三方库 / 标准库）：

- `from datetime import datetime`
- `from urllib.parse import urlparse`
- `import asyncio`
- `import hashlib`
- `import hmac`
- `import json`
- `import os`
- `import urllib.parse`
- `import requests`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `VikingDBKnowledgeBaseProvider` | 25 | `` |
| 函数 | `parse_uri` | 321 | `(uri: str) -> tuple[str, str]` |

## 符号详解

### `VikingDBKnowledgeBaseProvider`

- **类型**：类  |  **行号**：25–318  |  **完整限定名**：`src.rag.vikingdb_knowledge_base.VikingDBKnowledgeBaseProvider`
- **基类**：`Retriever`
- **定义**：

```python
class VikingDBKnowledgeBaseProvider(Retriever):
```
- **成员概览**：

  - `attr api_url`
  - `attr api_ak`
  - `attr api_sk`
  - `attr retrieval_size`
  - `attr region`
  - `attr service`
  - `def __init__`
  - `def _hmac_sha256`
  - `def _hash_sha256`
  - `def _get_signed_key`
  - `def _create_canonical_request`
  - `def _create_signature`
  - `def _make_signed_request`
  - `def query_relevant_documents`
  - `async def query_relevant_documents_async`
  - `def list_resources`
  - `async def list_resources_async`

**摘要**：

VikingDBKnowledgeBaseProvider is a provider that uses VikingDB Knowledge base API to retrieve documents.

### `parse_uri`

- **类型**：函数  |  **行号**：321–325  |  **完整限定名**：`src.rag.vikingdb_knowledge_base.parse_uri`
- **签名**：

```python
def parse_uri(uri: str) -> tuple[str, str]:
```

**说明**（自动推断）：

解析 RAG 后端的 URI 字符串，拆分出 scheme、host、port、collection 等组成部分，供对应的 retriever 构造客户端时使用。

## 调用关系（下游）

**被以下模块导入**：

- `src.rag`
- `src.rag.builder`
- `tests.unit.rag.test_vikingdb_knowledge_base`

## 示例用法

```python
from src.rag.vikingdb_knowledge_base import parse_uri
#
# TODO: 结合业务场景补充 parse_uri 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

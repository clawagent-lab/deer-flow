# `src/rag/ragflow.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/ragflow.py`
- **模块导入名**：`src.rag.ragflow`
- **代码行数**：163
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
RAGFlow 平台的 RAG 检索器适配实现。

``RAGFlowProvider`` 继承 ``Retriever``，通过 RAGFlow 的检索 API 按
``Resource.uri`` 解析出的 dataset/document 进行检索，支持配置
``RAGFLOW_PAGE_SIZE`` 控制每页返回数量，以及 ``RAGFLOW_CROSS_LANGUAGES``
指定跨语言检索范围，将结果映射为统一的 ``Document`` / ``Chunk`` 模型。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.rag.retriever import Chunk, Document, Resource, Retriever`

**外部依赖**（第三方库 / 标准库）：

- `from typing import List, Optional`
- `from urllib.parse import urlparse`
- `import asyncio`
- `import os`
- `import requests`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `RAGFlowProvider` | 22 | `` |
| 函数 | `parse_uri` | 159 | `(uri: str) -> tuple[str, str]` |

## 符号详解

### `RAGFlowProvider`

- **类型**：类  |  **行号**：22–156  |  **完整限定名**：`src.rag.ragflow.RAGFlowProvider`
- **基类**：`Retriever`
- **定义**：

```python
class RAGFlowProvider(Retriever):
```
- **成员概览**：

  - `attr api_url`
  - `attr api_key`
  - `attr page_size`
  - `attr cross_languages`
  - `def __init__`
  - `def query_relevant_documents`
  - `async def query_relevant_documents_async`
  - `def list_resources`
  - `async def list_resources_async`

**摘要**：

RAGFlowProvider is a provider that uses RAGFlow to retrieve documents.

### `parse_uri`

- **类型**：函数  |  **行号**：159–163  |  **完整限定名**：`src.rag.ragflow.parse_uri`
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
- `tests.unit.rag.test_ragflow`

## 示例用法

```python
from src.rag.ragflow import parse_uri
#
# TODO: 结合业务场景补充 parse_uri 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

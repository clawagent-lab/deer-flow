# `src/rag/retriever.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/retriever.py`
- **模块导入名**：`src.rag.retriever`
- **代码行数**：164
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
RAG 检索器的核心抽象与数据模型。

定义检索增强生成的基础类型契约：
- ``Chunk``：文档分块及其相似度分数；
- ``Document``：聚合多个 ``Chunk`` 的文档，可序列化为 dict；
- ``Resource``：Pydantic 模型，描述可检索资源的 URI/标题/描述；
- ``Retriever``：抽象基类，规定 ``list_resources`` / ``query_relevant_documents``
  等同步与异步接口，各后端 Provider 继承并实现具体逻辑。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from pydantic import BaseModel, Field`
- `import abc`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `Chunk` | 19 | `` |
| 类 | `Document` | 28 | `` |
| 类 | `Resource` | 62 | `` |
| 类 | `Retriever` | 72 | `` |

## 符号详解

### `Chunk`

- **类型**：类  |  **行号**：19–25  |  **完整限定名**：`src.rag.retriever.Chunk`
- **定义**：

```python
class Chunk:
```
- **成员概览**：

  - `attr content`
  - `attr similarity`
  - `def __init__`

**说明**（自动推断）：

检索分块数据类，承载一段文档的文本、元数据与来源信息。

### `Document`

- **类型**：类  |  **行号**：28–59  |  **完整限定名**：`src.rag.retriever.Document`
- **定义**：

```python
class Document:
```
- **成员概览**：

  - `attr id`
  - `attr url`
  - `attr title`
  - `attr chunks`
  - `def __init__`
  - `def to_dict`

**摘要**：

Document is a class that represents a document.

### `Resource`

- **类型**：类  |  **行号**：62–69  |  **完整限定名**：`src.rag.retriever.Resource`
- **基类**：`BaseModel`
- **定义**：

```python
class Resource(BaseModel):
```
- **成员概览**：

  - `attr uri`
  - `attr title`
  - `attr description`

**摘要**：

Resource is a class that represents a resource.

### `Retriever`

- **类型**：类  |  **行号**：72–164  |  **完整限定名**：`src.rag.retriever.Retriever`
- **基类**：`abc.ABC`
- **定义**：

```python
class Retriever(abc.ABC):
```
- **成员概览**：

  - `def list_resources`
  - `async def list_resources_async`
  - `def query_relevant_documents`
  - `async def query_relevant_documents_async`
  - `def ingest_file`

**摘要**：

Define a RAG provider, which can be used to query documents and resources.

## 调用关系（下游）

**被以下模块导入**：

- `src.config.configuration`
- `src.rag`
- `src.rag.builder`
- `src.rag.dify`
- `src.rag.milvus`
- `src.rag.moi`
- `src.rag.qdrant`
- `src.rag.ragflow`
- `src.rag.vikingdb_knowledge_base`
- `src.server.app`
- `src.server.chat_request`
- `src.server.rag_request`
- `src.tools`
- `tests.unit.rag.test_milvus`
- `tests.unit.rag.test_retriever`
- `tests.unit.server.test_chat_request`

## 示例用法

```python
from src.rag.retriever import Chunk
#
# TODO: 结合业务场景补充 Chunk 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

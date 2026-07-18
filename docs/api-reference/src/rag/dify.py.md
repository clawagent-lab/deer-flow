# `src/rag/dify.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/dify.py`
- **模块导入名**：`src.rag.dify`
- **代码行数**：158
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
Dify RAG 平台的检索器适配实现。

``DifyProvider`` 继承 ``Retriever``，通过 Dify 的 dataset 检索 API
（混合检索：关键词权重 0.3 + 向量权重 0.7）按 ``Resource.uri`` 指定的
dataset 查询相关文档分块，并将其映射为统一的 ``Document`` / ``Chunk`` 模型。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.rag.retriever import Chunk, Document, Resource, Retriever`

**外部依赖**（第三方库 / 标准库）：

- `from urllib.parse import urlparse`
- `import asyncio`
- `import os`
- `import requests`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `DifyProvider` | 20 | `` |
| 函数 | `parse_uri` | 154 | `(uri: str) -> tuple[str, str]` |

## 符号详解

### `DifyProvider`

- **类型**：类  |  **行号**：20–151  |  **完整限定名**：`src.rag.dify.DifyProvider`
- **基类**：`Retriever`
- **定义**：

```python
class DifyProvider(Retriever):
```
- **成员概览**：

  - `attr api_url`
  - `attr api_key`
  - `def __init__`
  - `def query_relevant_documents`
  - `async def query_relevant_documents_async`
  - `def list_resources`
  - `async def list_resources_async`

**摘要**：

DifyProvider is a provider that uses dify to retrieve documents.

### `parse_uri`

- **类型**：函数  |  **行号**：154–158  |  **完整限定名**：`src.rag.dify.parse_uri`
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
- `tests.unit.rag.test_dify`

## 示例用法

```python
from src.rag.dify import parse_uri
#
# TODO: 结合业务场景补充 parse_uri 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

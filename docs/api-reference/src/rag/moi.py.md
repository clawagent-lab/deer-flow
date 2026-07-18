# `src/rag/moi.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/moi.py`
- **模块导入名**：`src.rag.moi`
- **代码行数**：182
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
MatrixOne Intelligence (MOI) 平台的 RAG 检索器适配实现。

``MOIProvider`` 继承 ``Retriever``，通过 MOI 的 BYOA API（自动追加
``/byoa`` 后缀）按 ``Resource.uri`` 指定的数据集检索文档，支持配置
``MOI_RETRIEVAL_SIZE`` 与 ``MOI_LIST_LIMIT`` 控制返回规模，将原始数据
（文档、图像、音视频等经 MOI 处理后的 AI-ready 数据）映射为统一的
``Document`` / ``Chunk`` 模型。
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
| 类 | `MOIProvider` | 22 | `` |

## 符号详解

### `MOIProvider`

- **类型**：类  |  **行号**：22–182  |  **完整限定名**：`src.rag.moi.MOIProvider`
- **基类**：`Retriever`
- **定义**：

```python
class MOIProvider(Retriever):
```
- **成员概览**：

  - `def __init__`
  - `def query_relevant_documents`
  - `async def query_relevant_documents_async`
  - `def list_resources`
  - `async def list_resources_async`
  - `def _parse_uri`

**摘要**：

MatrixOne Intelligence (MOI) is a multimodal data AI processing platform.
It supports connecting, processing, managing, and using both structured and unstructured data.
Through steps such as parsing, extraction, segmentation, cleaning, and enhancement,
it transforms raw data like documents, images, and audio/video into AI-ready application data.
With its self-developed data service layer (the MatrixOne database),
it can directly provide retrieval services for the processed data.

## 调用关系（下游）

**被以下模块导入**：

- `src.rag`
- `src.rag.builder`

## 示例用法

```python
from src.rag.moi import MOIProvider
#
# TODO: 结合业务场景补充 MOIProvider 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/rag/builder.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/builder.py`
- **模块导入名**：`src.rag.builder`
- **代码行数**：36
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
RAG 检索器工厂。

根据 ``src.config.tools.SELECTED_RAG_PROVIDER`` 配置项，构造并返回对应的
``Retriever`` 实现（Dify / RAGFlow / MOI / VikingDB / Milvus / Qdrant）。
未配置或为空时返回 ``None``，表示不启用 RAG 增强。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.tools import SELECTED_RAG_PROVIDER, RAGProvider`
- `from src.rag.dify import DifyProvider`
- `from src.rag.milvus import MilvusProvider`
- `from src.rag.moi import MOIProvider`
- `from src.rag.qdrant import QdrantProvider`
- `from src.rag.ragflow import RAGFlowProvider`
- `from src.rag.retriever import Retriever`
- `from src.rag.vikingdb_knowledge_base import VikingDBKnowledgeBaseProvider`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `build_retriever` | 21 | `() -> Retriever \| None` |

## 符号详解

### `build_retriever`

- **类型**：函数  |  **行号**：21–36  |  **完整限定名**：`src.rag.builder.build_retriever`
- **签名**：

```python
def build_retriever() -> Retriever | None:
```

**说明**（自动推断）：

工厂函数，构建并返回 `r` 相关的可运行对象（如图、检索器、智能体等）。

## 调用关系（下游）

**被以下模块导入**：

- `src.graph`
- `src.rag`
- `src.server.app`

## 示例用法

```python
from src.rag.builder import build_retriever
#
# TODO: 结合业务场景补充 build_retriever 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

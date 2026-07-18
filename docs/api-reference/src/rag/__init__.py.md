# `src/rag/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/rag/__init__.py`
- **模块导入名**：`src.rag`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：32
- **架构归属**：src/rag —— 检索增强生成：多后端适配（Milvus / Qdrant / Dify / Ragflow / VikingDB / Moi）+ Builder 工厂

## 模块概述

```text
RAG（检索增强生成）模块包。

统一聚合各检索后端的 Provider 实现与抽象基类：对外暴露 ``Retriever``、
``Document``、``Chunk``、``Resource`` 等核心类型，以及 ``build_retriever``
工厂，按配置（Dify / RAGFlow / Milvus / Qdrant / MOI / VikingDB 等）
构造对应的检索器实例。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .builder import build_retriever`
- `from .dify import DifyProvider`
- `from .milvus import MilvusProvider`
- `from .moi import MOIProvider`
- `from .qdrant import QdrantProvider`
- `from .ragflow import RAGFlowProvider`
- `from .retriever import Chunk, Document, Resource, Retriever`
- `from .vikingdb_knowledge_base import VikingDBKnowledgeBaseProvider`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.types`
- `src.tools.retriever`
- `tests.unit.tools.test_tools_retriever`

## 示例用法

```python
# import src.rag
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

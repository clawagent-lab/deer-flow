# `src/server/rag_request.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/rag_request.py`
- **模块导入名**：`src.server.rag_request`
- **代码行数**：35
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
RAG 相关请求/响应 Pydantic 模型。

定义 ``RAGConfigResponse``（返回当前 RAG provider，如 ragflow）、
``RAGResourceRequest``（按 query 检索资源）与 ``RAGResourcesResponse``
（返回 ``Resource`` 列表），用于 RAG 配置查询与知识库资源检索接口。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.rag.retriever import Resource`

**外部依赖**（第三方库 / 标准库）：

- `from pydantic import BaseModel, Field`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `RAGConfigResponse` | 16 | `` |
| 类 | `RAGResourceRequest` | 24 | `` |
| 类 | `RAGResourcesResponse` | 32 | `` |

## 符号详解

### `RAGConfigResponse`

- **类型**：类  |  **行号**：16–21  |  **完整限定名**：`src.server.rag_request.RAGConfigResponse`
- **基类**：`BaseModel`
- **定义**：

```python
class RAGConfigResponse(BaseModel):
```
- **成员概览**：

  - `attr provider`

**摘要**：

Response model for RAG config.

### `RAGResourceRequest`

- **类型**：类  |  **行号**：24–29  |  **完整限定名**：`src.server.rag_request.RAGResourceRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class RAGResourceRequest(BaseModel):
```
- **成员概览**：

  - `attr query`

**摘要**：

Request model for RAG resource.

### `RAGResourcesResponse`

- **类型**：类  |  **行号**：32–35  |  **完整限定名**：`src.server.rag_request.RAGResourcesResponse`
- **基类**：`BaseModel`
- **定义**：

```python
class RAGResourcesResponse(BaseModel):
```
- **成员概览**：

  - `attr resources`

**摘要**：

Response model for RAG resources.

## 调用关系（下游）

**被以下模块导入**：

- `src.server.app`
- `src.server.config_request`

## 示例用法

```python
from src.server.rag_request import RAGConfigResponse
#
# TODO: 结合业务场景补充 RAGConfigResponse 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

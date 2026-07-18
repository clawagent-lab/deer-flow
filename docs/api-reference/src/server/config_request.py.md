# `src/server/config_request.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/config_request.py`
- **模块导入名**：`src.server.config_request`
- **代码行数**：19
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
服务端配置响应模型。

定义 ``ConfigResponse`` Pydantic 模型，向客户端返回 RAG 配置
（``RAGConfigResponse``）与可用 LLM 模型清单等运行期配置信息。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.server.rag_request import RAGConfigResponse`

**外部依赖**（第三方库 / 标准库）：

- `from pydantic import BaseModel, Field`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `ConfigResponse` | 15 | `` |

## 符号详解

### `ConfigResponse`

- **类型**：类  |  **行号**：15–19  |  **完整限定名**：`src.server.config_request.ConfigResponse`
- **基类**：`BaseModel`
- **定义**：

```python
class ConfigResponse(BaseModel):
```
- **成员概览**：

  - `attr rag`
  - `attr models`

**摘要**：

Response model for server config.

## 调用关系（下游）

**被以下模块导入**：

- `src.server.app`

## 示例用法

```python
from src.server.config_request import ConfigResponse
#
# TODO: 结合业务场景补充 ConfigResponse 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/tools/retriever.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/retriever.py`
- **模块导入名**：`src.tools.retriever`
- **代码行数**：76
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
本地知识库检索工具。

定义 ``RetrieverTool``（同步/异步双实现），依据关键词从 ``rag://`` 前缀
资源中检索相关文档。工具基于 ``src.rag`` 的 ``Retriever`` 与 ``Resource``
抽象，按当前 ``SELECTED_RAG_PROVIDER`` 配置进行检索，优先级高于网络搜索。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.tools import SELECTED_RAG_PROVIDER`
- `from src.rag import Document, Resource, Retriever, build_retriever`

**外部依赖**（第三方库 / 标准库）：

- `from typing import List, Optional, Type`
- `from langchain_core.callbacks import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun`
- `from langchain_core.tools import BaseTool`
- `from pydantic import BaseModel, Field`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 24 | `logging.getLogger(__name__)` |
| 类 | `RetrieverInput` | 27 | `` |
| 类 | `RetrieverTool` | 31 | `` |
| 函数 | `get_retriever_tool` | 68 | `(resources: List[Resource]) -> RetrieverTool \| None` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：24–24  |  **完整限定名**：`src.tools.retriever.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `RetrieverInput`

- **类型**：类  |  **行号**：27–28  |  **完整限定名**：`src.tools.retriever.RetrieverInput`
- **基类**：`BaseModel`
- **定义**：

```python
class RetrieverInput(BaseModel):
```
- **成员概览**：

  - `attr keywords`

**说明**（自动推断）：

Pydantic 数据模型 `RetrieverInput`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `RetrieverTool`

- **类型**：类  |  **行号**：31–65  |  **完整限定名**：`src.tools.retriever.RetrieverTool`
- **基类**：`BaseTool`
- **定义**：

```python
class RetrieverTool(BaseTool):
```
- **成员概览**：

  - `attr name`
  - `attr description`
  - `attr args_schema`
  - `attr retriever`
  - `attr resources`
  - `def _run`
  - `async def _arun`

**说明**（自动推断）：

LangChain 工具类 `RetrieverTool`，封装为可在智能体中调用的 tool 接口。

### `get_retriever_tool`

- **类型**：函数  |  **行号**：68–76  |  **完整限定名**：`src.tools.retriever.get_retriever_tool`
- **签名**：

```python
def get_retriever_tool(resources: List[Resource]) -> RetrieverTool | None:
```

**说明**（自动推断）：

工厂函数，根据配置创建并返回 `retriever` 工具实例，供智能体调用。

## 调用关系（下游）

**被以下模块导入**：

- `src.rag`
- `src.tools`
- `tests.unit.tools.test_tools_retriever`

## 示例用法

```python
from src.tools.retriever import get_retriever_tool
#
# TODO: 结合业务场景补充 get_retriever_tool 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

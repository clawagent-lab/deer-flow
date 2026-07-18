# `src/config/tools.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/config/tools.py`
- **模块导入名**：`src.config.tools`
- **代码行数**：43
- **架构归属**：src/config —— 配置加载（`conf.yaml` / `.env`）、模型与工具开关、报告样式、智能体映射

## 模块概述

```text
工具开关配置：定义搜索引擎、爬虫引擎、RAG 提供方的枚举，并通过环境变量读取当前选中项。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from dotenv import load_dotenv`
- `import enum`
- `import os`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `SearchEngine` | 14 | `` |
| 类 | `CrawlerEngine` | 25 | `` |
| 常量 | `SELECTED_SEARCH_ENGINE` | 31 | `os.getenv('SEARCH_API', SearchEngine.TAVILY.value)` |
| 类 | `RAGProvider` | 34 | `` |
| 常量 | `SELECTED_RAG_PROVIDER` | 43 | `os.getenv('RAG_PROVIDER')` |

## 符号详解

### `SearchEngine`

- **类型**：类  |  **行号**：14–22  |  **完整限定名**：`src.config.tools.SearchEngine`
- **基类**：`enum.Enum`
- **定义**：

```python
class SearchEngine(enum.Enum):
```
- **成员概览**：

  - `attr TAVILY`
  - `attr INFOQUEST`
  - `attr DUCKDUCKGO`
  - `attr BRAVE_SEARCH`
  - `attr ARXIV`
  - `attr SEARX`
  - `attr WIKIPEDIA`
  - `attr SERPER`

**说明**（自动推断）：

枚举类型 `SearchEngine`，定义该维度可选的取值集合。

### `CrawlerEngine`

- **类型**：类  |  **行号**：25–27  |  **完整限定名**：`src.config.tools.CrawlerEngine`
- **基类**：`enum.Enum`
- **定义**：

```python
class CrawlerEngine(enum.Enum):
```
- **成员概览**：

  - `attr JINA`
  - `attr INFOQUEST`

**说明**（自动推断）：

枚举类型 `CrawlerEngine`，定义该维度可选的取值集合。

### `SELECTED_SEARCH_ENGINE`

- **类型**：模块常量  |  **行号**：31–31  |  **完整限定名**：`src.config.tools.SELECTED_SEARCH_ENGINE`
- **值**：

```python
SELECTED_SEARCH_ENGINE = os.getenv('SEARCH_API', SearchEngine.TAVILY.value)
```

**说明**（自动推断）：

模块级常量 `SELECTED_SEARCH_ENGINE`，在导入时初始化，供本模块及相关流程引用。

### `RAGProvider`

- **类型**：类  |  **行号**：34–40  |  **完整限定名**：`src.config.tools.RAGProvider`
- **基类**：`enum.Enum`
- **定义**：

```python
class RAGProvider(enum.Enum):
```
- **成员概览**：

  - `attr DIFY`
  - `attr RAGFLOW`
  - `attr VIKINGDB_KNOWLEDGE_BASE`
  - `attr MOI`
  - `attr MILVUS`
  - `attr QDRANT`

**说明**（自动推断）：

枚举类型 `RAGProvider`，定义该维度可选的取值集合。

### `SELECTED_RAG_PROVIDER`

- **类型**：模块常量  |  **行号**：43–43  |  **完整限定名**：`src.config.tools.SELECTED_RAG_PROVIDER`
- **值**：

```python
SELECTED_RAG_PROVIDER = os.getenv('RAG_PROVIDER')
```

**说明**（自动推断）：

模块级常量 `SELECTED_RAG_PROVIDER`，在导入时初始化，供本模块及相关流程引用。

## 调用关系（下游）

**被以下模块导入**：

- `src.config`
- `src.crawler.crawler`
- `src.rag.builder`
- `src.server.app`
- `src.tools.retriever`

## 示例用法

```python
from src.config.tools import SearchEngine
#
# TODO: 结合业务场景补充 SearchEngine 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/tools/search.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/search.py`
- **模块导入名**：`src.tools.search`
- **代码行数**：155
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
网络搜索工具集。

依据配置 ``SELECTED_SEARCH_ENGINE`` 动态选择并返回对应的搜索工具：
Tavily、InfoQuest、DuckDuckGo、Brave、Google Serper、Arxiv、Searx、Wikipedia
等。所有工具均通过 ``create_logged_tool`` 包装为带日志版本，并按 ``conf.yaml``
中的 ``SEARCH_ENGINE`` 配置注入域名过滤、搜索深度等参数。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config import SELECTED_SEARCH_ENGINE, SearchEngine, load_yaml_config`
- `from src.tools.decorators import create_logged_tool`
- `from src.tools.infoquest_search.infoquest_search_results import InfoQuestSearchResults`
- `from src.tools.tavily_search.tavily_search_results_with_images import TavilySearchWithImages`

**外部依赖**（第三方库 / 标准库）：

- `from typing import List, Optional`
- `from langchain_community.tools import BraveSearch, DuckDuckGoSearchResults, GoogleSerperRun, SearxSearchRun, WikipediaQueryRun`
- `from langchain_community.tools.arxiv import ArxivQueryRun`
- `from langchain_community.utilities import ArxivAPIWrapper, BraveSearchWrapper, GoogleSerperAPIWrapper, SearxSearchWrapper, WikipediaAPIWrapper`
- `import logging`
- `import os`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 39 | `logging.getLogger(__name__)` |
| 常量 | `LoggedTavilySearch` | 42 | `create_logged_tool(TavilySearchWithImages)` |
| 常量 | `LoggedInfoQuestSearch` | 43 | `create_logged_tool(InfoQuestSearchResults)` |
| 常量 | `LoggedDuckDuckGoSearch` | 44 | `create_logged_tool(DuckDuckGoSearchResults)` |
| 常量 | `LoggedBraveSearch` | 45 | `create_logged_tool(BraveSearch)` |
| 常量 | `LoggedSerperSearch` | 46 | `create_logged_tool(GoogleSerperRun)` |
| 常量 | `LoggedArxivSearch` | 47 | `create_logged_tool(ArxivQueryRun)` |
| 常量 | `LoggedSearxSearch` | 48 | `create_logged_tool(SearxSearchRun)` |
| 常量 | `LoggedWikipediaSearch` | 49 | `create_logged_tool(WikipediaQueryRun)` |
| 函数 | `get_search_config` | 52 | `()` |
| 函数 | `get_web_search_tool` | 59 | `(max_search_results: int)` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：39–39  |  **完整限定名**：`src.tools.search.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `LoggedTavilySearch`

- **类型**：模块常量  |  **行号**：42–42  |  **完整限定名**：`src.tools.search.LoggedTavilySearch`
- **值**：

```python
LoggedTavilySearch = create_logged_tool(TavilySearchWithImages)
```

**说明**（自动推断）：

对 `TavilySearch` 工具的日志包装版本，由 `create_logged_tool(TavilySearch)` 生成，在原始工具调用前后记录请求与响应，便于审计与调试。

### `LoggedInfoQuestSearch`

- **类型**：模块常量  |  **行号**：43–43  |  **完整限定名**：`src.tools.search.LoggedInfoQuestSearch`
- **值**：

```python
LoggedInfoQuestSearch = create_logged_tool(InfoQuestSearchResults)
```

**说明**（自动推断）：

对 `InfoQuestSearch` 工具的日志包装版本，由 `create_logged_tool(InfoQuestSearch)` 生成，在原始工具调用前后记录请求与响应，便于审计与调试。

### `LoggedDuckDuckGoSearch`

- **类型**：模块常量  |  **行号**：44–44  |  **完整限定名**：`src.tools.search.LoggedDuckDuckGoSearch`
- **值**：

```python
LoggedDuckDuckGoSearch = create_logged_tool(DuckDuckGoSearchResults)
```

**说明**（自动推断）：

对 `DuckDuckGoSearch` 工具的日志包装版本，由 `create_logged_tool(DuckDuckGoSearch)` 生成，在原始工具调用前后记录请求与响应，便于审计与调试。

### `LoggedBraveSearch`

- **类型**：模块常量  |  **行号**：45–45  |  **完整限定名**：`src.tools.search.LoggedBraveSearch`
- **值**：

```python
LoggedBraveSearch = create_logged_tool(BraveSearch)
```

**说明**（自动推断）：

对 `BraveSearch` 工具的日志包装版本，由 `create_logged_tool(BraveSearch)` 生成，在原始工具调用前后记录请求与响应，便于审计与调试。

### `LoggedSerperSearch`

- **类型**：模块常量  |  **行号**：46–46  |  **完整限定名**：`src.tools.search.LoggedSerperSearch`
- **值**：

```python
LoggedSerperSearch = create_logged_tool(GoogleSerperRun)
```

**说明**（自动推断）：

对 `SerperSearch` 工具的日志包装版本，由 `create_logged_tool(SerperSearch)` 生成，在原始工具调用前后记录请求与响应，便于审计与调试。

### `LoggedArxivSearch`

- **类型**：模块常量  |  **行号**：47–47  |  **完整限定名**：`src.tools.search.LoggedArxivSearch`
- **值**：

```python
LoggedArxivSearch = create_logged_tool(ArxivQueryRun)
```

**说明**（自动推断）：

对 `ArxivSearch` 工具的日志包装版本，由 `create_logged_tool(ArxivSearch)` 生成，在原始工具调用前后记录请求与响应，便于审计与调试。

### `LoggedSearxSearch`

- **类型**：模块常量  |  **行号**：48–48  |  **完整限定名**：`src.tools.search.LoggedSearxSearch`
- **值**：

```python
LoggedSearxSearch = create_logged_tool(SearxSearchRun)
```

**说明**（自动推断）：

对 `SearxSearch` 工具的日志包装版本，由 `create_logged_tool(SearxSearch)` 生成，在原始工具调用前后记录请求与响应，便于审计与调试。

### `LoggedWikipediaSearch`

- **类型**：模块常量  |  **行号**：49–49  |  **完整限定名**：`src.tools.search.LoggedWikipediaSearch`
- **值**：

```python
LoggedWikipediaSearch = create_logged_tool(WikipediaQueryRun)
```

**说明**（自动推断）：

对 `WikipediaSearch` 工具的日志包装版本，由 `create_logged_tool(WikipediaSearch)` 生成，在原始工具调用前后记录请求与响应，便于审计与调试。

### `get_search_config`

- **类型**：函数  |  **行号**：52–55  |  **完整限定名**：`src.tools.search.get_search_config`
- **签名**：

```python
def get_search_config():
```

**说明**（自动推断）：

从 `conf.yaml` 读取搜索引擎配置段并返回字典，供搜索工具初始化时使用。

### `get_web_search_tool`

- **类型**：函数  |  **行号**：59–155  |  **完整限定名**：`src.tools.search.get_web_search_tool`
- **签名**：

```python
def get_web_search_tool(max_search_results: int):
```

**说明**（自动推断）：

工厂函数，根据配置创建并返回 `web_search` 工具实例，供智能体调用。

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`
- `src.tools`
- `tests.unit.tools.test_search`

## 示例用法

```python
from src.tools.search import get_search_config
#
# TODO: 结合业务场景补充 get_search_config 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

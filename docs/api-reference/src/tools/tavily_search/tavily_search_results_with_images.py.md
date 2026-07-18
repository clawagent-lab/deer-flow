# `src/tools/tavily_search/tavily_search_results_with_images.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/tavily_search/tavily_search_results_with_images.py`
- **模块导入名**：`src.tools.tavily_search.tavily_search_results_with_images`
- **代码行数**：174
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
Tavily 带图像搜索的 LangChain 工具模块。

定义 ``TavilySearchWithImages``，继承自 ``langchain_community`` 的 ``TavilySearchResults``，
通过 ``EnhancedTavilySearchAPIWrapper`` 调用 Tavily API，
在返回文本检索结果的同时附带图像及图像描述，供研究智能体获取更丰富的多媒体信息。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.tools.tavily_search.tavily_search_api_wrapper import EnhancedTavilySearchAPIWrapper`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Dict, List, Optional, Tuple, Union`
- `from langchain_core.callbacks import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun`
- `from langchain_community.tools.tavily_search.tool import TavilySearchResults`
- `from pydantic import Field`
- `import json`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 27 | `logging.getLogger(__name__)` |
| 类 | `TavilySearchWithImages` | 30 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：27–27  |  **完整限定名**：`src.tools.tavily_search.tavily_search_results_with_images.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `TavilySearchWithImages`

- **类型**：类  |  **行号**：30–174  |  **完整限定名**：`src.tools.tavily_search.tavily_search_results_with_images.TavilySearchWithImages`
- **基类**：`TavilySearchResults`
- **定义**：

```python
class TavilySearchWithImages(TavilySearchResults):
```
- **成员概览**：

  - `attr include_image_descriptions`
  - `attr api_wrapper`
  - `def _run`
  - `async def _arun`

**摘要**：

Tool that queries the Tavily Search API and gets back json.

**setup**：

```text
Install ``langchain-openai`` and ``tavily-python``, and set environment variable ``TAVILY_API_KEY``.

        .. code-block:: bash

            pip install -U langchain-community tavily-python
            export TAVILY_API_KEY="your-api-key"
```

**instantiate**：

```text
.. code-block:: python

            from langchain_tavily.tavily_search import TavilySearch

            tool = TavilySearch(
                max_results=5,
                include_answer=True,
                include_raw_content=True,
                include_images=True,
                include_image_descriptions=True,
                # search_depth="advanced",
                # include_domains = []
                # exclude_domains = []
            )

    Invoke directly with args:

        .. code-block:: python

            tool.invoke({'query': 'who won the last french open'})

        .. code-block:: json

            {
                "url": "https://www.nytimes.com...",
                "content": "Novak Djokovic won the last French Open by beating Casper Ruud ..."
            }

    Invoke with tool call:

        .. code-block:: python

            tool.invoke({"args": {'query': 'who won the last french open'}, "type": "tool_call", "id": "foo", "name": "tavily"})

        .. code-block:: python

            ToolMessage(
                content='{ "url": "https://www.nytimes.com...", "content": "Novak Djokovic won the last French Open by beating Casper Ruud ..." }',
                artifact={
                    'query': 'who won the last french open',
                    'follow_up_questions': None,
                    'answer': 'Novak ...',
                    'images': [
                        'https://www.amny.com/wp-content/uploads/2023/06/AP23162622181176-1200x800.jpg',
                        ...
                        ],
                    'results': [
                        {
                            'title': 'Djokovic ...',
                            'url': 'https://www.nytimes.com...',
                            'content': "Novak...",
                            'score': 0.99505633,
                            'raw_content': 'Tennis
Novak ...'
                        },
                        ...
                    ],
                    'response_time': 2.92
                },
                tool_call_id='1',
                name='tavily_search_results_json',
            )
```

## 调用关系（下游）

**被以下模块导入**：

- `src.tools.search`
- `src.tools.tavily_search`
- `tests.unit.tools.test_tavily_search_results_with_images`

## 示例用法

```python
from src.tools.tavily_search.tavily_search_results_with_images import TavilySearchWithImages
#
# TODO: 结合业务场景补充 TavilySearchWithImages 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

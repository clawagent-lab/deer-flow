# `src/tools/infoquest_search/infoquest_search_results.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/infoquest_search/infoquest_search_results.py`
- **模块导入名**：`src.tools.infoquest_search.infoquest_search_results`
- **代码行数**：236
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
Tool for the InfoQuest search API.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.tools.infoquest_search.infoquest_search_api import InfoQuestAPIWrapper`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Dict, List, Literal, Optional, Tuple, Type, Union`
- `from langchain_core.callbacks import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun`
- `from langchain_core.tools import BaseTool`
- `from pydantic import BaseModel, Field`
- `import json`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 18 | `logging.getLogger(__name__)` |
| 类 | `InfoQuestInput` | 20 | `` |
| 类 | `InfoQuestSearchResults` | 25 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：18–18  |  **完整限定名**：`src.tools.infoquest_search.infoquest_search_results.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `InfoQuestInput`

- **类型**：类  |  **行号**：20–23  |  **完整限定名**：`src.tools.infoquest_search.infoquest_search_results.InfoQuestInput`
- **基类**：`BaseModel`
- **定义**：

```python
class InfoQuestInput(BaseModel):
```
- **成员概览**：

  - `attr query`

**摘要**：

Input for the InfoQuest tool.

### `InfoQuestSearchResults`

- **类型**：类  |  **行号**：25–236  |  **完整限定名**：`src.tools.infoquest_search.infoquest_search_results.InfoQuestSearchResults`
- **基类**：`BaseTool`
- **定义**：

```python
class InfoQuestSearchResults(BaseTool):
```
- **成员概览**：

  - `attr name`
  - `attr description`
  - `attr args_schema`
  - `attr time_range`
  - `attr site`
  - `attr api_wrapper`
  - `attr response_format`
  - `def __init__`
  - `def _run`
  - `async def _arun`

**摘要**：

Tool that queries the InfoQuest Search API and returns processed results with images.

**setup**：

```text
Install required packages and set environment variable ``INFOQUEST_API_KEY``.

    .. code-block:: bash

        pip install -U langchain-community aiohttp
        export INFOQUEST_API_KEY="your-api-key"
```

**instantiate**：

```text
.. code-block:: python

        from your_module import InfoQuestSearch 

        tool = InfoQuestSearchResults(
            output_format="json",
            time_range=10,
            site="nytimes.com"
        )

Invoke directly with args:
    .. code-block:: python

        tool.invoke({
            'query': 'who won the last french open'
        })

    .. code-block:: json

        [
            {
                "type": "page",
                "title": "Djokovic Claims French Open Title...",
                "url": "https://www.nytimes.com/...",
                "desc": "Novak Djokovic won the 2024 French Open by defeating Casper Ruud..."
            },
            {
                "type": "news",
                "time_frame": "2 days ago",
                "title": "French Open Finals Recap",
                "url": "https://www.nytimes.com/...",
                "source": "New York Times"
            },
            {
                "type": "image_url",
                "image_url": {"url": "https://www.nytimes.com/.../djokovic.jpg"},
                "image_description": "Novak Djokovic celebrating his French Open victory"
            }
        ]

Invoke with tool call:
    .. code-block:: python

        tool.invoke({
            "args": {
                'query': 'who won the last french open',
            },
            "type": "tool_call",
            "id": "foo",
            "name": "infoquest"
        })

    .. code-block:: python

        ToolMessage(
            content='[
                {"type": "page", "title": "Djokovic Claims...", "url": "https://www.nytimes.com/...", "desc": "Novak Djokovic won..."},
                {"type": "news", "time_frame": "2 days ago", "title": "French Open Finals...", "url": "https://www.nytimes.com/...", "source": "New York Times"},
                {"type": "image_url", "image_url": {"url": "https://www.nytimes.com/.../djokovic.jpg"}, "image_description": "Novak Djokovic celebrating..."}
            ]',
            tool_call_id='1',
            name='infoquest_search_results_json',
        )
```

## 调用关系（下游）

**被以下模块导入**：

- `src.tools.infoquest_search`
- `src.tools.search`

## 示例用法

```python
from src.tools.infoquest_search.infoquest_search_results import InfoQuestInput
#
# TODO: 结合业务场景补充 InfoQuestInput 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

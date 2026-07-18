# `src/tools/crawl.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/crawl.py`
- **模块导入名**：`src.tools.crawl`
- **代码行数**：67
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
网页抓取工具。

提供 ``crawl_tool`` LangChain 工具，对给定 URL 进行抓取并返回 Markdown 格式
正文内容；自动识别 PDF 链接并跳过直接抓取，正文过长者通过
``compress_crawl_content`` 截断至前 1000 字符。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.crawler.article import Article`
- `from src.crawler import Crawler`
- `from .decorators import log_io`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Annotated, Optional`
- `from urllib.parse import urlparse`
- `from langchain_core.tools import tool`
- `import json`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 22 | `logging.getLogger(__name__)` |
| 函数 | `is_pdf_url` | 24 | `(url: Optional[str]) -> bool` |
| 函数 | `crawl_tool` | 35 | `(url: Annotated[str, 'The url to crawl.']) -> str` |
| 函数 | `compress_crawl_content` | 61 | `(article: Article) -> str` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：22–22  |  **完整限定名**：`src.tools.crawl.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `is_pdf_url`

- **类型**：函数  |  **行号**：24–30  |  **完整限定名**：`src.tools.crawl.is_pdf_url`
- **签名**：

```python
def is_pdf_url(url: Optional[str]) -> bool:
```

**摘要**：

Check if the URL points to a PDF file.

### `crawl_tool`

- **类型**：函数  |  **行号**：35–58  |  **完整限定名**：`src.tools.crawl.crawl_tool`
- **装饰器**：`@tool`, `@log_io`
- **签名**：

```python
def crawl_tool(url: Annotated[str, 'The url to crawl.']) -> str:
```

**摘要**：

Use this to crawl a url and get a readable content in markdown format.

### `compress_crawl_content`

- **类型**：函数  |  **行号**：61–67  |  **完整限定名**：`src.tools.crawl.compress_crawl_content`
- **签名**：

```python
def compress_crawl_content(article: Article) -> str:
```

**摘要**：

Compress user-defined function for article content.
We can customize this function to implement different compression strategies.
Currently, it truncates the markdown content to the first 1000 characters.

## 调用关系（下游）

**被以下模块导入**：

- `src.tools`
- `tests.unit.tools.test_crawl`

## 示例用法

```python
from src.tools.crawl import is_pdf_url
#
# TODO: 结合业务场景补充 is_pdf_url 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

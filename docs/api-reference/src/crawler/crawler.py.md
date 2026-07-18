# `src/crawler/crawler.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/crawler/crawler.py`
- **模块导入名**：`src.crawler.crawler`
- **代码行数**：238
- **架构归属**：src/crawler —— 网页抓取与正文抽取（Jina、Readability、InfoQuest 等多客户端）

## 模块概述

```text
统一爬取调度模块：``Crawler`` 依据配置在 JinaClient、ReadabilityExtractor、InfoQuestClient 等引擎间选择，抓取 URL 并返回 ``Article``，附带安全截断等工具函数。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.tools import CrawlerEngine`
- `from src.config import load_yaml_config`
- `from src.crawler.article import Article`
- `from src.crawler.infoquest_client import InfoQuestClient`
- `from src.crawler.jina_client import JinaClient`
- `from src.crawler.readability_extractor import ReadabilityExtractor`

**外部依赖**（第三方库 / 标准库）：

- `import re`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 16 | `logging.getLogger(__name__)` |
| 函数 | `safe_truncate` | 19 | `(text: str, max_length: int=500) -> str` |
| 函数 | `is_html_content` | 54 | `(content: str) -> bool` |
| 类 | `Crawler` | 139 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：16–16  |  **完整限定名**：`src.crawler.crawler.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `safe_truncate`

- **类型**：函数  |  **行号**：19–51  |  **完整限定名**：`src.crawler.crawler.safe_truncate`
- **签名**：

```python
def safe_truncate(text: str, max_length: int=500) -> str:
```

**摘要**：

Safely truncate text to a maximum length without breaking multi-byte characters.

**参数**：

```text
text: The text to truncate
    max_length: Maximum number of characters to keep
```

**返回值**：

```text
Truncated text that is safe to use without encoding issues
```

### `is_html_content`

- **类型**：函数  |  **行号**：54–136  |  **完整限定名**：`src.crawler.crawler.is_html_content`
- **签名**：

```python
def is_html_content(content: str) -> bool:
```

**摘要**：

Check if the provided content is HTML.

### `Crawler`

- **类型**：类  |  **行号**：139–238  |  **完整限定名**：`src.crawler.crawler.Crawler`
- **定义**：

```python
class Crawler:
```
- **成员概览**：

  - `def crawl`
  - `def _select_crawler_tool`
  - `def _crawl_with_tool`

**说明**（自动推断）：

爬虫类 `Crawler`，实现 URL 抓取与正文抽取流程，协调各抽取器与客户端。

## 调用关系（下游）

**被以下模块导入**：

- `src.crawler`
- `tests.unit.crawler.test_crawler_class`

## 示例用法

```python
from src.crawler.crawler import safe_truncate
#
# TODO: 结合业务场景补充 safe_truncate 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

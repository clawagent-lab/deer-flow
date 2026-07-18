# `src/crawler/infoquest_client.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/crawler/infoquest_client.py`
- **模块导入名**：`src.crawler.infoquest_client`
- **代码行数**：153
- **架构归属**：src/crawler —— 网页抓取与正文抽取（Jina、Readability、InfoQuest 等多客户端）

## 模块概述

```text
Util that calls InfoQuest Crawler API.

In order to set this up, follow instructions at:
https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Dict, Any`
- `import json`
- `import logging`
- `import os`
- `import requests`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 17 | `logging.getLogger(__name__)` |
| 类 | `InfoQuestClient` | 19 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：17–17  |  **完整限定名**：`src.crawler.infoquest_client.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `InfoQuestClient`

- **类型**：类  |  **行号**：19–153  |  **完整限定名**：`src.crawler.infoquest_client.InfoQuestClient`
- **定义**：

```python
class InfoQuestClient:
```
- **成员概览**：

  - `def __init__`
  - `def crawl`
  - `def _prepare_headers`
  - `def _prepare_request_data`

**摘要**：

Client for interacting with the InfoQuest web crawling API.

## 调用关系（下游）

**被以下模块导入**：

- `src.crawler.crawler`
- `tests.unit.crawler.test_crawler_class`
- `tests.unit.crawler.test_infoquest_client`

## 示例用法

```python
from src.crawler.infoquest_client import InfoQuestClient
#
# TODO: 结合业务场景补充 InfoQuestClient 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

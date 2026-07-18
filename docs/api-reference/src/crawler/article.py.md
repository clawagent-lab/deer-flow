# `src/crawler/article.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/crawler/article.py`
- **模块导入名**：`src.crawler.article`
- **代码行数**：55
- **架构归属**：src/crawler —— 网页抓取与正文抽取（Jina、Readability、InfoQuest 等多客户端）

## 模块概述

```text
文章数据模型模块：``Article`` 封装标题与 HTML 内容，提供转 Markdown、转消息列表（含图片抽取）等方法，作为爬取结果的统一承载结构。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from urllib.parse import urljoin`
- `from markdownify import markdownify`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `Article` | 12 | `` |

## 符号详解

### `Article`

- **类型**：类  |  **行号**：12–55  |  **完整限定名**：`src.crawler.article.Article`
- **定义**：

```python
class Article:
```
- **成员概览**：

  - `attr url`
  - `def __init__`
  - `def to_markdown`
  - `def to_message`

**说明**（自动推断）：

文章数据类，承载抓取结果的标题、正文、URL 等字段。

## 调用关系（下游）

**被以下模块导入**：

- `src.crawler`
- `src.crawler.crawler`
- `src.crawler.readability_extractor`
- `src.tools.crawl`
- `tests.unit.crawler.test_article`

## 示例用法

```python
from src.crawler.article import Article
#
# TODO: 结合业务场景补充 Article 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

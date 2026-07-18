# `src/crawler/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/crawler/__init__.py`
- **模块导入名**：`src.crawler`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：11
- **架构归属**：src/crawler —— 网页抓取与正文抽取（Jina、Readability、InfoQuest 等多客户端）

## 模块概述

```text
网页爬取与正文抽取包入口：导出 ``Article``、``Crawler``、``JinaClient``、``ReadabilityExtractor`` 四个核心组件，统一对外提供 URL 抓取与可读内容提取能力。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .article import Article`
- `from .crawler import Crawler`
- `from .jina_client import JinaClient`
- `from .readability_extractor import ReadabilityExtractor`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

**被以下模块导入**：

- `src.tools.crawl`
- `tests.integration.test_crawler`
- `tests.unit.crawler.test_crawler_class`

## 示例用法

```python
# import src.crawler
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

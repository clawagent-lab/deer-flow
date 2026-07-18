# `src/crawler/readability_extractor.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/crawler/readability_extractor.py`
- **模块导入名**：`src.crawler.readability_extractor`
- **代码行数**：31
- **架构归属**：src/crawler —— 网页抓取与正文抽取（Jina、Readability、InfoQuest 等多客户端）

## 模块概述

```text
正文抽取模块：``ReadabilityExtractor`` 基于 readabilipy/Readability 算法从原始 HTML 中提取标题与正文，封装为 ``Article`` 返回。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .article import Article`

**外部依赖**（第三方库 / 标准库）：

- `from readabilipy import simple_json_from_html_string`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 12 | `logging.getLogger(__name__)` |
| 类 | `ReadabilityExtractor` | 15 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：12–12  |  **完整限定名**：`src.crawler.readability_extractor.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `ReadabilityExtractor`

- **类型**：类  |  **行号**：15–31  |  **完整限定名**：`src.crawler.readability_extractor.ReadabilityExtractor`
- **定义**：

```python
class ReadabilityExtractor:
```
- **成员概览**：

  - `def extract_article`

**说明**（自动推断）：

正文抽取器类 `ReadabilityExtractor`，从原始 HTML 中提取可读正文内容。

## 调用关系（下游）

**被以下模块导入**：

- `src.crawler`
- `src.crawler.crawler`
- `tests.unit.crawler.test_readability_extractor`

## 示例用法

```python
from src.crawler.readability_extractor import ReadabilityExtractor
#
# TODO: 结合业务场景补充 ReadabilityExtractor 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

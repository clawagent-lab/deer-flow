# `src/citations/collector.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/citations/collector.py`
- **模块导入名**：`src.citations.collector`
- **代码行数**：285
- **架构归属**：src/citations —— 引用元数据采集、抽取与格式化，支撑报告中的来源标注

## 模块概述

```text
Citation collector for gathering and managing citations during research.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .models import Citation, CitationMetadata`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Dict, List, Optional`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 13 | `logging.getLogger(__name__)` |
| 类 | `CitationCollector` | 16 | `` |
| 函数 | `extract_urls_from_text` | 257 | `(text: str) -> List[str]` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：13–13  |  **完整限定名**：`src.citations.collector.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `CitationCollector`

- **类型**：类  |  **行号**：16–254  |  **完整限定名**：`src.citations.collector.CitationCollector`
- **定义**：

```python
class CitationCollector:
```
- **成员概览**：

  - `def __init__`
  - `def add_from_search_results`
  - `def add_from_crawl_result`
  - `def mark_used`
  - `def get_number`
  - `def get_metadata`
  - `def get_all_citations`
  - `def get_used_citations`
  - `def to_dict`
  - `def from_dict`
  - `def merge_with`
  - `def count`
  - `def used_count`
  - `def clear`

**摘要**：

Collects and manages citations during the research process.

### `extract_urls_from_text`

- **类型**：函数  |  **行号**：257–285  |  **完整限定名**：`src.citations.collector.extract_urls_from_text`
- **签名**：

```python
def extract_urls_from_text(text: str) -> List[str]:
```

**摘要**：

Extract URLs from markdown text.

**参数**：

```text
text: Markdown text that may contain URLs
```

**返回值**：

```text
List of URLs found in the text
```

## 调用关系（下游）

**被以下模块导入**：

- `src.citations`
- `tests.unit.citations.test_citations`
- `tests.unit.citations.test_collector`

## 示例用法

```python
from src.citations.collector import extract_urls_from_text
#
# TODO: 结合业务场景补充 extract_urls_from_text 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

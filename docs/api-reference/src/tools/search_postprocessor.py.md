# `src/tools/search_postprocessor.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/search_postprocessor.py`
- **模块导入名**：`src.tools.search_postprocessor`
- **代码行数**：226
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
搜索结果后处理器。

定义 ``SearchResultProcessor``，对搜索返回的结果列表进行统一清洗：
去重（按 URL）、低分过滤、移除 base64 内嵌图片、截断过长正文/描述，
并按相关性分数降序排序，输出更精炼、可控的搜索结果集。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Dict, List`
- `from urllib.parse import urlparse`
- `import base64`
- `import logging`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 15 | `logging.getLogger(__name__)` |
| 类 | `SearchResultPostProcessor` | 18 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：15–15  |  **完整限定名**：`src.tools.search_postprocessor.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `SearchResultPostProcessor`

- **类型**：类  |  **行号**：18–226  |  **完整限定名**：`src.tools.search_postprocessor.SearchResultPostProcessor`
- **定义**：

```python
class SearchResultPostProcessor:
```
- **成员概览**：

  - `attr base64_pattern`
  - `def __init__`
  - `def process_results`
  - `def _remove_base64_images`
  - `def processPage`
  - `def processImage`
  - `def _truncate_long_content`
  - `def _remove_duplicates`

**摘要**：

Search result post-processor

## 调用关系（下游）

**被以下模块导入**：

- `src.tools.tavily_search.tavily_search_api_wrapper`
- `tests.unit.tools.test_search_postprocessor`

## 示例用法

```python
from src.tools.search_postprocessor import SearchResultPostProcessor
#
# TODO: 结合业务场景补充 SearchResultPostProcessor 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

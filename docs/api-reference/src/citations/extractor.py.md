# `src/citations/extractor.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/citations/extractor.py`
- **模块导入名**：`src.citations.extractor`
- **代码行数**：445
- **架构归属**：src/citations —— 引用元数据采集、抽取与格式化，支撑报告中的来源标注

## 模块概述

```text
Citation extraction utilities for extracting citations from tool results.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .models import CitationMetadata`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Dict, List, Optional`
- `from langchain_core.messages import AIMessage, ToolMessage`
- `import json`
- `import logging`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 17 | `logging.getLogger(__name__)` |
| 函数 | `extract_citations_from_messages` | 20 | `(messages: List[Any]) -> List[Dict[str, Any]]` |
| 函数 | `_extract_from_tool_message` | 65 | `(message: ToolMessage) -> List[Dict[str, Any]]` |
| 函数 | `_extract_from_search_results` | 147 | `(data: Any) -> List[Dict[str, Any]]` |
| 函数 | `_result_to_citation` | 183 | `(result: Dict[str, Any]) -> Optional[Dict[str, Any]]` |
| 函数 | `extract_title_from_content` | 209 | `(content: Optional[str], max_length: int=200) -> str` |
| 函数 | `_extract_from_crawl_result` | 287 | `(data: Any) -> Optional[Dict[str, Any]]` |
| 函数 | `_extract_domain` | 320 | `(url: Optional[str]) -> str` |
| 函数 | `merge_citations` | 364 | `(existing: List[Dict[str, Any]], new: List[Dict[str, Any]]) -> List[Dict[str, Any]]` |
| 函数 | `citations_to_markdown_references` | 410 | `(citations: List[Dict[str, Any]]) -> str` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：17–17  |  **完整限定名**：`src.citations.extractor.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `extract_citations_from_messages`

- **类型**：函数  |  **行号**：20–62  |  **完整限定名**：`src.citations.extractor.extract_citations_from_messages`
- **签名**：

```python
def extract_citations_from_messages(messages: List[Any]) -> List[Dict[str, Any]]:
```

**摘要**：

Extract citation metadata from agent messages (tool calls/results).

**参数**：

```text
messages: List of messages from agent execution
```

**返回值**：

```text
List of citation dictionaries
```

### `_extract_from_tool_message`

- **类型**：函数  |  **行号**：65–144  |  **完整限定名**：`src.citations.extractor._extract_from_tool_message`
- **签名**：

```python
def _extract_from_tool_message(message: ToolMessage) -> List[Dict[str, Any]]:
```

**摘要**：

Extract citations from a tool message result.

**参数**：

```text
message: ToolMessage with tool execution result
```

**返回值**：

```text
List of citation dictionaries
```

### `_extract_from_search_results`

- **类型**：函数  |  **行号**：147–180  |  **完整限定名**：`src.citations.extractor._extract_from_search_results`
- **签名**：

```python
def _extract_from_search_results(data: Any) -> List[Dict[str, Any]]:
```

**摘要**：

Extract citations from web search results.

**参数**：

```text
data: Parsed JSON data from search tool
```

**返回值**：

```text
List of citation dictionaries
```

### `_result_to_citation`

- **类型**：函数  |  **行号**：183–206  |  **完整限定名**：`src.citations.extractor._result_to_citation`
- **签名**：

```python
def _result_to_citation(result: Dict[str, Any]) -> Optional[Dict[str, Any]]:
```

**摘要**：

Convert a search result to a citation dictionary.

**参数**：

```text
result: Search result dictionary
```

**返回值**：

```text
Citation dictionary or None
```

### `extract_title_from_content`

- **类型**：函数  |  **行号**：209–284  |  **完整限定名**：`src.citations.extractor.extract_title_from_content`
- **签名**：

```python
def extract_title_from_content(content: Optional[str], max_length: int=200) -> str:
```

**摘要**：

Intelligent title extraction supporting multiple formats.

**参数**：

```text
content: The content to extract title from (can be None)
    max_length: Maximum title length (default: 200)
```

**返回值**：

```text
Extracted title or "Untitled"
```

**priority**：

```text
1. HTML <title> tag
2. Markdown h1 (# Title)
3. Markdown h2-h6 (## Title, etc.)
4. JSON/YAML title field
5. First substantial non-empty line
6. "Untitled" as fallback
```

### `_extract_from_crawl_result`

- **类型**：函数  |  **行号**：287–317  |  **完整限定名**：`src.citations.extractor._extract_from_crawl_result`
- **签名**：

```python
def _extract_from_crawl_result(data: Any) -> Optional[Dict[str, Any]]:
```

**摘要**：

Extract citation from crawl tool result.

**参数**：

```text
data: Parsed JSON data from crawl tool
```

**返回值**：

```text
Citation dictionary or None
```

### `_extract_domain`

- **类型**：函数  |  **行号**：320–361  |  **完整限定名**：`src.citations.extractor._extract_domain`
- **签名**：

```python
def _extract_domain(url: Optional[str]) -> str:
```

**摘要**：

Extract domain from URL using urllib with regex fallback.

**参数**：

```text
url: The URL string to extract domain from (can be None)
```

**返回值**：

```text
The domain netloc (including port if present), or empty string if extraction fails
```

**handles**：

```text
- Standard URLs: https://www.example.com/path
- Short URLs: example.com
- Invalid URLs: graceful fallback
```

### `merge_citations`

- **类型**：函数  |  **行号**：364–407  |  **完整限定名**：`src.citations.extractor.merge_citations`
- **签名**：

```python
def merge_citations(existing: List[Dict[str, Any]], new: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
```

**摘要**：

Merge new citations into existing list, avoiding duplicates.

**参数**：

```text
existing: Existing citations list
    new: New citations to add
```

**返回值**：

```text
Merged list of citations
```

### `citations_to_markdown_references`

- **类型**：函数  |  **行号**：410–445  |  **完整限定名**：`src.citations.extractor.citations_to_markdown_references`
- **签名**：

```python
def citations_to_markdown_references(citations: List[Dict[str, Any]]) -> str:
```

**摘要**：

Convert citations list to markdown references section.

**参数**：

```text
citations: List of citation dictionaries
```

**返回值**：

```text
Markdown formatted references section
```

## 调用关系（下游）

**被以下模块导入**：

- `src.citations`
- `tests.unit.citations.test_citations`
- `tests.unit.citations.test_extractor`

## 示例用法

```python
from src.citations.extractor import extract_citations_from_messages
#
# TODO: 结合业务场景补充 extract_citations_from_messages 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

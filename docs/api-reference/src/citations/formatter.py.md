# `src/citations/formatter.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/citations/formatter.py`
- **模块导入名**：`src.citations.formatter`
- **代码行数**：397
- **架构归属**：src/citations —— 引用元数据采集、抽取与格式化，支撑报告中的来源标注

## 模块概述

```text
Citation formatter for generating citation sections and inline references.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .models import Citation`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Dict, List`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `CitationFormatter` | 14 | `` |
| 函数 | `parse_citations_from_report` | 242 | `(report: str, section_patterns: List[str]=None) -> Dict[str, Any]` |
| 函数 | `_extract_markdown_links` | 300 | `(text: str) -> List[Dict[str, str]]` |
| 函数 | `_extract_numbered_citations` | 325 | `(text: str) -> List[Dict[str, str]]` |
| 函数 | `_extract_footnote_citations` | 350 | `(text: str) -> List[Dict[str, str]]` |
| 函数 | `_extract_html_links` | 375 | `(text: str) -> List[Dict[str, str]]` |

## 符号详解

### `CitationFormatter`

- **类型**：类  |  **行号**：14–239  |  **完整限定名**：`src.citations.formatter.CitationFormatter`
- **定义**：

```python
class CitationFormatter:
```
- **成员概览**：

  - `attr SUPERSCRIPT_MAP`
  - `def __init__`
  - `def format_inline_marker`
  - `def format_reference`
  - `def format_simple_reference`
  - `def format_rich_reference`
  - `def format_citations_section`
  - `def format_footnotes_section`
  - `def add_citation_markers_to_text`
  - `def build_citation_data_json`

**摘要**：

Formats citations for display in reports.

### `parse_citations_from_report`

- **类型**：函数  |  **行号**：242–297  |  **完整限定名**：`src.citations.formatter.parse_citations_from_report`
- **签名**：

```python
def parse_citations_from_report(report: str, section_patterns: List[str]=None) -> Dict[str, Any]:
```

**摘要**：

Extract citation information from report, supporting multiple formats.

**参数**：

```text
report: The report markdown text
    section_patterns: Custom section header patterns (optional)
```

**返回值**：

```text
Dictionary with 'citations' list and 'count' of unique citations
```

### `_extract_markdown_links`

- **类型**：函数  |  **行号**：300–322  |  **完整限定名**：`src.citations.formatter._extract_markdown_links`
- **签名**：

```python
def _extract_markdown_links(text: str) -> List[Dict[str, str]]:
```

**摘要**：

Extract Markdown links [title](url).

**参数**：

```text
text: Text to extract from
```

**返回值**：

```text
List of citation dictionaries with title, url, and format
```

### `_extract_numbered_citations`

- **类型**：函数  |  **行号**：325–347  |  **完整限定名**：`src.citations.formatter._extract_numbered_citations`
- **签名**：

```python
def _extract_numbered_citations(text: str) -> List[Dict[str, str]]:
```

**摘要**：

Extract numbered citations [1] Title - URL.

**参数**：

```text
text: Text to extract from
```

**返回值**：

```text
List of citation dictionaries
```

### `_extract_footnote_citations`

- **类型**：函数  |  **行号**：350–372  |  **完整限定名**：`src.citations.formatter._extract_footnote_citations`
- **签名**：

```python
def _extract_footnote_citations(text: str) -> List[Dict[str, str]]:
```

**摘要**：

Extract footnote citations [^1]: Title - URL.

**参数**：

```text
text: Text to extract from
```

**返回值**：

```text
List of citation dictionaries
```

### `_extract_html_links`

- **类型**：函数  |  **行号**：375–397  |  **完整限定名**：`src.citations.formatter._extract_html_links`
- **签名**：

```python
def _extract_html_links(text: str) -> List[Dict[str, str]]:
```

**摘要**：

Extract HTML links <a href="url">title</a>.

**参数**：

```text
text: Text to extract from
```

**返回值**：

```text
List of citation dictionaries
```

## 调用关系（下游）

**被以下模块导入**：

- `src.citations`
- `tests.unit.citations.test_citations`
- `tests.unit.citations.test_formatter`

## 示例用法

```python
from src.citations.formatter import parse_citations_from_report
#
# TODO: 结合业务场景补充 parse_citations_from_report 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/citations/test_formatter.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/citations/test_formatter.py`
- **模块导入名**：`tests.unit.citations.test_formatter`
- **代码行数**：423
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for citation formatter enhancements.

Tests the multi-format citation parsing and extraction capabilities.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.citations.formatter import parse_citations_from_report, _extract_markdown_links, _extract_numbered_citations, _extract_footnote_citations, _extract_html_links`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestExtractMarkdownLinks` | 19 | `` |
| 类 | `TestExtractNumberedCitations` | 76 | `` |
| 类 | `TestExtractFootnoteCitations` | 129 | `` |
| 类 | `TestExtractHtmlLinks` | 175 | `` |
| 类 | `TestParseCitationsFromReport` | 233 | `` |

## 符号详解

### `TestExtractMarkdownLinks`

- **类型**：类  |  **行号**：19–73  |  **完整限定名**：`tests.unit.citations.test_formatter.TestExtractMarkdownLinks`
- **定义**：

```python
class TestExtractMarkdownLinks:
```
- **成员概览**：

  - `def test_extract_single_markdown_link`
  - `def test_extract_multiple_markdown_links`
  - `def test_extract_markdown_link_with_spaces`
  - `def test_extract_markdown_link_ignore_non_http`
  - `def test_extract_markdown_link_with_query_params`
  - `def test_extract_markdown_link_empty_text`
  - `def test_extract_markdown_link_strip_whitespace`

**摘要**：

Test Markdown link extraction [title](url).

### `TestExtractNumberedCitations`

- **类型**：类  |  **行号**：76–126  |  **完整限定名**：`tests.unit.citations.test_formatter.TestExtractNumberedCitations`
- **定义**：

```python
class TestExtractNumberedCitations:
```
- **成员概览**：

  - `def test_extract_single_numbered_citation`
  - `def test_extract_multiple_numbered_citations`
  - `def test_extract_numbered_citation_with_long_title`
  - `def test_extract_numbered_citation_requires_valid_format`
  - `def test_extract_numbered_citation_empty_text`
  - `def test_extract_numbered_citation_various_numbers`
  - `def test_extract_numbered_citation_ignore_non_http`

**摘要**：

Test numbered citation extraction [1] Title - URL.

### `TestExtractFootnoteCitations`

- **类型**：类  |  **行号**：129–172  |  **完整限定名**：`tests.unit.citations.test_formatter.TestExtractFootnoteCitations`
- **定义**：

```python
class TestExtractFootnoteCitations:
```
- **成员概览**：

  - `def test_extract_single_footnote_citation`
  - `def test_extract_multiple_footnote_citations`
  - `def test_extract_footnote_with_complex_number`
  - `def test_extract_footnote_citation_with_spaces`
  - `def test_extract_footnote_citation_empty_text`
  - `def test_extract_footnote_requires_caret`

**摘要**：

Test footnote citation extraction [^1]: Title - URL.

### `TestExtractHtmlLinks`

- **类型**：类  |  **行号**：175–230  |  **完整限定名**：`tests.unit.citations.test_formatter.TestExtractHtmlLinks`
- **定义**：

```python
class TestExtractHtmlLinks:
```
- **成员概览**：

  - `def test_extract_single_html_link`
  - `def test_extract_multiple_html_links`
  - `def test_extract_html_link_single_quotes`
  - `def test_extract_html_link_with_attributes`
  - `def test_extract_html_link_ignore_non_http`
  - `def test_extract_html_link_case_insensitive`
  - `def test_extract_html_link_empty_text`
  - `def test_extract_html_link_strip_whitespace`

**摘要**：

Test HTML link extraction <a href="url">title</a>.

### `TestParseCitationsFromReport`

- **类型**：类  |  **行号**：233–423  |  **完整限定名**：`tests.unit.citations.test_formatter.TestParseCitationsFromReport`
- **定义**：

```python
class TestParseCitationsFromReport:
```
- **成员概览**：

  - `def test_parse_markdown_links_from_report`
  - `def test_parse_numbered_citations_from_report`
  - `def test_parse_mixed_format_citations`
  - `def test_parse_citations_deduplication`
  - `def test_parse_citations_various_section_patterns`
  - `def test_parse_citations_custom_patterns`
  - `def test_parse_citations_empty_report`
  - `def test_parse_citations_no_section`
  - `def test_parse_citations_complex_report`
  - `def test_parse_citations_stops_at_next_section`
  - `def test_parse_citations_preserves_metadata`
  - `def test_parse_citations_whitespace_handling`
  - `def test_parse_citations_multiline_links`

**摘要**：

Test comprehensive citation parsing from complete reports.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.citations.test_formatter import TestExtractMarkdownLinks
#
# TODO: 结合业务场景补充 TestExtractMarkdownLinks 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

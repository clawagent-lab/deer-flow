# `tests/unit/citations/test_extractor.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/citations/test_extractor.py`
- **模块导入名**：`tests.unit.citations.test_extractor`
- **代码行数**：251
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for extractor optimizations.

Tests the enhanced domain extraction and title extraction functions.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.citations.extractor import _extract_domain, extract_title_from_content`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestExtractDomainOptimization` | 16 | `` |
| 类 | `TestExtractTitleFromContent` | 89 | `` |

## 符号详解

### `TestExtractDomainOptimization`

- **类型**：类  |  **行号**：16–86  |  **完整限定名**：`tests.unit.citations.test_extractor.TestExtractDomainOptimization`
- **定义**：

```python
class TestExtractDomainOptimization:
```
- **成员概览**：

  - `def test_extract_domain_standard_urls`
  - `def test_extract_domain_with_port`
  - `def test_extract_domain_with_subdomain`
  - `def test_extract_domain_invalid_url`
  - `def test_extract_domain_empty_url`
  - `def test_extract_domain_without_scheme`
  - `def test_extract_domain_complex_urls`
  - `def test_extract_domain_ipv4`
  - `def test_extract_domain_query_params`
  - `def test_extract_domain_url_fragments`

**摘要**：

Test domain extraction with urllib + regex fallback strategy.

### `TestExtractTitleFromContent`

- **类型**：类  |  **行号**：89–251  |  **完整限定名**：`tests.unit.citations.test_extractor.TestExtractTitleFromContent`
- **定义**：

```python
class TestExtractTitleFromContent:
```
- **成员概览**：

  - `def test_extract_title_html_title_tag`
  - `def test_extract_title_html_title_case_insensitive`
  - `def test_extract_title_markdown_h1`
  - `def test_extract_title_markdown_h1_with_spaces`
  - `def test_extract_title_markdown_h2_fallback`
  - `def test_extract_title_markdown_h6_fallback`
  - `def test_extract_title_prefers_h1_over_h2`
  - `def test_extract_title_json_field`
  - `def test_extract_title_yaml_field`
  - `def test_extract_title_first_substantial_line`
  - `def test_extract_title_skips_short_lines`
  - `def test_extract_title_skips_code_blocks`
  - `def test_extract_title_skips_list_items`
  - `def test_extract_title_skips_separators`
  - `def test_extract_title_max_length`
  - `def test_extract_title_empty_content`
  - `def test_extract_title_no_title_found`
  - `def test_extract_title_whitespace_handling`
  - `def test_extract_title_multiline_html`
  - `def test_extract_title_mixed_formats`
  - `def test_extract_title_real_world_example`
  - `def test_extract_title_json_with_nested_title`
  - `def test_extract_title_preserves_special_characters`

**摘要**：

Test intelligent title extraction with 5-tier priority system.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.citations.test_extractor import TestExtractDomainOptimization
#
# TODO: 结合业务场景补充 TestExtractDomainOptimization 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/eval/test_metrics.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/eval/test_metrics.py`
- **模块导入名**：`tests.unit.eval.test_metrics`
- **代码行数**：207
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for report evaluation metrics.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.eval.metrics import compute_metrics, count_citations, count_images, count_words, detect_sections, extract_domains, get_word_count_target`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestCountWords` | 17 | `` |
| 类 | `TestCountCitations` | 36 | `` |
| 类 | `TestExtractDomains` | 58 | `` |
| 类 | `TestCountImages` | 88 | `` |
| 类 | `TestDetectSections` | 103 | `` |
| 类 | `TestComputeMetrics` | 137 | `` |
| 类 | `TestGetWordCountTarget` | 191 | `` |

## 符号详解

### `TestCountWords`

- **类型**：类  |  **行号**：17–33  |  **完整限定名**：`tests.unit.eval.test_metrics.TestCountWords`
- **定义**：

```python
class TestCountWords:
```
- **成员概览**：

  - `def test_english_words`
  - `def test_chinese_characters`
  - `def test_mixed_content`
  - `def test_empty_string`

**摘要**：

Tests for word counting function.

### `TestCountCitations`

- **类型**：类  |  **行号**：36–55  |  **完整限定名**：`tests.unit.eval.test_metrics.TestCountCitations`
- **定义**：

```python
class TestCountCitations:
```
- **成员概览**：

  - `def test_markdown_citations`
  - `def test_no_citations`
  - `def test_invalid_urls`
  - `def test_complex_urls`

**摘要**：

Tests for citation counting function.

### `TestExtractDomains`

- **类型**：类  |  **行号**：58–85  |  **完整限定名**：`tests.unit.eval.test_metrics.TestExtractDomains`
- **定义**：

```python
class TestExtractDomains:
```
- **成员概览**：

  - `def test_extract_multiple_domains`
  - `def test_deduplicate_domains`
  - `def test_no_urls`

**摘要**：

Tests for domain extraction function.

### `TestCountImages`

- **类型**：类  |  **行号**：88–100  |  **完整限定名**：`tests.unit.eval.test_metrics.TestCountImages`
- **定义**：

```python
class TestCountImages:
```
- **成员概览**：

  - `def test_markdown_images`
  - `def test_no_images`

**摘要**：

Tests for image counting function.

### `TestDetectSections`

- **类型**：类  |  **行号**：103–134  |  **完整限定名**：`tests.unit.eval.test_metrics.TestDetectSections`
- **定义**：

```python
class TestDetectSections:
```
- **成员概览**：

  - `def test_detect_title`
  - `def test_detect_key_points`
  - `def test_detect_chinese_sections`
  - `def test_detect_citations_section`

**摘要**：

Tests for section detection function.

### `TestComputeMetrics`

- **类型**：类  |  **行号**：137–188  |  **完整限定名**：`tests.unit.eval.test_metrics.TestComputeMetrics`
- **定义**：

```python
class TestComputeMetrics:
```
- **成员概览**：

  - `def test_complete_report`
  - `def test_minimal_report`
  - `def test_metrics_to_dict`

**摘要**：

Tests for the main compute_metrics function.

### `TestGetWordCountTarget`

- **类型**：类  |  **行号**：191–207  |  **完整限定名**：`tests.unit.eval.test_metrics.TestGetWordCountTarget`
- **定义**：

```python
class TestGetWordCountTarget:
```
- **成员概览**：

  - `def test_strategic_investment_target`
  - `def test_news_target`
  - `def test_default_target`

**摘要**：

Tests for word count target function.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.eval.test_metrics import TestCountWords
#
# TODO: 结合业务场景补充 TestCountWords 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

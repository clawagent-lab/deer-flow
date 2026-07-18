# `tests/unit/citations/test_models.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/citations/test_models.py`
- **模块导入名**：`tests.unit.citations.test_models`
- **代码行数**：467
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for citation models.

Tests the Pydantic BaseModel implementation of CitationMetadata and Citation classes.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.citations.models import Citation, CitationMetadata`

**外部依赖**（第三方库 / 标准库）：

- `from pydantic import ValidationError`
- `import json`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestCitationMetadata` | 18 | `` |
| 类 | `TestCitation` | 206 | `` |
| 类 | `TestCitationIntegration` | 393 | `` |

## 符号详解

### `TestCitationMetadata`

- **类型**：类  |  **行号**：18–203  |  **完整限定名**：`tests.unit.citations.test_models.TestCitationMetadata`
- **定义**：

```python
class TestCitationMetadata:
```
- **成员概览**：

  - `def test_create_basic_metadata`
  - `def test_metadata_with_all_fields`
  - `def test_metadata_domain_auto_extraction`
  - `def test_metadata_id_generation`
  - `def test_metadata_id_length`
  - `def test_metadata_from_dict`
  - `def test_metadata_from_dict_removes_id`
  - `def test_metadata_to_dict`
  - `def test_metadata_from_search_result`
  - `def test_metadata_pydantic_validation`
  - `def test_metadata_model_dump`
  - `def test_metadata_model_dump_json`
  - `def test_metadata_with_images_and_extra`

**摘要**：

Test CitationMetadata Pydantic model.

### `TestCitation`

- **类型**：类  |  **行号**：206–390  |  **完整限定名**：`tests.unit.citations.test_models.TestCitation`
- **定义**：

```python
class TestCitation:
```
- **成员概览**：

  - `def test_create_basic_citation`
  - `def test_citation_properties`
  - `def test_citation_to_markdown_reference`
  - `def test_citation_to_numbered_reference`
  - `def test_citation_to_inline_marker`
  - `def test_citation_to_footnote`
  - `def test_citation_with_context_and_text`
  - `def test_citation_from_dict`
  - `def test_citation_to_dict`
  - `def test_citation_round_trip`
  - `def test_citation_model_dump`
  - `def test_citation_model_dump_json`
  - `def test_citation_pydantic_validation`

**摘要**：

Test Citation Pydantic model.

### `TestCitationIntegration`

- **类型**：类  |  **行号**：393–467  |  **完整限定名**：`tests.unit.citations.test_models.TestCitationIntegration`
- **定义**：

```python
class TestCitationIntegration:
```
- **成员概览**：

  - `def test_search_result_to_citation_workflow`
  - `def test_multiple_citations_with_different_formats`
  - `def test_citation_json_serialization_roundtrip`

**摘要**：

Integration tests for citation models.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.citations.test_models import TestCitationMetadata
#
# TODO: 结合业务场景补充 TestCitationMetadata 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

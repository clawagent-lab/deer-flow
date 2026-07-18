# `tests/unit/citations/test_citations.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/citations/test_citations.py`
- **模块导入名**：`tests.unit.citations.test_citations`
- **代码行数**：136
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.citations.collector import CitationCollector`
- `from src.citations.extractor import _extract_domain, citations_to_markdown_references, extract_citations_from_messages, merge_citations`
- `from src.citations.formatter import CitationFormatter`
- `from src.citations.models import Citation, CitationMetadata`

**外部依赖**（第三方库 / 标准库）：

- `from langchain_core.messages import ToolMessage`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestCitationMetadata` | 17 | `` |
| 类 | `TestCitation` | 46 | `` |
| 类 | `TestExtractor` | 58 | `` |
| 类 | `TestCollector` | 119 | `` |
| 类 | `TestFormatter` | 132 | `` |

## 符号详解

### `TestCitationMetadata`

- **类型**：类  |  **行号**：17–43  |  **完整限定名**：`tests.unit.citations.test_citations.TestCitationMetadata`
- **定义**：

```python
class TestCitationMetadata:
```
- **成员概览**：

  - `def test_initialization`
  - `def test_id_generation`
  - `def test_to_dict`

**说明**（自动推断）：

pytest 测试类 `TestCitationMetadata`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestCitation`

- **类型**：类  |  **行号**：46–55  |  **完整限定名**：`tests.unit.citations.test_citations.TestCitation`
- **定义**：

```python
class TestCitation:
```
- **成员概览**：

  - `def test_citation_wrapper`

**说明**（自动推断）：

pytest 测试类 `TestCitation`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestExtractor`

- **类型**：类  |  **行号**：58–116  |  **完整限定名**：`tests.unit.citations.test_citations.TestExtractor`
- **定义**：

```python
class TestExtractor:
```
- **成员概览**：

  - `def test_extract_from_tool_message_web_search`
  - `def test_extract_domain`
  - `def test_merge_citations`
  - `def test_citations_to_markdown`

**说明**（自动推断）：

正文抽取器类 `TestExtractor`，从原始 HTML 中提取可读正文内容。

### `TestCollector`

- **类型**：类  |  **行号**：119–129  |  **完整限定名**：`tests.unit.citations.test_citations.TestCollector`
- **定义**：

```python
class TestCollector:
```
- **成员概览**：

  - `def test_add_citations`

**说明**（自动推断）：

pytest 测试类 `TestCollector`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestFormatter`

- **类型**：类  |  **行号**：132–136  |  **完整限定名**：`tests.unit.citations.test_citations.TestFormatter`
- **定义**：

```python
class TestFormatter:
```
- **成员概览**：

  - `def test_format_inline`

**说明**（自动推断）：

pytest 测试类 `TestFormatter`，聚合一组相关的测试用例方法（以 `test_` 开头）。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.citations.test_citations import TestCitationMetadata
#
# TODO: 结合业务场景补充 TestCitationMetadata 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

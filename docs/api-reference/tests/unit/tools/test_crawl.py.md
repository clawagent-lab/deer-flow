# `tests/unit/tools/test_crawl.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/tools/test_crawl.py`
- **模块导入名**：`tests.unit.tools.test_crawl`
- **代码行数**：216
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.tools.crawl import crawl_tool, is_pdf_url`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import Mock, patch`
- `import json`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestCrawlTool` | 7 | `` |
| 类 | `TestPDFHandling` | 136 | `` |

## 符号详解

### `TestCrawlTool`

- **类型**：类  |  **行号**：7–133  |  **完整限定名**：`tests.unit.tools.test_crawl.TestCrawlTool`
- **定义**：

```python
class TestCrawlTool:
```
- **成员概览**：

  - `def test_crawl_tool_success`
  - `def test_crawl_tool_short_content`
  - `def test_crawl_tool_crawler_exception`
  - `def test_crawl_tool_crawler_instantiation_exception`
  - `def test_crawl_tool_markdown_conversion_exception`
  - `def test_crawl_tool_with_none_content`

**说明**（自动推断）：

LangChain 工具类 `TestCrawlTool`，封装为可在智能体中调用的 tool 接口。

### `TestPDFHandling`

- **类型**：类  |  **行号**：136–216  |  **完整限定名**：`tests.unit.tools.test_crawl.TestPDFHandling`
- **定义**：

```python
class TestPDFHandling:
```
- **成员概览**：

  - `def test_is_pdf_url_with_pdf_urls`
  - `def test_is_pdf_url_with_non_pdf_urls`
  - `def test_crawl_tool_with_pdf_url`
  - `def test_crawl_tool_with_issue_pdf_url`
  - `def test_crawl_tool_skips_crawler_for_pdfs`

**摘要**：

Test PDF URL detection and handling for issue #701.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.tools.test_crawl import TestCrawlTool
#
# TODO: 结合业务场景补充 TestCrawlTool 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

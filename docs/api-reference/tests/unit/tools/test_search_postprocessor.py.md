# `tests/unit/tools/test_search_postprocessor.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/tools/test_search_postprocessor.py`
- **模块导入名**：`tests.unit.tools.test_search_postprocessor`
- **代码行数**：263
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.tools.search_postprocessor import SearchResultPostProcessor`

**外部依赖**（第三方库 / 标准库）：

- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestSearchResultPostProcessor` | 6 | `` |

## 符号详解

### `TestSearchResultPostProcessor`

- **类型**：类  |  **行号**：6–263  |  **完整限定名**：`tests.unit.tools.test_search_postprocessor.TestSearchResultPostProcessor`
- **定义**：

```python
class TestSearchResultPostProcessor:
```
- **成员概览**：

  - `def post_processor`
  - `def test_process_results_empty_input`
  - `def test_process_results_with_valid_page_results`
  - `def test_process_results_filter_low_score`
  - `def test_process_results_remove_duplicates`
  - `def test_process_results_sort_by_score`
  - `def test_process_results_truncate_long_content`
  - `def test_process_results_remove_base64_images`
  - `def test_process_results_with_image_type`
  - `def test_process_results_filter_base64_image_urls`
  - `def test_process_results_truncate_long_image_description`
  - `def test_process_results_other_types_passthrough`
  - `def test_process_results_truncate_long_content_with_no_config`
  - `def test_process_results_truncate_long_content_with_max_content_length_config`
  - `def test_process_results_truncate_long_content_with_min_score_config`

**摘要**：

Test cases for SearchResultPostProcessor

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.tools.test_search_postprocessor import TestSearchResultPostProcessor
#
# TODO: 结合业务场景补充 TestSearchResultPostProcessor 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

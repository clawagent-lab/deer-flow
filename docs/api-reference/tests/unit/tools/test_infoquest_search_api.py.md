# `tests/unit/tools/test_infoquest_search_api.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/tools/test_infoquest_search_api.py`
- **模块导入名**：`tests.unit.tools.test_infoquest_search_api`
- **代码行数**：218
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.tools.infoquest_search.infoquest_search_api import InfoQuestAPIWrapper`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import Mock, patch`
- `import pytest`
- `import requests`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestInfoQuestAPIWrapper` | 12 | `` |

## 符号详解

### `TestInfoQuestAPIWrapper`

- **类型**：类  |  **行号**：12–218  |  **完整限定名**：`tests.unit.tools.test_infoquest_search_api.TestInfoQuestAPIWrapper`
- **定义**：

```python
class TestInfoQuestAPIWrapper:
```
- **成员概览**：

  - `def wrapper`
  - `def mock_response_data`
  - `def test_raw_results_success`
  - `def test_raw_results_with_time_range_and_site`
  - `def test_raw_results_http_error`
  - `async def test_raw_results_async_success`
  - `async def test_raw_results_async_error`
  - `def test_clean_results_with_images`
  - `def test_clean_results_empty_categories`
  - `def test_clean_results_url_deduplication`

**说明**（自动推断）：

API 包装类 `TestInfoQuestAPIWrapper`，对底层 SDK 做适配与增强，提供统一调用接口。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.tools.test_infoquest_search_api import TestInfoQuestAPIWrapper
#
# TODO: 结合业务场景补充 TestInfoQuestAPIWrapper 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

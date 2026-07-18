# `tests/unit/tools/test_tavily_search_api_wrapper.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/tools/test_tavily_search_api_wrapper.py`
- **模块导入名**：`tests.unit.tools.test_tavily_search_api_wrapper`
- **代码行数**：207
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.tools.tavily_search.tavily_search_api_wrapper import EnhancedTavilySearchAPIWrapper`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import AsyncMock, MagicMock, Mock, patch`
- `import json`
- `import pytest`
- `import requests`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestEnhancedTavilySearchAPIWrapper` | 14 | `` |

## 符号详解

### `TestEnhancedTavilySearchAPIWrapper`

- **类型**：类  |  **行号**：14–207  |  **完整限定名**：`tests.unit.tools.test_tavily_search_api_wrapper.TestEnhancedTavilySearchAPIWrapper`
- **定义**：

```python
class TestEnhancedTavilySearchAPIWrapper:
```
- **成员概览**：

  - `def wrapper`
  - `def mock_response_data`
  - `def test_raw_results_success`
  - `def test_raw_results_with_all_parameters`
  - `def test_raw_results_http_error`
  - `async def test_raw_results_async_success`
  - `async def test_raw_results_async_error`
  - `def test_clean_results_with_images`
  - `def test_clean_results_without_raw_content`
  - `def test_clean_results_empty_images`

**说明**（自动推断）：

API 包装类 `TestEnhancedTavilySearchAPIWrapper`，对底层 SDK 做适配与增强，提供统一调用接口。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.tools.test_tavily_search_api_wrapper import TestEnhancedTavilySearchAPIWrapper
#
# TODO: 结合业务场景补充 TestEnhancedTavilySearchAPIWrapper 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/tools/test_search.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/tools/test_search.py`
- **模块导入名**：`tests.unit.tools.test_search`
- **代码行数**：291
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config import SearchEngine`
- `from src.tools.search import get_web_search_tool`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import patch`
- `from pydantic import ValidationError`
- `import os`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestGetWebSearchTool` | 14 | `` |

## 符号详解

### `TestGetWebSearchTool`

- **类型**：类  |  **行号**：14–291  |  **完整限定名**：`tests.unit.tools.test_search.TestGetWebSearchTool`
- **定义**：

```python
class TestGetWebSearchTool:
```
- **成员概览**：

  - `def test_get_web_search_tool_tavily`
  - `def test_get_web_search_tool_duckduckgo`
  - `def test_get_web_search_tool_brave`
  - `def test_get_web_search_tool_arxiv`
  - `def test_get_web_search_tool_unsupported_engine`
  - `def test_get_web_search_tool_brave_no_api_key`
  - `def test_get_web_search_tool_serper`
  - `def test_get_web_search_tool_serper_no_api_key`
  - `def test_get_web_search_tool_tavily_with_custom_config`
  - `def test_get_web_search_tool_tavily_with_empty_config`
  - `def test_get_web_search_tool_tavily_image_descriptions_disabled_when_images_disabled`
  - `def test_get_web_search_tool_tavily_partial_config`
  - `def test_get_web_search_tool_tavily_with_no_config_file`
  - `def test_get_web_search_tool_tavily_multiple_domains`
  - `def test_tavily_with_no_search_engine_section`
  - `def test_tavily_with_completely_empty_config`
  - `def test_tavily_with_only_include_answer_param`
  - `def test_tavily_with_only_search_depth_param`
  - `def test_tavily_with_only_include_domains_param`
  - `def test_tavily_with_explicit_false_boolean_values`
  - `def test_tavily_with_empty_domain_lists`
  - `def test_tavily_all_parameters_optional_mix`

**说明**（自动推断）：

LangChain 工具类 `TestGetWebSearchTool`，封装为可在智能体中调用的 tool 接口。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.tools.test_search import TestGetWebSearchTool
#
# TODO: 结合业务场景补充 TestGetWebSearchTool 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

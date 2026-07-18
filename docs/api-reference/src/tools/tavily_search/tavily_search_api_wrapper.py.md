# `src/tools/tavily_search/tavily_search_api_wrapper.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/tavily_search/tavily_search_api_wrapper.py`
- **模块导入名**：`src.tools.tavily_search.tavily_search_api_wrapper`
- **代码行数**：136
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
Tavily 搜索 API 增强封装模块。

在 ``langchain_tavily`` 原生 ``TavilySearchAPIWrapper`` 基础上扩展，
提供同步与异步的 ``raw_results`` / ``raw_results_async`` 方法，
支持图像、图像描述等额外字段的检索，并通过 ``SearchResultPostProcessor`` 对结果进行后处理。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config import load_yaml_config`
- `from src.tools.search_postprocessor import SearchResultPostProcessor`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Dict, List, Optional`
- `from langchain_tavily._utilities import TAVILY_API_URL`
- `from langchain_tavily.tavily_search import TavilySearchAPIWrapper`
- `import json`
- `import aiohttp`
- `import requests`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `get_search_config` | 24 | `()` |
| 类 | `EnhancedTavilySearchAPIWrapper` | 30 | `` |

## 符号详解

### `get_search_config`

- **类型**：函数  |  **行号**：24–27  |  **完整限定名**：`src.tools.tavily_search.tavily_search_api_wrapper.get_search_config`
- **签名**：

```python
def get_search_config():
```

**说明**（自动推断）：

从 `conf.yaml` 读取搜索引擎配置段并返回字典，供搜索工具初始化时使用。

### `EnhancedTavilySearchAPIWrapper`

- **类型**：类  |  **行号**：30–136  |  **完整限定名**：`src.tools.tavily_search.tavily_search_api_wrapper.EnhancedTavilySearchAPIWrapper`
- **基类**：`OriginalTavilySearchAPIWrapper`
- **定义**：

```python
class EnhancedTavilySearchAPIWrapper(OriginalTavilySearchAPIWrapper):
```
- **成员概览**：

  - `def raw_results`
  - `async def raw_results_async`
  - `def clean_results_with_images`

**说明**（自动推断）：

API 包装类 `EnhancedTavilySearchAPIWrapper`，对底层 SDK 做适配与增强，提供统一调用接口。

## 调用关系（下游）

**被以下模块导入**：

- `src.tools.tavily_search`
- `src.tools.tavily_search.tavily_search_results_with_images`
- `tests.unit.tools.test_tavily_search_api_wrapper`
- `tests.unit.tools.test_tavily_search_results_with_images`

## 示例用法

```python
from src.tools.tavily_search.tavily_search_api_wrapper import get_search_config
#
# TODO: 结合业务场景补充 get_search_config 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

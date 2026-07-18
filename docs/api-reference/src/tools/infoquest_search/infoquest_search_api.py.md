# `src/tools/infoquest_search/infoquest_search_api.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/infoquest_search/infoquest_search_api.py`
- **模块导入名**：`src.tools.infoquest_search.infoquest_search_api`
- **代码行数**：232
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
Util that calls InfoQuest Search API.

In order to set this up, follow instructions at:
https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config import load_yaml_config`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Dict, List`
- `from langchain_core.utils import get_from_dict_or_env`
- `from pydantic import BaseModel, ConfigDict, SecretStr, model_validator`
- `import json`
- `import aiohttp`
- `import requests`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 20 | `logging.getLogger(__name__)` |
| 常量 | `INFOQUEST_API_URL` | 22 | `'https://search.infoquest.bytepluses.com'` |
| 函数 | `get_search_config` | 24 | `()` |
| 类 | `InfoQuestAPIWrapper` | 29 | `` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：20–20  |  **完整限定名**：`src.tools.infoquest_search.infoquest_search_api.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `INFOQUEST_API_URL`

- **类型**：模块常量  |  **行号**：22–22  |  **完整限定名**：`src.tools.infoquest_search.infoquest_search_api.INFOQUEST_API_URL`
- **值**：

```python
INFOQUEST_API_URL = 'https://search.infoquest.bytepluses.com'
```

**说明**（自动推断）：

外部服务 API 地址常量 `INFOQUEST_API_URL`，在模块导入时从配置或环境变量读取。

### `get_search_config`

- **类型**：函数  |  **行号**：24–27  |  **完整限定名**：`src.tools.infoquest_search.infoquest_search_api.get_search_config`
- **签名**：

```python
def get_search_config():
```

**说明**（自动推断）：

从 `conf.yaml` 读取搜索引擎配置段并返回字典，供搜索工具初始化时使用。

### `InfoQuestAPIWrapper`

- **类型**：类  |  **行号**：29–232  |  **完整限定名**：`src.tools.infoquest_search.infoquest_search_api.InfoQuestAPIWrapper`
- **基类**：`BaseModel`
- **定义**：

```python
class InfoQuestAPIWrapper(BaseModel):
```
- **成员概览**：

  - `attr infoquest_api_key`
  - `attr model_config`
  - `def validate_environment`
  - `def raw_results`
  - `async def raw_results_async`
  - `def clean_results_with_images`

**摘要**：

Wrapper for InfoQuest Search API.

## 调用关系（下游）

**被以下模块导入**：

- `src.tools.infoquest_search`
- `src.tools.infoquest_search.infoquest_search_results`
- `tests.unit.tools.test_infoquest_search_api`

## 示例用法

```python
from src.tools.infoquest_search.infoquest_search_api import get_search_config
#
# TODO: 结合业务场景补充 get_search_config 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

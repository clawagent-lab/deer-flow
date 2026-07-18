# `tests/unit/crawler/test_jina_client.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/crawler/test_jina_client.py`
- **模块导入名**：`tests.unit.crawler.test_jina_client`
- **代码行数**：126
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.crawler.jina_client import JinaClient`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import Mock, patch`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestJinaClient` | 11 | `` |

## 符号详解

### `TestJinaClient`

- **类型**：类  |  **行号**：11–126  |  **完整限定名**：`tests.unit.crawler.test_jina_client.TestJinaClient`
- **定义**：

```python
class TestJinaClient:
```
- **成员概览**：

  - `def test_crawl_success`
  - `def test_crawl_http_error`
  - `def test_crawl_empty_response`
  - `def test_crawl_whitespace_only_response`
  - `def test_crawl_not_found`
  - `def test_crawl_without_api_key_logs_warning`
  - `def test_crawl_exception_handling`

**说明**（自动推断）：

外部服务客户端类 `TestJinaClient`，封装对应的 HTTP 调用与响应解析逻辑。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.crawler.test_jina_client import TestJinaClient
#
# TODO: 结合业务场景补充 TestJinaClient 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

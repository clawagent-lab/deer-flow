# `tests/integration/test_crawler.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/integration/test_crawler.py`
- **模块导入名**：`tests.integration.test_crawler`
- **代码行数**：29
- **架构归属**：tests/integration —— 集成测试（跨组件 / 外部服务，如 crawler、nodes、template、tts）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.crawler import Crawler`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `test_crawler_initialization` | 7 | `()` |
| 函数 | `test_crawler_crawl_valid_url` | 13 | `()` |
| 函数 | `test_crawler_markdown_output` | 22 | `()` |

## 符号详解

### `test_crawler_initialization`

- **类型**：函数  |  **行号**：7–10  |  **完整限定名**：`tests.integration.test_crawler.test_crawler_initialization`
- **签名**：

```python
def test_crawler_initialization():
```

**摘要**：

Test that crawler can be properly initialized.

### `test_crawler_crawl_valid_url`

- **类型**：函数  |  **行号**：13–19  |  **完整限定名**：`tests.integration.test_crawler.test_crawler_crawl_valid_url`
- **签名**：

```python
def test_crawler_crawl_valid_url():
```

**摘要**：

Test crawling with a valid URL.

### `test_crawler_markdown_output`

- **类型**：函数  |  **行号**：22–29  |  **完整限定名**：`tests.integration.test_crawler.test_crawler_markdown_output`
- **签名**：

```python
def test_crawler_markdown_output():
```

**摘要**：

Test that crawler output can be converted to markdown.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.integration.test_crawler import test_crawler_initialization
#
# TODO: 结合业务场景补充 test_crawler_initialization 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

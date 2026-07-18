# `tests/unit/checkpoint/postgres_mock_utils.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/checkpoint/postgres_mock_utils.py`
- **模块导入名**：`tests.unit.checkpoint.postgres_mock_utils`
- **代码行数**：153
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from pathlib import Path`
- `from typing import Any, Dict, Optional`
- `from unittest.mock import MagicMock, patch`
- `import shutil`
- `import tempfile`
- `import psycopg`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `PostgreSQLMockInstance` | 14 | `` |
| 函数 | `mock_postgresql` | 138 | `()` |
| 函数 | `clean_mock_postgresql` | 147 | `()` |

## 符号详解

### `PostgreSQLMockInstance`

- **类型**：类  |  **行号**：14–134  |  **完整限定名**：`tests.unit.checkpoint.postgres_mock_utils.PostgreSQLMockInstance`
- **定义**：

```python
class PostgreSQLMockInstance:
```
- **成员概览**：

  - `def __init__`
  - `def _setup_mock_data`
  - `def connect`
  - `def _setup_mock_methods`
  - `def _mock_execute`
  - `def _mock_fetchone`
  - `def disconnect`
  - `def reset_data`
  - `def get_table_count`
  - `def create_test_data`

**摘要**：

Utility class for managing PostgreSQL mock instances.

### `mock_postgresql`

- **类型**：函数  |  **行号**：138–143  |  **完整限定名**：`tests.unit.checkpoint.postgres_mock_utils.mock_postgresql`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_postgresql():
```

**摘要**：

Create a PostgreSQL mock instance.

### `clean_mock_postgresql`

- **类型**：函数  |  **行号**：147–153  |  **完整限定名**：`tests.unit.checkpoint.postgres_mock_utils.clean_mock_postgresql`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def clean_mock_postgresql():
```

**摘要**：

Create a clean PostgreSQL mock instance that resets between tests.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.checkpoint.postgres_mock_utils import mock_postgresql
#
# TODO: 结合业务场景补充 mock_postgresql 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

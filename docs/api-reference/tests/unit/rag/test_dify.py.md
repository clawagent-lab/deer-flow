# `tests/unit/rag/test_dify.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/rag/test_dify.py`
- **模块导入名**：`tests.unit.rag.test_dify`
- **代码行数**：154
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.rag.dify import DifyProvider, parse_uri`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `DummyResource` | 12 | `` |
| 类 | `DummyChunk` | 19 | `` |
| 类 | `DummyDocument` | 25 | `` |
| 函数 | `patch_imports` | 34 | `(monkeypatch)` |
| 函数 | `test_parse_uri_valid` | 43 | `()` |
| 函数 | `test_parse_uri_invalid` | 50 | `()` |
| 函数 | `test_init_env_vars` | 55 | `(monkeypatch)` |
| 函数 | `test_init_missing_env` | 63 | `(monkeypatch)` |
| 函数 | `test_query_relevant_documents_success` | 75 | `(mock_post, monkeypatch)` |
| 函数 | `test_query_relevant_documents_error` | 107 | `(mock_post, monkeypatch)` |
| 函数 | `test_list_resources_success` | 121 | `(mock_get, monkeypatch)` |
| 函数 | `test_list_resources_error` | 145 | `(mock_get, monkeypatch)` |

## 符号详解

### `DummyResource`

- **类型**：类  |  **行号**：12–16  |  **完整限定名**：`tests.unit.rag.test_dify.DummyResource`
- **定义**：

```python
class DummyResource:
```
- **成员概览**：

  - `def __init__`

**说明**（自动推断）：

测试用替身类 `DummyResource`，模拟真实对象的接口行为以隔离外部依赖。

### `DummyChunk`

- **类型**：类  |  **行号**：19–22  |  **完整限定名**：`tests.unit.rag.test_dify.DummyChunk`
- **定义**：

```python
class DummyChunk:
```
- **成员概览**：

  - `def __init__`

**说明**（自动推断）：

测试用替身类 `DummyChunk`，模拟真实对象的接口行为以隔离外部依赖。

### `DummyDocument`

- **类型**：类  |  **行号**：25–29  |  **完整限定名**：`tests.unit.rag.test_dify.DummyDocument`
- **定义**：

```python
class DummyDocument:
```
- **成员概览**：

  - `def __init__`

**说明**（自动推断）：

测试用替身类 `DummyDocument`，模拟真实对象的接口行为以隔离外部依赖。

### `patch_imports`

- **类型**：函数  |  **行号**：34–40  |  **完整限定名**：`tests.unit.rag.test_dify.patch_imports`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_imports(monkeypatch):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_imports`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `test_parse_uri_valid`

- **类型**：函数  |  **行号**：43–47  |  **完整限定名**：`tests.unit.rag.test_dify.test_parse_uri_valid`
- **签名**：

```python
def test_parse_uri_valid():
```

**说明**（自动推断）：

测试用例函数 `test_parse_uri_valid`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_parse_uri_invalid`

- **类型**：函数  |  **行号**：50–52  |  **完整限定名**：`tests.unit.rag.test_dify.test_parse_uri_invalid`
- **签名**：

```python
def test_parse_uri_invalid():
```

**说明**（自动推断）：

测试用例函数 `test_parse_uri_invalid`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_init_env_vars`

- **类型**：函数  |  **行号**：55–60  |  **完整限定名**：`tests.unit.rag.test_dify.test_init_env_vars`
- **签名**：

```python
def test_init_env_vars(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_init_env_vars`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_init_missing_env`

- **类型**：函数  |  **行号**：63–71  |  **完整限定名**：`tests.unit.rag.test_dify.test_init_missing_env`
- **签名**：

```python
def test_init_missing_env(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_init_missing_env`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_query_relevant_documents_success`

- **类型**：函数  |  **行号**：75–103  |  **完整限定名**：`tests.unit.rag.test_dify.test_query_relevant_documents_success`
- **装饰器**：`@patch`
- **签名**：

```python
def test_query_relevant_documents_success(mock_post, monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_query_relevant_documents_success`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_query_relevant_documents_error`

- **类型**：函数  |  **行号**：107–117  |  **完整限定名**：`tests.unit.rag.test_dify.test_query_relevant_documents_error`
- **装饰器**：`@patch`
- **签名**：

```python
def test_query_relevant_documents_error(mock_post, monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_query_relevant_documents_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_list_resources_success`

- **类型**：函数  |  **行号**：121–141  |  **完整限定名**：`tests.unit.rag.test_dify.test_list_resources_success`
- **装饰器**：`@patch`
- **签名**：

```python
def test_list_resources_success(mock_get, monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_list_resources_success`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_list_resources_error`

- **类型**：函数  |  **行号**：145–154  |  **完整限定名**：`tests.unit.rag.test_dify.test_list_resources_error`
- **装饰器**：`@patch`
- **签名**：

```python
def test_list_resources_error(mock_get, monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_list_resources_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.rag.test_dify import patch_imports
#
# TODO: 结合业务场景补充 patch_imports 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

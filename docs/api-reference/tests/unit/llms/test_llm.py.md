# `tests/unit/llms/test_llm.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/llms/test_llm.py`
- **模块导入名**：`tests.unit.llms.test_llm`
- **代码行数**：127
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.llms import llm`

**外部依赖**（第三方库 / 标准库）：

- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `DummyChatOpenAI` | 9 | `` |
| 函数 | `patch_chat_openai` | 18 | `(monkeypatch)` |
| 函数 | `dummy_conf` | 23 | `()` |
| 函数 | `test_get_env_llm_conf` | 31 | `(monkeypatch)` |
| 函数 | `test_create_llm_use_conf_merges_env` | 44 | `(monkeypatch, dummy_conf)` |
| 函数 | `test_create_llm_use_conf_invalid_type` | 55 | `(monkeypatch, dummy_conf)` |
| 函数 | `test_create_llm_use_conf_empty_conf` | 65 | `(monkeypatch)` |
| 函数 | `test_get_llm_by_type_caches` | 75 | `(monkeypatch, dummy_conf)` |
| 函数 | `test_create_llm_filters_unexpected_keys` | 90 | `(monkeypatch, caplog)` |

## 符号详解

### `DummyChatOpenAI`

- **类型**：类  |  **行号**：9–14  |  **完整限定名**：`tests.unit.llms.test_llm.DummyChatOpenAI`
- **定义**：

```python
class DummyChatOpenAI:
```
- **成员概览**：

  - `def __init__`
  - `def invoke`

**说明**（自动推断）：

测试用替身类 `DummyChatOpenAI`，模拟真实对象的接口行为以隔离外部依赖。

### `patch_chat_openai`

- **类型**：函数  |  **行号**：18–19  |  **完整限定名**：`tests.unit.llms.test_llm.patch_chat_openai`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_chat_openai(monkeypatch):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_chat_openai`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `dummy_conf`

- **类型**：函数  |  **行号**：23–28  |  **完整限定名**：`tests.unit.llms.test_llm.dummy_conf`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def dummy_conf():
```

**说明**（自动推断）：

测试配置 fixture `dummy_conf`，构造被测模块所需的配置对象。

### `test_get_env_llm_conf`

- **类型**：函数  |  **行号**：31–41  |  **完整限定名**：`tests.unit.llms.test_llm.test_get_env_llm_conf`
- **签名**：

```python
def test_get_env_llm_conf(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_get_env_llm_conf`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_create_llm_use_conf_merges_env`

- **类型**：函数  |  **行号**：44–52  |  **完整限定名**：`tests.unit.llms.test_llm.test_create_llm_use_conf_merges_env`
- **签名**：

```python
def test_create_llm_use_conf_merges_env(monkeypatch, dummy_conf):
```

**说明**（自动推断）：

测试用例函数 `test_create_llm_use_conf_merges_env`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_create_llm_use_conf_invalid_type`

- **类型**：函数  |  **行号**：55–62  |  **完整限定名**：`tests.unit.llms.test_llm.test_create_llm_use_conf_invalid_type`
- **签名**：

```python
def test_create_llm_use_conf_invalid_type(monkeypatch, dummy_conf):
```

**说明**（自动推断）：

测试用例函数 `test_create_llm_use_conf_invalid_type`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_create_llm_use_conf_empty_conf`

- **类型**：函数  |  **行号**：65–72  |  **完整限定名**：`tests.unit.llms.test_llm.test_create_llm_use_conf_empty_conf`
- **签名**：

```python
def test_create_llm_use_conf_empty_conf(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_create_llm_use_conf_empty_conf`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_get_llm_by_type_caches`

- **类型**：函数  |  **行号**：75–87  |  **完整限定名**：`tests.unit.llms.test_llm.test_get_llm_by_type_caches`
- **签名**：

```python
def test_get_llm_by_type_caches(monkeypatch, dummy_conf):
```

**说明**（自动推断）：

测试用例函数 `test_get_llm_by_type_caches`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_create_llm_filters_unexpected_keys`

- **类型**：函数  |  **行号**：90–127  |  **完整限定名**：`tests.unit.llms.test_llm.test_create_llm_filters_unexpected_keys`
- **签名**：

```python
def test_create_llm_filters_unexpected_keys(monkeypatch, caplog):
```

**摘要**：

Test that unexpected configuration keys like SEARCH_ENGINE are filtered out (Issue #411).

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.llms.test_llm import patch_chat_openai
#
# TODO: 结合业务场景补充 patch_chat_openai 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

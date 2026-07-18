# `tests/test_ppt_localization.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/test_ppt_localization.py`
- **模块导入名**：`tests.test_ppt_localization`
- **代码行数**：135
- **架构归属**：tests —— 测试套件根目录（pytest + pytest-asyncio + pytest-cov，覆盖率门槛 25%）

## 模块概述

```text
Unit tests for PPT composer localization functionality.

These tests verify that the ppt_composer_node correctly passes locale information
to get_prompt_template, allowing for locale-specific prompt selection.
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `MockLLMResponse` | 14 | `` |
| 类 | `MockLLM` | 21 | `` |
| 类 | `TestPPTLocalization` | 29 | `` |

## 符号详解

### `MockLLMResponse`

- **类型**：类  |  **行号**：14–18  |  **完整限定名**：`tests.test_ppt_localization.MockLLMResponse`
- **定义**：

```python
class MockLLMResponse:
```
- **成员概览**：

  - `def __init__`

**摘要**：

Mock LLM response object.

### `MockLLM`

- **类型**：类  |  **行号**：21–26  |  **完整限定名**：`tests.test_ppt_localization.MockLLM`
- **定义**：

```python
class MockLLM:
```
- **成员概览**：

  - `def invoke`

**摘要**：

Mock LLM model with invoke method.

### `TestPPTLocalization`

- **类型**：类  |  **行号**：29–135  |  **完整限定名**：`tests.test_ppt_localization.TestPPTLocalization`
- **定义**：

```python
class TestPPTLocalization:
```
- **成员概览**：

  - `def test_locale_passed_to_prompt_template`
  - `def test_default_locale_fallback`

**摘要**：

Test suite for PPT composer locale handling.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.test_ppt_localization import MockLLMResponse
#
# TODO: 结合业务场景补充 MockLLMResponse 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

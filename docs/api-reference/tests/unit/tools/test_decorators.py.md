# `tests/unit/tools/test_decorators.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/tools/test_decorators.py`
- **模块导入名**：`tests.unit.tools.test_decorators`
- **代码行数**：119
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.tools.decorators import create_logged_tool`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import Mock, call, patch`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `MockBaseTool` | 9 | `` |
| 类 | `TestLoggedToolMixin` | 16 | `` |

## 符号详解

### `MockBaseTool`

- **类型**：类  |  **行号**：9–13  |  **完整限定名**：`tests.unit.tools.test_decorators.MockBaseTool`
- **定义**：

```python
class MockBaseTool:
```
- **成员概览**：

  - `def _run`

**摘要**：

Mock base tool class for testing.

### `TestLoggedToolMixin`

- **类型**：类  |  **行号**：16–119  |  **完整限定名**：`tests.unit.tools.test_decorators.TestLoggedToolMixin`
- **定义**：

```python
class TestLoggedToolMixin:
```
- **成员概览**：

  - `def test_run_calls_log_operation`
  - `def test_run_calls_super_run`
  - `def test_run_logs_result`
  - `def test_run_returns_super_result`
  - `def test_run_with_no_args`
  - `def test_run_with_mixed_args_kwargs`
  - `def test_run_class_name_replacement`

**说明**（自动推断）：

pytest 测试类 `TestLoggedToolMixin`，聚合一组相关的测试用例方法（以 `test_` 开头）。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.tools.test_decorators import MockBaseTool
#
# TODO: 结合业务场景补充 MockBaseTool 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

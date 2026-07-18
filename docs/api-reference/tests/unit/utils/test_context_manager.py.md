# `tests/unit/utils/test_context_manager.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/utils/test_context_manager.py`
- **模块导入名**：`tests.unit.utils.test_context_manager`
- **代码行数**：235
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.utils.context_manager import ContextManager`

**外部依赖**（第三方库 / 标准库）：

- `from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestContextManager` | 7 | `` |

## 符号详解

### `TestContextManager`

- **类型**：类  |  **行号**：7–235  |  **完整限定名**：`tests.unit.utils.test_context_manager.TestContextManager`
- **定义**：

```python
class TestContextManager:
```
- **成员概览**：

  - `def test_count_tokens_with_empty_messages`
  - `def test_count_tokens_with_system_message`
  - `def test_count_tokens_with_human_message`
  - `def test_count_tokens_with_ai_message`
  - `def test_count_tokens_with_tool_message`
  - `def test_count_tokens_with_multiple_messages`
  - `def test_is_over_limit_when_under_limit`
  - `def test_is_over_limit_when_over_limit`
  - `def test_compress_messages_when_not_over_limit`
  - `def test_compress_messages_with_tool_message`
  - `def test_compress_messages_with_preserve_prefix_message`
  - `def test_compress_messages_without_config`
  - `def test_count_message_tokens_with_additional_kwargs`
  - `def test_count_message_tokens_minimum_one_token`
  - `def test_count_text_tokens_english_only`
  - `def test_count_text_tokens_chinese_only`
  - `def test_count_text_tokens_mixed_content`
  - `def test_compress_messages_with_runtime_when_not_over_limit`
  - `def test_compress_messages_with_runtime_when_over_limit`

**摘要**：

Test cases for ContextManager

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.utils.test_context_manager import TestContextManager
#
# TODO: 结合业务场景补充 TestContextManager 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/podcast/test_script_writer_node.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/podcast/test_script_writer_node.py`
- **模块导入名**：`tests.unit.podcast.test_script_writer_node`
- **代码行数**：214
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.podcast.graph.script_writer_node import script_writer_node`
- `from src.podcast.types import Script, ScriptLine`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `import json`
- `import openai`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestScriptWriterNode` | 14 | `` |

## 符号详解

### `TestScriptWriterNode`

- **类型**：类  |  **行号**：14–214  |  **完整限定名**：`tests.unit.podcast.test_script_writer_node.TestScriptWriterNode`
- **定义**：

```python
class TestScriptWriterNode:
```
- **成员概览**：

  - `def sample_state`
  - `def sample_script`
  - `def sample_script_json`
  - `def test_script_writer_with_json_mode_success`
  - `def test_script_writer_fallback_on_json_object_not_supported`
  - `def test_script_writer_reraises_other_bad_request_errors`
  - `def test_script_writer_fallback_with_markdown_wrapped_json`
  - `def test_script_writer_fallback_raises_on_invalid_json`
  - `def test_script_writer_fallback_raises_on_invalid_schema`

**摘要**：

Tests for script_writer_node function.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.podcast.test_script_writer_node import TestScriptWriterNode
#
# TODO: 结合业务场景补充 TestScriptWriterNode 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/server/test_tool_call_chunks.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/server/test_tool_call_chunks.py`
- **模块导入名**：`tests.unit.server.test_tool_call_chunks`
- **代码行数**：317
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for tool call chunk processing.

Tests for the fix of issue #523: Tool name concatenation in consecutive tool calls.
This ensures that tool call chunks are properly segregated by index to prevent
tool names from being concatenated when multiple tool calls happen in sequence.
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.server.app import _process_tool_call_chunks, _validate_tool_call_chunks`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `import logging`
- `import os`
- `import sys`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestProcessToolCallChunks` | 28 | `` |
| 类 | `TestValidateToolCallChunks` | 192 | `` |
| 类 | `TestRealWorldScenarios` | 230 | `` |

## 符号详解

### `TestProcessToolCallChunks`

- **类型**：类  |  **行号**：28–189  |  **完整限定名**：`tests.unit.server.test_tool_call_chunks.TestProcessToolCallChunks`
- **定义**：

```python
class TestProcessToolCallChunks:
```
- **成员概览**：

  - `def test_empty_tool_call_chunks`
  - `def test_single_tool_call_single_chunk`
  - `def test_consecutive_tool_calls_different_indices`
  - `def test_different_tools_different_indices`
  - `def test_streaming_chunks_same_index`
  - `def test_tool_call_index_collision_warning`
  - `def test_chunks_without_explicit_index`
  - `def test_chunk_sorting_by_index`
  - `def test_args_accumulation`
  - `def test_preserve_tool_id`
  - `def test_multiple_indices_detected`

**摘要**：

Test cases for _process_tool_call_chunks function.

### `TestValidateToolCallChunks`

- **类型**：类  |  **行号**：192–227  |  **完整限定名**：`tests.unit.server.test_tool_call_chunks.TestValidateToolCallChunks`
- **定义**：

```python
class TestValidateToolCallChunks:
```
- **成员概览**：

  - `def test_validate_empty_chunks`
  - `def test_validate_logs_chunk_info`
  - `def test_validate_detects_multiple_indices`

**摘要**：

Test cases for _validate_tool_call_chunks function.

### `TestRealWorldScenarios`

- **类型**：类  |  **行号**：230–313  |  **完整限定名**：`tests.unit.server.test_tool_call_chunks.TestRealWorldScenarios`
- **定义**：

```python
class TestRealWorldScenarios:
```
- **成员概览**：

  - `def test_issue_523_scenario_consecutive_web_search`
  - `def test_mixed_tools_consecutive_calls`
  - `def test_long_sequence_tool_calls`

**摘要**：

Test cases for real-world scenarios from issue #523.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.server.test_tool_call_chunks import TestProcessToolCallChunks
#
# TODO: 结合业务场景补充 TestProcessToolCallChunks 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

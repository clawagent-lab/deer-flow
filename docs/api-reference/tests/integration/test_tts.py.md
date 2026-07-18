# `tests/integration/test_tts.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/integration/test_tts.py`
- **模块导入名**：`tests.integration.test_tts`
- **代码行数**：247
- **架构归属**：tests/integration —— 集成测试（跨组件 / 外部服务，如 crawler、nodes、template、tts）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.tools.tts import VolcengineTTS`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `import base64`
- `import json`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestVolcengineTTS` | 11 | `` |

## 符号详解

### `TestVolcengineTTS`

- **类型**：类  |  **行号**：11–247  |  **完整限定名**：`tests.integration.test_tts.TestVolcengineTTS`
- **定义**：

```python
class TestVolcengineTTS:
```
- **成员概览**：

  - `def test_initialization`
  - `def test_initialization_with_defaults`
  - `def test_text_to_speech_success`
  - `def test_text_to_speech_api_error`
  - `def test_text_to_speech_no_data`
  - `def test_text_to_speech_with_custom_parameters`
  - `def test_text_to_speech_auto_generated_uid`
  - `def test_text_to_speech_request_exception`

**摘要**：

Test suite for the VolcengineTTS class.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.integration.test_tts import TestVolcengineTTS
#
# TODO: 结合业务场景补充 TestVolcengineTTS 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

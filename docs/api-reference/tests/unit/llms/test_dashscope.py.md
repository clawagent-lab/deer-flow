# `tests/unit/llms/test_dashscope.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/llms/test_dashscope.py`
- **模块导入名**：`tests.unit.llms.test_dashscope`
- **代码行数**：305
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.llms import llm`
- `from src.llms.providers import dashscope`
- `from src.llms.providers.dashscope import ChatDashscope, _convert_chunk_to_generation_chunk, _convert_delta_to_message_chunk`

**外部依赖**（第三方库 / 标准库）：

- `from langchain_core.messages import AIMessageChunk, ChatMessageChunk, FunctionMessageChunk, HumanMessageChunk, SystemMessageChunk, ToolMessageChunk`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `DummyChatDashscope` | 23 | `` |
| 函数 | `dashscope_conf` | 29 | `()` |
| 函数 | `test_convert_delta_to_message_chunk_roles_and_extras` | 44 | `()` |
| 函数 | `test_convert_chunk_to_generation_chunk_skip_and_usage` | 86 | `()` |
| 函数 | `test_llm_selects_dashscope_and_sets_enable_thinking` | 118 | `(monkeypatch, dashscope_conf)` |
| 函数 | `test_llm_verify_ssl_false_adds_http_clients` | 134 | `(monkeypatch, dashscope_conf)` |
| 函数 | `test_convert_delta_to_message_chunk_developer_and_function_call_and_tool_calls` | 148 | `()` |
| 函数 | `test_convert_delta_to_message_chunk_default_class_and_unknown_role` | 177 | `()` |
| 函数 | `test_convert_chunk_to_generation_chunk_empty_choices_and_usage` | 190 | `()` |
| 函数 | `test_convert_chunk_to_generation_chunk_includes_base_info_and_logprobs` | 203 | `()` |
| 函数 | `test_convert_chunk_to_generation_chunk_beta_stream_format` | 220 | `()` |
| 函数 | `test_chatdashscope_create_chat_result_adds_reasoning_content` | 233 | `(monkeypatch)` |
| 函数 | `test_chatdashscope_create_chat_result_dict_passthrough` | 282 | `(monkeypatch)` |

## 符号详解

### `DummyChatDashscope`

- **类型**：类  |  **行号**：23–25  |  **完整限定名**：`tests.unit.llms.test_dashscope.DummyChatDashscope`
- **定义**：

```python
class DummyChatDashscope:
```
- **成员概览**：

  - `def __init__`

**说明**（自动推断）：

测试用替身类 `DummyChatDashscope`，模拟真实对象的接口行为以隔离外部依赖。

### `dashscope_conf`

- **类型**：函数  |  **行号**：29–41  |  **完整限定名**：`tests.unit.llms.test_dashscope.dashscope_conf`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def dashscope_conf():
```

**说明**（自动推断）：

测试配置 fixture `dashscope_conf`，构造被测模块所需的配置对象。

### `test_convert_delta_to_message_chunk_roles_and_extras`

- **类型**：函数  |  **行号**：44–83  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_convert_delta_to_message_chunk_roles_and_extras`
- **签名**：

```python
def test_convert_delta_to_message_chunk_roles_and_extras():
```

**说明**（自动推断）：

测试用例函数 `test_convert_delta_to_message_chunk_roles_and_extras`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_convert_chunk_to_generation_chunk_skip_and_usage`

- **类型**：函数  |  **行号**：86–115  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_convert_chunk_to_generation_chunk_skip_and_usage`
- **签名**：

```python
def test_convert_chunk_to_generation_chunk_skip_and_usage():
```

**说明**（自动推断）：

测试用例函数 `test_convert_chunk_to_generation_chunk_skip_and_usage`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_llm_selects_dashscope_and_sets_enable_thinking`

- **类型**：函数  |  **行号**：118–131  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_llm_selects_dashscope_and_sets_enable_thinking`
- **签名**：

```python
def test_llm_selects_dashscope_and_sets_enable_thinking(monkeypatch, dashscope_conf):
```

**说明**（自动推断）：

测试用例函数 `test_llm_selects_dashscope_and_sets_enable_thinking`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_llm_verify_ssl_false_adds_http_clients`

- **类型**：函数  |  **行号**：134–145  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_llm_verify_ssl_false_adds_http_clients`
- **签名**：

```python
def test_llm_verify_ssl_false_adds_http_clients(monkeypatch, dashscope_conf):
```

**说明**（自动推断）：

测试用例函数 `test_llm_verify_ssl_false_adds_http_clients`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_convert_delta_to_message_chunk_developer_and_function_call_and_tool_calls`

- **类型**：函数  |  **行号**：148–174  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_convert_delta_to_message_chunk_developer_and_function_call_and_tool_calls`
- **签名**：

```python
def test_convert_delta_to_message_chunk_developer_and_function_call_and_tool_calls():
```

**说明**（自动推断）：

测试用例函数 `test_convert_delta_to_message_chunk_developer_and_function_call_and_tool_calls`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_convert_delta_to_message_chunk_default_class_and_unknown_role`

- **类型**：函数  |  **行号**：177–187  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_convert_delta_to_message_chunk_default_class_and_unknown_role`
- **签名**：

```python
def test_convert_delta_to_message_chunk_default_class_and_unknown_role():
```

**说明**（自动推断）：

测试用例函数 `test_convert_delta_to_message_chunk_default_class_and_unknown_role`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_convert_chunk_to_generation_chunk_empty_choices_and_usage`

- **类型**：函数  |  **行号**：190–200  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_convert_chunk_to_generation_chunk_empty_choices_and_usage`
- **签名**：

```python
def test_convert_chunk_to_generation_chunk_empty_choices_and_usage():
```

**说明**（自动推断）：

测试用例函数 `test_convert_chunk_to_generation_chunk_empty_choices_and_usage`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_convert_chunk_to_generation_chunk_includes_base_info_and_logprobs`

- **类型**：函数  |  **行号**：203–217  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_convert_chunk_to_generation_chunk_includes_base_info_and_logprobs`
- **签名**：

```python
def test_convert_chunk_to_generation_chunk_includes_base_info_and_logprobs():
```

**说明**（自动推断）：

测试用例函数 `test_convert_chunk_to_generation_chunk_includes_base_info_and_logprobs`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_convert_chunk_to_generation_chunk_beta_stream_format`

- **类型**：函数  |  **行号**：220–230  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_convert_chunk_to_generation_chunk_beta_stream_format`
- **签名**：

```python
def test_convert_chunk_to_generation_chunk_beta_stream_format():
```

**说明**（自动推断）：

测试用例函数 `test_convert_chunk_to_generation_chunk_beta_stream_format`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_chatdashscope_create_chat_result_adds_reasoning_content`

- **类型**：函数  |  **行号**：233–279  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_chatdashscope_create_chat_result_adds_reasoning_content`
- **签名**：

```python
def test_chatdashscope_create_chat_result_adds_reasoning_content(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_chatdashscope_create_chat_result_adds_reasoning_content`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_chatdashscope_create_chat_result_dict_passthrough`

- **类型**：函数  |  **行号**：282–305  |  **完整限定名**：`tests.unit.llms.test_dashscope.test_chatdashscope_create_chat_result_dict_passthrough`
- **签名**：

```python
def test_chatdashscope_create_chat_result_dict_passthrough(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_chatdashscope_create_chat_result_dict_passthrough`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.llms.test_dashscope import dashscope_conf
#
# TODO: 结合业务场景补充 dashscope_conf 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

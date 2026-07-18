# `tests/unit/prompt_enhancer/graph/test_enhancer_node.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/prompt_enhancer/graph/test_enhancer_node.py`
- **模块导入名**：`tests.unit.prompt_enhancer.graph.test_enhancer_node`
- **代码行数**：526
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.report_style import ReportStyle`
- `from src.prompt_enhancer.graph.enhancer_node import prompt_enhancer_node`
- `from src.prompt_enhancer.graph.state import PromptEnhancerState`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `from langchain_core.messages import HumanMessage, SystemMessage`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `mock_llm` | 15 | `()` |
| 函数 | `mock_llm_xml_with_whitespace` | 29 | `()` |
| 函数 | `mock_llm_xml_multiline` | 49 | `()` |
| 函数 | `mock_llm_no_xml` | 67 | `()` |
| 函数 | `mock_llm_malformed_xml` | 77 | `()` |
| 函数 | `mock_messages` | 91 | `()` |
| 类 | `TestPromptEnhancerNode` | 99 | `` |

## 符号详解

### `mock_llm`

- **类型**：函数  |  **行号**：15–25  |  **完整限定名**：`tests.unit.prompt_enhancer.graph.test_enhancer_node.mock_llm`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_llm():
```

**摘要**：

Mock LLM that returns a test response.

### `mock_llm_xml_with_whitespace`

- **类型**：函数  |  **行号**：29–45  |  **完整限定名**：`tests.unit.prompt_enhancer.graph.test_enhancer_node.mock_llm_xml_with_whitespace`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_llm_xml_with_whitespace():
```

**摘要**：

Mock LLM that returns XML response with extra whitespace.

### `mock_llm_xml_multiline`

- **类型**：函数  |  **行号**：49–63  |  **完整限定名**：`tests.unit.prompt_enhancer.graph.test_enhancer_node.mock_llm_xml_multiline`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_llm_xml_multiline():
```

**摘要**：

Mock LLM that returns XML response with multiline content.

### `mock_llm_no_xml`

- **类型**：函数  |  **行号**：67–73  |  **完整限定名**：`tests.unit.prompt_enhancer.graph.test_enhancer_node.mock_llm_no_xml`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_llm_no_xml():
```

**摘要**：

Mock LLM that returns response without XML tags.

### `mock_llm_malformed_xml`

- **类型**：函数  |  **行号**：77–87  |  **完整限定名**：`tests.unit.prompt_enhancer.graph.test_enhancer_node.mock_llm_malformed_xml`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_llm_malformed_xml():
```

**摘要**：

Mock LLM that returns response with malformed XML.

### `mock_messages`

- **类型**：函数  |  **行号**：91–96  |  **完整限定名**：`tests.unit.prompt_enhancer.graph.test_enhancer_node.mock_messages`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_messages():
```

**摘要**：

Mock messages returned by apply_prompt_template.

### `TestPromptEnhancerNode`

- **类型**：类  |  **行号**：99–526  |  **完整限定名**：`tests.unit.prompt_enhancer.graph.test_enhancer_node.TestPromptEnhancerNode`
- **定义**：

```python
class TestPromptEnhancerNode:
```
- **成员概览**：

  - `def test_basic_prompt_enhancement`
  - `def test_prompt_enhancement_with_report_style`
  - `def test_prompt_enhancement_with_context`
  - `def test_error_handling`
  - `def test_template_error_handling`
  - `def test_prefix_removal`
  - `def test_whitespace_handling`
  - `def test_xml_with_whitespace_handling`
  - `def test_xml_multiline_content`
  - `def test_fallback_to_prefix_removal`
  - `def test_malformed_xml_fallback`
  - `def test_case_sensitive_prefix_removal`
  - `def test_prefix_with_extra_whitespace`
  - `def test_xml_with_special_characters`
  - `def test_very_long_response`
  - `def test_empty_response_content`
  - `def test_only_whitespace_response`

**摘要**：

Test cases for prompt_enhancer_node function.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.prompt_enhancer.graph.test_enhancer_node import mock_llm
#
# TODO: 结合业务场景补充 mock_llm 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

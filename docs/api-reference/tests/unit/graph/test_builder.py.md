# `tests/unit/graph/test_builder.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/graph/test_builder.py`
- **模块导入名**：`tests.unit.graph.test_builder`
- **代码行数**：134
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `import src.graph.builder`

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock, patch`
- `import importlib`
- `import sys`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `mock_state` | 14 | `()` |
| 函数 | `test_continue_to_running_research_team_no_plan` | 30 | `(mock_state)` |
| 函数 | `test_continue_to_running_research_team_no_steps` | 35 | `(mock_state)` |
| 函数 | `test_continue_to_running_research_team_all_executed` | 40 | `(mock_state)` |
| 函数 | `test_continue_to_running_research_team_next_researcher` | 48 | `(mock_state)` |
| 函数 | `test_continue_to_running_research_team_next_coder` | 59 | `(mock_state)` |
| 函数 | `test_continue_to_running_research_team_next_coder_withresult` | 70 | `(mock_state)` |
| 函数 | `test_continue_to_running_research_team_default_planner` | 81 | `(mock_state)` |
| 函数 | `test_build_base_graph_adds_nodes_and_edges` | 90 | `(MockStateGraph)` |
| 函数 | `test_build_graph_with_memory_uses_memory` | 105 | `(MockMemorySaver, mock_build_base_graph)` |
| 函数 | `test_build_graph_without_memory` | 117 | `(mock_build_base_graph)` |
| 函数 | `test_graph_is_compiled` | 126 | `()` |

## 符号详解

### `mock_state`

- **类型**：函数  |  **行号**：14–27  |  **完整限定名**：`tests.unit.graph.test_builder.mock_state`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `test_continue_to_running_research_team_no_plan`

- **类型**：函数  |  **行号**：30–32  |  **完整限定名**：`tests.unit.graph.test_builder.test_continue_to_running_research_team_no_plan`
- **签名**：

```python
def test_continue_to_running_research_team_no_plan(mock_state):
```

**说明**（自动推断）：

测试用例函数 `test_continue_to_running_research_team_no_plan`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_continue_to_running_research_team_no_steps`

- **类型**：函数  |  **行号**：35–37  |  **完整限定名**：`tests.unit.graph.test_builder.test_continue_to_running_research_team_no_steps`
- **签名**：

```python
def test_continue_to_running_research_team_no_steps(mock_state):
```

**说明**（自动推断）：

测试用例函数 `test_continue_to_running_research_team_no_steps`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_continue_to_running_research_team_all_executed`

- **类型**：函数  |  **行号**：40–45  |  **完整限定名**：`tests.unit.graph.test_builder.test_continue_to_running_research_team_all_executed`
- **签名**：

```python
def test_continue_to_running_research_team_all_executed(mock_state):
```

**说明**（自动推断）：

测试用例函数 `test_continue_to_running_research_team_all_executed`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_continue_to_running_research_team_next_researcher`

- **类型**：函数  |  **行号**：48–56  |  **完整限定名**：`tests.unit.graph.test_builder.test_continue_to_running_research_team_next_researcher`
- **签名**：

```python
def test_continue_to_running_research_team_next_researcher(mock_state):
```

**说明**（自动推断）：

测试用例函数 `test_continue_to_running_research_team_next_researcher`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_continue_to_running_research_team_next_coder`

- **类型**：函数  |  **行号**：59–67  |  **完整限定名**：`tests.unit.graph.test_builder.test_continue_to_running_research_team_next_coder`
- **签名**：

```python
def test_continue_to_running_research_team_next_coder(mock_state):
```

**说明**（自动推断）：

测试用例函数 `test_continue_to_running_research_team_next_coder`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_continue_to_running_research_team_next_coder_withresult`

- **类型**：函数  |  **行号**：70–78  |  **完整限定名**：`tests.unit.graph.test_builder.test_continue_to_running_research_team_next_coder_withresult`
- **签名**：

```python
def test_continue_to_running_research_team_next_coder_withresult(mock_state):
```

**说明**（自动推断）：

测试用例函数 `test_continue_to_running_research_team_next_coder_withresult`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_continue_to_running_research_team_default_planner`

- **类型**：函数  |  **行号**：81–86  |  **完整限定名**：`tests.unit.graph.test_builder.test_continue_to_running_research_team_default_planner`
- **签名**：

```python
def test_continue_to_running_research_team_default_planner(mock_state):
```

**说明**（自动推断）：

测试用例函数 `test_continue_to_running_research_team_default_planner`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_build_base_graph_adds_nodes_and_edges`

- **类型**：函数  |  **行号**：90–100  |  **完整限定名**：`tests.unit.graph.test_builder.test_build_base_graph_adds_nodes_and_edges`
- **装饰器**：`@patch`
- **签名**：

```python
def test_build_base_graph_adds_nodes_and_edges(MockStateGraph):
```

**说明**（自动推断）：

测试用例函数 `test_build_base_graph_adds_nodes_and_edges`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_build_graph_with_memory_uses_memory`

- **类型**：函数  |  **行号**：105–113  |  **完整限定名**：`tests.unit.graph.test_builder.test_build_graph_with_memory_uses_memory`
- **装饰器**：`@patch`, `@patch`
- **签名**：

```python
def test_build_graph_with_memory_uses_memory(MockMemorySaver, mock_build_base_graph):
```

**说明**（自动推断）：

测试用例函数 `test_build_graph_with_memory_uses_memory`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_build_graph_without_memory`

- **类型**：函数  |  **行号**：117–123  |  **完整限定名**：`tests.unit.graph.test_builder.test_build_graph_without_memory`
- **装饰器**：`@patch`
- **签名**：

```python
def test_build_graph_without_memory(mock_build_base_graph):
```

**说明**（自动推断）：

测试用例函数 `test_build_graph_without_memory`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_graph_is_compiled`

- **类型**：函数  |  **行号**：126–134  |  **完整限定名**：`tests.unit.graph.test_builder.test_graph_is_compiled`
- **签名**：

```python
def test_graph_is_compiled():
```

**说明**（自动推断）：

测试用例函数 `test_graph_is_compiled`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.graph.test_builder import mock_state
#
# TODO: 结合业务场景补充 mock_state 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

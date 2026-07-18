# `tests/integration/test_nodes.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/integration/test_nodes.py`
- **模块导入名**：`tests.integration.test_nodes`
- **代码行数**：3028
- **架构归属**：tests/integration —— 集成测试（跨组件 / 外部服务，如 crawler、nodes、template、tts）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.graph.nodes import _execute_agent_step, _setup_and_execute_agent_step, coordinator_node, human_feedback_node, planner_node, reporter_node, researcher_node, extract_plan_content`
- `from src.prompts.planner_model import Plan`

**外部依赖**（第三方库 / 标准库）：

- `from collections import namedtuple`
- `from unittest.mock import MagicMock, patch`
- `from pydantic import ValidationError`
- `import json`
- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestExtractPlanContent` | 21 | `` |
| 常量 | `MOCK_SEARCH_RESULTS` | 359 | `[{'title': 'Test Title 1', 'content': 'Test Content 1'}, {'title': 'Test Title 2', 'content': 'Te...` |
| 函数 | `mock_state` | 366 | `()` |
| 函数 | `mock_configurable` | 375 | `()` |
| 函数 | `mock_config` | 382 | `()` |
| 函数 | `patch_config_from_runnable_config` | 388 | `(mock_configurable)` |
| 函数 | `mock_tavily_search` | 397 | `()` |
| 函数 | `mock_web_search_tool` | 408 | `()` |
| 函数 | `test_background_investigation_node_tavily` | 419 | `(mock_state, mock_tavily_search, mock_web_search_tool, search_engine, patch_config_from_runnable_...` |
| 函数 | `test_background_investigation_node_malformed_response` | 453 | `(mock_state, mock_tavily_search, patch_config_from_runnable_config, mock_config)` |
| 函数 | `mock_plan` | 475 | `()` |
| 函数 | `mock_state_planner` | 486 | `()` |
| 函数 | `mock_configurable_planner` | 496 | `()` |
| 函数 | `patch_config_from_runnable_config_planner` | 504 | `(mock_configurable_planner)` |
| 函数 | `patch_apply_prompt_template` | 513 | `()` |
| 函数 | `patch_repair_json_output` | 522 | `()` |
| 函数 | `patch_plan_model_validate` | 528 | `()` |
| 函数 | `patch_ai_message` | 534 | `()` |
| 函数 | `test_planner_node_basic_has_enough_context` | 543 | `(mock_state_planner, patch_config_from_runnable_config_planner, patch_apply_prompt_template, patc...` |
| 函数 | `test_planner_node_basic_not_enough_context` | 572 | `(mock_state_planner, patch_config_from_runnable_config_planner, patch_apply_prompt_template, patc...` |
| 函数 | `test_planner_node_stream_mode_has_enough_context` | 607 | `(mock_state_planner, patch_config_from_runnable_config_planner, patch_apply_prompt_template, patc...` |
| 函数 | `test_planner_node_stream_mode_not_enough_context` | 635 | `(mock_state_planner, patch_config_from_runnable_config_planner, patch_apply_prompt_template, patc...` |
| 函数 | `test_planner_node_plan_iterations_exceeded` | 668 | `(mock_state_planner)` |
| 函数 | `test_planner_node_json_decode_error_first_iteration` | 681 | `(mock_state_planner)` |
| 函数 | `test_planner_node_json_decode_error_second_iteration` | 703 | `(mock_state_planner)` |
| 函数 | `patch_plan_and_repair` | 729 | `(monkeypatch)` |
| 函数 | `mock_state_base` | 736 | `()` |
| 函数 | `test_human_feedback_node_auto_accepted` | 751 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_edit_plan` | 762 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_accepted` | 774 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_invalid_interrupt` | 786 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_none_feedback` | 798 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_empty_feedback` | 810 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_json_decode_error_first_iteration` | 822 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_model_validate_error` | 846 | `(mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_list_plan_runs_enforcement_after_normalization` | 883 | `(mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_json_decode_error_second_iteration` | 927 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `test_human_feedback_node_not_enough_context` | 942 | `(monkeypatch, mock_state_base, mock_config)` |
| 函数 | `mock_state_coordinator` | 964 | `()` |
| 函数 | `mock_configurable_coordinator` | 973 | `()` |
| 函数 | `patch_config_from_runnable_config_coordinator` | 980 | `(mock_configurable_coordinator)` |
| 函数 | `patch_apply_prompt_template_coordinator` | 989 | `()` |
| 函数 | `patch_handoff_to_planner` | 998 | `()` |
| 函数 | `patch_logger` | 1004 | `()` |
| 函数 | `make_mock_llm_response` | 1009 | `(tool_calls=None)` |
| 函数 | `test_coordinator_node_no_tool_calls` | 1015 | `(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_templa...` |
| 函数 | `test_coordinator_node_with_tool_calls_planner` | 1040 | `(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_templa...` |
| 函数 | `test_coordinator_node_with_tool_calls_background_investigator` | 1064 | `(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_templa...` |
| 函数 | `test_coordinator_node_with_tool_calls_locale_override` | 1090 | `(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_templa...` |
| 函数 | `test_coordinator_node_tool_calls_exception_handling` | 1121 | `(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_templa...` |
| 函数 | `mock_state_reporter` | 1155 | `()` |
| 函数 | `mock_state_reporter_with_observations` | 1166 | `()` |
| 函数 | `mock_configurable_reporter` | 1176 | `()` |
| 函数 | `patch_config_from_runnable_config_reporter` | 1182 | `(mock_configurable_reporter)` |
| 函数 | `patch_apply_prompt_template_reporter` | 1191 | `()` |
| 函数 | `patch_human_message` | 1200 | `()` |
| 函数 | `patch_logger_reporter` | 1207 | `()` |
| 函数 | `make_mock_llm_response_reporter` | 1212 | `(content)` |
| 函数 | `test_reporter_node_basic` | 1218 | `(mock_state_reporter, patch_config_from_runnable_config_reporter, patch_apply_prompt_template_rep...` |
| 函数 | `test_reporter_node_with_observations` | 1246 | `(mock_state_reporter_with_observations, patch_config_from_runnable_config_reporter, patch_apply_p...` |
| 函数 | `test_reporter_node_locale_default` | 1273 | `(patch_config_from_runnable_config_reporter, patch_apply_prompt_template_reporter, patch_human_me...` |
| 类 | `Step` | 1303 | `` |
| 函数 | `mock_step` | 1311 | `()` |
| 函数 | `mock_completed_step` | 1316 | `()` |
| 函数 | `mock_state_with_steps` | 1321 | `(mock_step, mock_completed_step)` |
| 函数 | `mock_state_no_unexecuted` | 1334 | `()` |
| 函数 | `mock_agent` | 1350 | `()` |
| 异步函数 | `test_execute_agent_step_basic` | 1367 | `(mock_state_with_steps, mock_agent)` |
| 异步函数 | `test_execute_agent_step_no_unexecuted_step` | 1390 | `(mock_state_no_unexecuted, mock_agent)` |
| 异步函数 | `test_execute_agent_step_with_resources_and_researcher` | 1406 | `(mock_step)` |
| 异步函数 | `test_execute_agent_step_recursion_limit_env` | 1444 | `(monkeypatch, mock_state_with_steps, mock_agent)` |
| 异步函数 | `test_execute_agent_step_recursion_limit_env_invalid` | 1464 | `(monkeypatch, mock_state_with_steps, mock_agent)` |
| 异步函数 | `test_execute_agent_step_recursion_limit_env_negative` | 1486 | `(monkeypatch, mock_state_with_steps, mock_agent)` |
| 函数 | `mock_configurable_with_mcp` | 1508 | `()` |
| 函数 | `mock_configurable_without_mcp` | 1528 | `()` |
| 函数 | `patch_config_from_runnable_config_with_mcp` | 1535 | `(mock_configurable_with_mcp)` |
| 函数 | `patch_config_from_runnable_config_without_mcp` | 1544 | `(mock_configurable_without_mcp)` |
| 函数 | `patch_create_agent` | 1553 | `()` |
| 函数 | `patch_execute_agent_step` | 1559 | `()` |
| 函数 | `patch_multiserver_mcp_client` | 1570 | `()` |
| 异步函数 | `test_setup_and_execute_agent_step_with_mcp` | 1598 | `(mock_state_with_steps, mock_config, patch_config_from_runnable_config_with_mcp, patch_create_age...` |
| 异步函数 | `test_setup_and_execute_agent_step_without_mcp` | 1628 | `(mock_state_with_steps, mock_config, patch_config_from_runnable_config_without_mcp, patch_create_...` |
| 异步函数 | `test_setup_and_execute_agent_step_with_mcp_no_enabled_tools` | 1653 | `(mock_state_with_steps, mock_config, patch_create_agent, patch_execute_agent_step)` |
| 异步函数 | `test_setup_and_execute_agent_step_with_mcp_tools_description_update` | 1694 | `(mock_state_with_steps, mock_config, patch_config_from_runnable_config_with_mcp, patch_create_age...` |
| 函数 | `mock_state_with_resources` | 1740 | `()` |
| 函数 | `mock_state_without_resources` | 1745 | `()` |
| 函数 | `patch_get_web_search_tool` | 1750 | `()` |
| 函数 | `patch_crawl_tool` | 1758 | `()` |
| 函数 | `patch_get_retriever_tool` | 1764 | `()` |
| 函数 | `patch_setup_and_execute_agent_step` | 1770 | `()` |
| 异步函数 | `test_researcher_node_with_retriever_tool` | 1782 | `(mock_state_with_resources, mock_config, patch_config_from_runnable_config, patch_get_web_search_...` |
| 异步函数 | `test_researcher_node_without_retriever_tool` | 1810 | `(mock_state_with_resources, mock_config, patch_config_from_runnable_config, patch_get_web_search_...` |
| 异步函数 | `test_researcher_node_without_resources` | 1835 | `(mock_state_without_resources, mock_config, patch_config_from_runnable_config, patch_get_web_sear...` |
| 异步函数 | `test_clarification_workflow_integration` | 1862 | `()` |
| 函数 | `test_clarification_parameters_combinations` | 1875 | `()` |
| 函数 | `test_handoff_tools` | 1902 | `()` |
| 函数 | `test_coordinator_tools_with_clarification_enabled` | 1920 | `(mock_get_llm)` |
| 函数 | `test_coordinator_tools_with_clarification_disabled` | 1964 | `(mock_get_llm)` |
| 函数 | `test_coordinator_empty_llm_response_corner_case` | 2005 | `(mock_get_llm)` |
| 函数 | `test_clarification_handoff_combines_history` | 2049 | `()` |
| 函数 | `test_clarification_history_reconstructed_from_messages` | 2111 | `()` |
| 函数 | `test_clarification_max_rounds_without_tool_call` | 2170 | `()` |
| 函数 | `test_clarification_human_message_support` | 2224 | `()` |
| 函数 | `test_clarification_no_history_defaults_to_topic` | 2287 | `()` |
| 函数 | `test_planner_node_issue_650_missing_step_type_basic` | 2334 | `()` |
| 函数 | `test_planner_node_issue_650_water_footprint_scenario` | 2371 | `()` |
| 函数 | `test_planner_node_issue_650_validation_error_fixed` | 2416 | `()` |
| 函数 | `test_human_feedback_node_issue_650_plan_parsing` | 2448 | `()` |
| 函数 | `test_plan_validation_with_all_issue_650_error_scenarios` | 2488 | `()` |
| 函数 | `test_clarification_skips_specific_topics` | 2540 | `()` |
| 异步函数 | `test_execute_agent_step_preserves_multiple_tool_messages` | 2598 | `()` |
| 异步函数 | `test_execute_agent_step_single_tool_call_still_works` | 2756 | `()` |
| 异步函数 | `test_execute_agent_step_no_tool_calls_still_works` | 2852 | `()` |
| 类 | `TestReporterNodeThinkTagStripping` | 2919 | `` |

## 符号详解

### `TestExtractPlanContent`

- **类型**：类  |  **行号**：21–346  |  **完整限定名**：`tests.integration.test_nodes.TestExtractPlanContent`
- **定义**：

```python
class TestExtractPlanContent:
```
- **成员概览**：

  - `def test_extract_plan_content_with_string`
  - `def test_extract_plan_content_with_ai_message`
  - `def test_extract_plan_content_with_dict`
  - `def test_extract_plan_content_with_other_type`
  - `def test_extract_plan_content_with_complex_dict`
  - `def test_extract_plan_content_with_non_string_content`
  - `def test_extract_plan_content_with_empty_string`
  - `def test_extract_plan_content_with_empty_dict`
  - `def test_extract_plan_content_with_content_dict`
  - `def test_extract_plan_content_with_content_string`
  - `def test_extract_plan_content_issue_703_case`
  - `def test_extract_plan_content_with_multimodal_list_issue_845`
  - `def test_extract_plan_content_with_multimodal_list_mixed_content`
  - `def test_extract_plan_content_with_multimodal_content_blocks`
  - `def test_extract_plan_content_with_generic_content_dict_format`
  - `def test_extract_plan_content_with_empty_multimodal_list`
  - `def test_extract_plan_content_multimodal_uses_first_text_only`
  - `def test_extract_plan_content_multimodal_full_flow_issue_845`

**摘要**：

Test cases for the extract_plan_content function.

### `MOCK_SEARCH_RESULTS`

- **类型**：模块常量  |  **行号**：359–362  |  **完整限定名**：`tests.integration.test_nodes.MOCK_SEARCH_RESULTS`
- **值**：

```python
MOCK_SEARCH_RESULTS = [{'title': 'Test Title 1', 'content': 'Test Content 1'}, {'title': 'Test Title 2', 'content': 'Test Content 2'}]
```

**说明**（自动推断）：

模块级常量 `MOCK_SEARCH_RESULTS`，在导入时初始化，供本模块及相关流程引用。

### `mock_state`

- **类型**：函数  |  **行号**：366–371  |  **完整限定名**：`tests.integration.test_nodes.mock_state`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_configurable`

- **类型**：函数  |  **行号**：375–378  |  **完整限定名**：`tests.integration.test_nodes.mock_configurable`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_configurable():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_configurable`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_config`

- **类型**：函数  |  **行号**：382–384  |  **完整限定名**：`tests.integration.test_nodes.mock_config`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_config():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_config`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `patch_config_from_runnable_config`

- **类型**：函数  |  **行号**：388–393  |  **完整限定名**：`tests.integration.test_nodes.patch_config_from_runnable_config`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_config_from_runnable_config(mock_configurable):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_config_from_runnable_config`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `mock_tavily_search`

- **类型**：函数  |  **行号**：397–404  |  **完整限定名**：`tests.integration.test_nodes.mock_tavily_search`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_tavily_search():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_tavily_search`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_web_search_tool`

- **类型**：函数  |  **行号**：408–415  |  **完整限定名**：`tests.integration.test_nodes.mock_web_search_tool`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_web_search_tool():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_web_search_tool`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `test_background_investigation_node_tavily`

- **类型**：函数  |  **行号**：419–450  |  **完整限定名**：`tests.integration.test_nodes.test_background_investigation_node_tavily`
- **装饰器**：`@pytest.mark.parametrize`
- **签名**：

```python
def test_background_investigation_node_tavily(mock_state, mock_tavily_search, mock_web_search_tool, search_engine, patch_config_from_runnable_config, mock_config):
```

**摘要**：

Test background_investigation_node with Tavily search engine

### `test_background_investigation_node_malformed_response`

- **类型**：函数  |  **行号**：453–471  |  **完整限定名**：`tests.integration.test_nodes.test_background_investigation_node_malformed_response`
- **签名**：

```python
def test_background_investigation_node_malformed_response(mock_state, mock_tavily_search, patch_config_from_runnable_config, mock_config):
```

**摘要**：

Test background_investigation_node with malformed Tavily response

### `mock_plan`

- **类型**：函数  |  **行号**：475–482  |  **完整限定名**：`tests.integration.test_nodes.mock_plan`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_plan():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_plan`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_state_planner`

- **类型**：函数  |  **行号**：486–492  |  **完整限定名**：`tests.integration.test_nodes.mock_state_planner`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_planner():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_planner`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_configurable_planner`

- **类型**：函数  |  **行号**：496–500  |  **完整限定名**：`tests.integration.test_nodes.mock_configurable_planner`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_configurable_planner():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_configurable_planner`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `patch_config_from_runnable_config_planner`

- **类型**：函数  |  **行号**：504–509  |  **完整限定名**：`tests.integration.test_nodes.patch_config_from_runnable_config_planner`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_config_from_runnable_config_planner(mock_configurable_planner):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_config_from_runnable_config_planner`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_apply_prompt_template`

- **类型**：函数  |  **行号**：513–518  |  **完整限定名**：`tests.integration.test_nodes.patch_apply_prompt_template`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_apply_prompt_template():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_apply_prompt_template`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_repair_json_output`

- **类型**：函数  |  **行号**：522–524  |  **完整限定名**：`tests.integration.test_nodes.patch_repair_json_output`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_repair_json_output():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_repair_json_output`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_plan_model_validate`

- **类型**：函数  |  **行号**：528–530  |  **完整限定名**：`tests.integration.test_nodes.patch_plan_model_validate`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_plan_model_validate():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_plan_model_validate`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_ai_message`

- **类型**：函数  |  **行号**：534–540  |  **完整限定名**：`tests.integration.test_nodes.patch_ai_message`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_ai_message():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_ai_message`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `test_planner_node_basic_has_enough_context`

- **类型**：函数  |  **行号**：543–569  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_basic_has_enough_context`
- **签名**：

```python
def test_planner_node_basic_has_enough_context(mock_state_planner, patch_config_from_runnable_config_planner, patch_apply_prompt_template, patch_repair_json_output, patch_plan_model_validate, patch_ai_message, mock_plan):
```

**说明**（自动推断）：

测试用例函数 `test_planner_node_basic_has_enough_context`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_planner_node_basic_not_enough_context`

- **类型**：函数  |  **行号**：572–604  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_basic_not_enough_context`
- **签名**：

```python
def test_planner_node_basic_not_enough_context(mock_state_planner, patch_config_from_runnable_config_planner, patch_apply_prompt_template, patch_repair_json_output, patch_plan_model_validate, patch_ai_message):
```

**说明**（自动推断）：

测试用例函数 `test_planner_node_basic_not_enough_context`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_planner_node_stream_mode_has_enough_context`

- **类型**：函数  |  **行号**：607–632  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_stream_mode_has_enough_context`
- **签名**：

```python
def test_planner_node_stream_mode_has_enough_context(mock_state_planner, patch_config_from_runnable_config_planner, patch_apply_prompt_template, patch_repair_json_output, patch_plan_model_validate, patch_ai_message, mock_plan):
```

**说明**（自动推断）：

测试用例函数 `test_planner_node_stream_mode_has_enough_context`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_planner_node_stream_mode_not_enough_context`

- **类型**：函数  |  **行号**：635–665  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_stream_mode_not_enough_context`
- **签名**：

```python
def test_planner_node_stream_mode_not_enough_context(mock_state_planner, patch_config_from_runnable_config_planner, patch_apply_prompt_template, patch_repair_json_output, patch_plan_model_validate, patch_ai_message):
```

**说明**（自动推断）：

测试用例函数 `test_planner_node_stream_mode_not_enough_context`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_planner_node_plan_iterations_exceeded`

- **类型**：函数  |  **行号**：668–678  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_plan_iterations_exceeded`
- **签名**：

```python
def test_planner_node_plan_iterations_exceeded(mock_state_planner):
```

**说明**（自动推断）：

测试用例函数 `test_planner_node_plan_iterations_exceeded`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_planner_node_json_decode_error_first_iteration`

- **类型**：函数  |  **行号**：681–700  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_json_decode_error_first_iteration`
- **签名**：

```python
def test_planner_node_json_decode_error_first_iteration(mock_state_planner):
```

**说明**（自动推断）：

测试用例函数 `test_planner_node_json_decode_error_first_iteration`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_planner_node_json_decode_error_second_iteration`

- **类型**：函数  |  **行号**：703–724  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_json_decode_error_second_iteration`
- **签名**：

```python
def test_planner_node_json_decode_error_second_iteration(mock_state_planner):
```

**说明**（自动推断）：

测试用例函数 `test_planner_node_json_decode_error_second_iteration`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `patch_plan_and_repair`

- **类型**：函数  |  **行号**：729–732  |  **完整限定名**：`tests.integration.test_nodes.patch_plan_and_repair`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_plan_and_repair(monkeypatch):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_plan_and_repair`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `mock_state_base`

- **类型**：函数  |  **行号**：736–748  |  **完整限定名**：`tests.integration.test_nodes.mock_state_base`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_base():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_base`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `test_human_feedback_node_auto_accepted`

- **类型**：函数  |  **行号**：751–759  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_auto_accepted`
- **签名**：

```python
def test_human_feedback_node_auto_accepted(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_auto_accepted`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_edit_plan`

- **类型**：函数  |  **行号**：762–771  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_edit_plan`
- **签名**：

```python
def test_human_feedback_node_edit_plan(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_edit_plan`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_accepted`

- **类型**：函数  |  **行号**：774–783  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_accepted`
- **签名**：

```python
def test_human_feedback_node_accepted(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_accepted`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_invalid_interrupt`

- **类型**：函数  |  **行号**：786–795  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_invalid_interrupt`
- **签名**：

```python
def test_human_feedback_node_invalid_interrupt(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_invalid_interrupt`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_none_feedback`

- **类型**：函数  |  **行号**：798–807  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_none_feedback`
- **签名**：

```python
def test_human_feedback_node_none_feedback(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_none_feedback`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_empty_feedback`

- **类型**：函数  |  **行号**：810–819  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_empty_feedback`
- **签名**：

```python
def test_human_feedback_node_empty_feedback(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_empty_feedback`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_json_decode_error_first_iteration`

- **类型**：函数  |  **行号**：822–844  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_json_decode_error_first_iteration`
- **签名**：

```python
def test_human_feedback_node_json_decode_error_first_iteration(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_json_decode_error_first_iteration`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_model_validate_error`

- **类型**：函数  |  **行号**：846–881  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_model_validate_error`
- **签名**：

```python
def test_human_feedback_node_model_validate_error(mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_model_validate_error`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_list_plan_runs_enforcement_after_normalization`

- **类型**：函数  |  **行号**：883–924  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_list_plan_runs_enforcement_after_normalization`
- **签名**：

```python
def test_human_feedback_node_list_plan_runs_enforcement_after_normalization(mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_list_plan_runs_enforcement_after_normalization`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_json_decode_error_second_iteration`

- **类型**：函数  |  **行号**：927–939  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_json_decode_error_second_iteration`
- **签名**：

```python
def test_human_feedback_node_json_decode_error_second_iteration(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_json_decode_error_second_iteration`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_human_feedback_node_not_enough_context`

- **类型**：函数  |  **行号**：942–960  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_not_enough_context`
- **签名**：

```python
def test_human_feedback_node_not_enough_context(monkeypatch, mock_state_base, mock_config):
```

**说明**（自动推断）：

测试用例函数 `test_human_feedback_node_not_enough_context`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `mock_state_coordinator`

- **类型**：函数  |  **行号**：964–969  |  **完整限定名**：`tests.integration.test_nodes.mock_state_coordinator`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_coordinator():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_coordinator`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_configurable_coordinator`

- **类型**：函数  |  **行号**：973–976  |  **完整限定名**：`tests.integration.test_nodes.mock_configurable_coordinator`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_configurable_coordinator():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_configurable_coordinator`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `patch_config_from_runnable_config_coordinator`

- **类型**：函数  |  **行号**：980–985  |  **完整限定名**：`tests.integration.test_nodes.patch_config_from_runnable_config_coordinator`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_config_from_runnable_config_coordinator(mock_configurable_coordinator):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_config_from_runnable_config_coordinator`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_apply_prompt_template_coordinator`

- **类型**：函数  |  **行号**：989–994  |  **完整限定名**：`tests.integration.test_nodes.patch_apply_prompt_template_coordinator`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_apply_prompt_template_coordinator():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_apply_prompt_template_coordinator`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_handoff_to_planner`

- **类型**：函数  |  **行号**：998–1000  |  **完整限定名**：`tests.integration.test_nodes.patch_handoff_to_planner`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_handoff_to_planner():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_handoff_to_planner`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_logger`

- **类型**：函数  |  **行号**：1004–1006  |  **完整限定名**：`tests.integration.test_nodes.patch_logger`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_logger():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_logger`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `make_mock_llm_response`

- **类型**：函数  |  **行号**：1009–1012  |  **完整限定名**：`tests.integration.test_nodes.make_mock_llm_response`
- **签名**：

```python
def make_mock_llm_response(tool_calls=None):
```

**说明**（自动推断）：

测试用 mock 对象 `make_mock_llm_response`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `test_coordinator_node_no_tool_calls`

- **类型**：函数  |  **行号**：1015–1037  |  **完整限定名**：`tests.integration.test_nodes.test_coordinator_node_no_tool_calls`
- **签名**：

```python
def test_coordinator_node_no_tool_calls(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_template_coordinator, patch_handoff_to_planner, patch_logger):
```

**说明**（自动推断）：

测试用例函数 `test_coordinator_node_no_tool_calls`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_coordinator_node_with_tool_calls_planner`

- **类型**：函数  |  **行号**：1040–1061  |  **完整限定名**：`tests.integration.test_nodes.test_coordinator_node_with_tool_calls_planner`
- **签名**：

```python
def test_coordinator_node_with_tool_calls_planner(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_template_coordinator, patch_handoff_to_planner, patch_logger):
```

**说明**（自动推断）：

测试用例函数 `test_coordinator_node_with_tool_calls_planner`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_coordinator_node_with_tool_calls_background_investigator`

- **类型**：函数  |  **行号**：1064–1087  |  **完整限定名**：`tests.integration.test_nodes.test_coordinator_node_with_tool_calls_background_investigator`
- **签名**：

```python
def test_coordinator_node_with_tool_calls_background_investigator(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_template_coordinator, patch_handoff_to_planner, patch_logger):
```

**说明**（自动推断）：

测试用例函数 `test_coordinator_node_with_tool_calls_background_investigator`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_coordinator_node_with_tool_calls_locale_override`

- **类型**：函数  |  **行号**：1090–1118  |  **完整限定名**：`tests.integration.test_nodes.test_coordinator_node_with_tool_calls_locale_override`
- **签名**：

```python
def test_coordinator_node_with_tool_calls_locale_override(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_template_coordinator, patch_handoff_to_planner, patch_logger):
```

**说明**（自动推断）：

测试用例函数 `test_coordinator_node_with_tool_calls_locale_override`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_coordinator_node_tool_calls_exception_handling`

- **类型**：函数  |  **行号**：1121–1151  |  **完整限定名**：`tests.integration.test_nodes.test_coordinator_node_tool_calls_exception_handling`
- **签名**：

```python
def test_coordinator_node_tool_calls_exception_handling(mock_state_coordinator, patch_config_from_runnable_config_coordinator, patch_apply_prompt_template_coordinator, patch_handoff_to_planner, patch_logger):
```

**说明**（自动推断）：

测试用例函数 `test_coordinator_node_tool_calls_exception_handling`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `mock_state_reporter`

- **类型**：函数  |  **行号**：1155–1162  |  **完整限定名**：`tests.integration.test_nodes.mock_state_reporter`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_reporter():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_reporter`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_state_reporter_with_observations`

- **类型**：函数  |  **行号**：1166–1172  |  **完整限定名**：`tests.integration.test_nodes.mock_state_reporter_with_observations`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_reporter_with_observations():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_reporter_with_observations`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_configurable_reporter`

- **类型**：函数  |  **行号**：1176–1178  |  **完整限定名**：`tests.integration.test_nodes.mock_configurable_reporter`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_configurable_reporter():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_configurable_reporter`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `patch_config_from_runnable_config_reporter`

- **类型**：函数  |  **行号**：1182–1187  |  **完整限定名**：`tests.integration.test_nodes.patch_config_from_runnable_config_reporter`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_config_from_runnable_config_reporter(mock_configurable_reporter):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_config_from_runnable_config_reporter`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_apply_prompt_template_reporter`

- **类型**：函数  |  **行号**：1191–1196  |  **完整限定名**：`tests.integration.test_nodes.patch_apply_prompt_template_reporter`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_apply_prompt_template_reporter():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_apply_prompt_template_reporter`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_human_message`

- **类型**：函数  |  **行号**：1200–1203  |  **完整限定名**：`tests.integration.test_nodes.patch_human_message`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_human_message():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_human_message`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_logger_reporter`

- **类型**：函数  |  **行号**：1207–1209  |  **完整限定名**：`tests.integration.test_nodes.patch_logger_reporter`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_logger_reporter():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_logger_reporter`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `make_mock_llm_response_reporter`

- **类型**：函数  |  **行号**：1212–1215  |  **完整限定名**：`tests.integration.test_nodes.make_mock_llm_response_reporter`
- **签名**：

```python
def make_mock_llm_response_reporter(content):
```

**说明**（自动推断）：

测试用 mock 对象 `make_mock_llm_response_reporter`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `test_reporter_node_basic`

- **类型**：函数  |  **行号**：1218–1243  |  **完整限定名**：`tests.integration.test_nodes.test_reporter_node_basic`
- **签名**：

```python
def test_reporter_node_basic(mock_state_reporter, patch_config_from_runnable_config_reporter, patch_apply_prompt_template_reporter, patch_human_message, patch_logger_reporter):
```

**说明**（自动推断）：

测试用例函数 `test_reporter_node_basic`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_reporter_node_with_observations`

- **类型**：函数  |  **行号**：1246–1270  |  **完整限定名**：`tests.integration.test_nodes.test_reporter_node_with_observations`
- **签名**：

```python
def test_reporter_node_with_observations(mock_state_reporter_with_observations, patch_config_from_runnable_config_reporter, patch_apply_prompt_template_reporter, patch_human_message, patch_logger_reporter):
```

**说明**（自动推断）：

测试用例函数 `test_reporter_node_with_observations`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_reporter_node_locale_default`

- **类型**：函数  |  **行号**：1273–1299  |  **完整限定名**：`tests.integration.test_nodes.test_reporter_node_locale_default`
- **签名**：

```python
def test_reporter_node_locale_default(patch_config_from_runnable_config_reporter, patch_apply_prompt_template_reporter, patch_human_message, patch_logger_reporter):
```

**说明**（自动推断）：

测试用例函数 `test_reporter_node_locale_default`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `Step`

- **类型**：类  |  **行号**：1303–1307  |  **完整限定名**：`tests.integration.test_nodes.Step`
- **定义**：

```python
class Step:
```
- **成员概览**：

  - `def __init__`

**说明**（自动推断）：

测试中导入的数据模型 `Step`（来自 src），用于构造测试用例的输入状态。

### `mock_step`

- **类型**：函数  |  **行号**：1311–1312  |  **完整限定名**：`tests.integration.test_nodes.mock_step`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_step():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_step`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_completed_step`

- **类型**：函数  |  **行号**：1316–1317  |  **完整限定名**：`tests.integration.test_nodes.mock_completed_step`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_completed_step():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_completed_step`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_state_with_steps`

- **类型**：函数  |  **行号**：1321–1330  |  **完整限定名**：`tests.integration.test_nodes.mock_state_with_steps`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_with_steps(mock_step, mock_completed_step):
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_with_steps`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_state_no_unexecuted`

- **类型**：函数  |  **行号**：1334–1346  |  **完整限定名**：`tests.integration.test_nodes.mock_state_no_unexecuted`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_no_unexecuted():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_no_unexecuted`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_agent`

- **类型**：函数  |  **行号**：1350–1363  |  **完整限定名**：`tests.integration.test_nodes.mock_agent`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_agent():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_agent`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `test_execute_agent_step_basic`

- **类型**：异步函数  |  **行号**：1367–1386  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_basic`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_basic(mock_state_with_steps, mock_agent):
```

**说明**（自动推断）：

测试用例函数 `test_execute_agent_step_basic`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_execute_agent_step_no_unexecuted_step`

- **类型**：异步函数  |  **行号**：1390–1402  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_no_unexecuted_step`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_no_unexecuted_step(mock_state_no_unexecuted, mock_agent):
```

**说明**（自动推断）：

测试用例函数 `test_execute_agent_step_no_unexecuted_step`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_execute_agent_step_with_resources_and_researcher`

- **类型**：异步函数  |  **行号**：1406–1440  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_with_resources_and_researcher`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_with_resources_and_researcher(mock_step):
```

**说明**（自动推断）：

测试用例函数 `test_execute_agent_step_with_resources_and_researcher`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_execute_agent_step_recursion_limit_env`

- **类型**：异步函数  |  **行号**：1444–1460  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_recursion_limit_env`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_recursion_limit_env(monkeypatch, mock_state_with_steps, mock_agent):
```

**说明**（自动推断）：

测试用例函数 `test_execute_agent_step_recursion_limit_env`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_execute_agent_step_recursion_limit_env_invalid`

- **类型**：异步函数  |  **行号**：1464–1482  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_recursion_limit_env_invalid`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_recursion_limit_env_invalid(monkeypatch, mock_state_with_steps, mock_agent):
```

**说明**（自动推断）：

测试用例函数 `test_execute_agent_step_recursion_limit_env_invalid`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_execute_agent_step_recursion_limit_env_negative`

- **类型**：异步函数  |  **行号**：1486–1504  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_recursion_limit_env_negative`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_recursion_limit_env_negative(monkeypatch, mock_state_with_steps, mock_agent):
```

**说明**（自动推断）：

测试用例函数 `test_execute_agent_step_recursion_limit_env_negative`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `mock_configurable_with_mcp`

- **类型**：函数  |  **行号**：1508–1524  |  **完整限定名**：`tests.integration.test_nodes.mock_configurable_with_mcp`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_configurable_with_mcp():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_configurable_with_mcp`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_configurable_without_mcp`

- **类型**：函数  |  **行号**：1528–1531  |  **完整限定名**：`tests.integration.test_nodes.mock_configurable_without_mcp`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_configurable_without_mcp():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_configurable_without_mcp`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `patch_config_from_runnable_config_with_mcp`

- **类型**：函数  |  **行号**：1535–1540  |  **完整限定名**：`tests.integration.test_nodes.patch_config_from_runnable_config_with_mcp`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_config_from_runnable_config_with_mcp(mock_configurable_with_mcp):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_config_from_runnable_config_with_mcp`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_config_from_runnable_config_without_mcp`

- **类型**：函数  |  **行号**：1544–1549  |  **完整限定名**：`tests.integration.test_nodes.patch_config_from_runnable_config_without_mcp`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_config_from_runnable_config_without_mcp(mock_configurable_without_mcp):
```

**说明**（自动推断）：

测试 fixture 函数 `patch_config_from_runnable_config_without_mcp`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_create_agent`

- **类型**：函数  |  **行号**：1553–1555  |  **完整限定名**：`tests.integration.test_nodes.patch_create_agent`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_create_agent():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_create_agent`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_execute_agent_step`

- **类型**：函数  |  **行号**：1559–1566  |  **完整限定名**：`tests.integration.test_nodes.patch_execute_agent_step`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_execute_agent_step():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_execute_agent_step`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_multiserver_mcp_client`

- **类型**：函数  |  **行号**：1570–1594  |  **完整限定名**：`tests.integration.test_nodes.patch_multiserver_mcp_client`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_multiserver_mcp_client():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_multiserver_mcp_client`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `test_setup_and_execute_agent_step_with_mcp`

- **类型**：异步函数  |  **行号**：1598–1624  |  **完整限定名**：`tests.integration.test_nodes.test_setup_and_execute_agent_step_with_mcp`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_setup_and_execute_agent_step_with_mcp(mock_state_with_steps, mock_config, patch_config_from_runnable_config_with_mcp, patch_create_agent, patch_execute_agent_step, patch_multiserver_mcp_client):
```

**说明**（自动推断）：

测试用例函数 `test_setup_and_execute_agent_step_with_mcp`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_setup_and_execute_agent_step_without_mcp`

- **类型**：异步函数  |  **行号**：1628–1649  |  **完整限定名**：`tests.integration.test_nodes.test_setup_and_execute_agent_step_without_mcp`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_setup_and_execute_agent_step_without_mcp(mock_state_with_steps, mock_config, patch_config_from_runnable_config_without_mcp, patch_create_agent, patch_execute_agent_step):
```

**说明**（自动推断）：

测试用例函数 `test_setup_and_execute_agent_step_without_mcp`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_setup_and_execute_agent_step_with_mcp_no_enabled_tools`

- **类型**：异步函数  |  **行号**：1653–1690  |  **完整限定名**：`tests.integration.test_nodes.test_setup_and_execute_agent_step_with_mcp_no_enabled_tools`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_setup_and_execute_agent_step_with_mcp_no_enabled_tools(mock_state_with_steps, mock_config, patch_create_agent, patch_execute_agent_step):
```

**说明**（自动推断）：

测试用例函数 `test_setup_and_execute_agent_step_with_mcp_no_enabled_tools`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_setup_and_execute_agent_step_with_mcp_tools_description_update`

- **类型**：异步函数  |  **行号**：1694–1736  |  **完整限定名**：`tests.integration.test_nodes.test_setup_and_execute_agent_step_with_mcp_tools_description_update`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_setup_and_execute_agent_step_with_mcp_tools_description_update(mock_state_with_steps, mock_config, patch_config_from_runnable_config_with_mcp, patch_create_agent, patch_execute_agent_step):
```

**说明**（自动推断）：

测试用例函数 `test_setup_and_execute_agent_step_with_mcp_tools_description_update`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `mock_state_with_resources`

- **类型**：函数  |  **行号**：1740–1741  |  **完整限定名**：`tests.integration.test_nodes.mock_state_with_resources`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_with_resources():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_with_resources`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_state_without_resources`

- **类型**：函数  |  **行号**：1745–1746  |  **完整限定名**：`tests.integration.test_nodes.mock_state_without_resources`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def mock_state_without_resources():
```

**说明**（自动推断）：

测试用 mock 对象 `mock_state_without_resources`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `patch_get_web_search_tool`

- **类型**：函数  |  **行号**：1750–1754  |  **完整限定名**：`tests.integration.test_nodes.patch_get_web_search_tool`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_get_web_search_tool():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_get_web_search_tool`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_crawl_tool`

- **类型**：函数  |  **行号**：1758–1760  |  **完整限定名**：`tests.integration.test_nodes.patch_crawl_tool`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_crawl_tool():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_crawl_tool`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_get_retriever_tool`

- **类型**：函数  |  **行号**：1764–1766  |  **完整限定名**：`tests.integration.test_nodes.patch_get_retriever_tool`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_get_retriever_tool():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_get_retriever_tool`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `patch_setup_and_execute_agent_step`

- **类型**：函数  |  **行号**：1770–1778  |  **完整限定名**：`tests.integration.test_nodes.patch_setup_and_execute_agent_step`
- **装饰器**：`@pytest.fixture`
- **签名**：

```python
def patch_setup_and_execute_agent_step():
```

**说明**（自动推断）：

测试 fixture 函数 `patch_setup_and_execute_agent_step`，通过 monkeypatch 替换目标对象以隔离被测单元。

### `test_researcher_node_with_retriever_tool`

- **类型**：异步函数  |  **行号**：1782–1806  |  **完整限定名**：`tests.integration.test_nodes.test_researcher_node_with_retriever_tool`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_researcher_node_with_retriever_tool(mock_state_with_resources, mock_config, patch_config_from_runnable_config, patch_get_web_search_tool, patch_crawl_tool, patch_get_retriever_tool, patch_setup_and_execute_agent_step):
```

**说明**（自动推断）：

测试用例函数 `test_researcher_node_with_retriever_tool`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_researcher_node_without_retriever_tool`

- **类型**：异步函数  |  **行号**：1810–1831  |  **完整限定名**：`tests.integration.test_nodes.test_researcher_node_without_retriever_tool`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_researcher_node_without_retriever_tool(mock_state_with_resources, mock_config, patch_config_from_runnable_config, patch_get_web_search_tool, patch_crawl_tool, patch_get_retriever_tool, patch_setup_and_execute_agent_step):
```

**说明**（自动推断）：

测试用例函数 `test_researcher_node_without_retriever_tool`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_researcher_node_without_resources`

- **类型**：异步函数  |  **行号**：1835–1853  |  **完整限定名**：`tests.integration.test_nodes.test_researcher_node_without_resources`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_researcher_node_without_resources(mock_state_without_resources, mock_config, patch_config_from_runnable_config, patch_get_web_search_tool, patch_crawl_tool, patch_get_retriever_tool, patch_setup_and_execute_agent_step):
```

**说明**（自动推断）：

测试用例函数 `test_researcher_node_without_resources`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_clarification_workflow_integration`

- **类型**：异步函数  |  **行号**：1862–1872  |  **完整限定名**：`tests.integration.test_nodes.test_clarification_workflow_integration`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_clarification_workflow_integration():
```

**摘要**：

Test the complete clarification workflow integration.

### `test_clarification_parameters_combinations`

- **类型**：函数  |  **行号**：1875–1899  |  **完整限定名**：`tests.integration.test_nodes.test_clarification_parameters_combinations`
- **签名**：

```python
def test_clarification_parameters_combinations():
```

**摘要**：

Test various combinations of clarification parameters.

### `test_handoff_tools`

- **类型**：函数  |  **行号**：1902–1916  |  **完整限定名**：`tests.integration.test_nodes.test_handoff_tools`
- **签名**：

```python
def test_handoff_tools():
```

**摘要**：

Test that handoff tools are properly defined.

### `test_coordinator_tools_with_clarification_enabled`

- **类型**：函数  |  **行号**：1920–1960  |  **完整限定名**：`tests.integration.test_nodes.test_coordinator_tools_with_clarification_enabled`
- **装饰器**：`@patch`
- **签名**：

```python
def test_coordinator_tools_with_clarification_enabled(mock_get_llm):
```

**摘要**：

Test that coordinator binds correct tools when clarification is enabled.

### `test_coordinator_tools_with_clarification_disabled`

- **类型**：函数  |  **行号**：1964–2001  |  **完整限定名**：`tests.integration.test_nodes.test_coordinator_tools_with_clarification_disabled`
- **装饰器**：`@patch`
- **签名**：

```python
def test_coordinator_tools_with_clarification_disabled(mock_get_llm):
```

**摘要**：

Test that coordinator binds two tools when clarification is disabled (fix for issue #733).

### `test_coordinator_empty_llm_response_corner_case`

- **类型**：函数  |  **行号**：2005–2041  |  **完整限定名**：`tests.integration.test_nodes.test_coordinator_empty_llm_response_corner_case`
- **装饰器**：`@patch`
- **签名**：

```python
def test_coordinator_empty_llm_response_corner_case(mock_get_llm):
```

**摘要**：

Corner case test: LLM returns empty response when clarification is enabled.

### `test_clarification_handoff_combines_history`

- **类型**：函数  |  **行号**：2049–2108  |  **完整限定名**：`tests.integration.test_nodes.test_clarification_handoff_combines_history`
- **签名**：

```python
def test_clarification_handoff_combines_history():
```

**摘要**：

Coordinator should merge original topic with all clarification answers before handoff.

### `test_clarification_history_reconstructed_from_messages`

- **类型**：函数  |  **行号**：2111–2167  |  **完整限定名**：`tests.integration.test_nodes.test_clarification_history_reconstructed_from_messages`
- **签名**：

```python
def test_clarification_history_reconstructed_from_messages():
```

**摘要**：

Coordinator should rebuild clarification history from full message log when state is incomplete.

### `test_clarification_max_rounds_without_tool_call`

- **类型**：函数  |  **行号**：2170–2221  |  **完整限定名**：`tests.integration.test_nodes.test_clarification_max_rounds_without_tool_call`
- **签名**：

```python
def test_clarification_max_rounds_without_tool_call():
```

**摘要**：

Coordinator should stop asking questions after max rounds and hand off with compiled topic.

### `test_clarification_human_message_support`

- **类型**：函数  |  **行号**：2224–2284  |  **完整限定名**：`tests.integration.test_nodes.test_clarification_human_message_support`
- **签名**：

```python
def test_clarification_human_message_support():
```

**摘要**：

Coordinator should treat HumanMessage instances from the user as user authored.

### `test_clarification_no_history_defaults_to_topic`

- **类型**：函数  |  **行号**：2287–2326  |  **完整限定名**：`tests.integration.test_nodes.test_clarification_no_history_defaults_to_topic`
- **签名**：

```python
def test_clarification_no_history_defaults_to_topic():
```

**摘要**：

If clarification never started, coordinator should forward the original topic.

### `test_planner_node_issue_650_missing_step_type_basic`

- **类型**：函数  |  **行号**：2334–2368  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_issue_650_missing_step_type_basic`
- **签名**：

```python
def test_planner_node_issue_650_missing_step_type_basic():
```

**摘要**：

Test planner_node with missing step_type fields (Issue #650).

### `test_planner_node_issue_650_water_footprint_scenario`

- **类型**：函数  |  **行号**：2371–2413  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_issue_650_water_footprint_scenario`
- **签名**：

```python
def test_planner_node_issue_650_water_footprint_scenario():
```

**摘要**：

Test the exact water footprint query scenario from Issue #650.

### `test_planner_node_issue_650_validation_error_fixed`

- **类型**：函数  |  **行号**：2416–2445  |  **完整限定名**：`tests.integration.test_nodes.test_planner_node_issue_650_validation_error_fixed`
- **签名**：

```python
def test_planner_node_issue_650_validation_error_fixed():
```

**摘要**：

Test that the validation error from Issue #650 is now prevented.

### `test_human_feedback_node_issue_650_plan_parsing`

- **类型**：函数  |  **行号**：2448–2485  |  **完整限定名**：`tests.integration.test_nodes.test_human_feedback_node_issue_650_plan_parsing`
- **签名**：

```python
def test_human_feedback_node_issue_650_plan_parsing():
```

**摘要**：

Test human_feedback_node with Issue #650 plan that has missing step_type.

### `test_plan_validation_with_all_issue_650_error_scenarios`

- **类型**：函数  |  **行号**：2488–2538  |  **完整限定名**：`tests.integration.test_nodes.test_plan_validation_with_all_issue_650_error_scenarios`
- **签名**：

```python
def test_plan_validation_with_all_issue_650_error_scenarios():
```

**摘要**：

Test all variations of Issue #650 error scenarios.

### `test_clarification_skips_specific_topics`

- **类型**：函数  |  **行号**：2540–2589  |  **完整限定名**：`tests.integration.test_nodes.test_clarification_skips_specific_topics`
- **签名**：

```python
def test_clarification_skips_specific_topics():
```

**摘要**：

Coordinator should skip clarification for already specific topics.

### `test_execute_agent_step_preserves_multiple_tool_messages`

- **类型**：异步函数  |  **行号**：2598–2752  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_preserves_multiple_tool_messages`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_preserves_multiple_tool_messages():
```

**摘要**：

Test for Issue #693: Verify that all ToolMessages from multiple tool calls
(e.g., multiple web_search calls) are preserved and not just the final result.

### `test_execute_agent_step_single_tool_call_still_works`

- **类型**：异步函数  |  **行号**：2756–2848  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_single_tool_call_still_works`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_single_tool_call_still_works():
```

**摘要**：

Test that the fix for Issue #693 doesn't break the case where
an agent makes only a single tool call.

### `test_execute_agent_step_no_tool_calls_still_works`

- **类型**：异步函数  |  **行号**：2852–2916  |  **完整限定名**：`tests.integration.test_nodes.test_execute_agent_step_no_tool_calls_still_works`
- **装饰器**：`@pytest.mark.asyncio`
- **签名**：

```python
async def test_execute_agent_step_no_tool_calls_still_works():
```

**摘要**：

Test that the fix for Issue #693 doesn't break the case where
an agent completes without making any tool calls.

### `TestReporterNodeThinkTagStripping`

- **类型**：类  |  **行号**：2919–3028  |  **完整限定名**：`tests.integration.test_nodes.TestReporterNodeThinkTagStripping`
- **定义**：

```python
class TestReporterNodeThinkTagStripping:
```
- **成员概览**：

  - `def _make_mock_state`
  - `def _run_reporter_node`
  - `def test_strips_think_tag_at_beginning`
  - `def test_strips_multiple_think_blocks`
  - `def test_preserves_content_without_think_tags`
  - `def test_empty_content_after_stripping`
  - `def test_non_string_content_passes_through`

**摘要**：

Tests for stripping <think> tags from reporter_node output (#781).

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.integration.test_nodes import mock_state
#
# TODO: 结合业务场景补充 mock_state 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `tests/unit/utils/test_json_utils.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/utils/test_json_utils.py`
- **模块导入名**：`tests.unit.utils.test_json_utils`
- **代码行数**：581
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.utils.json_utils import _extract_json_from_content, repair_json_output, sanitize_args, sanitize_tool_response`

**外部依赖**（第三方库 / 标准库）：

- `import json`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestRepairJsonOutput` | 14 | `` |
| 类 | `TestExtractJsonFromContent` | 159 | `` |
| 类 | `TestSanitizeToolResponse` | 223 | `` |
| 类 | `TestSanitizeArgs` | 275 | `` |
| 类 | `TestRepairJsonOutputEdgeCases` | 325 | `` |
| 类 | `TestExtractJsonFromContentEdgeCases` | 461 | `` |
| 类 | `TestSanitizeToolResponseEdgeCases` | 518 | `` |

## 符号详解

### `TestRepairJsonOutput`

- **类型**：类  |  **行号**：14–156  |  **完整限定名**：`tests.unit.utils.test_json_utils.TestRepairJsonOutput`
- **定义**：

```python
class TestRepairJsonOutput:
```
- **成员概览**：

  - `def test_valid_json_object`
  - `def test_valid_json_array`
  - `def test_json_with_code_block_json`
  - `def test_json_with_code_block_ts`
  - `def test_json_with_code_block_uppercase_json`
  - `def test_json_with_code_block_uppercase_ts`
  - `def test_json_with_code_block_mixed_case_json`
  - `def test_json_with_code_block_uppercase_ts_with_prefix`
  - `def test_json_with_code_block_uppercase_json_with_prefix`
  - `def test_json_with_plain_code_block_uppercase`
  - `def test_malformed_json_repair`
  - `def test_non_json_content`
  - `def test_empty_string`
  - `def test_whitespace_only`
  - `def test_json_with_unicode`
  - `def test_json_code_block_without_closing`
  - `def test_json_repair_broken_json`
  - `def test_nested_json_object`
  - `def test_json_array_with_objects`
  - `def test_content_with_json_in_middle`

**说明**（自动推断）：

pytest 测试类 `TestRepairJsonOutput`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestExtractJsonFromContent`

- **类型**：类  |  **行号**：159–220  |  **完整限定名**：`tests.unit.utils.test_json_utils.TestExtractJsonFromContent`
- **定义**：

```python
class TestExtractJsonFromContent:
```
- **成员概览**：

  - `def test_json_with_extra_tokens_after_closing_brace`
  - `def test_json_with_extra_tokens_after_closing_bracket`
  - `def test_nested_json_with_extra_tokens`
  - `def test_json_with_string_containing_braces`
  - `def test_json_with_escaped_quotes`
  - `def test_clean_json_no_extra_tokens`
  - `def test_empty_object`
  - `def test_empty_array`
  - `def test_extra_closing_brace_no_opening`
  - `def test_extra_closing_bracket_no_opening`

**说明**（自动推断）：

pytest 测试类 `TestExtractJsonFromContent`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestSanitizeToolResponse`

- **类型**：类  |  **行号**：223–272  |  **完整限定名**：`tests.unit.utils.test_json_utils.TestSanitizeToolResponse`
- **定义**：

```python
class TestSanitizeToolResponse:
```
- **成员概览**：

  - `def test_basic_sanitization`
  - `def test_json_with_extra_tokens`
  - `def test_very_long_response_truncation`
  - `def test_custom_max_length`
  - `def test_control_character_removal`
  - `def test_none_content`
  - `def test_whitespace_handling`
  - `def test_json_array_with_extra_tokens`

**说明**（自动推断）：

pytest 测试类 `TestSanitizeToolResponse`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestSanitizeArgs`

- **类型**：类  |  **行号**：275–322  |  **完整限定名**：`tests.unit.utils.test_json_utils.TestSanitizeArgs`
- **定义**：

```python
class TestSanitizeArgs:
```
- **成员概览**：

  - `def test_sanitize_special_characters`
  - `def test_sanitize_square_brackets`
  - `def test_sanitize_curly_braces`
  - `def test_sanitize_mixed_brackets`
  - `def test_sanitize_non_string_input`
  - `def test_sanitize_empty_string`
  - `def test_sanitize_plain_text`
  - `def test_sanitize_nested_structures`

**说明**（自动推断）：

pytest 测试类 `TestSanitizeArgs`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestRepairJsonOutputEdgeCases`

- **类型**：类  |  **行号**：325–458  |  **完整限定名**：`tests.unit.utils.test_json_utils.TestRepairJsonOutputEdgeCases`
- **定义**：

```python
class TestRepairJsonOutputEdgeCases:
```
- **成员概览**：

  - `def test_code_block_with_leading_spaces`
  - `def test_code_block_with_tabs`
  - `def test_code_block_with_multiple_newlines`
  - `def test_code_block_with_spaces_before_closing`
  - `def test_json_with_newlines_in_values`
  - `def test_json_with_special_unicode`
  - `def test_json_boolean_values`
  - `def test_json_numeric_values`
  - `def test_plain_code_block_marker`
  - `def test_multiple_json_objects_takes_first_complete`
  - `def test_chinese_json_with_code_block`
  - `def test_code_block_uppercase_json_with_leading_spaces`
  - `def test_code_block_uppercase_json_with_tabs`
  - `def test_code_block_mixed_case_with_multiple_newlines`
  - `def test_code_block_uppercase_with_spaces_before_closing`
  - `def test_code_block_case_insensitive_various_languages`

**说明**（自动推断）：

pytest 测试类 `TestRepairJsonOutputEdgeCases`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestExtractJsonFromContentEdgeCases`

- **类型**：类  |  **行号**：461–515  |  **完整限定名**：`tests.unit.utils.test_json_utils.TestExtractJsonFromContentEdgeCases`
- **定义**：

```python
class TestExtractJsonFromContentEdgeCases:
```
- **成员概览**：

  - `def test_deeply_nested_json`
  - `def test_json_array_of_arrays`
  - `def test_json_with_backslashes_in_string`
  - `def test_json_with_forward_slashes`
  - `def test_mixed_object_and_array`
  - `def test_json_with_unicode_escape_sequences`
  - `def test_no_json_structure`
  - `def test_unbalanced_braces_in_middle`
  - `def test_json_with_comma_separated_values`

**说明**（自动推断）：

pytest 测试类 `TestExtractJsonFromContentEdgeCases`，聚合一组相关的测试用例方法（以 `test_` 开头）。

### `TestSanitizeToolResponseEdgeCases`

- **类型**：类  |  **行号**：518–581  |  **完整限定名**：`tests.unit.utils.test_json_utils.TestSanitizeToolResponseEdgeCases`
- **定义**：

```python
class TestSanitizeToolResponseEdgeCases:
```
- **成员概览**：

  - `def test_json_object_with_extra_tokens`
  - `def test_truncation_at_exact_boundary`
  - `def test_truncation_one_over_boundary`
  - `def test_multiple_control_characters`
  - `def test_newline_and_tab_preservation`
  - `def test_non_json_content_unchanged`
  - `def test_json_array_at_start`
  - `def test_empty_json_structures_preserved`
  - `def test_whitespace_variations`

**说明**（自动推断）：

pytest 测试类 `TestSanitizeToolResponseEdgeCases`，聚合一组相关的测试用例方法（以 `test_` 开头）。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.utils.test_json_utils import TestRepairJsonOutput
#
# TODO: 结合业务场景补充 TestRepairJsonOutput 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

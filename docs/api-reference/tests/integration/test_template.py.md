# `tests/integration/test_template.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/integration/test_template.py`
- **模块导入名**：`tests.integration.test_template`
- **代码行数**：144
- **架构归属**：tests/integration —— 集成测试（跨组件 / 外部服务，如 crawler、nodes、template、tts）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.prompts.template import apply_prompt_template, get_prompt_template`

**外部依赖**（第三方库 / 标准库）：

- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `test_get_prompt_template_success` | 9 | `()` |
| 函数 | `test_get_prompt_template_not_found` | 17 | `()` |
| 函数 | `test_apply_prompt_template` | 24 | `()` |
| 函数 | `test_apply_prompt_template_empty_messages` | 42 | `()` |
| 函数 | `test_apply_prompt_template_multiple_messages` | 55 | `()` |
| 函数 | `test_apply_prompt_template_with_special_chars` | 73 | `()` |
| 函数 | `test_multiple_template_types` | 86 | `(prompt_name)` |
| 函数 | `test_current_time_format` | 94 | `()` |
| 函数 | `test_apply_prompt_template_reporter` | 110 | `()` |

## 符号详解

### `test_get_prompt_template_success`

- **类型**：函数  |  **行号**：9–14  |  **完整限定名**：`tests.integration.test_template.test_get_prompt_template_success`
- **签名**：

```python
def test_get_prompt_template_success():
```

**摘要**：

Test successful template loading

### `test_get_prompt_template_not_found`

- **类型**：函数  |  **行号**：17–21  |  **完整限定名**：`tests.integration.test_template.test_get_prompt_template_not_found`
- **签名**：

```python
def test_get_prompt_template_not_found():
```

**摘要**：

Test handling of non-existent template

### `test_apply_prompt_template`

- **类型**：函数  |  **行号**：24–39  |  **完整限定名**：`tests.integration.test_template.test_apply_prompt_template`
- **签名**：

```python
def test_apply_prompt_template():
```

**摘要**：

Test template variable substitution

### `test_apply_prompt_template_empty_messages`

- **类型**：函数  |  **行号**：42–52  |  **完整限定名**：`tests.integration.test_template.test_apply_prompt_template_empty_messages`
- **签名**：

```python
def test_apply_prompt_template_empty_messages():
```

**摘要**：

Test template with empty messages list

### `test_apply_prompt_template_multiple_messages`

- **类型**：函数  |  **行号**：55–70  |  **完整限定名**：`tests.integration.test_template.test_apply_prompt_template_multiple_messages`
- **签名**：

```python
def test_apply_prompt_template_multiple_messages():
```

**摘要**：

Test template with multiple messages

### `test_apply_prompt_template_with_special_chars`

- **类型**：函数  |  **行号**：73–82  |  **完整限定名**：`tests.integration.test_template.test_apply_prompt_template_with_special_chars`
- **签名**：

```python
def test_apply_prompt_template_with_special_chars():
```

**摘要**：

Test template with special characters in variables

### `test_multiple_template_types`

- **类型**：函数  |  **行号**：86–91  |  **完整限定名**：`tests.integration.test_template.test_multiple_template_types`
- **装饰器**：`@pytest.mark.parametrize`
- **签名**：

```python
def test_multiple_template_types(prompt_name):
```

**摘要**：

Test loading different types of templates

### `test_current_time_format`

- **类型**：函数  |  **行号**：94–107  |  **完整限定名**：`tests.integration.test_template.test_current_time_format`
- **签名**：

```python
def test_current_time_format():
```

**摘要**：

Test the format of CURRENT_TIME in rendered template

### `test_apply_prompt_template_reporter`

- **类型**：函数  |  **行号**：110–144  |  **完整限定名**：`tests.integration.test_template.test_apply_prompt_template_reporter`
- **签名**：

```python
def test_apply_prompt_template_reporter():
```

**摘要**：

Test reporter template rendering with different styles and locale

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.integration.test_template import test_get_prompt_template_success
#
# TODO: 结合业务场景补充 test_get_prompt_template_success 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `test_fix.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`test_fix.py`
- **模块导入名**：`test_fix`
- **代码行数**：24
- **架构归属**：test_fix.py

## 模块概述

```text
This script manually patches sys.modules to fix the LLM import issue
so that tests can run without requiring LLM configuration.
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from unittest.mock import MagicMock`
- `import sys`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `mock_llm` | 11 | `MagicMock()` |
| 常量 | `mock_llm.invoke.return_value` | 12 | `'Mock LLM response'` |
| 常量 | `mock_llm_module` | 15 | `MagicMock()` |
| 常量 | `mock_llm_module.get_llm_by_type` | 16 | `lambda llm_type: mock_llm` |
| 常量 | `mock_llm_module.basic_llm` | 17 | `mock_llm` |
| 常量 | `mock_llm_module._create_llm_use_conf` | 18 | `lambda llm_type, conf: mock_llm` |
| 常量 | `sys.modules['src.llms.llm']` | 21 | `mock_llm_module` |

## 符号详解

### `mock_llm`

- **类型**：模块常量  |  **行号**：11–11  |  **完整限定名**：`test_fix.mock_llm`
- **值**：

```python
mock_llm = MagicMock()
```

**说明**（自动推断）：

测试用 mock 对象 `mock_llm`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_llm.invoke.return_value`

- **类型**：模块常量  |  **行号**：12–12  |  **完整限定名**：`test_fix.mock_llm.invoke.return_value`
- **值**：

```python
mock_llm.invoke.return_value = 'Mock LLM response'
```

**说明**（自动推断）：

测试用 mock 对象 `mock_llm.invoke.return_value`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_llm_module`

- **类型**：模块常量  |  **行号**：15–15  |  **完整限定名**：`test_fix.mock_llm_module`
- **值**：

```python
mock_llm_module = MagicMock()
```

**说明**（自动推断）：

测试用 mock 对象 `mock_llm_module`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_llm_module.get_llm_by_type`

- **类型**：模块常量  |  **行号**：16–16  |  **完整限定名**：`test_fix.mock_llm_module.get_llm_by_type`
- **值**：

```python
mock_llm_module.get_llm_by_type = lambda llm_type: mock_llm
```

**说明**（自动推断）：

测试用 mock 对象 `mock_llm_module.get_llm_by_type`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_llm_module.basic_llm`

- **类型**：模块常量  |  **行号**：17–17  |  **完整限定名**：`test_fix.mock_llm_module.basic_llm`
- **值**：

```python
mock_llm_module.basic_llm = mock_llm
```

**说明**（自动推断）：

测试用 mock 对象 `mock_llm_module.basic_llm`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `mock_llm_module._create_llm_use_conf`

- **类型**：模块常量  |  **行号**：18–18  |  **完整限定名**：`test_fix.mock_llm_module._create_llm_use_conf`
- **值**：

```python
mock_llm_module._create_llm_use_conf = lambda llm_type, conf: mock_llm
```

**说明**（自动推断）：

测试用 mock 对象 `mock_llm_module._create_llm_use_conf`，用于在测试中替换真实 LLM 依赖以隔离外部调用。

### `sys.modules['src.llms.llm']`

- **类型**：模块常量  |  **行号**：21–21  |  **完整限定名**：`test_fix.sys.modules['src.llms.llm']`
- **值**：

```python
sys.modules['src.llms.llm'] = mock_llm_module
```

**说明**（自动推断）：

测试 hack：直接替换 `sys.modules` 中的模块缓存，用于隔离或注入 mock 模块。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from test_fix import mock_llm
#
# TODO: 结合业务场景补充 mock_llm 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

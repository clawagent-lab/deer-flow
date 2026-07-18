# `tests/unit/config/test_loader.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/config/test_loader.py`
- **模块导入名**：`tests.unit.config.test_loader`
- **代码行数**：82
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

_（该模块未提供 docstring。）_

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.loader import load_yaml_config, process_dict, replace_env_vars`

**外部依赖**（第三方库 / 标准库）：

- `import os`
- `import tempfile`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `test_replace_env_vars_with_env` | 10 | `(monkeypatch)` |
| 函数 | `test_replace_env_vars_without_env` | 15 | `(monkeypatch)` |
| 函数 | `test_replace_env_vars_non_string` | 20 | `()` |
| 函数 | `test_replace_env_vars_regular_string` | 24 | `()` |
| 函数 | `test_process_dict_nested` | 28 | `(monkeypatch)` |
| 函数 | `test_process_dict_empty` | 38 | `()` |
| 函数 | `test_load_yaml_config_file_not_exist` | 42 | `()` |
| 函数 | `test_load_yaml_config` | 46 | `(monkeypatch)` |
| 函数 | `test_load_yaml_config_cache` | 69 | `(monkeypatch)` |

## 符号详解

### `test_replace_env_vars_with_env`

- **类型**：函数  |  **行号**：10–12  |  **完整限定名**：`tests.unit.config.test_loader.test_replace_env_vars_with_env`
- **签名**：

```python
def test_replace_env_vars_with_env(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_replace_env_vars_with_env`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_replace_env_vars_without_env`

- **类型**：函数  |  **行号**：15–17  |  **完整限定名**：`tests.unit.config.test_loader.test_replace_env_vars_without_env`
- **签名**：

```python
def test_replace_env_vars_without_env(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_replace_env_vars_without_env`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_replace_env_vars_non_string`

- **类型**：函数  |  **行号**：20–21  |  **完整限定名**：`tests.unit.config.test_loader.test_replace_env_vars_non_string`
- **签名**：

```python
def test_replace_env_vars_non_string():
```

**说明**（自动推断）：

测试用例函数 `test_replace_env_vars_non_string`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_replace_env_vars_regular_string`

- **类型**：函数  |  **行号**：24–25  |  **完整限定名**：`tests.unit.config.test_loader.test_replace_env_vars_regular_string`
- **签名**：

```python
def test_replace_env_vars_regular_string():
```

**说明**（自动推断）：

测试用例函数 `test_replace_env_vars_regular_string`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_process_dict_nested`

- **类型**：函数  |  **行号**：28–35  |  **完整限定名**：`tests.unit.config.test_loader.test_process_dict_nested`
- **签名**：

```python
def test_process_dict_nested(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_process_dict_nested`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_process_dict_empty`

- **类型**：函数  |  **行号**：38–39  |  **完整限定名**：`tests.unit.config.test_loader.test_process_dict_empty`
- **签名**：

```python
def test_process_dict_empty():
```

**说明**（自动推断）：

测试用例函数 `test_process_dict_empty`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_yaml_config_file_not_exist`

- **类型**：函数  |  **行号**：42–43  |  **完整限定名**：`tests.unit.config.test_loader.test_load_yaml_config_file_not_exist`
- **签名**：

```python
def test_load_yaml_config_file_not_exist():
```

**说明**（自动推断）：

测试用例函数 `test_load_yaml_config_file_not_exist`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_yaml_config`

- **类型**：函数  |  **行号**：46–66  |  **完整限定名**：`tests.unit.config.test_loader.test_load_yaml_config`
- **签名**：

```python
def test_load_yaml_config(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_load_yaml_config`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

### `test_load_yaml_config_cache`

- **类型**：函数  |  **行号**：69–82  |  **完整限定名**：`tests.unit.config.test_loader.test_load_yaml_config_cache`
- **签名**：

```python
def test_load_yaml_config_cache(monkeypatch):
```

**说明**（自动推断）：

测试用例函数 `test_load_yaml_config_cache`。通过 pytest 框架执行，验证被测对象在特定输入下的行为是否符合预期。

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.config.test_loader import test_replace_env_vars_with_env
#
# TODO: 结合业务场景补充 test_replace_env_vars_with_env 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

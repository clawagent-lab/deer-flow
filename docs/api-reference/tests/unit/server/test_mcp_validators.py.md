# `tests/unit/server/test_mcp_validators.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`tests/unit/server/test_mcp_validators.py`
- **模块导入名**：`tests.unit.server.test_mcp_validators`
- **代码行数**：450
- **架构归属**：tests/unit —— 单元测试（按模块组织，聚焦单个类/函数的行为）

## 模块概述

```text
Unit tests for MCP server configuration validators.

Tests cover:
- Command validation (allowlist)
- Argument validation (path traversal, command injection)
- Environment variable validation
- URL validation
- Header validation
- Full config validation
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.server.mcp_validators import ALLOWED_COMMANDS, MCPValidationError, validate_args_for_local_file_access, validate_command, validate_command_injection, validate_environment_variables, validate_headers, validate_mcp_server_config, validate_url`

**外部依赖**（第三方库 / 标准库）：

- `import pytest`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `TestValidateCommand` | 31 | `` |
| 类 | `TestValidateArgsForLocalFileAccess` | 70 | `` |
| 类 | `TestValidateCommandInjection` | 151 | `` |
| 类 | `TestValidateEnvironmentVariables` | 209 | `` |
| 类 | `TestValidateUrl` | 247 | `` |
| 类 | `TestValidateHeaders` | 292 | `` |
| 类 | `TestValidateMCPServerConfig` | 326 | `` |
| 类 | `TestMCPServerMetadataRequest` | 399 | `` |

## 符号详解

### `TestValidateCommand`

- **类型**：类  |  **行号**：31–67  |  **完整限定名**：`tests.unit.server.test_mcp_validators.TestValidateCommand`
- **定义**：

```python
class TestValidateCommand:
```
- **成员概览**：

  - `def test_allowed_commands`
  - `def test_allowed_command_with_path`
  - `def test_disallowed_command`
  - `def test_disallowed_dangerous_commands`
  - `def test_empty_command`
  - `def test_none_command`

**摘要**：

Tests for validate_command function.

### `TestValidateArgsForLocalFileAccess`

- **类型**：类  |  **行号**：70–148  |  **完整限定名**：`tests.unit.server.test_mcp_validators.TestValidateArgsForLocalFileAccess`
- **定义**：

```python
class TestValidateArgsForLocalFileAccess:
```
- **成员概览**：

  - `def test_safe_args`
  - `def test_directory_traversal`
  - `def test_absolute_path_with_dangerous_extension`
  - `def test_windows_absolute_path`
  - `def test_home_directory_reference`
  - `def test_null_byte`
  - `def test_excessively_long_argument`
  - `def test_dangerous_extensions`
  - `def test_empty_args`

**摘要**：

Tests for validate_args_for_local_file_access function.

### `TestValidateCommandInjection`

- **类型**：类  |  **行号**：151–206  |  **完整限定名**：`tests.unit.server.test_mcp_validators.TestValidateCommandInjection`
- **定义**：

```python
class TestValidateCommandInjection:
```
- **成员概览**：

  - `def test_safe_args`
  - `def test_shell_metacharacters`
  - `def test_command_chaining`
  - `def test_backtick_injection`
  - `def test_process_substitution`

**摘要**：

Tests for validate_command_injection function.

### `TestValidateEnvironmentVariables`

- **类型**：类  |  **行号**：209–244  |  **完整限定名**：`tests.unit.server.test_mcp_validators.TestValidateEnvironmentVariables`
- **定义**：

```python
class TestValidateEnvironmentVariables:
```
- **成员概览**：

  - `def test_safe_env_vars`
  - `def test_dangerous_env_vars`
  - `def test_null_byte_in_value`
  - `def test_empty_env`

**摘要**：

Tests for validate_environment_variables function.

### `TestValidateUrl`

- **类型**：类  |  **行号**：247–289  |  **完整限定名**：`tests.unit.server.test_mcp_validators.TestValidateUrl`
- **定义**：

```python
class TestValidateUrl:
```
- **成员概览**：

  - `def test_valid_urls`
  - `def test_invalid_scheme`
  - `def test_credentials_in_url`
  - `def test_null_byte_in_url`
  - `def test_empty_url`
  - `def test_no_host`

**摘要**：

Tests for validate_url function.

### `TestValidateHeaders`

- **类型**：类  |  **行号**：292–323  |  **完整限定名**：`tests.unit.server.test_mcp_validators.TestValidateHeaders`
- **定义**：

```python
class TestValidateHeaders:
```
- **成员概览**：

  - `def test_valid_headers`
  - `def test_newline_in_header_name`
  - `def test_newline_in_header_value`
  - `def test_null_byte_in_header`
  - `def test_empty_headers`

**摘要**：

Tests for validate_headers function.

### `TestValidateMCPServerConfig`

- **类型**：类  |  **行号**：326–396  |  **完整限定名**：`tests.unit.server.test_mcp_validators.TestValidateMCPServerConfig`
- **定义**：

```python
class TestValidateMCPServerConfig:
```
- **成员概览**：

  - `def test_valid_stdio_config`
  - `def test_valid_sse_config`
  - `def test_valid_http_config`
  - `def test_invalid_transport`
  - `def test_combined_validation_errors`
  - `def test_non_strict_mode`
  - `def test_stdio_with_dangerous_args`
  - `def test_sse_with_invalid_url`

**摘要**：

Tests for the main validate_mcp_server_config function.

### `TestMCPServerMetadataRequest`

- **类型**：类  |  **行号**：399–450  |  **完整限定名**：`tests.unit.server.test_mcp_validators.TestMCPServerMetadataRequest`
- **定义**：

```python
class TestMCPServerMetadataRequest:
```
- **成员概览**：

  - `def test_valid_request`
  - `def test_invalid_command_raises_validation_error`
  - `def test_command_injection_raises_validation_error`
  - `def test_invalid_url_raises_validation_error`

**摘要**：

Tests for Pydantic model validation.

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
from tests.unit.server.test_mcp_validators import TestValidateCommand
#
# TODO: 结合业务场景补充 TestValidateCommand 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/server/mcp_validators.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/mcp_validators.py`
- **模块导入名**：`src.server.mcp_validators`
- **代码行数**：532
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
MCP Server Configuration Validators.

This module provides security validation for MCP server configurations,
inspired by Flowise's validateMCPServerConfig implementation. It prevents:
- Command injection attacks
- Path traversal attacks
- Unauthorized file access
- Dangerous environment variable modifications

Reference: https://github.com/FlowiseAI/Flowise/blob/main/packages/components/nodes/tools/MCP/core.ts
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Dict, List, Optional`
- `from urllib.parse import urlparse`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 22 | `logging.getLogger(__name__)` |
| 类 | `MCPValidationError` | 25 | `` |
| 常量 | `ALLOWED_COMMANDS` | 36 | `frozenset(['node', 'npx', 'python', 'python3', 'docker', 'uvx', 'uv', 'deno', 'bun'])` |
| 常量 | `DANGEROUS_ENV_VARS` | 49 | `frozenset(['PATH', 'LD_LIBRARY_PATH', 'DYLD_LIBRARY_PATH', 'LD_PRELOAD', 'DYLD_INSERT_LIBRARIES',...` |
| 常量 | `SHELL_METACHARACTERS` | 62 | `frozenset([';', '&', '\|', '`', '$', '(', ')', '{', '}', '[', ']', '<', '>', '\n', '\r'])` |
| 常量 | `DANGEROUS_EXTENSIONS` | 81 | `frozenset(['.exe', '.dll', '.so', '.dylib', '.bat', '.cmd', '.ps1', '.sh', '.bash', '.zsh', '.env...` |
| 常量 | `COMMAND_CHAINING_PATTERNS` | 101 | `['&&', '\|\|', ';;', '>>', '<<', '$(', '<(', '>(']` |
| 常量 | `MAX_ARG_LENGTH` | 113 | `1000` |
| 常量 | `ALLOWED_URL_SCHEMES` | 116 | `frozenset(['http', 'https'])` |
| 函数 | `validate_mcp_server_config` | 119 | `(transport: str, command: Optional[str]=None, args: Optional[List[str]]=None, url: Optional[str]=...` |
| 函数 | `validate_command` | 205 | `(command: str) -> None` |
| 函数 | `validate_args_for_local_file_access` | 236 | `(args: List[str]) -> None` |
| 函数 | `validate_command_injection` | 330 | `(args: List[str]) -> None` |
| 函数 | `validate_environment_variables` | 370 | `(env: Dict[str, str]) -> None` |
| 函数 | `validate_url` | 431 | `(url: str) -> None` |
| 函数 | `validate_headers` | 479 | `(headers: Dict[str, str]) -> None` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：22–22  |  **完整限定名**：`src.server.mcp_validators.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `MCPValidationError`

- **类型**：类  |  **行号**：25–31  |  **完整限定名**：`src.server.mcp_validators.MCPValidationError`
- **基类**：`Exception`
- **定义**：

```python
class MCPValidationError(Exception):
```
- **成员概览**：

  - `def __init__`

**摘要**：

Exception raised when MCP server configuration validation fails.

### `ALLOWED_COMMANDS`

- **类型**：模块常量  |  **行号**：36–46  |  **完整限定名**：`src.server.mcp_validators.ALLOWED_COMMANDS`
- **值**：

```python
ALLOWED_COMMANDS = frozenset(['node', 'npx', 'python', 'python3', 'docker', 'uvx', 'uv', 'deno', 'bun'])
```

**说明**（自动推断）：

白名单常量 `ALLOWED_COMMANDS`，列出允许的取值集合，用于输入校验。

### `DANGEROUS_ENV_VARS`

- **类型**：模块常量  |  **行号**：49–59  |  **完整限定名**：`src.server.mcp_validators.DANGEROUS_ENV_VARS`
- **值**：

```python
DANGEROUS_ENV_VARS = frozenset(['PATH', 'LD_LIBRARY_PATH', 'DYLD_LIBRARY_PATH', 'LD_PRELOAD', 'DYLD_INSERT_LIBRARIES', 'PYTHONPATH', 'NODE...
```

**说明**（自动推断）：

黑名单/跳过规则常量 `DANGEROUS_ENV_VARS`，列出需拒绝或排除的取值。

### `SHELL_METACHARACTERS`

- **类型**：模块常量  |  **行号**：62–78  |  **完整限定名**：`src.server.mcp_validators.SHELL_METACHARACTERS`
- **值**：

```python
SHELL_METACHARACTERS = frozenset([';', '&', '|', '`', '$', '(', ')', '{', '}', '[', ']', '<', '>', '\n', '\r'])
```

**说明**（自动推断）：

模块级常量 `SHELL_METACHARACTERS`，在导入时初始化，供本模块及相关流程引用。

### `DANGEROUS_EXTENSIONS`

- **类型**：模块常量  |  **行号**：81–98  |  **完整限定名**：`src.server.mcp_validators.DANGEROUS_EXTENSIONS`
- **值**：

```python
DANGEROUS_EXTENSIONS = frozenset(['.exe', '.dll', '.so', '.dylib', '.bat', '.cmd', '.ps1', '.sh', '.bash', '.zsh', '.env', '.pem', '.key', '...
```

**说明**（自动推断）：

黑名单/跳过规则常量 `DANGEROUS_EXTENSIONS`，列出需拒绝或排除的取值。

### `COMMAND_CHAINING_PATTERNS`

- **类型**：模块常量  |  **行号**：101–110  |  **完整限定名**：`src.server.mcp_validators.COMMAND_CHAINING_PATTERNS`
- **值**：

```python
COMMAND_CHAINING_PATTERNS = ['&&', '||', ';;', '>>', '<<', '$(', '<(', '>(']
```

**说明**（自动推断）：

正则模式常量 `COMMAND_CHAINING_PATTERNS`，用于文本匹配或抽取。

### `MAX_ARG_LENGTH`

- **类型**：模块常量  |  **行号**：113–113  |  **完整限定名**：`src.server.mcp_validators.MAX_ARG_LENGTH`
- **值**：

```python
MAX_ARG_LENGTH = 1000
```

**说明**（自动推断）：

数值上限常量 `MAX_ARG_LENGTH`，用于约束对应操作的规模或阈值。

### `ALLOWED_URL_SCHEMES`

- **类型**：模块常量  |  **行号**：116–116  |  **完整限定名**：`src.server.mcp_validators.ALLOWED_URL_SCHEMES`
- **值**：

```python
ALLOWED_URL_SCHEMES = frozenset(['http', 'https'])
```

**说明**（自动推断）：

外部服务 API 地址常量 `ALLOWED_URL_SCHEMES`，在模块导入时从配置或环境变量读取。

### `validate_mcp_server_config`

- **类型**：函数  |  **行号**：119–202  |  **完整限定名**：`src.server.mcp_validators.validate_mcp_server_config`
- **签名**：

```python
def validate_mcp_server_config(transport: str, command: Optional[str]=None, args: Optional[List[str]]=None, url: Optional[str]=None, env: Optional[Dict[str, str]]=None, headers: Optional[Dict[str, str]]=None, strict: bool=True) -> None:
```

**摘要**：

Validate MCP server configuration for security issues.

**参数**：

```text
transport: The type of MCP connection (stdio, sse, streamable_http)
    command: The command to execute (for stdio transport)
    args: Command arguments (for stdio transport)
    url: The URL of the server (for sse/streamable_http transport)
    env: Environment variables (for stdio transport)
    headers: HTTP headers (for sse/streamable_http transport)
    strict: If True, raise exceptions; if False, log warnings only
```

**异常**：

```text
MCPValidationError: If validation fails in strict mode
```

### `validate_command`

- **类型**：函数  |  **行号**：205–233  |  **完整限定名**：`src.server.mcp_validators.validate_command`
- **签名**：

```python
def validate_command(command: str) -> None:
```

**摘要**：

Validate the command against an allowlist of safe executables.

**参数**：

```text
command: The command to validate
```

**异常**：

```text
MCPValidationError: If the command is not in the allowlist
```

### `validate_args_for_local_file_access`

- **类型**：函数  |  **行号**：236–327  |  **完整限定名**：`src.server.mcp_validators.validate_args_for_local_file_access`
- **签名**：

```python
def validate_args_for_local_file_access(args: List[str]) -> None:
```

**摘要**：

Validate arguments to prevent path traversal and unauthorized file access.

**参数**：

```text
args: List of command arguments to validate
```

**异常**：

```text
MCPValidationError: If any argument contains dangerous patterns
```

### `validate_command_injection`

- **类型**：函数  |  **行号**：330–367  |  **完整限定名**：`src.server.mcp_validators.validate_command_injection`
- **签名**：

```python
def validate_command_injection(args: List[str]) -> None:
```

**摘要**：

Validate arguments to prevent shell command injection.

**参数**：

```text
args: List of command arguments to validate
```

**异常**：

```text
MCPValidationError: If any argument contains injection patterns
```

### `validate_environment_variables`

- **类型**：函数  |  **行号**：370–428  |  **完整限定名**：`src.server.mcp_validators.validate_environment_variables`
- **签名**：

```python
def validate_environment_variables(env: Dict[str, str]) -> None:
```

**摘要**：

Validate environment variables to prevent dangerous modifications.

**参数**：

```text
env: Dictionary of environment variables
```

**异常**：

```text
MCPValidationError: If any environment variable is dangerous
```

### `validate_url`

- **类型**：函数  |  **行号**：431–476  |  **完整限定名**：`src.server.mcp_validators.validate_url`
- **签名**：

```python
def validate_url(url: str) -> None:
```

**摘要**：

Validate URL for SSE/HTTP transport.

**参数**：

```text
url: The URL to validate
```

**异常**：

```text
MCPValidationError: If the URL is invalid or potentially dangerous
```

### `validate_headers`

- **类型**：函数  |  **行号**：479–532  |  **完整限定名**：`src.server.mcp_validators.validate_headers`
- **签名**：

```python
def validate_headers(headers: Dict[str, str]) -> None:
```

**摘要**：

Validate HTTP headers for potential injection attacks.

**参数**：

```text
headers: Dictionary of HTTP headers
```

**异常**：

```text
MCPValidationError: If any header contains dangerous patterns
```

## 调用关系（下游）

**被以下模块导入**：

- `src.server.mcp_request`
- `src.server.mcp_utils`
- `tests.unit.server.test_mcp_validators`

## 示例用法

```python
from src.server.mcp_validators import validate_mcp_server_config
#
# TODO: 结合业务场景补充 validate_mcp_server_config 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

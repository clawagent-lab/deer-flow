# `src/server/mcp_utils.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/mcp_utils.py`
- **模块导入名**：`src.server.mcp_utils`
- **代码行数**：150
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
MCP（Model Context Protocol）工具加载工具函数。

提供 ``load_mcp_tools`` 等异步函数，依据 server_type（stdio / sse /
streamable_http）创建对应 MCP 客户端会话，初始化连接并列举可用工具列表，
供 DeerFlow 动态接入外部 MCP 工具服务。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.server.mcp_validators import MCPValidationError, validate_mcp_server_config`

**外部依赖**（第三方库 / 标准库）：

- `from datetime import timedelta`
- `from typing import Any, Dict, List, Optional`
- `from fastapi import HTTPException`
- `from mcp import ClientSession, StdioServerParameters`
- `from mcp.client.sse import sse_client`
- `from mcp.client.stdio import stdio_client`
- `from mcp.client.streamable_http import streamablehttp_client`
- `import logging`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 23 | `logging.getLogger(__name__)` |
| 异步函数 | `_get_tools_from_client_session` | 26 | `(client_context_manager: Any, timeout_seconds: int=10) -> List` |
| 异步函数 | `load_mcp_tools` | 58 | `(server_type: str, command: Optional[str]=None, args: Optional[List[str]]=None, url: Optional[str...` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：23–23  |  **完整限定名**：`src.server.mcp_utils.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `_get_tools_from_client_session`

- **类型**：异步函数  |  **行号**：26–55  |  **完整限定名**：`src.server.mcp_utils._get_tools_from_client_session`
- **签名**：

```python
async def _get_tools_from_client_session(client_context_manager: Any, timeout_seconds: int=10) -> List:
```

**摘要**：

Helper function to get tools from a client session.

**参数**：

```text
client_context_manager: A context manager that returns (read, write) functions
    timeout_seconds: Timeout in seconds for the read operation
```

**返回值**：

```text
List of available tools from the MCP server
```

**异常**：

```text
Exception: If there's an error during the process
```

### `load_mcp_tools`

- **类型**：异步函数  |  **行号**：58–150  |  **完整限定名**：`src.server.mcp_utils.load_mcp_tools`
- **签名**：

```python
async def load_mcp_tools(server_type: str, command: Optional[str]=None, args: Optional[List[str]]=None, url: Optional[str]=None, env: Optional[Dict[str, str]]=None, headers: Optional[Dict[str, str]]=None, timeout_seconds: Optional[int]=30, sse_read_timeout: Optional[int]=None) -> List:
```

**摘要**：

Load tools from an MCP server.

**参数**：

```text
server_type: The type of MCP server connection (stdio, sse, or streamable_http)
    command: The command to execute (for stdio type)
    args: Command arguments (for stdio type)
    url: The URL of the SSE/HTTP server (for sse/streamable_http type)
    env: Environment variables (for stdio type)
    headers: HTTP headers (for sse/streamable_http type)
    timeout_seconds: Timeout in seconds (default: 30)
    sse_read_timeout: SSE read timeout in seconds (for sse type, default: same as timeout_seconds)
```

**返回值**：

```text
List of available tools from the MCP server
```

**异常**：

```text
HTTPException: If there's an error loading the tools
```

## 调用关系（下游）

**被以下模块导入**：

- `src.server.app`
- `tests.unit.server.test_chat_request`
- `tests.unit.server.test_mcp_utils`

## 示例用法

```python
from src.server.mcp_utils import load_mcp_tools
#
# TODO: 结合业务场景补充 load_mcp_tools 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

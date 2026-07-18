# `src/server/mcp_request.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/mcp_request.py`
- **模块导入名**：`src.server.mcp_request`
- **代码行数**：146
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
MCP 服务端元数据请求/响应模型。

定义 ``MCPServerMetadataRequest``（支持 stdio、sse、streamable_http 三种传输方式）
与 ``MCPServerMetadataResponse``，请求模型内嵌 ``model_validator`` 对命令、参数、
环境变量、URL、HTTP 头等进行安全校验，防止命令注入、本地文件越权访问等风险。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.server.mcp_validators import MCPValidationError, validate_args_for_local_file_access, validate_command, validate_command_injection, validate_environment_variables, validate_headers, validate_url`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Dict, List, Optional`
- `from pydantic import BaseModel, Field, model_validator`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `MCPServerMetadataRequest` | 26 | `` |
| 类 | `MCPServerMetadataResponse` | 120 | `` |

## 符号详解

### `MCPServerMetadataRequest`

- **类型**：类  |  **行号**：26–117  |  **完整限定名**：`src.server.mcp_request.MCPServerMetadataRequest`
- **基类**：`BaseModel`
- **定义**：

```python
class MCPServerMetadataRequest(BaseModel):
```
- **成员概览**：

  - `attr transport`
  - `attr command`
  - `attr args`
  - `attr url`
  - `attr env`
  - `attr headers`
  - `attr timeout_seconds`
  - `attr sse_read_timeout`
  - `def validate_security`

**摘要**：

Request model for MCP server metadata.

### `MCPServerMetadataResponse`

- **类型**：类  |  **行号**：120–146  |  **完整限定名**：`src.server.mcp_request.MCPServerMetadataResponse`
- **基类**：`BaseModel`
- **定义**：

```python
class MCPServerMetadataResponse(BaseModel):
```
- **成员概览**：

  - `attr transport`
  - `attr command`
  - `attr args`
  - `attr url`
  - `attr env`
  - `attr headers`
  - `attr tools`

**摘要**：

Response model for MCP server metadata.

## 调用关系（下游）

**被以下模块导入**：

- `src.server.app`
- `tests.unit.server.test_mcp_request`

## 示例用法

```python
from src.server.mcp_request import MCPServerMetadataRequest
#
# TODO: 结合业务场景补充 MCPServerMetadataRequest 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `backend/packages/harness/deerflow/mcp/client.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/mcp/client.py`  ·  行数: 69

**模块文档首行**（仅供参考）: MCP client using langchain-mcp-adapters.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: logging
- `typing` -> Any
- `deerflow.config.extensions_config` -> ExtensionsConfig, McpServerConfig

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `build_server_params(server_name: str, config: McpServerConfig) -> dict[str, Any]`  L11
  - _文档首行_（仅供参考）: Build server parameters for MultiServerMCPClient.
  - 分支数 6，函数体节点数 176；raise: ValueError(f"MCP server '{server_name}' with stdio transport requires 'command' field"), ValueError(f"MCP server '{server_name}' with {transport_type} transport requires 'url' field"), ValueError(f"MCP server '{server_name}' has unsupported transport type: {transport_type}")；return: params
  - 调用: ValueError

#### `ƒ` `build_servers_config(extensions_config: ExtensionsConfig) -> dict[str, dict[str, Any]]`  L45
  - _文档首行_（仅供参考）: Build servers configuration for MultiServerMCPClient.
  - 分支数 3，函数体节点数 110；return: {}, servers_config
  - 调用: get_enabled_mcp_servers, info, items, build_server_params, error

## 文件内调用关系
- `build_servers_config` -> build_server_params

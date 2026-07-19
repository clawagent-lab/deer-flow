# `backend/packages/harness/deerflow/tools/mcp_metadata.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/mcp_metadata.py`  ·  行数: 53

**模块文档首行**（仅供参考）: Single source of truth for the MCP-tool metadata tag.

## 模块概览
- 函数 4 个，类 0 个，模块级常量 2 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Any
- `langchain.tools` -> BaseTool

## 模块级常量
- `MCP_TOOL_METADATA_KEY` = 'deerflow_mcp'
- `MCP_TOOL_ROUTING_METADATA_KEY` = 'deerflow_mcp_routing'

## 函数
#### `ƒ` `tag_mcp_tool(tool: BaseTool) -> BaseTool`  L25
  - _文档首行_（仅供参考）: Mark ``tool`` as MCP-sourced. Mutates in place and returns it for chaining.
  - 分支数 0，函数体节点数 28；return: tool

#### `ƒ` `is_mcp_tool(tool: BaseTool) -> bool`  L31
  - _文档首行_（仅供参考）: True when ``tool`` carries the MCP-source tag written by :func:`tag_mcp_tool`.
  - 分支数 0，函数体节点数 28；return: (getattr(tool, 'metadata', None) or {}).get(MCP_TOOL_METADATA_KEY) is True
  - 调用: get, getattr
  - 反射: getattr (L33)

#### `ƒ` `tag_mcp_routing(tool: BaseTool, routing: Mapping[str, Any]) -> BaseTool`  L36
  - _文档首行_（仅供参考）: Attach serialized MCP routing metadata to ``tool``.
  - 分支数 0，函数体节点数 43；return: tool
  - 调用: dict

#### `ƒ` `get_mcp_routing(tool: BaseTool) -> dict[str, Any] | None`  L45
  - _文档首行_（仅供参考）: Return routing metadata only for MCP tools whose routing mode is active.
  - 分支数 2，函数体节点数 74；return: None, routing
  - 调用: is_mcp_tool, get, getattr, isinstance
  - 反射: getattr (L49)

## 文件内调用关系
- `get_mcp_routing` -> is_mcp_tool

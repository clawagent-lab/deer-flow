# `backend/packages/harness/deerflow/tools/tools.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/tools.py`  ·  行数: 178

## 模块概览
- 函数 3 个，类 0 个，模块级常量 3 个

## 依赖（import）
- 模块: logging
- `langchain.tools` -> BaseTool
- `deerflow.config` -> get_app_config
- `deerflow.config.app_config` -> AppConfig
- `deerflow.reflection` -> resolve_variable
- `deerflow.sandbox.security` -> is_host_bash_allowed
- `deerflow.tools.builtins` -> ask_clarification_tool, present_file_tool, review_skill_package, task_tool, view_image_tool
- `deerflow.tools.mcp_metadata` -> tag_mcp_tool
- `deerflow.tools.sync` -> make_sync_tool_wrapper

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `BUILTIN_TOOLS` = [present_file_tool, ask_clarification_tool, review_skill_...
- `SUBAGENT_TOOLS` = [task_tool]

## 函数
#### `ƒ` `_is_host_bash_tool(tool: object) -> bool`  L27
  - _文档首行_（仅供参考）: Return True if the tool config represents a host-bash execution surface.
  - 分支数 2，函数体节点数 47；return: True, False
  - 调用: getattr
  - 反射: getattr (L29), getattr (L30)

#### `ƒ` `_ensure_sync_invocable_tool(tool: BaseTool) -> BaseTool`  L38
  - _文档首行_（仅供参考）: Attach a sync wrapper to async-only tools used by sync agent callers.
  - 分支数 1，函数体节点数 51；return: tool
  - 调用: getattr, make_sync_tool_wrapper
  - 反射: getattr (L40), getattr (L40)

#### `ƒ` `get_available_tools(groups: list[str] | None, include_mcp: bool, model_name: str | None, subagent_enabled: bool, *, app_config: AppConfig | None) -> list[BaseTool]`  L45
  - _文档首行_（仅供参考）: Get all available tools from config.
  - 分支数 17，函数体节点数 620；return: unique_tools
  - 调用: get_app_config, is_host_bash_allowed, _is_host_bash_tool, resolve_variable, warning, _ensure_sync_invocable_tool, copy, getattr, append, extend, info, get_model_config, from_file, get_enabled_mcp_servers, get_cached_mcp_tools, len, tag_mcp_tool, error, get_acp_agents, build_invoke_acp_agent_tool（+4）
  - 反射: getattr (L93), getattr (L94), getattr (L153)

## 文件内调用关系
- `get_available_tools` -> _is_host_bash_tool, _ensure_sync_invocable_tool

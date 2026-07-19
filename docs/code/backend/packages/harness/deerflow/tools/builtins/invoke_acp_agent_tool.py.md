# `backend/packages/harness/deerflow/tools/builtins/invoke_acp_agent_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/invoke_acp_agent_tool.py`  ·  行数: 258

**模块文档首行**（仅供参考）: Built-in tool for invoking external ACP-compatible agents.

## 模块概览
- 函数 6 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: logging, os, shutil
- `typing` -> Annotated, Any
- `langchain_core.runnables` -> RunnableConfig
- `langchain_core.tools` -> BaseTool, InjectedToolArg, StructuredTool
- `pydantic` -> BaseModel, Field

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_get_work_dir(thread_id: str | None) -> str`  L20
  - _文档首行_（仅供参考）: Get the per-thread ACP workspace directory.
  - 分支数 2，函数体节点数 97；return: str(work_dir)
  - 调用: get_paths, acp_workspace_dir, get_effective_user_id, warning, mkdir, info, str
  - 文件IO: mkdir (L48)

#### `ƒ` `_build_mcp_servers() -> dict[str, dict[str, Any]]`  L53
  - _文档首行_（仅供参考）: Build ACP ``mcpServers`` config from DeerFlow's enabled MCP servers.
  - 分支数 0，函数体节点数 35；return: build_servers_config(ExtensionsConfig.from_file())
  - 调用: build_servers_config, from_file

#### `ƒ` `_build_acp_mcp_servers() -> list[dict[str, Any]]`  L61
  - _文档首行_（仅供参考）: Build ACP ``mcpServers`` payload for ``new_session``.
  - 分支数 5，函数体节点数 260；raise: ValueError(f"MCP server '{name}' with stdio transport requires 'command' field"), ValueError(f"MCP server '{name}' with {transport_type} transport requires 'url' field"), ValueError(f"MCP server '{name}' has unsupported transport type: {transport_type}")；return: mcp_servers
  - 调用: from_file, get_enabled_mcp_servers, items, ValueError, append

#### `ƒ` `_build_permission_response(options: list[Any], *, auto_approve: bool) -> Any`  L97
  - _文档首行_（仅供参考）: Build an ACP permission response.
  - 分支数 6，函数体节点数 105；return: RequestPermissionResponse(outcome=AllowedOutcome(outcome='selected', optionId=option_id)), RequestPermissionResponse(outcome=DeniedOutcome(outcome='cancelled'))
  - 调用: getattr, RequestPermissionResponse, AllowedOutcome, DeniedOutcome
  - 反射: getattr (L111), getattr (L114), getattr (L116)

#### `ƒ` `_format_invocation_error(agent: str, cmd: str, exc: Exception) -> str`  L127
  - _文档首行_（仅供参考）: Return a user-facing ACP invocation error with actionable remediation.
  - 分支数 2，函数体节点数 78；return: f"Error invoking ACP agent '{agent}': {exc}", f'{message} The installed `codex` CLI does not speak ACP directly. Install a Codex ACP adapter (for example `npx @zed-industries/codex-acp`) or update `acp_agents.codex.command` and `args` in config.yaml.', f'{message} Install the agent binary or update `acp_agents.{agent}.command` in config.yaml.'
  - 调用: isinstance, which

#### `ƒ` `build_invoke_acp_agent_tool(agents: dict) -> BaseTool`  L139
  - _文档首行_（仅供参考）: Create the ``invoke_acp_agent`` tool with a description generated from configured agents.
  - 分支数 10，函数体节点数 682；return: f"Error: Unknown agent '{agent}'. Available: {available}", 'Error: agent-client-protocol package is not installed. Run `uv sync` to install project dependencies.', ''.join(self._chunks), response, result or '(no response)', _format_invocation_error(agent, cmd, e), StructuredTool.from_function(name='invoke_acp_agent', description=description, coroutine=_invoke, args_schema=_InvokeACPAgentInput)
  - 调用: join, items, dict, info, len, debug, keys, get, hasattr, isinstance, append, _build_permission_response, warning, _CollectingClient, _get_work_dir, _build_acp_mcp_servers, startswith, spawn_agent_process, initialize, ClientCapabilities（+7）
  - 反射: hasattr (L195)

## 类
### 类 `_InvokeACPAgentInput`  L15
- 继承: BaseModel
- 类/实例变量:
  - `agent` = Field(description='Name of the ACP agent to invoke')
  - `prompt` = Field(description='The concise task prompt to send to the...

## 文件内调用关系
- `build_invoke_acp_agent_tool` -> _build_permission_response, _get_work_dir, _build_acp_mcp_servers, _format_invocation_error

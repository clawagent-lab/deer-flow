# `backend/packages/harness/deerflow/tools/builtins/setup_agent_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/setup_agent_tool.py`  ·  行数: 99

## 模块概览
- 函数 1 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: logging, yaml
- `langchain_core.messages` -> ToolMessage
- `langchain_core.tools` -> tool
- `langgraph.types` -> Command
- `deerflow.config.agents_config` -> validate_agent_name
- `deerflow.config.paths` -> get_paths
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `setup_agent(soul: str, description: str, runtime: Runtime, skills: list[str] | None) -> Command`    @tool(...)  L17
  - _文档首行_（仅供参考）: Setup the custom DeerFlow agent.
  - 分支数 8，函数体节点数 360；return: Command(update={'messages': [ToolMessage(content='Error: soul content is empty; refusing to create agent with an empty SOUL.md', tool_call_id=runtime.tool_call_id)]}), Command(update={'created_agent_name': agent_name, 'messages': [ToolMessage(content=f"Agent '{agent_name}' created successfully!", tool_call_id=runtime.tool_call_id)]}), Command(update={'messages': [ToolMessage(content=f'Error: {e}', tool_call_id=runtime.tool_call_id)]})
  - 调用: strip, Command, ToolMessage, get, validate_agent_name, get_paths, resolve_runtime_user_id, user_agent_dir, exists, mkdir, open, dump, write_text, info, rmtree, error, tool
  - 文件IO: exists (L65), mkdir (L66), open (L77), write_text (L81), exists (L94)

## 文件内调用关系
_无文件内调用_

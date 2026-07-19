# `backend/packages/harness/deerflow/tools/builtins/present_file_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/present_file_tool.py`  ·  行数: 122

## 模块概览
- 函数 3 个，类 0 个，模块级常量 1 个

## 依赖（import）
- `pathlib` -> Path
- `typing` -> Annotated
- `langchain.tools` -> InjectedToolCallId, tool
- `langchain_core.messages` -> ToolMessage
- `langgraph.config` -> get_config
- `langgraph.types` -> Command
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX, get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `OUTPUTS_VIRTUAL_PREFIX` = f'{VIRTUAL_PATH_PREFIX}/outputs'

## 函数
#### `ƒ` `_get_thread_id(runtime: Runtime) -> str | None`  L16
  - _文档首行_（仅供参考）: Resolve the current thread id from runtime context or RunnableConfig.
  - 分支数 3，函数体节点数 87；return: thread_id, get_config().get('configurable', {}).get('thread_id'), None
  - 调用: get, getattr, get_config
  - 反射: getattr (L22)

#### `ƒ` `_normalize_presented_filepath(runtime: Runtime, filepath: str) -> str`  L33
  - _文档首行_（仅供参考）: Normalize a presented file path to the `/mnt/user-data/outputs/*` contract.
  - 分支数 6，函数体节点数 213；raise: ValueError('Thread runtime state is not available'), ValueError('Thread ID is not available in runtime context or runtime config'), ValueError('Thread outputs path is not available in runtime state'), ValueError(f'Only files in {OUTPUTS_VIRTUAL_PREFIX} can be presented: {filepath}')；return: f'{OUTPUTS_VIRTUAL_PREFIX}/{relative_path.as_posix()}'
  - 调用: ValueError, _get_thread_id, get, resolve, Path, lstrip, startswith, resolve_virtual_path, get_paths, get_effective_user_id, expanduser, relative_to, as_posix

#### `ƒ` `present_file_tool(runtime: Runtime, filepaths: list[str], tool_call_id: Annotated[str, InjectedToolCallId]) -> Command`    @tool(...)  L84
  - _文档首行_（仅供参考）: Make files visible to the user for viewing and rendering in the client interface.
  - 分支数 1，函数体节点数 92；return: Command(update={'messages': [ToolMessage(f'Error: {exc}', tool_call_id=tool_call_id)]}), Command(update={'artifacts': normalized_paths, 'messages': [ToolMessage('Successfully presented files', tool_call_id=tool_call_id)]})
  - 调用: _normalize_presented_filepath, Command, ToolMessage, tool

## 文件内调用关系
- `_normalize_presented_filepath` -> _get_thread_id
- `present_file_tool` -> _normalize_presented_filepath

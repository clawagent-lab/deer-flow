# `backend/packages/harness/deerflow/tools/builtins/update_agent_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/update_agent_tool.py`  ·  行数: 309

**模块文档首行**（仅供参考）: update_agent tool — let a custom agent persist updates to its own SOUL.md / config.

## 模块概览
- 函数 5 个，类 0 个，模块级常量 5 个

## 依赖（import）
- 模块: logging, tempfile, yaml
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Annotated, Any
- `langchain_core.messages` -> ToolMessage
- `langchain_core.tools` -> tool
- `langgraph.types` -> Command
- `pydantic` -> BeforeValidator
- `deerflow.config.agents_config` -> load_agent_config, preserve_non_managed_fields, validate_agent_name
- `deerflow.config.app_config` -> get_app_config
- `deerflow.config.paths` -> get_paths
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_NULLISH_STRINGS` = frozenset({'null', 'none', 'undefined'})
- `_UNTRUSTED_CHANNELS` = frozenset({'github'})
- `OptionalText` = Annotated[str | None, BeforeValidator(_normalize_nullish_...
- `OptionalStringList` = Annotated[list[str] | None, BeforeValidator(_normalize_nu...

## 函数
#### `ƒ` `_stage_temp(path: Path, text: str) -> Path`  L47
  - _文档首行_（仅供参考）: Write ``text`` into a sibling temp file and return its path.
  - 分支数 1，函数体节点数 97；raise: bare raise；return: Path(fd.name)
  - 调用: mkdir, NamedTemporaryFile, write, flush, close, Path, unlink
  - 文件IO: mkdir (L53), write (L62), unlink (L68)

#### `ƒ` `_cleanup_temps(temps: list[Path]) -> None`  L72
  - _文档首行_（仅供参考）: Best-effort removal of staged temp files.
  - 分支数 2，函数体节点数 40
  - 调用: unlink, debug
  - 文件IO: unlink (L76)

#### `ƒ` `_is_nullish_string(value: object) -> bool`  L81
  - 分支数 0，函数体节点数 29；return: isinstance(value, str) and value.strip().lower() in _NULLISH_STRINGS
  - 调用: isinstance, lower, strip

#### `ƒ` `_normalize_nullish_string(value: object) -> object`  L85
  - 分支数 0，函数体节点数 17；return: None if _is_nullish_string(value) else value
  - 调用: _is_nullish_string

#### `ƒ` `update_agent(runtime: Runtime, soul: OptionalText, description: OptionalText, skills: OptionalStringList, tool_groups: OptionalStringList, model: OptionalText) -> Command`    @tool(...)  L94
  - _文档首行_（仅供参考）: Persist updates to the current custom agent's SOUL.md and config.yaml.
  - 分支数 24，函数体节点数 1020；raise: bare raise；return: Command(update={'messages': [ToolMessage(content=f'Error: {message}', tool_call_id=tool_call_id, status='error')]}), _err(f'update_agent is disabled on the {channel_name!r} channel. Self-mutation requests must come from an operator-trusted surface (chat UI or the HTTP API), not a webhook fan-out.'), _err('No fields provided. Pass at least one of: soul, description, skills, tool_groups, model. Omit unchanged fields instead of passing null-like strings such as "null", "none", or "undefined".'), _err('soul content is empty; refusing to update agent with an empty SOUL.md. Omit the soul field if you do not want to change it.'), _err(str(e)), _err("update_agent is only available inside a custom agent's chat. There is no agent_name in the current runtime context, so there is nothing to update. If you are inside the bootstrap flow, use setup_agent instead."), _err(f"Unknown model '{model}'. Pass a model name that exists in config.yaml's models section."), _err(f"Agent '{agent_name}' only exists in the legacy shared layout and is not scoped to a user. Run scripts/migrate_user_isolation.py to move legacy agents into the per-user layout before updating."), _err(f"Agent '{agent_name}' does not exist for the current user. Use setup_agent to create a new agent first."), _err(f"Agent '{agent_name}' has an unreadable config: {e}"), _err(f"Agent '{agent_name}' could not be loaded."), _err(f"Partial update for agent '{agent_name}': {[p.name for p in committed]} were updated, but the rest failed ({e}). Re-run update_agent to retry the remaining fields."), _err(f"Failed to update agent '{agent_name}': {e}"), Command(update={'messages': [ToolMessage(content=f"No changes applied to agent '{agent_name}'. The provided values matched the existing config.", tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(content=f"Agent '{agent_name}' updated successfully. Changed: {', '.join(updated_fields)}. The new configuration takes effect on the next user turn.", tool_call_id=tool_call_id)]})
  - 调用: get, Command, ToolMessage, _err, strip, validate_agent_name, str, resolve_runtime_user_id, get_model_config, get_app_config, get_paths, user_agent_dir, agent_dir, exists, load_agent_config, append, preserve_non_managed_fields, items, setdefault, bool（+10）
  - 文件IO: exists (L189), exists (L189), mkdir (L250), replace (L274)

## 文件内调用关系
- `_normalize_nullish_string` -> _is_nullish_string
- `update_agent` -> _stage_temp, _cleanup_temps

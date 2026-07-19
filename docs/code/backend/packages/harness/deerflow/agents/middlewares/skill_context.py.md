# `backend/packages/harness/deerflow/agents/middlewares/skill_context.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/skill_context.py`  ·  行数: 201

**模块文档首行**（仅供参考）: Deterministic capture and rendering for loaded skill files.

## 模块概览
- 函数 13 个，类 1 个，模块级常量 4 个

## 依赖（import）
- 模块: logging, posixpath, re, yaml
- `__future__` -> annotations
- `collections.abc` -> Collection, Mapping
- `html` -> escape
- `typing` -> Any, TypedDict
- `langchain_core.messages` -> AIMessage, AnyMessage, ToolMessage
- `deerflow.agents.thread_state` -> _SKILL_DESCRIPTION_MAX_CHARS, SkillEntry

## 模块级常量
- `_SKILL_FILE_NAME` = 'SKILL.md'
- `_FRONT_MATTER_RE` = re.compile('^---\\s*\\n(.*?)\\n---\\s*\\n', re.DOTALL)
- `SKILL_CONTEXT_ENTRY_KEY` = 'skill_context_entry'
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `_tool_call_name(tool_call: dict[str, Any]) -> str`  L28
  - 分支数 2，函数体节点数 73；return: name, function['name'], ''
  - 调用: get, isinstance

#### `ƒ` `_tool_call_id(tool_call: dict[str, Any]) -> str | None`  L38
  - 分支数 0，函数体节点数 37；return: str(tool_call_id) if tool_call_id else None
  - 调用: get, str

#### `ƒ` `_tool_call_path(tool_call: dict[str, Any]) -> str | None`  L43
  - 分支数 3，函数体节点数 74；return: None, value
  - 调用: get, isinstance

#### `ƒ` `_normalize_under_root(path: str, normalized_root: str) -> str | None`  L54
  - 分支数 1，函数体节点数 47；return: normalized, None
  - 调用: normpath, startswith

#### `ƒ` `_is_skill_file(path: str) -> bool`  L61
  - 分支数 0，函数体节点数 19；return: posixpath.basename(path) == _SKILL_FILE_NAME
  - 调用: basename

#### `ƒ` `_skill_name_from_path(skill_md_path: str) -> str`  L65
  - _文档首行_（仅供参考）: Derive the skill name from the directory containing SKILL.md.
  - 分支数 0，函数体节点数 22；return: posixpath.basename(posixpath.dirname(skill_md_path))
  - 调用: basename, dirname

#### `ƒ` `_parse_description(content: str) -> str`  L70
  - _文档首行_（仅供参考）: Extract frontmatter description from already-read SKILL.md content.
  - 分支数 4，函数体节点数 96；return: '', ' '.join(description.split())[:_SKILL_DESCRIPTION_MAX_CHARS]
  - 调用: match, safe_load, group, isinstance, get, join, split

#### `ƒ` `_is_tool_error_text(content: str) -> bool`  L87
  - 分支数 0，函数体节点数 17；return: content.lstrip().startswith('Error:')
  - 调用: startswith, lstrip

#### `ƒ` `build_skill_entry_metadata_from_read(path: str, content: str, *, skills_root: str) -> SkillEntryMetadata | None`  L91
  - 分支数 1，函数体节点数 76；return: None, {'path': normalized_path, 'description': _parse_description(content)}
  - 调用: normpath, rstrip, _normalize_under_root, _is_skill_file, _is_tool_error_text, _parse_description

#### `ƒ` `read_skill_entry_metadata(additional_kwargs: Mapping[str, object] | None) -> SkillEntryMetadata | None`  L107
  - 分支数 3，函数体节点数 109；return: None, {'path': path, 'description': ' '.join(description.split())[:_SKILL_DESCRIPTION_MAX_CHARS] if isinstance(description, str) else ''}
  - 调用: get, isinstance, join, split

#### `ƒ` `_escape_context_text(value: object) -> str`  L123
  - 分支数 0，函数体节点数 18；return: escape(str(value), quote=False)
  - 调用: escape, str

#### `ƒ` `extract_skills(messages: list[AnyMessage], *, skills_root: str, read_tool_names: Collection[str]) -> list[SkillEntry]`  L127
  - _文档首行_（仅供参考）: Enumerate skill-file reads (AI read_file call + paired ToolMessage result).
  - 分支数 12，函数体节点数 343；return: entries
  - 调用: normpath, rstrip, frozenset, isinstance, _tool_call_name, _tool_call_id, _tool_call_path, _normalize_under_root, _is_skill_file, enumerate, getattr, str, get, read_skill_entry_metadata, _is_tool_error_text, warning, append, _skill_name_from_path
  - 反射: getattr (L154)

#### `ƒ` `render_skill_context(entries: list[SkillEntry]) -> str`  L185
  - _文档首行_（仅供参考）: Render active-skill references as a compact reminder, not the body.
  - 分支数 3，函数体节点数 135；return: '', '\n'.join(lines)
  - 调用: _escape_context_text, get, isinstance, join, split, append

## 类
### 类 `SkillEntryMetadata`  L23
- 继承: TypedDict
- 类/实例变量:
  - `path` = <annotated>
  - `description` = <annotated>

## 文件内调用关系
- `build_skill_entry_metadata_from_read` -> _normalize_under_root, _is_skill_file, _is_tool_error_text, _parse_description
- `extract_skills` -> _tool_call_name, _tool_call_id, _tool_call_path, _normalize_under_root, _is_skill_file, read_skill_entry_metadata, _is_tool_error_text, _skill_name_from_path
- `render_skill_context` -> _escape_context_text

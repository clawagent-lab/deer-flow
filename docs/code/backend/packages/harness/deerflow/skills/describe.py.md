# `backend/packages/harness/deerflow/skills/describe.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/describe.py`  ·  行数: 188

**模块文档首行**（仅供参考）: describe_skill — deferred skill metadata retrieval at runtime.

## 模块概览
- 函数 4 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: html, logging
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> TYPE_CHECKING, Annotated
- `langchain_core.messages` -> ToolMessage
- `langchain_core.tools` -> InjectedToolCallId, tool
- `langgraph.types` -> Command
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.skills.catalog` -> SkillCatalog
- `deerflow.skills.types` -> SkillCategory

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 函数
#### `ƒ` `build_describe_skill_tool(catalog: SkillCatalog, *, container_base_path: str) -> BaseTool`  L51
  - _文档首行_（仅供参考）: Build the ``describe_skill`` tool as a closure over *catalog*.
  - 分支数 1，函数体节点数 92；return: Command(update={'messages': [ToolMessage(content=content, tool_call_id=tool_call_id, name='describe_skill')]}), describe_skill
  - 调用: search, _render_skill_metadata, Command, ToolMessage

#### `ƒ` `build_skill_search_setup(skills: list, *, enabled: bool, container_base_path: str) -> SkillSearchSetup`  L102
  - _文档首行_（仅供参考）: Build the skill search setup from a filtered skill list.
  - 分支数 1，函数体节点数 65；return: SkillSearchSetup(None, frozenset()), SkillSearchSetup(describe_skill_tool=build_describe_skill_tool(catalog, container_base_path=container_base_path), skill_names=catalog.names)
  - 调用: SkillSearchSetup, frozenset, SkillCatalog, tuple, build_describe_skill_tool

#### `ƒ` `_render_skill_metadata(skills: list, container_base_path: str) -> str`  L130
  - _文档首行_（仅供参考）: Render structured metadata for a list of matched skills.
  - 分支数 1，函数体节点数 157；return: '\n\n'.join(blocks)
  - 调用: join, get_container_file_path, escape, append

#### `ƒ` `get_skill_index_prompt_section(*, skill_names: frozenset[str], container_base_path: str, skill_evolution_section: str) -> str`  L150
  - _文档首行_（仅供参考）: Generate ``<skill_system>`` with a name-only ``<skill_index>``.
  - 分支数 1，函数体节点数 84；return: '', f"<skill_system>\nYou have access to skills that provide optimized workflows for specific tasks.\n\n**Skill Discovery:**\n1. Check <skill_index> for a skill name that matches your task\n2. Call describe_skill(name) to fetch its description and capabilities\n3. If the skill matches, call read_file on the returned location to load full instructions\n4. Follow the skill's instructions precisely\n\n**Explicit Slash Skill Activation:**\n- If the user starts a request with `/<skill-name>`, that skill was explicitly requested.\n- The runtime injects the activated skill content; do not call `read_file` for that SKILL.md again unless the injected skill references supporting resources you need.\n{evolution}\n<skill_index>\n{names}\n</skill_index>\n\nSkills are located at: {container_base_path}\n</skill_system>"
  - 调用: frozenset, join, escape, sorted

## 类
### 类 `SkillSearchSetup`  L36  @dataclass(...)
- _文档首行_: Result of assembling skill search for one agent build.
- 类/实例变量:
  - `describe_skill_tool` = <annotated>
  - `skill_names` = <annotated>

## 文件内调用关系
- `build_describe_skill_tool` -> _render_skill_metadata
- `build_skill_search_setup` -> build_describe_skill_tool

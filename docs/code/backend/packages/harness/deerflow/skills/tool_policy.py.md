# `backend/packages/harness/deerflow/skills/tool_policy.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/tool_policy.py`  ·  行数: 66

## 模块概览
- 函数 2 个，类 1 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `typing` -> Protocol
- `deerflow.skills.types` -> Skill

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `ALWAYS_AVAILABLE_BUILTIN_TOOL_NAMES` = frozenset({'describe_skill', 'read_file', 'review_skill_p...

## 函数
#### `ƒ` `allowed_tool_names_for_skills(skills: list[Skill]) -> set[str] | None`  L28
  - _文档首行_（仅供参考）: Return the union of explicit skill allowed-tools declarations.
  - 分支数 5，函数体节点数 99；return: None, allowed
  - 调用: set, info, update

#### `ƒ` `filter_tools_by_skill_allowed_tools(tools: list[ToolT], skills: list[Skill], *, always_allowed_tool_names: set[str] | frozenset[str]) -> list[ToolT]`  L54
  - 分支数 1，函数体节点数 89；return: tools, [tool for tool in tools if tool.name in allowed_with_framework_tools]
  - 调用: frozenset, allowed_tool_names_for_skills, set

## 类
### 类 `NamedTool`  L9
- 继承: Protocol
- 类/实例变量:
  - `name` = <annotated>

## 文件内调用关系
- `filter_tools_by_skill_allowed_tools` -> allowed_tool_names_for_skills

# `backend/packages/harness/deerflow/agents/thread_state.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/thread_state.py`  ·  行数: 252

## 模块概览
- 函数 9 个，类 7 个，模块级常量 5 个

## 依赖（import）
- `collections.abc` -> Mapping
- `typing` -> Annotated, NotRequired, TypedDict
- `langchain.agents` -> AgentState
- `deerflow.agents.goal_state` -> GoalState
- `deerflow.subagents.status_contract` -> SUBAGENT_STATUS_VALUES

## 模块级常量
- `SandboxStateField` = Annotated[NotRequired[SandboxState | None], merge_sandbox]
- `TERMINAL_STATUSES` = frozenset(SUBAGENT_STATUS_VALUES)
- `_DELEGATION_LEDGER_MAX_ENTRIES` = 50
- `_SKILL_CONTEXT_MAX_ENTRIES` = 8
- `_SKILL_DESCRIPTION_MAX_CHARS` = 500

## 函数
#### `ƒ` `merge_sandbox(existing: SandboxState | None, new: SandboxState | None) -> SandboxState | None`  L34
  - _文档首行_（仅供参考）: Reducer for sandbox state - accepts idempotent writes only.
  - 分支数 3，函数体节点数 80；raise: ValueError(f'Conflicting sandbox state updates: {existing_id!r} != {new_id!r}')；return: existing, new
  - 调用: get, ValueError

#### `ƒ` `merge_artifacts(existing: list[str] | None, new: list[str] | None) -> list[str]`  L58
  - _文档首行_（仅供参考）: Reducer for artifacts list - merges and deduplicates artifacts.
  - 分支数 2，函数体节点数 67；return: new or [], existing, list(dict.fromkeys(existing + new))
  - 调用: list, fromkeys

#### `ƒ` `merge_viewed_images(existing: dict[str, ViewedImageData] | None, new: dict[str, ViewedImageData] | None) -> dict[str, ViewedImageData]`  L68
  - _文档首行_（仅供参考）: Reducer for viewed_images dict - merges image dictionaries.
  - 分支数 3，函数体节点数 80；return: new or {}, existing, {}, {**existing, **new}
  - 调用: len

#### `ƒ` `merge_todos(existing: list | None, new: list | None) -> list | None`  L85
  - _文档首行_（仅供参考）: Reducer for todos list - keeps the last non-None value.
  - 分支数 1，函数体节点数 33；return: existing, new

#### `ƒ` `merge_goal(existing: GoalState | None, new: GoalState | None) -> GoalState | None`  L98
  - _文档首行_（仅供参考）: Reducer for goal state - preserves existing when a node does not touch it.
  - 分支数 1，函数体节点数 33；return: existing, new

#### `ƒ` `merge_promoted(existing: PromotedTools | None, new: PromotedTools | None) -> PromotedTools | None`  L110
  - _文档首行_（仅供参考）: Reducer for deferred-tool promotions, scoped by catalog hash.
  - 分支数 2，函数体节点数 101；return: existing, {'catalog_hash': new['catalog_hash'], 'names': list(dict.fromkeys(new['names']))}, {'catalog_hash': existing['catalog_hash'], 'names': list(dict.fromkeys(existing['names'] + new['names']))}
  - 调用: get, list, fromkeys

#### `ƒ` `merge_delegations(existing: list[DelegationEntry] | None, new: list[DelegationEntry] | None) -> list[DelegationEntry]`  L151
  - _文档首行_（仅供参考）: Reducer for the delegation ledger.
  - 分支数 7，函数体节点数 240；return: existing or [], merged
  - 调用: get, append, len

#### `ƒ` `_normalize_skill_entry(entry: Mapping[str, object]) -> SkillEntry`  L193
  - _文档首行_（仅供参考）: Drop legacy payload keys before storing skill_context back to state.
  - 分支数 0，函数体节点数 95；return: {'name': str(entry.get('name') or ''), 'path': str(entry['path']), 'description': ' '.join(description.split())[:_SKILL_DESCRIPTION_MAX_CHARS] if isinstance(description, str) else '', 'loaded_at': loaded_at if isinstance(loaded_at, int) else 0}
  - 调用: get, str, isinstance, join, split

#### `ƒ` `merge_skill_context(existing: list[SkillEntry] | None, new: list[SkillEntry] | None) -> list[SkillEntry]`  L205
  - _文档首行_（仅供参考）: Reducer for the skill-context channel.
  - 分支数 6，函数体节点数 212；return: normalized_existing, merged
  - 调用: _normalize_skill_entry, append, remove, len

## 类
### 类 `SandboxState`  L10
- 继承: TypedDict
- 类/实例变量:
  - `sandbox_id` = <annotated>

### 类 `ThreadDataState`  L14
- 继承: TypedDict
- 类/实例变量:
  - `workspace_path` = <annotated>
  - `uploads_path` = <annotated>
  - `outputs_path` = <annotated>

### 类 `ViewedImageData`  L20
- 继承: TypedDict
- _文档首行_: Metadata for a viewed image file.
- 类/实例变量:
  - `mime_type` = <annotated>
  - `size` = <annotated>
  - `actual_path` = <annotated>

### 类 `PromotedTools`  L105
- 继承: TypedDict
- 类/实例变量:
  - `catalog_hash` = <annotated>
  - `names` = <annotated>

### 类 `DelegationEntry`  L135
- 继承: TypedDict
- 类/实例变量:
  - `id` = <annotated>
  - `run_id` = <annotated>
  - `description` = <annotated>
  - `subagent_type` = <annotated>
  - `status` = <annotated>
  - `result_brief` = <annotated>
  - `result_sha256` = <annotated>
  - `result_ref` = <annotated>
  - `stop_reason` = <annotated>
  - `created_at` = <annotated>

### 类 `SkillEntry`  L186
- 继承: TypedDict
- 类/实例变量:
  - `name` = <annotated>
  - `path` = <annotated>
  - `description` = <annotated>
  - `loaded_at` = <annotated>

### 类 `ThreadState`  L239
- 继承: AgentState
- 类/实例变量:
  - `sandbox` = <annotated>
  - `thread_data` = <annotated>
  - `title` = <annotated>
  - `artifacts` = <annotated>
  - `todos` = <annotated>
  - `goal` = <annotated>
  - `uploaded_files` = <annotated>
  - `viewed_images` = <annotated>
  - `promoted` = <annotated>
  - `delegations` = <annotated>
  - `skill_context` = <annotated>
  - `summary_text` = <annotated>

## 文件内调用关系
- `merge_skill_context` -> _normalize_skill_entry

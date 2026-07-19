# `backend/packages/harness/deerflow/agents/lead_agent/prompt.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/lead_agent/prompt.py`  ·  行数: 1087

## 模块概览
- 函数 28 个，类 1 个，模块级常量 11 个

## 依赖（import）
- 模块: asyncio, html, logging, threading
- `__future__` -> annotations
- `collections` -> OrderedDict
- `dataclasses` -> dataclass, field
- `functools` -> lru_cache
- `typing` -> TYPE_CHECKING
- `deerflow.config.agents_config` -> load_agent_soul
- `deerflow.config.subagents_config` -> DEFAULT_MAX_TOTAL_SUBAGENTS_PER_RUN, clamp_subagent_concurrency, clamp_total_subagents_per_run
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.skills.storage` -> get_or_new_skill_storage, get_or_new_user_skill_storage
- `deerflow.skills.types` -> Skill, SkillCategory
- `deerflow.subagents` -> get_available_subagent_names
- `deerflow.tools.builtins.tool_search` -> get_deferred_tools_prompt_section

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_ENABLED_SKILLS_BY_CONFIG_CACHE_MAXSIZE` = 256
- `_ENABLED_SKILLS_REFRESH_WAIT_TIMEOUT_SECONDS` = 5.0
- `_enabled_skills_lock` = threading.Lock()
- `_enabled_skills_cache` = None
- `_enabled_skills_by_config_cache` = OrderedDict()
- `_enabled_skills_refresh_active` = False
- `_enabled_skills_refresh_version` = 0
- `_enabled_skills_refresh_event` = threading.Event()
- `_enabled_skills_refresh_waiters` = []
- `SYSTEM_PROMPT_TEMPLATE` = '\n<role>\nYou are {agent_name}, an open-source super age...

## 函数
#### `ƒ` `_load_enabled_skills_sync() -> list[Skill]`  L61
  - 分支数 0，函数体节点数 20；return: list(get_or_new_skill_storage().load_skills(enabled_only=True))
  - 调用: list, load_skills, get_or_new_skill_storage

#### `ƒ` `_start_enabled_skills_refresh_thread() -> None`  L65
  - 分支数 0，函数体节点数 19
  - 调用: start, Thread

#### `ƒ` `_refresh_enabled_skills_cache_worker() -> None`  L73
  - 分支数 7，函数体节点数 145；return: None
  - 调用: _load_enabled_skills_sync, exception, set

#### `ƒ` `_ensure_enabled_skills_cache() -> threading.Event`  L106
  - 分支数 3，函数体节点数 49；return: _enabled_skills_refresh_event
  - 调用: set, clear, _start_enabled_skills_refresh_thread

#### `ƒ` `_invalidate_enabled_skills_cache() -> _EnabledSkillsRefreshHandle`  L122
  - 分支数 2，函数体节点数 66；return: refresh_handle
  - 调用: cache_clear, clear, _EnabledSkillsRefreshHandle, append, _start_enabled_skills_refresh_thread

#### `ƒ` `prime_enabled_skills_cache() -> None`  L140
  - 分支数 0，函数体节点数 7
  - 调用: _ensure_enabled_skills_cache

#### `ƒ` `warm_enabled_skills_cache(timeout_seconds: float) -> bool`  L144
  - 分支数 1，函数体节点数 32；return: True, False
  - 调用: wait, _ensure_enabled_skills_cache, warning

#### `ƒ` `_get_enabled_skills()`  L152
  - 分支数 0，函数体节点数 6；return: get_cached_enabled_skills()
  - 调用: get_cached_enabled_skills

#### `ƒ` `get_cached_enabled_skills() -> list[Skill]`  L156
  - _文档首行_（仅供参考）: Return the cached enabled-skills list, kicking off a background refresh on miss.
  - 分支数 2，函数体节点数 38；return: list(cached), []
  - 调用: list, _ensure_enabled_skills_cache

#### `ƒ` `get_enabled_skills_for_config(app_config: AppConfig | None, user_id: str | None) -> list[Skill]`  L172
  - _文档首行_（仅供参考）: Return enabled skills using the caller's config source and user scope.
  - 分支数 8，函数体节点数 191；return: _get_enabled_skills(), list(cached_skills), list(skills)
  - 调用: _get_enabled_skills, id, get, move_to_end, list, load_skills, get_or_new_user_skill_storage, get_or_new_skill_storage, len, popitem

#### `ƒ` `_skill_mutability_label(category: SkillCategory | str) -> str`  L214
  - 分支数 2，函数体节点数 35；return: '[custom, editable]', '[legacy, read-only]', '[built-in]'

#### `ƒ` `_render_available_skill(name: str, description: str, category: SkillCategory | str, location: str) -> str`  L222
  - 分支数 0，函数体节点数 78；return: f'    <skill>\n        <name>{esc_name}</name>\n        <description>{esc_description} {_skill_mutability_label(category)}</description>\n        <location>{esc_location}</location>\n    </skill>'
  - 调用: escape, _skill_mutability_label

#### `ƒ` `clear_skills_system_prompt_cache() -> None`  L233
  - 分支数 0，函数体节点数 7
  - 调用: _invalidate_enabled_skills_cache

#### `⏵ƒ` `async refresh_skills_system_prompt_cache_async() -> None`  L237
  - 分支数 2，函数体节点数 51；raise: TimeoutError('Timed out waiting for enabled skills cache refresh'), RuntimeError('Enabled skills cache refresh failed')
  - 调用: _invalidate_enabled_skills_cache, to_thread, TimeoutError, RuntimeError

#### `ƒ` `invalidate_user_skill_cache(user_id: str) -> None`  L246
  - _文档首行_（仅供参考）: Invalidate the skill cache for a specific user only.
  - 分支数 2，函数体节点数 52
  - 调用: pop, cache_clear

#### `⏵ƒ` `async refresh_user_skills_system_prompt_cache_async(user_id: str) -> None`  L263
  - _文档首行_（仅供参考）: Per-user variant of :func:`refresh_skills_system_prompt_cache_async`.
  - 分支数 0，函数体节点数 14
  - 调用: invalidate_user_skill_cache

#### `ƒ` `_build_skill_evolution_section(skill_evolution_enabled: bool) -> str`  L274
  - 分支数 1，函数体节点数 16；return: '', '\n## Skill Self-Evolution\nAfter completing a task, consider creating or updating a skill when:\n- The task required 5+ tool calls to resolve\n- You overcame non-obvious errors or pitfalls\n- The user corrected your approach and the corrected version worked\n- You discovered a non-trivial, recurring workflow\nIf you used a skill and encountered issues not covered by it, patch it immediately.\n\n**CRITICAL: You MUST use the `skill_manage` tool for ALL skill operations.**\n- `skill_manage(action="create", name="my-skill", content="...")` — Create a new skill\n- `skill_manage(action="patch", name="my-skill", find="...", replace="...")` — Patch an existing skill\n- `skill_manage(action="edit", name="my-skill", content="...")` — Full edit of an existing skill\n- `skill_manage(action="write_file", name="my-skill", path="scripts/run.py", content="...")` — Add supporting files\n- `skill_manage(action="delete", name="my-skill")` — Delete a skill\n\n**⛔ NEVER write SKILL.md files to `/mnt/user-data/workspace` or `/mnt/user-data/outputs`.**\nSkills are NOT deliverables — they are persistent capabilities managed through `skill_manage`.\nThe tool stores skills in the per-user skills directory automatically; you do NOT need to specify a path.\n\nPrefer patch over edit. Before creating a new skill, confirm with the user first.\nSkip simple one-off tasks.\n'

#### `ƒ` `_build_available_subagents_description(available_names: list[str], bash_available: bool, *, app_config: AppConfig | None) -> str`  L302
  - _文档首行_（仅供参考）: Dynamically build subagent type descriptions from registry.
  - 分支数 3，函数体节点数 136；return: '\n'.join(lines)
  - 调用: append, get_subagent_config, escape, strip, split, join

#### `ƒ` `_build_subagent_section(max_concurrent: int, max_total: int, *, app_config: AppConfig | None) -> str`  L339
  - _文档首行_（仅供参考）: Build the subagent system prompt section with dynamic subagent limits.
  - 分支数 0，函数体节点数 211；return: f"""<subagent_system>\n**🚀 SUBAGENT MODE ACTIVE - DECOMPOSE, DELEGATE, SYNTHESIZE**\n\nYou are running with subagent capabilities enabled. Your role is to be a **task orchestrator**:\n1. **DECOMPOSE**: Break complex tasks into parallel sub-tasks\n2. **DELEGATE**: Launch multiple subagents simultaneously using parallel `task` calls\n3. **SYNTHESIZE**: Collect and integrate results into a coherent answer\n\n**CORE PRINCIPLE: Complex tasks should be decomposed and distributed across multiple subagents for parallel execution.**\n\n**⛔ HARD CONCURRENCY LIMIT: MAXIMUM {n} `task` CALLS PER RESPONSE. THIS IS NOT OPTIONAL.**\n- Each response, you may include **at most {n}** `task` tool calls. Any excess calls are **silently discarded** by the system — you will lose that work.\n- **Before launching subagents, you MUST count your sub-tasks in your thinking:**\n  - If count ≤ {n}: Launch all in this response.\n  - If count > {n}: **Pick the {n} most important/foundational sub-tasks for this turn.** Save the rest for the next turn.\n- **HARD TOTAL LIMIT: MAXIMUM {total} `task` CALLS PER RUN. THIS IS NOT OPTIONAL.**\n  - Before each batch, count `task` delegations already launched for the current user request/run.\n  - "Work already delegated" may include older thread history; reuse it when helpful, but do not count older runs against this run's {total} total.\n  - Do not launch a new batch if it would exceed {total} total subagents for this run.\n  - When the total limit is reached, synthesize with existing results or continue directly with ordinary tools.\n- **Multi-batch execution** (for >{n} sub-tasks):\n  - Turn 1: Launch sub-tasks 1-{n} in parallel → wait for results\n  - Turn 2: Launch next batch in parallel → wait for results\n  - ... continue until all sub-tasks are complete\n  - Final turn: Synthesize ALL results into a coherent answer\n- **Example thinking pattern**: "I identified 6 sub-tasks. Since the limit is {n} per turn, I will launch the first {n} now, and the rest in the next turn."\n\n**Available Subagents:**\n{available_subagents}\n\n**Your Orchestration Strategy:**\n\n✅ **DECOMPOSE + PARALLEL EXECUTION (Preferred Approach):**\n\nFor complex queries, break them down into focused sub-tasks and execute in parallel batches (max {n} per turn):\n\n**Example 1: "Why is Tencent's stock price declining?" (3 sub-tasks → 1 batch)**\n→ Turn 1: Launch 3 subagents in parallel:\n- Subagent 1: Recent financial reports, earnings data, and revenue trends\n- Subagent 2: Negative news, controversies, and regulatory issues\n- Subagent 3: Industry trends, competitor performance, and market sentiment\n→ Turn 2: Synthesize results\n\n**Example 2: "Compare 5 cloud providers" (5 sub-tasks → multi-batch)**\n→ Turn 1: Launch {n} subagents in parallel (first batch)\n→ Turn 2: Launch remaining subagents in parallel\n→ Final turn: Synthesize ALL results into comprehensive comparison\n\n**Example 3: "Refactor the authentication system"**\n→ Turn 1: Launch 3 subagents in parallel:\n- Subagent 1: Analyze current auth implementation and technical debt\n- Subagent 2: Research best practices and security patterns\n- Subagent 3: Review related tests, documentation, and vulnerabilities\n→ Turn 2: Synthesize results\n\n✅ **USE Parallel Subagents (max {n} per turn) when:**\n- **Complex research questions**: Requires multiple information sources or perspectives\n- **Multi-aspect analysis**: Task has several independent dimensions to explore\n- **Large codebases**: Need to analyze different parts simultaneously\n- **Comprehensive investigations**: Questions requiring thorough coverage from multiple angles\n\n❌ **DO NOT use subagents (execute directly) when:**\n- **Task cannot be decomposed**: If you can't break it into 2+ meaningful parallel sub-tasks, execute directly\n- **Ultra-simple actions**: Read one file, quick edits, single commands\n- **Need immediate clarification**: Must ask user before proceeding\n- **Meta conversation**: Questions about conversation history\n- **Sequential dependencies**: Each step depends on previous results (do steps yourself sequentially)\n\n**CRITICAL WORKFLOW** (STRICTLY follow this before EVERY action):\n1. **COUNT**: In your thinking, list all sub-tasks and count them explicitly: "I have N sub-tasks"\n2. **PLAN BATCHES**: If N > {n}, explicitly plan which sub-tasks go in which batch:\n   - "Batch 1 (this turn): first {n} sub-tasks"\n   - "Batch 2 (next turn): next batch of sub-tasks"\n3. **EXECUTE**: Launch ONLY the current batch (max {n} `task` calls). Do NOT launch sub-tasks from future batches.\n4. **REPEAT**: After results return, launch the next batch. Continue until all batches complete.\n5. **SYNTHESIZE**: After ALL batches are done, synthesize all results.\n6. **Cannot decompose** → Execute directly using available tools ({direct_tool_examples})\n\n**⛔ VIOLATION: Launching more than {n} `task` calls in a single response is a HARD ERROR. The system WILL discard excess calls and you WILL lose work. Always batch.**\n\n**Remember: Subagents are for parallel decomposition, not for wrapping single tasks.**\n\n**How It Works:**\n- The task tool runs subagents asynchronously in the background\n- The backend automatically polls for completion (you don't need to poll)\n- The tool call will block until the subagent completes its work\n- Once complete, the result is returned to you directly\n\n**Usage Example 1 - Single Batch (≤{n} sub-tasks):**\n\n```python\n# User asks: "Why is Tencent's stock price declining?"\n# Thinking: 3 sub-tasks → fits in 1 batch\n\n# Turn 1: Launch 3 subagents in parallel\ntask(description="Tencent financial data", prompt="...", subagent_type="general-purpose")\ntask(description="Tencent news & regulation", prompt="...", subagent_type="general-purpose")\ntask(description="Industry & market trends", prompt="...", subagent_type="general-purpose")\n# All 3 run in parallel → synthesize results\n```\n\n**Usage Example 2 - Multiple Batches (>{n} sub-tasks):**\n\n```python\n# User asks: "Compare AWS, Azure, GCP, Alibaba Cloud, and Oracle Cloud"\n# Thinking: 5 sub-tasks → need multiple batches (max {n} per batch)\n\n# Turn 1: Launch first batch of {n}\ntask(description="AWS analysis", prompt="...", subagent_type="general-purpose")\ntask(description="Azure analysis", prompt="...", subagent_type="general-purpose")\ntask(description="GCP analysis", prompt="...", subagent_type="general-purpose")\n\n# Turn 2: Launch remaining batch (after first batch completes)\ntask(description="Alibaba Cloud analysis", prompt="...", subagent_type="general-purpose")\ntask(description="Oracle Cloud analysis", prompt="...", subagent_type="general-purpose")\n\n# Turn 3: Synthesize ALL results from both batches\n```\n\n**Counter-Example - Direct Execution (NO subagents):**\n\n```python\n{direct_execution_example}\n```\n\n**CRITICAL**:\n- **Max {n} `task` calls per turn** - the system enforces this, excess calls are discarded\n- Only use `task` when you can launch 2+ subagents in parallel\n- Single task = No value from subagents = Execute directly\n- For >{n} sub-tasks, use sequential batches of {n} across multiple turns\n</subagent_system>"""
  - 调用: clamp_subagent_concurrency, clamp_total_subagents_per_run, get_available_subagent_names, _build_available_subagents_description

#### `ƒ` `_get_memory_context(agent_name: str | None, *, app_config: AppConfig | None) -> str`  L728
  - _文档首行_（仅供参考）: Get memory context for injection into system prompt.
  - 分支数 4，函数体节点数 108；return: '', f'<memory>\n{memory_content}\n</memory>\n'
  - 调用: get_memory_config, get_context, get_memory_manager, get_effective_user_id, strip, exception

#### `ƒ` `_get_cached_skills_prompt_section(skill_signature: tuple[tuple[str, str, str, str], ...], disabled_skill_signature: tuple[tuple[str, str, str, str], ...], available_skills_key: tuple[str, ...] | None, container_base_path: str, skill_evolution_section: str) -> str`    @lru_cache(...)  L771
  - 分支数 3，函数体节点数 276；return: f"<skill_system>\nYou have access to skills that provide optimized workflows for specific tasks. Each skill contains best practices, frameworks, and references to additional resources.\n\n**Progressive Loading Pattern:**\n1. When a user query matches a skill's use case, immediately call `read_file` on the skill's main file using the path attribute provided in the skill tag below\n2. Read and understand the skill's workflow and instructions\n3. The skill file contains references to external resources under the same folder\n4. Load referenced resources only when needed during execution\n5. Follow the skill's instructions precisely\n\n**Explicit Slash Skill Activation:**\n- If the user starts a request with `/<skill-name>`, that skill was explicitly requested for the current turn.\n- Follow the activated skill before choosing a general workflow.\n- The runtime injects the activated skill content for explicit slash activations; do not call `read_file` for that SKILL.md again unless the injected skill references supporting resources you need.\n\n**Skills are located at:** {container_base_path}\n{skill_evolution_section}\n{skills_list}\n{disabled_section}\n\n</skill_system>"
  - 调用: join, _render_available_skill, escape, lru_cache

#### `ƒ` `get_skills_prompt_section(available_skills: set[str] | None, *, app_config: AppConfig | None, user_id: str | None, skill_names: frozenset[str] | None) -> str`  L820
  - _文档首行_（仅供参考）: Generate the skills prompt section.
  - 分支数 7，函数体节点数 361；return: get_skill_index_prompt_section(skill_names=skill_names, container_base_path=container_base_path, skill_evolution_section=skill_evolution_section), '', _get_cached_skills_prompt_section(skill_signature, disabled_skill_signature, available_key, container_base_path, skill_evolution_section)
  - 调用: get_app_config, _build_skill_evolution_section, get_skill_index_prompt_section, get_or_new_user_skill_storage, get_or_new_skill_storage, load_skills, get_enabled_skills_for_config, any, tuple, get_container_file_path, sorted, _get_cached_skills_prompt_section

#### `ƒ` `get_agent_soul(agent_name: str | None) -> str`  L890
  - 分支数 1，函数体节点数 37；return: f'<soul>\n{html.escape(soul, quote=False)}\n</soul>\n', ''
  - 调用: load_agent_soul, escape

#### `ƒ` `_build_self_update_section(agent_name: str | None) -> str`  L904
  - _文档首行_（仅供参考）: Prompt block that teaches the custom agent to persist self-updates via update_agent.
  - 分支数 1，函数体节点数 26；return: '', f"""<self_update>\nYou are running as the custom agent **{agent_name}** with a persisted SOUL.md and config.yaml.\n\nWhen the user asks you to update your own description, personality, behaviour, skill set, tool groups, or default model,\nyou MUST persist the change with the `update_agent` tool. Do NOT use `bash`, `write_file`, or any sandbox tool to edit\nSOUL.md or config.yaml — those write into a temporary sandbox/tool workspace and the changes will be lost on the next turn.\n\nRules:\n- Always pass the FULL replacement text for `soul` (no patch semantics). Start from your current SOUL above and apply the user's edits.\n- Only pass the fields that should change. Omit the others to preserve them.\n- Never pass literal strings like `"null"`, `"none"`, or `"undefined"` for unchanged fields.\n- Pass `skills=[]` to disable all skills, or omit `skills` to keep the existing whitelist.\n- After `update_agent` returns successfully, tell the user the change is persisted and will take effect on the next turn.\n</self_update>\n"""

#### `ƒ` `_build_acp_section(*, app_config: AppConfig | None) -> str`  L925
  - _文档首行_（仅供参考）: Build the ACP agent prompt section, only if ACP agents are configured.
  - 分支数 3，函数体节点数 55；return: '', '\n**ACP Agent Tasks (invoke_acp_agent):**\n- ACP agents (e.g. codex, claude_code) run in their own independent workspace — NOT in `/mnt/user-data/`\n- When writing prompts for ACP agents, describe the task only — do NOT reference `/mnt/user-data` paths\n- ACP agent results are accessible at `/mnt/acp-workspace/` (read-only) — use `ls`, `read_file`, or `bash cp` to retrieve output files\n- To deliver ACP output to the user: copy from `/mnt/acp-workspace/<file>` to `/mnt/user-data/outputs/<file>`, then use `present_files`'
  - 调用: get_acp_agents, getattr
  - 反射: getattr (L935)

#### `ƒ` `_build_custom_mounts_section(*, app_config: AppConfig | None) -> str`  L949
  - _文档首行_（仅供参考）: Build a prompt section for explicitly configured sandbox mounts.
  - 分支数 4，函数体节点数 119；return: '', f'\n**Custom Mounted Directories:**\n{mounts_list}\n- If the user needs files outside `/mnt/user-data`, use these absolute container paths directly when they match the requested directory'
  - 调用: get_app_config, exception, append, join

#### `ƒ` `_build_memory_tool_section(*, app_config: AppConfig | None) -> str`  L976
  - _文档首行_（仅供参考）: Build tool-mode memory guidance for the static system prompt.
  - 分支数 3，函数体节点数 61；return: '', '<memory_tool_system>\nMemory is running in tool mode. Use the injected <memory> block as current context, and use the memory tools to keep durable user memory accurate:\n- Call `memory_search` before relying on memory that may be absent, stale, or too broad for the injected context.\n- Call `memory_add` only for stable facts useful in future sessions: explicit user preferences, corrections, personal/work context, or durable project context.\n- Call `memory_update` when an existing fact is outdated or imprecise; prefer updating over adding a near-duplicate.\n- Call `memory_delete` only when a fact is clearly wrong or no longer relevant.\n</memory_tool_system>'
  - 调用: get_memory_config, should_use_memory_tools, exception

#### `ƒ` `apply_prompt_template(subagent_enabled: bool, max_concurrent_subagents: int, max_total_subagents: int | None, *, agent_name: str | None, available_skills: set[str] | None, app_config: AppConfig | None, deferred_names: frozenset[str], mcp_routing_hints_section: str, user_id: str | None, skill_names: frozenset[str] | None) -> str`  L1003
  - 分支数 1，函数体节点数 338；return: SYSTEM_PROMPT_TEMPLATE.format(agent_name=agent_name or 'DeerFlow 2.0', soul=get_agent_soul(agent_name), self_update_section=_build_self_update_section(agent_name), skills_section=skills_section, deferred_tools_section=deferred_tools_section, mcp_routing_hints_section=mcp_routing_hints_section, subagent_section=subagent_section, memory_tool_section=memory_tool_section, subagent_reminder=subagent_reminder, skill_first_reminder=skill_first_reminder, subagent_thinking=subagent_thinking, acp_section=acp_and_mounts_section)
  - 调用: frozenset, clamp_subagent_concurrency, getattr, clamp_total_subagents_per_run, _build_subagent_section, get_skills_prompt_section, get_deferred_tools_prompt_section, _build_acp_section, _build_custom_mounts_section, join, _build_memory_tool_section, format, get_agent_soul, _build_self_update_section
  - 反射: getattr (L1020), getattr (L1021)

## 类
### 类 `_EnabledSkillsRefreshHandle`  L49  @dataclass
- 类/实例变量:
  - `version` = <annotated>
  - `event` = field(default_factory=threading.Event)
  - `error` = None
- 方法:
  #### `m` `wait(self, timeout: float | None) -> bool`  L54
    - 分支数 0，函数体节点数 23；return: self.event.wait(timeout=timeout)
    - 调用: wait

## 文件内调用关系
- `_refresh_enabled_skills_cache_worker` -> _load_enabled_skills_sync
- `_ensure_enabled_skills_cache` -> _start_enabled_skills_refresh_thread
- `_invalidate_enabled_skills_cache` -> _start_enabled_skills_refresh_thread
- `prime_enabled_skills_cache` -> _ensure_enabled_skills_cache
- `warm_enabled_skills_cache` -> wait, _ensure_enabled_skills_cache
- `_get_enabled_skills` -> get_cached_enabled_skills
- `get_cached_enabled_skills` -> _ensure_enabled_skills_cache
- `get_enabled_skills_for_config` -> _get_enabled_skills
- `_render_available_skill` -> _skill_mutability_label
- `clear_skills_system_prompt_cache` -> _invalidate_enabled_skills_cache
- `refresh_skills_system_prompt_cache_async` -> _invalidate_enabled_skills_cache
- `refresh_user_skills_system_prompt_cache_async` -> invalidate_user_skill_cache
- `_build_subagent_section` -> _build_available_subagents_description
- `_get_cached_skills_prompt_section` -> _render_available_skill
- `get_skills_prompt_section` -> _build_skill_evolution_section, get_enabled_skills_for_config, _get_cached_skills_prompt_section
- `apply_prompt_template` -> _build_subagent_section, get_skills_prompt_section, _build_acp_section, _build_custom_mounts_section, _build_memory_tool_section, get_agent_soul, _build_self_update_section
- `_EnabledSkillsRefreshHandle.wait` -> wait

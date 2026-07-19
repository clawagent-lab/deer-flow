# `backend/packages/harness/deerflow/tools/skill_manage_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/skill_manage_tool.py`  ·  行数: 299

**模块文档首行**（仅供参考）: Tool for creating and evolving custom skills.

## 模块概览
- 函数 10 个，类 0 个，模块级常量 2 个

## 功能语义解读

### 模块职责

本模块将“agent 在沙盒运行时内自助管理自定义技能（custom skills）的入口”封装为一个 LangChain tool（`@tool("skill_manage", parse_docstring=True)`）。它面向 agent 自动产出，而非 CLI/人类操作：所有写操作都强制经过安全扫描、（user_id, skill_name）粒度锁、JSONL 历史记录与系统 prompt 缓存刷新，确保 agent 在不脱离沙盒执行上下文的前提下，仅能修改属于当前 user 的 `skills/custom/<name>/` 目录，对公共/遗留技能一律只读。

### 6 个 action 的功能与校验流程

`_skill_manage_impl`（L113）按 `action` 分发，公共前置步骤为：`SkillStorage.validate_skill_name` 校验名称、`resolve_runtime_user_id(runtime)` 解析用户、`_get_lock(user_id, name)` 取锁、`get_or_new_user_skill_storage(user_id)` 取/建存储，再 `async with lock` 进入临界区。

| action | 目标 | 关键校验与副作用 |
|---|---|---|
| `create` | 新建 `SKILL.md` | 拒重名（`custom_skill_exists`）→ `content` 必填 → `validate_skill_markdown_content` → 静态扫描候选（仅含 SKILL.md）→ `_scan_or_raise` → 写盘 → 追加 history（`prev_content=None`）→ 刷新系统 prompt 缓存 |
| `edit` | 整体覆盖 `SKILL.md` | `ensure_custom_skill_is_editable`（拦截只读技能）→ `content` 必填 → 同样的 markdown/静态/动态扫描链 → 先读 `prev_content` 再写 → history |
| `patch` | 对 `SKILL.md` 局部 find/replace | `find`/`replace` 必填 → 读 `prev_content` → `occurrences = prev_content.count(find)`，为 0 报“Patch target not found”→ 若传 `expected_count` 且不匹配则报错 → `replacement_count = expected_count or 1`，用 `str.replace(find, replace, replacement_count)` 生成 `new_content` → 走与 `edit` 相同的扫描链 → 写盘 + history |
| `delete` | 删除整个自定义技能目录 | 无内容扫描，`delete_custom_skill` 接收一个 `history_meta`（scanner 标注 `"Deletion requested."` 的 allow）→ 刷新 prompt 缓存 |
| `write_file` | 写入/覆盖支撑文件（`path`） | `ensure_custom_skill_is_editable` → `path`/`content` 必填 → `ensure_safe_support_path` 防路径穿越 → 读 `prev_content`（不存在则 None）→ **按 `path` 是否在 `scripts/` 下决定 `executable` 标志**（见下）→ 静态扫描候选（若 `skill_storage` 非 None 会 `copytree` 现有目录，再叠加新文件内容）→ `_scan_or_raise` → 写盘 + history |
| `remove_file` | 删除支撑文件 | `ensure_custom_skill_is_editable` → `path` 必填 → `ensure_safe_support_path` → 文件不存在抛 `FileNotFoundError` → 读 `prev_content` 入历史 → `target.unlink`（删除本身不扫描，scanner 仍记 `"Deletion requested."` 的 allow） |

action 兜底：若未命中以上分支，再用 `public_skill_exists`（涵盖 built-in PUBLIC 与 legacy 共享）判断是否只读技能并给出提示，否则抛 `Unsupported action '<action>'`。这意味着只读技能不会因为 action 写错而误进入写路径。

### (user_id, skill_name) 粒度锁 `_skill_locks`

模块级 `_skill_locks: WeakValueDictionary[tuple[str, str], asyncio.Lock]`（L34）以 `(user_id, name)` 为键缓存 `asyncio.Lock`，`_get_lock`（L37）缺失即新建并写回。设计要点：

- **粒度**：锁只覆盖同一用户、同一技能名，避免不同用户/不同技能间相互阻塞。
- **弱引用**：`WeakValueDictionary` 使无引用的锁可被 GC 回收，长期运行下不会无限增长。
- **临界区**：`_skill_manage_impl` 全程在 `async with lock:` 内执行写路径，保证同一技能的并发 action 串行化（读 `prev_content` → 扫描 → 写盘 → 历史 为原子序列）。

### 写操作扫描链：enforce_static_scan + scan_skill_content

每次会修改磁盘内容的 action（create / edit / patch / write_file）都执行两段扫描，**任一 CRITICAL/block 即拒**：

1. **静态扫描**（`_scan_static_candidate_or_raise`，L87）：在 `tempfile.TemporaryDirectory` 下重建候选技能目录——若 `skill_storage` 为 None 则空建目录，否则 `shutil.copytree` 现有自定义技能目录，再把待写文件覆盖到对应 `relative_path`——然后调用 `enforce_static_scan(skill_dir, skill_name=name)`。若抛 `StaticScanBlockedError` 由 `_raise_static_block` 转成带 `findings` JSON 的 `ValueError`；若抛 `StaticScannerError` 由 `_raise_static_scan_failure` 转成 `ValueError`。返回的 `list[StaticFinding]` 会被喂给下一步。
2. **内容扫描**（`_scan_or_raise`，L66）：调 `scan_skill_content(content, executable=..., location=f"{name}/{path}", static_findings=...)`。判定规则：`result.decision == "block"` 一律抛 `ValueError("Security scan blocked the write: ...")`；若 `executable=True` 且 decision 非 `"allow"`（即 warn/review 等）也抛 `ValueError("Security scan rejected executable content: ...")`——对脚本类内容更严格。最终 `scan` dict（`{"decision", "reason"}` 加上 `scan["static_findings"] = static_findings`）写入历史记录的 `scanner` 字段。

`delete` / `remove_file` 不涉及新内容写入磁盘，故不走扫描链，仅在 history 中以 `{"decision": "allow", "reason": "Deletion requested."}` 记录。

### JSONL 历史记录格式

`_history_record`（L54）产出固定字段集合，由 `skill_storage.append_history` 以 JSONL 追加到技能历史文件：

```json
{
  "action": "create|edit|patch|delete|write_file|remove_file",
  "author": "agent",
  "thread_id": "<runtime.context.thread_id 或 config.configurable.thread_id，可能为 null>",
  "file_path": "SKILL.md 或 <support_path>",
  "prev_content": "<变更前全文，新建/删除时为 null>",
  "new_content": "<变更后全文，删除时为 null>",
  "scanner": {"decision": "...", "reason": "...", "static_findings": [...]}
}
```

字段说明：`author` 硬编码 `"agent"`，标识由本 tool 产出（区别于人类编辑）；`thread_id` 来自 `_get_thread_id`，优先 `runtime.context["thread_id"]`，回退 `runtime.config["configurable"]["thread_id"]`，用于跨会话追溯；`scanner` 在写操作里包含动态+静态扫描结论，在删除操作里固定为 allow。

### write_file 对 `scripts/` 的可执行扫描差异

L226：`executable = "scripts/" in path or path.startswith("scripts/")`。当支撑文件位于 `scripts/` 子目录时，`_scan_or_raise` 以 `executable=True` 调用 `scan_skill_content`，此时除了 `block` 之外，`warn`/`review` 等非 `allow` 决定也会被拒绝（见扫描链第 2 步），从而对可执行脚本施加更严格的内容审查；非 scripts 路径下则仅拦截 `block`，允许 warn/review 通过。

### make_sync_tool_wrapper 同步/异步双模式

模块在 L298 通过 `skill_manage_tool.func = make_sync_tool_wrapper(_skill_manage_impl, "skill_manage")` 将异步实现替换为同步可调用版本挂到 `.func`。这是 deerflow 工具层的统一模式（见 `deerflow.tools.sync`）：异步实现 `_skill_manage_impl` 由 `@tool` 装饰器暴露给 LangChain 的异步执行路径，而 `.func` 提供同步入口，使同一 tool 既能跑在异步事件循环里，也能被同步 middleware / 非异步调用点直接调用。所有阻塞 IO（文件读写、`copytree`、`enforce_static_scan`）都通过 `_to_thread`（`asyncio.to_thread` 包装）从事件循环卸载到线程池，符合 deerflow 的 blocking-IO 约束。

### skill_evolution.enabled 总开关 gating

本 tool 不会无条件注册到 agent。在 `backend/packages/harness/deerflow/tools/tools.py` L93-97，`build_agent_tools`（或等价装配函数）会读取 `config.skill_evolution`：仅当 `getattr(skill_evolution_config, "enabled", False)` 为真时，才 `from deerflow.tools.skill_manage_tool import skill_manage_tool` 并 `builtin_tools.append(skill_manage_tool)`。即“技能自进化”能力受配置开关 gating——关闭时 agent 完全看不到该 tool，也无法触发任何自定义技能写操作。这是技能管理功能的全局安全阀。


## 依赖（import）
- 模块: asyncio, json, logging, shutil, tempfile
- `__future__` -> annotations
- `pathlib` -> Path
- `typing` -> Any, NoReturn
- `weakref` -> WeakValueDictionary
- `langchain.tools` -> tool
- `deerflow.agents.lead_agent.prompt` -> refresh_user_skills_system_prompt_cache_async
- `deerflow.runtime.user_context` -> resolve_runtime_user_id
- `deerflow.skills.security_scanner` -> scan_skill_content
- `deerflow.skills.security_static_scanner` -> StaticFinding, StaticScanBlockedError, StaticScannerError, enforce_static_scan
- `deerflow.skills.storage` -> get_or_new_user_skill_storage
- `deerflow.skills.storage.skill_storage` -> SkillStorage
- `deerflow.skills.types` -> SKILL_MD_FILE
- `deerflow.tools.sync` -> make_sync_tool_wrapper
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_skill_locks` = WeakValueDictionary()

## 函数
#### `ƒ` `_get_lock(user_id: str, name: str) -> asyncio.Lock`  L37
  - 分支数 1，函数体节点数 57；return: lock
  - 调用: get, Lock

#### `ƒ` `_get_thread_id(runtime: Runtime | None) -> str | None`  L46
  - 分支数 2，函数体节点数 59；return: None, runtime.context.get('thread_id'), runtime.config.get('configurable', {}).get('thread_id')
  - 调用: get

#### `ƒ` `_history_record(*, action: str, file_path: str, prev_content: str | None, new_content: str | None, thread_id: str | None, scanner: dict[str, Any]) -> dict[str, Any]`  L54
  - 分支数 0，函数体节点数 69；return: {'action': action, 'author': 'agent', 'thread_id': thread_id, 'file_path': file_path, 'prev_content': prev_content, 'new_content': new_content, 'scanner': scanner}

#### `⏵ƒ` `async _scan_or_raise(content: str, *, executable: bool, location: str, static_findings: list[StaticFinding] | None) -> dict[str, Any]`  L66
  - 分支数 2，函数体节点数 108；raise: ValueError(f'Security scan blocked the write: {result.reason}'), ValueError(f'Security scan rejected executable content: {result.reason}')；return: {'decision': result.decision, 'reason': result.reason}
  - 调用: scan_skill_content, ValueError

#### `ƒ` `_raise_static_block(error: StaticScanBlockedError) -> NoReturn`  L75
  - 分支数 0，函数体节点数 42；raise: ValueError(f'{error} Findings: {json.dumps(payload, ensure_ascii=False)}')
  - 调用: ValueError, dumps

#### `ƒ` `_raise_static_scan_failure(name: str, error: StaticScannerError) -> NoReturn`  L83
  - 分支数 0，函数体节点数 25；raise: ValueError(f"Static security scan failed for skill '{name}': {error}")
  - 调用: ValueError

#### `⏵ƒ` `async _scan_static_candidate_or_raise(name: str, updates: dict[str, str], skill_storage: SkillStorage | None) -> list[StaticFinding]`  L87
  - 分支数 4，函数体节点数 167；return: enforce_static_scan(skill_dir, skill_name=name), await _to_thread(_scan_candidate)
  - 调用: TemporaryDirectory, Path, mkdir, copytree, get_custom_skill_dir, items, write_text, enforce_static_scan, _to_thread, _raise_static_block, _raise_static_scan_failure
  - 文件IO: mkdir (L92), mkdir (L97), write_text (L98)

#### `⏵ƒ` `async _to_thread(func, *args, **kwargs)`  L109
  - 分支数 0，函数体节点数 21；可变参数（*args/**kwargs）；return: await asyncio.to_thread(func, *args, **kwargs)
  - 调用: to_thread

#### `⏵ƒ` `async _skill_manage_impl(runtime: Runtime, action: str, name: str, content: str | None, path: str | None, find: str | None, replace: str | None, expected_count: int | None) -> str`  L113
  - _文档首行_（仅供参考）: Manage custom skills under skills/custom/.
  - 分支数 17，函数体节点数 1112；raise: ValueError(f"Custom skill '{name}' already exists."), ValueError('content is required for create.'), ValueError('content is required for edit.'), ValueError('find and replace are required for patch.'), ValueError('Patch target not found in SKILL.md.'), ValueError(f'Expected {expected_count} replacements but found {occurrences}.'), ValueError('path and content are required for write_file.'), ValueError('path is required for remove_file.'), FileNotFoundError(f"Supporting file '{path}' not found for skill '{name}'."), ValueError(f"'{name}' is a read-only skill (built-in or legacy shared). To customise it, create your own version with the same name."), ValueError(f"Unsupported action '{action}'.")；return: f"Created custom skill '{name}'.", f"Updated custom skill '{name}'.", f"Patched custom skill '{name}' ({replacement_count} replacement(s) applied, {occurrences} match(es) found).", f"Deleted custom skill '{name}'.", f"Wrote '{path}' for custom skill '{name}'.", f"Removed '{path}' from custom skill '{name}'."
  - 调用: validate_skill_name, resolve_runtime_user_id, _get_lock, _get_thread_id, get_or_new_user_skill_storage, _to_thread, ValueError, _scan_static_candidate_or_raise, _scan_or_raise, _history_record, refresh_user_skills_system_prompt_cache_async, get_custom_skill_file, count, replace, startswith, FileNotFoundError
  - 文件IO: replace (L189)

#### `⏵ƒ` `async skill_manage_tool(runtime: Runtime, action: str, name: str, content: str | None, path: str | None, find: str | None, replace: str | None, expected_count: int | None) -> str`    @tool(...)  L265
  - _文档首行_（仅供参考）: Manage custom skills under skills/custom/.
  - 分支数 0，函数体节点数 85；return: await _skill_manage_impl(runtime=runtime, action=action, name=name, content=content, path=path, find=find, replace=replace, expected_count=expected_count)
  - 调用: _skill_manage_impl, tool

## 文件内调用关系
- `_scan_static_candidate_or_raise` -> _to_thread, _raise_static_block, _raise_static_scan_failure
- `_skill_manage_impl` -> _get_lock, _get_thread_id, _to_thread, _scan_static_candidate_or_raise, _scan_or_raise, _history_record
- `skill_manage_tool` -> _skill_manage_impl

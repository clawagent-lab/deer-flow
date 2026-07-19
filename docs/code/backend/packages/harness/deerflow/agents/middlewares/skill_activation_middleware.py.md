# `backend/packages/harness/deerflow/agents/middlewares/skill_activation_middleware.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/skill_activation_middleware.py`  ·  行数: 581

**模块文档首行**（仅供参考）: Middleware for skill activation: explicit slash + in-context secret binding.

## 模块概览
- 函数 2 个，类 3 个，模块级常量 3 个

## 功能语义解读

本节基于源码实际控制流（非 docstring 转载）补充深度语义说明，便于审计与跨模块协作。

### 1. 模块职责：LangGraph AgentMiddleware 的双职责

`SkillActivationMiddleware` 继承自 `langchain.agents.middleware.AgentMiddleware`，通过 `@override` 的 `wrap_model_call` / `awrap_model_call` 钩子（L561/L572）拦截每一次模型调用。它在**同一次 hook 入口**内串行承担两件相互独立的事：

- **职责 A — Slash 显式激活**：当用户在最近一条真实用户消息里写了 `/skill-name ...`，中间件从磁盘读取该技能的完整 `SKILL.md`，构造一条隐藏 `HumanMessage` 注入到当次模型请求中，使模型"看到"用户显式选择了该技能及其全部内容。
- **职责 B — 请求级密钥绑定（binding point A+，#3861/#3914）**：无论本次是否发生新激活，都重新计算"本次模型调用应该向 context 注入哪些 secret"，写入 `ACTIVE_SECRETS_CONTEXT_KEY`，供下游 sandbox env 注入使用。

入口 `_handle_model_request`（L349）显式串联：先 `_prepare_model_request`（职责 A，可能短路返回 AIMessage 错误消息），再 `_resolve_secret_bindings`（职责 B）。

### 2. 初始化参数的语义

`__init__`（L90-104）接收四个关键字参数：

- **`available_skills: set[str] | None`**：技能白名单。`None` 表示不限制；非 `None` 时，slash 激活（L147）与密钥绑定（L499）都会拒绝白名单外的技能。这是多 Agent 部署下隔离"每个 agent 只能用部分技能"的核心闸门。
- **`app_config` / `user_id`**：决定 `_storage()`（L106）返回全局 `SkillStorage` 还是 per-user `UserScopedSkillStorage`；后者把 custom 技能放在用户私有目录下。
- **`slash_source_owner_token: str`**（强制非空，L99-100 抛 `ValueError`）：中间件实例私有的 owner token。职责 B 中写入 / 读取 run_context 里的 slash 源路径时都携带此 token（L396、L406）。run_context 是 caller 可合并的 dict，若无 token 签名，caller 就能伪造一条 slash 源记录让任意技能获得免 `secrets-autonomous` 检查的密钥绑定。token 把"谁能声明 slash 源"收紧到"持有本中间件实例的调用链"。

### 3. 激活流程：`_resolve_activation` → `_build_activation_reminder` → 注入隐藏 HumanMessage

`_prepare_model_request`（L311）的激活主路径：

1. **找目标**：`_find_activation_target`（L258）倒序扫描 `request.messages`，定位最近一条真实用户消息（`_is_user_activation_target` → `is_real_user_message`）。命中后还要过两道去重闸（见下节），任一命中即返回 `None` 放弃激活。
2. **解析激活**：`_resolve_activation(text)`（L135）依次执行：
   - `parse_slash_skill_reference(text)` 判定是否 slash 引用，否则返回 `None`（不激活）；
   - `storage.load_skills(enabled_only=False)` 载入全量技能，按 `candidate.name == reference.name` 找目标；未安装 / 已禁用 / 不在白名单分别返回带 `failure_message` 的 `_ActivationResolution`；
   - `resolve_slash_skill` 复算 `container_file_path` 与 `remaining_text`；
   - `_read_skill_content`（L114）读 `SKILL.md`，路径校验优先走 `storage.validate_skill_file_path`（user-scoped 目录不在全局 root 下，`relative_to` 会误拒），否则回退 `resolve()` + `relative_to(skills_root)`；
   - `sha256` 算 `content_hash`；`category == SkillCategory.CUSTOM` 才 `editable=True`（PUBLIC/LEGACY 只读）。
3. **构造提醒**：`_build_activation_reminder`（L182）把 `remaining_text`、完整 `skill_content` 及元数据（name/category/path/sha256/editable）做 `html.escape` 后嵌进 `<slash_skill_activation>...<skill>...<skill_content encoding="xml-escaped">` 的 XML 风格串。`editable` 字段告诉模型该技能能否被用户修改。
4. **注入（不写 state）**：`_make_activation_message`（L546）构造 `HumanMessage`，`additional_kwargs={"hide_from_ui": True, _SLASH_SKILL_ACTIVATION_KEY: True}`，`id=f"{stable_id}__slash_activation"`，若 `target.id` 存在再带上 `_SLASH_SKILL_ACTIVATION_TARGET_ID_KEY=target.id`。`_prepare_model_request` 通过 `messages.insert(target_index, activation_msg)` + `request.override(messages=messages)` 返回新 `ModelRequest`。

**关键事实**：reminder 仅通过 `request.override(messages=...)` 作用于**当次**模型调用，**不写入 graph state**。下一次模型调用重建 `request.messages` 时该 reminder 已消失——这是引入 run_key 去重的直接原因。

### 4. run_key 去重：为什么一次激活在 run 内有效

LangGraph agent 的 tool-loop 会让一次用户 slash 命令在一次 run 内触发**多次**模型调用（模型决策 → tool → 再回模型）。若不去重，每次 model call 都会重复：读盘 `SKILL.md`、注入 reminder、记 "activate" audit 事件。

去重机制由两部分组成，都在 `_find_activation_target` 中（L258-286）：

- **`_has_existing_activation_for_target`**（L208）：检查 reminder 是否还在 `request.messages` 扫描窗口里（针对 reminder 尚未被 tool-loop 抹去的早段调用）。
- **`_already_activated`**（L244）+ **run_context**：检查 `run_context.get(_SLASH_SKILL_ACTIVATION_RUN_KEY) == run_key`。`run_key` 由 `_activation_run_key`（L224）计算：优先 `target.id`（LangGraph 在 state 中分配并保持稳定），无 id 时 fallback 为 `"sha256:" + sha256(content).hexdigest()`。同一个用户 slash 消息 key 不变；新用户 slash 消息（新 id / 新文本）产生新 key，仍会激活。

成功激活后，`_prepare_model_request` 在 L343 用 `run_context[_SLASH_SKILL_ACTIVATION_RUN_KEY] = run_key` 记录。**直接赋值（`=`）而非累积成 set**：`_find_activation_target` 只把"最近一条真实用户消息"当目标，run 内更早的激活一旦被新激活替代就无需保留。注释明确写"do not 'fix' this into a set"。

效果：一次 slash 激活在 run 内只触发**一次**读盘 + 一次 reminder 注入 + 一次 "activate" audit。但 `_resolve_secret_bindings`（职责 B）仍每次执行——它依赖的是 run_context 里的 slash 源路径，不是 reminder。

### 5. `_resolve_secret_bindings`：双源密钥绑定 + 每次重算

`_resolve_secret_bindings`（L357）在每次模型调用时重算注入集，**REPLACE 而非累积**（L424 直接 `context[ACTIVE_SECRETS_CONTEXT_KEY] = injected`，空则 `pop`）。这意味着 skill_context 中被移除的技能、或 caller 停止提供的 secret 值，下一次调用会**自动**失去注入。

**双源 union**（sources 列表 L400-410）：

1. **Slash 源**：若本次有新 `activation`，`write_slash_skill_source_path(context, activation.container_file_path, owner_token=...)` 写入 run_context（L393）。随后 `read_slash_skill_source_path(..., owner_token=...)` 读回，`_resolve_registry_skill(registry, slash_path, require_autonomous=False)` 解析。**Slash 源免检 `secrets-autonomous` opt-out**（显式仪式路径），但仍要 enabled + 声明 secrets + 白名单。
2. **skill_context 源**：`_in_context_secret_sources`（L503）遍历 `request.state["skill_context"]`（ThreadState 中模型此前加载过的技能引用），每条按 `entry.get("path")` 调 `_resolve_registry_skill(..., require_autonomous=True)`。**此源要求 `secrets_autonomous=True`**——技能 frontmatter 可用 `secrets-autonomous: false` 退出自动密钥注入。

两源都通过 `_resolve_registry_skill` 按**路径**匹配 live registry 中的 `Skill`。registry 由 `_load_skill_registry_by_path`（L447）**每次调用重新加载**（不缓存）：操作员通过 `extensions_config` 禁用技能不会改 `SKILL.md` 的 mtime，基于 mtime 的缓存会错过 enable/disable 切换并继续注入已禁用技能的密钥——为"立即吊销"的安全特性牺牲速度。代价可控：L402 只在 caller 真的带了 `request_secrets` 时才触发。

注入值的来源严格限定：`extract_request_secrets(context)` 来自 caller 的 `context.secrets`，**绝不来自宿主环境**；`env_policy.build_sandbox_env` 在注入前清理宿主环境变量，技能无法借机收割宿主平台凭据。secret **值**永不记日志，audit journal 只记名称（`audit_state` 的 `secrets` 字段是 sorted name 列表）。

audit 去重（L433-438）：构造的 `audit_state` 与 `context[_SECRETS_BINDING_AUDIT_KEY]` 比对，相同则跳过，避免每次调用重复记 audit；首次全空也跳过；missing 项会 `logger.warning` 并经 `_record_secret_binding` 写 journal。

### 6. `_resolve_registry_skill`：按路径非按名字匹配（防 confused deputy）

`_resolve_registry_skill`（L475-501）的核心安全约束是**严格用 `posixpath.normpath(path)` 作 key 查 registry dict，绝不回退到 by-name 匹配**。

设计动因（confused deputy 防御）：DeerFlow 允许 custom skill 同名 shadow public/legacy skill，`load_skills` 按名字去重时 custom 胜出。若用名字 fallback，一个引用 `public/foo` 路径的来源就可能绑定到 `custom/foo` 的密钥——而 `custom/foo` 可能由其他用户写入，这就构成 confused deputy：攻击者用同名 custom 技能"截胡"本应给 public 技能的密钥。按路径匹配让"路径不对应"直接 bind nothing。

路径解析失败的处置方向是 **fail closed**（返回 `None` → 该源此调用绑定 nothing）：这也覆盖 caller 伪造路径的场景（#3938），以及 registry 读取失败时 `_load_skill_registry_by_path` 返回 `None` 导致两源都 bind nothing 的场景（L403/410 守卫）——用"该次调用放弃注入"换取"不信任陈旧 caller 数据"。

闸门集合（L492-500）：skill 必须 `enabled`、声明非空 `required_secrets`、白名单匹配（`available_skills is not None` 时 `skill.name in self._available_skills`）；`require_autonomous=True` 时额外要求 `skill.secrets_autonomous` 为真。slash 路径传 `False` 走显式仪式豁免，in-context 路径传 `True` 强制 opt-in。

## 依赖（import）
- 模块: asyncio, hashlib, html, logging, posixpath, uuid
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `dataclasses` -> dataclass
- `pathlib` -> Path
- `typing` -> TYPE_CHECKING, override
- `langchain.agents.middleware` -> AgentMiddleware
- `langchain.agents.middleware.types` -> ModelRequest, ModelResponse
- `langchain_core.messages` -> AIMessage, HumanMessage
- `deerflow.runtime.secret_context` -> _SECRETS_BINDING_AUDIT_KEY, _SLASH_SKILL_ACTIVATION_RUN_KEY, ACTIVE_SECRETS_CONTEXT_KEY, extract_request_secrets, read_slash_skill_source_path, write_slash_skill_source_path
- `deerflow.skills.slash` -> parse_slash_skill_reference, resolve_slash_skill
- `deerflow.skills.storage` -> get_or_new_skill_storage, get_or_new_user_skill_storage
- `deerflow.skills.storage.skill_storage` -> SkillStorage
- `deerflow.skills.types` -> SKILL_MD_FILE, SecretRequirement, Skill, SkillCategory
- `deerflow.utils.messages` -> get_original_user_content_text, is_real_user_message

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_SLASH_SKILL_ACTIVATION_KEY` = 'slash_skill_activation'
- `_SLASH_SKILL_ACTIVATION_TARGET_ID_KEY` = 'slash_skill_activation_target_id'

## 函数
#### `ƒ` `is_slash_skill_activation_reminder(message: object) -> bool`  L78
  - _文档首行_（仅供参考）: Return whether a message is hidden slash-skill activation context.
  - 分支数 0，函数体节点数 31；return: isinstance(message, HumanMessage) and bool(message.additional_kwargs.get(_SLASH_SKILL_ACTIVATION_KEY))
  - 调用: isinstance, bool, get

#### `ƒ` `_is_user_activation_target(message: object) -> bool`  L83
  - 分支数 0，函数体节点数 13；return: is_real_user_message(message)
  - 调用: is_real_user_message

## 类
### 类 `_Activation`  L61  @dataclass(...)
- 类/实例变量:
  - `skill_name` = <annotated>
  - `category` = <annotated>
  - `container_file_path` = <annotated>
  - `skill_content` = <annotated>
  - `content_hash` = <annotated>
  - `remaining_text` = <annotated>
  - `editable` = <annotated>
  - `required_secrets` = ()

### 类 `_ActivationResolution`  L73  @dataclass(...)
- 类/实例变量:
  - `activation` = None
  - `failure_message` = None

### 类 `SkillActivationMiddleware`  L87
- 继承: AgentMiddleware
- _文档首行_: Inject full SKILL.md content when the user explicitly types /skill-name.
- 方法:
  #### `st` `_read_skill_content(skill_file: Path, skills_root: Path, *, storage: SkillStorage | None) -> str`    @staticmethod  L114
    - 分支数 4，函数体节点数 124；raise: ValueError(f'Expected {SKILL_MD_FILE}, got {skill_file.name}'), ValueError('Resolved skill file must stay within the configured skills root.'), FileNotFoundError(resolved_file)；return: resolved_file.read_text(encoding='utf-8')
    - 调用: ValueError, hasattr, validate_skill_file_path, resolve, relative_to, is_file, FileNotFoundError, read_text
  - 文件IO: read_text (L133)
  - 反射: hasattr (L122)
  #### `st` `_build_activation_reminder(activation: _Activation) -> str`    @staticmethod  L182
    - 分支数 0，函数体节点数 146；return: f'<slash_skill_activation>\nThe user explicitly activated the `{escaped_skill_name}` skill for this turn.\nTreat the task text as:\n<user_request>\n{escaped_user_request}\n</user_request>\n\nFollow this skill before choosing a general workflow. Load supporting resources from the same skill directory only when needed.\n\n<skill name="{escaped_skill_name}" category="{escaped_category}" path="{escaped_path}" sha256="{escaped_content_hash}" editable="{editable_str}">\n<skill_content encoding="xml-escaped">\n{escaped_skill_content}\n</skill_content>\n</skill>\n</slash_skill_activation>'
    - 调用: escape
  #### `st` `_has_existing_activation_for_target(messages: list, target_index: int, target: HumanMessage) -> bool`    @staticmethod  L208
    - 分支数 5，函数体节点数 103；return: False, True, is_slash_skill_activation_reminder(previous)
    - 调用: is_slash_skill_activation_reminder, get
  #### `st` `_activation_run_key(target: HumanMessage) -> str`    @staticmethod  L224
    - _文档首行_（仅供参考）: Stable identity for a user slash message, used to activate once per run.
    - 分支数 1，函数体节点数 53；return: target.id, 'sha256:' + hashlib.sha256(content.encode('utf-8')).hexdigest()
    - 调用: get_original_user_content_text, hexdigest, sha256, encode
  #### `st` `_run_context(request: ModelRequest) -> dict | None`    @staticmethod  L238
    - 分支数 0，函数体节点数 44；return: context if isinstance(context, dict) else None
    - 调用: getattr, isinstance
  - 反射: getattr (L239), getattr (L240)
  #### `st` `_already_activated(run_context: dict | None, run_key: str) -> bool`    @staticmethod  L244
    - _文档首行_（仅供参考）: Whether ``run_key`` was already recorded as activated earlier in this run.
    - 分支数 0，函数体节点数 38；return: isinstance(run_context, dict) and run_context.get(_SLASH_SKILL_ACTIVATION_RUN_KEY) == run_key
    - 调用: isinstance, get
  #### `st` `_record_activation(request: ModelRequest, activation: _Activation, *, hook: str) -> None`    @staticmethod  L289
    - 分支数 2，函数体节点数 108；return: None
    - 调用: getattr, isinstance, get, record_middleware, debug
  - 反射: getattr (L290), getattr (L291)
  #### `st` `_record_secret_binding(context: dict, audit_state: dict, *, hook: str) -> None`    @staticmethod  L530
    - 分支数 2，函数体节点数 60；return: None
    - 调用: get, record_middleware, debug
  #### `st` `_make_activation_message(target: HumanMessage, activation_content: str) -> HumanMessage`    @staticmethod  L546
    - 分支数 1，函数体节点数 70；return: HumanMessage(content=activation_content, id=f'{stable_id}__slash_activation', additional_kwargs=additional_kwargs)
    - 调用: str, uuid4, HumanMessage
  #### `m` `__init__(self, *, available_skills: set[str] | None, app_config: AppConfig | None, user_id: str | None, slash_source_owner_token: str) -> None`  L90
    - 分支数 1，函数体节点数 98；raise: ValueError('slash_source_owner_token must be a non-empty string')
    - 调用: __init__, super, isinstance, ValueError, set
  #### `m` `_storage(self) -> SkillStorage`  L106
    - 分支数 2，函数体节点数 47；return: get_or_new_user_skill_storage(self._user_id, app_config=self._app_config), get_or_new_skill_storage(app_config=self._app_config), get_or_new_skill_storage()
    - 调用: get_or_new_user_skill_storage, get_or_new_skill_storage
  #### `m` `_resolve_activation(self, text: str) -> _ActivationResolution | None`  L135
    - 分支数 6，函数体节点数 328；return: None, _ActivationResolution(failure_message=f'Skill `/{reference.name}` is not installed.'), _ActivationResolution(failure_message=f'Skill `/{reference.name}` is installed but disabled. Enable it before using slash activation.'), _ActivationResolution(failure_message=f'Skill `/{reference.name}` is not available for this agent.'), _ActivationResolution(failure_message=f'Skill `/{reference.name}` could not be resolved.'), _ActivationResolution(failure_message=f'Skill `/{reference.name}` could not be loaded safely. Please check the skill installation.'), _ActivationResolution(activation=_Activation(skill_name=resolved.skill.name, category=str(resolved.skill.category), container_file_path=resolved.container_file_path, skill_content=skill_content, content_hash=content_hash, remaining_text=resolved.remaining_text, editable=editable, required_secrets=tuple(resolved.skill.required_secrets or ())))
    - 调用: parse_slash_skill_reference, _storage, load_skills, next, _ActivationResolution, resolve_slash_skill, get_container_root, _read_skill_content, get_skills_root_path, exception, hexdigest, sha256, encode, _Activation, str, tuple
  #### `m` `_find_activation_target(self, messages: list, *, run_context: dict | None) -> tuple[int, HumanMessage, _ActivationResolution, str] | None`  L258
    - 分支数 6，函数体节点数 180；return: None, (target_index, target, resolution, run_key)
    - 调用: next, range, len, _is_user_activation_target, _has_existing_activation_for_target, _activation_run_key, _already_activated, get_original_user_content_text, _resolve_activation
  #### `m` `_prepare_model_request(self, request: ModelRequest, *, hook: str) -> tuple[ModelRequest | AIMessage | None, _Activation | None]`  L311
    - 分支数 4，函数体节点数 217；return: (None, None), (AIMessage(content=resolution.failure_message), None), (request.override(messages=messages), activation)
    - 调用: _run_context, _find_activation_target, list, AIMessage, info, _record_activation, _make_activation_message, _build_activation_reminder, insert, override
  #### `m` `_handle_model_request(self, request: ModelRequest, *, hook: str) -> ModelRequest | AIMessage`  L349
    - 分支数 1，函数体节点数 72；return: prepared, effective
    - 调用: _prepare_model_request, isinstance, _resolve_secret_bindings
  #### `m` `_resolve_secret_bindings(self, request: ModelRequest, activation: _Activation | None, *, hook: str) -> None`  L357
    - _文档首行_（仅供参考）: Recompute the per-run secret injection set (binding point A+, #3861/#3914).
    - 分支数 13，函数体节点数 452；return: None
    - 调用: getattr, isinstance, write_slash_skill_source_path, extract_request_secrets, _load_skill_registry_by_path, read_slash_skill_source_path, _resolve_registry_skill, append, tuple, extend, _in_context_secret_sources, set, add, setdefault, pop, sorted, items, get, warning, join（+1）
  - 反射: getattr (L383), getattr (L384)
  #### `m` `_load_skill_registry_by_path(self) -> dict[str, Skill] | None`  L447
    - _文档首行_（仅供参考）: Load the live skill registry keyed by normalized container file path.
    - 分支数 1，函数体节点数 78；return: None, {posixpath.normpath(skill.get_container_file_path(container_root)): skill for skill in skills}
    - 调用: _storage, load_skills, get_container_root, exception, normpath, get_container_file_path
  #### `m` `_resolve_registry_skill(self, registry: dict[str, Skill], path: object, *, require_autonomous: bool) -> Skill | None`  L475
    - _文档首行_（仅供参考）: Resolve a container path to a live registry skill eligible for secret
    - 分支数 4，函数体节点数 120；return: None, skill
    - 调用: isinstance, get, normpath
  #### `m` `_in_context_secret_sources(self, request: ModelRequest, registry: dict[str, Skill]) -> list[tuple[str, tuple[SecretRequirement, ...]]]`  L503
    - _文档首行_（仅供参考）: Map ``ThreadState.skill_context`` entries to declared-secret sources.
    - 分支数 4，函数体节点数 194；return: [], sources
    - 调用: getattr, get, set, isinstance, _resolve_registry_skill, add, append, tuple
  - 反射: getattr (L511)
  #### `m` `wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse | AIMessage`    @override  L561
    - 分支数 1，函数体节点数 56；return: prepared, handler(prepared)
    - 调用: _handle_model_request, isinstance, handler
  #### `⏵m` `async awrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], Awaitable[ModelResponse]]) -> ModelResponse | AIMessage`    @override  L572
    - 分支数 1，函数体节点数 66；return: prepared, await handler(prepared)
    - 调用: to_thread, isinstance, handler

## 文件内调用关系
- `SkillActivationMiddleware.__init__` -> __init__
- `SkillActivationMiddleware._resolve_activation` -> _storage, _read_skill_content
- `SkillActivationMiddleware._has_existing_activation_for_target` -> is_slash_skill_activation_reminder
- `SkillActivationMiddleware._find_activation_target` -> _is_user_activation_target, _has_existing_activation_for_target, _activation_run_key, _already_activated, _resolve_activation
- `SkillActivationMiddleware._prepare_model_request` -> _run_context, _find_activation_target, _record_activation, _make_activation_message, _build_activation_reminder
- `SkillActivationMiddleware._handle_model_request` -> _prepare_model_request, _resolve_secret_bindings
- `SkillActivationMiddleware._resolve_secret_bindings` -> _load_skill_registry_by_path, _resolve_registry_skill, _in_context_secret_sources, _record_secret_binding
- `SkillActivationMiddleware._load_skill_registry_by_path` -> _storage
- `SkillActivationMiddleware._in_context_secret_sources` -> _resolve_registry_skill
- `SkillActivationMiddleware.wrap_model_call` -> _handle_model_request

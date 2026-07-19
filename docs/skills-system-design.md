# DeerFlow Skills 系统设计文档

> 本文是对 DeerFlow 项目中 Skills 系统实现的整理性设计文档，面向希望理解或扩展技能子系统的维护者。
> 代码是权威契约；当本文与代码冲突时，以代码为准并请同步更新本文。
>
> 说明：项目中 "hermes" 仅在 `backend/packages/harness/deerflow/sandbox/env_policy.py:11` 的注释里作为
> 环境变量 blocklist 的借鉴对象出现（"hermes's fixed provider blocklist"），并非实际集成。
> 故本文实质即 Skills 系统的设计整理。

---

## 一、总览

Skills 是 DeerFlow 的"过程化记忆"：以 `SKILL.md` 为入口的可复用任务包，支持发现、加载、激活、
安装、审查、安全扫描、按用户隔离。代码分布在三层：

```
skills/                                  # 技能内容（数据层）
├── public/                              # 内置公共技能（只读，随仓库提交）
└── custom/                              # 用户自定义技能（gitignore）

backend/packages/harness/deerflow/skills/  # 核心框架（harness 层）
├── types.py           Skill / SkillCategory / SecretRequirement 数据类
├── parser.py          SKILL.md frontmatter 解析
├── catalog.py         延迟发现用的不可变搜索目录
├── describe.py        describe_skill 工具构造器
├── slash.py           /skill-name 激活语法解析
├── installer.py       .skill ZIP 安装（安全提取）
├── validation.py      frontmatter 校验
├── permissions.py     沙盒可读权限
├── frontmatter.py     共享 frontmatter 助手
├── package_paths.py   包路径工具
├── tool_policy.py     allowed-tools 策略
├── security_scanner.py        LLM 扫描器
├── security_static_scanner.py 静态扫描器
├── storage/           存储抽象层（见第四节）
├── skillscan/         原生确定性扫描器（models / orchestrator）
└── review/            技能包只读审查核心（analyzer / readers / renderer / digest / cli ...）

backend/packages/harness/deerflow/agents/middlewares/   # 运行时激活链
├── skill_activation_middleware.py   /slash 激活 + 密钥绑定
├── skill_tool_policy_middleware.py  allowed-tools 动态收窄
└── skill_context.py                 已加载技能的持久上下文捕获

backend/packages/harness/deerflow/tools/
├── skill_manage_tool.py                        # agent 用的 skill_manage 工具
└── builtins/review_skill_package_tool.py       # 技能包审查工具

backend/app/gateway/routers/skills.py           # Gateway REST 路由
```

---

## 二、数据模型与 SKILL.md 协议

### Skill 数据类（`skills/types.py`）

| 字段 | 位置 | 说明 |
|------|------|------|
| `name` / `description` | `types.py:39` | 必填，触发依据 |
| `license` | `types.py:44` | 可选 |
| `skill_dir` / `skill_file` / `relative_path` | `types.py:45-47` | 文件位置 |
| `category` | `types.py:48` | `PUBLIC` / `CUSTOM` / `LEGACY`（`types.py:10`）|
| `allowed_tools` | `types.py:49` | 可选工具白名单 |
| `enabled` | `types.py:50` | 由 extensions_config 注入 |
| `required_secrets` | `types.py:51` | `tuple[SecretRequirement, ...]`（#3861 请求级密钥）|
| `secrets_autonomous` | `types.py:55` | 是否允许自主加载时绑定密钥，默认 true |

`SkillCategory`（`types.py:10-22`）三类：
- `PUBLIC`：随平台内置，只读
- `CUSTOM`：用户自创，可编辑/删除
- `LEGACY`：用户隔离迁移前的全局自定义技能，只读可见，沙盒挂载在 `/mnt/skills/legacy/<name>/`

### SKILL.md 格式

YAML frontmatter + Markdown 正文：

```yaml
---
name: data-analysis            # 必填，hyphen-case
description: ...               # 必填，触发依据
license: ...                   # 可选
allowed-tools: [bash, read_file]   # 可选
required-secrets: ***      # 可选，#3861
  - API_TOKEN
  - {name: DB_PASSWORD, optional: false}
secrets-autonomous: ***           # 可选，#3914
---
# 正文：工作流、示例、参数说明
```

支持目录结构：
```
skill-name/
├── SKILL.md          # 必需
├── scripts/          # 可执行脚本
├── references/       # 按需加载的文档
├── templates/        # 模板
└── assets/           # 输出素材
```

frontmatter 解析在 `parser.py::parse_skill_file`（`parser.py:117`），子解析器：
- `parse_allowed_tools`（`parser.py:41`）
- `parse_required_secrets`（`parser.py:64`）：接受字符串或 `{name, optional}` 映射，非法名以警告丢弃
- `parse_secrets_autonomous`（`parser.py:101`）：非布尔值 fail-closed 到 `false`

### 公共技能清单（`skills/public/`，共 20 个）

data-analysis, deep-research, skill-creator, skill-reviewer,
image/music/video/podcast/ppt/newsletter-generation,
github-deep-research, systematic-literature-review,
chart-visualization, frontend-design, code-documentation,
consulting-analysis, academic-paper-review, claude-to-deerflow,
bootstrap, find-skills, surprise-me, web-design-guidelines,
vercel-deploy-claimable。

---

## 三、发现与加载（两种模式）

配置开关：`skills.deferred_discovery`（默认 `false`）。

### Legacy / 默认（`deferred_discovery: false`）

所有启用技能的完整元数据 + 容器路径注入系统提示的 `<available_skills>` 块。

### 延迟发现（`deferred_discovery: true`）

- 系统提示只放紧凑的 `<skill_index>`（仅名字），保持 prefix-cache 友好
- agent 调用 `describe_skill` 工具按需取元数据
- 再用 `read_file` 加载 `SKILL.md` 正文

支持模块：
- `catalog.py::SkillCatalog`（`catalog.py:42`）：不可变、纯搜索。`MAX_RESULTS = 5`（`catalog.py:23`）
  - 查询语法（`catalog.py:59` `search`）：
    - `select:a,b`：精确匹配，不截断
    - `+prefix query`：前缀过滤 + 正则排序
    - 自由文本正则：最多 5 条，名字命中权重高于描述命中
- `describe.py::build_describe_skill_tool(catalog)`：闭包构造 `describe_skill` 工具
- `build_skill_search_setup(...)` 产出 `SkillSearchSetup(describe_skill_tool, skill_names)`，接入 LangGraph agent 工厂（`agent.py`）与嵌入式客户端（`client.py`）

---

## 四、存储层（模板方法模式）

`storage/skill_storage.py::SkillStorage`（抽象基类）用模板方法组合原子操作，
子类只实现少量存储介质相关的原子方法。

### 三类后端

| 层级 | 实现 | 布局 |
|------|------|------|
| 全局本地 | `LocalSkillStorage`（`storage/local_skill_storage.py:29`）| `<root>/{public,custom}/<name>/SKILL.md`；历史在 `custom/.history/<name>.jsonl` |
| 用户隔离 | `UserScopedSkillStorage`（`storage/user_scoped_skill_storage.py:49`）| 自定义技能在 `{base}/users/{user_id}/skills/custom/`；公共技能仍读全局；全局 `skills/custom/` 作为 `LEGACY` 只读回退 |
| 测试 | mock | -- |

### UserScopedSkillStorage 布局（`user_scoped_skill_storage.py:1-27`）

```
<host_root>/public/<name>/SKILL.md            ← 全局，只读
<user_custom_root>/<name>/SKILL.md             ← 按用户，读写
<user_custom_root>/.history/<name>.jsonl       ← 按用户历史
<user_skills_root>/_skill_states.json          ← 按用户启用状态
<global_custom_root>/<name>/SKILL.md           ← legacy 回退，只读
```

启用状态隔离：CUSTOM / LEGACY 状态存于按用户的 `_skill_states.json`（`user_scoped_skill_storage.py:87`），
PUBLIC 状态仍全局存于 `extensions_config.json`，防同名自定义技能跨用户泄漏状态。
用户首次创建自定义技能后，按用户目录存在，全局 `custom/` 回退消失（shadow-mount 语义）。

### 关键方法

- `validate_skill_name`（`skill_storage.py:37`）：hyphen-case，≤64 字符
- `ensure_safe_support_path`（`skill_storage.py:81`）：支持文件必须落在 `references/templates/scripts/assets/` 之一，禁 `..`
- `load_skills(enabled_only)`（`skill_storage.py:242`）：**每次调用都重扫磁盘 + 重读 extensions_config**，使启用/禁用立即生效，无 TTL 缓存
- `ensure_custom_skill_is_editable`（`skill_storage.py:281`）：只有 CUSTOM 可编辑，PUBLIC/LEGACY 只读
- `install_skill_from_archive` / `ainstall_skill_from_archive`（`skill_storage.py:159`）：ZIP 安装

抽象原子操作（子类必须实现）：`get_skills_root_path`、`_iter_skill_files`、`read_custom_skill`、
`write_custom_skill`、`ainstall_skill_from_archive`、`delete_custom_skill`、
`custom_skill_exists`、`public_skill_exists`、`append_history`、`read_history`
（见 `skill_storage.py:108-198`）。

存储实例按 `(app_config, user_id)` 单例缓存。`POST /api/skills/reload` 是管理员进程级失效钩子。

---

## 五、激活机制（三条路径）

### 1. /slash 激活（`slash.py` + `skill_activation_middleware.py`）

语法：`/skill-name task`，严格正则（`slash.py:18`）：
```
^/([a-z0-9]+(?:-[a-z0-9]+)*)(?:\s+|$)
```

保留命令（`slash.py:17`，不会被当技能）：
`bootstrap / goal / help / memory / models / new / status`

解析与解析结果（`slash.py:38` `parse_slash_skill_reference`、`slash.py:52` `resolve_slash_skill`）：
- 拒绝前导空白、缺失分隔符、保留命令、已禁用技能、自定义 agent 白名单外的技能

中间件 `SkillActivationMiddleware`（`skill_activation_middleware.py:87`）：
- `_resolve_activation`（`skill_activation_middleware.py:135`）：校验 enabled + allowlist，读取 SKILL.md 内容并算 sha256
- `_build_activation_reminder`（`skill_activation_middleware.py:182`）：把完整 SKILL.md 内容包成 `<slash_skill_activation>` 隐藏消息注入当前轮
- 一次激活在整个 run 内有效：用 `run_key`（消息 id 或文本 sha256）去重，避免 tool-loop 每次模型调用重复读盘（`skill_activation_middleware.py:224` `_activation_run_key`）
- CUSTOM 可编辑；PUBLIC/LEGACY 只读（`skill_activation_middleware.py:167`）

前后端解析契约由 `contracts/slash_skill_contract.json` 固定，`tests/test_slash_skill_contract.py` 与前端 `slash-contract.test.ts` 双向锁定。

### 2. 自主 / 上下文激活（`skill_context.py` + `DurableContextMiddleware`）

- agent 用 `read_file` 读 `SKILL.md` 后，`skill_context.py` 解析路径并记录 `(name, path, description)` 到 `ThreadState.skill_context`
- 在 summarization 压缩消息前捕获，避免丢失
- 每次模型调用重新解析 live registry 按路径校验（enabled + allowlist）

### 3. 安装时激活

`POST /api/skills/install` 从 `.skill` ZIP 解包到 `custom/`（见第八节路由）。

---

## 六、工具策略（allowed-tools）

`skill_tool_policy_middleware.py`：只在真正激活后动态收窄工具集。

- **slash 激活**是 run-scoped 权威源，压制 `skill_context` 作为策略源（防止后读的技能扩大显式权限）
- **自主捕获的技能**在无 slash 源时用并集语义
- `tool_search` / `describe_skill` 始终保留为发现基础设施
- 每次模型调用重载完整 live registry，enable/disable 和 frontmatter 编辑立即生效
- 子代理（subagent）静态过滤：因其配置技能在会话启动时全部加载

这是"best-effort 行为收窄"，不是硬安全边界。

---

## 七、skill_manage 工具（agent 自助管理）

`tools/skill_manage_tool.py`：agent 在沙盒内通过此工具管理自定义技能。

### Actions（`skill_manage_tool.py:141-239`）

| action | 作用 |
|--------|------|
| `create` | 新建技能（写 SKILL.md）|
| `edit` | 整体替换 SKILL.md |
| `patch` | find/replace 局部替换，可带 `expected_count` |
| `delete` | 删除技能 |
| `write_file` | 写支持文件（scripts/references/templates/assets/）|
| `remove_file` | 删支持文件 |

### 特性

- 按 `(user_id, skill_name)` 加锁防跨用户阻塞（`skill_manage_tool.py:34` `_skill_locks`）
- 每次写操作都跑 `scan_skill_content` + `enforce_static_scan`（静态扫描）
- 写完追加 JSONL 历史：`action / author / thread_id / file_path / prev_content / new_content / scanner`（`skill_manage_tool.py:54` `_history_record`）
- 写完异步刷新该用户的系统提示技能缓存（`refresh_user_skills_system_prompt_cache_async`）
- 写入路径强制落在 `references/templates/scripts/assets/` 之一

**关键约束**（见 `skills/public/skill-creator/SKILL.md`）：
在 DeerFlow 沙盒里绝不能用普通 `write_file` 创建技能文件（会落到 `/mnt/user-data/outputs/` 对未来会话不可见），必须用 `skill_manage`。

---

## 八、Gateway REST 路由（`app/gateway/routers/skills.py`）

路由前缀 `/api`，tag `skills`（`skills.py:31`）。管理类操作需 `require_admin_user`（`skills.py:11`）。

| 方法 | 路径 | 鉴权 | 作用 |
|------|------|------|------|
| GET | `/api/skills` | -- | 列出所有技能（name/description/license/category/enabled/editable）|
| GET | `/api/skills/custom` | -- | 列出自定义技能 |
| GET | `/api/skills/custom/{name}` | admin | 读取自定义技能内容 |
| PUT | `/api/skills/custom/{name}` | admin | 编辑自定义技能 |
| DELETE | `/api/skills/custom/{name}` | admin | 删除自定义技能 |
| GET | `/api/skills/custom/{name}/history` | admin | 历史记录 |
| POST | `/api/skills/custom/{name}/rollback` | admin | 回滚 |
| POST | `/api/skills/install` | admin | 从 `.skill` ZIP 安装 |
| POST | `/api/skills/reload` | admin | 进程级缓存失效 |
| GET | `/api/skills/...`（启用状态相关）| -- | 见 `skills.py:390+` |
| PUT | `/api/skills/...`（启用状态相关）| -- | 见 `skills.py:413+` |

`POST /api/skills/reload` 是 admin-only、进程级失效钩子，适用于可信的 MinIO/NFS/CSI 直接挂载写入后失效本进程缓存。
`SkillStorage` 实例不缓存目录——`load_skills()` 每次扫描——所以该路由清空 `(app_config, user_id)` 单例缓存与渲染提示段的 LRU，
并等待最多共享刷新超时时间的 off-loop single-flight 刷新。每个 Uvicorn worker / K8s Pod 需分别触发。

---

## 九、安全扫描（两层）

### SkillScan（`skills/skillscan/`，原生确定性扫描器）

- 安装/写入前离线运行，在 LLM 扫描器之前
- 结构化 findings：`rule_id, severity, file, line, message, remediation`（脱敏 evidence）
- `CRITICAL` 阻断，`warn` 传给 `scan_skill_content()`
- `scan_archive_preflight()` / `scan_skill_dir()` 纯同步，dispatch 出事件循环
- `enforce_static_scan()` 应用阻断策略 + `skill_scan.enabled` 总开关
- Phase 1 规则定义在 `skillscan/orchestrator.py` 的 Python 常量里，不依赖 Semgrep/OpenGrep
- 不向核心路径引入 YAML 规则引擎依赖

### LLM 扫描器（`security_scanner.py::scan_skill_content`）

- 接收静态 findings 作为输入
- 决策：`allow / warn / block`
- 可执行文件（scripts/）要求 `allow`，否则拒绝

### 安装路径安全（`installer.py::safe_extract_skill_archive`，`installer.py:117`）

- 拒绝绝对路径 / `..` 遍历（`installer.py:64` `is_unsafe_zip_member`）
- 拒绝符号链接条目
- 拒绝可执行二进制（ELF/PE/Mach-O 魔数，`installer.py:88` `is_executable_binary_prefix`）
- 总大小上限 512 MB（`installer.py:120` `max_total_size`）
- 条目数上限 4096（`installer.py:121` `max_entries`），防 zip bomb
- 嵌套 `SKILL.md` 不允许（包边界）

异常类型：`SkillAlreadyExistsError`、`SkillSecurityScanError`（`installer.py:48-62`）。

---

## 十、请求级密钥（required-secrets，#3861 / #3914）

让调用方按请求传入短命凭据（如 ERP token）给技能脚本，值不进 prompt / 参数 / 命令串 / trace。

### 链路

1. **声明**：frontmatter `required-secrets: [NAME]` 或 `{name, optional}` → `parser.py:64` `parse_required_secrets`
2. **携带**：调用方放 `context.secrets`（不在消息里）→ `runtime/secret_context.py`
3. **绑定**（`skill_activation_middleware.py:357` `_resolve_secret_bindings`）：每次模型调用重算注入集，两源并集后 **REPLACE**：
   - **slash 源**：run 内最近一次 `/skill` 激活（只存容器路径，不存声明的密钥）
   - **上下文源**：`ThreadState.skill_context` 里的技能
   - 两者都按**规范化容器路径**解析 live registry 技能（`skill_activation_middleware.py:475` `_resolve_registry_skill`，不按名字，防 confused deputy），enabled + allowlist 都查；上下文源额外查 `secrets-autonomous`
4. **注入**：`bash_tool` 读 `runtime.context[__active_skill_secrets]`，传 `execute_command(env=...)`
5. **环境擦洗**（`env_policy.py:100` `build_sandbox_env`）：先剥离 `os.environ` 里所有 `*KEY*/*SECRET*/*TOKEN*/*PASS*/*CREDENTIAL*/*DSN*`（`env_policy.py:24` `_SECRET_NAME_PATTERNS`）+ 连接串黑名单（`env_policy.py:66` `_BLOCKED_EXACT_NAMES`，含 `DATABASE_URL/REDIS_URL/GH_PAT/MYSQL_PWD/REDISCLI_AUTH/PGPASSFILE/PGSERVICEFILE` 等），再叠加注入值
   - 注释（`env_policy.py:10-13`）明确对标 codex 与 hermes 的 blocklist 策略：DeerFlow 默认擦洗，codex 默认关闭
6. **泄漏面已封堵**：prompt / trace / checkpoint / audit / stdout / run-record 都不携带密钥值

### 三重授权

技能 **enabled**（operator）× 值 **supplied**（caller `context.secrets`）× 名字 **declared**（frontmatter），∩ 语义。

### 非目标

- 无持久化 / vaulting：值是请求级，服务端不存
- 子代理不继承注入集
- MCP 的 per-user 凭据缺口（#3322）是兄弟问题，不在此覆盖

测试：`tests/test_skill_request_scoped_secrets.py`。

---

## 十一、技能审查（review）

`skills/review/`：只读包快照 + 确定性事实 + 资源/eval 分析 + 报告渲染 + CLI。

### 约束

- 不得 import `app.*`
- 不得执行目标脚本
- 不得装依赖
- 不得联网
- 复用共享 frontmatter 助手与 SkillScan

### 模块

`analyzer.py / readers.py / renderer.py / digest.py / resource_graph.py / eval_schema.py / models.py / cli.py`

### 工具与契约

- JSON 契约在 `contracts/skill_review/`
- `review_skill_package` 内置工具（`tools/builtins/review_skill_package_tool.py`）：结果标 `review_subject_entry`（非 `skill_context_entry`），所以审查不等于激活，不绑定 `required-secrets`，不应用 `allowed-tools`
- 模型可见的是紧凑 JSON（控制标签中和化），完整原始 payload 在 `ToolMessage.artifact`
- CI 应以 `python -m deerflow.skills.review.cli --fail-on error --fail-on-incomplete` 运行，blocker/error 与未评估包均失败

### 公共技能分工

- `skills/public/skill-reviewer`：负责语义就绪审查 + 建议
- `skills/public/skill-creator`：负责变异与运行实验

---

## 十二、测试覆盖

`backend/tests/` 下约 30 个 skill 相关测试，覆盖：

- loader / parser / installer
- storage（local + user-scoped + 生命周期）
- slash 契约（前后端共享 `contracts/slash_skill_contract.json`）
- skill_manage 工具
- 工具策略中间件
- 请求级密钥隔离
- SkillScan 原生扫描
- 技能审查
- 权限
- 元数据 prompt 注入
- 三类挂载 e2e
- 子代理技能配置

阻塞 IO 回归锚点：`tests/blocking_io/test_skills_load.py`（锁定 `LocalSkillStorage.load_skills` 的 `asyncio.to_thread` offload，修 #1917）。

---

## 十三、技能生命周期：提取 · 优化 · 合并 · 审核 · 发布

本节回答"一个技能从无到有、到发布上线的完整闭环是如何实现的"。涉及五个阶段，分别由不同的模块/技能承载：

| 阶段 | 主导模块/技能 | 触发方式 |
|------|--------------|----------|
| 提取（创建） | `skill-creator` + `skill_manage` 工具 | agent 自助 / 用户驱动 |
| 优化（迭代） | `skill-creator` 的 eval+improve 循环 | 评估驱动 |
| 合并（打包/安装） | `package_skill.py` + `installer.py` + Gateway 路由 | 发布前打包、目标环境安装 |
| 审核（审查） | `skill-reviewer` + `review_skill_package` 工具 + SkillScan | 发布前/日常审计 |
| 发布（上线） | `extensions_config.json` 启用 + `POST /api/skills/reload` | 操作员启用 |

### 13.1 提取（创建）

#### 13.1.1 总开关：skill_evolution

agent 能否自助创建/修改技能受 `config.yaml -> skill_evolution.enabled` 控制（`config/skill_evolution_config.py:4`）。

- **工具 gating**（`tools/tools.py:93-97`）：只有 `skill_evolution.enabled=true` 时，`skill_manage_tool` 才被加入 builtin_tools 列表，agent 才看得到这个工具
- **提示注入**（`agents/lead_agent/prompt.py:274` `_build_skill_evolution_section`）：启用时向系统提示注入 "Skill Self-Evolution" 段落，告知 agent 何时该创建技能（5+ 工具调用、克服非显然错误、用户纠正后成功、发现可复用工作流）以及"必须用 skill_manage、绝不写 /mnt/user-data"的硬约束
- **关闭时**：段落为空，工具不加载，agent 无自助创建能力

#### 13.1.2 人工/agent 创建流程

两条路径：

**A. agent 自助（运行时）**：调用 `skill_manage(action="create", name=..., content=...)`（`tools/skill_manage_tool.py:141`）
- 校验技能名（hyphen-case，≤64 字符）
- 校验 frontmatter（name 必须匹配请求名）
- 静态扫描（`enforce_static_scan`）+ LLM 扫描（`scan_skill_content`）
- 写入用户目录 `users/{user_id}/skills/custom/<name>/SKILL.md`
- 追加 JSONL 历史
- 异步刷新该用户的系统提示技能缓存

**B. 离线脚手架**：`skills/public/skill-creator/scripts/init_skill.py` 从模板生成技能骨架，配合 `quick_validate.py` 做基础校验（frontmatter 格式、命名规范、描述无尖括号等）

#### 13.1.3 安全闸门（创建即扫描）

每次 `skill_manage` 写操作（create/edit/patch/write_file）都强制跑两层扫描（见第九节），`CRITICAL` finding 直接拒绝写入。LLM 扫描器（`security_scanner.py:100`）会接收静态 findings 作为上下文，用 `skill_evolution.moderation_model_name`（可选）或默认模型判定 `allow/warn/block`。

### 13.2 优化（迭代）

优化由 `skill-creator` 技能驱动，核心是一个 **eval → grade → improve → rerun** 的闭环。所有脚本在 `skills/public/skill-creator/scripts/`。

#### 13.2.1 评估运行（run_eval.py）

`run_eval.py:35` `run_single_query`：测试某条用户 query 是否会触发技能。

机制：
1. 在 `.claude/commands/` 下创建临时 command 文件，把技能描述注入 `available_skills`
2. 用 `claude -p --output-format stream-json --include-partial-messages` 跑 query
3. 通过流式事件（`content_block_start`）早期检测是否触发了技能读取，无需等工具执行完
4. 每 query 跑 `runs_per_query` 次（默认 3），按 `trigger_threshold` 判定 pass/fail
5. 多 query 并行（`ProcessPoolExecutor`）

#### 13.2.2 描述优化（improve_description.py）

`improve_description.py:50`：基于 eval 失败结果调用 `claude -p` 改写 description。

输入：
- 当前 description + 完整 SKILL.md 内容
- 失败的 should-trigger（漏触发）和 should-not-trigger（误触发）列表
- 历史尝试（防重复，要求结构性不同）

输出：新的 description 文本。

#### 13.2.3 闭环（run_loop.py）

`run_loop.py:47` `run_loop`：组合 eval + improve，支持 train/test split 防过拟合。

```
for iteration in 1..max_iterations:
    1. run_eval(train + test 一起跑，并行)
    2. 若全过 → 退出
    3. improve_description(失败结果 + 历史)
    4. 记录历史
    5. 选 best_description（按 test 分数，非 train，防过拟合）
```

最终产出 `best_description` + HTML 报告（`generate_report.py`）。

#### 13.2.4 行为基准（aggregate_benchmark.py + grader agent）

描述优化只解决"触发准确度"。行为质量用另一套机制：

- **并行跑 with_skill / without_skill（baseline）**：skill-creator 的 SKILL.md 规定同一轮 spawn 两个子代理，一个带技能一个不带，跑同一 prompt
- **grading**：`agents/grader.md` 定义的 grader 子代理逐条评估 assertions，产出 `grading.json`（expectations/summary/claims/eval_feedback）
- **聚合**：`aggregate_benchmark.py:45` 计算 mean/stddev/min/max，产出 `benchmark.json` + `benchmark.md`，含 with vs without 的 delta
- **可视化**：`eval-viewer/generate_review.py` 生成浏览器查看器（Outputs 标签看定性产出 + Benchmark 标签看定量对比）
- **分析**：`agents/analyzer.md` 做分析 pass，发现非区分性 assertion、高方差 eval、time/token 权衡

#### 13.2.5 盲比较（可选）

`agents/comparator.md`：把两个版本的输出匿名给独立 agent 评判，用于"新版本是否真的更好"的严格验证。

#### 13.2.6 优化后的落地

description 优化结果通过 `skill_manage(action="patch")` 写回 SKILL.md frontmatter；SKILL.md 正文的改进同样用 patch/edit。每次写都走扫描 + 历史。

### 13.3 合并（打包 / 安装）

"合并"在 DeerFlow 里体现为把一个技能目录打包成可分发的 `.skill` 归档，再在目标环境安装。

#### 13.3.1 打包（package_skill.py）

`skills/public/skill-creator/scripts/package_skill.py:42`：

1. 先跑 `quick_validate`（frontmatter + 命名校验）
2. 遍历技能目录 `rglob`，排除：
   - `__pycache__` / `node_modules` / `*.pyc` / `.DS_Store`
   - 根级 `evals/` 目录（评估数据不进发布包，但嵌套的 eval fixture 允许）
3. 写成 `<skill-name>.skill`（ZIP_DEFLATED）
4. arcname 保留 `skill_name/...` 前缀

注意：DeerFlow 沙盒环境里 `skill-creator/SKILL.md` 明确说"跳过 package_skill.py 步骤"——因为 `skill_manage` 已经把技能持久化到按用户目录，立即对所有未来会话可见，无需打包安装。打包主要用于跨环境分发或归档。

#### 13.3.2 安装（installer.py + Gateway 路由）

安装路径：`POST /api/skills/install`（管理员鉴权），或 `SkillStorage.install_skill_from_archive`。

`installer.py::safe_extract_skill_archive`（`installer.py:117`）的安全提取流程：
1. 条目数 ≤ 4096（zip bomb 防御）
2. 逐条检查：拒绝绝对路径 / `..` 遍历 / 符号链接
3. 拒绝可执行二进制（ELF/PE/Mach-O 魔数）
4. 累计大小 ≤ 512 MB
5. 写入 staging 目录，再原子移入 `custom/<name>/`
6. 安装前后都跑 SkillScan（`scan_archive_preflight` + `_scan_skill_archive_contents_or_raise`）

安装后技能处于"已安装但可能未启用"状态，需通过 `extensions_config.json` 或 `PUT /api/skills/{name}` 启用。

### 13.4 审核（审查）

审核是**只读**的，不改技能内容。由 `skill-reviewer` 公共技能 + `review_skill_package` 内置工具 + review 核心模块协作。

#### 13.4.1 review_skill_package 工具

`tools/builtins/review_skill_package_tool.py:27`：

- **非激活**：结果标 `review_subject_entry`（不是 `skill_context_entry`），所以审查不触发 allowed-tools、不绑定 required-secrets、不算激活
- **输入**：`target`（`skill://public/name`、`skill://custom/name`、`skill://legacy/name`、`inline://SKILL.md`、本地路径/归档）
- **profile**：`deerflow`（默认）或 `agentskills`（跨规范移植性）
- **include_content**：`none` / `facts-only` / `semantic-review`
- **输出**：`ToolMessage.content` 是紧凑 JSON（控制标签中和化），完整 payload 在 `ToolMessage.artifact`，含中英双语 Markdown 渲染

#### 13.4.2 确定性事实（review/analyzer.py）

`skills/review/analyzer.py:27` `analyze_skill_package` 产出 `review-facts.v1`：
- 结构检查：根 SKILL.md 存在且为 UTF-8 文本、无嵌套 SKILL.md（eval fixture 除外）
- frontmatter 解析（复用共享 helper）
- 资源图（`resource_graph.py`）：references/templates/scripts/assets 的引用关系
- eval 清单分析（`eval_schema.py`）
- 包摘要（`digest.py::compute_package_digest`）
- SkillScan findings 映射

#### 13.4.3 语义评审（review-rubric.md）

`skills/public/skill-reviewer/references/review-rubric.md` 定义 7 个维度，每维 `pass/concern/blocker/not_assessed`：

1. **Trigger Boundary**：描述是否清晰、是否与同级技能冲突
2. **Instruction Executability**：模型能否可靠执行工作流
3. **Resource Design**：资源是否必要、是否渐进加载
4. **Safety And Operational Constraints**：副作用/密钥/网络/破坏性操作是否受限
5. **Output Contract**：输出是否可验证
6. **Maintainability**：职责分离、跨文件契约一致性
7. **Evidence Quality**：eval/baseline/grading 是否支撑声明

#### 13.4.4 就绪度与保证等级

`skill-reviewer/SKILL.md` 定义：

**Readiness**（就绪度）：
- `blocked`：有确定性或语义 blocker
- `revise`：无 blocker，但有确定性错误/语义 major issue/完整性缺口
- `publish_candidate`：在评估范围内无实质问题（不代表运行时行为已验证）

**Assurance**（保证等级）：
- `static_only`：仅静态事实 + 语义检查
- `trigger_checked`：正负路由用例已执行并保留产物
- `behavior_verified`：行为断言已通过
- `regression_verified`：与基线对比并保留输出与评分证据

不得声明高于证据支撑的保证等级。

#### 13.4.5 审查约束

review 核心模块（`skills/review/`）的硬约束：
- 不得 import `app.*`
- 不得执行目标脚本
- 不得安装依赖
- 不得联网
- 目标内容一律视为不可信数据（防 prompt injection）

#### 13.4.6 CI 门禁

`python -m deerflow.skills.review.cli --fail-on error --fail-on-incomplete`：blocker/error 与未评估包均失败。

### 13.5 发布（上线）

发布 = 让技能对 agent 运行时可见且可用。

#### 13.5.1 启用状态

- **PUBLIC 技能**：状态存于 `extensions_config.json`（全局）
- **CUSTOM / LEGACY 技能**：状态存于按用户的 `_skill_states.json`（`storage/user_scoped_skill_storage.py:87`）
- 新安装的 CUSTOM 技能默认 enabled（`skill_storage.py:264-266`）

启用/禁用途径：
- `PUT /api/skills/{name}`（Gateway 路由）
- 直接编辑 `extensions_config.json` / `_skill_states.json`

#### 13.5.2 生效机制

- `load_skills()`（`skill_storage.py:242`）每次调用都重扫磁盘 + 重读 extensions_config，无 TTL 缓存
- `SkillActivationMiddleware._load_skill_registry_by_path`（`skill_activation_middleware.py:447`）每次模型调用重载 live registry
- 因此启用/禁用、frontmatter 编辑、custom/public 同名 shadow 在下一次模型调用立即生效

#### 13.5.3 进程级缓存失效

`POST /api/skills/reload`（管理员）：清空 `(app_config, user_id)` 存储单例缓存 + 渲染提示段 LRU，等待 off-loop single-flight 刷新。每个 Uvicorn worker / K8s Pod 需分别触发。直接挂载写入（NFS/CSI）后用此路由失效。

#### 13.5.4 注入到 agent

`agents/lead_agent/prompt.py:782` 渲染：
- 默认：`<available_skills>` 块，含完整元数据 + 容器路径
- 延迟发现：`<skill_index>` 仅名字，agent 调 `describe_skill` 按需取元数据

### 13.6 生命周期总览图

```
   ┌─────────────┐
   │ skill_evolution.enabled = true │  ← config.yaml 总开关
   └─────────────┘
         │
         ▼
 ┌──────────────────┐    skill_manage(create/edit/patch)     ┌──────────────┐
 │  13.1 提取(创建)  │ ─────────────────────────────────────▶ │  custom/<name>/SKILL.md  │
 └──────────────────┘    + 静态扫描 + LLM 扫描 + 历史         └──────────────┘
                                                                    │
                         ┌──────────────────────────────────────────┘
                         ▼
                 ┌──────────────────┐  run_eval → improve_description → run_loop
                 │  13.2 优化(迭代)  │  + with/without_skill benchmark + grader
                 └──────────────────┘  + eval-viewer + analyzer
                         │
                         │ skill_manage(patch) 写回改进
                         ▼
                 ┌──────────────────┐  package_skill.py → <name>.skill
                 │  13.3 合并(打包)  │  safe_extract_skill_archive → install
                 └──────────────────┘
                         │
                         ▼
                 ┌──────────────────┐  review_skill_package + SkillScan
                 │  13.4 审核(审查)  │  + 7 维 rubric + readiness/assurance
                 └──────────────────┘
                         │ publish_candidate
                         ▼
                 ┌──────────────────┐  extensions_config / _skill_states.json
                 │  13.5 发布(上线)  │  + PUT /api/skills/{name} + /api/skills/reload
                 └──────────────────┘
                         │
                         ▼
              <available_skills> 或 <skill_index> 注入系统提示
              agent 通过 /slash 或 read_file 激活使用
```

### 13.7 关键设计要点

1. **创建即扫描**：skill_manage 的每次写操作都跑两层扫描，CRITICAL 即拒，不放过任何写入路径
2. **优化有量化闭环**：eval 驱动 + train/test split 防过拟合 + benchmark 对比 baseline + 盲比较，不是凭感觉改
3. **审查与变异分离**：skill-reviewer 只读不写，skill-creator 负责变异；review_subject_entry 标签确保审查不激活
4. **发布零停机**：load_skills 每次重扫 + 每次模型调用重载 registry，启用/禁用立即生效，无需重启
5. **按用户隔离贯穿全周期**：创建/优化/发布都按 user_id 隔离，同名技能不跨用户泄漏
6. **打包是可选的**：沙盒内 skill_manage 已持久化，打包仅用于跨环境分发；DeerFlow 明确说"跳过 package_skill.py"
7. **总开关兜底**：skill_evolution.enabled=false 时 agent 完全无自助创建能力，工具不加载、提示不注入

---

## 十四、关键设计原则小结

1. **安全优先**：环境默认擦洗（不继承 host 凭据）、两层扫描、安装路径硬限制、三重授权
2. **即时生效**：`load_skills` 每次重扫、每次模型调用重载 live registry，无 TTL 缓存
3. **按用户隔离**：自定义技能按用户目录，启用状态按用户文件，LEGACY 只读回退
4. **行为收窄非硬边界**：allowed-tools 是 best-effort，承认有未捕获的加载路径
5. **延迟发现可选**：默认全量注入提示，可选紧凑 `<skill_index>` + `describe_skill` 按需加载
6. **slash 是显式仪式**：激活后 run 内权威，压制自主上下文策略源，密钥绑定豁免 `secrets-autonomous` opt-out
7. **审查不等于激活**：`review_subject_entry` 标签隔离，审查目标不触发副作用
8. **创建即扫描**：skill_manage 每次写操作都跑两层扫描，CRITICAL 即拒
9. **优化有量化闭环**：eval 驱动 + train/test split + benchmark 对比 + 盲比较
10. **审查与变异分离**：skill-reviewer 只读，skill-creator 负责变异

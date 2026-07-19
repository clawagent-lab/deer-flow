# `backend/packages/harness/deerflow/skills/slash.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/slash.py`  ·  行数: 75

## 模块概览
- 函数 2 个，类 2 个，模块级常量 2 个

## 功能语义解读

### 模块职责

本模块是 `/skill-name task` slash 激活语法的**后端入口闸门**：从用户输入文本中识别以 `/` 起首的 skill 激活指令，剥离前缀 slash 与 skill 名，返回剩余 task 文本，并在此基础上完成"该 skill 是否已安装、已启用、已被白名单允许、对应的容器内 `SKILL.md` 路径是什么"的运行时校验。它同时是前后端 slash 语法契约的 Python 一侧实现，与前端 `frontend/src/core/skills/slash.ts` 通过 `contracts/slash_skill_contract.json` 双向锁定。

### `_SLASH_SKILL_RE` 正则设计

模块第 18 行：

```python
_SLASH_SKILL_RE = re.compile(r"^/([a-z0-9]+(?:-[a-z0-9]+)*)(?:\s+|$)")
```

其设计要点：

- `^/`：必须以 `/` 起首，且无前导空白 —— `parse_slash_skill_reference` 用 `re.match`（隐含 `^`），但正则显式再写 `^/` 双重锁定，确保 `  /foo` 这类带前导空白的文本不会被误判为激活。
- `([a-z0-9]+(?:-[a-z0-9]+)*)`：捕获组定义 **hyphen-case** skill 名语法：
  - 首段 `[a-z0-9]+` 必须由小写字母或数字组成，不允许大写、下划线、驼峰；
  - 后续 `(?:-[a-z0-9]+)*` 允许零或多个 `-segment`，每段同样仅小写字母/数字，且 `-` 不可连续（`--` 不匹配）、不可尾随（`foo-` 不匹配）；
  - 整体匹配 `research`、`code-review`、`a-b-c`，但拒绝 `Foo`、`foo_bar`、`foo--bar`、`foo-`。
- `(?:\s+|$)`：skill 名之后必须是**至少一个空白字符**或**字符串结尾**。这一非捕获组是"分隔符强制"：`/foox` 不会匹配，因为 `o` 既非空白也非串尾；而 `/foo` 或 `/foo bar` 都合法。这一约束防止 `/path/like/this` 被 `re.match` 误判为 skill `path`。
- 捕获组 1 即为 skill 名，由 `match.group(1)` 取出。

### `RESERVED_SLASH_SKILL_NAMES` 保留命令

模块第 17 行：

```python
RESERVED_SLASH_SKILL_NAMES = frozenset({"bootstrap", "goal", "help", "memory", "models", "new", "status"})
```

共 7 个保留名，均为 Composer/IM 通道的**控制命令**，不可被 skill 占用。即便正则匹配通过，`parse_slash_skill_reference` 仍会在第 44 行检查 `name in RESERVED_SLASH_SKILL_NAMES` 并返回 `None`，使这些命令走它们各自的原生处理路径而不被当作 skill 激活：

| 保留名 | 作用 |
|--------|------|
| `bootstrap` | 引导/初始化流程命令（如模式创建、schema 引导） |
| `goal` | 线程级目标条件管理：`/goal`、`/goal clear`、`/goal <condition>`，由前端 input-box 拦截并走 Gateway `/api/threads/{id}/goal` |
| `help` | 帮助命令 |
| `memory` | 用户记忆管理命令，走 Gateway `/api/memory*` |
| `models` | 模型列表/选择命令 |
| `new` | 新建会话/线程命令 |
| `status` | 状态查询命令 |

`frozenset` 的选择使成员判定 O(1) 且不可变，避免运行时被意外篡改。

### `SlashSkillReference` vs `ResolvedSlashSkill`

两个 `@dataclass(frozen=True, slots=True)` 不可变值对象，分别代表解析流程的两个阶段：

| 维度 | `SlashSkillReference` (L22) | `ResolvedSlashSkill` (L30) |
|------|------------------------------|------------------------------|
| 阶段 | **纯语法解析** | **解析 + 运行时校验 + 路径计算** |
| 字段 | `name: str`、`remaining_text: str` | `skill: Skill`、`remaining_text: str`、`container_file_path: str` |
| 是否知道 skill 存在 | 否，仅持有名字字符串 | 是，持有完整 `Skill` 对象 |
| 是否校验 enabled/白名单 | 否 | 是 |
| 是否计算容器路径 | 否 | 是，`container_file_path` 已就绪 |
| 产出函数 | `parse_slash_skill_reference` | `resolve_slash_skill` |

`frozen=True` + `slots=True` 使二者成为轻量、不可变、不可继承的值对象，适合在解析层与执行层之间安全传递。

### `parse_slash_skill_reference` 与 `resolve_slash_skill` 的分工

**`parse_slash_skill_reference(text: str) -> SlashSkillReference | None`**（L38）—— 纯解析层：

1. 用 `_SLASH_SKILL_RE.match(text)` 匹配；不匹配返回 `None`。
2. 取捕获组 1 为 `name`；若 `name` 命中 `RESERVED_SLASH_SKILL_NAMES` 返回 `None`。
3. 否则构造 `SlashSkillReference`，其中 `remaining_text = text[match.end():].lstrip()`：`match.end()` 落在分隔空白之后（因 `(?:\s+|$)` 也被消费），再 `lstrip()` 抹掉剩余前导空白，得到干净的 task 文本。

该函数**不触碰任何运行时状态**：不查 skill 列表、不校验 enabled、不计算路径。前端 `parseSlashSkillReference` 是其 TypeScript 镜像。

**`resolve_slash_skill(text, skills, *, available_skills=None, container_base_path=DEFAULT_SKILLS_CONTAINER_PATH) -> ResolvedSlashSkill | None`**（L52）—— 校验 + 路径计算层，三道闸门：

1. 调 `parse_slash_skill_reference(text)`；为 `None` 直接返回 `None`（语法/保留名闸门）。
2. 若传入 `available_skills`（即自定义 agent 的 skill 白名单，`set[str] | None`），且 `reference.name not in available_skills`，返回 `None`（白名单闸门）。`None` 表示"不施加白名单约束"，仅由默认/全量 agent 路径使用。
3. 在 `skills` 列表中线性查找 `candidate.name == reference.name and candidate.enabled` 的首个 `Skill`；找不到返回 `None`（已安装且启用闸门）。`next(..., None)` 保证只取首个匹配且无匹配时返回 `None`。
4. 通过三道闸门后，调 `skill.get_container_file_path(container_base_path)` 计算 `SKILL.md` 在 sandbox 容器内的绝对路径（默认基路径 `DEFAULT_SKILLS_CONTAINER_PATH = "/mnt/skills"`，见 `deerflow.constants` 与 `deerflow.skills.types`），并连同 `reference.remaining_text` 一起封装为 `ResolvedSlashSkill` 返回。

二者分工的核心：`parse_*` 只回答"文本在语法上是不是 skill 激活、是哪个 skill、剩余 task 是什么"；`resolve_*` 在此基础上回答"这个 skill 在当前运行时是否真的可用，可用的话容器内的 `SKILL.md` 路径是什么"。调用方可按需停在第一阶段（例如仅做语法高亮）或走到第二阶段（真正加载 skill 内容）。

### 与前端 `slash.ts` 的契约锁定

后端 `slash.py` 与前端 `frontend/src/core/skills/slash.ts` 是**双向镜像**：

- 二者各自定义同名的 `RESERVED_SLASH_SKILL_NAMES`（Python `frozenset` ↔ TS `Set`）与同形的 `SLASH_SKILL_RE`（正则字面量完全一致：`^/([a-z0-9]+(?:-[a-z0-9]+)*)(?:\s+|$)`）。
- 前端 `parseSlashSkillReference` 与 `resolveSlashSkillDisplay` 分别镜像后端 `parse_slash_skill_reference` 与 `resolve_slash_skill` 的语义（前端 display 版本不计算容器路径，仅判定 enabled + 名称匹配，因为前端只需决定是否渲染激活 chip）。
- 两套实现共同被 `contracts/slash_skill_contract.json` 这一**跨语言契约夹具**锁定。该 JSON 显式声明 `version`、`description`、`reserved_slash_skill_names`（7 个，顺序与后端一致）与 `skill_name_pattern`（与 `_SLASH_SKILL_RE` 字面同形）。
- 锁定机制通过**双侧契约测试**强制：后端 `backend/tests/test_slash_skill_contract.py` 与前端 `frontend/tests/unit/core/skills/slash-contract.test.ts` 各自加载同一份 JSON 并断言本地常量与之一致。因此任何一侧单独新增保留命令、修改 skill 名语法都会在 CI 失败，确保前端只有在后端确实会把文本当作 skill 激活时才渲染激活 chip，避免前后端语义漂移。

## 依赖（import）
- 模块: re
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH
- `deerflow.skills.types` -> Skill

## 模块级常量
- `RESERVED_SLASH_SKILL_NAMES` = frozenset({'bootstrap', 'goal', 'help', 'memory', 'models...
- `_SLASH_SKILL_RE` = re.compile('^/([a-z0-9]+(?:-[a-z0-9]+)*)(?:\\s+|$)')

## 函数
#### `ƒ` `parse_slash_skill_reference(text: str) -> SlashSkillReference | None`  L38
  - _文档首行_（仅供参考）: Parse strict `/skill-name task` syntax, ignoring reserved control commands.
  - 分支数 2，函数体节点数 68；return: None, SlashSkillReference(name=name, remaining_text=text[match.end():].lstrip())
  - 调用: match, group, SlashSkillReference, lstrip, end

#### `ƒ` `resolve_slash_skill(text: str, skills: list[Skill], *, available_skills: set[str] | None, container_base_path: str) -> ResolvedSlashSkill | None`  L52
  - _文档首行_（仅供参考）: Resolve text into an enabled, whitelisted skill activation if possible.
  - 分支数 3，函数体节点数 128；return: None, ResolvedSlashSkill(skill=skill, remaining_text=reference.remaining_text, container_file_path=skill.get_container_file_path(container_base_path))
  - 调用: parse_slash_skill_reference, next, ResolvedSlashSkill, get_container_file_path

## 类
### 类 `SlashSkillReference`  L22  @dataclass(...)
- _文档首行_: Parsed slash-skill command with the skill name and remaining task text.
- 类/实例变量:
  - `name` = <annotated>
  - `remaining_text` = <annotated>

### 类 `ResolvedSlashSkill`  L30  @dataclass(...)
- _文档首行_: Slash-skill activation resolved against enabled runtime-visible skills.
- 类/实例变量:
  - `skill` = <annotated>
  - `remaining_text` = <annotated>
  - `container_file_path` = <annotated>

## 文件内调用关系
- `resolve_slash_skill` -> parse_slash_skill_reference

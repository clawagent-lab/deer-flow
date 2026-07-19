# `backend/packages/harness/deerflow/skills/types.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/types.py`  ·  行数: 93

## 模块概览
- 函数 0 个，类 3 个，模块级常量 1 个

## 功能语义解读

### 模块职责
本模块是 deerflow 技能子系统的领域类型定义中心，集中声明技能的分类枚举（`SkillCategory`）、机密声明（`SecretRequirement`）与技能元数据载体（`Skill`）三类核心数据结构，供解析、编目、存储、挂载与工具层共享。所有下游模块（parser/catalog/storage/skill_manage_tool 等）均以此处定义的类型作为数据契约，避免在散落位置重复定义技能形状。模块自身仅依赖 `deerflow.constants.DEFAULT_SKILLS_CONTAINER_PATH`，保持纯粹的类型层无外部副作用。

### 核心数据结构设计意图
- **frozen dataclass**：`Skill` 与 `SecretRequirement` 均标注 `@dataclass(frozen=True)`，实例一旦构造即不可变，因而天然可哈希、可作为集合元素或字典键使用，适合在 catalog 缓存、去重比较、集合运算等场景中以值语义安全传递；冻结同时杜绝了下游误改 `skill_dir`、`category` 等关键字段导致的路径漂移。
- **SkillCategory 选用 StrEnum**：`PUBLIC`/`CUSTOM`/`LEGACY` 三个取值既是枚举成员又是普通字符串，使得 `f"{container_base_path}/{self.category}"` 这类路径拼接无需 `.value` 访问，类型安全与字符串便利性兼得；其取值还直接对应容器内挂载子目录名与沙箱权限策略（public 只读、custom 可编辑、legacy 只读但可见）。
- **SecretRequirement 的双角色 name**：`name` 字段同时承担两个职责——既是运行期从 `context.secrets` 中查找凭据的键，又是注入到技能沙箱子进程环境的变量名，单一字段串起"声明—查找—注入"链路；`optional` 标记缺省时是否阻断激活，使机密约束可在数据结构层显式表达而非散落于业务代码。

### 关键方法功能
- **`skill_path` 属性（空串约定）**：将 `relative_path.as_posix()` 结果中代表"当前目录根"的 `"."` 归一化为空串 `""`，保证位于分类根下的技能（无中间子路径）在后续拼接时不会产生 `/skills/public/.` 这样的脏路径，统一了"无相对子路径"的表示形式。
- **`get_container_path` 分支逻辑**：先拼出 `category_base = f"{container_base_path}/{self.category}"`，再依据 `skill_path` 真值分支——非空时追加 `/{skill_path}`，为空时直接返回 `category_base`，刻意避免尾部多余斜杠或 `/.` 片段；`container_base_path` 默认取自 `DEFAULT_SKILLS_CONTAINER_PATH`，支持调用方覆盖以适配不同沙箱挂载根。
- **`get_container_file_path` 复用**：直接委托 `get_container_path` 得到技能目录容器路径，再固定追加 `/SKILL.md`，复用既有路径构造逻辑以保证一致性，不重复实现分支判断。
- **`__repr__` 刻意省略敏感字段**：仅暴露 `name`、`description`、`category` 三项，有意省去 `required_secrets`（机密变量名）、`skill_dir`/`skill_file`（宿主文件系统路径）、`allowed_tools`、`license`、`enabled`、`secrets_autonomous` 等，防止日志或异常打印中泄漏机密变量名与宿主路径信息。

### 协作关系
本模块作为技能子系统的类型底座，被下游广泛复用：parser 解析 frontmatter 后构造 `Skill` 实例、catalog/registry 按其做编目与去重、storage 层据 `get_container_path`/`get_container_file_path` 计算挂载与读取路径、skill_manage_tool 与网关 skills 路由据此序列化技能元数据。模块依赖面极窄，仅引入 `deerflow.constants` 的容器路径常量，符合"类型层零外部副作用"的定位。

## 依赖（import）
- `dataclasses` -> dataclass, field
- `enum` -> StrEnum
- `pathlib` -> Path
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH

## 模块级常量
- `SKILL_MD_FILE` = 'SKILL.md'

## 类
### 类 `SkillCategory`  L10
- 继承: StrEnum
- _文档首行_: Source category for a skill.
- 类/实例变量:
  - `PUBLIC` = 'public'
  - `CUSTOM` = 'custom'
  - `LEGACY` = 'legacy'

### 类 `SecretRequirement`  L26  @dataclass(...)
- _文档首行_: A request-scoped secret a skill declares it needs (issue #3861).
- 类/实例变量:
  - `name` = <annotated>
  - `optional` = False

### 类 `Skill`  L39  @dataclass(...)
- _文档首行_: Represents a skill with its metadata and file path
- 类/实例变量:
  - `name` = <annotated>
  - `description` = <annotated>
  - `license` = <annotated>
  - `skill_dir` = <annotated>
  - `skill_file` = <annotated>
  - `relative_path` = <annotated>
  - `category` = <annotated>
  - `allowed_tools` = None
  - `enabled` = False
  - `required_secrets` = field(default_factory=tuple)
  - `secrets_autonomous` = True
- 方法:
  #### `prop` `skill_path(self) -> str`    @property  L58
    - _文档首行_（仅供参考）: Returns the relative path from the category root (skills/{category}) to this skill's directory
    - 分支数 0，函数体节点数 29；return: '' if path == '.' else path
    - 调用: as_posix
  #### `m` `get_container_path(self, container_base_path: str) -> str`  L63
    - _文档首行_（仅供参考）: Get the full path to this skill in the container.
    - 分支数 1，函数体节点数 47；return: f'{category_base}/{skill_path}', category_base
  #### `m` `get_container_file_path(self, container_base_path: str) -> str`  L79
    - _文档首行_（仅供参考）: Get the full path to this skill's main file (SKILL.md) in the container.
    - 分支数 0，函数体节点数 23；return: f'{self.get_container_path(container_base_path)}/SKILL.md'
    - 调用: get_container_path
  #### `m` `__repr__(self) -> str`  L91
    - 分支数 0，函数体节点数 26；return: f'Skill(name={self.name!r}, description={self.description!r}, category={self.category!r})'

## 文件内调用关系
- `Skill.get_container_file_path` -> get_container_path

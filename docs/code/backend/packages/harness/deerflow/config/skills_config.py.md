# `backend/packages/harness/deerflow/config/skills_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/skills_config.py`  ·  行数: 78

## 模块概览
- 函数 1 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: os
- `pathlib` -> Path
- `pydantic` -> BaseModel, Field
- `deerflow.config.runtime_paths` -> project_root, resolve_path
- `deerflow.constants` -> DEFAULT_SKILLS_CONTAINER_PATH

## 函数
#### `ƒ` `_legacy_skills_candidates() -> tuple[Path, ...]`  L10
  - _文档首行_（仅供参考）: Return source-tree skills locations for monorepo compatibility.
  - 分支数 0，函数体节点数 44；return: (repo_root / 'skills',)
  - 调用: resolve, Path

## 类
### 类 `SkillsConfig`  L17
- 继承: BaseModel
- _文档首行_: Configuration for skills system
- 类/实例变量:
  - `use` = Field(default='deerflow.skills.storage.local_skill_storag...
  - `path` = Field(default=None, description='Path to skills directory...
  - `container_path` = Field(default=DEFAULT_SKILLS_CONTAINER_PATH, description=...
  - `deferred_discovery` = Field(default=False, description='When enabled, skill met...
- 方法:
  #### `m` `get_skills_path(self) -> Path`  L37
    - _文档首行_（仅供参考）: Get the resolved skills directory path.
    - 分支数 5，函数体节点数 72；return: resolve_path(self.path), resolve_path(env_path), project_default, candidate
    - 调用: resolve_path, getenv, project_root, is_dir, _legacy_skills_candidates
  - 环境变量: getenv (L53)
  #### `m` `get_skill_container_path(self, skill_name: str, category: str) -> str`  L66
    - _文档首行_（仅供参考）: Get the full container path for a specific skill.
    - 分支数 0，函数体节点数 29；return: f'{self.container_path}/{category}/{skill_name}'

## 文件内调用关系
- `SkillsConfig.get_skills_path` -> _legacy_skills_candidates

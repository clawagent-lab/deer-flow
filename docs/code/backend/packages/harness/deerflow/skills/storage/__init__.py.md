# `backend/packages/harness/deerflow/skills/storage/__init__.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/storage/__init__.py`  ·  行数: 204

**模块文档首行**（仅供参考）: SkillStorage singleton + reflection-based factory.

## 模块概览
- 函数 5 个，类 0 个，模块级常量 8 个
- `__all__`: LocalSkillStorage, SkillStorage, UserScopedSkillStorage, get_or_new_skill_storage, get_or_new_user_skill_storage, user_should_see_legacy_skills, reset_skill_storage, reset_user_skill_storage

## 依赖（import）
- 模块: logging, threading
- `__future__` -> annotations
- `collections` -> OrderedDict
- `deerflow.skills.storage.local_skill_storage` -> LocalSkillStorage
- `deerflow.skills.storage.skill_storage` -> SkillStorage
- `deerflow.skills.storage.user_scoped_skill_storage` -> UserScopedSkillStorage
- `deerflow.skills.types` -> SkillCategory

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_default_skill_storage` = None
- `_default_skill_storage_config` = None
- `_skill_storage_lock` = threading.Lock()
- `_MAX_USER_SCOPED_STORAGES` = 64
- `_user_scoped_storages` = OrderedDict()
- `_user_scoped_storage_lock` = threading.Lock()
- `__all__` = ['LocalSkillStorage', 'SkillStorage', 'UserScopedSkillSto...

## 函数
#### `ƒ` `get_or_new_skill_storage(**kwargs) -> SkillStorage`  L36
  - _文档首行_（仅供参考）: Return a ``SkillStorage`` instance — either a new one or the process singleton.
  - 分支数 6，函数体节点数 215；可变参数（*args/**kwargs）；return: cls(host_path=host_path if host_path is not None else str(skills_config.get_skills_path()), container_path=skills_config.container_path, **kwargs), _make_storage(app_config.skills, host_path=str(skills_path), **kwargs), _make_storage(SkillsConfig(), host_path=str(skills_path), **kwargs), _make_storage(app_config.skills, **kwargs), _default_skill_storage
  - 调用: resolve_class, cls, str, get_skills_path, pop, _make_storage, SkillsConfig, get_app_config

#### `ƒ` `get_or_new_user_skill_storage(user_id: str, **kwargs) -> SkillStorage`  L104
  - _文档首行_（仅供参考）: Return a per-user ``SkillStorage`` instance for custom skill isolation.
  - 分支数 3，函数体节点数 109；可变参数（*args/**kwargs）；return: cached
  - 调用: make_safe_user_id, get, move_to_end, UserScopedSkillStorage, len, popitem, info

#### `ƒ` `user_should_see_legacy_skills(user_id: str, **kwargs) -> bool`  L146
  - _文档首行_（仅供参考）: Return whether discovery exposes any LEGACY skills for this user.
  - 分支数 1，函数体节点数 79；可变参数（*args/**kwargs）；return: any(((skill.category.value if hasattr(skill.category, 'value') else skill.category) == SkillCategory.LEGACY.value for skill in storage.load_skills(enabled_only=False)))
  - 调用: UserScopedSkillStorage, make_safe_user_id, get_or_new_user_skill_storage, any, hasattr, load_skills
  - 反射: hasattr (L159)

#### `ƒ` `reset_skill_storage() -> None`  L162
  - _文档首行_（仅供参考）: Clear all cached storage instances (used in tests and hot-reload scenarios).
  - 分支数 2，函数体节点数 28
  - 调用: clear

#### `ƒ` `reset_user_skill_storage(user_id: str | None) -> None`  L172
  - _文档首行_（仅供参考）: Clear per-user skill storage cache for a specific user, or all users.
  - 分支数 2，函数体节点数 47
  - 调用: make_safe_user_id, pop, clear

## 文件内调用关系
- `user_should_see_legacy_skills` -> get_or_new_user_skill_storage

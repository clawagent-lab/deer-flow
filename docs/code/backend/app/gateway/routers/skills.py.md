# `backend/app/gateway/routers/skills.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/skills.py`  ·  行数: 504

## 模块概览
- 函数 16 个，类 10 个，模块级常量 3 个

## 依赖（import）
- 模块: asyncio, json, logging, tempfile
- `pathlib` -> Path
- `typing` -> Literal
- `fastapi` -> APIRouter, Depends, HTTPException, Request
- `pydantic` -> BaseModel, Field
- `app.gateway.deps` -> get_config, require_admin_user
- `app.gateway.path_utils` -> resolve_thread_virtual_path
- `deerflow.agents.lead_agent.prompt` -> clear_skills_system_prompt_cache, refresh_skills_system_prompt_cache_async, refresh_user_skills_system_prompt_cache_async
- `deerflow.config.app_config` -> AppConfig
- `deerflow.config.extensions_config` -> ExtensionsConfig, SkillStateConfig, get_extensions_config, reload_extensions_config
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.skills` -> Skill
- `deerflow.skills.installer` -> SkillAlreadyExistsError, SkillSecurityScanError
- `deerflow.skills.security_scanner` -> scan_skill_content
- `deerflow.skills.security_static_scanner` -> StaticFinding, StaticScanBlockedError, StaticScannerError, enforce_static_scan
- `deerflow.skills.storage` -> SkillStorage, get_or_new_user_skill_storage
- `deerflow.skills.types` -> SKILL_MD_FILE, SkillCategory

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api', tags=['skills'])
- `_ADMIN_REQUIRED_DETAIL` = 'Admin privileges required to manage skills.'

## 函数
#### `ƒ` `_skill_to_response(skill: Skill) -> SkillResponse`  L98
  - _文档首行_（仅供参考）: Convert a Skill object to a SkillResponse.
  - 分支数 0，函数体节点数 49；return: SkillResponse(name=skill.name, description=skill.description, license=skill.license, category=skill.category, enabled=skill.enabled, editable=skill.category == SkillCategory.CUSTOM)
  - 调用: SkillResponse

#### `ƒ` `_static_scan_http_detail(error: StaticScanBlockedError) -> dict`  L110
  - 分支数 0，函数体节点数 25；return: {'message': str(error), 'skill_name': error.skill_name, 'findings': error.findings}
  - 调用: str

#### `⏵ƒ` `async _scan_static_skill_markdown_or_raise(skill_name: str, content: str, *, app_config: AppConfig) -> list[StaticFinding]`  L118
  - 分支数 2，函数体节点数 128；raise: HTTPException(status_code=400, detail=_static_scan_http_detail(e)), HTTPException(status_code=400, detail=f"Static security scan failed for skill '{skill_name}': {e}")；return: enforce_static_scan(skill_dir, skill_name=skill_name, app_config=app_config), await asyncio.to_thread(_scan_markdown)
  - 调用: TemporaryDirectory, Path, mkdir, write_text, enforce_static_scan, to_thread, HTTPException, _static_scan_http_detail
  - 文件IO: mkdir (L122), write_text (L123)

#### `ƒ` `_get_user_skill_storage(config: AppConfig) -> SkillStorage`  L134
  - _文档首行_（仅供参考）: Return a user-scoped skill storage for custom skill operations.
  - 分支数 0，函数体节点数 19；return: get_or_new_user_skill_storage(get_effective_user_id(), app_config=config)
  - 调用: get_or_new_user_skill_storage, get_effective_user_id

#### `⏵ƒ` `async list_skills(config: AppConfig) -> SkillsListResponse`    @router.get(...)  L149
  - 分支数 1，函数体节点数 86；raise: HTTPException(status_code=500, detail=f'Failed to load skills: {str(e)}')；return: SkillsListResponse(skills=[_skill_to_response(skill) for skill in skills])
  - 调用: Depends, load_skills, _get_user_skill_storage, SkillsListResponse, _skill_to_response, error, HTTPException, str, get

#### `⏵ƒ` `async install_skill(request: Request, body: SkillInstallRequest, config: AppConfig) -> SkillInstallResponse`    @router.post(...)  L165
  - 分支数 2，函数体节点数 209；raise: HTTPException(status_code=404, detail=str(e)), HTTPException(status_code=409, detail=str(e)), HTTPException(status_code=400, detail={'message': str(e), 'skill_name': e.skill_name, 'findings': e.findings}), HTTPException(status_code=400, detail=str(e)), bare raise, HTTPException(status_code=500, detail=f'Failed to install skill: {str(e)}')；return: SkillInstallResponse(**result)
  - 调用: Depends, require_admin_user, resolve_thread_virtual_path, ainstall_skill_from_archive, _get_user_skill_storage, refresh_user_skills_system_prompt_cache_async, get_effective_user_id, SkillInstallResponse, HTTPException, str, error, post

#### `⏵ƒ` `async reload_skills(request: Request) -> SkillReloadResponse`    @router.post(...)  L202
  - _文档首行_（仅供参考）: Invalidate process-local skill prompt caches after external file changes.
  - 分支数 1，函数体节点数 68；raise: HTTPException(status_code=500, detail='Failed to invalidate skills cache.')；return: SkillReloadResponse(success=True, scope='process', message='Skill caches invalidated; subsequent runs in this Gateway process will rescan the latest skills.')
  - 调用: require_admin_user, refresh_skills_system_prompt_cache_async, exception, HTTPException, SkillReloadResponse, post

#### `⏵ƒ` `async list_custom_skills(config: AppConfig) -> SkillsListResponse`    @router.get(...)  L219
  - _文档首行_（仅供参考）: List only user-owned custom skills (SkillCategory.CUSTOM).
  - 分支数 1，函数体节点数 100；raise: HTTPException(status_code=500, detail=f'Failed to list custom skills: {str(e)}')；return: SkillsListResponse(skills=[_skill_to_response(skill) for skill in skills])
  - 调用: Depends, load_skills, _get_user_skill_storage, SkillsListResponse, _skill_to_response, error, HTTPException, str, get

#### `⏵ƒ` `async get_custom_skill(skill_name: str, request: Request, config: AppConfig) -> CustomSkillContentResponse`    @router.get(...)  L236
  - 分支数 0，函数体节点数 48；return: await _read_custom_skill_response(skill_name, config)
  - 调用: Depends, require_admin_user, _read_custom_skill_response, get

#### `⏵ƒ` `async _read_custom_skill_response(skill_name: str, config: AppConfig) -> CustomSkillContentResponse`  L241
  - 分支数 2，函数体节点数 154；raise: HTTPException(status_code=404, detail=f"Custom skill '{skill_name}' not found"), bare raise, HTTPException(status_code=500, detail=f'Failed to get custom skill: {str(e)}')；return: CustomSkillContentResponse(**_skill_to_response(skill).model_dump(), content=storage.read_custom_skill(skill_name))
  - 调用: replace, _get_user_skill_storage, load_skills, next, HTTPException, CustomSkillContentResponse, model_dump, _skill_to_response, read_custom_skill, error, str
  - 文件IO: replace (L243), replace (L243)

#### `⏵ƒ` `async update_custom_skill(skill_name: str, body: CustomSkillUpdateRequest, request: Request, config: AppConfig) -> CustomSkillContentResponse`    @router.put(...)  L258
  - 分支数 2，函数体节点数 299；raise: HTTPException(status_code=400, detail=f'Security scan blocked the edit: {scan.reason}'), bare raise, HTTPException(status_code=404, detail=str(e)), HTTPException(status_code=400, detail=str(e)), HTTPException(status_code=500, detail=f'Failed to update custom skill: {str(e)}')；return: await _read_custom_skill_response(skill_name, config)
  - 调用: Depends, require_admin_user, replace, _get_user_skill_storage, ensure_custom_skill_is_editable, validate_skill_markdown_content, _scan_static_skill_markdown_or_raise, scan_skill_content, HTTPException, read_custom_skill, write_custom_skill, append_history, refresh_user_skills_system_prompt_cache_async, get_effective_user_id, _read_custom_skill_response, str, error, put
  - 文件IO: replace (L261), replace (L261)

#### `⏵ƒ` `async delete_custom_skill(skill_name: str, request: Request, config: AppConfig) -> dict[str, bool]`    @router.delete(...)  L297
  - 分支数 1，函数体节点数 170；raise: HTTPException(status_code=404, detail=str(e)), HTTPException(status_code=400, detail=str(e)), HTTPException(status_code=500, detail=f'Failed to delete custom skill: {str(e)}')；return: {'success': True}
  - 调用: Depends, require_admin_user, replace, _get_user_skill_storage, delete_custom_skill, refresh_user_skills_system_prompt_cache_async, get_effective_user_id, HTTPException, str, error, delete
  - 文件IO: replace (L300), replace (L300)

#### `⏵ƒ` `async get_custom_skill_history(skill_name: str, request: Request, config: AppConfig) -> CustomSkillHistoryResponse`    @router.get(...)  L326
  - 分支数 2，函数体节点数 147；raise: HTTPException(status_code=404, detail=f"Custom skill '{skill_name}' not found"), bare raise, HTTPException(status_code=500, detail=f'Failed to read history: {str(e)}')；return: CustomSkillHistoryResponse(history=storage.read_history(skill_name))
  - 调用: Depends, require_admin_user, replace, _get_user_skill_storage, custom_skill_exists, exists, get_skill_history_file, HTTPException, CustomSkillHistoryResponse, read_history, error, str, get
  - 文件IO: replace (L329), replace (L329), exists (L331)

#### `⏵ƒ` `async rollback_custom_skill(skill_name: str, body: SkillRollbackRequest, request: Request, config: AppConfig) -> CustomSkillContentResponse`    @router.post(...)  L342
  - 分支数 5，函数体节点数 415；raise: HTTPException(status_code=404, detail=f"Custom skill '{skill_name}' not found"), HTTPException(status_code=400, detail=f"Custom skill '{skill_name}' has no history"), HTTPException(status_code=400, detail='Selected history entry has no previous content to roll back to'), HTTPException(status_code=400, detail=f'Rollback blocked by security scanner: {scan.reason}'), bare raise, HTTPException(status_code=400, detail='history_index is out of range'), HTTPException(status_code=404, detail=str(e)), HTTPException(status_code=400, detail=str(e)), HTTPException(status_code=500, detail=f'Failed to roll back custom skill: {str(e)}')；return: await _read_custom_skill_response(skill_name, config)
  - 调用: Depends, require_admin_user, _get_user_skill_storage, custom_skill_exists, exists, get_skill_history_file, HTTPException, read_history, get, validate_skill_markdown_content, _scan_static_skill_markdown_or_raise, scan_skill_content, get_custom_skill_file, read_text, append_history, write_custom_skill, refresh_user_skills_system_prompt_cache_async, get_effective_user_id, _read_custom_skill_response, str（+2）
  - 文件IO: exists (L346), exists (L359), read_text (L359)

#### `⏵ƒ` `async get_skill(skill_name: str, config: AppConfig) -> SkillResponse`    @router.get(...)  L396
  - 分支数 2，函数体节点数 144；raise: HTTPException(status_code=404, detail=f"Skill '{skill_name}' not found"), bare raise, HTTPException(status_code=500, detail=f'Failed to get skill: {str(e)}')；return: _skill_to_response(skill)
  - 调用: Depends, replace, load_skills, _get_user_skill_storage, next, HTTPException, _skill_to_response, error, str, get
  - 文件IO: replace (L398), replace (L398)

#### `⏵ƒ` `async update_skill(skill_name: str, body: SkillUpdateRequest, request: Request, config: AppConfig) -> SkillResponse`    @router.put(...)  L419
  - 分支数 10，函数体节点数 578；raise: HTTPException(status_code=404, detail=f"Skill '{skill_name}' not found"), HTTPException(status_code=500, detail=f"Failed to reload skill '{skill_name}' after update"), bare raise, HTTPException(status_code=500, detail=f'Failed to update skill: {str(e)}')；return: _skill_to_response(updated_skill)
  - 调用: Depends, require_admin_user, replace, _get_user_skill_storage, load_skills, next, HTTPException, resolve_config_path, cwd, info, get_extensions_config, SkillStateConfig, model_dump, items, open, dump, reload_extensions_config, isinstance, set_skill_enabled_state, to_thread（+6）
  - 文件IO: replace (L426), replace (L426), open (L451), open (L473)

## 类
### 类 `SkillResponse`  L36
- 继承: BaseModel
- _文档首行_: Response model for skill information.
- 类/实例变量:
  - `name` = Field(..., description='Name of the skill')
  - `description` = Field(..., description='Description of what the skill does')
  - `license` = Field(None, description='License information')
  - `category` = Field(..., description='Category of the skill (public, cu...
  - `enabled` = Field(default=True, description='Whether this skill is en...
  - `editable` = Field(default=False, description='Whether this skill can ...

### 类 `SkillsListResponse`  L47
- 继承: BaseModel
- _文档首行_: Response model for listing all skills.
- 类/实例变量:
  - `skills` = <annotated>

### 类 `SkillUpdateRequest`  L53
- 继承: BaseModel
- _文档首行_: Request model for updating a skill.
- 类/实例变量:
  - `enabled` = Field(..., description='Whether to enable or disable the ...

### 类 `SkillInstallRequest`  L59
- 继承: BaseModel
- _文档首行_: Request model for installing a skill from a .skill file.
- 类/实例变量:
  - `thread_id` = Field(..., description='The thread ID where the .skill fi...
  - `path` = Field(..., description='Virtual path to the .skill file (...

### 类 `SkillInstallResponse`  L66
- 继承: BaseModel
- _文档首行_: Response model for skill installation.
- 类/实例变量:
  - `success` = Field(..., description='Whether the installation was succ...
  - `skill_name` = Field(..., description='Name of the installed skill')
  - `message` = Field(..., description='Installation result message')

### 类 `SkillReloadResponse`  L74
- 继承: BaseModel
- _文档首行_: Response model for process-local skill cache invalidation.
- 类/实例变量:
  - `success` = Field(..., description='Whether the skill caches were inv...
  - `scope` = Field(..., description='Reload scope; only the current Ga...
  - `message` = Field(..., description='Human-readable reload status')

### 类 `CustomSkillContentResponse`  L82
- 继承: SkillResponse
- 类/实例变量:
  - `content` = Field(..., description='Raw SKILL.md content')

### 类 `CustomSkillUpdateRequest`  L86
- 继承: BaseModel
- 类/实例变量:
  - `content` = Field(..., description='Replacement SKILL.md content')

### 类 `CustomSkillHistoryResponse`  L90
- 继承: BaseModel
- 类/实例变量:
  - `history` = <annotated>

### 类 `SkillRollbackRequest`  L94
- 继承: BaseModel
- 类/实例变量:
  - `history_index` = Field(default=-1, description='History entry index to res...

## 文件内调用关系
- `_scan_static_skill_markdown_or_raise` -> _static_scan_http_detail
- `list_skills` -> _get_user_skill_storage, _skill_to_response
- `install_skill` -> _get_user_skill_storage
- `list_custom_skills` -> _get_user_skill_storage, _skill_to_response
- `get_custom_skill` -> _read_custom_skill_response
- `_read_custom_skill_response` -> _get_user_skill_storage, _skill_to_response
- `update_custom_skill` -> _get_user_skill_storage, _scan_static_skill_markdown_or_raise, _read_custom_skill_response
- `delete_custom_skill` -> _get_user_skill_storage, delete_custom_skill
- `get_custom_skill_history` -> _get_user_skill_storage
- `rollback_custom_skill` -> _get_user_skill_storage, _scan_static_skill_markdown_or_raise, _read_custom_skill_response
- `get_skill` -> _get_user_skill_storage, _skill_to_response
- `update_skill` -> _get_user_skill_storage, _skill_to_response

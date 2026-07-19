# `backend/app/gateway/routers/agents.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/agents.py`  ·  行数: 491

**模块文档首行**（仅供参考）: CRUD API for custom agents.

## 模块概览
- 函数 12 个，类 6 个，模块级常量 3 个

## 依赖（import）
- 模块: asyncio, logging, re, shutil, yaml
- `fastapi` -> APIRouter, HTTPException
- `pydantic` -> BaseModel, Field
- `deerflow.config.agents_api_config` -> get_agents_api_config
- `deerflow.config.agents_config` -> AgentConfig, list_custom_agents, load_agent_config, load_agent_soul, preserve_non_managed_fields
- `deerflow.config.paths` -> get_paths
- `deerflow.runtime.user_context` -> get_effective_user_id

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api', tags=['agents'])
- `AGENT_NAME_PATTERN` = re.compile('^[A-Za-z0-9-]+$')

## 函数
#### `ƒ` `_validate_agent_name(name: str) -> None`  L61
  - _文档首行_（仅供参考）: Validate agent name against allowed pattern.
  - 分支数 1，函数体节点数 31；raise: HTTPException(status_code=422, detail=f"Invalid agent name '{name}'. Must match ^[A-Za-z0-9-]+$ (letters, digits, and hyphens only).")
  - 调用: match, HTTPException

#### `ƒ` `_normalize_agent_name(name: str) -> str`  L77
  - _文档首行_（仅供参考）: Normalize agent name to lowercase for filesystem storage.
  - 分支数 0，函数体节点数 15；return: name.lower()
  - 调用: lower

#### `ƒ` `_require_agents_api_enabled() -> None`  L82
  - _文档首行_（仅供参考）: Reject access unless the custom-agent management API is explicitly enabled.
  - 分支数 1，函数体节点数 21；raise: HTTPException(status_code=403, detail='Custom-agent management API is disabled. Set agents_api.enabled=true to expose agent and user-profile routes over HTTP.')
  - 调用: get_agents_api_config, HTTPException

#### `ƒ` `_agent_config_to_response(agent_cfg: AgentConfig, include_soul: bool, *, user_id: str | None) -> AgentResponse`  L91
  - _文档首行_（仅供参考）: Convert AgentConfig to AgentResponse.
  - 分支数 1，函数体节点数 80；return: AgentResponse(name=agent_cfg.name, description=agent_cfg.description, model=agent_cfg.model, tool_groups=agent_cfg.tool_groups, skills=agent_cfg.skills, soul=soul)
  - 调用: load_agent_soul, AgentResponse

#### `⏵ƒ` `async list_agents() -> AgentsListResponse`    @router.get(...)  L113
  - _文档首行_（仅供参考）: List all custom agents.
  - 分支数 1，函数体节点数 91；raise: HTTPException(status_code=500, detail=f'Failed to list agents: {str(e)}')；return: AgentsListResponse(agents=[_agent_config_to_response(a, include_soul=True, user_id=user_id) for a in agents])
  - 调用: _require_agents_api_enabled, get_effective_user_id, list_custom_agents, AgentsListResponse, _agent_config_to_response, error, HTTPException, str, get

#### `⏵ƒ` `async check_agent_name(name: str) -> dict`    @router.get(...)  L135
  - _文档首行_（仅供参考）: Check whether an agent name is valid and not yet taken.
  - 分支数 0，函数体节点数 88；return: {'available': available, 'name': normalized}
  - 调用: _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name, get_effective_user_id, get_paths, exists, user_agent_dir, agent_dir, get
  - 文件IO: exists (L155), exists (L155)

#### `⏵ƒ` `async get_agent(name: str) -> AgentResponse`    @router.get(...)  L165
  - _文档首行_（仅供参考）: Get a specific custom agent by name.
  - 分支数 1，函数体节点数 120；raise: HTTPException(status_code=404, detail=f"Agent '{name}' not found"), HTTPException(status_code=500, detail=f'Failed to get agent: {str(e)}')；return: _agent_config_to_response(agent_cfg, include_soul=True, user_id=user_id)
  - 调用: _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name, get_effective_user_id, load_agent_config, _agent_config_to_response, HTTPException, error, str, get

#### `⏵ƒ` `async create_agent_endpoint(request: AgentCreateRequest) -> AgentResponse`    @router.post(...)  L199
  - _文档首行_（仅供参考）: Create a new custom agent.
  - 分支数 11，函数体节点数 370；raise: bare raise, HTTPException(status_code=500, detail=f'Failed to create agent: {str(e)}'), HTTPException(status_code=409, detail=f"Agent '{normalized_name}' already exists")；return: None, _agent_config_to_response(agent_cfg, include_soul=True, user_id=user_id), response
  - 调用: _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name, get_effective_user_id, get_paths, user_agent_dir, agent_dir, exists, mkdir, open, dump, write_text, info, load_agent_config, _agent_config_to_response, rmtree, to_thread, error, HTTPException, str（+1）
  - 文件IO: exists (L224), mkdir (L229), open (L244), write_text (L249), exists (L257)

#### `⏵ƒ` `async update_agent(name: str, request: AgentUpdateRequest) -> AgentResponse`    @router.put(...)  L279
  - _文档首行_（仅供参考）: Update an existing custom agent.
  - 分支数 11，函数体节点数 447；raise: HTTPException(status_code=404, detail=f"Agent '{name}' not found"), HTTPException(status_code=409, detail=f"Agent '{name}' only exists in the legacy shared layout and is not scoped to a user. Run scripts/migrate_user_isolation.py to move legacy agents into the per-user layout before updating."), bare raise, HTTPException(status_code=500, detail=f'Failed to update agent: {str(e)}')；return: _agent_config_to_response(refreshed_cfg, include_soul=True, user_id=user_id)
  - 调用: _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name, get_effective_user_id, load_agent_config, HTTPException, get_paths, user_agent_dir, agent_dir, exists, bool, items, preserve_non_managed_fields, setdefault, open, dump, write_text, info, _agent_config_to_response, error（+2）
  - 文件IO: exists (L312), exists (L312), open (L358), write_text (L364)

#### `⏵ƒ` `async get_user_profile() -> UserProfileResponse`    @router.get(...)  L396
  - _文档首行_（仅供参考）: Return the current USER.md content.
  - 分支数 2，函数体节点数 100；raise: HTTPException(status_code=500, detail=f'Failed to read user profile: {str(e)}')；return: UserProfileResponse(content=None), UserProfileResponse(content=raw or None)
  - 调用: _require_agents_api_enabled, get_paths, exists, UserProfileResponse, strip, read_text, error, HTTPException, str, get
  - 文件IO: exists (L406), read_text (L408)

#### `⏵ƒ` `async update_user_profile(request: UserProfileUpdateRequest) -> UserProfileResponse`    @router.put(...)  L421
  - _文档首行_（仅供参考）: Create or overwrite the global USER.md.
  - 分支数 1，函数体节点数 115；raise: HTTPException(status_code=500, detail=f'Failed to update user profile: {str(e)}')；return: UserProfileResponse(content=request.content or None)
  - 调用: _require_agents_api_enabled, get_paths, mkdir, write_text, info, UserProfileResponse, error, HTTPException, str, put
  - 文件IO: mkdir (L434), write_text (L435)

#### `⏵ƒ` `async delete_agent(name: str) -> None`    @router.delete(...)  L449
  - _文档首行_（仅供参考）: Delete a custom agent.
  - 分支数 4，函数体节点数 229；raise: HTTPException(status_code=500, detail=f'Failed to delete agent: {str(e)}'), HTTPException(status_code=409, detail=f"Agent '{name}' only exists in the legacy shared layout and is not scoped to a user. Run scripts/migrate_user_isolation.py to move legacy agents into the per-user layout before deleting."), HTTPException(status_code=404, detail=f"Agent '{name}' not found")；return: (outcome, str(agent_dir)), ('deleted', str(agent_dir))
  - 调用: _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name, get_effective_user_id, get_paths, user_agent_dir, exists, agent_dir, str, rmtree, to_thread, error, HTTPException, info, delete
  - 文件IO: exists (L470), exists (L471)

## 类
### 类 `AgentResponse`  L23
- 继承: BaseModel
- _文档首行_: Response model for a custom agent.
- 类/实例变量:
  - `name` = Field(..., description='Agent name (hyphen-case)')
  - `description` = Field(default='', description='Agent description')
  - `model` = Field(default=None, description='Optional model override')
  - `tool_groups` = Field(default=None, description='Optional tool group whit...
  - `skills` = Field(default=None, description='Optional skill whitelist...
  - `soul` = Field(default=None, description='SOUL.md content')

### 类 `AgentsListResponse`  L34
- 继承: BaseModel
- _文档首行_: Response model for listing all custom agents.
- 类/实例变量:
  - `agents` = <annotated>

### 类 `AgentCreateRequest`  L40
- 继承: BaseModel
- _文档首行_: Request body for creating a custom agent.
- 类/实例变量:
  - `name` = Field(..., description='Agent name (must match ^[A-Za-z0-...
  - `description` = Field(default='', description='Agent description')
  - `model` = Field(default=None, description='Optional model override')
  - `tool_groups` = Field(default=None, description='Optional tool group whit...
  - `skills` = Field(default=None, description='Optional skill whitelist...
  - `soul` = Field(default='', description='SOUL.md content — agent pe...

### 类 `AgentUpdateRequest`  L51
- 继承: BaseModel
- _文档首行_: Request body for updating a custom agent.
- 类/实例变量:
  - `description` = Field(default=None, description='Updated description')
  - `model` = Field(default=None, description='Updated model override')
  - `tool_groups` = Field(default=None, description='Updated tool group white...
  - `skills` = Field(default=None, description='Updated skill whitelist ...
  - `soul` = Field(default=None, description='Updated SOUL.md content')

### 类 `UserProfileResponse`  L378
- 继承: BaseModel
- _文档首行_: Response model for the global user profile (USER.md).
- 类/实例变量:
  - `content` = Field(default=None, description='USER.md content, or null...

### 类 `UserProfileUpdateRequest`  L384
- 继承: BaseModel
- _文档首行_: Request body for setting the global user profile.
- 类/实例变量:
  - `content` = Field(default='', description="USER.md content — describe...

## 文件内调用关系
- `list_agents` -> _require_agents_api_enabled, _agent_config_to_response
- `check_agent_name` -> _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name
- `get_agent` -> _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name, _agent_config_to_response
- `create_agent_endpoint` -> _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name, _agent_config_to_response
- `update_agent` -> _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name, _agent_config_to_response
- `get_user_profile` -> _require_agents_api_enabled
- `update_user_profile` -> _require_agents_api_enabled
- `delete_agent` -> _require_agents_api_enabled, _validate_agent_name, _normalize_agent_name

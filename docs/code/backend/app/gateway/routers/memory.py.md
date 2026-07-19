# `backend/app/gateway/routers/memory.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/memory.py`  ·  行数: 418

**模块文档首行**（仅供参考）: Memory API router for retrieving and managing global memory data.

## 模块概览
- 函数 13 个，类 9 个，模块级常量 1 个

## 依赖（import）
- `typing` -> Literal
- `fastapi` -> APIRouter, HTTPException, Request
- `pydantic` -> BaseModel, Field
- `app.gateway.internal_auth` -> get_trusted_internal_owner_user_id
- `deerflow.agents.memory` -> get_memory_manager
- `deerflow.config.memory_config` -> get_memory_config
- `deerflow.config.paths` -> make_safe_user_id
- `deerflow.runtime.user_context` -> get_effective_user_id

## 模块级常量
- `router` = APIRouter(prefix='/api', tags=['memory'])

## 函数
#### `ƒ` `_resolve_memory_user_id(request: Request) -> str`  L17
  - _文档首行_（仅供参考）: Resolve the memory owner for this request.
  - 分支数 1，函数体节点数 30；return: make_safe_user_id(raw_owner), get_effective_user_id()
  - 调用: get_trusted_internal_owner_user_id, make_safe_user_id, get_effective_user_id

#### `ƒ` `_map_memory_fact_value_error(exc: ValueError) -> HTTPException`  L84
  - _文档首行_（仅供参考）: Convert updater validation errors into stable API responses.
  - 分支数 1，函数体节点数 43；return: HTTPException(status_code=400, detail=detail)
  - 调用: HTTPException

#### `ƒ` `_require_capability(name: str, *, label: str)`  L93
  - _文档首行_（仅供参考）: Return a DeerMem-internal capability (bound method) or raise 501.
  - 分支数 1，函数体节点数 56；raise: HTTPException(status_code=501, detail=f"Operation '{label}' not supported by memory backend '{type(manager).__name__}'.")；return: getattr(manager, name)
  - 调用: get_memory_manager, hasattr, HTTPException, type, getattr
  - 反射: hasattr (L103), getattr (L108)

#### `⏵ƒ` `async get_memory(http_request: Request) -> MemoryResponse`    @router.get(...)  L152
  - _文档首行_（仅供参考）: Get the current global memory data.
  - 分支数 0，函数体节点数 46；return: MemoryResponse(**memory_data)
  - 调用: get_memory, get_memory_manager, _resolve_memory_user_id, MemoryResponse, get

#### `⏵ƒ` `async reload_memory(http_request: Request) -> MemoryResponse`    @router.post(...)  L197
  - _文档首行_（仅供参考）: Reload memory data from file.
  - 分支数 1，函数体节点数 74；return: MemoryResponse(**memory_data)
  - 调用: _resolve_memory_user_id, get_memory_manager, hasattr, reload_memory, get_memory, MemoryResponse, post
  - 反射: hasattr (L208)

#### `⏵ƒ` `async clear_memory(http_request: Request) -> MemoryResponse`    @router.delete(...)  L226
  - _文档首行_（仅供参考）: Clear all persisted memory data.
  - 分支数 1，函数体节点数 60；raise: HTTPException(status_code=500, detail='Failed to clear memory data.')；return: MemoryResponse(**memory_data)
  - 调用: clear_memory, get_memory_manager, _resolve_memory_user_id, HTTPException, MemoryResponse, delete

#### `⏵ƒ` `async create_memory_fact_endpoint(request: FactCreateRequest, http_request: Request) -> MemoryResponse`    @router.post(...)  L243
  - _文档首行_（仅供参考）: Create a single fact manually.
  - 分支数 2，函数体节点数 113；raise: _map_memory_fact_value_error(exc), HTTPException(status_code=500, detail='Failed to create memory fact.'), HTTPException(status_code=409, detail='Fact was not stored because memory.max_facts kept higher-confidence facts')；return: MemoryResponse(**memory_data)
  - 调用: _require_capability, create_fact, _resolve_memory_user_id, _map_memory_fact_value_error, HTTPException, MemoryResponse, post

#### `⏵ƒ` `async delete_memory_fact_endpoint(fact_id: str, http_request: Request) -> MemoryResponse`    @router.delete(...)  L271
  - _文档首行_（仅供参考）: Delete a single fact from memory by fact id.
  - 分支数 1，函数体节点数 89；raise: HTTPException(status_code=404, detail=f"Memory fact '{fact_id}' not found."), HTTPException(status_code=500, detail='Failed to delete memory fact.')；return: MemoryResponse(**memory_data)
  - 调用: _require_capability, delete_fact, _resolve_memory_user_id, HTTPException, MemoryResponse, delete

#### `⏵ƒ` `async update_memory_fact_endpoint(fact_id: str, request: FactPatchRequest, http_request: Request) -> MemoryResponse`    @router.patch(...)  L291
  - _文档首行_（仅供参考）: Partially update a single fact manually.
  - 分支数 1，函数体节点数 119；raise: _map_memory_fact_value_error(exc), HTTPException(status_code=404, detail=f"Memory fact '{fact_id}' not found."), HTTPException(status_code=500, detail='Failed to update memory fact.')；return: MemoryResponse(**memory_data)
  - 调用: _require_capability, update_fact, _resolve_memory_user_id, _map_memory_fact_value_error, HTTPException, MemoryResponse, patch

#### `⏵ƒ` `async export_memory(http_request: Request) -> MemoryResponse`    @router.get(...)  L319
  - _文档首行_（仅供参考）: Export the current memory data.
  - 分支数 0，函数体节点数 46；return: MemoryResponse(**memory_data)
  - 调用: get_memory, get_memory_manager, _resolve_memory_user_id, MemoryResponse, get

#### `⏵ƒ` `async import_memory(request: MemoryResponse, http_request: Request) -> MemoryResponse`    @router.post(...)  L332
  - _文档首行_（仅供参考）: Import and persist memory data.
  - 分支数 1，函数体节点数 68；raise: HTTPException(status_code=500, detail='Failed to import memory data.')；return: MemoryResponse(**memory_data)
  - 调用: import_memory, get_memory_manager, model_dump, _resolve_memory_user_id, HTTPException, MemoryResponse, post

#### `⏵ƒ` `async get_memory_config_endpoint() -> MemoryConfigResponse`    @router.get(...)  L348
  - _文档首行_（仅供参考）: Get the memory system configuration.
  - 分支数 0，函数体节点数 59；return: MemoryConfigResponse(enabled=config.enabled, mode=config.mode, injection_enabled=config.injection_enabled, shutdown_flush_timeout_seconds=config.shutdown_flush_timeout_seconds, manager_class=config.manager_class, backend_config=config.backend_config)
  - 调用: get_memory_config, MemoryConfigResponse, get

#### `⏵ƒ` `async get_memory_status(http_request: Request) -> MemoryStatusResponse`    @router.get(...)  L398
  - _文档首行_（仅供参考）: Get the memory system status including configuration and data.
  - 分支数 0，函数体节点数 90；return: MemoryStatusResponse(config=MemoryConfigResponse(enabled=config.enabled, mode=config.mode, injection_enabled=config.injection_enabled, shutdown_flush_timeout_seconds=config.shutdown_flush_timeout_seconds, manager_class=config.manager_class, backend_config=config.backend_config), data=MemoryResponse(**memory_data))
  - 调用: get_memory_config, get_memory, get_memory_manager, _resolve_memory_user_id, MemoryStatusResponse, MemoryConfigResponse, MemoryResponse, get

## 类
### 类 `ContextSection`  L39
- 继承: BaseModel
- _文档首行_: Model for context sections (user and history).
- 类/实例变量:
  - `summary` = Field(default='', description='Summary content')
  - `updatedAt` = Field(default='', description='Last update timestamp')

### 类 `UserContext`  L46
- 继承: BaseModel
- _文档首行_: Model for user context.
- 类/实例变量:
  - `workContext` = Field(default_factory=ContextSection)
  - `personalContext` = Field(default_factory=ContextSection)
  - `topOfMind` = Field(default_factory=ContextSection)

### 类 `HistoryContext`  L54
- 继承: BaseModel
- _文档首行_: Model for history context.
- 类/实例变量:
  - `recentMonths` = Field(default_factory=ContextSection)
  - `earlierContext` = Field(default_factory=ContextSection)
  - `longTermBackground` = Field(default_factory=ContextSection)

### 类 `Fact`  L62
- 继承: BaseModel
- _文档首行_: Model for a memory fact.
- 类/实例变量:
  - `id` = Field(..., description='Unique identifier for the fact')
  - `content` = Field(..., description='Fact content')
  - `category` = Field(default='context', description='Fact category')
  - `confidence` = Field(default=0.5, description='Confidence score (0-1)')
  - `createdAt` = Field(default='', description='Creation timestamp')
  - `source` = Field(default='unknown', description='Source thread ID')
  - `sourceError` = Field(default=None, description='Optional description of ...

### 类 `MemoryResponse`  L74
- 继承: BaseModel
- _文档首行_: Response model for memory data.
- 类/实例变量:
  - `version` = Field(default='1.0', description='Memory schema version')
  - `lastUpdated` = Field(default='', description='Last update timestamp')
  - `user` = Field(default_factory=UserContext)
  - `history` = Field(default_factory=HistoryContext)
  - `facts` = Field(default_factory=list)

### 类 `FactCreateRequest`  L111
- 继承: BaseModel
- _文档首行_: Request model for creating a memory fact.
- 类/实例变量:
  - `content` = Field(..., min_length=1, description='Fact content')
  - `category` = Field(default='context', description='Fact category')
  - `confidence` = Field(default=0.5, ge=0.0, le=1.0, description='Confidenc...

### 类 `FactPatchRequest`  L119
- 继承: BaseModel
- _文档首行_: PATCH request model that preserves existing values for omitted fields.
- 类/实例变量:
  - `content` = Field(default=None, min_length=1, description='Fact conte...
  - `category` = Field(default=None, description='Fact category')
  - `confidence` = Field(default=None, ge=0.0, le=1.0, description='Confiden...

### 类 `MemoryConfigResponse`  L127
- 继承: BaseModel
- _文档首行_: Response model for memory configuration.
- 类/实例变量:
  - `enabled` = Field(..., description='Whether the memory mechanism is e...
  - `mode` = Field(..., description="Memory operation mode: 'middlewar...
  - `injection_enabled` = Field(..., description='Whether memory is injected into t...
  - `shutdown_flush_timeout_seconds` = Field(..., description="Hard budget (s) to drain pending ...
  - `manager_class` = Field(..., description='Active memory backend selector (b...
  - `backend_config` = Field(..., description='Backend-private config (self-inte...

### 类 `MemoryStatusResponse`  L138
- 继承: BaseModel
- _文档首行_: Response model for memory status.
- 类/实例变量:
  - `config` = <annotated>
  - `data` = <annotated>

## 文件内调用关系
- `get_memory` -> get_memory, _resolve_memory_user_id
- `reload_memory` -> _resolve_memory_user_id, reload_memory, get_memory
- `clear_memory` -> clear_memory, _resolve_memory_user_id
- `create_memory_fact_endpoint` -> _require_capability, _resolve_memory_user_id, _map_memory_fact_value_error
- `delete_memory_fact_endpoint` -> _require_capability, _resolve_memory_user_id
- `update_memory_fact_endpoint` -> _require_capability, _resolve_memory_user_id, _map_memory_fact_value_error
- `export_memory` -> get_memory, _resolve_memory_user_id
- `import_memory` -> import_memory, _resolve_memory_user_id
- `get_memory_status` -> get_memory, _resolve_memory_user_id

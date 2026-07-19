# `backend/app/gateway/routers/assistants_compat.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/assistants_compat.py`  ·  行数: 150

**模块文档首行**（仅供参考）: Assistants compatibility endpoints.

## 模块概览
- 函数 6 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `typing` -> Any
- `fastapi` -> APIRouter, HTTPException
- `pydantic` -> BaseModel, Field

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/assistants', tags=['assistants-com...

## 函数
#### `ƒ` `_get_default_assistant() -> AssistantResponse`  L43
  - _文档首行_（仅供参考）: Return the default lead_agent assistant.
  - 分支数 0，函数体节点数 45；return: AssistantResponse(assistant_id='lead_agent', graph_id='lead_agent', name='lead_agent', config={}, metadata={'created_by': 'system'}, description='DeerFlow lead agent', created_at=now, updated_at=now, version=1)
  - 调用: isoformat, now, AssistantResponse

#### `ƒ` `_list_assistants() -> list[AssistantResponse]`  L59
  - _文档首行_（仅供参考）: List all available assistants from config.
  - 分支数 2，函数体节点数 96；return: assistants
  - 调用: _get_default_assistant, list_custom_agents, isoformat, now, append, AssistantResponse, debug

#### `⏵ƒ` `async search_assistants(body: AssistantSearchRequest | None) -> list[AssistantResponse]`    @router.post(...)  L89
  - _文档首行_（仅供参考）: Search assistants.
  - 分支数 2，函数体节点数 138；return: assistants[offset:offset + limit]
  - 调用: _list_assistants, lower, post

#### `⏵ƒ` `async get_assistant_compat(assistant_id: str) -> AssistantResponse`    @router.get(...)  L107
  - _文档首行_（仅供参考）: Get an assistant by ID.
  - 分支数 2，函数体节点数 49；raise: HTTPException(status_code=404, detail=f'Assistant {assistant_id} not found')；return: a
  - 调用: _list_assistants, HTTPException, get

#### `⏵ƒ` `async get_assistant_graph(assistant_id: str) -> dict`    @router.get(...)  L116
  - _文档首行_（仅供参考）: Get the graph structure for an assistant.
  - 分支数 1，函数体节点数 64；raise: HTTPException(status_code=404, detail=f'Assistant {assistant_id} not found')；return: {'graph_id': 'lead_agent', 'nodes': [], 'edges': []}
  - 调用: any, _list_assistants, HTTPException, get

#### `⏵ƒ` `async get_assistant_schemas(assistant_id: str) -> dict`    @router.get(...)  L134
  - _文档首行_（仅供参考）: Get JSON schemas for an assistant's input/output/state.
  - 分支数 1，函数体节点数 66；raise: HTTPException(status_code=404, detail=f'Assistant {assistant_id} not found')；return: {'graph_id': 'lead_agent', 'input_schema': {}, 'output_schema': {}, 'state_schema': {}, 'config_schema': {}}
  - 调用: any, _list_assistants, HTTPException, get

## 类
### 类 `AssistantResponse`  L23
- 继承: BaseModel
- 类/实例变量:
  - `assistant_id` = <annotated>
  - `graph_id` = <annotated>
  - `name` = <annotated>
  - `config` = Field(default_factory=dict)
  - `metadata` = Field(default_factory=dict)
  - `description` = None
  - `created_at` = ''
  - `updated_at` = ''
  - `version` = 1

### 类 `AssistantSearchRequest`  L35
- 继承: BaseModel
- 类/实例变量:
  - `graph_id` = None
  - `name` = None
  - `metadata` = None
  - `limit` = 10
  - `offset` = 0

## 文件内调用关系
- `_list_assistants` -> _get_default_assistant
- `search_assistants` -> _list_assistants
- `get_assistant_compat` -> _list_assistants
- `get_assistant_graph` -> _list_assistants
- `get_assistant_schemas` -> _list_assistants

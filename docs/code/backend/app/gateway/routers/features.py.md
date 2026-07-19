# `backend/app/gateway/routers/features.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/features.py`  ·  行数: 41

**模块文档首行**（仅供参考）: Read-only feature-flag endpoint for the frontend bootstrap.

## 模块概览
- 函数 1 个，类 2 个，模块级常量 1 个

## 依赖（import）
- `fastapi` -> APIRouter, Depends
- `pydantic` -> BaseModel, Field
- `app.gateway.deps` -> get_config
- `deerflow.config.app_config` -> AppConfig

## 模块级常量
- `router` = APIRouter(prefix='/api', tags=['features'])

## 函数
#### `⏵ƒ` `async list_features(config: AppConfig) -> FeaturesResponse`    @router.get(...)  L36
  - _文档首行_（仅供参考）: Return availability of optional, config-gated frontend features.
  - 分支数 0，函数体节点数 42；return: FeaturesResponse(agents_api=AgentsApiFeature(enabled=config.agents_api.enabled))
  - 调用: Depends, FeaturesResponse, AgentsApiFeature, get

## 类
### 类 `AgentsApiFeature`  L18
- 继承: BaseModel
- _文档首行_: Availability of the custom-agent management API.
- 类/实例变量:
  - `enabled` = Field(..., description='Whether the agents_api routes are...

### 类 `FeaturesResponse`  L24
- 继承: BaseModel
- _文档首行_: Frontend-facing feature availability flags.
- 类/实例变量:
  - `agents_api` = <annotated>

## 文件内调用关系
_无文件内调用_

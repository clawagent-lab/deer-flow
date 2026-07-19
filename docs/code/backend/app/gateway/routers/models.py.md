# `backend/app/gateway/routers/models.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/models.py`  ·  行数: 133

## 模块概览
- 函数 2 个，类 3 个，模块级常量 1 个

## 依赖（import）
- `fastapi` -> APIRouter, Depends, HTTPException
- `pydantic` -> BaseModel, Field
- `app.gateway.deps` -> get_config
- `deerflow.config.app_config` -> AppConfig

## 模块级常量
- `router` = APIRouter(prefix='/api', tags=['models'])

## 函数
#### `⏵ƒ` `async list_models(config: AppConfig) -> ModelsListResponse`    @router.get(...)  L40
  - _文档首行_（仅供参考）: List all available models from configuration.
  - 分支数 0，函数体节点数 89；return: ModelsListResponse(models=models, token_usage=TokenUsageResponse(enabled=config.token_usage.enabled))
  - 调用: Depends, ModelResponse, ModelsListResponse, TokenUsageResponse, get

#### `⏵ƒ` `async get_model(model_name: str, config: AppConfig) -> ModelResponse`    @router.get(...)  L99
  - _文档首行_（仅供参考）: Get a specific model by name.
  - 分支数 1，函数体节点数 93；raise: HTTPException(status_code=404, detail=f"Model '{model_name}' not found")；return: ModelResponse(name=model.name, model=model.model, display_name=model.display_name, description=model.description, supports_thinking=model.supports_thinking, supports_reasoning_effort=model.supports_reasoning_effort)
  - 调用: Depends, get_model_config, HTTPException, ModelResponse, get

## 类
### 类 `ModelResponse`  L10
- 继承: BaseModel
- _文档首行_: Response model for model information.
- 类/实例变量:
  - `name` = Field(..., description='Unique identifier for the model')
  - `model` = Field(..., description='Actual provider model identifier')
  - `display_name` = Field(None, description='Human-readable name')
  - `description` = Field(None, description='Model description')
  - `supports_thinking` = Field(default=False, description='Whether model supports ...
  - `supports_reasoning_effort` = Field(default=False, description='Whether model supports ...

### 类 `TokenUsageResponse`  L21
- 继承: BaseModel
- _文档首行_: Token usage display configuration.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Whether token usage dis...

### 类 `ModelsListResponse`  L27
- 继承: BaseModel
- _文档首行_: Response model for listing all models.
- 类/实例变量:
  - `models` = <annotated>
  - `token_usage` = <annotated>

## 文件内调用关系
_无文件内调用_

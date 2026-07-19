# `backend/app/gateway/routers/suggestions.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/suggestions.py`  ·  行数: 142

## 模块概览
- 函数 4 个，类 4 个，模块级常量 4 个

## 依赖（import）
- 模块: json, logging, llm_text
- `fastapi` -> APIRouter, Depends, Request
- `pydantic` -> BaseModel, Field
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_config
- `deerflow.config.app_config` -> AppConfig
- `deerflow.utils.oneshot_llm` -> run_oneshot_llm

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api', tags=['suggestions'])
- `_strip_markdown_code_fence` = llm_text.strip_markdown_code_fence
- `_strip_think_blocks` = llm_text.strip_think_blocks

## 函数
#### `ƒ` `_parse_json_string_list(text: str) -> list[str] | None`  L41
  - 分支数 6，函数体节点数 168；return: None, out
  - 调用: _strip_think_blocks, _strip_markdown_code_fence, find, rfind, loads, isinstance, strip, append

#### `ƒ` `_format_conversation(messages: list[SuggestionMessage]) -> str`  L66
  - 分支数 3，函数体节点数 121；return: '\n'.join(parts).strip()
  - 调用: lower, strip, append, join

#### `⏵ƒ` `async get_suggestions_config(config: AppConfig) -> SuggestionsConfigResponse`    @router.get(...)  L85
  - 分支数 0，函数体节点数 36；return: SuggestionsConfigResponse(enabled=config.suggestions.enabled)
  - 调用: Depends, SuggestionsConfigResponse, get

#### `⏵ƒ` `async generate_suggestions(thread_id: str, body: SuggestionsRequest, request: Request, config: AppConfig) -> SuggestionsResponse`    @router.post(...), require_permission(...)  L98
  - 分支数 4，函数体节点数 223；return: SuggestionsResponse(suggestions=[]), SuggestionsResponse(suggestions=cleaned)
  - 调用: Depends, SuggestionsResponse, _format_conversation, run_oneshot_llm, _parse_json_string_list, strip, replace, exception, post, require_permission
  - 文件IO: replace (L136)

## 类
### 类 `SuggestionMessage`  L18
- 继承: BaseModel
- 类/实例变量:
  - `role` = Field(..., description='Message role: user|assistant')
  - `content` = Field(..., description='Message content as plain text')

### 类 `SuggestionsRequest`  L23
- 继承: BaseModel
- 类/实例变量:
  - `messages` = Field(..., description='Recent conversation messages')
  - `n` = Field(default=3, ge=1, le=5, description='Number of sugge...
  - `model_name` = Field(default=None, description='Optional model override')

### 类 `SuggestionsResponse`  L29
- 继承: BaseModel
- 类/实例变量:
  - `suggestions` = Field(default_factory=list, description='Suggested follow...

### 类 `SuggestionsConfigResponse`  L33
- 继承: BaseModel
- 类/实例变量:
  - `enabled` = Field(..., description='Whether follow-up suggestions are...

## 文件内调用关系
- `generate_suggestions` -> _format_conversation, _parse_json_string_list

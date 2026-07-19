# `backend/app/gateway/routers/input_polish.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/input_polish.py`  ·  行数: 108

## 模块概览
- 函数 4 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: logging, llm_text
- `fastapi` -> APIRouter, Depends, HTTPException, Request
- `pydantic` -> BaseModel, Field
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_config
- `deerflow.config.app_config` -> AppConfig
- `deerflow.utils.oneshot_llm` -> run_oneshot_llm

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api', tags=['input-polish'])

## 函数
#### `ƒ` `_clean_rewritten_text(text: str) -> str`  L28
  - 分支数 0，函数体节点数 35；return: candidate.strip()
  - 调用: strip_think_blocks, strip_markdown_code_fence, strip

#### `ƒ` `_build_system_instruction() -> str`  L39
  - 分支数 0，函数体节点数 6；return: "You are DeerFlow's pre-send prompt optimizer.\nRewrite the user's rough draft into a clearer instruction for an AI agent before it is sent.\nDo not answer the task.\nPreserve the user's language, intent, entities, file paths, URLs, code blocks, and any leading slash command prefix exactly.\nImprove the draft by making the goal, scope, constraints, and desired output explicit when they are implied by the draft.\nFor vague quality words such as 'better', 'good-looking', or 'polished', translate them into concrete but generic quality criteria.\nDo not invent facts, business context, tools, file names, dates, metrics, or user preferences that are not implied.\nPrefer one concise paragraph or a short bullet list. Keep it under 180 words unless the original draft is longer.\nOutput only the rewritten draft, with no markdown wrapper, explanation, or alternatives."

#### `ƒ` `_build_user_content(text: str, locale: str | None) -> str`  L53
  - 分支数 0，函数体节点数 36；return: f'Locale hint: {locale_hint}\n\nRewrite this draft while preserving its intent:\n<draft>\n{text}\n</draft>'
  - 调用: strip

#### `⏵ƒ` `async polish_input(body: InputPolishRequest, request: Request, config: AppConfig) -> InputPolishResponse`    @router.post(...), require_permission(...)  L65
  - 分支数 5，函数体节点数 216；raise: HTTPException(status_code=404, detail='Input polishing is disabled'), HTTPException(status_code=400, detail='Input text is required'), HTTPException(status_code=400, detail=f'Input text exceeds {max_chars} characters'), HTTPException(status_code=503, detail='Failed to polish input')；return: InputPolishResponse(rewritten_text=rewritten, changed=rewritten != text)
  - 调用: Depends, HTTPException, strip, len, run_oneshot_llm, _build_system_instruction, _build_user_content, _clean_rewritten_text, exception, InputPolishResponse, post, require_permission

## 类
### 类 `InputPolishRequest`  L17
- 继承: BaseModel
- 类/实例变量:
  - `text` = Field(..., description='Draft text currently shown in the...
  - `locale` = Field(default=None, description='Optional UI locale hint')
  - `thread_id` = Field(default=None, description='Optional thread id for t...

### 类 `InputPolishResponse`  L23
- 继承: BaseModel
- 类/实例变量:
  - `rewritten_text` = Field(..., description='Polished draft text')
  - `changed` = Field(..., description='Whether the model changed the ori...

## 文件内调用关系
- `polish_input` -> _build_system_instruction, _build_user_content, _clean_rewritten_text

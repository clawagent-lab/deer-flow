# `backend/app/gateway/routers/console.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/routers/console.py`  ·  行数: 493

**模块文档首行**（仅供参考）: Read-only operations-console endpoints.

## 模块概览
- 函数 10 个，类 7 个，模块级常量 5 个

## 依赖（import）
- 模块: asyncio, logging
- `datetime` -> UTC, datetime, time, timedelta
- `typing` -> NamedTuple
- `fastapi` -> APIRouter, HTTPException, Query, Request
- `pydantic` -> BaseModel, Field
- `sqlalchemy` -> func, select
- `app.gateway.authz` -> require_permission
- `app.gateway.deps` -> get_current_user
- `deerflow.config` -> get_app_config
- `deerflow.config.agents_config` -> list_custom_agents
- `deerflow.persistence.engine` -> get_session_factory
- `deerflow.persistence.run.model` -> RunRow
- `deerflow.persistence.thread_meta.model` -> ThreadMetaRow

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `router` = APIRouter(prefix='/api/console', tags=['console'])
- `_ACTIVE_STATUSES` = ('pending', 'running')
- `_FAILED_STATUSES` = ('error', 'timeout')
- `_ERROR_EXCERPT_CHARS` = 300

## 函数
#### `ƒ` `_session_factory_or_503()`  L121
  - 分支数 1，函数体节点数 25；raise: HTTPException(status_code=503, detail='Console requires a SQL database backend; set database.backend to sqlite or postgres in config.yaml.')；return: sf
  - 调用: get_session_factory, HTTPException

#### `ƒ` `_as_utc(dt: datetime | None) -> datetime | None`  L131
  - _文档首行_（仅供参考）: Normalize DB timestamps: SQLite round-trips them naive, Postgres aware.
  - 分支数 1，函数体节点数 42；return: None, dt.replace(tzinfo=UTC) if dt.tzinfo is None else dt
  - 调用: replace
  - 文件IO: replace (L135)

#### `ƒ` `_build_pricing_map() -> dict[str, _ModelPricing]`  L153
  - _文档首行_（仅供参考）: Collect per-model prices from ``models[*].pricing`` in config.yaml.
  - 分支数 7，函数体节点数 246；return: {}, pricing
  - 调用: get_app_config, warning, getattr, isinstance, float, get, upper, str, _ModelPricing, setdefault, lower
  - 反射: getattr (L171), getattr (L186)

#### `ƒ` `_pricing_currency(pricing: dict[str, _ModelPricing]) -> str | None`  L193
  - _文档首行_（仅供参考）: Display currency: the first configured entry's (one currency per deployment).
  - 分支数 0，函数体节点数 38；return: next(iter(pricing.values())).currency if pricing else None
  - 调用: next, iter, values

#### `ƒ` `_lookup_pricing(pricing: dict[str, _ModelPricing], model: str | None) -> _ModelPricing | None`  L198
  - 分支数 1，函数体节点数 51；return: None, pricing.get(model) or pricing.get(model.lower())
  - 调用: get, lower

#### `ƒ` `_token_cost(input_tokens: int, output_tokens: int, price: _ModelPricing, cache_read_tokens: int) -> float`  L204
  - _文档首行_（仅供参考）: Cache-aware spend: cache-hit input tokens are billed at the hit price.
  - 分支数 0，函数体节点数 123；return: uncached / 1000000 * price.input_per_million + cache_read / 1000000 * hit_price + output_tokens / 1000000 * price.output_per_million
  - 调用: min, max, int

#### `ƒ` `_run_cost(pricing: dict[str, _ModelPricing], *, model_name: str | None, total_input_tokens: int | None, total_output_tokens: int | None, token_usage_by_model: dict | None) -> float | None`  L217
  - _文档首行_（仅供参考）: Estimate one run's spend, or None when none of its models are priced.
  - 分支数 8，函数体节点数 244；return: cost, None, _token_cost(input_tokens, output_tokens, price)
  - 调用: isinstance, items, _lookup_pricing, int, get, _token_cost

#### `⏵ƒ` `async console_stats(request: Request) -> ConsoleStatsResponse`    @router.get(...), require_permission(...)  L271
  - _文档首行_（仅供参考）: Return the dashboard's headline counters.
  - 分支数 5，函数体节点数 449；return: ConsoleStatsResponse(total_runs=total_runs, active_runs=active_runs, failed_runs=failed_runs, total_threads=total_threads, total_agents=total_agents, total_tokens=total_tokens, total_cost=total_cost, currency=_pricing_currency(pricing))
  - 调用: _session_factory_or_503, get_current_user, _build_pricing_map, sf, scalar, where, select_from, select, count, in_, coalesce, sum, all, execute, _run_cost, round, to_thread, len, warning, ConsoleStatsResponse（+3）

#### `⏵ƒ` `async console_runs(request: Request, limit: int, offset: int, status: str | None) -> ConsoleRunsResponse`    @router.get(...), require_permission(...)  L340
  - _文档首行_（仅供参考）: Return a page of the user's runs across all threads.
  - 分支数 5，函数体节点数 454；return: ConsoleRunsResponse(runs=items, has_more=has_more)
  - 调用: Query, _session_factory_or_503, get_current_user, offset, limit, order_by, join, select, desc, where, sf, all, execute, _build_pricing_map, len, now, _as_utc, total_seconds, _run_cost, append（+6）

#### `⏵ƒ` `async console_usage(request: Request, days: int, tz_offset_minutes: int) -> ConsoleUsageResponse`    @router.get(...), require_permission(...)  L404
  - _文档首行_（仅供参考）: Aggregate token usage by local day and by model.
  - 分支数 13，函数体节点数 768；return: ConsoleUsageResponse(days=list(day_buckets.values()), by_model=by_model, total_tokens=total_tokens, total_runs=total_runs, total_cost=total_cost, currency=_pricing_currency(pricing))
  - 调用: Query, _session_factory_or_503, get_current_user, timedelta, date, now, combine, where, select, sf, all, scalars, execute, range, isoformat, ConsoleUsageDay, _build_pricing_map, _as_utc, get, _run_cost（+13）

## 类
### 类 `ConsoleStatsResponse`  L46
- 继承: BaseModel
- _文档首行_: Headline counters for the console dashboard.
- 类/实例变量:
  - `total_runs` = Field(..., description='All recorded runs for the current...
  - `active_runs` = Field(..., description='Runs currently pending or running')
  - `failed_runs` = Field(..., description='Runs that ended in error or timeo...
  - `total_threads` = Field(..., description='Conversation threads owned by the...
  - `total_agents` = Field(..., description='Custom agents owned by the curren...
  - `total_tokens` = Field(..., description='Tokens consumed across all record...
  - `total_cost` = Field(default=None, description='Estimated spend across p...
  - `currency` = Field(default=None, description='Display currency taken f...

### 类 `ConsoleRunItem`  L59
- 继承: BaseModel
- _文档首行_: One run in the cross-thread run listing.
- 类/实例变量:
  - `run_id` = <annotated>
  - `thread_id` = <annotated>
  - `thread_title` = Field(default=None, description='Display name from thread...
  - `assistant_id` = None
  - `status` = <annotated>
  - `model_name` = None
  - `created_at` = None
  - `updated_at` = None
  - `duration_seconds` = Field(default=None, description='Wall-clock duration; liv...
  - `total_tokens` = 0
  - `message_count` = 0
  - `cost` = Field(default=None, description='Estimated spend for this...
  - `error` = Field(default=None, description='Error excerpt for failed...

### 类 `ConsoleRunsResponse`  L77
- 继承: BaseModel
- _文档首行_: Paginated cross-thread run listing, newest first.
- 类/实例变量:
  - `runs` = <annotated>
  - `has_more` = <annotated>

### 类 `ConsoleUsageDay`  L84
- 继承: BaseModel
- _文档首行_: Token usage aggregated over one local-time day.
- 类/实例变量:
  - `date` = Field(..., description='Local date (YYYY-MM-DD) per the r...
  - `total_tokens` = 0
  - `input_tokens` = 0
  - `output_tokens` = 0
  - `runs` = 0
  - `cost` = Field(default=0.0, description='Estimated spend for the d...

### 类 `ConsoleUsageModelBreakdown`  L95
- 继承: BaseModel
- _文档首行_: Token usage attributed to one model.
- 类/实例变量:
  - `tokens` = 0
  - `runs` = Field(default=0, description='Runs that used this model (...
  - `cost` = Field(default=None, description='Estimated spend for this...
  - `input_tokens` = Field(default=0, description='Input tokens attributed to ...
  - `cache_read_tokens` = Field(default=0, description='Prompt-cache-hit input toke...

### 类 `ConsoleUsageResponse`  L105
- 继承: BaseModel
- _文档首行_: Daily token-usage series plus per-model breakdown for the window.
- 类/实例变量:
  - `days` = <annotated>
  - `by_model` = <annotated>
  - `total_tokens` = <annotated>
  - `total_runs` = <annotated>
  - `total_cost` = Field(default=None, description='Estimated spend for the ...
  - `currency` = Field(default=None, description='Display currency taken f...

### 类 `_ModelPricing`  L143
- 继承: NamedTuple
- 类/实例变量:
  - `input_per_million` = <annotated>
  - `output_per_million` = <annotated>
  - `currency` = <annotated>
  - `input_cache_hit_per_million` = None

## 文件内调用关系
- `_run_cost` -> _lookup_pricing, _token_cost
- `console_stats` -> _session_factory_or_503, _build_pricing_map, _run_cost, _pricing_currency
- `console_runs` -> _session_factory_or_503, _build_pricing_map, _as_utc, _run_cost
- `console_usage` -> _session_factory_or_503, _build_pricing_map, _as_utc, _run_cost, _lookup_pricing, _token_cost, _pricing_currency

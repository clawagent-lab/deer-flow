# `backend/packages/harness/deerflow/config/scheduler_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/scheduler_config.py`  ·  行数: 10

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 类
### 类 `SchedulerConfig`  L4
- 继承: BaseModel
- 类/实例变量:
  - `enabled` = Field(default=False)
  - `poll_interval_seconds` = Field(default=5, ge=1, le=300)
  - `lease_seconds` = Field(default=120, ge=5, le=3600)
  - `max_concurrent_runs` = Field(default=3, ge=1, le=32)
  - `min_once_delay_seconds` = Field(default=60, ge=1, le=86400)

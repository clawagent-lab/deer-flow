# `backend/packages/harness/deerflow/config/run_events_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/run_events_config.py`  ·  行数: 34

**模块文档首行**（仅供参考）: Run event storage configuration.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Literal
- `pydantic` -> BaseModel, Field

## 类
### 类 `RunEventsConfig`  L21
- 继承: BaseModel
- 类/实例变量:
  - `backend` = Field(default='memory', description="Storage backend for ...
  - `max_trace_content` = Field(default=10240, description='Maximum trace content s...
  - `track_token_usage` = Field(default=True, description='Whether RunJournal shoul...

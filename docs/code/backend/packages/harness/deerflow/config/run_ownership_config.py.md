# `backend/packages/harness/deerflow/config/run_ownership_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/run_ownership_config.py`  ·  行数: 48

**模块文档首行**（仅供参考）: Run ownership configuration for multi-worker deployments.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `pydantic` -> BaseModel, Field

## 类
### 类 `RunOwnershipConfig`  L8
- 继承: BaseModel
- _文档首行_: Per-run ownership and lease configuration.
- 类/实例变量:
  - `lease_seconds` = Field(default=30, ge=5, description='Seconds before a run...
  - `grace_seconds` = Field(default=10, ge=0, description='Extra seconds past l...
  - `heartbeat_enabled` = Field(default=False, description='When True, the worker p...

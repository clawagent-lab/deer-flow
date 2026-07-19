# `backend/packages/harness/deerflow/config/safety_finish_reason_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/safety_finish_reason_config.py`  ·  行数: 48

**模块文档首行**（仅供参考）: Configuration for SafetyFinishReasonMiddleware.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `pydantic` -> BaseModel, Field

## 类
### 类 `SafetyDetectorConfig`  L14
- 继承: BaseModel
- _文档首行_: One detector entry under ``safety_finish_reason.detectors``.
- 类/实例变量:
  - `use` = Field(description="Class path of a SafetyTerminationDetec...
  - `config` = Field(default_factory=dict, description='Constructor kwar...

### 类 `SafetyFinishReasonConfig`  L26
- 继承: BaseModel
- _文档首行_: Configuration for the SafetyFinishReasonMiddleware.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Master switch for the Sa...
  - `detectors` = Field(default=None, description='Custom detector list. Le...

# `backend/packages/harness/deerflow/config/input_polish_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/input_polish_config.py`  ·  行数: 10

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 类
### 类 `InputPolishConfig`  L4
- 继承: BaseModel
- _文档首行_: Configuration for pre-send input polishing.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether to enable pre-se...
  - `max_chars` = Field(default=4000, ge=1, description='Maximum number of ...
  - `model_name` = Field(default=None, description='Optional model name over...

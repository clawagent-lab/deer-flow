# `backend/packages/harness/deerflow/config/read_before_write_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/read_before_write_config.py`  ·  行数: 19

**模块文档首行**（仅供参考）: Configuration for the read-before-write file gate middleware (issue #3857).

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 类
### 类 `ReadBeforeWriteConfig`  L6
- 继承: BaseModel
- _文档首行_: Deterministic version gate on file-modifying tools.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether to block writes ...

# `backend/packages/harness/deerflow/config/skill_scan_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/skill_scan_config.py`  ·  行数: 13

**模块文档首行**（仅供参考）: Configuration for native skill safety scanning.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 类
### 类 `SkillScanConfig`  L6
- 继承: BaseModel
- _文档首行_: Configuration for deterministic SkillScan analyzers.
- 类/实例变量:
  - `enabled` = Field(default=True, description='Whether native determini...

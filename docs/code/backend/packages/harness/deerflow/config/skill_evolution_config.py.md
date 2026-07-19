# `backend/packages/harness/deerflow/config/skill_evolution_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/skill_evolution_config.py`  ·  行数: 15

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `pydantic` -> BaseModel, Field

## 类
### 类 `SkillEvolutionConfig`  L4
- 继承: BaseModel
- _文档首行_: Configuration for agent-managed skill evolution.
- 类/实例变量:
  - `enabled` = Field(default=False, description='Whether the agent can c...
  - `moderation_model_name` = Field(default=None, description='Optional model name for ...

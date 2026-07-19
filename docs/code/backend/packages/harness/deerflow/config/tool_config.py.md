# `backend/packages/harness/deerflow/config/tool_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/tool_config.py`  ·  行数: 21

## 模块概览
- 函数 0 个，类 2 个，模块级常量 0 个

## 依赖（import）
- `pydantic` -> BaseModel, ConfigDict, Field

## 类
### 类 `ToolGroupConfig`  L4
- 继承: BaseModel
- _文档首行_: Config section for a tool group
- 类/实例变量:
  - `name` = Field(..., description='Unique name for the tool group')
  - `model_config` = ConfigDict(extra='allow')

### 类 `ToolConfig`  L11
- 继承: BaseModel
- _文档首行_: Config section for a tool
- 类/实例变量:
  - `name` = Field(..., description='Unique name for the tool')
  - `group` = Field(..., description='Group name for the tool')
  - `use` = Field(..., description='Variable name of the tool provide...
  - `model_config` = ConfigDict(extra='allow')

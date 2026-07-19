# `backend/packages/harness/deerflow/runtime/runs/schemas.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/runs/schemas.py`  ·  行数: 22

**模块文档首行**（仅供参考）: Run status and disconnect mode enums.

## 模块概览
- 函数 0 个，类 2 个，模块级常量 0 个

## 依赖（import）
- `enum` -> StrEnum

## 类
### 类 `RunStatus`  L6
- 继承: StrEnum
- _文档首行_: Lifecycle status of a single run.
- 类/实例变量:
  - `pending` = 'pending'
  - `running` = 'running'
  - `success` = 'success'
  - `error` = 'error'
  - `timeout` = 'timeout'
  - `interrupted` = 'interrupted'

### 类 `DisconnectMode`  L17
- 继承: StrEnum
- _文档首行_: Behaviour when the SSE consumer disconnects.
- 类/实例变量:
  - `cancel` = 'cancel'
  - `continue_` = 'continue'

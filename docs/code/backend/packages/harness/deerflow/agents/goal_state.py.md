# `backend/packages/harness/deerflow/agents/goal_state.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/goal_state.py`  ·  行数: 32

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `typing` -> Any, Literal, NotRequired, TypedDict

## 模块级常量
- `GoalBlocker` = Literal['none', 'missing_evidence', 'needs_user_input', '...

## 类
### 类 `GoalEvaluation`  L15
- 继承: TypedDict
- 类/实例变量:
  - `satisfied` = <annotated>
  - `blocker` = <annotated>
  - `reason` = <annotated>
  - `evidence_summary` = <annotated>

### 类 `GoalState`  L22
- 继承: TypedDict
- 类/实例变量:
  - `objective` = <annotated>
  - `status` = <annotated>
  - `created_at` = <annotated>
  - `updated_at` = <annotated>
  - `continuation_count` = <annotated>
  - `max_continuations` = <annotated>
  - `no_progress_count` = <annotated>
  - `max_no_progress_continuations` = <annotated>
  - `last_evaluation` = <annotated>

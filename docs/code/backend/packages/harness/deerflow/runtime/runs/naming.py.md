# `backend/packages/harness/deerflow/runtime/runs/naming.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/runs/naming.py`  ·  行数: 17

**模块文档首行**（仅供参考）: Run naming helpers for LangChain/LangSmith tracing.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Any

## 函数
#### `ƒ` `resolve_root_run_name(config: Mapping[str, Any], assistant_id: str | None) -> str`  L9
  - 分支数 3，函数体节点数 79；return: agent_name, assistant_id or 'lead_agent'
  - 调用: get, isinstance, strip

## 文件内调用关系
_无文件内调用_

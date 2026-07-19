# `backend/packages/harness/deerflow/tools/builtins/clarification_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/clarification_tool.py`  ·  行数: 56

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `typing` -> Literal
- `langchain.tools` -> tool

## 函数
#### `ƒ` `ask_clarification_tool(question: str, clarification_type: Literal['missing_info', 'ambiguous_requirement', 'approach_choice', 'risk_confirmation', 'suggestion'], context: str | None, options: list[str] | None) -> str`    @tool(...)  L7
  - _文档首行_（仅供参考）: Ask the user for clarification when you need more information to proceed.
  - 分支数 0，函数体节点数 49；return: 'Clarification request processed by middleware'
  - 调用: tool

## 文件内调用关系
_无文件内调用_

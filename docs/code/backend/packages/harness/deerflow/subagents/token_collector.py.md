# `backend/packages/harness/deerflow/subagents/token_collector.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/subagents/token_collector.py`  ·  行数: 84

**模块文档首行**（仅供参考）: Callback handler that collects LLM token usage within a subagent.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Any
- `langchain_core.callbacks` -> BaseCallbackHandler

## 类
### 类 `SubagentTokenCollector`  L16
- 继承: BaseCallbackHandler
- _文档首行_: Lightweight callback handler that collects LLM token usage within a subagent.
- 方法:
  #### `m` `__init__(self, caller: str)`  L19
    - 分支数 0，函数体节点数 62
    - 调用: __init__, super, set
  #### `m` `on_llm_end(self, response: Any, *, run_id: Any, tags: list[str] | None, **kwargs) -> None`  L25
    - 分支数 10，函数体节点数 329；可变参数（*args/**kwargs）；return: None
    - 调用: str, hasattr, getattr, dict, get, isinstance, max, int, add, append
  - 反射: hasattr (L39), getattr (L41), getattr (L61)
  #### `m` `snapshot_records(self) -> list[dict[str, int | str | None]]`  L81
    - _文档首行_（仅供参考）: Return a copy of the accumulated usage records.
    - 分支数 0，函数体节点数 34；return: list(self._records)
    - 调用: list

## 文件内调用关系
- `SubagentTokenCollector.__init__` -> __init__

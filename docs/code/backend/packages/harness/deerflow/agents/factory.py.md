# `backend/packages/harness/deerflow/agents/factory.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/factory.py`  ·  行数: 410

**模块文档首行**（仅供参考）: Pure-argument factory for DeerFlow agents.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 3 个

## 依赖（import）
- 模块: logging
- `__future__` -> annotations
- `typing` -> TYPE_CHECKING
- `langchain.agents` -> create_agent
- `langchain.agents.middleware` -> AgentMiddleware
- `deerflow.agents.features` -> RuntimeFeatures
- `deerflow.agents.middlewares.clarification_middleware` -> ClarificationMiddleware
- `deerflow.agents.middlewares.dangling_tool_call_middleware` -> DanglingToolCallMiddleware
- `deerflow.agents.middlewares.tool_error_handling_middleware` -> ToolErrorHandlingMiddleware
- `deerflow.agents.thread_state` -> ThreadState
- `deerflow.tools.builtins` -> ask_clarification_tool

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_TODO_SYSTEM_PROMPT` = '\n<todo_list_system>\nYou have access to the `write_todo...
- `_TODO_TOOL_DESCRIPTION` = 'Use this tool to create and manage a structured task lis...

## 函数
#### `ƒ` `create_deerflow_agent(model: BaseChatModel, tools: list[BaseTool] | None, *, system_prompt: str | None, middleware: list[AgentMiddleware] | None, features: RuntimeFeatures | None, extra_middleware: list[AgentMiddleware] | None, plan_mode: bool, state_schema: type | None, checkpointer: BaseCheckpointSaver | None, name: str) -> CompiledStateGraph`  L63
  - _文档首行_（仅供参考）: Create a DeerFlow agent from plain Python arguments.
  - 分支数 8，函数体节点数 292；raise: ValueError("Cannot specify both 'middleware' and 'features'.  Use one or the other."), ValueError("Cannot use 'extra_middleware' with 'middleware' (full takeover)."), TypeError(f'extra_middleware items must be AgentMiddleware instances, got {type(mw).__name__}')；return: create_agent(model=model, tools=effective_tools or None, middleware=effective_middleware, system_prompt=system_prompt, state_schema=effective_state, checkpointer=checkpointer, name=name)
  - 调用: ValueError, isinstance, TypeError, type, list, RuntimeFeatures, _assemble_from_features, append, add, create_agent

#### `ƒ` `_assemble_from_features(feat: RuntimeFeatures, *, name: str, plan_mode: bool, extra_middleware: list[AgentMiddleware] | None) -> tuple[list[AgentMiddleware], list[BaseTool]]`  L157
  - _文档首行_（仅供参考）: Build an ordered middleware chain + extra tools from *feat*.
  - 分支数 26，函数体节点数 712；raise: ValueError('guardrail=True requires a custom AgentMiddleware instance (no built-in GuardrailMiddleware yet)'), ValueError('summarization=True requires a custom AgentMiddleware instance (SummarizationMiddleware needs a model argument)')；return: (chain, extra_tools)
  - 调用: isinstance, append, ThreadDataMiddleware, UploadsMiddleware, SandboxMiddleware, DanglingToolCallMiddleware, ValueError, ToolErrorHandlingMiddleware, TodoMiddleware, TitleMiddleware, get_memory_config, should_use_memory_tools, get_memory_tools, warning, add, MemoryMiddleware, ViewImageMiddleware, SubagentLimitMiddleware, from_config, LoopDetectionConfig（+7）

#### `ƒ` `_insert_extra(chain: list[AgentMiddleware], extras: list[AgentMiddleware]) -> None`  L336
  - _文档首行_（仅供参考）: Insert extra middlewares into *chain* using ``@Next``/``@Prev`` anchors.
  - 分支数 16，函数体节点数 681；raise: ValueError(f'{type(mw).__name__} cannot have both @Next and @Prev'), ValueError(f'Conflict: {type(mw).__name__} and {next_targets[next_anchor].__name__} both @Next({next_anchor.__name__})'), ValueError(f'Conflict: {type(mw).__name__} @Next({next_anchor.__name__}) and {prev_targets[next_anchor].__name__} @Prev({next_anchor.__name__}) — use cross-anchoring between extras instead'), ValueError(f'Conflict: {type(mw).__name__} and {prev_targets[prev_anchor].__name__} both @Prev({prev_anchor.__name__})'), ValueError(f'Conflict: {type(mw).__name__} @Prev({prev_anchor.__name__}) and {next_targets[prev_anchor].__name__} @Next({prev_anchor.__name__}) — use cross-anchoring between extras instead'), ValueError(f"Circular dependency among extra middlewares: {', '.join((t.__name__ for t in circular))}"), ValueError(f"Cannot resolve positions for {', '.join(names)} — anchors {', '.join((a.__name__ for _, _, a in remaining))} not found in chain")
  - 调用: getattr, type, ValueError, append, next, enumerate, isinstance, insert, list, len, range, join
  - 反射: getattr (L353), getattr (L354)

## 文件内调用关系
- `create_deerflow_agent` -> _assemble_from_features
- `_assemble_from_features` -> _insert_extra

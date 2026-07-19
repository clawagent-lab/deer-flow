# `backend/packages/harness/deerflow/runtime/context_compaction.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/context_compaction.py`  ·  行数: 143

**模块文档首行**（仅供参考）: Manual thread-context compaction helpers.

## 模块概览
- 函数 3 个，类 3 个，模块级常量 0 个

## 依赖（import）
- 模块: hashlib
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `types` -> SimpleNamespace
- `typing` -> Any
- `langgraph.checkpoint.base` -> uuid6
- `deerflow.agents.middlewares.summarization_middleware` -> DeerFlowSummarizationMiddleware, create_summarization_middleware
- `deerflow.config.app_config` -> AppConfig, get_app_config
- `deerflow.runtime.goal` -> _call_checkpointer_method, _next_channel_version
- `deerflow.utils.time` -> now_iso

## 函数
#### `ƒ` `_create_compaction_middleware(*, app_config: AppConfig, keep: tuple[str, int | float] | None) -> DeerFlowSummarizationMiddleware`  L40
  - 分支数 1，函数体节点数 51；raise: ContextCompactionDisabled('Context compaction is disabled.')；return: middleware
  - 调用: create_summarization_middleware, ContextCompactionDisabled

#### `ƒ` `_checkpoint_namespace(checkpoint_tuple: Any) -> str`  L51
  - 分支数 0，函数体节点数 70；return: checkpoint_ns if isinstance(checkpoint_ns, str) else ''
  - 调用: getattr, isinstance, get
  - 反射: getattr (L52)

#### `⏵ƒ` `async compact_thread_context(checkpointer: Any, thread_id: str, *, keep: tuple[str, int | float] | None, force: bool, user_id: str | None, agent_name: str | None, app_config: AppConfig | None) -> ThreadCompactionResult`  L58
  - _文档首行_（仅供参考）: Summarize old messages in a thread and write a compacted checkpoint.
  - 分支数 6，函数体节点数 636；raise: LookupError(f'Thread {thread_id} checkpoint not found')；return: ThreadCompactionResult(thread_id=thread_id, compacted=False, reason='not_enough_messages'), ThreadCompactionResult(thread_id=thread_id, compacted=True, removed_message_count=len(result.messages_to_summarize), preserved_message_count=len(result.preserved_messages), summary_updated=True, checkpoint_id=new_checkpoint_id, total_tokens=result.total_tokens)
  - 调用: get_app_config, _create_compaction_middleware, _call_checkpointer_method, LookupError, dict, getattr, get, isinstance, ThreadCompactionResult, list, SimpleNamespace, acompact_state, _next_channel_version, str, uuid6, now_iso, len, hexdigest, sha256, encode（+1）
  - 反射: getattr (L77), getattr (L78)

## 类
### 类 `ContextCompactionDisabled`  L18
- 继承: RuntimeError
- _文档首行_: Raised when manual compaction is requested while summarization is disabled.

### 类 `ContextCompactionFailed`  L22
- 继承: RuntimeError
- _文档首行_: Raised when a compressible thread cannot be summarized.

### 类 `ThreadCompactionResult`  L27  @dataclass(...)
- _文档首行_: Result returned after a manual context-compaction attempt.
- 类/实例变量:
  - `thread_id` = <annotated>
  - `compacted` = <annotated>
  - `reason` = None
  - `removed_message_count` = 0
  - `preserved_message_count` = 0
  - `summary_updated` = False
  - `checkpoint_id` = None
  - `total_tokens` = 0

## 文件内调用关系
- `compact_thread_context` -> _create_compaction_middleware, _checkpoint_namespace

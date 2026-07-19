# `backend/packages/harness/deerflow/utils/oneshot_llm.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/utils/oneshot_llm.py`  ·  行数: 73

**模块文档首行**（仅供参考）: Shared helper for one-shot, non-graph LLM text requests.

## 模块概览
- 函数 2 个，类 0 个，模块级常量 0 个

## 依赖（import）
- 模块: os
- `__future__` -> annotations
- `langchain_core.messages` -> HumanMessage, SystemMessage
- `deerflow.config.app_config` -> AppConfig
- `deerflow.models` -> create_chat_model
- `deerflow.runtime.user_context` -> get_effective_user_id
- `deerflow.tracing` -> inject_langfuse_metadata
- `deerflow.utils.llm_text` -> extract_response_text

## 函数
#### `ƒ` `_resolve_environment() -> str | None`  L29
  - 分支数 0，函数体节点数 26；return: os.environ.get('DEER_FLOW_ENV') or os.environ.get('ENVIRONMENT')
  - 调用: get

#### `⏵ƒ` `async run_oneshot_llm(*, system_instruction: str, user_content: str, run_name: str, app_config: AppConfig, model_name: str | None, thread_id: str | None) -> str`  L33
  - _文档首行_（仅供参考）: Run a single non-graph system+user LLM turn and return the raw text.
  - 分支数 0，函数体节点数 112；return: extract_response_text(response.content)
  - 调用: create_chat_model, inject_langfuse_metadata, get_effective_user_id, _resolve_environment, ainvoke, SystemMessage, HumanMessage, extract_response_text

## 文件内调用关系
- `run_oneshot_llm` -> _resolve_environment

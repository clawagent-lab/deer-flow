# `backend/scripts/e2e_safety_termination_demo.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/scripts/e2e_safety_termination_demo.py`  ·  行数: 207

**模块文档首行**（仅供参考）: End-to-end demo: SafetyFinishReasonMiddleware on the real DeerFlow lead-agent.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: sys
- `__future__` -> annotations
- `typing` -> Any
- `langchain_core.language_models` -> BaseChatModel
- `langchain_core.messages` -> AIMessage
- `langchain_core.outputs` -> ChatGeneration, ChatResult

## 函数
#### `ƒ` `main() -> int`  L85
  - 分支数 13，函数体节点数 772；return: fake, 1, 0
  - 调用: _ContentFilteredFakeModel, DeerFlowClient, print, stream, append, next, isinstance, get, reversed, len, items, type, str

## 类
### 类 `_ContentFilteredFakeModel`  L32
- 继承: BaseChatModel
- _文档首行_: First call returns finish_reason=content_filter + truncated write_file
- 类/实例变量:
  - `call_count` = 0
- 方法:
  #### `prop` `_llm_type(self) -> str`    @property  L42
    - 分支数 0，函数体节点数 9；return: 'fake-content-filtered'
  #### `m` `bind_tools(self, tools, **kwargs)`  L45
    - 分支数 0，函数体节点数 8；可变参数（*args/**kwargs）；return: self
  #### `m` `_generate(self, messages, stop, run_manager, **kwargs)`  L48
    - 分支数 1，函数体节点数 81；可变参数（*args/**kwargs）；return: ChatResult(generations=[ChatGeneration(message=msg)])
    - 调用: AIMessage, ChatResult, ChatGeneration
  #### `⏵m` `async _agenerate(self, messages, stop, run_manager, **kwargs)`  L76
    - 分支数 0，函数体节点数 26；可变参数（*args/**kwargs）；return: self._generate(messages, stop=stop, run_manager=run_manager, **kwargs)
    - 调用: _generate

## 文件内调用关系
- `_ContentFilteredFakeModel._agenerate` -> _generate

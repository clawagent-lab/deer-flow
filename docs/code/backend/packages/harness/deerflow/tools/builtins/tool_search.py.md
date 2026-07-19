# `backend/packages/harness/deerflow/tools/builtins/tool_search.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/tool_search.py`  ·  行数: 342

**模块文档首行**（仅供参考）: Tool search — deferred tool discovery at runtime.

## 模块概览
- 函数 11 个，类 2 个，模块级常量 2 个

## 依赖（import）
- 模块: hashlib, html, json, logging, re
- `collections.abc` -> Iterable
- `dataclasses` -> dataclass
- `functools` -> cached_property
- `typing` -> TYPE_CHECKING, Annotated, Any
- `langchain.tools` -> BaseTool
- `langchain_core.messages` -> ToolMessage
- `langchain_core.tools` -> InjectedToolCallId, tool
- `langchain_core.utils.function_calling` -> convert_to_openai_function
- `langgraph.types` -> Command
- `deerflow.tools.mcp_metadata` -> get_mcp_routing, is_mcp_tool

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `MAX_RESULTS` = 5

## 函数
#### `ƒ` `_compile_catalog_regex(pattern: str) -> re.Pattern[str]`  L45
  - _文档首行_（仅供参考）: Compile ``pattern`` case-insensitively, falling back to a literal match.
  - 分支数 1，函数体节点数 50；return: re.compile(pattern, re.IGNORECASE), re.compile(re.escape(pattern), re.IGNORECASE)
  - 调用: compile, escape
  - 危险执行: compile (L52), compile (L54)

#### `ƒ` `_catalog_regex_score(pattern: str, t: BaseTool) -> int`  L112
  - 分支数 0，函数体节点数 42；return: len(regex.findall(f"{t.name} {t.description or ''}"))
  - 调用: _compile_catalog_regex, len, findall

#### `ƒ` `build_tool_search_tool(catalog: DeferredToolCatalog) -> BaseTool`  L142
  - 分支数 1，函数体节点数 134；return: Command(update={'promoted': {'catalog_hash': catalog_hash, 'names': names}, 'messages': [ToolMessage(content=content, tool_call_id=tool_call_id, name='tool_search')]}), tool_search
  - 调用: search, dumps, convert_to_openai_function, Command, ToolMessage

#### `ƒ` `build_deferred_tool_setup(candidate_tools: list[BaseTool], *, enabled: bool) -> DeferredToolSetup`  L175
  - _文档首行_（仅供参考）: Build deferred-tool setup from one agent build's candidate tools.
  - 分支数 2，函数体节点数 88；return: DeferredToolSetup(None, frozenset(), None), DeferredToolSetup(build_tool_search_tool(catalog), catalog.names, catalog.hash)
  - 调用: DeferredToolSetup, frozenset, is_mcp_tool, DeferredToolCatalog, tuple, build_tool_search_tool

#### `ƒ` `assemble_deferred_tools(candidate_tools: list[BaseTool], *, enabled: bool) -> tuple[list[BaseTool], DeferredToolSetup]`  L200
  - _文档首行_（仅供参考）: Build the final tool list and deferred setup from candidate tools.
  - 分支数 2，函数体节点数 99；raise: RuntimeError('tool_search enabled and MCP candidates exist, but no deferred set was recovered - refusing to bind MCP schemas (fail-closed).')；return: (final_tools, deferred_setup)
  - 调用: build_deferred_tool_setup, any, is_mcp_tool, RuntimeError, list, append

#### `ƒ` `_routing_priority(value: Any) -> int`  L221
  - 分支数 1，函数体节点数 23；return: int(value), 0
  - 调用: int

#### `ƒ` `_routing_keywords(value: Any) -> list[str]`  L231
  - 分支数 1，函数体节点数 47；return: [], [keyword for keyword in (str(item).strip() for item in value) if keyword]
  - 调用: isinstance, strip, str

#### `ƒ` `build_mcp_routing_middleware(tools: Iterable[BaseTool], deferred_setup: DeferredToolSetup, *, top_k: int) -> 'AgentMiddleware | None'`  L239
  - _文档首行_（仅供参考）: Build PR2 auto-promotion middleware from the caller's deferred tools.
  - 分支数 7，函数体节点数 192；return: None, McpRoutingMiddleware(routing_index, deferred_setup.catalog_hash, top_k)
  - 调用: getattr, get_mcp_routing, get, _routing_keywords, debug, str, _routing_priority, McpRoutingMiddleware
  - 反射: getattr (L255)

#### `ƒ` `get_deferred_tools_prompt_section(*, deferred_names: frozenset[str]) -> str`  L282
  - _文档首行_（仅供参考）: Generate <available-deferred-tools> from an explicit deferred-name set.
  - 分支数 1，函数体节点数 55；return: '', f'<available-deferred-tools>\n{names}\n</available-deferred-tools>'
  - 调用: frozenset, join, escape, sorted

#### `ƒ` `_format_keyword_list(keywords: list[str]) -> str`  L304
  - 分支数 1，函数体节点数 50；return: keywords[0], f"{', '.join(keywords[:-1])}, or {keywords[-1]}"
  - 调用: len, join

#### `ƒ` `get_mcp_routing_hints_prompt_section(tools: Iterable[BaseTool], *, deferred_names: frozenset[str]) -> str`  L310
  - _文档首行_（仅供参考）: Render <mcp_routing_hints> from MCP tools carrying routing metadata.
  - 分支数 6，函数体节点数 255；return: '', '\n'.join(lines)
  - 调用: frozenset, get_mcp_routing, get, append, int, escape, str, sorted, _format_keyword_list, join

## 类
### 类 `DeferredToolCatalog`  L64  @dataclass(...)
- _文档首行_: Immutable catalog of deferred tools. Pure search, no mutation.
- 类/实例变量:
  - `tools` = <annotated>
- 方法:
  #### `m` `names(self) -> frozenset[str]`    @cached_property  L70
    - 分支数 0，函数体节点数 27；return: frozenset((t.name for t in self.tools))
    - 调用: frozenset
  #### `m` `hash(self) -> str`    @cached_property  L74
    - 分支数 0，函数体节点数 77；return: hashlib.sha256(blob.encode('utf-8')).hexdigest()[:16]
    - 调用: convert_to_openai_function, sorted, dumps, hexdigest, sha256, encode
  #### `m` `search(self, query: str) -> list[BaseTool]`  L79
    - 分支数 7，函数体节点数 296；return: [], [t for t in self.tools if t.name in wanted], candidates[:MAX_RESULTS], [t for _, t in scored][:MAX_RESULTS]
    - 调用: strip, startswith, split, lower, len, sort, _catalog_regex_score, _compile_catalog_regex, search, append

### 类 `DeferredToolSetup`  L121  @dataclass(...)
- _文档首行_: Result of assembling deferred-tool support for one agent build.
- 类/实例变量:
  - `tool_search_tool` = <annotated>
  - `deferred_names` = <annotated>
  - `catalog_hash` = <annotated>

## 文件内调用关系
- `_catalog_regex_score` -> _compile_catalog_regex
- `build_tool_search_tool` -> search
- `build_deferred_tool_setup` -> build_tool_search_tool
- `assemble_deferred_tools` -> build_deferred_tool_setup
- `build_mcp_routing_middleware` -> _routing_keywords, _routing_priority
- `get_mcp_routing_hints_prompt_section` -> _format_keyword_list
- `DeferredToolCatalog.search` -> _catalog_regex_score, _compile_catalog_regex, search

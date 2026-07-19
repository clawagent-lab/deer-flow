# `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/prompt.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/memory/backends/deermem/deermem/core/prompt.py`  ·  行数: 856

**模块文档首行**（仅供参考）: Prompt templates for memory update and injection.

## 模块概览
- 函数 11 个，类 0 个，模块级常量 10 个

## 依赖（import）
- 模块: html, logging, math, re, threading, time
- `__future__` -> annotations
- `typing` -> Any, cast

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `MEMORY_UPDATE_PROMPT` = 'You are a memory management system. Your task is to anal...
- `STALENESS_REVIEW_PROMPT` = '## Staleness Review\n\nThe following facts have reached ...
- `CONSOLIDATION_PROMPT` = '## Memory Consolidation\n\nThe following fact categories...
- `FACT_EXTRACTION_PROMPT` = 'Extract factual information about the user from this mes...
- `_TIKTOKEN_ENCODING_MISSING` = object()
- `_TIKTOKEN_ENCODING_LOADING` = object()
- `_TIKTOKEN_RETRY_COOLDOWN_S` = 600.0
- `_tiktoken_encoding_cache` = {}
- `_tiktoken_encoding_cache_lock` = threading.Lock()

## 函数
#### `ƒ` `_get_tiktoken_encoding(encoding_name: str) -> tiktoken.Encoding | None`  L285
  - _文档首行_（仅供参考）: Return a cached tiktoken encoding, or ``None`` on failure / unavailability.
  - 分支数 9，函数体节点数 170；return: None, cast('tiktoken.Encoding', cached), encoding
  - 调用: get, isinstance, monotonic, cast, get_encoding, warning

#### `ƒ` `_char_based_token_estimate(text: str) -> int`  L332
  - _文档首行_（仅供参考）: Network-free token estimate that accounts for CJK density.
  - 分支数 0，函数体节点数 65；return: (len(text) - cjk) // 4 + cjk // 2
  - 调用: sum, len

#### `ƒ` `_count_tokens(text: str, encoding_name: str, *, use_tiktoken: bool) -> int`  L352
  - _文档首行_（仅供参考）: Count tokens in text using tiktoken.
  - 分支数 3，函数体节点数 69；return: _char_based_token_estimate(text), len(encoding.encode(text))
  - 调用: _char_based_token_estimate, _get_tiktoken_encoding, len, encode

#### `ƒ` `warm_tiktoken_cache() -> bool`  L381
  - _文档首行_（仅供参考）: Pre-warm the tiktoken encoding cache.
  - 分支数 0，函数体节点数 14；return: _get_tiktoken_encoding('cl100k_base') is not None
  - 调用: _get_tiktoken_encoding

#### `ƒ` `_coerce_confidence(value: Any, default: float) -> float`  L392
  - _文档首行_（仅供参考）: Coerce a confidence-like value to a bounded float in [0, 1].
  - 分支数 2，函数体节点数 72；return: max(0.0, min(1.0, default)), max(0.0, min(1.0, confidence))
  - 调用: float, max, min, isfinite

#### `ƒ` `_format_fact_line(fact: dict[str, Any]) -> str | None`  L408
  - _文档首行_（仅供参考）: Build a single formatted fact line, or return ``None`` for invalid facts.
  - 分支数 3，函数体节点数 194；return: None, f'- [{category} | {confidence:.2f}] {content} (avoid: {source_error})', f'- [{category} | {confidence:.2f}] {content}'
  - 调用: get, isinstance, strip, str, _coerce_confidence, escape

#### `ƒ` `_escape_summary(value: Any) -> str`  L438
  - _文档首行_（仅供参考）: Escape a user-editable context summary for the ``<memory>`` block.
  - 分支数 0，函数体节点数 22；return: html.escape(str(value), quote=False)
  - 调用: escape, str

#### `ƒ` `_select_fact_lines(ranked_facts: list[dict[str, Any]], *, token_budget: int, use_tiktoken: bool) -> tuple[list[str], int]`  L454
  - _文档首行_（仅供参考）: Greedily select formatted fact lines within a *line-only* token budget.
  - 分支数 3，函数体节点数 131；return: (lines, consumed)
  - 调用: _format_fact_line, _count_tokens, append

#### `ƒ` `_fallback_format_facts(valid_facts: list[dict[str, Any]], *, preceding_section_cost: int, max_tokens: int, use_tiktoken: bool) -> tuple[str, list[str]] | tuple[None, None]`  L498
  - _文档首行_（仅供参考）: Confidence-only ranking used when the primary path raises an exception.
  - 分支数 2，函数体节点数 159；return: (None, None), (header + '\n'.join(lines), lines)
  - 调用: sorted, _coerce_confidence, get, _count_tokens, _select_fact_lines, join

#### `ƒ` `format_memory_for_injection(memory_data: dict[str, Any], max_tokens: int, *, use_tiktoken: bool, guaranteed_categories: list[str] | None, guaranteed_token_budget: int) -> str`  L535
  - _文档首行_（仅供参考）: Format memory data for injection into system prompt.
  - 分支数 25，函数体节点数 1100；raise: TypeError('guaranteed_categories must be an iterable of strings, not a bare str')；return: '', _coerce_confidence(fact.get('confidence'), default=0.0), False, bool(cat) and cat in effective_guaranteed, result
  - 调用: isinstance, TypeError, frozenset, strip, get, append, _escape_summary, join, _count_tokens, _coerce_confidence, bool, sorted, _category_match, _select_fact_lines, warning, _fallback_format_facts, max, len, int, rstrip

#### `ƒ` `format_conversation_for_update(messages: list[Any]) -> str`  L800
  - _文档首行_（仅供参考）: Format conversation messages for memory update prompt.
  - 分支数 11，函数体节点数 244；return: '\n\n'.join(lines)
  - 调用: getattr, str, isinstance, append, get, join, strip, sub, len, escape
  - 反射: getattr (L811), getattr (L812)

## 文件内调用关系
- `_count_tokens` -> _char_based_token_estimate, _get_tiktoken_encoding
- `warm_tiktoken_cache` -> _get_tiktoken_encoding
- `_format_fact_line` -> _coerce_confidence
- `_select_fact_lines` -> _format_fact_line, _count_tokens
- `_fallback_format_facts` -> _coerce_confidence, _count_tokens, _select_fact_lines
- `format_memory_for_injection` -> _escape_summary, _count_tokens, _coerce_confidence, _select_fact_lines, _fallback_format_facts

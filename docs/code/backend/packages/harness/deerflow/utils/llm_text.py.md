# `backend/packages/harness/deerflow/utils/llm_text.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/utils/llm_text.py`  ·  行数: 61

**模块文档首行**（仅供参考）: Utilities for normalizing LLM response text before structured parsing.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: re
- `__future__` -> annotations

## 模块级常量
- `_THINK_BLOCK_RE` = re.compile('<think\\b[^>]*>.*?</think\\s*>', re.IGNORECAS...
- `_OPEN_THINK_RE` = re.compile('<think\\b[^>]*>', re.IGNORECASE)

## 函数
#### `ƒ` `strip_think_blocks(text: str, *, truncate_unclosed: bool) -> str`  L13
  - _文档首行_（仅供参考）: Remove inline reasoning ``<think>`` blocks from a model response.
  - 分支数 2，函数体节点数 59；return: text.strip()
  - 调用: sub, search, start, strip

#### `ƒ` `strip_markdown_code_fence(text: str) -> str`  L33
  - _文档首行_（仅供参考）: Remove a single wrapping markdown code fence when present.
  - 分支数 2，函数体节点数 88；return: stripped, '\n'.join(lines[1:-1]).strip()
  - 调用: strip, startswith, splitlines, len, join

#### `ƒ` `extract_response_text(content: object) -> str`  L44
  - _文档首行_（仅供参考）: Extract textual content from common chat-model response content shapes.
  - 分支数 7，函数体节点数 127；return: content, '\n'.join(parts), '', str(content)
  - 调用: isinstance, append, get, join, str

## 文件内调用关系
_无文件内调用_

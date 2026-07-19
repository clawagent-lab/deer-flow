# `backend/packages/harness/deerflow/sandbox/path_patterns.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/path_patterns.py`  ·  行数: 69

**模块文档首行**（仅供参考）: Shared construction of the host→virtual output-masking regexes.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 2 个

## 依赖（import）
- 模块: re
- `__future__` -> annotations

## 模块级常量
- `_SEGMENT_BOUNDARY` = '(?=/|$|[^\\w./-])'
- `_PATH_TAIL` = '(?:[/\\\\][^\\s\\"\';&|<>()]*)?'

## 函数
#### `ƒ` `build_output_mask_pattern(base: str, *, separator_agnostic: bool) -> re.Pattern[str]`  L47
  - _文档首行_（仅供参考）: Compile the matcher for one host ``base`` in model-visible output.
  - 分支数 1，函数体节点数 58；return: re.compile(escaped + _SEGMENT_BOUNDARY + _PATH_TAIL)
  - 调用: escape, replace, compile
  - 文件IO: replace (L67)
  - 危险执行: compile (L68)

## 文件内调用关系
_无文件内调用_

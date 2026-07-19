# `backend/packages/harness/deerflow/tui/theme.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/theme.py`  ·  行数: 43

**模块文档首行**（仅供参考）: Restrained colour + symbol palette for the TUI.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 2 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass

## 模块级常量
- `THEME` = Theme()
- `SYMBOLS` = {'user': '›', 'assistant': '●', 'tool': '⚙', 'running': '...

## 类
### 类 `Theme`  L14  @dataclass(...)
- 类/实例变量:
  - `bg` = '#1a1b26'
  - `panel` = '#1f2335'
  - `border` = '#2f334d'
  - `text` = '#c0caf5'
  - `dim` = '#565f89'
  - `muted` = '#737aa2'
  - `primary` = '#7dcfff'
  - `user` = '#7aa2f7'
  - `assistant` = '#c0caf5'
  - `tool` = '#bb9af7'
  - `accent` = '#9ece6a'
  - `warning` = '#e0af68'
  - `error` = '#f7768e'

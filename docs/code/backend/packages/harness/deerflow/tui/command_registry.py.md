# `backend/packages/harness/deerflow/tui/command_registry.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/command_registry.py`  ·  行数: 117

**模块文档首行**（仅供参考）: Slash-command registry for the DeerFlow TUI (pure).

## 模块概览
- 函数 3 个，类 2 个，模块级常量 2 个

## 依赖（import）
- `__future__` -> annotations
- `dataclasses` -> dataclass
- `typing` -> Literal

## 模块级常量
- `BUILTIN_COMMANDS` = (Command('help', 'Show commands and keybindings'), Comman...
- `_BUILTIN_NAMES` = frozenset((c.name for c in BUILTIN_COMMANDS))

## 函数
#### `ƒ` `build_registry(skills: list[dict]) -> list[Command]`  L59
  - _文档首行_（仅供参考）: Merge built-ins with one command per enabled skill.
  - 分支数 3，函数体节点数 92；return: commands
  - 调用: list, get, append, Command

#### `ƒ` `filter_commands(commands: list[Command], query: str) -> list[Command]`  L72
  - _文档首行_（仅供参考）: Filter + rank commands for the picker.
  - 分支数 5，函数体节点数 149；return: commands, prefix + substring + description
  - 调用: lower, strip, startswith, append

#### `ƒ` `resolve(text: str, skills: list[str] | None) -> Resolution`  L96
  - _文档首行_（仅供参考）: Classify a submitted input line.
  - 分支数 4，函数体节点数 153；return: Resolution(kind='message', text=text), Resolution(kind='unknown', name=''), Resolution(kind='builtin', name=name, args=args), Resolution(kind='skill', name=name, args=args), Resolution(kind='unknown', name=name, args=args)
  - 调用: strip, startswith, Resolution, partition

## 类
### 类 `Command`  L21  @dataclass(...)
- 类/实例变量:
  - `name` = <annotated>
  - `description` = <annotated>
  - `category` = 'builtin'

### 类 `Resolution`  L28  @dataclass(...)
- 类/实例变量:
  - `kind` = <annotated>
  - `name` = ''
  - `args` = ''
  - `text` = ''

## 文件内调用关系
_无文件内调用_

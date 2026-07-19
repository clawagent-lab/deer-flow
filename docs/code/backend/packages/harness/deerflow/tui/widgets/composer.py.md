# `backend/packages/harness/deerflow/tui/widgets/composer.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tui/widgets/composer.py`  ·  行数: 24

**模块文档首行**（仅供参考）: Composer input with a wide-character (CJK) cursor fix.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `textual.widgets` -> Input

## 类
### 类 `ComposerInput`  L19
- 继承: Input
- 方法:
  #### `prop` `_cursor_offset(self) -> int`    @property  L21
    - 分支数 0，函数体节点数 17；return: self._position_to_cell(self.cursor_position)
    - 调用: _position_to_cell

## 文件内调用关系
_无文件内调用_

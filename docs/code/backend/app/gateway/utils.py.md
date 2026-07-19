# `backend/app/gateway/utils.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/gateway/utils.py`  ·  行数: 7

**模块文档首行**（仅供参考）: Shared utility helpers for the Gateway layer.

## 模块概览
- 函数 1 个，类 0 个，模块级常量 0 个

## 函数
#### `ƒ` `sanitize_log_param(value: str) -> str`  L4
  - _文档首行_（仅供参考）: Strip control characters to prevent log injection.
  - 分支数 0，函数体节点数 27；return: value.replace('\n', '').replace('\r', '').replace('\x00', '')
  - 调用: replace
  - 文件IO: replace (L6), replace (L6), replace (L6)

## 文件内调用关系
_无文件内调用_

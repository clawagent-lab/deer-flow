# `backend/scripts/record_gateway.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/scripts/record_gateway.py`  ·  行数: 128

**模块文档首行**（仅供参考）: Recording gateway for *record-through-browser* (Plan A).

## 模块概览
- 函数 2 个，类 0 个，模块级常量 1 个

## 依赖（import）
- 模块: json, os, sys, tempfile
- `__future__` -> annotations
- `pathlib` -> Path

## 模块级常量
- `_BACKEND` = Path(__file__).resolve().parents[1]

## 函数
#### `ƒ` `_install_capture(out_path: Path) -> None`  L28
  - 分支数 7，函数体节点数 320；return: None, model
  - 调用: str, caller_identity, pop, getattr, hash_messages, hash_replay_input, messages_to_dict, open, write, dumps, flush, Capture, original, list, values
  - 文件IO: open (L70), write (L71)
  - 反射: getattr (L61), getattr (L84)

#### `ƒ` `main() -> int`  L88
  - 分支数 2，函数体节点数 310；return: 2, 0
  - 调用: get, print, int, Path, mkdir, write_text, mkdtemp, build_config_yaml, real_model_block, str, prepare_hermetic_extras, setdefault, join, _install_capture, run
  - 文件IO: mkdir (L101), write_text (L102), write_text (L108)
  - 子进程: run (L122)

## 文件内调用关系
- `main` -> _install_capture

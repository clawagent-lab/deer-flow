# `backend/app/channels/run_policy.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/app/channels/run_policy.py`  ·  行数: 103

**模块文档首行**（仅供参考）: Per-channel run policy registry.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Awaitable, Callable
- `dataclasses` -> dataclass
- `typing` -> TYPE_CHECKING, Any

## 模块级常量
- `CHANNEL_RUN_POLICY` = {}

## 类
### 类 `ChannelRunPolicy`  L24  @dataclass(...)
- _文档首行_: Per-channel knobs applied by :meth:`ChannelManager._apply_channel_policy`.
- 类/实例变量:
  - `is_interactive` = True
  - `default_recursion_limit` = None
  - `credentials_provider` = None
  - `requires_bound_identity` = True
  - `fire_and_forget` = False
  - `serialize_thread_runs` = False

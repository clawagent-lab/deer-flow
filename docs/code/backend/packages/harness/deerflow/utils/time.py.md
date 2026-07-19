# `backend/packages/harness/deerflow/utils/time.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/utils/time.py`  ·  行数: 96

**模块文档首行**（仅供参考）: ISO 8601 timestamp helpers for the Gateway and embedded runtime.

## 模块概览
- 函数 3 个，类 0 个，模块级常量 2 个
- `__all__`: coerce_iso, is_lease_expired, now_iso

## 依赖（import）
- 模块: re
- `__future__` -> annotations
- `datetime` -> UTC, datetime, timedelta

## 模块级常量
- `__all__` = ['coerce_iso', 'is_lease_expired', 'now_iso']
- `_UNIX_TIMESTAMP_PATTERN` = re.compile('^\\d{10}(?:\\.\\d+)?$')

## 函数
#### `ƒ` `is_lease_expired(lease_expires_at: str | None, *, grace_seconds: int) -> bool`  L23
  - _文档首行_（仅供参考）: Return ``True`` when *lease_expires_at* has elapsed past grace.
  - 分支数 3，函数体节点数 82；return: True, dt < datetime.now(UTC) - timedelta(seconds=grace_seconds)
  - 调用: fromisoformat, replace, now, timedelta
  - 文件IO: replace (L36)

#### `ƒ` `now_iso() -> str`  L50
  - _文档首行_（仅供参考）: Return the current UTC time as an ISO 8601 string.
  - 分支数 0，函数体节点数 17；return: datetime.now(UTC).isoformat()
  - 调用: isoformat, now

#### `ƒ` `coerce_iso(value: object) -> str`  L58
  - _文档首行_（仅供参考）: Best-effort coerce a stored timestamp to an ISO 8601 string.
  - 分支数 9，函数体节点数 179；return: '', str(value), value.isoformat(), datetime.fromtimestamp(float(value), UTC).isoformat(), value
  - 调用: isinstance, str, replace, astimezone, isoformat, fromtimestamp, float, match
  - 文件IO: replace (L79)

## 文件内调用关系
_无文件内调用_

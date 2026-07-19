# `backend/packages/harness/deerflow/scheduler/schedules.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/scheduler/schedules.py`  ·  行数: 56

## 模块概览
- 函数 3 个，类 0 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `zoneinfo` -> ZoneInfo, ZoneInfoNotFoundError
- `croniter` -> croniter

## 函数
#### `ƒ` `validate_timezone(timezone_name: str) -> str`  L9
  - 分支数 1，函数体节点数 31；raise: ValueError(f'Unknown timezone: {timezone_name}')；return: timezone_name
  - 调用: ZoneInfo, ValueError

#### `ƒ` `normalize_cron_expression(expr: str) -> str`  L17
  - 分支数 1，函数体节点数 44；raise: ValueError('Cron expression must contain exactly 5 fields')；return: ' '.join(parts)
  - 调用: split, len, ValueError, join

#### `ƒ` `next_run_at(schedule_type: str, schedule_spec: dict[str, object], timezone_name: str, *, now: datetime) -> datetime | None`  L24
  - 分支数 6，函数体节点数 216；raise: ValueError('once schedule requires run_at'), ValueError(f'Unsupported schedule_type: {schedule_type}')；return: run_at if run_at > now else None, next_local.astimezone(UTC)
  - 调用: validate_timezone, replace, get, isinstance, ValueError, fromisoformat, ZoneInfo, normalize_cron_expression, str, astimezone, get_next, croniter
  - 文件IO: replace (L33), replace (L43), replace (L52)

## 文件内调用关系
- `next_run_at` -> validate_timezone, normalize_cron_expression

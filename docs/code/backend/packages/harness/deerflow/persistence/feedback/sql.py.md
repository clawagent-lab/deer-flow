# `backend/packages/harness/deerflow/persistence/feedback/sql.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/feedback/sql.py`  ·  行数: 241

**模块文档首行**（仅供参考）: SQLAlchemy-backed feedback storage.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: uuid
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> case, func, select
- `sqlalchemy.ext.asyncio` -> AsyncSession, async_sessionmaker
- `deerflow.persistence.feedback.model` -> FeedbackRow
- `deerflow.runtime.user_context` -> AUTO, _AutoSentinel, resolve_user_id
- `deerflow.utils.time` -> coerce_iso

## 类
### 类 `FeedbackRepository`  L19
- 方法:
  #### `st` `_row_to_dict(row: FeedbackRow) -> dict`    @staticmethod  L24
    - 分支数 1，函数体节点数 48；return: d
    - 调用: to_dict, get, isinstance, coerce_iso
  #### `m` `__init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None`  L20
    - 分支数 0，函数体节点数 18
  #### `⏵m` `async create(self, *, run_id: str, thread_id: str, rating: int, user_id: str | None | _AutoSentinel, message_id: str | None, comment: str | None) -> dict`  L32
    - _文档首行_（仅供参考）: Create a feedback record. rating must be +1 or -1.
    - 分支数 2，函数体节点数 154；raise: ValueError(f'rating must be +1 or -1, got {rating}')；return: self._row_to_dict(row)
    - 调用: ValueError, resolve_user_id, FeedbackRow, str, uuid4, now, _sf, add, commit, refresh, _row_to_dict
  #### `⏵m` `async get(self, feedback_id: str, *, user_id: str | None | _AutoSentinel) -> dict | None`  L62
    - 分支数 3，函数体节点数 89；return: None, self._row_to_dict(row)
    - 调用: resolve_user_id, _sf, get, _row_to_dict
  - 网络调用: get (L70)
  #### `⏵m` `async list_by_run(self, thread_id: str, run_id: str, *, limit: int, user_id: str | None | _AutoSentinel) -> list[dict]`  L77
    - 分支数 2，函数体节点数 147；return: [self._row_to_dict(r) for r in result.scalars()]
    - 调用: resolve_user_id, where, select, limit, order_by, asc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async list_by_thread(self, thread_id: str, *, limit: int, user_id: str | None | _AutoSentinel) -> list[dict]`  L94
    - 分支数 2，函数体节点数 136；return: [self._row_to_dict(r) for r in result.scalars()]
    - 调用: resolve_user_id, where, select, limit, order_by, asc, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async delete(self, feedback_id: str, *, user_id: str | None | _AutoSentinel) -> bool`  L110
    - 分支数 3，函数体节点数 96；return: False, True
    - 调用: resolve_user_id, _sf, get, delete, commit
  - 网络调用: get (L118), delete (L123)
  #### `⏵m` `async upsert(self, *, run_id: str, thread_id: str, rating: int, user_id: str | None | _AutoSentinel, comment: str | None) -> dict`  L127
    - _文档首行_（仅供参考）: Create or update feedback for (thread_id, run_id, user_id). rating must be +1 or -1.
    - 分支数 3，函数体节点数 230；raise: ValueError(f'rating must be +1 or -1, got {rating}')；return: self._row_to_dict(row)
    - 调用: ValueError, resolve_user_id, _sf, where, select, execute, scalar_one_or_none, now, FeedbackRow, str, uuid4, add, commit, refresh, _row_to_dict
  #### `⏵m` `async delete_by_run(self, *, thread_id: str, run_id: str, user_id: str | None | _AutoSentinel) -> bool`  L167
    - _文档首行_（仅供参考）: Delete the current user's feedback for a run. Returns True if a record was deleted.
    - 分支数 2，函数体节点数 124；return: False, True
    - 调用: resolve_user_id, _sf, where, select, execute, scalar_one_or_none, delete, commit
  - 网络调用: delete (L186)
  #### `⏵m` `async list_by_thread_grouped(self, thread_id: str, *, user_id: str | None | _AutoSentinel) -> dict[str, dict]`  L190
    - _文档首行_（仅供参考）: Return feedback grouped by run_id for a thread: {run_id: feedback_dict}.
    - 分支数 2，函数体节点数 122；return: {row.run_id: self._row_to_dict(row) for row in result.scalars()}
    - 调用: resolve_user_id, where, select, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async list_by_run_ids(self, thread_id: str, run_ids: set[str], *, user_id: str | None | _AutoSentinel) -> dict[str, dict]`  L205
    - _文档首行_（仅供参考）: Return feedback for only the selected runs in one thread.
    - 分支数 3，函数体节点数 145；return: {}, {row.run_id: self._row_to_dict(row) for row in result.scalars()}
    - 调用: resolve_user_id, where, select, in_, _sf, execute, _row_to_dict, scalars
  #### `⏵m` `async aggregate_by_run(self, thread_id: str, run_id: str) -> dict`  L226
    - _文档首行_（仅供参考）: Aggregate feedback stats for a run using database-side counting.
    - 分支数 1，函数体节点数 152；return: {'run_id': run_id, 'total': row.total, 'positive': row.positive, 'negative': row.negative}
    - 调用: where, select, label, count, coalesce, sum, case, _sf, one, execute

## 文件内调用关系
- `FeedbackRepository._row_to_dict` -> get
- `FeedbackRepository.create` -> _row_to_dict
- `FeedbackRepository.get` -> get, _row_to_dict
- `FeedbackRepository.list_by_run` -> _row_to_dict
- `FeedbackRepository.list_by_thread` -> _row_to_dict
- `FeedbackRepository.delete` -> get, delete
- `FeedbackRepository.upsert` -> _row_to_dict
- `FeedbackRepository.delete_by_run` -> delete
- `FeedbackRepository.list_by_thread_grouped` -> _row_to_dict
- `FeedbackRepository.list_by_run_ids` -> _row_to_dict

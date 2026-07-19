# `backend/packages/harness/deerflow/config/database_config.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/config/database_config.py`  ·  行数: 103

**模块文档首行**（仅供参考）: Unified database backend configuration.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: os
- `__future__` -> annotations
- `typing` -> Literal
- `pydantic` -> BaseModel, Field

## 类
### 类 `DatabaseConfig`  L40
- 继承: BaseModel
- 类/实例变量:
  - `backend` = Field(default='memory', description="Storage backend for ...
  - `sqlite_dir` = Field(default='.deer-flow/data', description='Directory f...
  - `postgres_url` = Field(default='', description='PostgreSQL connection URL,...
  - `echo_sql` = Field(default=False, description='Echo all SQL statements...
  - `pool_size` = Field(default=5, description='Connection pool size for th...
- 方法:
  #### `prop` `_resolved_sqlite_dir(self) -> str`    @property  L70
    - _文档首行_（仅供参考）: Resolve sqlite_dir to an absolute path (relative to CWD).
    - 分支数 0，函数体节点数 25；return: str(Path(self.sqlite_dir).resolve())
    - 调用: str, resolve, Path
  #### `prop` `sqlite_path(self) -> str`    @property  L77
    - _文档首行_（仅供参考）: Unified SQLite file path shared by checkpointer and app.
    - 分支数 0，函数体节点数 22；return: os.path.join(self._resolved_sqlite_dir, 'deerflow.db')
    - 调用: join
  #### `prop` `checkpointer_sqlite_path(self) -> str`    @property  L83
    - _文档首行_（仅供参考）: SQLite file path for the LangGraph checkpointer (alias for sqlite_path).
    - 分支数 0，函数体节点数 14；return: self.sqlite_path
  #### `prop` `app_sqlite_path(self) -> str`    @property  L88
    - _文档首行_（仅供参考）: SQLite file path for application ORM data (alias for sqlite_path).
    - 分支数 0，函数体节点数 14；return: self.sqlite_path
  #### `prop` `app_sqlalchemy_url(self) -> str`    @property  L93
    - _文档首行_（仅供参考）: SQLAlchemy async URL for the application ORM engine.
    - 分支数 3，函数体节点数 72；raise: ValueError(f'No SQLAlchemy URL for backend={self.backend!r}')；return: f'sqlite+aiosqlite:///{self.sqlite_path}', url
    - 调用: startswith, replace, ValueError
  - 文件IO: replace (L100)

## 文件内调用关系
_无文件内调用_

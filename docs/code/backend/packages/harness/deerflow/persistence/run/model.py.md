# `backend/packages/harness/deerflow/persistence/run/model.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/persistence/run/model.py`  ·  行数: 70

**模块文档首行**（仅供参考）: ORM model for run metadata.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 0 个

## 依赖（import）
- `__future__` -> annotations
- `datetime` -> UTC, datetime
- `sqlalchemy` -> JSON, DateTime, Index, String, Text, text
- `sqlalchemy.orm` -> Mapped, mapped_column
- `deerflow.persistence.base` -> Base

## 类
### 类 `RunRow`  L13
- 继承: Base
- 类/实例变量:
  - `__tablename__` = 'runs'
  - `run_id` = mapped_column(String(64), primary_key=True)
  - `thread_id` = mapped_column(String(64), nullable=False, index=True)
  - `assistant_id` = mapped_column(String(128))
  - `user_id` = mapped_column(String(64), index=True)
  - `status` = mapped_column(String(20), default='pending')
  - `model_name` = mapped_column(String(128))
  - `multitask_strategy` = mapped_column(String(20), default='reject')
  - `metadata_json` = mapped_column(JSON, default=dict)
  - `kwargs_json` = mapped_column(JSON, default=dict)
  - `error` = mapped_column(Text)
  - `stop_reason` = mapped_column(String(50))
  - `message_count` = mapped_column(default=0)
  - `first_human_message` = mapped_column(Text)
  - `last_ai_message` = mapped_column(Text)
  - `total_input_tokens` = mapped_column(default=0)
  - `total_output_tokens` = mapped_column(default=0)
  - `total_tokens` = mapped_column(default=0)
  - `llm_call_count` = mapped_column(default=0)
  - `lead_agent_tokens` = mapped_column(default=0)
  - `subagent_tokens` = mapped_column(default=0)
  - `middleware_tokens` = mapped_column(default=0)
  - `token_usage_by_model` = mapped_column(JSON, default=dict, server_default=text("'{...
  - `follow_up_to_run_id` = mapped_column(String(64))
  - `owner_worker_id` = mapped_column(String(128), nullable=True)
  - …(+4)

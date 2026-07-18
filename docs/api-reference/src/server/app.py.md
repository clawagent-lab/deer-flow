# `src/server/app.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/server/app.py`
- **模块导入名**：`src.server.app`
- **代码行数**：1313
- **架构归属**：src/server —— FastAPI 服务层（chat / config / eval / mcp / rag 路由 + 校验工具）

## 模块概述

```text
DeerFlow 主 FastAPI 应用模块。

负责构建并配置 ASGI 应用实例 ``app``，集成 LangGraph 多智能体研究流程，
提供聊天对话、研究报告、播客/PPT 生成、提示词增强、MCP 工具加载、
RAG 资源管理、报告评估等 HTTP 与 SSE 流式接口，并管理 PostgreSQL/MongoDB
等 Checkpoint 持久化连接的生命周期。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config.configuration import get_recursion_limit`
- `from src.config.loader import get_bool_env, get_int_env, get_str_env`
- `from src.config.report_style import ReportStyle`
- `from src.config.tools import SELECTED_RAG_PROVIDER`
- `from src.citations import merge_citations`
- `from src.graph.builder import build_graph_with_memory`
- `from src.graph.checkpoint import chat_stream_message`
- `from src.graph.utils import build_clarified_topic_from_history, reconstruct_clarification_history`
- `from src.llms.llm import get_configured_llm_models`
- `from src.podcast.graph.builder import build_graph`
- `from src.ppt.graph.builder import build_graph`
- `from src.prompt_enhancer.graph.builder import build_graph`
- `from src.prose.graph.builder import build_graph`
- `from src.eval import ReportEvaluator`
- `from src.rag.builder import build_retriever`
- `from src.rag.milvus import load_examples`
- `from src.rag.qdrant import load_examples`
- `from src.rag.retriever import Resource`
- `from src.server.chat_request import ChatRequest, EnhancePromptRequest, GeneratePodcastRequest, GeneratePPTRequest, GenerateProseRequest, TTSRequest`
- `from src.server.eval_request import EvaluateReportRequest, EvaluateReportResponse`
- `from src.server.config_request import ConfigResponse`
- `from src.server.mcp_request import MCPServerMetadataRequest, MCPServerMetadataResponse`
- `from src.server.mcp_utils import load_mcp_tools`
- `from src.server.rag_request import RAGConfigResponse, RAGResourceRequest, RAGResourcesResponse`
- `from src.tools import VolcengineTTS`
- `from src.utils.json_utils import sanitize_args`
- `from src.utils.log_sanitizer import sanitize_agent_name, sanitize_log_input, sanitize_thread_id, sanitize_tool_name, sanitize_user_content`

**外部依赖**（第三方库 / 标准库）：

- `from typing import Annotated, Any, List, Optional, cast`
- `from uuid import uuid4`
- `from dotenv import load_dotenv`
- `from fastapi import FastAPI, HTTPException, Query, UploadFile`
- `from fastapi.middleware.cors import CORSMiddleware`
- `from fastapi.responses import Response, StreamingResponse`
- `from langchain_core.messages import AIMessageChunk, BaseMessage, ToolMessage`
- `from langgraph.checkpoint.mongodb import AsyncMongoDBSaver`
- `from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver`
- `from langgraph.store.memory import InMemoryStore`
- `from langgraph.types import Command`
- `from psycopg.rows import dict_row`
- `from psycopg_pool import AsyncConnectionPool`
- `from contextlib import asynccontextmanager`
- `import asyncio`
- `import base64`
- `import json`
- `import logging`
- `import os`
- `import re`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 93 | `logging.getLogger(__name__)` |
| 常量 | `INTERNAL_SERVER_ERROR_DETAIL` | 100 | `'Internal Server Error'` |
| 异步函数 | `lifespan` | 115 | `(app)` |
| 常量 | `app` | 226 | `FastAPI(title='DeerFlow API', description='API for Deer', version='0.1.0', lifespan=lifespan)` |
| 常量 | `allowed_origins_str` | 236 | `get_str_env('ALLOWED_ORIGINS', 'http://localhost:3000')` |
| 常量 | `allowed_origins` | 237 | `[origin.strip() for origin in allowed_origins_str.split(',')]` |
| 常量 | `in_memory_store` | 252 | `InMemoryStore()` |
| 常量 | `graph` | 253 | `build_graph_with_memory()` |
| 异步函数 | `chat_stream` | 257 | `(request: ChatRequest)` |
| 函数 | `_validate_tool_call_chunks` | 298 | `(tool_call_chunks)` |
| 函数 | `_process_tool_call_chunks` | 331 | `(tool_call_chunks)` |
| 函数 | `_get_agent_name` | 417 | `(agent, message_metadata)` |
| 函数 | `_create_event_stream_message` | 427 | `(message_chunk, message_metadata, thread_id, agent_name)` |
| 函数 | `_create_interrupt_event` | 466 | `(thread_id, event_data)` |
| 函数 | `_process_initial_messages` | 487 | `(message, thread_id)` |
| 异步函数 | `_process_message_chunk` | 504 | `(message_chunk, message_metadata, thread_id, agent)` |
| 函数 | `extract_citations_from_event` | 602 | `(event: Any, safe_thread_id: str='unknown') -> list` |
| 异步函数 | `_stream_graph_events` | 651 | `(graph_instance, workflow_input, workflow_config, thread_id)` |
| 异步函数 | `_astream_workflow_generator` | 782 | `(messages: List[dict], thread_id: str, resources: List[Resource], max_plan_iterations: int, max_s...` |
| 函数 | `_make_event` | 965 | `(event_type: str, data: dict[str, any])` |
| 异步函数 | `text_to_speech` | 988 | `(request: TTSRequest)` |
| 异步函数 | `generate_podcast` | 1044 | `(request: GeneratePodcastRequest)` |
| 异步函数 | `generate_ppt` | 1058 | `(request: GeneratePPTRequest)` |
| 异步函数 | `generate_prose` | 1077 | `(request: GenerateProseRequest)` |
| 异步函数 | `evaluate_report` | 1101 | `(request: EvaluateReportRequest)` |
| 异步函数 | `enhance_prompt` | 1134 | `(request: EnhancePromptRequest)` |
| 异步函数 | `mcp_server_metadata` | 1175 | `(request: MCPServerMetadataRequest)` |
| 异步函数 | `rag_config` | 1225 | `()` |
| 异步函数 | `rag_resources` | 1231 | `(request: Annotated[RAGResourceRequest, Query()])` |
| 常量 | `MAX_UPLOAD_SIZE_BYTES` | 1239 | `10 * 1024 * 1024` |
| 常量 | `ALLOWED_EXTENSIONS` | 1240 | `{'.md', '.txt'}` |
| 函数 | `_sanitize_filename` | 1243 | `(filename: str) -> str` |
| 异步函数 | `upload_rag_resource` | 1256 | `(file: UploadFile)` |
| 异步函数 | `config` | 1308 | `()` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：93–93  |  **完整限定名**：`src.server.app.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `INTERNAL_SERVER_ERROR_DETAIL`

- **类型**：模块常量  |  **行号**：100–100  |  **完整限定名**：`src.server.app.INTERNAL_SERVER_ERROR_DETAIL`
- **值**：

```python
INTERNAL_SERVER_ERROR_DETAIL = 'Internal Server Error'
```

**说明**（自动推断）：

模块级常量 `INTERNAL_SERVER_ERROR_DETAIL`，在导入时初始化，供本模块及相关流程引用。

### `lifespan`

- **类型**：异步函数  |  **行号**：115–223  |  **完整限定名**：`src.server.app.lifespan`
- **装饰器**：`@asynccontextmanager`
- **签名**：

```python
async def lifespan(app):
```

**摘要**：

Application lifecycle manager
- Startup: Register asyncio exception handler and initialize global connection pools
- Shutdown: Clean up global connection pools

### `app`

- **类型**：模块常量  |  **行号**：226–231  |  **完整限定名**：`src.server.app.app`
- **值**：

```python
app = FastAPI(title='DeerFlow API', description='API for Deer', version='0.1.0', lifespan=lifespan)
```

**说明**（自动推断）：

FastAPI 应用实例：DeerFlow 的 HTTP 入口，挂载 chat / generate / enhance / RAG 等路由，并通过 lifespan 管理 PostgreSQL / MongoDB checkpoint 连接池。

### `allowed_origins_str`

- **类型**：模块常量  |  **行号**：236–236  |  **完整限定名**：`src.server.app.allowed_origins_str`
- **值**：

```python
allowed_origins_str = get_str_env('ALLOWED_ORIGINS', 'http://localhost:3000')
```

**说明**（自动推断）：

CORS 允许来源集合，从配置解析得到，供 FastAPI 中间件校验跨域请求。

### `allowed_origins`

- **类型**：模块常量  |  **行号**：237–237  |  **完整限定名**：`src.server.app.allowed_origins`
- **值**：

```python
allowed_origins = [origin.strip() for origin in allowed_origins_str.split(',')]
```

**说明**（自动推断）：

CORS 允许来源集合，从配置解析得到，供 FastAPI 中间件校验跨域请求。

### `in_memory_store`

- **类型**：模块常量  |  **行号**：252–252  |  **完整限定名**：`src.server.app.in_memory_store`
- **值**：

```python
in_memory_store = InMemoryStore()
```

**说明**（自动推断）：

进程内会话存储字典，用于在无持久化 checkpoint 时保留会话级状态。

### `graph`

- **类型**：模块常量  |  **行号**：253–253  |  **完整限定名**：`src.server.app.graph`
- **值**：

```python
graph = build_graph_with_memory()
```

**说明**（自动推断）：

已编译的 LangGraph 工作流实例，模块导入时即构建完成，供 `invoke` / `astream` 直接调用。

### `chat_stream`

- **类型**：异步函数  |  **行号**：257–295  |  **完整限定名**：`src.server.app.chat_stream`
- **装饰器**：`@app.post`
- **签名**：

```python
async def chat_stream(request: ChatRequest):
```

**说明**（自动推断）：

FastAPI 路由处理函数（POST @app.post）。解析请求体并调用对应业务流程，返回 JSON 或 SSE 流式响应。

### `_validate_tool_call_chunks`

- **类型**：函数  |  **行号**：298–328  |  **完整限定名**：`src.server.app._validate_tool_call_chunks`
- **签名**：

```python
def _validate_tool_call_chunks(tool_call_chunks):
```

**摘要**：

Validate and log tool call chunk structure for debugging.

### `_process_tool_call_chunks`

- **类型**：函数  |  **行号**：331–414  |  **完整限定名**：`src.server.app._process_tool_call_chunks`
- **签名**：

```python
def _process_tool_call_chunks(tool_call_chunks):
```

**摘要**：

Process tool call chunks with proper index-based grouping.

### `_get_agent_name`

- **类型**：函数  |  **行号**：417–424  |  **完整限定名**：`src.server.app._get_agent_name`
- **签名**：

```python
def _get_agent_name(agent, message_metadata):
```

**摘要**：

Extract agent name from agent tuple.

### `_create_event_stream_message`

- **类型**：函数  |  **行号**：427–463  |  **完整限定名**：`src.server.app._create_event_stream_message`
- **签名**：

```python
def _create_event_stream_message(message_chunk, message_metadata, thread_id, agent_name):
```

**摘要**：

Create base event stream message.

### `_create_interrupt_event`

- **类型**：函数  |  **行号**：466–484  |  **完整限定名**：`src.server.app._create_interrupt_event`
- **签名**：

```python
def _create_interrupt_event(thread_id, event_data):
```

**摘要**：

Create interrupt event.

### `_process_initial_messages`

- **类型**：函数  |  **行号**：487–501  |  **完整限定名**：`src.server.app._process_initial_messages`
- **签名**：

```python
def _process_initial_messages(message, thread_id):
```

**摘要**：

Process initial messages and yield formatted events.

### `_process_message_chunk`

- **类型**：异步函数  |  **行号**：504–599  |  **完整限定名**：`src.server.app._process_message_chunk`
- **签名**：

```python
async def _process_message_chunk(message_chunk, message_metadata, thread_id, agent):
```

**摘要**：

Process a single message chunk and yield appropriate events.

### `extract_citations_from_event`

- **类型**：函数  |  **行号**：602–648  |  **完整限定名**：`src.server.app.extract_citations_from_event`
- **签名**：

```python
def extract_citations_from_event(event: Any, safe_thread_id: str='unknown') -> list:
```

**摘要**：

Extract all citations from event data using an iterative, depth-limited traversal.

### `_stream_graph_events`

- **类型**：异步函数  |  **行号**：651–779  |  **完整限定名**：`src.server.app._stream_graph_events`
- **签名**：

```python
async def _stream_graph_events(graph_instance, workflow_input, workflow_config, thread_id):
```

**摘要**：

Stream events from the graph and process them.

### `_astream_workflow_generator`

- **类型**：异步函数  |  **行号**：782–962  |  **完整限定名**：`src.server.app._astream_workflow_generator`
- **签名**：

```python
async def _astream_workflow_generator(messages: List[dict], thread_id: str, resources: List[Resource], max_plan_iterations: int, max_step_num: int, max_search_results: int, auto_accepted_plan: bool, interrupt_feedback: str, mcp_settings: dict, enable_background_investigation: bool, enable_web_search: bool, report_style: ReportStyle, enable_deep_thinking: bool, enable_clarification: bool, max_clarification_rounds: int, locale: str='en-US', interrupt_before_tools: Optional[List[str]]=None):
```

**摘要**：

异步生成器：驱动 LangGraph 工作流并以 SSE 事件流形式产出每个节点的输出。

### `_make_event`

- **类型**：函数  |  **行号**：965–984  |  **完整限定名**：`src.server.app._make_event`
- **签名**：

```python
def _make_event(event_type: str, data: dict[str, any]):
```

**说明**（自动推断）：

构造 SSE 事件字符串的辅助函数，将事件类型与数据组装为 `text/event-stream` 格式。

### `text_to_speech`

- **类型**：异步函数  |  **行号**：988–1040  |  **完整限定名**：`src.server.app.text_to_speech`
- **装饰器**：`@app.post`
- **签名**：

```python
async def text_to_speech(request: TTSRequest):
```

**摘要**：

Convert text to speech using volcengine TTS API.

### `generate_podcast`

- **类型**：异步函数  |  **行号**：1044–1054  |  **完整限定名**：`src.server.app.generate_podcast`
- **装饰器**：`@app.post`
- **签名**：

```python
async def generate_podcast(request: GeneratePodcastRequest):
```

**说明**（自动推断）：

FastAPI 路由处理函数（POST @app.post）。解析请求体并调用对应业务流程，返回 JSON 或 SSE 流式响应。

### `generate_ppt`

- **类型**：异步函数  |  **行号**：1058–1073  |  **完整限定名**：`src.server.app.generate_ppt`
- **装饰器**：`@app.post`
- **签名**：

```python
async def generate_ppt(request: GeneratePPTRequest):
```

**说明**（自动推断）：

FastAPI 路由处理函数（POST @app.post）。解析请求体并调用对应业务流程，返回 JSON 或 SSE 流式响应。

### `generate_prose`

- **类型**：异步函数  |  **行号**：1077–1097  |  **完整限定名**：`src.server.app.generate_prose`
- **装饰器**：`@app.post`
- **签名**：

```python
async def generate_prose(request: GenerateProseRequest):
```

**说明**（自动推断）：

FastAPI 路由处理函数（POST @app.post）。解析请求体并调用对应业务流程，返回 JSON 或 SSE 流式响应。

### `evaluate_report`

- **类型**：异步函数  |  **行号**：1101–1130  |  **完整限定名**：`src.server.app.evaluate_report`
- **装饰器**：`@app.post`
- **签名**：

```python
async def evaluate_report(request: EvaluateReportRequest):
```

**摘要**：

Evaluate report quality using automated metrics and optionally LLM-as-Judge.

### `enhance_prompt`

- **类型**：异步函数  |  **行号**：1134–1171  |  **完整限定名**：`src.server.app.enhance_prompt`
- **装饰器**：`@app.post`
- **签名**：

```python
async def enhance_prompt(request: EnhancePromptRequest):
```

**说明**（自动推断）：

FastAPI 路由处理函数（POST @app.post）。解析请求体并调用对应业务流程，返回 JSON 或 SSE 流式响应。

### `mcp_server_metadata`

- **类型**：异步函数  |  **行号**：1175–1221  |  **完整限定名**：`src.server.app.mcp_server_metadata`
- **装饰器**：`@app.post`
- **签名**：

```python
async def mcp_server_metadata(request: MCPServerMetadataRequest):
```

**摘要**：

Get information about an MCP server.

### `rag_config`

- **类型**：异步函数  |  **行号**：1225–1227  |  **完整限定名**：`src.server.app.rag_config`
- **装饰器**：`@app.get`
- **签名**：

```python
async def rag_config():
```

**摘要**：

Get the config of the RAG.

### `rag_resources`

- **类型**：异步函数  |  **行号**：1231–1236  |  **完整限定名**：`src.server.app.rag_resources`
- **装饰器**：`@app.get`
- **签名**：

```python
async def rag_resources(request: Annotated[RAGResourceRequest, Query()]):
```

**摘要**：

Get the resources of the RAG.

### `MAX_UPLOAD_SIZE_BYTES`

- **类型**：模块常量  |  **行号**：1239–1239  |  **完整限定名**：`src.server.app.MAX_UPLOAD_SIZE_BYTES`
- **值**：

```python
MAX_UPLOAD_SIZE_BYTES = 10 * 1024 * 1024
```

**说明**（自动推断）：

数值上限常量 `MAX_UPLOAD_SIZE_BYTES`，用于约束对应操作的规模或阈值。

### `ALLOWED_EXTENSIONS`

- **类型**：模块常量  |  **行号**：1240–1240  |  **完整限定名**：`src.server.app.ALLOWED_EXTENSIONS`
- **值**：

```python
ALLOWED_EXTENSIONS = {'.md', '.txt'}
```

**说明**（自动推断）：

白名单常量 `ALLOWED_EXTENSIONS`，列出允许的取值集合，用于输入校验。

### `_sanitize_filename`

- **类型**：函数  |  **行号**：1243–1252  |  **完整限定名**：`src.server.app._sanitize_filename`
- **签名**：

```python
def _sanitize_filename(filename: str) -> str:
```

**摘要**：

Sanitize filename to prevent path traversal attacks.

### `upload_rag_resource`

- **类型**：异步函数  |  **行号**：1256–1304  |  **完整限定名**：`src.server.app.upload_rag_resource`
- **装饰器**：`@app.post`
- **签名**：

```python
async def upload_rag_resource(file: UploadFile):
```

**说明**（自动推断）：

FastAPI 路由处理函数（POST @app.post）。解析请求体并调用对应业务流程，返回 JSON 或 SSE 流式响应。

### `config`

- **类型**：异步函数  |  **行号**：1308–1313  |  **完整限定名**：`src.server.app.config`
- **装饰器**：`@app.get`
- **签名**：

```python
async def config():
```

**摘要**：

Get the config of the server.

## 调用关系（下游）

**被以下模块导入**：

- `src.server`
- `tests.unit.server.test_app`
- `tests.unit.server.test_tool_call_chunks`

## 示例用法

```python
from src.server.app import lifespan
#
# TODO: 结合业务场景补充 lifespan 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

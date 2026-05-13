# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
uv sync                          # Install Python deps (creates venv + downloads interpreter)
uv pip install -e ".[dev]"       # Dev deps (ruff, langgraph-cli)
uv pip install -e ".[test]"      # Test deps

# Run
uv run server.py --reload        # FastAPI backend (SSE streaming API)
uv run main.py                   # Console CLI interface
make langgraph-dev               # LangGraph Studio for visual graph debugging
cd web && pnpm dev               # Next.js frontend

# Test
make test                        # All tests via pytest
pytest tests/unit/test_foo.py    # Single test file
pytest tests/unit/test_foo.py::test_name  # Single test
make coverage                    # Tests with coverage report

# Lint/Format
make lint                        # Ruff lint with auto-fix (includes import sorting)
make format                      # Ruff format
make lint-frontend               # Frontend: lint + typecheck + test + build

# License headers (required on all source files)
make add-license-all             # Add MIT headers to all .py/.ts files
make check-license-all           # Verify headers present
```

## Pre-commit Hook

The pre-commit hook runs `make lint`, `make format`, and `make check-license-all`. Install it:

```bash
chmod +x pre-commit
ln -s ../../pre-commit .git/hooks/pre-commit
```

## Architecture

### Agent Graph (LangGraph StateGraph)

The core workflow is a directed graph defined in `src/graph/builder.py`:

```
START → coordinator → background_investigator → planner
  → research_team (dispatches to researcher | analyst | coder)
  → planner (loops until all steps complete)
  → reporter → END
```

- `coordinator_node` — Entry point. Routes to planner or responds directly (greetings, small talk) via tool calls (`handoff_to_planner`, `direct_response`).
- `background_investigation_node` — Pre-research web search to provide context for planning.
- `planner_node` — Generates a `Plan` (pydantic model in `src/prompts/planner_model.py`) with typed `Step`s (`RESEARCH`, `ANALYSIS`, `PROCESSING`). Can loop: after the research team finishes all steps, planner re-evaluates whether more iterations are needed.
- `research_team_node` — Dispatcher that routes to the correct specialist based on the current step's `step_type`.
- `reporter_node` — Synthesizes all observations into a final report. Strips `<think&gt;` tags from model output.

State is defined in `src/graph/types.py` as `State(MessagesState)` — extends LangGraph's message state with plan, observations, citations, clarification fields, and workflow control (`goto`).

Conditional edge `continue_to_running_research_team` in `builder.py` determines the next node by finding the first incomplete step and routing by `step_type`.

### Agent Creation

`src/agents/agents.py` — `create_agent()` factory using `langchain.agents.create_agent`. Key pattern:
- Each agent gets an LLM via `AGENT_LLM_MAP` in `src/config/agents.py` (maps agent name → LLM type: `"basic"`, `"reasoning"`, `"vision"`, `"code"`)
- `DynamicPromptMiddleware` injects the system prompt from Jinja2 templates before each model call
- `PreModelHookMiddleware` wraps optional pre-model hooks
- Tools can be wrapped with interrupt logic via `tool_interceptor.py` for human-in-the-loop on specific tools

### Prompt System

Prompts are Jinja2 templates in `src/prompts/` as `.md` files:
- `{agent_name}.md` — English default (e.g., `researcher.md`, `planner.md`)
- `{agent_name}.zh_CN.md` — Locale override (falls back to English if not found)
- `template.py` — `apply_prompt_template()` renders template with state vars + `Configuration` fields + `CURRENT_TIME`
- `planner_model.py` — Pydantic models `Plan` and `Step` with `StepType` enum

### LLM Configuration

`src/llms/llm.py` — LLM instances created from `conf.yaml`:
- Four LLM types: `BASIC_MODEL`, `REASONING_MODEL`, `VISION_MODEL`, `CODE_MODEL`
- Provider auto-detection: Google AI Studio (`platform: google_aistudio`), Azure (`azure_endpoint`), Dashscope (`base_url` contains `dashscope`), DeepSeek (reasoning type), or default OpenAI-compatible
- Environment variable overrides: `{TYPE}_MODEL__{key}` (e.g., `BASIC_MODEL__api_key`)
- `token_limit` in config controls context compression thresholds (not passed to LLM constructor)
- Instances are cached globally in `_llm_cache`

### Configuration

- `conf.yaml` — LLM models, search engine, crawler engine, tool interrupts, web search toggle. Env vars: `$VAR_NAME` syntax supported. Changes require restart (config is cached by `load_yaml_config`).
- `Configuration` dataclass in `src/config/configuration.py` — Runtime config: `max_plan_iterations`, `max_step_num`, `max_search_results`, `report_style`, `enable_deep_thinking`, `mcp_settings`, etc. Merges from `RunnableConfig` + env vars.
- `src/config/tools.py` — `SearchEngine` and `CrawlerEngine` enums, `RAGProvider` enum. `SEARCH_API` env var selects search engine (default: tavily).

### Server (FastAPI)

`src/server/app.py` — Main FastAPI application:
- `POST /api/chat/stream` — SSE streaming endpoint. Streams graph events (`message_chunk`, `tool_calls`, `tool_call_result`, `interrupt`, `citations`) to the frontend.
- Checkpointing: PostgreSQL or MongoDB via `LANGGRAPH_CHECKPOINT_SAVER=true` + `LANGGRAPH_CHECKPOINT_DB_URL`. Connection pools initialized in `lifespan()`.
- Additional endpoints: `/api/tts`, `/api/podcast/generate`, `/api/ppt/generate`, `/api/prose/generate`, `/api/prompt/enhance`, `/api/report/evaluate`, `/api/mcp/server/metadata`, `/api/rag/*`, `/api/config`

### Tools

`src/tools/` — Available tools registered in `__init__.py`:
- `search.py` / `tavily_search/` / `infoquest_search/` — Web search (Tavily, DuckDuckGo, Brave, Arxiv, Wikipedia, Searx, Serper)
- `crawl.py` — Web page content extraction (Jina or InfoQuest crawler)
- `python_repl.py` — Sandboxed Python code execution for data analysis
- `retriever.py` — RAG retrieval tool
- `tts.py` — Volcengine TTS API
- `decorators.py` — Tool decorators (e.g., `@log_tool_io`)

### Sub-Graphs (Independent LangGraph Workflows)

Each has its own `graph/builder.py`:
- `src/podcast/` — Converts report to podcast audio
- `src/ppt/` — Generates PowerPoint from report
- `src/prose/` — Prose writing/refinement
- `src/prompt_enhancer/` — Improves user prompts before research
- `src/rag/` — RAG integration (Dify, RAGFlow, VikingDB, Milvus, Qdrant)

### Frontend (web/)

Next.js app with Ant Design + Radix UI. Communicates with backend via SSE on `/api/chat/stream`. Uses pnpm.

## Key Patterns

- **State transitions use `Command`**: `interrupt` for human feedback, `Command(goto=...)` for routing. State meta fields (locale, research_topic, clarification state) must be explicitly preserved in `Command.update()` dicts via `preserve_state_meta_fields()`.
- **Plan validation**: `validate_and_fix_plan()` repairs missing `step_type` fields and enforces web search requirements.
- **Citations**: Extracted from tool responses during research, accumulated via `merge_citations()`, sent as a final `citations` SSE event.
- **Context management**: `ContextManager` in `src/utils/context_manager.py` handles message truncation to stay within LLM token limits.
- **License headers**: All `.py` and `.ts` files must have the MIT license header. The pre-commit hook enforces this.

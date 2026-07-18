# Repository Guidelines

## Project Structure & Module Organization

The Python 3.12 backend lives in `src/`. Orchestration is under `src/graph/`, API code under `src/server/`, model adapters under `src/llms/`, and integrations under `src/tools/`, `src/crawler/`, and `src/rag/`. Prompt templates are in `src/prompts/`. Entry points are `main.py` (console) and `server.py` (FastAPI). Tests mirror these areas in `tests/unit/` and `tests/integration/`. The Next.js/TypeScript UI is in `web/`, with source in `web/src/`, tests in `web/tests/`, and static files in `web/public/`. Documentation, examples, and images belong in `docs/`, `examples/`, and `assets/`.

## Build, Test, and Development Commands

- `uv sync && make install-dev` installs runtime, development, and test dependencies.
- `make serve` starts the backend with reload; `uv run main.py` launches the console UI.
- `cd web && pnpm install && pnpm dev` starts the frontend on port 3000.
- `./bootstrap.sh -d` runs backend and frontend together in development mode.
- `make test` runs the Python suite; `make coverage` also writes `coverage.xml`.
- `make lint && make format` applies Ruff import fixes and formatting.
- `make lint-frontend` installs, lints, type-checks, tests, and builds the UI.

## Coding Style & Naming Conventions

Use four spaces, type hints, focused functions, and PEP 8 naming: `snake_case` for Python functions/modules and `PascalCase` for classes. Ruff enforces an 88-character line length and Python 3.12 syntax. For TypeScript, follow ESLint and Prettier; use `PascalCase` React components, `camelCase` variables, and ordered imports. New Python and TypeScript source files require the repository license header; verify with `make check-license-all`.

## Testing Guidelines

Pytest discovers `test_*.py` beneath `tests/`; keep unit tests beside the matching domain and reserve `tests/integration/` for cross-component or external-service behavior. The configured coverage floor is 25%. Run a focused test with `uv run pytest tests/unit/graph/test_builder.py`. Frontend tests use Jest: `cd web && pnpm test:run`, or `pnpm test:coverage` for coverage.

## Commit & Pull Request Guidelines

Recent history follows Conventional Commit-style subjects such as `fix: ...`, `feat(tool): ...`, `docs: ...`, and `build(deps): ...`. Keep subjects imperative and commits narrowly scoped. Pull requests should explain the change and validation performed, reference related issues, include tests and documentation when behavior changes, and add screenshots for visible UI updates. Before requesting review, ensure backend checks and the relevant frontend lint, typecheck, test, and build commands pass.

## Configuration & Security

Copy `.env.example` to `.env` and `conf.yaml.example` to `conf.yaml`; never commit credentials. Consult `docs/configuration_guide.md` before adding providers, and avoid binding the backend beyond localhost unless the deployment is secured.

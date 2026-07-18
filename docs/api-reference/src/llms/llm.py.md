# `src/llms/llm.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/llms/llm.py`
- **模块导入名**：`src.llms.llm`
- **代码行数**：347
- **架构归属**：src/llms —— LLM 适配层（统一封装 dashscope 等提供商，按类型路由）

## 模块概述

```text
LLM 子包入口。

统一对外暴露大语言模型（LLM）的构造入口与缓存机制，供 DeerFlow 各智能体
按 LLMType（如 basic/reasoning）获取对应的 LangChain ChatModel 实例。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from src.config import load_yaml_config`
- `from src.config.agents import LLMType`
- `from src.llms.providers.dashscope import ChatDashscope`

**外部依赖**（第三方库 / 标准库）：

- `from pathlib import Path`
- `from typing import Any, Dict, get_args`
- `from langchain_core.language_models import BaseChatModel`
- `from langchain_deepseek import ChatDeepSeek`
- `from langchain_google_genai import ChatGoogleGenerativeAI`
- `from langchain_openai import AzureChatOpenAI, ChatOpenAI`
- `import logging`
- `import os`
- `import httpx`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 常量 | `logger` | 25 | `logging.getLogger(__name__)` |
| 常量 | `ALLOWED_LLM_CONFIG_KEYS` | 32 | `{'model', 'api_key', 'base_url', 'api_base', 'max_retries', 'timeout', 'max_tokens', 'temperature...` |
| 函数 | `_get_config_file_path` | 77 | `() -> str` |
| 函数 | `_get_llm_type_config_keys` | 82 | `() -> dict[str, str]` |
| 函数 | `_get_env_llm_conf` | 92 | `(llm_type: str) -> Dict[str, Any]` |
| 函数 | `_create_llm_use_conf` | 107 | `(llm_type: LLMType, conf: Dict[str, Any]) -> BaseChatModel` |
| 函数 | `get_llm_by_type` | 198 | `(llm_type: LLMType) -> BaseChatModel` |
| 函数 | `get_configured_llm_models` | 211 | `() -> dict[str, list[str]]` |
| 函数 | `_get_model_token_limit_defaults` | 248 | `() -> dict[str, int]` |
| 函数 | `_infer_token_limit_from_model` | 280 | `(model_name: str) -> int` |
| 函数 | `get_llm_token_limit_by_type` | 306 | `(llm_type: str) -> int` |

## 符号详解

### `logger`

- **类型**：模块常量  |  **行号**：25–25  |  **完整限定名**：`src.llms.llm.logger`
- **值**：

```python
logger = logging.getLogger(__name__)
```

**说明**（自动推断）：

模块级日志器，通过 `logging.getLogger(__name__)` 获取，用于本模块内的事件记录与调试输出。

### `ALLOWED_LLM_CONFIG_KEYS`

- **类型**：模块常量  |  **行号**：32–74  |  **完整限定名**：`src.llms.llm.ALLOWED_LLM_CONFIG_KEYS`
- **值**：

```python
ALLOWED_LLM_CONFIG_KEYS = {'model', 'api_key', 'base_url', 'api_base', 'max_retries', 'timeout', 'max_tokens', 'temperature', 'top_p', 'frequen...
```

**说明**（自动推断）：

白名单常量 `ALLOWED_LLM_CONFIG_KEYS`，列出允许的取值集合，用于输入校验。

### `_get_config_file_path`

- **类型**：函数  |  **行号**：77–79  |  **完整限定名**：`src.llms.llm._get_config_file_path`
- **签名**：

```python
def _get_config_file_path() -> str:
```

**摘要**：

Get the path to the configuration file.

### `_get_llm_type_config_keys`

- **类型**：函数  |  **行号**：82–89  |  **完整限定名**：`src.llms.llm._get_llm_type_config_keys`
- **签名**：

```python
def _get_llm_type_config_keys() -> dict[str, str]:
```

**摘要**：

Get mapping of LLM types to their configuration keys.

### `_get_env_llm_conf`

- **类型**：函数  |  **行号**：92–104  |  **完整限定名**：`src.llms.llm._get_env_llm_conf`
- **签名**：

```python
def _get_env_llm_conf(llm_type: str) -> Dict[str, Any]:
```

**摘要**：

Get LLM configuration from environment variables.
Environment variables should follow the format: {LLM_TYPE}__{KEY}
e.g., BASIC_MODEL__api_key, BASIC_MODEL__base_url

### `_create_llm_use_conf`

- **类型**：函数  |  **行号**：107–195  |  **完整限定名**：`src.llms.llm._create_llm_use_conf`
- **签名**：

```python
def _create_llm_use_conf(llm_type: LLMType, conf: Dict[str, Any]) -> BaseChatModel:
```

**摘要**：

Create LLM instance using configuration.

### `get_llm_by_type`

- **类型**：函数  |  **行号**：198–208  |  **完整限定名**：`src.llms.llm.get_llm_by_type`
- **签名**：

```python
def get_llm_by_type(llm_type: LLMType) -> BaseChatModel:
```

**摘要**：

Get LLM instance by type. Returns cached instance if available.

### `get_configured_llm_models`

- **类型**：函数  |  **行号**：211–245  |  **完整限定名**：`src.llms.llm.get_configured_llm_models`
- **签名**：

```python
def get_configured_llm_models() -> dict[str, list[str]]:
```

**摘要**：

Get all configured LLM models grouped by type.

**返回值**：

```text
Dictionary mapping LLM type to list of configured model names.
```

### `_get_model_token_limit_defaults`

- **类型**：函数  |  **行号**：248–277  |  **完整限定名**：`src.llms.llm._get_model_token_limit_defaults`
- **签名**：

```python
def _get_model_token_limit_defaults() -> dict[str, int]:
```

**摘要**：

Get default token limits for common LLM models.
These are conservative limits to prevent token overflow errors (Issue #721).
Users can override by setting token_limit in their config.

### `_infer_token_limit_from_model`

- **类型**：函数  |  **行号**：280–303  |  **完整限定名**：`src.llms.llm._infer_token_limit_from_model`
- **签名**：

```python
def _infer_token_limit_from_model(model_name: str) -> int:
```

**摘要**：

Infer a reasonable token limit from the model name.
This helps protect against token overflow errors when token_limit is not explicitly configured.

**参数**：

```text
model_name: The model name from configuration
```

**返回值**：

```text
A conservative token limit based on known model capabilities
```

### `get_llm_token_limit_by_type`

- **类型**：函数  |  **行号**：306–342  |  **完整限定名**：`src.llms.llm.get_llm_token_limit_by_type`
- **签名**：

```python
def get_llm_token_limit_by_type(llm_type: str) -> int:
```

**摘要**：

Get the maximum token limit for a given LLM type.

**参数**：

```text
llm_type (str): The type of LLM (e.g., 'basic', 'reasoning', 'vision', 'code').
```

**返回值**：

```text
int: The maximum token limit for the specified LLM type (conservative estimate).
```

## 调用关系（下游）

**被以下模块导入**：

- `src.agents.agents`
- `src.graph.nodes`
- `src.podcast.graph.script_writer_node`
- `src.ppt.graph.ppt_composer_node`
- `src.prompt_enhancer.graph.enhancer_node`
- `src.prose.graph.prose_continue_node`
- `src.prose.graph.prose_fix_node`
- `src.prose.graph.prose_improve_node`
- `src.prose.graph.prose_longer_node`
- `src.prose.graph.prose_shorter_node`
- `src.prose.graph.prose_zap_node`
- `src.server.app`

## 示例用法

```python
from src.llms.llm import get_llm_by_type
#
# TODO: 结合业务场景补充 get_llm_by_type 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

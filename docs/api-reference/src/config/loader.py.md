# `src/config/loader.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/config/loader.py`
- **模块导入名**：`src.config.loader`
- **代码行数**：80
- **架构归属**：src/config —— 配置加载（`conf.yaml` / `.env`）、模型与工具开关、报告样式、智能体映射

## 模块概述

```text
配置加载模块：读取 conf.yaml 与环境变量，提供类型化的配置访问辅助函数与 YAML 解析缓存。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Any, Dict`
- `import os`
- `import yaml`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 函数 | `get_bool_env` | 12 | `(name: str, default: bool=False) -> bool` |
| 函数 | `get_str_env` | 19 | `(name: str, default: str='') -> str` |
| 函数 | `get_int_env` | 24 | `(name: str, default: int=0) -> int` |
| 函数 | `replace_env_vars` | 35 | `(value: str) -> str` |
| 函数 | `process_dict` | 45 | `(config: Dict[str, Any]) -> Dict[str, Any]` |
| 函数 | `load_yaml_config` | 63 | `(file_path: str) -> Dict[str, Any]` |

## 符号详解

### `get_bool_env`

- **类型**：函数  |  **行号**：12–16  |  **完整限定名**：`src.config.loader.get_bool_env`
- **签名**：

```python
def get_bool_env(name: str, default: bool=False) -> bool:
```

**说明**（自动推断）：

从环境变量读取 `bool` 值，支持默认值与类型转换（bool）。

### `get_str_env`

- **类型**：函数  |  **行号**：19–21  |  **完整限定名**：`src.config.loader.get_str_env`
- **签名**：

```python
def get_str_env(name: str, default: str='') -> str:
```

**说明**（自动推断）：

从环境变量读取 `str` 值，支持默认值与类型转换（str）。

### `get_int_env`

- **类型**：函数  |  **行号**：24–32  |  **完整限定名**：`src.config.loader.get_int_env`
- **签名**：

```python
def get_int_env(name: str, default: int=0) -> int:
```

**说明**（自动推断）：

从环境变量读取 `int` 值，支持默认值与类型转换（int）。

### `replace_env_vars`

- **类型**：函数  |  **行号**：35–42  |  **完整限定名**：`src.config.loader.replace_env_vars`
- **签名**：

```python
def replace_env_vars(value: str) -> str:
```

**摘要**：

Replace environment variables in string values.

### `process_dict`

- **类型**：函数  |  **行号**：45–57  |  **完整限定名**：`src.config.loader.process_dict`
- **签名**：

```python
def process_dict(config: Dict[str, Any]) -> Dict[str, Any]:
```

**摘要**：

Recursively process dictionary to replace environment variables.

### `load_yaml_config`

- **类型**：函数  |  **行号**：63–80  |  **完整限定名**：`src.config.loader.load_yaml_config`
- **签名**：

```python
def load_yaml_config(file_path: str) -> Dict[str, Any]:
```

**摘要**：

Load and process YAML configuration file.

## 调用关系（下游）

**被以下模块导入**：

- `src.config`
- `src.config.configuration`
- `src.graph.checkpoint`
- `src.rag.milvus`
- `src.rag.qdrant`
- `src.server.app`
- `tests.unit.config.test_loader`

## 示例用法

```python
# src/config/loader.py 示例用法
#
# 加载 conf.yaml 与 .env 配置，提供全局配置常量。
#
# 1) 加载 conf.yaml
from src.config.loader import load_yaml_config

config = load_yaml_config("conf.yaml")
search_config = config.get("SEARCH_ENGINE", {})
print(search_config.get("engine"))

# 2) 使用模块级常量（在导入时即从 .env / conf.yaml 读取）
from src.config import SELECTED_SEARCH_ENGINE, SearchEngine

if SELECTED_SEARCH_ENGINE == SearchEngine.TAVILY.value:
    print("使用 Tavily 搜索")

# 3) 获取 LLM 配置
from src.config.loader import get_env
api_key = get_env("OPENAI_API_KEY", default="")
# 注意：仅在需要时读取，避免敏感信息泄露到日志
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

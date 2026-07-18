# `src/podcast/types.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/podcast/types.py`
- **模块导入名**：`src.podcast.types`
- **代码行数**：23
- **架构归属**：src/podcast —— 播客生成子图（脚本撰写 → TTS → 音频合成）

## 模块概述

```text
播客（Podcast）模块的类型定义。

使用 Pydantic 定义脚本相关的数据结构：ScriptLine 表示单行对白
（含男/女声标识与段落文本），Script 表示完整脚本（含语言 locale
与对白行列表），供脚本撰写节点的结构化输出使用。
```

## 依赖关系（上游）

**外部依赖**（第三方库 / 标准库）：

- `from typing import Literal`
- `from pydantic import BaseModel, Field`

## 导出符号表

| 类型 | 名称 | 行号 | 签名 / 值 |
|------|------|------|-----------|
| 类 | `ScriptLine` | 16 | `` |
| 类 | `Script` | 21 | `` |

## 符号详解

### `ScriptLine`

- **类型**：类  |  **行号**：16–18  |  **完整限定名**：`src.podcast.types.ScriptLine`
- **基类**：`BaseModel`
- **定义**：

```python
class ScriptLine(BaseModel):
```
- **成员概览**：

  - `attr speaker`
  - `attr paragraph`

**说明**（自动推断）：

Pydantic 数据模型 `ScriptLine`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

### `Script`

- **类型**：类  |  **行号**：21–23  |  **完整限定名**：`src.podcast.types.Script`
- **基类**：`BaseModel`
- **定义**：

```python
class Script(BaseModel):
```
- **成员概览**：

  - `attr locale`
  - `attr lines`

**说明**（自动推断）：

Pydantic 数据模型 `Script`，用于 API 请求/响应的结构化校验与序列化。字段即对应的数据契约。

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.builder`
- `src.graph.nodes`
- `src.podcast.graph.script_writer_node`
- `src.podcast.graph.state`
- `tests.unit.podcast.test_script_writer_node`

## 示例用法

```python
from src.podcast.types import ScriptLine
#
# TODO: 结合业务场景补充 ScriptLine 的典型调用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

# `src/tools/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/__init__.py`
- **模块导入名**：`src.tools`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：23
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
DeerFlow 工具集包入口。

对外导出研究流程中可用的 LangChain 工具：网页抓取 ``crawl_tool``、
Python 代码执行 ``python_repl_tool``、本地知识检索 ``get_retriever_tool``、
网络搜索 ``get_web_search_tool`` 以及火山引擎语音合成 ``VolcengineTTS``。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .crawl import crawl_tool`
- `from .python_repl import python_repl_tool`
- `from .retriever import get_retriever_tool`
- `from .search import get_web_search_tool`
- `from .tts import VolcengineTTS`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

**被以下模块导入**：

- `src.graph.nodes`
- `src.server.app`

## 示例用法

```python
# import src.tools
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

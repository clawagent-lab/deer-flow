# `src/tools/tavily_search/__init__.py`

> 本文档由 `scripts/gen_api_reference.py` 自动生成。如内容与源码不一致，请重新运行该脚本。

## 文件信息

- **相对路径**：`src/tools/tavily_search/__init__.py`
- **模块导入名**：`src.tools.tavily_search`
- **类型**：包初始化文件（`__init__.py`）
- **代码行数**：13
- **架构归属**：src/tools —— 工具集（搜索、爬取、TTS、Python REPL、检索器、装饰器）

## 模块概述

```text
Tavily 搜索工具子包。

提供对 Tavily 搜索 API 的增强封装，支持返回图像结果，
对外暴露 ``EnhancedTavilySearchAPIWrapper``（API 封装）与 ``TavilySearchWithImages``（LangChain 工具）两个组件。
```

## 依赖关系（上游）

**内部依赖**（项目内模块）：

- `from .tavily_search_api_wrapper import EnhancedTavilySearchAPIWrapper`
- `from .tavily_search_results_with_images import TavilySearchWithImages`

## 导出符号表

_该模块没有顶层类/函数/常量。_

## 符号详解

_无顶层符号。_

## 调用关系（下游）

_暂无其他内部模块导入本模块（可能为入口或叶子模块，或仅被测试间接覆盖）。_

## 示例用法

```python
# import src.tools.tavily_search
# TODO: 补充该模块的典型使用示例。
```

## 备注

- 自动生成时间：2026-07-19T01:15:07
- 重新生成：`python scripts/gen_api_reference.py`

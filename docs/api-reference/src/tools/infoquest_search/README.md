# `src/tools/infoquest_search/` 模块索引

> 本目录下共有 3 个 Python 源文件，下表汇总了每个文件及其文档链接。

| 源文件 | 文档 | 模块名 | 行数 | 顶层符号数 | 简述 |
|--------|------|--------|------|------------|------|
| `src/tools/infoquest_search/__init__.py` | [src/tools/infoquest_search/__init__.py.md](__init__.py.md) | `src.tools.infoquest_search` | 13 | 0 | InfoQuest 搜索工具子包。 |
| `src/tools/infoquest_search/infoquest_search_api.py` | [src/tools/infoquest_search/infoquest_search_api.py.md](infoquest_search_api.py.md) | `src.tools.infoquest_search.infoquest_search_api` | 232 | 4 | Util that calls InfoQuest Search API. |
| `src/tools/infoquest_search/infoquest_search_results.py` | [src/tools/infoquest_search/infoquest_search_results.py.md](infoquest_search_results.py.md) | `src.tools.infoquest_search.infoquest_search_results` | 236 | 3 | Tool for the InfoQuest search API. |

## 目录内依赖关系

```mermaid
graph LR
    src_tools_infoquest_search_infoquest_search_api[src.tools.infoquest_search.infoquest_search_api] --> src_tools_infoquest_search[src.tools.infoquest_search]
    src_tools_infoquest_search_infoquest_search_results[src.tools.infoquest_search.infoquest_search_results] --> src_tools_infoquest_search[src.tools.infoquest_search]
    src_tools_infoquest_search_infoquest_search_api[src.tools.infoquest_search.infoquest_search_api] --> src_tools_infoquest_search_infoquest_search_results[src.tools.infoquest_search.infoquest_search_results]
```

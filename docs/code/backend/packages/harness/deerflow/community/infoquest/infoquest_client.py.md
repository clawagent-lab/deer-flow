# `backend/packages/harness/deerflow/community/infoquest/infoquest_client.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/community/infoquest/infoquest_client.py`  ·  行数: 405

**模块文档首行**（仅供参考）: Util that calls InfoQuest Search And Fetch API.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 1 个

## 依赖（import）
- 模块: json, logging, os, requests
- `typing` -> Any

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `InfoQuestClient`  L17
- _文档首行_: Client for interacting with the InfoQuest web search and fetch API.
- 方法:
  #### `st` `_prepare_headers() -> dict[str, str]`    @staticmethod  L110
    - _文档首行_（仅供参考）: Prepare request headers.
    - 分支数 1，函数体节点数 61；return: headers
    - 调用: getenv, debug, warning
  - 环境变量: getenv (L117), getenv (L118)
  #### `st` `clean_results(raw_results: list[dict[str, dict[str, dict[str, Any]]]]) -> list[dict]`    @staticmethod  L179
    - _文档首行_（仅供参考）: Clean results from InfoQuest Web-Search API.
    - 分支数 14，函数体节点数 413；return: clean_results
    - 调用: debug, set, get, isinstance, add, append, len
  #### `st` `clean_results_with_image_search(raw_results: list[dict[str, dict[str, dict[str, Any]]]]) -> list[dict]`    @staticmethod  L286
    - _文档首行_（仅供参考）: Clean results from InfoQuest Web-Search API.
    - 分支数 6，函数体节点数 227；return: clean_results
    - 调用: debug, set, get, isinstance, add, append, len
  #### `m` `__init__(self, fetch_time: int, fetch_timeout: int, fetch_navigation_timeout: int, search_time_range: int, image_search_time_range: int, image_size: str)`  L20
    - 分支数 1，函数体节点数 241
    - 调用: info, bool, getenv, isEnabledFor, debug
  - 环境变量: getenv (L29)
  #### `m` `fetch(self, url: str, return_format: str) -> str`  L45
    - 分支数 8，函数体节点数 394；return: f'Error: {error_message}', response_data['reader_result'], response_data['content'], response.text
    - 调用: isEnabledFor, len, debug, _prepare_headers, _prepare_crawl_request_data, post, strip, loads, warning, str, error
  - 网络调用: post (L66)
  #### `m` `_prepare_crawl_request_data(self, url: str, return_format: str) -> dict[str, Any]`  L125
    - _文档首行_（仅供参考）: Prepare request data with formatted parameters.
    - 分支数 5，函数体节点数 134；return: data
    - 调用: lower, debug, update
  #### `m` `web_search_raw_results(self, query: str, site: str, output_format: str) -> dict`  L151
    - _文档首行_（仅供参考）: Get results from the InfoQuest Web-Search API synchronously.
    - 分支数 3，函数体节点数 152；return: response_json
    - 调用: _prepare_headers, post, raise_for_status, json, isEnabledFor, dumps, len, debug
  - 网络调用: post (L167)
  #### `m` `web_search(self, query: str, site: str, output_format: str) -> str`  L234
    - 分支数 4，函数体节点数 256；return: result_json, f'Error: {error_message}', json.dumps(raw_results, indent=2, ensure_ascii=False)
    - 调用: isEnabledFor, len, debug, bool, web_search_raw_results, clean_results, dumps, error, warning, str
  #### `m` `image_search_raw_results(self, query: str, site: str, output_format: str) -> dict`  L315
    - _文档首行_（仅供参考）: Get image search results from the InfoQuest Web-Search API synchronously.
    - 分支数 6，函数体节点数 223；return: response_json
    - 调用: _prepare_headers, warning, post, raise_for_status, json, isEnabledFor, dumps, len, debug
  - 网络调用: post (L342)
  #### `m` `image_search(self, query: str, site: str, output_format: str) -> str`  L353
    - 分支数 4，函数体节点数 275；return: result_json, f'Error: {error_message}', json.dumps(raw_results, indent=2, ensure_ascii=False)
    - 调用: isEnabledFor, len, debug, bool, info, image_search_raw_results, clean_results_with_image_search, dumps, error, warning, str

## 文件内调用关系
- `InfoQuestClient.fetch` -> _prepare_headers, _prepare_crawl_request_data
- `InfoQuestClient.web_search_raw_results` -> _prepare_headers
- `InfoQuestClient.web_search` -> web_search_raw_results, clean_results
- `InfoQuestClient.image_search_raw_results` -> _prepare_headers
- `InfoQuestClient.image_search` -> image_search_raw_results, clean_results_with_image_search

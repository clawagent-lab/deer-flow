# `backend/packages/harness/deerflow/utils/readability.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/utils/readability.py`  ·  行数: 84

## 模块概览
- 函数 0 个，类 2 个，模块级常量 1 个

## 依赖（import）
- 模块: logging, re, subprocess
- `urllib.parse` -> urljoin
- `markdownify` -> md
- `readabilipy` -> simple_json_from_html_string

## 模块级常量
- `logger` = logging.getLogger(__name__)

## 类
### 类 `Article`  L12
- 类/实例变量:
  - `url` = <annotated>
- 方法:
  #### `m` `__init__(self, title: str, html_content: str)`  L15
    - 分支数 0，函数体节点数 23
  #### `m` `to_markdown(self, including_title: bool) -> str`  L19
    - 分支数 2，函数体节点数 69；return: markdown
    - 调用: strip, str, md
  #### `m` `to_message(self) -> list[dict]`  L31
    - 分支数 5，函数体节点数 165；return: [{'type': 'text', 'text': 'No content available'}], content
    - 调用: to_markdown, strip, split, enumerate, urljoin, append

### 类 `ReadabilityExtractor`  L58
- 方法:
  #### `m` `extract_article(self, html: str) -> Article`  L59
    - 分支数 4，函数体节点数 181；return: Article(title=title, html_content=html_content)
    - 调用: simple_json_from_html_string, getattr, isinstance, decode, strip, warning, type, get, str, Article
  - 反射: getattr (L63)

## 文件内调用关系
- `Article.to_message` -> to_markdown

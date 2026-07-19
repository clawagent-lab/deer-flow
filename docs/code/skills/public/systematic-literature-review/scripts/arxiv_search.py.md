# `skills/public/systematic-literature-review/scripts/arxiv_search.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/systematic-literature-review/scripts/arxiv_search.py`  ·  行数: 307

**模块文档首行**（仅供参考）: arXiv search client for the systematic-literature-review skill.

## 模块概览
- 函数 6 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: argparse, json, sys
- `__future__` -> annotations
- `typing` -> Any

## 模块级常量
- `NS_MAP` = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://...
- `ARXIV_ENDPOINT` = 'http://export.arxiv.org/api/query'
- `MAX_RESULTS_UPPER_BOUND` = 50
- `DEFAULT_TIMEOUT_SECONDS` = 30

## 函数
#### `ƒ` `_build_search_query(query: str, category: str | None, start_date: str | None, end_date: str | None) -> str`  L94
  - _文档首行_（仅供参考）: Build arXiv's `search_query` field.
  - 分支数 3，函数体节点数 130；return: ' AND '.join(parts)
  - 调用: append, replace, join
  - 文件IO: replace (L119), replace (L120)

#### `ƒ` `_normalise_arxiv_id(raw_id: str) -> str`  L125
  - _文档首行_（仅供参考）: Convert a full arXiv URL to a bare id.
  - 分支数 3，函数体节点数 76；return: base, tail
  - 调用: split, rsplit, rpartition, isdigit

#### `ƒ` `_parse_entry(entry: Any) -> dict`  L145
  - _文档首行_（仅供参考）: Turn one Atom <entry> element into a paper dict.
  - 分支数 3，函数体节点数 306；return: (node.text or '').strip() if node is not None and node.text else '', {'id': arxiv_id, 'title': ' '.join(_text('atom:title').split()), 'authors': authors, 'abstract': abstract, 'published': published, 'updated': updated, 'categories': categories, 'pdf_url': pdf_url, 'abs_url': abs_url}
  - 调用: find, strip, _text, _normalise_arxiv_id, findtext, findall, get, split, join

#### `ƒ` `search(query: str, max_results: int, category: str | None, sort_by: str, start_date: str | None, end_date: str | None) -> list[dict]`  L195
  - _文档首行_（仅供参考）: Query arXiv and return a list of paper dicts.
  - 分支数 1，函数体节点数 151；return: [], [_parse_entry(e) for e in entries]
  - 调用: min, _build_search_query, get, raise_for_status, fromstring, findall, _parse_entry
  - 网络调用: get (L231)

#### `ƒ` `_build_parser() -> argparse.ArgumentParser`  L243
  - 分支数 0，函数体节点数 104；return: parser
  - 调用: ArgumentParser, add_argument

#### `ƒ` `main() -> int`  L285
  - 分支数 1，函数体节点数 96；return: 1, 0
  - 调用: parse_args, _build_parser, search, print, dump, write
  - 文件IO: write (L301)

## 文件内调用关系
- `_parse_entry` -> _normalise_arxiv_id
- `search` -> _build_search_query, _parse_entry
- `main` -> _build_parser, search

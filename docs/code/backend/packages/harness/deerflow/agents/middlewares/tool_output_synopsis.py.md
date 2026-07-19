# `backend/packages/harness/deerflow/agents/middlewares/tool_output_synopsis.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/middlewares/tool_output_synopsis.py`  ·  行数: 636

**模块文档首行**（仅供参考）: Deterministic summaries for oversized tool output previews.

## 模块概览
- 函数 22 个，类 1 个，模块级常量 17 个

## 依赖（import）
- 模块: csv, io, json, re, ET, yaml
- `__future__` -> annotations
- `collections` -> Counter
- `dataclasses` -> dataclass
- `typing` -> Any, Literal

## 模块级常量
- `ToolOutputKind` = Literal['json', 'csv', 'tsv', 'yaml', 'xml', 'code', 'tex...
- `_KEY_LIMIT` = 12
- `_SCALAR_LIMIT` = 6
- `_TABLE_SAMPLE_ROWS` = 50
- `_TABLE_COLUMN_LIMIT` = 18
- `_TEXT_HEADER_LIMIT` = 16
- `_TEXT_EXCERPT_CHARS` = 420
- `_CODE_IMPORT_LIMIT` = 12
- `_CODE_SYMBOL_LIMIT` = 24
- `_JSON_SHAPE_MAX_DEPTH` = 2
- `_JSON_STRUCTURE_LIMIT` = 24
- `_JSON_STRUCTURE_DEPTH` = 4
- `_MAX_SYNOPSIS_INPUT_BYTES` = 5000000
- `_CODE_HINTS` = (re.compile('^\\s*(?:from\\s+\\S+\\s+import|import\\s+\\S...
- `_TABLE_MIN_DATA_ROWS` = 5
- `_TABLE_HEADER_IDENT_RE` = re.compile('^[A-Za-z0-9_][A-Za-z0-9_.\\-]*$')
- `_YAML_KEY_LINE_RE` = re.compile('^\\s*[A-Za-z_][A-Za-z0-9_.\\-]*:\\s*\\S.*$')

## 函数
#### `ƒ` `build_tool_output_synopsis(content: str, *, tool_name: str) -> ToolOutputSynopsis`  L63
  - _文档首行_（仅供参考）: Return a typed synopsis for *content* without using an LLM.
  - 分支数 11，函数体节点数 284；return: ToolOutputSynopsis(kind='unknown', title='Empty output', summary=['The tool returned an empty string.'], structure=[], notable_items=[]), ToolOutputSynopsis(kind='unknown', title='Oversized output', summary=[f"The output has {len(content)} characters ({len(content.encode('utf-8')) / 1024 / 1024:.1f} MB). Parsing skipped due to size limit."], structure=[], notable_items=[], sample=_head_tail_sample(content, _TEXT_EXCERPT_CHARS * 2)), ToolOutputSynopsis(kind='unknown', title='Binary-like output', summary=[f'The output has {len(content)} characters and includes non-text control bytes.'], structure=[], notable_items=[], sample=_head_tail_sample(content, _TEXT_EXCERPT_CHARS * 2)), json_synopsis, xml_synopsis, table, yaml_synopsis, _summarize_code(content), _summarize_text(content, tool_name=tool_name)
  - 调用: ToolOutputSynopsis, len, encode, _head_tail_sample, _looks_binary, strip, _try_json, _try_xml, _try_table, _try_yaml, _looks_code, _summarize_code, _summarize_text

#### `ƒ` `render_tool_output_preview(content: str, *, tool_name: str, virtual_path: str, head_chars: int, tail_chars: int) -> str`  L128
  - _文档首行_（仅供参考）: Render a file-backed preview as a typed synopsis plus a raw head/tail sample.
  - 分支数 4，函数体节点数 317；return: '\n'.join(lines)
  - 调用: len, build_tool_output_synopsis, max, _summarize_text, extend, append, _build_raw_sample, join

#### `ƒ` `_clip(value: str, limit: int) -> str`  L183
  - 分支数 2，函数体节点数 49；return: '', value, value[:max(0, limit - 3)] + '...'
  - 调用: len, max

#### `ƒ` `_build_raw_sample(content: str, *, head_budget: int, tail_budget: int, existing: str) -> str`  L191
  - _文档首行_（仅供参考）: Compose the inline head/tail raw sample.
  - 分支数 8，函数体节点数 229；return: existing, '', content, f'{parts[0]}\n...\n{parts[1]}', parts[0]
  - 调用: len, rfind, append, find

#### `ƒ` `_one_line(value: str, limit: int) -> str`  L226
  - 分支数 0，函数体节点数 28；return: _clip(re.sub('\\s+', ' ', value).strip(), limit)
  - 调用: _clip, strip, sub

#### `ƒ` `_head_tail_sample(content: str, limit: int) -> str`  L230
  - 分支数 2，函数体节点数 64；return: '', content, f'{content[:half]}\n...\n{content[-half:]}'
  - 调用: len, max

#### `ƒ` `_looks_binary(content: str) -> bool`  L239
  - 分支数 1，函数体节点数 69；return: True, controls / max(1, len(sample)) > 0.05
  - 调用: sum, ord, max, len

#### `ƒ` `_type_name(value: Any) -> str`  L247
  - 分支数 5，函数体节点数 61；return: 'object', 'array', 'boolean', 'null', 'number', 'string'
  - 调用: isinstance

#### `ƒ` `_short_value(value: Any) -> str`  L261
  - 分支数 1，函数体节点数 39；return: json.dumps(_clip(value, 80), ensure_ascii=False), _clip(repr(value), 80)
  - 调用: isinstance, dumps, _clip, repr

#### `ƒ` `_json_shape(value: Any, *, depth: int) -> str`  L267
  - 分支数 3，函数体节点数 150；return: '...', f'object(keys={len(value)}{suffix})', f'array(len={len(value)}{suffix})', _type_name(value)
  - 调用: isinstance, str, list, keys, join, len, _json_shape, _type_name

#### `ƒ` `_json_path(parent: str, key: Any) -> str`  L281
  - 分支数 1，函数体节点数 53；return: f'{parent}.{key_text}', f'{parent}[{json.dumps(key_text, ensure_ascii=False)}]'
  - 调用: str, match, dumps

#### `ƒ` `_json_container_description(value: Any) -> str`  L288
  - 分支数 3，函数体节点数 114；return: f'object keys {len(value)}{suffix}', detail, _type_name(value)
  - 调用: isinstance, str, list, keys, join, len, _type_name

#### `ƒ` `_json_container_paths(value: Any, *, limit: int) -> list[str]`  L301
  - _文档首行_（仅供参考）: Summarize nested JSON container paths.
  - 分支数 7，函数体节点数 211；return: None, paths
  - 调用: len, isinstance, list, items, _json_path, append, _json_container_description, walk

#### `ƒ` `_scalar_examples(value: Any, *, path: str, limit: int) -> list[str]`  L334
  - 分支数 7，函数体节点数 206；return: None, examples
  - 调用: len, isinstance, list, items, walk, enumerate, append, _short_value

#### `ƒ` `_try_json(content: str) -> ToolOutputSynopsis | None`  L358
  - 分支数 6，函数体节点数 277；return: None, ToolOutputSynopsis(kind='json', title='JSON output', summary=summary, structure=structure, notable_items=notable)
  - 调用: strip, startswith, JSONDecoder, raw_decode, len, _json_shape, extend, _json_container_paths, _scalar_examples, isinstance, str, keys, append, join, _type_name, ToolOutputSynopsis

#### `ƒ` `_try_xml(stripped: str) -> ToolOutputSynopsis | None`  L401
  - 分支数 3，函数体节点数 144；return: None, ToolOutputSynopsis(kind='xml', title='XML output', summary=[f'XML document with root tag {root.tag}.'], structure=structure, notable_items=[])
  - 调用: startswith, fromstring, Counter, list, len, extend, most_common, ToolOutputSynopsis

#### `ƒ` `_try_table(content: str, *, delimiter: str, kind: Literal['csv', 'tsv']) -> ToolOutputSynopsis | None`  L427
  - 分支数 7，函数体节点数 422；return: None, ToolOutputSynopsis(kind=kind, title=title, summary=[f'{label} table with {data_rows} data rows and {width} columns.'], structure=[f"columns: {', '.join(columns[:_TABLE_COLUMN_LIMIT])}", f"first data row: {' | '.join(first_data_pairs) or '(none)'}"], notable_items=[])
  - 调用: join, splitlines, list, reader, StringIO, any, strip, len, match, startswith, enumerate, sum, max, zip, append, _clip, upper, ToolOutputSynopsis

#### `ƒ` `_looks_yaml(content: str) -> bool`  L483
  - _文档首行_（仅供参考）: Heuristic detector for YAML-shaped content.
  - 分支数 6，函数体节点数 106；return: True, False
  - 调用: lstrip, startswith, _looks_code, splitlines, match, strip, split, isupper

#### `ƒ` `_try_yaml(content: str) -> ToolOutputSynopsis | None`  L513
  - 分支数 9，函数体节点数 275；return: None, ToolOutputSynopsis(kind='yaml', title='YAML output', summary=summary, structure=structure, notable_items=[])
  - 调用: _looks_yaml, len, safe_load, isinstance, sum, values, str, keys, join, list, items, append, _type_name, ToolOutputSynopsis

#### `ƒ` `_looks_code(content: str) -> bool`  L558
  - 分支数 0，函数体节点数 24；return: any((pattern.search(content) for pattern in _CODE_HINTS))
  - 调用: any, search

#### `ƒ` `_summarize_code(content: str) -> ToolOutputSynopsis`  L562
  - 分支数 4，函数体节点数 197；return: ToolOutputSynopsis(kind='code', title='Code-like output', summary=[f'Code-like text with {len(lines)} lines.'], structure=structure, notable_items=symbols[:_CODE_SYMBOL_LIMIT])
  - 调用: splitlines, strip, match, append, _one_line, group, len, join, ToolOutputSynopsis

#### `ƒ` `_summarize_text(content: str, *, tool_name: str, include_excerpts: bool) -> ToolOutputSynopsis`  L592
  - 分支数 8，函数体节点数 331；return: ToolOutputSynopsis(kind='text', title='Text output', summary=summary_lines, structure=[], notable_items=[])
  - 调用: splitlines, strip, sub, set, match, _one_line, add, append, len, split, join, max, ToolOutputSynopsis

## 类
### 类 `ToolOutputSynopsis`  L52  @dataclass(...)
- _文档首行_: Structured preview data for an oversized tool output.
- 类/实例变量:
  - `kind` = <annotated>
  - `title` = <annotated>
  - `summary` = <annotated>
  - `structure` = <annotated>
  - `notable_items` = <annotated>
  - `sample` = ''

## 文件内调用关系
- `build_tool_output_synopsis` -> _head_tail_sample, _looks_binary, _try_json, _try_xml, _try_table, _try_yaml, _looks_code, _summarize_code, _summarize_text
- `render_tool_output_preview` -> build_tool_output_synopsis, _summarize_text, _build_raw_sample
- `_one_line` -> _clip
- `_short_value` -> _clip
- `_json_shape` -> _json_shape, _type_name
- `_json_container_description` -> _type_name
- `_json_container_paths` -> _json_path, _json_container_description
- `_scalar_examples` -> _short_value
- `_try_json` -> _json_shape, _json_container_paths, _scalar_examples, _type_name
- `_try_table` -> _clip
- `_looks_yaml` -> _looks_code
- `_try_yaml` -> _looks_yaml, _type_name
- `_summarize_code` -> _one_line
- `_summarize_text` -> _one_line

# `backend/packages/harness/deerflow/utils/file_conversion.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/utils/file_conversion.py`  ·  行数: 320

**模块文档首行**（仅供参考）: File conversion utilities.

## 模块概览
- 函数 9 个，类 0 个，模块级常量 8 个

## 依赖（import）
- 模块: asyncio, logging, re
- `pathlib` -> Path
- `deerflow.config.app_config` -> get_app_config

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `CONVERTIBLE_EXTENSIONS` = {'.pdf', '.ppt', '.pptx', '.xls', '.xlsx', '.doc', '.docx'}
- `_ASYNC_THRESHOLD_BYTES` = 1 * 1024 * 1024
- `_MIN_CHARS_PER_PAGE` = 50
- `_BOLD_HEADING_RE` = re.compile('^\\*\\*((ITEM|PART|SECTION|SCHEDULE|EXHIBIT|A...
- `_SPLIT_BOLD_HEADING_RE` = re.compile('^\\*\\*[\\dA-Z][\\d\\.]*\\*\\*\\s+\\*\\*(?!\\...
- `MAX_OUTLINE_ENTRIES` = 50
- `_ALLOWED_PDF_CONVERTERS` = {'auto', 'pymupdf4llm', 'markitdown'}

## 函数
#### `ƒ` `_pymupdf_output_too_sparse(text: str, file_path: Path) -> bool`  L50
  - _文档首行_（仅供参考）: Return True if pymupdf4llm output is suspiciously short (image-based PDF).
  - 分支数 4，函数体节点数 111；return: chars / pages < _MIN_CHARS_PER_PAGE, chars < 200
  - 调用: len, strip, open, str, close
  - 文件IO: open (L63)

#### `ƒ` `_convert_pdf_with_pymupdf4llm(file_path: Path) -> str | None`  L79
  - _文档首行_（仅供参考）: Attempt PDF conversion with pymupdf4llm.
  - 分支数 2，函数体节点数 48；return: None, pymupdf4llm.to_markdown(str(file_path))
  - 调用: to_markdown, str, exception

#### `ƒ` `_convert_with_markitdown(file_path: Path) -> str`  L97
  - _文档首行_（仅供参考）: Convert any supported file to markdown text using MarkItDown.
  - 分支数 0，函数体节点数 30；return: md.convert(str(file_path)).text_content
  - 调用: MarkItDown, convert, str

#### `ƒ` `_do_convert(file_path: Path, pdf_converter: str) -> str`  L105
  - _文档首行_（仅供参考）: Synchronous conversion — called directly or via asyncio.to_thread.
  - 分支数 4，函数体节点数 96；return: pymupdf_text, _convert_with_markitdown(file_path)
  - 调用: lower, _convert_pdf_with_pymupdf4llm, _pymupdf_output_too_sparse, warning, len, strip, _convert_with_markitdown

#### `⏵ƒ` `async convert_file_to_markdown(file_path: Path) -> Path | None`  L138
  - _文档首行_（仅供参考）: Convert a supported document file to Markdown.
  - 分支数 2，函数体节点数 121；return: md_path, None
  - 调用: _get_pdf_converter, stat, to_thread, _do_convert, with_suffix, write_text, info, len, error
  - 文件IO: stat (L153), write_text (L161)

#### `ƒ` `_clean_bold_title(raw: str) -> str`  L207
  - _文档首行_（仅供参考）: Normalise a title string that may contain pymupdf4llm bold artefacts.
  - 分支数 1，函数体节点数 53；return: m.group(1).strip(), merged
  - 调用: strip, sub, fullmatch, group

#### `ƒ` `extract_outline(md_path: Path) -> list[dict]`  L228
  - _文档首行_（仅供参考）: Extract document outline (headings) from a Markdown file.
  - 分支数 11，函数体节点数 214；return: [], outline
  - 调用: open, enumerate, strip, startswith, _clean_bold_title, lstrip, append, match, group, join, findall, len, pop
  - 文件IO: open (L257)

#### `ƒ` `_get_uploads_config_value(key: str, default: object) -> object`  L295
  - _文档首行_（仅供参考）: Read a value from the uploads config, supporting dict and attribute access.
  - 分支数 1，函数体节点数 56；return: uploads_cfg.get(key, default), getattr(uploads_cfg, key, default)
  - 调用: get_app_config, getattr, isinstance, get
  - 反射: getattr (L298), getattr (L301)

#### `ƒ` `_get_pdf_converter() -> str`  L304
  - _文档首行_（仅供参考）: Read pdf_converter setting from app config, defaulting to 'auto'.
  - 分支数 2，函数体节点数 51；return: 'auto', raw
  - 调用: lower, strip, str, _get_uploads_config_value, warning

## 文件内调用关系
- `_do_convert` -> _convert_pdf_with_pymupdf4llm, _pymupdf_output_too_sparse, _convert_with_markitdown
- `convert_file_to_markdown` -> _get_pdf_converter, _do_convert
- `extract_outline` -> _clean_bold_title
- `_get_pdf_converter` -> _get_uploads_config_value

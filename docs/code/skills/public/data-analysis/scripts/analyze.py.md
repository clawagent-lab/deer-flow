# `skills/public/data-analysis/scripts/analyze.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/data-analysis/scripts/analyze.py`  ·  行数: 567

**模块文档首行**（仅供参考）: Data Analysis Script using DuckDB.

## 模块概览
- 函数 15 个，类 0 个，模块级常量 3 个

## 依赖（import）
- 模块: argparse, hashlib, json, logging, os, re, subprocess, sys, tempfile

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `CACHE_DIR` = os.path.join(tempfile.gettempdir(), '.data-analysis-cache')
- `TABLE_MAP_SUFFIX` = '.table_map.json'

## 函数
#### `ƒ` `compute_files_hash(files: list[str]) -> str`  L38
  - _文档首行_（仅供参考）: Compute a combined SHA256 hash of all input files for cache key.
  - 分支数 4，函数体节点数 78；return: hasher.hexdigest()
  - 调用: sha256, sorted, open, read, update, encode, hexdigest
  - 文件IO: open (L43), read (L44)

#### `ƒ` `get_cache_db_path(files_hash: str) -> str`  L52
  - _文档首行_（仅供参考）: Get the path to the cached DuckDB database file.
  - 分支数 0，函数体节点数 34；return: os.path.join(CACHE_DIR, f'{files_hash}.duckdb')
  - 调用: makedirs, join

#### `ƒ` `get_table_map_path(files_hash: str) -> str`  L58
  - _文档首行_（仅供参考）: Get the path to the cached table map JSON file.
  - 分支数 0，函数体节点数 26；return: os.path.join(CACHE_DIR, f'{files_hash}{TABLE_MAP_SUFFIX}')
  - 调用: join

#### `ƒ` `save_table_map(files_hash: str, table_map: dict[str, str]) -> None`  L63
  - _文档首行_（仅供参考）: Save table map to a JSON file alongside the cached DB.
  - 分支数 1，函数体节点数 51
  - 调用: get_table_map_path, open, dump
  - 文件IO: open (L66)

#### `ƒ` `load_table_map(files_hash: str) -> dict[str, str] | None`  L70
  - _文档首行_（仅供参考）: Load table map from cache. Returns None if not found.
  - 分支数 3，函数体节点数 68；return: None, json.load(f)
  - 调用: get_table_map_path, exists, open, load
  - 文件IO: exists (L73), open (L76)

#### `ƒ` `sanitize_table_name(name: str) -> str`  L82
  - _文档首行_（仅供参考）: Sanitize a sheet/file name into a valid SQL table name.
  - 分支数 1，函数体节点数 45；return: sanitized
  - 调用: sub, isdigit

#### `ƒ` `load_files(con: duckdb.DuckDBPyConnection, files: list[str]) -> dict[str, str]`  L90
  - _文档首行_（仅供参考）: Load Excel/CSV files into DuckDB tables.
  - 分支数 4，函数体节点数 148；return: table_map
  - 调用: execute, exists, error, lower, splitext, _load_excel, _load_csv, warning
  - 文件IO: exists (L100)

#### `ƒ` `_load_excel(con: duckdb.DuckDBPyConnection, file_path: str, table_map: dict[str, str]) -> None`  L116
  - _文档首行_（仅供参考）: Load all sheets from an Excel file into DuckDB tables.
  - 分支数 3，函数体节点数 189
  - 调用: load_workbook, close, sanitize_table_name, values, execute, fetchone, info, warning

#### `ƒ` `_load_csv(con: duckdb.DuckDBPyConnection, file_path: str, table_map: dict[str, str]) -> None`  L158
  - _文档首行_（仅供参考）: Load a CSV file into a DuckDB table.
  - 分支数 2，函数体节点数 173
  - 调用: splitext, basename, sanitize_table_name, values, execute, fetchone, info, warning

#### `ƒ` `action_inspect(con: duckdb.DuckDBPyConnection, table_map: dict[str, str]) -> str`  L188
  - _文档首行_（仅供参考）: Inspect the schema of all loaded tables.
  - 分支数 7，函数体节点数 490；return: result
  - 调用: items, append, fetchone, execute, fetchall, len, join, enumerate, fetchdf, to_string, str, print

#### `ƒ` `action_query(con: duckdb.DuckDBPyConnection, sql: str, table_map: dict[str, str], output_file: str | None) -> str`  L241
  - _文档首行_（仅供参考）: Execute a SQL query and return/export results.
  - 分支数 5，函数体节点数 242；return: error_msg, _export_results(columns, rows, output_file), _format_table(columns, rows)
  - 调用: sorted, items, len, sub, escape, execute, fetchall, join, print, _export_results, _format_table

#### `ƒ` `_format_table(columns: list[str], rows: list[tuple]) -> str`  L282
  - _文档首行_（仅供参考）: Format query results as a readable table.
  - 分支数 4，函数体节点数 284；return: msg, result
  - 调用: print, len, str, enumerate, max, min, join, ljust, range, append

#### `ƒ` `_export_results(columns: list[str], rows: list[tuple], output_file: str) -> str`  L317
  - _文档首行_（仅供参考）: Export query results to a file (CSV, JSON, or Markdown).
  - 分支数 11，函数体节点数 367；return: msg
  - 调用: makedirs, dirname, lower, splitext, open, writer, writerow, writerows, enumerate, hasattr, isoformat, isinstance, hex, append, dump, write, join, replace, str, print（+1）
  - 文件IO: open (L325), open (L343), open (L347), write (L349), write (L350), write (L353), replace (L354)
  - 反射: hasattr (L337)

#### `ƒ` `action_summary(con: duckdb.DuckDBPyConnection, table_name: str, table_map: dict[str, str]) -> str`  L366
  - _文档首行_（仅供参考）: Generate statistical summary for a table.
  - 分支数 9，函数体节点数 601；return: msg, result
  - 调用: get, fetchall, execute, join, items, print, fetchone, append, upper, strip, sub, zip, isinstance

#### `ƒ` `main()`  L480
  - 分支数 8，函数体节点数 413
  - 调用: ArgumentParser, add_argument, parse_args, error, compute_files_hash, get_cache_db_path, load_table_map, exists, info, connect, len, join, keys, load_files, close, remove, exit, save_table_map, action_inspect, action_query（+1）
  - 文件IO: exists (L525), exists (L543)

## 文件内调用关系
- `save_table_map` -> get_table_map_path
- `load_table_map` -> get_table_map_path
- `load_files` -> _load_excel, _load_csv
- `_load_excel` -> sanitize_table_name
- `_load_csv` -> sanitize_table_name
- `action_query` -> _export_results, _format_table
- `main` -> compute_files_hash, get_cache_db_path, load_table_map, load_files, save_table_map, action_inspect, action_query, action_summary

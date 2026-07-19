# `backend/packages/harness/deerflow/sandbox/search.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/sandbox/search.py`  ·  行数: 223

## 模块概览
- 函数 7 个，类 1 个，模块级常量 6 个

## 依赖（import）
- 模块: fnmatch, os, re
- `dataclasses` -> dataclass
- `pathlib` -> Path, PurePosixPath

## 模块级常量
- `IGNORE_PATTERNS` = ['.git', '.svn', '.hg', '.bzr', 'node_modules', '__pycach...
- `DEFAULT_MAX_FILE_SIZE_BYTES` = 1000000
- `DEFAULT_LINE_SUMMARY_LENGTH` = 200
- `_EXACT_IGNORE_NAMES` = frozenset((os.path.normcase(p) for p in IGNORE_PATTERNS i...
- `_GLOB_IGNORE_PATTERNS` = [p for p in IGNORE_PATTERNS if any((c in p for c in '*?['))]
- `_GLOB_IGNORE_RE` = re.compile('|'.join((fnmatch.translate(os.path.normcase(p...

## 函数
#### `ƒ` `should_ignore_name(name: str) -> bool`  L82
  - 分支数 1，函数体节点数 46；return: True, _GLOB_IGNORE_RE is not None and _GLOB_IGNORE_RE.match(normalized) is not None
  - 调用: normcase, match

#### `ƒ` `should_ignore_path(path: str) -> bool`  L89
  - 分支数 0，函数体节点数 33；return: any((should_ignore_name(segment) for segment in path.replace('\\', '/').split('/') if segment))
  - 调用: any, should_ignore_name, split, replace
  - 文件IO: replace (L90)

#### `ƒ` `path_matches(pattern: str, rel_path: str) -> bool`  L93
  - 分支数 2，函数体节点数 49；return: True, path.match(pattern[3:]), False
  - 调用: PurePosixPath, match, startswith

#### `ƒ` `truncate_line(line: str, max_chars: int) -> str`  L102
  - 分支数 1，函数体节点数 48；return: line, line[:max_chars - 3] + '...'
  - 调用: rstrip, len

#### `ƒ` `is_binary_file(path: Path, sample_size: int) -> bool`  L109
  - 分支数 2，函数体节点数 38；return: b'\x00' in handle.read(sample_size), True
  - 调用: open, read
  - 文件IO: open (L111), read (L112)

#### `ƒ` `find_glob_matches(root: Path, pattern: str, *, include_dirs: bool, max_results: int) -> tuple[list[str], bool]`  L117
  - 分支数 11，函数体节点数 276；raise: FileNotFoundError(root), NotADirectoryError(root)；return: (matches, truncated)
  - 调用: resolve, exists, FileNotFoundError, is_dir, NotADirectoryError, walk, should_ignore_name, relative_to, Path, as_posix, path_matches, append, str, len
  - 文件IO: exists (L122)

#### `ƒ` `find_grep_matches(root: Path, pattern: str, *, glob_pattern: str | None, literal: bool, case_sensitive: bool, max_results: int, max_file_size: int, line_summary_length: int) -> tuple[list[GrepMatch], bool]`  L155
  - 分支数 15，函数体节点数 403；raise: FileNotFoundError(root), NotADirectoryError(root)；return: (matches, truncated)
  - 调用: resolve, exists, FileNotFoundError, is_dir, NotADirectoryError, escape, compile, walk, should_ignore_name, relative_to, Path, as_posix, path_matches, is_symlink, is_relative_to, stat, is_binary_file, open, enumerate, len（+5）
  - 文件IO: exists (L170), stat (L202), open (L204)
  - 危险执行: compile (L177)

## 类
### 类 `GrepMatch`  L65  @dataclass(...)
- 类/实例变量:
  - `path` = <annotated>
  - `line_number` = <annotated>
  - `line` = <annotated>

## 文件内调用关系
- `should_ignore_path` -> should_ignore_name
- `find_glob_matches` -> should_ignore_name, path_matches
- `find_grep_matches` -> should_ignore_name, path_matches, is_binary_file, truncate_line

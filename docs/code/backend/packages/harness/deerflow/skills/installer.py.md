# `backend/packages/harness/deerflow/skills/installer.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/installer.py`  ·  行数: 336

**模块文档首行**（仅供参考）: Shared skill archive installation logic.

## 模块概览
- 函数 20 个，类 2 个，模块级常量 5 个

## 功能语义解读

### 模块职责
本模块为 Gateway 与 Client 共享的 skill ZIP 安装包**安全提取与扫描**纯业务逻辑层（模块 docstring L1-5 明确：无 FastAPI/HTTP 依赖，两端均委托至此）。职责链为：压缩包多层安全校验 → 受控提取到目标目录 → 提取内容静态/动态扫描 → 原子性安装到保留目标位置。模块不直接处理 HTTP/上传，仅暴露同步入口与异步扫描协程供上层路由调用。

### safe_extract_skill_archive 多层防护（L117-177）
核心防护函数，默认参数 `max_total_size=512*1024*1024`（**512MB**）、`max_entries=4096`（**4096 条目**），按以下顺序施加多层防护：

1. **条目数预检（zip bomb by entry count）**：L141-148 在任何 per-member 工作之前先检查 `len(infos) > max_entries`，超过 4096 立即 `raise ValueError`。注释明确说明此检查**无条件执行**（不依赖可选的 `skill_scan.enabled`），因为提取路径每条安装必经；同类早 abort 也存在于 `skillscan/orchestrator.py::scan_archive_preflight`，但那是可选的。
2. **路径遍历防护**：L150-152 调用 `is_unsafe_zip_member`（L64-79）拒绝三类不安全路径——POSIX 绝对路径（`/` 开头）、`PurePosixPath.is_absolute()`、`PureWindowsPath(name).is_absolute()`（兼容 Windows 盘符），以及 `..` 出现在路径 parts 中的条目。
3. **符号链接跳过**：L154-156 通过 `is_symlink_member`（L82-85，读取 `external_attr >> 16` 后 `stat.S_ISLNK(mode)`）检测符号链接条目，**不物化**，仅 `logger.warning` 后 `continue`，避免链接逃逸目标目录。
4. **目标越界二次校验**：L158-161 将 `\` 统一为 `/`、`posixpath.normpath` 规范化后用 `dest_root.joinpath(*PurePosixPath(...).parts)` 拼接，再 `member_path.resolve().is_relative_to(dest_root)` 二次确认未逃逸目标根目录（针对规范化后仍能越界的边缘情况）。
5. **可执行二进制魔数检测**：L168-172 在写入首块（65536 字节 chunk）时调用 `is_executable_binary_prefix` 检测 ELF/PE/Mach-O 魔数，命中即 `raise ValueError(f"Archive contains executable binary member: {info.filename!r}")`，在数据落盘前拦截。
6. **总解压体积累计（zip bomb by size）**：L174-176 累计 `total_written`，超过 512MB 即 `raise ValueError("Skill archive is too large or appears highly compressed.")`，对高度压缩炸弹有效。

补充：目录条目（`info.is_dir()`）仅 `mkdir` 不写数据不累计体积；常规文件以 65536 字节块流式写入并实时累计，魔数检测仅在 `first_chunk` 触发一次。

### _EXECUTABLE_MAGIC_PREFIXES 检测格式（L34-45）
模块级常量为 10 元组，覆盖三大类可执行格式的完整魔数。注释 L32-33 说明使用**完整 magic 而非较短共享前缀**，避免误伤非可执行数据文件（如某些短前缀可能匹配二进制数据）：

- `b"\x7fELF"` — ELF（Linux/Unix 可执行）
- `b"MZ"` — PE/DOS（Windows 可执行，含 .exe/.dll）
- Mach-O 单架构四端序：
  - `b"\xfe\xed\xfa\xce"` — 32-bit big-endian
  - `b"\xfe\xed\xfa\xcf"` — 64-bit big-endian
  - `b"\xce\xfa\xed\xfe"` — 32-bit little-endian
  - `b"\xcf\xfa\xed\xfe"` — 64-bit little-endian
- Mach-O fat 多架构四变体：
  - `b"\xca\xfe\xba\xbe"` — fat big-endian
  - `b"\xbe\xba\xfe\xca"` — fat little-endian
  - `b"\xca\xfe\xba\xbf"` — fat64 big-endian
  - `b"\xbf\xba\xfe\xca"` — fat64 little-endian

`is_executable_binary_prefix`（L88-90）通过 `prefix.startswith(_EXECUTABLE_MAGIC_PREFIXES)` 单次判定——只要文件首块以任一魔数开头即判为可执行二进制。注意 `MZ` 仅 2 字节较短，但 PE 文件头强制该前缀，且完整 magic 元组中其他项均为 4 字节，整体误伤风险可控。

### SkillAlreadyExistsError / SkillSecurityScanError 异常用途

- **`SkillAlreadyExistsError`（L48-49，继承 ValueError）**：在 `_move_staged_skill_into_reserved_target`（L216-230）中抛出。流程为 `target.mkdir(mode=0o700)`（L220）尝试创建保留目标，若已存在则抛 `FileExistsError`，L226-227 转换为 `SkillAlreadyExistsError(f"Skill '{target.name}' already exists")`。`finally` 块（L228-230）在"已预留目录但未完成安装"时回滚 `shutil.rmtree(target)`，保证目标目录不留半成品残留。
- **`SkillSecurityScanError`（L52-61，继承 ValueError）**：携带 `findings: list[StaticFinding]` 与 `skill_name: str | None` 上下文。`__init__`（L58-61）将 findings 浅拷贝为 `dict` 列表（`[dict(finding) for finding in (findings or [])]`），避免外部可变引用污染。该异常在以下场景抛出：
  - 文件非 UTF-8（L243，`UnicodeDecodeError` 转换）
  - `scan_skill_content` 内部异常（L248，任意 `Exception` 包装）
  - scanner `decision == "block"`（L252-255，区分 SKILL.md 与普通文件消息文案）
  - executable 文件但 `decision != "allow"`（L256-257，**即 warn 也不允许可执行文件**）
  - decision 不在 `{"allow","warn"}`（L258-259，未知决策值）
  - 嵌套 SKILL.md（L305，任何子目录下名为 SKILL.md 的文件被禁止）
  - 静态扫描 blocked / 失败（L283-285，`StaticScanBlockedError`/`StaticScannerError` 转换）
  - archive 预检 critical findings（L268-272，`scan_archive_preflight_or_raise` 中过滤 `severity == "CRITICAL"`）

### 扫描策略：scripts/ 按可执行扫描，references/templates 按非可执行扫描
`_scan_skill_archive_contents_or_raise`（L293-323）的扫描编排按以下顺序：

1. **整树静态扫描**：先调用 `_scan_static_skill_archive_or_raise`（L279-285）执行 `enforce_static_scan`（通过 `asyncio.to_thread` 卸载到线程池避免阻塞事件循环），返回 `static_findings` 供后续 per-file 复用。
2. **顶层 SKILL.md 单独扫描**：L297-298 以 `executable=False`、附带该文件的 static findings 扫描。
3. **全量枚举**：`_collect_scannable_files`（L288-290）`sorted(skill_dir.rglob('*'))` 排序后过滤 `is_file()`，结果稳定可预测。
4. **顶层 SKILL.md 跳过**（L302-303，已在上一步扫描）；**嵌套 SKILL.md 拒绝**（L304-305，任何子目录下名为 SKILL.md 的文件直接 `raise SkillSecurityScanError`）。
5. **per-file 分类扫描**：
   - `_is_code_file`（L205-213）返回 True → 以 `executable=True` 扫描（L307-314）。判定逻辑：`_is_code_file_by_name`（L198-202）——`scripts/` 下任何文件，或后缀属于 `_CODE_SUFFIXES`（.bash/.cjs/.js/.mjs/.php/.pl/.ps1/.py/.rb/.sh/.ts/.zsh）；否则对**无后缀**文件 `asyncio.to_thread(_has_shebang, path)` 检测 `#!` 前缀（L190-195，shebang 嗅探卸载到线程池）。
   - 否则若 `_should_scan_support_file`（L184-187）返回 True → 以 `executable=False` 扫描（L315-322）。该函数判定：`scripts/` 下任何文件（实际被上一分支短路，不会到达此处），或位于 `references/`/`templates/` 且后缀属于 `_PROMPT_INPUT_SUFFIXES`（.json/.markdown/.md/.rst/.txt/.yaml/.yml）。
6. **实际生效策略**：`scripts/` 全部按**可执行**扫描（含无后缀 shebang 脚本）；`references/`、`templates/` 下指定文本后缀文件按**非可执行**扫描；其余文件（无 shebang 的无后缀文件、不在白名单后缀的文件）**不进入内容扫描**，仅受静态扫描覆盖。

### _run_async_install 同步/异步桥接（L326-335）
该函数将异步安装协程 `coro` 桥接到同步调用方，兼容两种调用上下文：

1. **检测当前事件循环**：L327-330 尝试 `asyncio.get_running_loop()`；若抛 `RuntimeError`（当前线程无运行中的事件循环）则置 `loop = None`。
2. **已在事件循环中（嵌套场景）**：L332-334 若 `loop is not None and loop.is_running()`——即调用方自身已身处事件循环，直接 `asyncio.run` 会抛 "asyncio.run() cannot be called from a running event loop"。此时创建 `ThreadPoolExecutor(max_workers=1)`，`executor.submit(asyncio.run, coro)` 在**新线程**中启动独立事件循环运行协程，主线程 `.result()` 阻塞等待结果。新线程无运行中的循环，`asyncio.run` 可正常工作。
3. **无运行中的循环（纯同步场景）**：L335 直接 `asyncio.run(coro)` 在当前线程创建临时事件循环执行并返回。

此模式使得同一安装入口既可被纯同步代码（如 CLI、后台任务）调用，也可被 async 框架（如 FastAPI/Starlette 路由）调用。线程池隔离的关键意义在于：调用 `_run_async_install` 的同步函数虽然会阻塞，但与其共享调用方事件循环的其他协程不会被阻塞——重活在新线程的独立事件循环中执行，主线程仅 `.result()` 等待。

## 依赖（import）
- 模块: asyncio, concurrent.futures, logging, posixpath, shutil, stat, zipfile
- `pathlib` -> Path, PurePosixPath, PureWindowsPath
- `deerflow.skills.permissions` -> make_skill_tree_sandbox_readable
- `deerflow.skills.security_scanner` -> scan_skill_content
- `deerflow.skills.security_static_scanner` -> StaticFinding, StaticScanBlockedError, StaticScannerError, enforce_static_scan, scan_archive_preflight, skill_scan_enabled

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_PROMPT_INPUT_DIRS` = {'references', 'templates'}
- `_PROMPT_INPUT_SUFFIXES` = frozenset({'.json', '.markdown', '.md', '.rst', '.txt', '...
- `_CODE_SUFFIXES` = frozenset({'.bash', '.cjs', '.js', '.mjs', '.php', '.pl',...
- `_EXECUTABLE_MAGIC_PREFIXES` = (b'\x7fELF', b'MZ', b'\xfe\xed\xfa\xce', b'\xfe\xed\xfa\x...

## 函数
#### `ƒ` `is_unsafe_zip_member(info: zipfile.ZipInfo) -> bool`  L64
  - _文档首行_（仅供参考）: Return True if the zip member path is absolute or attempts directory traversal.
  - 分支数 5，函数体节点数 83；return: False, True
  - 调用: replace, startswith, PurePosixPath, is_absolute, PureWindowsPath
  - 文件IO: replace (L69)

#### `ƒ` `is_symlink_member(info: zipfile.ZipInfo) -> bool`  L82
  - _文档首行_（仅供参考）: Detect symlinks based on the external attributes stored in the ZipInfo.
  - 分支数 0，函数体节点数 29；return: stat.S_ISLNK(mode)
  - 调用: S_ISLNK

#### `ƒ` `is_executable_binary_prefix(prefix: bytes) -> bool`  L88
  - _文档首行_（仅供参考）: Detect ELF, PE, and Mach-O executables by magic bytes.
  - 分支数 0，函数体节点数 17；return: prefix.startswith(_EXECUTABLE_MAGIC_PREFIXES)
  - 调用: startswith

#### `ƒ` `should_ignore_archive_entry(path: Path) -> bool`  L93
  - _文档首行_（仅供参考）: Return True for macOS metadata dirs and dotfiles.
  - 分支数 0，函数体节点数 27；return: path.name.startswith('.') or path.name == '__MACOSX'
  - 调用: startswith

#### `ƒ` `resolve_skill_dir_from_archive(temp_path: Path) -> Path`  L98
  - _文档首行_（仅供参考）: Locate the skill root directory from extracted archive contents.
  - 分支数 2，函数体节点数 68；raise: ValueError('Skill archive is empty')；return: items[0], temp_path
  - 调用: iterdir, should_ignore_archive_entry, ValueError, len, is_dir
  - 文件IO: iterdir (L109)

#### `ƒ` `safe_extract_skill_archive(zip_ref: zipfile.ZipFile, dest_path: Path, max_total_size: int, max_entries: int) -> None`  L117
  - _文档首行_（仅供参考）: Safely extract a skill archive with security protections.
  - 分支数 10，函数体节点数 289；raise: ValueError(f'Skill archive contains too many entries ({len(infos)} > {max_entries}).'), ValueError(f'Archive contains unsafe member path: {info.filename!r}'), ValueError(f'Zip entry escapes destination: {info.filename!r}'), ValueError(f'Archive contains executable binary member: {info.filename!r}'), ValueError('Skill archive is too large or appears highly compressed.')
  - 调用: resolve, infolist, len, ValueError, is_unsafe_zip_member, is_symlink_member, warning, normpath, replace, joinpath, PurePosixPath, is_relative_to, mkdir, is_dir, open, read, is_executable_binary_prefix, write
  - 文件IO: replace (L158), mkdir (L162), mkdir (L165), open (L168), open (L168), read (L170), write (L177)

#### `ƒ` `_is_script_support_file(rel_path: Path) -> bool`  L180
  - 分支数 0，函数体节点数 27；return: bool(rel_path.parts) and rel_path.parts[0] == 'scripts'
  - 调用: bool

#### `ƒ` `_should_scan_support_file(rel_path: Path) -> bool`  L184
  - 分支数 1，函数体节点数 47；return: True, bool(rel_path.parts) and rel_path.parts[0] in _PROMPT_INPUT_DIRS and (rel_path.suffix.lower() in _PROMPT_INPUT_SUFFIXES)
  - 调用: _is_script_support_file, bool, lower

#### `ƒ` `_has_shebang(path: Path) -> bool`  L190
  - 分支数 2，函数体节点数 33；return: f.read(2) == b'#!', False
  - 调用: open, read
  - 文件IO: open (L192), read (L193)

#### `ƒ` `_is_code_file_by_name(rel_path: Path) -> bool`  L198
  - _文档首行_（仅供参考）: Pure name-based code classification: scripts/ members and code suffixes.
  - 分支数 1，函数体节点数 29；return: True, rel_path.suffix.lower() in _CODE_SUFFIXES
  - 调用: _is_script_support_file, lower

#### `⏵ƒ` `async _is_code_file(path: Path, rel_path: Path) -> bool`  L205
  - _文档首行_（仅供参考）: Classify code files anywhere in the tree for the executable scan policy.
  - 分支数 1，函数体节点数 39；return: True, not rel_path.suffix and await asyncio.to_thread(_has_shebang, path)
  - 调用: _is_code_file_by_name, to_thread

#### `ƒ` `_move_staged_skill_into_reserved_target(staging_target: Path, target: Path) -> None`  L216
  - 分支数 3，函数体节点数 106；raise: SkillAlreadyExistsError(f"Skill '{target.name}' already exists")
  - 调用: mkdir, iterdir, move, str, make_skill_tree_sandbox_readable, SkillAlreadyExistsError, exists, rmtree
  - 文件IO: mkdir (L220), iterdir (L222), exists (L229)

#### `ƒ` `_findings_for_file(findings: list[StaticFinding], rel_path: str) -> list[StaticFinding]`  L233
  - 分支数 0，函数体节点数 39；return: [finding for finding in findings if finding.get('file') in {rel_path, None}]
  - 调用: get

#### `⏵ƒ` `async _scan_skill_file_or_raise(skill_dir: Path, path: Path, skill_name: str, *, executable: bool, static_findings: list[StaticFinding] | None) -> None`  L237
  - 分支数 6，函数体节点数 234；raise: SkillSecurityScanError(f"Security scan failed for skill '{skill_name}': {location} must be valid UTF-8"), SkillSecurityScanError(f'Security scan failed for {location}: {e}'), SkillSecurityScanError(f"Security scan blocked skill '{skill_name}': {reason}"), SkillSecurityScanError(f'Security scan blocked {location}: {reason}'), SkillSecurityScanError(f'Security scan rejected executable {location}: {reason}'), SkillSecurityScanError(f'Security scan failed for {location}: invalid scanner decision {decision!r}')
  - 调用: as_posix, relative_to, to_thread, SkillSecurityScanError, scan_skill_content, getattr, str
  - 反射: getattr (L250), getattr (L251)

#### `ƒ` `scan_archive_preflight_or_raise(archive_path: Path, *, app_config) -> None`  L262
  - 分支数 2，函数体节点数 70；raise: SkillSecurityScanError(f'Static security scan blocked unsafe skill archive: {format_static_archive_findings(critical)}', findings=critical, skill_name=None)；return: None
  - 调用: skill_scan_enabled, scan_archive_preflight, SkillSecurityScanError, format_static_archive_findings

#### `ƒ` `format_static_archive_findings(findings: list[StaticFinding]) -> str`  L275
  - 分支数 0，函数体节点数 54；return: '; '.join((f"{finding['rule_id']} ({finding['severity']}) at {finding.get('file') or '<archive>'}: {finding['message']}" for finding in findings))
  - 调用: join, get

#### `⏵ƒ` `async _scan_static_skill_archive_or_raise(skill_dir: Path, skill_name: str, *, app_config) -> list[StaticFinding]`  L279
  - 分支数 1，函数体节点数 79；raise: SkillSecurityScanError(str(e), findings=e.findings, skill_name=e.skill_name), SkillSecurityScanError(f"Static security scan failed for skill '{skill_name}': {e}", skill_name=skill_name)；return: await asyncio.to_thread(enforce_static_scan, skill_dir, skill_name=skill_name, app_config=app_config)
  - 调用: to_thread, SkillSecurityScanError, str

#### `ƒ` `_collect_scannable_files(skill_dir: Path) -> list[Path]`  L288
  - _文档首行_（仅供参考）: Enumerate archive files for scanning (blocking; run off the event loop).
  - 分支数 0，函数体节点数 34；return: [candidate for candidate in sorted(skill_dir.rglob('*')) if candidate.is_file()]
  - 调用: sorted, rglob, is_file
  - 文件IO: rglob (L290)

#### `⏵ƒ` `async _scan_skill_archive_contents_or_raise(skill_dir: Path, skill_name: str, *, app_config) -> list[StaticFinding]`  L293
  - _文档首行_（仅供参考）: Run the skill security scanner against all installable text and script files.
  - 分支数 5，函数体节点数 189；raise: SkillSecurityScanError(f"Security scan failed for skill '{skill_name}': nested SKILL.md is not allowed at {skill_name}/{rel_path.as_posix()}")；return: static_findings
  - 调用: _scan_static_skill_archive_or_raise, _scan_skill_file_or_raise, _findings_for_file, to_thread, relative_to, Path, SkillSecurityScanError, as_posix, _is_code_file, _should_scan_support_file

#### `ƒ` `_run_async_install(coro)`  L326
  - 分支数 3，函数体节点数 68；return: executor.submit(asyncio.run, coro).result(), asyncio.run(coro)
  - 调用: get_running_loop, is_running, ThreadPoolExecutor, result, submit, run
  - 子进程: run (L335)

## 类
### 类 `SkillAlreadyExistsError`  L48
- 继承: ValueError
- _文档首行_: Raised when a skill with the same name is already installed.

### 类 `SkillSecurityScanError`  L52
- 继承: ValueError
- _文档首行_: Raised when a skill archive fails security scanning.
- 类/实例变量:
  - `findings` = <annotated>
  - `skill_name` = <annotated>
- 方法:
  #### `m` `__init__(self, message: str, *, findings: list[StaticFinding] | None, skill_name: str | None) -> None`  L58
    - 分支数 0，函数体节点数 61
    - 调用: __init__, super, dict

## 文件内调用关系
- `resolve_skill_dir_from_archive` -> should_ignore_archive_entry
- `safe_extract_skill_archive` -> is_unsafe_zip_member, is_symlink_member, is_executable_binary_prefix
- `_should_scan_support_file` -> _is_script_support_file
- `_is_code_file_by_name` -> _is_script_support_file
- `_is_code_file` -> _is_code_file_by_name
- `scan_archive_preflight_or_raise` -> format_static_archive_findings
- `_scan_skill_archive_contents_or_raise` -> _scan_static_skill_archive_or_raise, _scan_skill_file_or_raise, _findings_for_file, _is_code_file, _should_scan_support_file
- `SkillSecurityScanError.__init__` -> __init__

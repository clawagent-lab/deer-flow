# `backend/packages/harness/deerflow/skills/skillscan/orchestrator.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/skills/skillscan/orchestrator.py`  ·  行数: 690

**模块文档首行**（仅供参考）: Native deterministic scanning for DeerFlow skills.

## 模块概览
- 函数 47 个，类 0 个，模块级常量 16 个

## 依赖（import）
- 模块: ast, io, logging, posixpath, re, stat, zipfile
- `__future__` -> annotations
- `collections.abc` -> Iterable
- `pathlib` -> Path, PurePosixPath, PureWindowsPath
- `typing` -> Any
- `deerflow.skills.package_paths` -> is_eval_fixture_skill_md
- `deerflow.skills.skillscan.models` -> FindingSeverity, RuleSpec, ScanResult, SecurityFinding, StaticScanBlockedError, StaticScannerError

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `MAX_TOTAL_ARCHIVE_BYTES` = 512 * 1024 * 1024
- `MAX_FILE_BYTES` = 64 * 1024 * 1024
- `_BLOCK_SEVERITY` = 'CRITICAL'
- `_NESTED_ZIP_PEEK_MEMBER_LIMIT` = 256
- `_MAX_ARCHIVE_MEMBERS` = 4096
- `_SPECS` = [RuleSpec('package-path-traversal', 'CRITICAL', 'Archive ...
- `RULES` = {spec.rule_id: spec for spec in _SPECS}
- `_ARCHIVE_SUFFIXES` = ('.zip', '.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2', ...
- `_HIDDEN_SENSITIVE_FILES` = {'.env', '.npmrc', '.pypirc', '.netrc', 'credentials', 'c...
- `_PLACEHOLDER_VALUES` = {'', 'x', 'xx', 'xxx', 'xxxx', 'changeme', 'change-me', '...
- `_SENSITIVE_PATH_RE` = re.compile('(~/.ssh|/etc/passwd|/etc/shadow|/var/run/dock...
- `_EXTERNAL_HTTP_RE` = re.compile('http://([A-Za-z0-9.-]+)(?::\\d+)?(?:/|\\b)')
- `_URL_RE` = re.compile('https?://[^\\s)\'\\"<>]+')
- `_LOCAL_HTTP_HOSTS` = {'localhost', '127.0.0.1', '0.0.0.0', '::1'}
- `_DESTRUCTIVE_RM_RE` = '\\brm\\s+(?:-\\S+\\s+|--no-preserve-root\\s+)*-\\S*[rR]\...

## 函数
#### `ƒ` `skill_scan_enabled(app_config: Any | None) -> bool`  L121
  - 分支数 3，函数体节点数 67；return: bool(skill_scan_config.enabled), True
  - 调用: get_app_config, getattr, hasattr, bool
  - 反射: getattr (L129), hasattr (L130)

#### `ƒ` `format_static_findings(findings: list[SecurityFinding]) -> str`  L135
  - 分支数 2，函数体节点数 100；return: '; '.join(parts)
  - 调用: append, join

#### `ƒ` `enforce_static_scan(skill_dir: Path, *, skill_name: str | None, app_config: Any | None) -> list[SecurityFinding]`  L145
  - 分支数 4，函数体节点数 193；raise: StaticScanBlockedError(blocked, skill_name=skill_name, message=f"Static security scan blocked skill '{skill_name}': {format_static_findings(blocked)}" if skill_name else f'Static security scan blocked skill content: {format_static_findings(blocked)}')；return: [], [dict(finding) for finding in result['findings']]
  - 调用: skill_scan_enabled, scan_skill_dir, Path, StaticScanBlockedError, format_static_findings, warning, join, dict

#### `ƒ` `scan_archive_preflight(archive_path: Path) -> ScanResult`  L170
  - 分支数 14，函数体节点数 386；raise: StaticScannerError(f'failed to read skill archive: {e}')；return: _scan_result([finding], scanner_errors), _scan_result(_dedupe(findings), scanner_errors)
  - 调用: ZipFile, infolist, len, _finding, _scan_result, _normalize_archive_name, extend, _scan_archive_member_metadata, is_dir, max, append, _is_hidden_sensitive_path, Path, PurePosixPath, _is_symlink_member, open, read, _is_executable_binary, _binary_magic_evidence, _is_nested_archive_name（+5）
  - 文件IO: open (L197), read (L198)

#### `ƒ` `scan_skill_dir(skill_dir: Path) -> ScanResult`  L214
  - 分支数 5，函数体节点数 202；raise: StaticScannerError(f'skill_dir is not a directory: {root}')；return: _scan_result(_dedupe(findings), scanner_errors)
  - 调用: Path, is_dir, StaticScannerError, sorted, rglob, is_file, _relative_file, read_bytes, append, extend, _scan_file_package_properties, stat, _decode_text_for_analysis, _scan_text_file, warning, _scan_result, _dedupe
  - 文件IO: rglob (L221), read_bytes (L224), stat (L229)

#### `ƒ` `_scan_archive_member_metadata(info: zipfile.ZipInfo, normalized: str) -> list[SecurityFinding]`  L243
  - 分支数 4，函数体节点数 165；return: findings
  - 调用: _archive_member_is_absolute, append, _finding, _archive_member_traverses, _is_symlink_member, PurePosixPath, len, is_eval_fixture_skill_md

#### `ƒ` `_scan_file_package_properties(rel_path: str, file_bytes: bytes, file_size: int) -> list[SecurityFinding]`  L257
  - 分支数 6，函数体节点数 224；return: findings
  - 调用: PurePosixPath, len, is_eval_fixture_skill_md, append, _finding, _is_hidden_sensitive_path, _is_nested_archive_name, _looks_like_archive, _nested_archive_finding, _is_executable_binary, _binary_magic_evidence

#### `ƒ` `_scan_text_file(rel_path: str, text: str) -> list[SecurityFinding]`  L275
  - 分支数 3，函数体节点数 120；return: findings
  - 调用: extend, _scan_secrets, PurePosixPath, _scan_declaration, _is_python_path, _scan_python, _is_shell_path, _scan_shell, _scan_network_and_resource

#### `ƒ` `_scan_secrets(rel_path: str, text: str) -> list[SecurityFinding]`  L288
  - 分支数 5，函数体节点数 173；return: findings
  - 调用: search, append, _finding_from_match, _looks_like_placeholder, group, compile, finditer, strip
  - 危险执行: compile (L306)

#### `ƒ` `_scan_declaration(rel_path: str, text: str) -> list[SecurityFinding]`  L315
  - 分支数 6，函数体节点数 188；return: findings
  - 调用: compile, search, append, _finding_from_match, finditer, startswith, group, _http_host
  - 危险执行: compile (L317), compile (L321)

#### `ƒ` `_scan_python(rel_path: str, text: str) -> list[SecurityFinding]`  L337
  - 分支数 21，函数体节点数 627；return: findings
  - 调用: parse, _collect_python_aliases, set, walk, isinstance, search, _is_outbound_url, _python_name, _python_call_name, _compile_mode_is_exec, append, _finding_for_node, startswith, _call_has_shell_true, _yaml_load_uses_safe_loader, _call_is_network_sink, add

#### `ƒ` `_scan_shell(rel_path: str, text: str) -> list[SecurityFinding]`  L407
  - 分支数 6，函数体节点数 206；return: findings
  - 调用: search, append, _finding_from_match, _finding_for_text

#### `ƒ` `_scan_network_and_resource(rel_path: str, text: str) -> list[SecurityFinding]`  L426
  - 分支数 4，函数体节点数 165；return: findings
  - 调用: search, append, _finding_from_match, finditer, group, startswith, match

#### `ƒ` `_finding(rule_id: str, *, file: str | None, evidence: str | None, line: int | None, severity: FindingSeverity | None) -> SecurityFinding`  L442
  - 分支数 1，函数体节点数 97；return: {'rule_id': rule_id, 'severity': severity or spec.severity, 'file': file, 'line': line, 'message': spec.message, 'remediation': spec.remediation, 'evidence': evidence}
  - 调用: startswith, _redact_secret_evidence

#### `ƒ` `_finding_from_match(rule_id: str, rel_path: str, text: str, match: re.Match[str]) -> SecurityFinding`  L457
  - 分支数 0，函数体节点数 49；return: _finding(rule_id, file=rel_path, line=_line_number(text, match.start()), evidence=match.group(0))
  - 调用: _finding, _line_number, start, group

#### `ƒ` `_finding_for_text(rule_id: str, rel_path: str, text: str, evidence: str) -> SecurityFinding`  L461
  - 分支数 0，函数体节点数 53；return: _finding(rule_id, file=rel_path, line=_line_number(text, index if index >= 0 else 0), evidence=evidence)
  - 调用: find, _finding, _line_number

#### `ƒ` `_finding_for_node(rule_id: str, rel_path: str, node: ast.AST | None, evidence: str) -> SecurityFinding`  L466
  - 分支数 0，函数体节点数 41；return: _finding(rule_id, file=rel_path, line=getattr(node, 'lineno', 1), evidence=evidence)
  - 调用: _finding, getattr
  - 反射: getattr (L467)

#### `ƒ` `_nested_archive_finding(rel_path: str, prefix: bytes, read_data, scanner_errors: list[str]) -> SecurityFinding`  L470
  - 分支数 3，函数体节点数 99；return: _finding('package-nested-archive', file=rel_path, evidence=f'{name}: contains an executable binary member', severity='CRITICAL'), _finding('package-nested-archive', file=rel_path, evidence=name)
  - 调用: PurePosixPath, startswith, read_data, append, _nested_zip_contains_executable, _finding

#### `ƒ` `_nested_zip_contains_executable(data: bytes) -> bool`  L483
  - 分支数 7，函数体节点数 85；return: True, False
  - 调用: ZipFile, BytesIO, infolist, is_dir, open, _is_executable_binary, read
  - 文件IO: open (L490), read (L491)

#### `ƒ` `_read_archive_member(zf: zipfile.ZipFile, info: zipfile.ZipInfo) -> bytes | None`  L500
  - 分支数 2，函数体节点数 50；return: None, member.read(MAX_FILE_BYTES + 1)
  - 调用: open, read
  - 文件IO: open (L503), read (L504)

#### `ƒ` `_redact_secret_evidence(value: str) -> str`  L507
  - 分支数 0，函数体节点数 9；return: '[redacted]'

#### `ƒ` `_scan_result(findings: list[SecurityFinding], scanner_errors: list[str]) -> ScanResult`  L514
  - 分支数 0，函数体节点数 50；return: {'findings': findings, 'blocked': blocked, 'scanner_errors': scanner_errors}
  - 调用: any

#### `ƒ` `_dedupe(findings: Iterable[SecurityFinding]) -> list[SecurityFinding]`  L519
  - 分支数 2，函数体节点数 106；return: deduped
  - 调用: set, add, append

#### `ƒ` `_line_number(text: str, index: int) -> int`  L531
  - 分支数 0，函数体节点数 29；return: text[:max(index, 0)].count('\n') + 1
  - 调用: count, max

#### `ƒ` `_normalize_archive_name(name: str) -> str`  L535
  - 分支数 0，函数体节点数 24；return: posixpath.normpath(name.replace('\\', '/')).removeprefix('./')
  - 调用: removeprefix, normpath, replace
  - 文件IO: replace (L536)

#### `ƒ` `_archive_member_is_absolute(name: str) -> bool`  L539
  - 分支数 0，函数体节点数 42；return: normalized.startswith('/') or PurePosixPath(normalized).is_absolute() or PureWindowsPath(name).is_absolute()
  - 调用: replace, startswith, is_absolute, PurePosixPath, PureWindowsPath
  - 文件IO: replace (L540)

#### `ƒ` `_archive_member_traverses(name: str) -> bool`  L544
  - 分支数 0，函数体节点数 23；return: '..' in PurePosixPath(name.replace('\\', '/')).parts
  - 调用: PurePosixPath, replace
  - 文件IO: replace (L545)

#### `ƒ` `_is_symlink_member(info: zipfile.ZipInfo) -> bool`  L548
  - 分支数 0，函数体节点数 22；return: stat.S_ISLNK(info.external_attr >> 16)
  - 调用: S_ISLNK

#### `ƒ` `_relative_file(path: Path, root: Path) -> str`  L552
  - 分支数 0，函数体节点数 27；return: path.resolve().relative_to(root.resolve()).as_posix()
  - 调用: as_posix, relative_to, resolve

#### `ƒ` `_is_hidden_sensitive_path(rel_path: str) -> bool`  L556
  - 分支数 2，函数体节点数 111；return: True, parts[-1] in _HIDDEN_SENSITIVE_FILES and (parts[-1].startswith('.') or any((token in parts[-1].lower() for token in ('credential', 'npmrc', 'pypirc', 'netrc'))))
  - 调用: PurePosixPath, startswith, any, lower

#### `ƒ` `_is_nested_archive_name(rel_path: str) -> bool`  L565
  - 分支数 0，函数体节点数 32；return: any((lower.endswith(suffix) for suffix in _ARCHIVE_SUFFIXES))
  - 调用: lower, any, endswith

#### `ƒ` `_looks_like_archive(file_bytes: bytes) -> bool`  L570
  - 分支数 0，函数体节点数 28；return: file_bytes.startswith(b'PK\x03\x04') or file_bytes.startswith(b'\x1f\x8b') or file_bytes.startswith(b"7z\xbc\xaf'\x1c")
  - 调用: startswith

#### `ƒ` `_is_executable_binary(prefix: bytes) -> bool`  L574
  - 分支数 0，函数体节点数 32；return: prefix.startswith(b'\x7fELF') or prefix.startswith(b'MZ') or prefix.startswith((b'\xfe\xed\xfa', b'\xcf\xfa\xed\xfe', b'\xca\xfe\xba\xbe'))
  - 调用: startswith

#### `ƒ` `_binary_magic_evidence(prefix: bytes) -> str`  L578
  - 分支数 2，函数体节点数 27；return: 'ELF', 'PE', 'Mach-O'
  - 调用: startswith

#### `ƒ` `_decode_text_for_analysis(file_bytes: bytes) -> str | None`  L586
  - 分支数 2，函数体节点数 35；return: None, file_bytes.decode('utf-8')
  - 调用: decode

#### `ƒ` `_is_python_path(rel_path: str, text: str) -> bool`  L597
  - 分支数 0，函数体节点数 48；return: PurePosixPath(rel_path).suffix.lower() == '.py' or (text.startswith('#!') and 'python' in text.splitlines()[0].lower())
  - 调用: lower, PurePosixPath, startswith, splitlines

#### `ƒ` `_is_shell_path(rel_path: str, text: str) -> bool`  L601
  - 分支数 0，函数体节点数 68；return: suffix in {'.sh', '.bash'} or (text.startswith('#!') and any((shell in text.splitlines()[0].lower() for shell in ('sh', 'bash', 'zsh'))))
  - 调用: lower, PurePosixPath, startswith, any, splitlines

#### `ƒ` `_looks_like_placeholder(value: str) -> bool`  L606
  - 分支数 1，函数体节点数 56；return: True, normalized.startswith('<') or normalized.startswith('${') or 'your' in normalized or ('example' in normalized)
  - 调用: lower, strip, startswith

#### `ƒ` `_http_host(url: str) -> str | None`  L613
  - 分支数 0，函数体节点数 32；return: match.group(1) if match else None
  - 调用: match, group

#### `ƒ` `_is_outbound_url(value: str) -> bool`  L618
  - 分支数 0，函数体节点数 34；return: bool(value.startswith(('http://', 'https://')) and (_http_host(value) or '') not in _LOCAL_HTTP_HOSTS)
  - 调用: bool, startswith, _http_host

#### `ƒ` `_collect_python_aliases(tree: ast.AST) -> dict[str, str]`  L622
  - 分支数 5，函数体节点数 130；return: aliases
  - 调用: walk, isinstance

#### `ƒ` `_python_name(node: ast.AST, aliases: dict[str, str]) -> str`  L634
  - 分支数 2，函数体节点数 86；return: aliases.get(node.id, node.id), f'{base}.{node.attr}' if base else node.attr, ''
  - 调用: isinstance, get, _python_name

#### `ƒ` `_python_call_name(node: ast.Call, aliases: dict[str, str]) -> str`  L643
  - 分支数 0，函数体节点数 30；return: _python_name(node.func, aliases)
  - 调用: _python_name

#### `ƒ` `_compile_mode_is_exec(node: ast.Call) -> bool`  L647
  - 分支数 1，函数体节点数 90；return: node.args[2].value == 'exec', any((keyword.arg == 'mode' and isinstance(keyword.value, ast.Constant) and (keyword.value.value == 'exec') for keyword in node.keywords))
  - 调用: len, isinstance, any

#### `ƒ` `_call_has_shell_true(node: ast.Call) -> bool`  L653
  - 分支数 0，函数体节点数 50；return: any((keyword.arg == 'shell' and isinstance(keyword.value, ast.Constant) and (keyword.value.value is True) for keyword in node.keywords))
  - 调用: any, isinstance

#### `ƒ` `_call_is_network_sink(call_name: str) -> bool`  L657
  - 分支数 0，函数体节点数 34；return: call_name in {'requests.get', 'requests.post', 'requests.put', 'requests.patch', 'requests.delete', 'requests.head', 'requests.options', 'requests.request', 'httpx.get', 'httpx.post', 'httpx.put', 'httpx.patch', 'httpx.delete', 'httpx.head', 'httpx.options', 'httpx.request', 'httpx.stream', 'urllib.request.urlopen', 'urllib.request.urlretrieve', 'socket.socket', 'socket.create_connection'}

#### `ƒ` `_yaml_load_uses_safe_loader(node: ast.Call) -> bool`  L683
  - 分支数 3，函数体节点数 47；return: True, False
  - 调用: _python_name

## 文件内调用关系
- `enforce_static_scan` -> skill_scan_enabled, scan_skill_dir, format_static_findings
- `scan_archive_preflight` -> _finding, _scan_result, _normalize_archive_name, _scan_archive_member_metadata, _is_hidden_sensitive_path, _is_symlink_member, _is_executable_binary, _binary_magic_evidence, _is_nested_archive_name, _looks_like_archive, _nested_archive_finding, _read_archive_member, _dedupe
- `scan_skill_dir` -> _relative_file, _scan_file_package_properties, _decode_text_for_analysis, _scan_text_file, _scan_result, _dedupe
- `_scan_archive_member_metadata` -> _archive_member_is_absolute, _finding, _archive_member_traverses, _is_symlink_member
- `_scan_file_package_properties` -> _finding, _is_hidden_sensitive_path, _is_nested_archive_name, _looks_like_archive, _nested_archive_finding, _is_executable_binary, _binary_magic_evidence
- `_scan_text_file` -> _scan_secrets, _scan_declaration, _is_python_path, _scan_python, _is_shell_path, _scan_shell, _scan_network_and_resource
- `_scan_secrets` -> _finding_from_match, _looks_like_placeholder
- `_scan_declaration` -> _finding_from_match, _http_host
- `_scan_python` -> _collect_python_aliases, _is_outbound_url, _python_name, _python_call_name, _compile_mode_is_exec, _finding_for_node, _call_has_shell_true, _yaml_load_uses_safe_loader, _call_is_network_sink
- `_scan_shell` -> _finding_from_match, _finding_for_text
- `_scan_network_and_resource` -> _finding_from_match
- `_finding` -> _redact_secret_evidence
- `_finding_from_match` -> _finding, _line_number
- `_finding_for_text` -> _finding, _line_number
- `_finding_for_node` -> _finding
- `_nested_archive_finding` -> _nested_zip_contains_executable, _finding
- `_nested_zip_contains_executable` -> _is_executable_binary
- `_is_outbound_url` -> _http_host
- `_python_name` -> _python_name
- `_python_call_name` -> _python_name
- `_yaml_load_uses_safe_loader` -> _python_name

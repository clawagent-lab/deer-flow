# `skills/public/podcast-generation/scripts/generate.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/podcast-generation/scripts/generate.py`  ·  行数: 374

## 模块概览
- 函数 13 个，类 2 个，模块级常量 6 个

## 依赖（import）
- 模块: argparse, base64, json, logging, os, random, time, uuid, requests
- `concurrent.futures` -> ThreadPoolExecutor, as_completed
- `typing` -> Literal, Optional

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `MINIMAX_DEFAULT_HOST` = 'https://api.minimaxi.com'
- `MINIMAX_RETRYABLE_CODES` = {1000, 1001, 1002, 1039}
- `DEFAULT_TTS_MAX_RETRIES` = 4
- `DEFAULT_MAX_WORKERS` = 4
- `DEFAULT_MINIMAX_MAX_WORKERS` = 1

## 函数
#### `ƒ` `_resolve_provider(override_env: str, existing_provider: str, has_existing_creds: bool) -> str`  L47
  - 分支数 3，函数体节点数 64；raise: ValueError(f'No credentials found. Set VOLCENGINE_TTS_APPID + VOLCENGINE_TTS_ACCESS_TOKEN for {existing_provider}, or MINIMAX_API_KEY for minimax (optionally force with {override_env}).')；return: override.strip().lower(), existing_provider, 'minimax'
  - 调用: getenv, lower, strip, ValueError
  - 环境变量: getenv (L48), getenv (L53)

#### `ƒ` `_resolve_tts_provider() -> str`  L62
  - 分支数 1，函数体节点数 56；raise: ValueError(f"Unknown podcast provider: {provider!r} (use 'volcengine' or 'minimax')")；return: provider
  - 调用: bool, getenv, _resolve_provider, ValueError
  - 环境变量: getenv (L64), getenv (L64)

#### `ƒ` `_default_max_retries() -> int`  L74
  - 分支数 1，函数体节点数 26；return: int(os.getenv('MINIMAX_TTS_MAX_RETRIES', str(DEFAULT_TTS_MAX_RETRIES))), DEFAULT_TTS_MAX_RETRIES
  - 调用: int, getenv, str
  - 环境变量: getenv (L76)

#### `ƒ` `_default_max_workers(provider: str) -> int`  L81
  - _文档首行_（仅供参考）: Each provider owns its own concurrency: MiniMax stays low to avoid rate
  - 分支数 1，函数体节点数 21；return: DEFAULT_MINIMAX_MAX_WORKERS, DEFAULT_MAX_WORKERS

#### `ƒ` `_parse_retry_after(response) -> Optional[float]`  L90
  - _文档首行_（仅供参考）: Return the server-provided Retry-After (seconds), if any.
  - 分支数 1，函数体节点数 53；return: float(value) if value else None, None
  - 调用: getattr, get, float
  - 反射: getattr (L92)

#### `ƒ` `_backoff_sleep(attempt: int, retry_after: Optional[float]) -> None`  L100
  - _文档首行_（仅供参考）: Sleep with exponential backoff + jitter, honoring Retry-After when present.
  - 分支数 0，函数体节点数 49
  - 调用: min, sleep, uniform

#### `ƒ` `text_to_speech_volcengine(text: str, voice_type: str, max_retries: Optional[int]) -> Optional[bytes]`  L110
  - _文档首行_（仅供参考）: Convert text to speech using Volcengine TTS (returns base64-decoded mp3 bytes).
  - 分支数 9，函数体节点数 349；return: None, base64.b64decode(audio_data)
  - 调用: getenv, _default_max_retries, str, uuid4, range, post, error, _backoff_sleep, warning, _parse_retry_after, json, get, b64decode
  - 网络调用: post (L133)
  - 环境变量: getenv (L117), getenv (L118), getenv (L119)

#### `ƒ` `text_to_speech_minimax(text: str, voice_id: str, max_retries: Optional[int]) -> Optional[bytes]`  L163
  - _文档首行_（仅供参考）: Convert text to speech using MiniMax t2a_v2 (returns hex-decoded mp3 bytes).
  - 分支数 11，函数体节点数 410；return: None, bytes.fromhex(audio_hex)
  - 调用: getenv, rstrip, _default_max_retries, range, post, error, _backoff_sleep, warning, _parse_retry_after, json, get, fromhex
  - 网络调用: post (L185)
  - 环境变量: getenv (L172), getenv (L173), getenv (L177)

#### `ƒ` `_process_line(args: tuple[int, ScriptLine, int, str]) -> tuple[int, Optional[bytes]]`  L231
  - _文档首行_（仅供参考）: Process a single script line for TTS. Returns (index, audio_bytes).
  - 分支数 4，函数体节点数 174；return: (i, audio)
  - 调用: info, getenv, text_to_speech_minimax, text_to_speech_volcengine, warning
  - 环境变量: getenv (L237), getenv (L239)

#### `ƒ` `tts_node(script: Script) -> list[bytes]`  L252
  - _文档首行_（仅供参考）: Convert script lines to audio chunks using TTS with multi-threading.
  - 分支数 7，函数体节点数 322；raise: ValueError('Script contains no lines to process'), ValueError('Volcengine TTS selected but VOLCENGINE_TTS_APPID / VOLCENGINE_TTS_ACCESS_TOKEN are not set'), ValueError('MiniMax TTS selected but MINIMAX_API_KEY is not set'), ValueError(f'TTS failed for {len(failed_indices)}/{total} lines after retries: line numbers {sorted((i + 1 for i in failed_indices))}. This is usually transient API rate limiting — wait a moment and retry.')；return: audio_chunks
  - 调用: len, ValueError, _resolve_tts_provider, _default_max_workers, getenv, info, enumerate, ThreadPoolExecutor, submit, as_completed, result, append, sorted, range
  - 环境变量: getenv (L267), getenv (L267), getenv (L273)

#### `ƒ` `mix_audio(audio_chunks: list[bytes]) -> bytes`  L300
  - _文档首行_（仅供参考）: Combine audio chunks into a single audio file.
  - 分支数 2，函数体节点数 64；raise: ValueError('No audio chunks to mix - TTS generation may have failed'), ValueError('Mixed audio is empty - TTS generation may have failed')；return: output
  - 调用: ValueError, join, len, info

#### `ƒ` `generate_markdown(script: Script, title: str) -> str`  L311
  - 分支数 1，函数体节点数 72；return: '\n'.join(lines)
  - 调用: append, join

#### `ƒ` `generate_podcast(script_file: str, output_file: str, transcript_file: Optional[str]) -> str`  L320
  - 分支数 9，函数体节点数 259；raise: ValueError(f"Invalid script format: missing 'lines' key. Got keys: {list(script_json.keys())}"), Exception('Failed to generate any audio')；return: result
  - 调用: open, load, ValueError, list, keys, from_dict, info, len, get, generate_markdown, dirname, makedirs, write, tts_node, Exception, mix_audio
  - 文件IO: open (L322), open (L337), write (L338), open (L349), write (L350)

## 类
### 类 `ScriptLine`  L25
- 方法:
  #### `m` `__init__(self, speaker: Literal['male', 'female'], paragraph: str)`  L26
    - 分支数 0，函数体节点数 31

### 类 `Script`  L31
- 方法:
  #### `cls` `from_dict(cls, data: dict) -> 'Script'`    @classmethod  L37
    - 分支数 1，函数体节点数 64；return: script
    - 调用: cls, get, append, ScriptLine
  #### `m` `__init__(self, locale: Literal['en', 'zh'], lines: Optional[list[ScriptLine]])`  L32
    - 分支数 0，函数体节点数 43

## 文件内调用关系
- `_resolve_tts_provider` -> _resolve_provider
- `text_to_speech_volcengine` -> _default_max_retries, _backoff_sleep, _parse_retry_after
- `text_to_speech_minimax` -> _default_max_retries, _backoff_sleep, _parse_retry_after
- `_process_line` -> text_to_speech_minimax, text_to_speech_volcengine
- `tts_node` -> _resolve_tts_provider, _default_max_workers
- `generate_podcast` -> from_dict, generate_markdown, tts_node, mix_audio

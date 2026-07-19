# `backend/packages/harness/deerflow/tools/builtins/view_image_tool.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/tools/builtins/view_image_tool.py`  ·  行数: 174

## 模块概览
- 函数 4 个，类 0 个，模块级常量 4 个

## 依赖（import）
- 模块: mimetypes
- `pathlib` -> Path
- `typing` -> Annotated
- `langchain.tools` -> InjectedToolCallId, tool
- `langchain_core.messages` -> ToolMessage
- `langgraph.types` -> Command
- `deerflow.agents.thread_state` -> ThreadDataState
- `deerflow.config.paths` -> VIRTUAL_PATH_PREFIX
- `deerflow.tools.types` -> Runtime

## 模块级常量
- `_ALLOWED_IMAGE_VIRTUAL_ROOTS` = (f'{VIRTUAL_PATH_PREFIX}/workspace', f'{VIRTUAL_PATH_PREF...
- `_ALLOWED_IMAGE_VIRTUAL_ROOTS_TEXT` = ', '.join(_ALLOWED_IMAGE_VIRTUAL_ROOTS)
- `_MAX_IMAGE_BYTES` = 20 * 1024 * 1024
- `_EXTENSION_TO_MIME` = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'im...

## 函数
#### `ƒ` `_is_allowed_image_virtual_path(image_path: str) -> bool`  L28
  - 分支数 0，函数体节点数 35；return: any((image_path == root or image_path.startswith(f'{root}/') for root in _ALLOWED_IMAGE_VIRTUAL_ROOTS))
  - 调用: any, startswith

#### `ƒ` `_detect_image_mime(image_data: bytes) -> str | None`  L32
  - 分支数 3，函数体节点数 59；return: 'image/jpeg', 'image/png', 'image/webp', None
  - 调用: startswith, len

#### `ƒ` `_sanitize_image_error(error: Exception, thread_data: ThreadDataState | None) -> str`  L42
  - 分支数 0，函数体节点数 34；return: mask_local_paths_in_output(f'{type(error).__name__}: {error}', thread_data)
  - 调用: mask_local_paths_in_output, type

#### `ƒ` `view_image_tool(runtime: Runtime, image_path: str, tool_call_id: Annotated[str, InjectedToolCallId]) -> Command`    @tool(...)  L49
  - _文档首行_（仅供参考）: Read an image file.
  - 分支数 13，函数体节点数 511；return: Command(update={'messages': [ToolMessage(f'Error: Only image paths under {_ALLOWED_IMAGE_VIRTUAL_ROOTS_TEXT} are allowed', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(f'Error: {str(e)}', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(f'Error: Image file not found: {image_path}', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(f'Error: Path is not a file: {image_path}', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(f"Error: Unsupported image format: {path.suffix}. Supported formats: {', '.join(_EXTENSION_TO_MIME)}", tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(f'Error reading image metadata: {_sanitize_image_error(e, thread_data)}', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(f'Error: Image file is too large: {image_size} bytes. Maximum supported size is {_MAX_IMAGE_BYTES} bytes', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(f'Error reading image file: {_sanitize_image_error(e, thread_data)}', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage('Error: Image file changed during read', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage('Error: File contents do not match a supported image format', tool_call_id=tool_call_id)]}), Command(update={'messages': [ToolMessage(f'Error: Image contents are {detected_mime_type}, but file extension indicates {expected_mime_type}', tool_call_id=tool_call_id)]}), Command(update={'viewed_images': new_viewed_images, 'messages': [ToolMessage('Successfully read image', tool_call_id=tool_call_id)]})
  - 调用: get_thread_data, _is_allowed_image_virtual_path, Command, ToolMessage, validate_local_tool_path, resolve_and_validate_user_data_path, str, Path, exists, is_file, get, lower, join, guess_type, stat, _sanitize_image_error, open, read, len, _detect_image_mime（+1）
  - 文件IO: exists (L100), stat (L124), open (L136), read (L137)

## 文件内调用关系
- `view_image_tool` -> _is_allowed_image_virtual_path, _sanitize_image_error, _detect_image_mime

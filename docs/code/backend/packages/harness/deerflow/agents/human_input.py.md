# `backend/packages/harness/deerflow/agents/human_input.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/agents/human_input.py`  ·  行数: 77

**模块文档首行**（仅供参考）: Structured human-input message metadata helpers.

## 模块概览
- 函数 2 个，类 2 个，模块级常量 2 个

## 依赖（import）
- `__future__` -> annotations
- `collections.abc` -> Mapping
- `typing` -> Literal, TypedDict

## 模块级常量
- `HUMAN_INPUT_RESPONSE_KEY` = 'human_input_response'
- `HumanInputResponse` = HumanInputTextResponse | HumanInputOptionResponse

## 函数
#### `ƒ` `_non_empty_string(value: object) -> str | None`  L33
  - 分支数 0，函数体节点数 29；return: value if isinstance(value, str) and value.strip() else None
  - 调用: isinstance, strip

#### `ƒ` `read_human_input_response(additional_kwargs: Mapping[str, object] | None) -> HumanInputResponse | None`  L37
  - _文档首行_（仅供参考）: Read a valid human-input response payload from message metadata.
  - 分支数 7，函数体节点数 211；return: None, {'version': 1, 'kind': 'human_input_response', 'source': source, 'request_id': request_id, 'response_kind': 'text', 'value': value}, {'version': 1, 'kind': 'human_input_response', 'source': source, 'request_id': request_id, 'response_kind': 'option', 'option_id': option_id, 'value': value}
  - 调用: get, isinstance, _non_empty_string

## 类
### 类 `HumanInputTextResponse`  L11
- 继承: TypedDict
- 类/实例变量:
  - `version` = <annotated>
  - `kind` = <annotated>
  - `source` = <annotated>
  - `request_id` = <annotated>
  - `response_kind` = <annotated>
  - `value` = <annotated>

### 类 `HumanInputOptionResponse`  L20
- 继承: TypedDict
- 类/实例变量:
  - `version` = <annotated>
  - `kind` = <annotated>
  - `source` = <annotated>
  - `request_id` = <annotated>
  - `response_kind` = <annotated>
  - `option_id` = <annotated>
  - `value` = <annotated>

## 文件内调用关系
- `read_human_input_response` -> _non_empty_string

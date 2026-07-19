# `backend/packages/harness/deerflow/reflection/resolvers.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/reflection/resolvers.py`  ·  行数: 96

## 模块概览
- 函数 3 个，类 0 个，模块级常量 1 个

## 依赖（import）
- `importlib` -> import_module

## 模块级常量
- `MODULE_TO_PACKAGE_HINTS` = {'langchain_google_genai': 'langchain-google-genai', 'lan...

## 函数
#### `ƒ` `_build_missing_dependency_hint(module_path: str, err: ImportError) -> str`  L11
  - _文档首行_（仅供参考）: Build an actionable hint when module import fails.
  - 分支数 1，函数体节点数 87；return: f"Missing dependency '{missing_module}'. Install it with `uv add {package_name}` (or `pip install {package_name}`), then restart DeerFlow."
  - 调用: split, getattr, get, replace
  - 文件IO: replace (L20)
  - 反射: getattr (L14)

#### `ƒ` `resolve_variable(variable_path: str, expected_type: type[T] | tuple[type, ...] | None) -> T`  L25
  - _文档首行_（仅供参考）: Resolve a variable from a path.
  - 分支数 6，函数体节点数 251；raise: ImportError(f"{variable_path} doesn't look like a variable path. Example: parent_package_name.sub_package_name.module_name:variable_name"), ImportError(f'Could not import module {module_path}. {hint}'), ImportError(f'Error importing module {module_path}: {err}'), ImportError(f'Module {module_path} does not define a {variable_name} attribute/class'), ValueError(f'{variable_path} is not an instance of {type_name}, got {type(variable).__name__}')；return: variable
  - 调用: rsplit, ImportError, import_module, split, getattr, isinstance, _build_missing_dependency_hint, join, ValueError, type
  - 反射: import_module (L49), getattr (L52), getattr (L60)

#### `ƒ` `resolve_class(class_path: str, base_class: type[T] | None) -> type[T]`  L73
  - _文档首行_（仅供参考）: Resolve a class from a module path and class name.
  - 分支数 2，函数体节点数 89；raise: ValueError(f'{class_path} is not a valid class'), ValueError(f'{class_path} is not a subclass of {base_class.__name__}')；return: model_class
  - 调用: resolve_variable, isinstance, ValueError, issubclass

## 文件内调用关系
- `resolve_variable` -> _build_missing_dependency_hint
- `resolve_class` -> resolve_variable

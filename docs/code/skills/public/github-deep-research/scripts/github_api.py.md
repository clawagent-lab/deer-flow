# `skills/public/github-deep-research/scripts/github_api.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `skills/public/github-deep-research/scripts/github_api.py`  ·  行数: 332

**模块文档首行**（仅供参考）: GitHub API client for deep research.

## 模块概览
- 函数 1 个，类 1 个，模块级常量 0 个

## 依赖（import）
- 模块: os, json, sys
- `typing` -> Any, Dict, List, Optional

## 函数
#### `ƒ` `main()`  L288
  - _文档首行_（仅供参考）: CLI interface for testing.
  - 分支数 4，函数体节点数 317
  - 调用: len, print, exit, getenv, GitHubAPI, get_repo_info, get_readme, format_tree, get_tree, get_languages, get_contributors, get_recent_commits, get_issues, get_pull_requests, get_releases, summarize_repo, commands[command], isinstance, dumps
  - 环境变量: getenv (L299)

## 类
### 类 `GitHubAPI`  L51
- _文档首行_: GitHub API client for repository analysis.
- 类/实例变量:
  - `BASE_URL` = 'https://api.github.com'
- 方法:
  #### `m` `__init__(self, token: Optional[str])`  L56
    - _文档首行_（仅供参考）: Initialize GitHub API client.
    - 分支数 1，函数体节点数 39
  #### `m` `_get(self, endpoint: str, params: Optional[Dict], accept: Optional[str]) -> Any`  L72
    - _文档首行_（仅供参考）: Make GET request to GitHub API.
    - 分支数 2，函数体节点数 103；return: resp.text, resp.json()
    - 调用: copy, get, raise_for_status, json
  - 网络调用: get (L81)
  #### `m` `get_repo_info(self, owner: str, repo: str) -> Dict`  L88
    - _文档首行_（仅供参考）: Get basic repository information.
    - 分支数 0，函数体节点数 28；return: self._get(f'/repos/{owner}/{repo}')
    - 调用: _get
  #### `m` `get_readme(self, owner: str, repo: str) -> str`  L92
    - _文档首行_（仅供参考）: Get repository README content as markdown.
    - 分支数 1，函数体节点数 42；return: self._get(f'/repos/{owner}/{repo}/readme', accept='application/vnd.github.raw'), f'[README not found: {e}]'
    - 调用: _get
  #### `m` `get_tree(self, owner: str, repo: str, branch: str, recursive: bool) -> Dict`  L101
    - _文档首行_（仅供参考）: Get repository directory tree.
    - 分支数 2，函数体节点数 81；raise: bare raise；return: self._get(f'/repos/{owner}/{repo}/git/trees/{branch}', params), self._get(f'/repos/{owner}/{repo}/git/trees/master', params)
    - 调用: _get
  #### `m` `get_file_content(self, owner: str, repo: str, path: str) -> str`  L114
    - _文档首行_（仅供参考）: Get content of a specific file.
    - 分支数 1，函数体节点数 48；return: self._get(f'/repos/{owner}/{repo}/contents/{path}', accept='application/vnd.github.raw'), f'[File not found: {e}]'
    - 调用: _get
  #### `m` `get_languages(self, owner: str, repo: str) -> Dict[str, int]`  L124
    - _文档首行_（仅供参考）: Get repository languages and their bytes.
    - 分支数 0，函数体节点数 37；return: self._get(f'/repos/{owner}/{repo}/languages')
    - 调用: _get
  #### `m` `get_contributors(self, owner: str, repo: str, limit: int) -> List[Dict]`  L128
    - _文档首行_（仅供参考）: Get repository contributors.
    - 分支数 0，函数体节点数 46；return: self._get(f'/repos/{owner}/{repo}/contributors', params={'per_page': min(limit, 100)})
    - 调用: _get, min
  #### `m` `get_recent_commits(self, owner: str, repo: str, limit: int, since: Optional[str]) -> List[Dict]`  L134
    - _文档首行_（仅供参考）: Get recent commits.
    - 分支数 1，函数体节点数 69；return: self._get(f'/repos/{owner}/{repo}/commits', params)
    - 调用: min, _get
  #### `m` `get_issues(self, owner: str, repo: str, state: str, limit: int, labels: Optional[str]) -> List[Dict]`  L151
    - _文档首行_（仅供参考）: Get repository issues.
    - 分支数 1，函数体节点数 76；return: self._get(f'/repos/{owner}/{repo}/issues', params)
    - 调用: min, _get
  #### `m` `get_pull_requests(self, owner: str, repo: str, state: str, limit: int) -> List[Dict]`  L171
    - _文档首行_（仅供参考）: Get repository pull requests.
    - 分支数 0，函数体节点数 53；return: self._get(f'/repos/{owner}/{repo}/pulls', params={'state': state, 'per_page': min(limit, 100)})
    - 调用: _get, min
  #### `m` `get_releases(self, owner: str, repo: str, limit: int) -> List[Dict]`  L180
    - _文档首行_（仅供参考）: Get repository releases.
    - 分支数 0，函数体节点数 46；return: self._get(f'/repos/{owner}/{repo}/releases', params={'per_page': min(limit, 100)})
    - 调用: _get, min
  #### `m` `get_tags(self, owner: str, repo: str, limit: int) -> List[Dict]`  L186
    - _文档首行_（仅供参考）: Get repository tags.
    - 分支数 0，函数体节点数 46；return: self._get(f'/repos/{owner}/{repo}/tags', params={'per_page': min(limit, 100)})
    - 调用: _get, min
  #### `m` `search_issues(self, owner: str, repo: str, query: str, limit: int) -> Dict`  L192
    - _文档首行_（仅供参考）: Search issues and PRs in repository.
    - 分支数 0，函数体节点数 55；return: self._get('/search/issues', params={'q': q, 'per_page': min(limit, 100)})
    - 调用: _get, min
  #### `m` `get_commit_activity(self, owner: str, repo: str) -> List[Dict]`  L197
    - _文档首行_（仅供参考）: Get weekly commit activity for the last year.
    - 分支数 0，函数体节点数 33；return: self._get(f'/repos/{owner}/{repo}/stats/commit_activity')
    - 调用: _get
  #### `m` `get_code_frequency(self, owner: str, repo: str) -> List[List[int]]`  L201
    - _文档首行_（仅供参考）: Get weekly additions/deletions.
    - 分支数 0，函数体节点数 37；return: self._get(f'/repos/{owner}/{repo}/stats/code_frequency')
    - 调用: _get
  #### `m` `format_tree(self, tree_data: Dict, max_depth: int) -> str`  L205
    - _文档首行_（仅供参考）: Format tree data as text directory structure.
    - 分支数 4，函数体节点数 128；return: '[Unable to parse tree]', '\n'.join(lines[:100])
    - 调用: count, split, append, join
  #### `m` `summarize_repo(self, owner: str, repo: str) -> Dict`  L230
    - _文档首行_（仅供参考）: Get comprehensive repository summary.
    - 分支数 4，函数体节点数 274；return: summary
    - 调用: get_repo_info, get, get_languages, get_contributors, len, get_releases

## 文件内调用关系
- `main` -> get_repo_info, get_readme, format_tree, get_tree, get_languages, get_contributors, get_recent_commits, get_issues, get_pull_requests, get_releases, summarize_repo
- `GitHubAPI.get_repo_info` -> _get
- `GitHubAPI.get_readme` -> _get
- `GitHubAPI.get_tree` -> _get
- `GitHubAPI.get_file_content` -> _get
- `GitHubAPI.get_languages` -> _get
- `GitHubAPI.get_contributors` -> _get
- `GitHubAPI.get_recent_commits` -> _get
- `GitHubAPI.get_issues` -> _get
- `GitHubAPI.get_pull_requests` -> _get
- `GitHubAPI.get_releases` -> _get
- `GitHubAPI.get_tags` -> _get
- `GitHubAPI.search_issues` -> _get
- `GitHubAPI.get_commit_activity` -> _get
- `GitHubAPI.get_code_frequency` -> _get
- `GitHubAPI.summarize_repo` -> get_repo_info, get_languages, get_contributors, get_releases

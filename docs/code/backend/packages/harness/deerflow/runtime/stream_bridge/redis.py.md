# `backend/packages/harness/deerflow/runtime/stream_bridge/redis.py`

> 代码事实分析（自动生成，基于 AST 静态分析，非 docstring 转载）  
> 源文件: `backend/packages/harness/deerflow/runtime/stream_bridge/redis.py`  ·  行数: 251

**模块文档首行**（仅供参考）: Redis Streams-backed stream bridge.

## 模块概览
- 函数 0 个，类 1 个，模块级常量 6 个

## 依赖（import）
- 模块: asyncio, inspect, json, logging, re
- `__future__` -> annotations
- `collections.abc` -> AsyncIterator, Mapping
- `typing` -> Any
- `.base` -> END_SENTINEL, HEARTBEAT_SENTINEL, StreamBridge, StreamEvent

## 模块级常量
- `logger` = logging.getLogger(__name__)
- `_KIND_EVENT` = 'event'
- `_KIND_END` = 'end'
- `_REDIS_STREAM_ID_RE` = re.compile('\\d+(-\\d+)?')
- `_XREAD_COUNT` = 64
- `_MAX_SUBSCRIBE_RETRIES` = 3

## 类
### 类 `RedisStreamBridge`  L51
- 继承: StreamBridge
- _文档首行_: Per-run stream bridge backed by Redis Streams.
- 类/实例变量:
  - `supports_cross_process` = True
- 方法:
  #### `cls` `_normalise_fields(cls, fields: Mapping[Any, Any]) -> dict[str, str]`    @classmethod  L114
    - 分支数 0，函数体节点数 54；return: {cls._decode(key): cls._decode(value) for key, value in fields.items()}
    - 调用: _decode, items
  #### `st` `_decode(value: Any) -> str`    @staticmethod  L108
    - 分支数 1，函数体节点数 30；return: value.decode('utf-8'), str(value)
    - 调用: isinstance, decode, str
  #### `st` `_encode_data(data: Any) -> str`    @staticmethod  L118
    - 分支数 0，函数体节点数 27；return: json.dumps(data, default=str, ensure_ascii=False, separators=(',', ':'))
    - 调用: dumps
  #### `st` `_decode_data(raw: str | None) -> Any`    @staticmethod  L122
    - 分支数 2，函数体节点数 44；return: None, json.loads(raw), raw
    - 调用: loads, warning
  #### `m` `__init__(self, *, redis_url: str, queue_maxsize: int, key_prefix: str, max_connections: int | None, stream_ttl_seconds: int | None, client: Redis | None) -> None`  L61
    - 分支数 1，函数体节点数 126
    - 调用: max, rstrip, from_url
  #### `m` `_stream_key(self, run_id: str) -> str`  L84
    - 分支数 0，函数体节点数 19；return: f'{self._key_prefix}:{run_id}'
  #### `m` `_entry_from_redis(self, event_id: str, fields: Mapping[Any, Any]) -> StreamEvent`  L131
    - 分支数 1，函数体节点数 77；return: END_SENTINEL, StreamEvent(id=event_id, event=payload.get('event', 'message'), data=self._decode_data(payload.get('data')))
    - 调用: _normalise_fields, get, StreamEvent, _decode_data
  #### `⏵m` `async _xadd_retained(self, key: str, fields: dict[str, str], *, maxlen: int) -> None`  L87
    - 分支数 2，函数体节点数 95；return: None
    - 调用: xadd, pipeline, expire, execute
  #### `⏵m` `async publish(self, run_id: str, event: str, data: Any) -> None`  L142
    - 分支数 0，函数体节点数 52
    - 调用: _stream_key, _xadd_retained, _encode_data
  #### `⏵m` `async publish_end(self, run_id: str) -> None`  L154
    - 分支数 0，函数体节点数 38
    - 调用: _stream_key, _xadd_retained
  #### `⏵m` `async stream_exists(self, run_id: str) -> bool`  L163
    - _文档首行_（仅供参考）: Return whether Redis still has retained stream data for *run_id*.
    - 分支数 0，函数体节点数 29；return: bool(await self._redis.exists(self._stream_key(run_id)))
    - 调用: bool, exists, _stream_key
  - 文件IO: exists (L165)
  #### `⏵m` `async _resolve_start_stream_id(self, key: str, last_event_id: str | None) -> str`  L167
    - 分支数 4，函数体节点数 98；return: '0-0', last_event_id, self._decode(event_id)
    - 调用: fullmatch, xrevrange, _normalise_fields, get, _decode
  #### `⏵m` `async subscribe(self, run_id: str, *, last_event_id: str | None, heartbeat_interval: float) -> AsyncIterator[StreamEvent]`  L181
    - 分支数 7，函数体节点数 241；生成器（yield）；raise: bare raise；return: None
    - 调用: _stream_key, _resolve_start_stream_id, max, int, xread, warning, min, sleep, _decode, _entry_from_redis
  #### `⏵m` `async cleanup(self, run_id: str, *, delay: float) -> None`  L237
    - 分支数 1，函数体节点数 42
    - 调用: sleep, delete, _stream_key
  #### `⏵m` `async close(self) -> None`  L242
    - 分支数 3，函数体节点数 60；return: None
    - 调用: getattr, close, isawaitable
  - 反射: getattr (L245), getattr (L245)

## 文件内调用关系
- `RedisStreamBridge._normalise_fields` -> _decode
- `RedisStreamBridge._entry_from_redis` -> _normalise_fields, _decode_data
- `RedisStreamBridge.publish` -> _stream_key, _xadd_retained, _encode_data
- `RedisStreamBridge.publish_end` -> _stream_key, _xadd_retained
- `RedisStreamBridge.stream_exists` -> _stream_key
- `RedisStreamBridge._resolve_start_stream_id` -> _normalise_fields, _decode
- `RedisStreamBridge.subscribe` -> _stream_key, _resolve_start_stream_id, _decode, _entry_from_redis
- `RedisStreamBridge.cleanup` -> _stream_key
- `RedisStreamBridge.close` -> close

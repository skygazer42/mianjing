# KV Cache

## 一句话定位

KV Cache 是自回归解码时的关键优化：把历史 token 的 Key 和 Value 缓存下来，避免重复计算。

## 高频面试题

1. KV Cache 为什么能显著加速推理？
2. KV Cache 优化的是 prefilling 还是 decoding？
3. KV Cache 的主要代价是什么？
4. batch 变大时，KV Cache 会遇到什么挑战？
5. KV Cache 和长上下文能力有什么关系？

## 原理剖析

- 生成第 `t` 个 token 时，前 `t-1` 个 token 的 K、V 实际上已经算过了。
- 如果每一步都重算整段历史，成本会非常高。
- KV Cache 的做法是把旧 K、V 存起来，新一步只计算当前 token 的 Q、K、V。
- 然后用最新 Q 去和“历史缓存 + 当前 K”一起做 attention。
- 代价是显存/内存占用会随上下文长度增长。

## 极简实现

```python
cache_k = []
cache_v = []


def append_kv(new_k: list[float], new_v: list[float]) -> None:
    cache_k.append(new_k)
    cache_v.append(new_v)


append_kv([0.1, 0.2], [1.0, 1.0])
append_kv([0.3, 0.4], [2.0, 2.0])
print(cache_k)
print(cache_v)
```

这个例子只展示“缓存并复用”的思路，没有展开完整 attention。

## 继续追问

1. 为什么长上下文推理时 KV Cache 会吃掉大量显存？
2. paged KV cache 在解决什么问题？
3. 为什么首 token 延迟和后续 token 延迟关注点不一样？

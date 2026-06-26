# Self-Attention

## 一句话定位

self-attention 的核心是：让每个 token 都能按相关性去读取其他 token 的信息。

## 高频面试题

1. Q、K、V 分别代表什么？
2. 为什么 attention score 要除以 `sqrt(d_k)`？
3. self-attention 为什么是 `O(n^2)`？
4. causal mask 是干什么的？
5. self-attention 和 cross-attention 的区别是什么？

## 原理剖析

- 每个 token 会生成三份表示：Query、Key、Value。
- Query 和其他 token 的 Key 做相似度计算，得到注意力分数。
- 分数经过 softmax 变成权重，再对所有 Value 做加权求和。
- 如果是自回归生成，还要加 causal mask，避免看到未来 token。

## 极简实现

```python
import math

def softmax(xs: list[float]) -> list[float]:
    exps = [math.exp(x) for x in xs]
    s = sum(exps)
    return [x / s for x in exps]


def attention(query: list[float], keys: list[list[float]], values: list[list[float]]) -> list[float]:
    scores = [sum(q * k for q, k in zip(query, key)) / math.sqrt(len(query)) for key in keys]
    weights = softmax(scores)
    return [
        sum(weight * value[dim] for weight, value in zip(weights, values))
        for dim in range(len(values[0]))
    ]


q = [1.0, 0.0]
ks = [[1.0, 0.0], [0.0, 1.0]]
vs = [[10.0, 0.0], [0.0, 20.0]]
print(attention(q, ks, vs))
```

## 继续追问

1. 为什么 attention 能比 RNN 更容易并行？
2. softmax 会带来哪些数值稳定性问题？
3. 长序列下 attention 成本为什么会成为瓶颈？

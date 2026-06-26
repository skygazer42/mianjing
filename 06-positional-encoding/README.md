# Positional Encoding

## 一句话定位

self-attention 天生不感知顺序，所以必须显式把位置信息注入到 token 表示里。

## 高频面试题

1. 为什么 Transformer 需要位置编码？
2. 正弦位置编码和可学习位置编码的区别是什么？
3. 为什么说正弦位置编码有一定外推能力？
4. 位置编码通常和 token embedding 怎么融合？
5. RoPE 和传统位置编码的差别是什么？

## 原理剖析

- “我爱你”和“你爱我”token 集合差不多，但语义完全不同，问题就在顺序。
- 传统 self-attention 看的是 token 间相似度，不带顺序偏好。
- 所以要给每个位置一个额外向量，再和 token embedding 相加。
- 正弦位置编码的好处是没有额外参数，而且不同维度对应不同频率。

## 极简实现

```python
import math

def positional_encoding(position: int, d_model: int) -> list[float]:
    vec = []
    for i in range(d_model):
        angle = position / (10000 ** (2 * (i // 2) / d_model))
        vec.append(math.sin(angle) if i % 2 == 0 else math.cos(angle))
    return vec


print(positional_encoding(3, 8))
```

## 继续追问

1. 为什么很多 decoder-only LLM 后来更偏向 RoPE？
2. 如果序列长度翻倍，传统位置编码会遇到什么问题？
3. 位置编码会不会破坏原始 token embedding 的语义信息？

# RoPE

## 一句话定位

RoPE（Rotary Position Embedding）通过对 Q 和 K 做旋转变换，把位置信息注入 attention 计算里。

## 高频面试题

1. RoPE 和传统位置编码的核心差别是什么？
2. 为什么很多 decoder-only 大模型喜欢用 RoPE？
3. RoPE 为什么更容易表达相对位置关系？
4. 长上下文外推时，RoPE 会遇到什么问题？
5. RoPE scaling 在解决什么问题？

## 原理剖析

- 传统位置编码常常是“把位置向量加到 embedding 上”。
- RoPE 的思路不同：直接对 Query 和 Key 的每一对维度做旋转。
- 这样一来，`QK^T` 的结果会天然携带相对位置信息。
- 所以它很适合自回归生成模型，也更贴近 attention 内部的计算方式。

## 极简实现

```python
import math

def rope_rotate(x1: float, x2: float, theta: float) -> tuple[float, float]:
    return (
        x1 * math.cos(theta) - x2 * math.sin(theta),
        x1 * math.sin(theta) + x2 * math.cos(theta),
    )


def apply_rope(vec: list[float], position: int) -> list[float]:
    out = []
    for i in range(0, len(vec), 2):
        theta = position / (10000 ** (i / len(vec)))
        out.extend(rope_rotate(vec[i], vec[i + 1], theta))
    return out


print(apply_rope([1.0, 2.0, 3.0, 4.0], 5))
```

## 继续追问

1. 为什么 RoPE 常和 KV Cache 一起讨论？
2. 如果上下文长度从 4k 扩到 128k，RoPE 哪些部分要改？
3. RoPE 和 ALiBi 的思路差异是什么？

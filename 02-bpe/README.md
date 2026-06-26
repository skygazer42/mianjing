# BPE

## 一句话定位

BPE（Byte Pair Encoding）是一种通过不断合并高频相邻子串来构造子词词表的方法。

## 高频面试题

1. 为什么需要 BPE，而不是直接按词切分？
2. BPE 训练时到底在合并什么？
3. BPE 如何缓解 OOV（未登录词）问题？
4. 词表大小变大时，序列长度和泛化能力会怎么变化？
5. BPE 和 WordPiece 的核心区别是什么？

## 原理剖析

- 最开始把文本拆成很细的单元，通常可以理解成字符级别。
- 统计所有相邻 token pair 的出现频次。
- 每一轮都把最常出现的 pair 合并成一个新 token。
- 不断重复，直到达到预设词表大小。
- 这样做的结果是：高频模式会被压缩成更长的 token，低频词仍然可以退化成更细粒度子词。

## 极简实现

```python
from collections import Counter

def most_common_pair(tokens: list[str]) -> tuple[str, str]:
    pairs = Counter(zip(tokens, tokens[1:]))
    return pairs.most_common(1)[0][0]


tokens = ["l", "o", "w", "l", "o", "w", "e", "r"]
pair = most_common_pair(tokens)
merged = []
i = 0
while i < len(tokens):
    if i + 1 < len(tokens) and (tokens[i], tokens[i + 1]) == pair:
        merged.append(tokens[i] + tokens[i + 1])
        i += 2
    else:
        merged.append(tokens[i])
        i += 1

print(pair)
print(merged)
```

这段代码只演示“一轮合并”，完整 BPE 会迭代很多轮。

## 继续追问

1. 为什么 BPE 适合多语言和代码场景？
2. BPE 词表太小时会发生什么？
3. 如果训练语料偏了，BPE 学出来的词表会有什么问题？

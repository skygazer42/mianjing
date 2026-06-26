# Embedding

## 一句话定位

embedding 就是把离散 token id 映射成连续向量，让模型可以在向量空间里学习语义关系。

## 高频面试题

1. one-hot 和 embedding 的区别是什么？
2. embedding 矩阵的形状怎么理解？
3. 为什么语义接近的 token 向量会更接近？
4. 输入 embedding 和输出 embedding 可以共享吗？
5. 词表变大时，embedding 成本会怎么变化？

## 原理剖析

- 假设词表大小是 `V`，隐藏维度是 `D`，那么 embedding 矩阵就是 `V x D`。
- 查某个 token，本质上就是按 id 去这个矩阵里取一行。
- 这和 one-hot 乘矩阵在数学上等价，但查表更高效。
- embedding 不是人工编码的语义，它是在训练目标下被梯度更新出来的参数。

## 极简实现

```python
embedding_table = [
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9],
]


def embedding_lookup(token_ids: list[int]) -> list[list[float]]:
    return [embedding_table[idx] for idx in token_ids]


print(embedding_lookup([0, 2]))
```

## 继续追问

1. 为什么 embedding 可以学到语义，而不是只学到编号？
2. 词表扩容后，新增 token 的 embedding 怎么初始化？
3. 输入 embedding 和位置编码是相加还是拼接？

# Transformer

## 一句话定位

Transformer 是由 attention、前馈网络、残差连接和归一化堆叠起来的序列建模架构。

## 高频面试题

1. Transformer 为什么能替代 RNN 成为主流？
2. 一个 Transformer block 里有哪些核心模块？
3. residual connection 和 layer norm 的作用是什么？
4. encoder-only、decoder-only、encoder-decoder 三种结构怎么区分？
5. pre-norm 和 post-norm 的差别是什么？

## 原理剖析

- attention 负责“信息交互”，MLP 负责“非线性变换”。
- residual 让深层网络更容易训练，避免信息被层层覆盖掉。
- layer norm 让数值分布更稳定。
- 多层堆叠以后，模型可以逐渐形成从局部模式到高阶语义的表达。
- 大语言模型常见的是 decoder-only Transformer。

## 极简实现

```python
def layer_norm(x: list[float]) -> list[float]:
    mean = sum(x) / len(x)
    var = sum((v - mean) ** 2 for v in x) / len(x)
    return [(v - mean) / (var + 1e-5) ** 0.5 for v in x]


def mlp(x: list[float]) -> list[float]:
    return [max(0.0, 2 * v) for v in x]


def transformer_block(x: list[float]) -> list[float]:
    attn_out = x
    x = [a + b for a, b in zip(x, attn_out)]
    ff_out = mlp(layer_norm(x))
    return [a + b for a, b in zip(x, ff_out)]


print(transformer_block([0.2, -0.1, 0.4]))
```

这个实现故意省略了真实 attention 细节，只保留 block 的骨架。

## 继续追问

1. 为什么 Transformer 更适合大规模预训练？
2. 多头注意力相比单头到底多了什么能力？
3. block 数量和 hidden size 变大时，训练瓶颈通常在哪里？

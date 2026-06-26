# Unigram

## 一句话定位

Unigram tokenizer 的思路不是“从小往大合并”，而是“先给大词表，再删掉没那么重要的子词”。

## 高频面试题

1. Unigram 和 BPE、WordPiece 的训练思路差别是什么？
2. 为什么 Unigram 常被描述成概率模型？
3. 什么是 subword regularization？
4. Unigram 为什么对长尾词和噪声更稳一些？
5. SentencePiece 和 Unigram 有什么关系？

## 原理剖析

- 先准备一个偏大的候选子词集合。
- 每个子词带一个概率或分数，用来表示它对语料切分的解释能力。
- 对一句话来说，可以有多种切分路径，系统会选总损失更低的那条。
- 训练过程中不断删掉“贡献小”的子词，让词表逐步收敛。
- 这类方法天然适合做采样式分词，也就是 subword regularization。

## 极简实现

```python
import math

def best_split(word: str, scores: dict[str, float]) -> tuple[float, list[str]]:
    dp = [(math.inf, []) for _ in range(len(word) + 1)]
    dp[0] = (0.0, [])
    for i in range(len(word)):
        cur_score, cur_path = dp[i]
        if cur_score == math.inf:
            continue
        for j in range(i + 1, len(word) + 1):
            piece = word[i:j]
            if piece in scores:
                cand = cur_score - math.log(scores[piece])
                if cand < dp[j][0]:
                    dp[j] = (cand, cur_path + [piece])
    return dp[-1]


scores = {"a": 0.2, "ab": 0.5, "b": 0.3}
print(best_split("ab", scores))
```

## 继续追问

1. Unigram 为什么适合做多种切分采样？
2. 如果某个词可以拆成很多种方式，如何选最优路径？
3. Unigram 的训练成本和 BPE 相比通常更高还是更低？

# WordPiece

## 一句话定位

WordPiece 是一种常见的子词切分方法，典型特点是推理时采用最长匹配，把词切成词表中能命中的最大子词。

## 高频面试题

1. WordPiece 和 BPE 的差异到底在哪？
2. WordPiece 推理时为什么常说是“贪心最长匹配”？
3. `[UNK]` 是怎么出现的？
4. BERT 为什么适合用 WordPiece？
5. WordPiece 在中文场景下和英文场景下会有什么不同？

## 原理剖析

- BPE 更像“按频次不断合并”，WordPiece 更强调“词表上的最优子词切分”。
- 推理阶段常用 longest-match-first：每次优先拿最长、能命中的子词。
- 如果从当前位置开始没有任何子词能命中，通常就回退到 `[UNK]`。
- 相比纯词级切分，WordPiece 可以更稳定地处理长尾词和新词。

## 极简实现

```python
def wordpiece_encode(word: str, vocab: set[str]) -> list[str]:
    pieces = []
    i = 0
    while i < len(word):
        matched = None
        for j in range(len(word), i, -1):
            piece = word[i:j] if i == 0 else "##" + word[i:j]
            if piece in vocab:
                matched = piece
                break
        if matched is None:
            return ["[UNK]"]
        pieces.append(matched)
        i = j
    return pieces


vocab = {"play", "##ing", "player"}
print(wordpiece_encode("playing", vocab))
```

## 继续追问

1. 最长匹配为什么不是全局最优搜索？
2. 如果词表里同时有 `play` 和 `player`，切分结果如何决定？
3. WordPiece 对检索、分类、生成任务的影响一样吗？

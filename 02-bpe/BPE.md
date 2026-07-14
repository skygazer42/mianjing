# BPE 到底是什么

**BPE（Byte Pair Encoding）本质上是一个贪心的相邻符号合并算法：**

1. 一开始把文本拆成最小符号，例如字符或字节。
2. 统计所有相邻符号对的出现次数。
3. 找到出现次数最多的符号对。
4. 把它们合并成一个新符号。
5. 重复执行若干次。

在 NLP 中，BPE 的目的不是单纯压缩文件，而是构造一个**子词词表**：

* 高频单词或词根可以成为一个 token。
* 低频单词可以拆成多个 token。
* 不需要给每个完整单词都分配词表项。
* 可以在词表大小和序列长度之间取得平衡。

---

# 一、先用一个例子理解

训练语料：

```text
low low lower
```

词频为：

```text
low   -> 2 次
lower -> 1 次
```

先把每个词拆成字符，并添加词尾标记 `</w>`：

```text
low   -> l o w </w>      频率 2
lower -> l o w e r </w>  频率 1
```

`</w>` 表示“一个词到这里结束”。

## 第一次统计相邻对

`low` 中有：

```text
(l, o)
(o, w)
(w, </w>)
```

因为 `low` 出现两次，所以每一对贡献 2 次。

`lower` 中有：

```text
(l, o)
(o, w)
(w, e)
(e, r)
(r, </w>)
```

最终统计：

| 相邻对         | 频次 |
| ----------- | -: |
| `(l, o)`    |  3 |
| `(o, w)`    |  3 |
| `(w, </w>)` |  2 |
| `(w, e)`    |  1 |
| `(e, r)`    |  1 |
| `(r, </w>)` |  1 |

假设并列时选择 `(l, o)`：

```text
l + o -> lo
```

语料变成：

```text
low   -> lo w </w>
lower -> lo w e r </w>
```

## 第二次合并

现在 `(lo, w)` 出现 3 次：

```text
lo + w -> low
```

语料变成：

```text
low   -> low </w>
lower -> low e r </w>
```

## 第三次合并

`(low, </w>)` 出现两次：

```text
low + </w> -> low</w>
```

结果：

```text
low   -> low</w>
lower -> low e r </w>
```

这时，独立单词 `low` 已经是一个 token，而 `lower` 仍然可以利用公共前缀 `low`。

这正是 BPE 的价值：

```text
高频结构：合并成大 token
低频结构：保留为多个小 token
```

---

# 二、数学定义

设一个词被表示为符号序列：

[
s_w = [s_1,s_2,\dots,s_n]
]

该词在语料中的出现次数为：

[
f(w)
]

相邻符号对 ((a,b)) 的全局频次为：

[
C(a,b)
======

\sum_w f(w)
\sum_{i=1}^{|s_w|-1}
\mathbf{1}[s_i=a \land s_{i+1}=b]
]

其中：

* (f(w)) 是词频。
* (\mathbf{1}[\cdot]) 是指示函数。
* 条件成立时值为 1，否则为 0。

每轮选择：

[
(a^*,b^*)=\arg\max_{(a,b)} C(a,b)
]

然后创建新符号：

[
c = a^* \oplus b^*
]

其中 (\oplus) 表示字符串拼接。

例如：

[
\text{lo} \oplus \text{w} = \text{low}
]

---

# 三、BPE 包含三个不同阶段

必须区分下面三件事。

## 1. 训练 tokenizer

训练阶段需要：

* 统计词频。
* 统计相邻 token 对。
* 反复寻找最高频 token 对。
* 保存每一次 merge 规则。

最终得到类似：

```text
l o   -> lo
lo w  -> low
low </w> -> low</w>
e r   -> er
low er -> lower
```

这些规则有严格的先后顺序。

---

## 2. 编码新文本

编码新文本时，**不能重新统计新文本中的频率**。

必须使用训练得到的 merge 顺序。

例如训练规则：

```text
rank 0: l + o   -> lo
rank 1: lo + w  -> low
rank 2: low + </w> -> low</w>
```

编码：

```text
low
```

初始：

```text
l o w </w>
```

应用 rank 0：

```text
lo w </w>
```

应用 rank 1：

```text
low </w>
```

应用 rank 2：

```text
low</w>
```

最终得到一个 token。

---

## 3. 解码

每一个 token ID 都对应一个字符串。

例如：

```text
8 -> low</w>
10 -> lower
5 -> </w>
```

把 token 字符串拼起来：

```text
low</w>lower</w>
```

再把 `</w>` 替换成空格：

```text
low lower
```

---

# 四、为什么 NumPy 不能把所有步骤完全向量化

NumPy 很适合：

* 提取所有相邻对。
* 对相邻对去重。
* 汇总频次。
* 找最大频次。

例如：

```python
ids = np.array([1, 3, 7, 9])

pairs = np.column_stack((ids[:-1], ids[1:]))
```

结果：

```text
[[1, 3],
 [3, 7],
 [7, 9]]
```

但是“合并”不能直接依靠一个简单布尔 mask。

考虑：

```text
A A A
```

合并：

```text
A + A -> AA
```

两个候选位置是：

```text
位置 0、1
位置 1、2
```

它们互相重叠。

正确的从左到右合并结果是：

```text
AA A
```

不能同时合并为两个 `AA`，因为中间的 `A` 不能被使用两次。

因此，教学版实现通常采用：

* NumPy 进行 pair 提取和统计。
* Python 循环进行不重叠合并。

---

# 五、完整 NumPy BPE 实现

下面实现包含：

* BPE 训练。
* 相邻 pair 统计。
* 不重叠合并。
* 新文本编码。
* token ID 转 token。
* 解码。
* merge 规则查看。

```python
from __future__ import annotations

from collections import Counter
import numpy as np


def count_adjacent_pairs(
    sequences: list[np.ndarray],
    frequencies: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """
    统计所有序列中的相邻 token 对。

    返回:
        unique_pairs:
            shape = [P, 2]
            每一行是 [left_token_id, right_token_id]

        counts:
            shape = [P]
            每一个 pair 考虑词频后的总出现次数
    """
    pair_blocks: list[np.ndarray] = []
    weight_blocks: list[np.ndarray] = []

    for ids, frequency in zip(sequences, frequencies):
        if ids.size < 2:
            continue

        # [a, b, c] -> [[a, b], [b, c]]
        pairs = np.column_stack((ids[:-1], ids[1:]))
        pair_blocks.append(pairs)

        # 一个词出现 frequency 次，
        # 它内部的每一个 pair 都应该增加 frequency。
        weights = np.full(
            pairs.shape[0],
            int(frequency),
            dtype=np.int64,
        )
        weight_blocks.append(weights)

    if not pair_blocks:
        return (
            np.empty((0, 2), dtype=np.int32),
            np.empty((0,), dtype=np.int64),
        )

    all_pairs = np.vstack(pair_blocks).astype(
        np.int32,
        copy=False,
    )
    all_weights = np.concatenate(weight_blocks)

    # 找到所有不同的 pair。
    #
    # inverse[i] 表示 all_pairs[i]
    # 对应 unique_pairs 中的哪一行。
    unique_pairs, inverse = np.unique(
        all_pairs,
        axis=0,
        return_inverse=True,
    )

    counts = np.zeros(
        unique_pairs.shape[0],
        dtype=np.int64,
    )

    # 按 inverse 累加对应的词频权重。
    np.add.at(counts, inverse, all_weights)

    return unique_pairs, counts


def merge_pair(
    ids: np.ndarray,
    pair: tuple[int, int],
    new_id: int,
) -> np.ndarray:
    """
    从左向右合并所有不重叠的 pair。

    例如:
        ids  = [A, A, A]
        pair = (A, A)

    正确结果:
        [AA, A]

    不能同时合并位置 (0, 1) 和 (1, 2)，
    因为它们共享中间的 A。
    """
    left_id, right_id = pair
    output: list[int] = []

    i = 0

    while i < ids.size:
        can_merge = (
            i + 1 < ids.size
            and int(ids[i]) == left_id
            and int(ids[i + 1]) == right_id
        )

        if can_merge:
            output.append(new_id)
            i += 2
        else:
            output.append(int(ids[i]))
            i += 1

    return np.asarray(output, dtype=np.int32)


class NumpyBPE:
    """
    教学版 BPE：

    1. 使用 text.split() 按空白预分词。
    2. 初始 token 是字符。
    3. 使用 </w> 表示词尾。
    4. 使用 NumPy 统计相邻 pair。
    5. 支持训练、编码和解码。

    这不是 GPT 式 byte-level BPE。
    """

    EOW = "</w>"

    def __init__(self) -> None:
        # 字符串 token -> 整数 ID
        self.symbol_to_id: dict[str, int] = {}

        # 整数 ID -> 字符串 token
        self.id_to_symbol: list[str] = []

        # 每项:
        # (
        #   left_id,
        #   right_id,
        #   new_id,
        #   训练时的 pair 频次
        # )
        self.merges: list[
            tuple[int, int, int, int]
        ] = []

        # pair -> merge 顺序
        #
        # rank 越小，表示该 merge 越早学到，
        # 编码时优先级越高。
        self.pair_rank: dict[
            tuple[int, int],
            int,
        ] = {}

        # pair -> 合并后的新 token ID
        self.pair_to_new_id: dict[
            tuple[int, int],
            int,
        ] = {}

        self.is_fitted = False

    @property
    def vocab_size(self) -> int:
        return len(self.id_to_symbol)

    def _add_symbol(self, symbol: str) -> int:
        existing_id = self.symbol_to_id.get(symbol)

        if existing_id is not None:
            return existing_id

        token_id = len(self.id_to_symbol)

        self.symbol_to_id[symbol] = token_id
        self.id_to_symbol.append(symbol)

        return token_id

    @staticmethod
    def _split_words(text: str) -> list[str]:
        """
        教学版预分词器。

        注意:
        text.split() 不保留连续空格和换行数量。
        """
        return text.split()

    def fit(
        self,
        corpus: list[str],
        *,
        num_merges: int = 100,
        min_pair_frequency: int = 2,
        verbose: bool = False,
    ) -> "NumpyBPE":
        if num_merges < 0:
            raise ValueError("num_merges 必须 >= 0")

        if min_pair_frequency < 1:
            raise ValueError(
                "min_pair_frequency 必须 >= 1"
            )

        # ---------------------------------
        # 第一步：统计完整单词的出现次数
        # ---------------------------------

        word_frequency: Counter[str] = Counter()

        for text in corpus:
            words = self._split_words(text)
            word_frequency.update(words)

        if not word_frequency:
            raise ValueError(
                "corpus 中没有可训练的词"
            )

        # 重新训练时清除旧状态。
        self.symbol_to_id.clear()
        self.id_to_symbol.clear()
        self.merges.clear()
        self.pair_rank.clear()
        self.pair_to_new_id.clear()
        self.is_fitted = False

        # ---------------------------------
        # 第二步：建立初始字符词表
        # ---------------------------------

        characters = sorted(
            {
                character
                for word in word_frequency
                for character in word
            }
        )

        for character in characters:
            self._add_symbol(character)

        eow_id = self._add_symbol(self.EOW)

        # ---------------------------------
        # 第三步：把每个词转换成 token ID
        # ---------------------------------

        words = list(word_frequency.keys())

        frequencies = np.asarray(
            [
                word_frequency[word]
                for word in words
            ],
            dtype=np.int64,
        )

        sequences = [
            np.asarray(
                [
                    self.symbol_to_id[character]
                    for character in word
                ]
                + [eow_id],
                dtype=np.int32,
            )
            for word in words
        ]

        # ---------------------------------
        # 第四步：重复学习 merge
        # ---------------------------------

        for step in range(num_merges):
            pairs, counts = count_adjacent_pairs(
                sequences,
                frequencies,
            )

            if counts.size == 0:
                break

            best_index = int(np.argmax(counts))

            best_pair = (
                int(pairs[best_index, 0]),
                int(pairs[best_index, 1]),
            )

            best_count = int(counts[best_index])

            if best_count < min_pair_frequency:
                break

            left_id, right_id = best_pair

            new_symbol = (
                self.id_to_symbol[left_id]
                + self.id_to_symbol[right_id]
            )

            new_id = self._add_symbol(new_symbol)

            rank = len(self.merges)

            self.merges.append(
                (
                    left_id,
                    right_id,
                    new_id,
                    best_count,
                )
            )

            self.pair_rank[best_pair] = rank
            self.pair_to_new_id[best_pair] = new_id

            # 将本轮的最佳 pair 应用于所有词。
            sequences = [
                merge_pair(
                    ids,
                    best_pair,
                    new_id,
                )
                for ids in sequences
            ]

            if verbose:
                print(
                    f"{step:02d}: "
                    f"{self.id_to_symbol[left_id]!r} + "
                    f"{self.id_to_symbol[right_id]!r} -> "
                    f"{self.id_to_symbol[new_id]!r}, "
                    f"count={best_count}"
                )

        self.is_fitted = True
        return self

    def _encode_word(
        self,
        word: str,
    ) -> np.ndarray:
        if not self.is_fitted:
            raise RuntimeError(
                "请先调用 fit()"
            )

        # ---------------------------------
        # 第一步：从字符 token 开始
        # ---------------------------------

        ids: list[int] = []

        for character in word:
            token_id = self.symbol_to_id.get(character)

            if token_id is None:
                raise ValueError(
                    f"字符 {character!r} "
                    "未出现在训练语料中；"
                    "教学版字符 BPE 无法无损表示它"
                )

            ids.append(token_id)

        ids.append(
            self.symbol_to_id[self.EOW]
        )

        sequence = np.asarray(
            ids,
            dtype=np.int32,
        )

        # ---------------------------------
        # 第二步：按训练 rank 应用 merge
        # ---------------------------------

        infinity = np.iinfo(np.int64).max

        while sequence.size >= 2:
            pairs = np.column_stack(
                (
                    sequence[:-1],
                    sequence[1:],
                )
            )

            ranks = np.fromiter(
                (
                    self.pair_rank.get(
                        (
                            int(left_id),
                            int(right_id),
                        ),
                        infinity,
                    )
                    for left_id, right_id in pairs
                ),
                dtype=np.int64,
                count=pairs.shape[0],
            )

            best_position = int(
                np.argmin(ranks)
            )

            # 当前序列中已经没有可应用的 merge。
            if ranks[best_position] == infinity:
                break

            best_pair = (
                int(pairs[best_position, 0]),
                int(pairs[best_position, 1]),
            )

            sequence = merge_pair(
                sequence,
                best_pair,
                self.pair_to_new_id[best_pair],
            )

        return sequence

    def encode(
        self,
        text: str,
    ) -> np.ndarray:
        words = self._split_words(text)

        if not words:
            return np.empty(
                (0,),
                dtype=np.int32,
            )

        encoded_words = [
            self._encode_word(word)
            for word in words
        ]

        return np.concatenate(encoded_words)

    def encode_tokens(
        self,
        text: str,
    ) -> list[str]:
        token_ids = self.encode(text)

        return [
            self.id_to_symbol[int(token_id)]
            for token_id in token_ids
        ]

    def decode(
        self,
        token_ids: np.ndarray | list[int],
    ) -> str:
        if not self.is_fitted:
            raise RuntimeError(
                "请先调用 fit()"
            )

        joined = "".join(
            self.id_to_symbol[int(token_id)]
            for token_id in token_ids
        )

        return joined.replace(
            self.EOW,
            " ",
        ).rstrip()

    def learned_merges(
        self,
    ) -> list[tuple[str, str, str, int]]:
        result: list[
            tuple[str, str, str, int]
        ] = []

        for (
            left_id,
            right_id,
            new_id,
            count,
        ) in self.merges:
            result.append(
                (
                    self.id_to_symbol[left_id],
                    self.id_to_symbol[right_id],
                    self.id_to_symbol[new_id],
                    count,
                )
            )

        return result
```

---

# 六、运行示例

```python
corpus = [
    "low low lower",
]

tokenizer = NumpyBPE().fit(
    corpus,
    num_merges=5,
    min_pair_frequency=1,
    verbose=True,
)

token_ids = tokenizer.encode(
    "low lower"
)

tokens = tokenizer.encode_tokens(
    "low lower"
)

decoded = tokenizer.decode(
    token_ids
)

print("vocab_size:", tokenizer.vocab_size)
print("token_ids:", token_ids.tolist())
print("tokens:", tokens)
print("decoded:", decoded)
```

输出类似：

```text
00: 'l' + 'o' -> 'lo', count=3
01: 'lo' + 'w' -> 'low', count=3
02: 'low' + '</w>' -> 'low</w>', count=2
03: 'e' + 'r' -> 'er', count=1
04: 'low' + 'er' -> 'lower', count=1

vocab_size: 11
token_ids: [8, 10, 5]
tokens: ['low</w>', 'lower', '</w>']
decoded: low lower
```

注意 `lower` 的编码结果是：

```text
lower + </w>
```

因为只学习了：

```text
low + er -> lower
```

还没有继续学习：

```text
lower + </w> -> lower</w>
```

增加一次 merge 后，它也可能成为一个完整的带词尾 token。

---

# 七、逐行理解 NumPy pair 统计

假设：

```python
ids = np.array(
    [4, 2, 8, 6],
    dtype=np.int32,
)
```

左侧序列：

```python
ids[:-1]
```

结果：

```text
[4, 2, 8]
```

右侧序列：

```python
ids[1:]
```

结果：

```text
[2, 8, 6]
```

组合：

```python
pairs = np.column_stack(
    (ids[:-1], ids[1:])
)
```

结果：

```text
[[4, 2],
 [2, 8],
 [8, 6]]
```

多个词的 pair 通过：

```python
all_pairs = np.vstack(pair_blocks)
```

拼接起来。

然后：

```python
unique_pairs, inverse = np.unique(
    all_pairs,
    axis=0,
    return_inverse=True,
)
```

假设：

```text
all_pairs =
[
  [1, 2],
  [2, 3],
  [1, 2],
  [1, 2]
]
```

得到：

```text
unique_pairs =
[
  [1, 2],
  [2, 3]
]

inverse =
[
  0,
  1,
  0,
  0
]
```

`inverse` 表示：

```text
第 0 个原始 pair 对应 unique_pairs[0]
第 1 个原始 pair 对应 unique_pairs[1]
第 2 个原始 pair 对应 unique_pairs[0]
第 3 个原始 pair 对应 unique_pairs[0]
```

最后：

```python
np.add.at(
    counts,
    inverse,
    all_weights,
)
```

按照 `inverse` 把词频权重累加起来。

---

# 八、训练时和编码时为什么不同

这是 BPE 最容易混淆的地方。

## 训练阶段

训练阶段选择：

```text
当前整个训练语料中频率最高的 pair
```

例如：

```text
(l, o) 出现 30000 次
(e, r) 出现 20000 次
```

先合并 `(l, o)`。

## 编码阶段

编码阶段不看新文本中的 pair 频率，而是看：

```text
这个 pair 在训练时是第几轮学到的
```

例如：

```text
rank 0: l + o
rank 1: lo + w
rank 2: e + r
```

编码时总是优先应用 rank 最小的可用规则。

否则，同一个单词在不同句子中可能得到不同编码，这会导致 token ID 不稳定。

---

# 九、词表大小是怎么计算的

假设初始字符数为：

[
A
]

特殊 token 数为：

[
S
]

成功执行 merge 的次数为：

[
M
]

理想情况下：

[
V = A + S + M
]

其中 (V) 是最终词表大小。

例如：

```text
初始字符：100 个
特殊 token：4 个
merge：30000 次
```

最终词表大约为：

```text
30104
```

实际实现中，重复表面字符串、保留 token 或额外控制 token 可能让数字略有不同。

---

# 十、BPE 如何与语言模型耦合

“耦合实现”不是 BPE 的固定术语。常见含义有两种：

1. 把 tokenizer 的训练、编码、解码组合成完整系统。
2. 把 tokenizer 输出连接到 Transformer、RNN 或其他语言模型。

完整数据流是：

```text
原始文本
   ↓
预分词
   ↓
BPE 编码
   ↓
token IDs
   ↓
Embedding 查表
   ↓
Transformer / RNN
   ↓
词表 logits
   ↓
预测 token IDs
   ↓
BPE 解码
   ↓
文本
```

---

## Token ID 进入 embedding

假设：

```python
input_ids = tokenizer.encode(
    "low lower"
)
```

结果：

```text
[8, 10, 5]
```

创建 embedding 矩阵：

```python
rng = np.random.default_rng(42)

vocab_size = tokenizer.vocab_size
hidden_size = 16

embedding = rng.normal(
    size=(vocab_size, hidden_size)
)
```

形状：

```text
embedding.shape = [词表大小, 隐藏维度]
```

查表：

```python
hidden_states = embedding[input_ids]
```

形状：

```text
input_ids.shape     = [sequence_length]
hidden_states.shape = [sequence_length, hidden_size]
```

完整例子：

```python
input_ids = tokenizer.encode(
    "low lower"
)

rng = np.random.default_rng(42)

vocab_size = tokenizer.vocab_size
hidden_size = 16

embedding = rng.normal(
    loc=0.0,
    scale=0.02,
    size=(vocab_size, hidden_size),
)

hidden_states = embedding[input_ids]

print("input_ids:", input_ids)
print("hidden_states shape:", hidden_states.shape)
```

---

## 与语言模型输出层耦合

语言模型需要为每个位置预测下一个 token。

输入：

```text
x0 x1 x2 x3
```

目标：

```text
x1 x2 x3 x4
```

NumPy 示例：

```python
input_ids = tokenizer.encode(
    "low lower low"
)

model_inputs = input_ids[:-1]
targets = input_ids[1:]

vocab_size = tokenizer.vocab_size
hidden_size = 16

rng = np.random.default_rng(42)

embedding = rng.normal(
    0.0,
    0.02,
    size=(vocab_size, hidden_size),
)

output_weight = rng.normal(
    0.0,
    0.02,
    size=(hidden_size, vocab_size),
)

hidden_states = embedding[model_inputs]

# 真实模型中，hidden_states 会先经过 Transformer。
logits = hidden_states @ output_weight

print("model_inputs shape:", model_inputs.shape)
print("targets shape:", targets.shape)
print("logits shape:", logits.shape)
```

形状关系：

```text
hidden_states:
[sequence_length, hidden_size]

output_weight:
[hidden_size, vocab_size]

logits:
[sequence_length, vocab_size]
```

每个位置都会输出对整个 BPE 词表的预测分数。

---

## 交叉熵损失

```python
shifted_logits = (
    logits
    - logits.max(axis=-1, keepdims=True)
)

exp_logits = np.exp(shifted_logits)

probabilities = (
    exp_logits
    / exp_logits.sum(axis=-1, keepdims=True)
)

positions = np.arange(targets.size)

target_probabilities = probabilities[
    positions,
    targets,
]

loss = -np.log(
    target_probabilities + 1e-12
).mean()

print("loss:", loss)
```

这里的核心耦合关系是：

```text
BPE 的 token ID
必须正好对应
embedding 和输出层的词表行列
```

---

# 十一、tokenizer 训练后为什么不能随便修改

假设训练模型时：

```text
token ID 100 -> "low"
```

模型的 embedding 第 100 行就逐渐学会表示 `"low"`。

后来重新训练 tokenizer，变成：

```text
token ID 100 -> "ing"
```

此时原来的 embedding 第 100 行仍然表示 `"low"` 的语义，但 tokenizer 却把它解释成 `"ing"`。

模型会彻底错乱。

因此正常流程是：

1. 训练 tokenizer。
2. 固定 token 到 ID 的映射。
3. 建立语言模型。
4. 训练语言模型。
5. 推理时继续使用同一份 tokenizer。

tokenizer 的以下内容都必须保存：

* 初始词表。
* token 到 ID 的映射。
* merge 规则。
* merge rank。
* 特殊 token ID。
* 文本规范化方式。
* 预分词规则。

---

# 十二、字符 BPE 的未知字符问题

上面的教学实现从训练语料中的字符开始。

假设训练语料只有：

```text
low lower
```

编码：

```text
hello
```

其中 `h` 没在训练字符表中出现，代码会报错。

有三种处理方式。

## 方案一：使用 `<unk>`

未知字符统一映射到：

```text
<unk>
```

缺点是无法无损恢复原文本。

例如：

```text
猫 -> <unk>
狗 -> <unk>
```

两者信息丢失。

## 方案二：建立足够大的 Unicode 字符表

问题是 Unicode 字符数量非常大，而且仍然可能遇到新字符。

## 方案三：使用 byte-level BPE

现代大模型常用这种办法。

---

# 十三、Byte-level BPE

Byte-level BPE 的初始符号不是 Unicode 字符，而是：

```text
0, 1, 2, ..., 255
```

即所有可能的单字节值。

任意字符串都可以编码成 UTF-8 字节，因此不会出现未知字符。

例如：

```python
text = "你好"

raw_bytes = text.encode("utf-8")

print(list(raw_bytes))
```

可能得到：

```text
[228, 189, 160, 229, 165, 189]
```

用 NumPy 表示：

```python
byte_ids = np.frombuffer(
    text.encode("utf-8"),
    dtype=np.uint8,
).astype(np.int32)
```

初始词表：

```python
id_to_bytes = [
    bytes([value])
    for value in range(256)
]
```

合并两个 token：

```python
left_bytes = id_to_bytes[left_id]
right_bytes = id_to_bytes[right_id]

new_bytes = left_bytes + right_bytes

new_id = len(id_to_bytes)
id_to_bytes.append(new_bytes)
```

解码：

```python
decoded_bytes = b"".join(
    id_to_bytes[token_id]
    for token_id in token_ids
)

text = decoded_bytes.decode(
    "utf-8",
    errors="strict",
)
```

Byte-level BPE 的主要优点：

* 没有未知字符。
* 可以表示所有语言。
* 可以表示 emoji。
* 可以表示特殊符号。
* 可以无损保留文本字节。

代价是：

* 非英文字符通常需要多个初始字节 token。
* 需要足够多的 merge 才能把常见中文或其他多字节字符合成较大的 token。

---

# 十四、GPT 式 BPE 不只是“直接在全文字节上合并”

GPT 类 tokenizer 通常还包含一个**预分词器**。

典型流程：

```text
原始字符串
   ↓
正则表达式预分词
   ↓
每个片段转成 UTF-8 字节
   ↓
在片段内部执行 BPE
```

预分词器可能把文本拆成：

* 单词。
* 标点。
* 空格加单词。
* 数字片段。
* 换行。
* 特殊符号。

这样可以控制 BPE 是否允许跨越某些边界合并。

例如：

```text
" hello"
```

有些 tokenizer 会把前导空格当成 token 的一部分。

因此可能出现：

```text
"hello"
" hello"
```

对应不同 token。

这也是很多 GPT tokenizer 中：

```text
hello
```

和：

```text
 hello
```

编码不同的原因。

---

# 十五、词表大和词表小的权衡

## 较大的词表

优点：

* 一个 token 可以表示更长的字符串。
* 序列更短。
* Transformer 处理的时间步更少。

缺点：

* embedding 矩阵更大。
* 输出层更大。
* 稀有 token 学习次数少。
* 模型参数量增加。

若 embedding 维度为 (d)，词表大小为 (V)，embedding 参数量为：

[
V \times d
]

如果输入 embedding 和输出层不共享参数，二者合计约为：

[
2Vd
]

例如：

```text
V = 50000
d = 4096
```

单个 embedding 参数量：

[
50000 \times 4096
=================

204,800,000
]

约 2.048 亿参数。

---

## 较小的词表

优点：

* embedding 和输出层更小。
* token 出现频次更高。
* 对构词变化具有更强的共享能力。

缺点：

* 文本序列更长。
* Transformer 注意力计算更昂贵。
* 单个词可能被拆得很碎。

---

# 十六、BPE 的时间复杂度

设：

* 当前训练 token 总数为 (N)。
* merge 次数为 (M)。

上面的朴素实现每轮都会：

1. 扫描全部 token。
2. 统计全部 pair。
3. 再扫描全部 token 执行 merge。

大约为：

[
O(MN)
]

随着合并进行，(N) 会逐渐减小，但大语料上仍然很慢。

编码一个长度为 (L) 的序列时，朴素实现反复扫描 pair，最坏情况接近：

[
O(L^2)
]

生产级实现通常使用：

* pair 到出现位置的倒排索引。
* 链表保存 token 邻接关系。
* 优先队列保存 pair rank。
* 只更新受本轮 merge 影响的局部 pair。
* Rust 或 C++ 实现核心循环。
* 并行预分词和批处理。

---

# 十七、常见错误

## 错误 1：没有乘词频

错误统计：

```text
每个不同单词只统计一次
```

正确统计：

```text
pair 出现次数 × 单词出现次数
```

`low` 出现 1000 次时，它内部的 pair 应贡献 1000 次。

---

## 错误 2：编码新文本时重新选最高频 pair

编码阶段必须使用训练好的 merge rank，不能根据当前句子重新学习。

---

## 错误 3：忽略重叠合并

```text
A A A
```

合并 `(A,A)` 的结果是：

```text
AA A
```

不是两个重叠的 `AA`。

---

## 错误 4：训练时和推理时使用不同预分词器

训练时：

```python
text.lower().split()
```

推理时：

```python
text.split()
```

会产生不一致行为。

大小写处理、Unicode 规范化和空白处理都必须固定。

---

## 错误 5：修改词表后继续使用旧模型

token ID 与 embedding 行是一一对应的。任何 token ID 变化都会破坏模型。

---

## 错误 6：认为 BPE 一定找到全局最优词表

BPE 是贪心算法：

```text
每次只选择当前频率最高的 pair
```

它不会回溯，也不保证找到全局最优分词。

---

## 错误 7：把“最长匹配”直接等同于 BPE

BPE 编码的依据是 merge rank。

最长匹配在某些词表中可能产生相同结果，但它不是 BPE 的严格定义。存在 merge 依赖时，盲目最长匹配可能得到不同分词。

---

# 十八、BPE、WordPiece 和 Unigram 的区别

| 方法        | 核心思想                   |
| --------- | ---------------------- |
| BPE       | 每次合并最高频相邻 pair         |
| WordPiece | 选择更有利于语言模型或似然目标的子词     |
| Unigram   | 从大词表开始，逐渐删除贡献较小的 token |
| 字符级       | 每个字符都是 token           |
| 字节级       | 每个字节是初始 token          |

BPE 是：

```text
从小词表开始，不断增加 token
```

Unigram 是：

```text
从大候选词表开始，不断删除 token
```

---

# 十九、完整心智模型

可以把 BPE 记成下面四句话：

### 训练

```text
找到训练语料中最常出现的相邻 token 对，
把它变成一个新 token，
重复很多次。
```

### 编码

```text
从字符或字节开始，
严格按照训练时的 merge 优先级合并。
```

### 解码

```text
把每个 token ID 对应的字符或字节拼回来。
```

### 与模型耦合

```text
BPE 决定 token ID；
token ID 决定 embedding 的索引；
模型预测的也是同一词表中的 token ID。
```

最关键的三个概念是：

1. **pair frequency**：决定训练时学什么。
2. **merge rank**：决定推理时先合并什么。
3. **稳定的 token ID**：保证 tokenizer 与模型参数一一对应。

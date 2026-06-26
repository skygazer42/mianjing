# Token

## 一句话定位

Token 是模型处理文本时的基本离散单元。原始字符串需要先经过 tokenizer 切分成 token，再映射成 token id 和 embedding 向量。

## 面试题总览

下面先放 `01-30` 的题目总表。  
当前这一页只详细展开 `01-05`，后面的题后续再逐步补充。

### 基础概念（01-10）

1. token、word、character 三者分别是什么？
2. 为什么同一句话在不同模型里 token 数可能不同？
3. token 数量为什么会影响训练吞吐、上下文长度和推理成本？
4. token 和 embedding 的关系是什么？
5. 中文、英文、代码的 tokenization 难点分别在哪里？
6. 一个模型的词表（vocab）是怎么设计出来的？
7. special token 有哪些，分别起什么作用？
8. 为什么大模型常说“上下文长度是 8k、32k、128k token”，而不是字符数？
9. token 太细和 token 太粗各有什么问题？
10. token 数和显存占用、attention 复杂度之间是什么关系？

### Tokenizer 设计（11-20）

11. 训练语料变化会不会影响 tokenizer 效果？为什么？
12. 为什么中文常常看起来“字少，但 token 不一定少”？
13. 为什么同一个句子在 GPT、BERT、LLaMA 这类模型上的 token 数可能差很多？
14. 如果新增领域词汇，应该改 tokenizer 还是只做微调？
15. tokenization 错了会对检索、分类、生成分别造成什么影响？
16. 为什么 LLM 更偏向 subword tokenization，而不是纯 character-level 或纯 word-level？
17. 请你用 3 句话解释 BPE 的训练过程。
18. BPE、WordPiece、Unigram、SentencePiece 的核心区别分别是什么？
19. WordPiece 为什么会出现 `[UNK]`，而 BPE 往往还能继续拆？
20. tokenizer 里的 normalization 和 pre-tokenization 分别在做什么？为什么重要？

### 工程与应用（21-30）

21. 为什么有些 tokenizer 是可逆的，而有些不是严格可逆的？
22. padding 和 truncation 分别是什么？为什么对 batch 训练和推理很重要？
23. 为什么英文、中文、阿拉伯语在同一个模型里的 token 成本可能差很多？
24. 为什么空格、标点、缩进、换行在 tokenizer 里也很重要？
25. 代码模型的 tokenizer 和通用文本 tokenizer，设计重点有什么不同？
26. 什么是 byte-level BPE？它相比普通子词切分的优缺点是什么？
27. 怎么判断一个 tokenizer 设计得好不好？你会看哪些指标？
28. 什么情况下值得为垂直领域重新训练 tokenizer？
29. 什么是 OOV（未登录词）问题？subword tokenization 是怎么缓解它的？
30. tokenizer 的词表大小和模型规模之间通常是什么关系？为什么不能无脑把词表做得特别大？

## 问题 01-05 详细解读

### 01. token、word、character 三者分别是什么？

答：

- `character` 是按字符切分，比如英文里的字母、中文里的单字。
- `word` 是按词切分，英文里通常以空格为天然边界，中文则没有这么直接。
- `token` 是 tokenizer 最终输出给模型的离散单元，它不一定等于一个词，也不一定等于一个字。

面试里最稳妥的说法是：`token` 是“模型视角下的基本文本单位”。

### 02. 为什么同一句话在不同模型里 token 数可能不同？

答：

- 不同模型使用的 tokenizer 不同。
- 词表大小、训练语料、切分策略也可能不同。
- 有的模型更倾向保留高频整词，有的模型更倾向拆成多个子词。

所以同一句话在 GPT、BERT、LLaMA 这类模型里，token 数可能明显不同。

### 03. token 数量为什么会影响训练吞吐、上下文长度和推理成本？

答：

- 模型的计算是按 token 序列展开的，不是按字符数展开的。
- token 越多，序列越长，训练时单个 batch 的总计算量就越大。
- 在推理阶段，token 变多也会直接拉高 attention 和 KV cache 的成本。

所以上下文长度、吞吐和 API 计费，通常都更关心 token 数，而不是字符数。

### 04. token 和 embedding 的关系是什么？

答：

- token 先被映射成 token id。
- token id 再通过 embedding 矩阵查表，变成向量表示。

因此：

- token 是离散符号
- embedding 是连续向量

一句话说，就是“token 是输入单位，embedding 是它的向量表示”。

### 05. 中文、英文、代码的 tokenization 难点分别在哪里？

答：

- 中文的问题是天然没有空格边界，切词本身就更难。
- 英文的问题是词形变化、复合词和长尾词比较多。
- 代码的问题是符号多、格式敏感，还包含变量名、缩进、换行和混合命名风格。

所以同一个 tokenizer 在中文、英文和代码场景下，往往不会同时达到最优效果。

## 原理剖析

- 模型不能直接吃字符串，必须先把文本切分成更稳定的离散单元。
- token 设计本质是在做折中：词表越大，单个 token 表达越强，但 embedding 矩阵更大。
- token 越细，序列越长，attention 成本越高。
- 同一个词在不同上下文里可以被切成不同 token 组合，这也是不同 tokenizer 表现差异的来源。

## 极简实现

```python
import re

def simple_tokenize(text: str) -> list[str]:
    text = text.lower().strip()
    return re.findall(r"\w+|[^\w\s]", text)


text = "Hello, Token!"
tokens = simple_tokenize(text)
print(tokens)  # ['hello', ',', 'token', '!']
```

这个实现只是演示“先切分，再编码”的基本思路，不等于生产级 tokenizer。

## 继续追问

1. 如果 tokenizer 改了，原来的 embedding 能不能直接复用？
2. 为什么大模型里 token 数往往直接决定 API 价格？
3. 为什么代码模型通常会有更适合代码语料的 tokenizer？

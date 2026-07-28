# Token 高频面试题（30 题）

## 一句话定位

Token 是 tokenizer 根据词表和规则得到的离散文本单元。原始字符串经过规范化、切分和词表映射成为 token id，再通过 embedding 变成模型可计算的连续向量。

本目录按“基础概念—设计原理—工程应用”整理 30 道高频题。每道题都链接到独立答案，适合逐题复习和继续追问。

## 基础概念（01–10）

1. [token、word、character 三者分别是什么？](./01.token、word、character三者分别是什么.md)
2. [为什么同一句话在不同模型里 token 数可能不同？](./02.为什么同一句话在不同模型里token数可能不同.md)
3. [token 数量为什么会影响训练吞吐、上下文长度和推理成本？](./03.token数量为什么会影响训练吞吐、上下文长度和推理成本.md)
4. [token 和 embedding 的关系是什么？](./04.token和embedding的关系是什么.md)
5. [中文、英文、代码的 tokenization 难点分别在哪里？](./05.中文、英文、代码的tokenization难点分别在哪里.md)
6. [一个模型的词表（vocab）是怎么设计出来的？](./06.一个模型的词表vocab是怎么设计出来的.md)
7. [special token 有哪些，分别起什么作用？](./07.special-token有哪些分别起什么作用.md)
8. [为什么大模型常说“上下文长度是 8k、32k、128k token”，而不是字符数？](./08.为什么上下文长度用token而不是字符数.md)
9. [token 太细和 token 太粗各有什么问题？](./09.token太细和token太粗各有什么问题.md)
10. [token 数和显存占用、attention 复杂度之间是什么关系？](./10.token数和显存占用attention复杂度之间是什么关系.md)

## Tokenizer 设计与算法（11–20）

11. [训练语料变化会不会影响 tokenizer 效果？为什么？](./11.训练语料变化会不会影响tokenizer效果.md)
12. [为什么中文常常看起来“字少，但 token 不一定少”？](./12.为什么中文字符少但token不一定少.md)
13. [BERT、GPT 和 LLaMA 的 tokenizer 设计有什么典型差异？](./13.BERT、GPT和LLaMA的tokenizer设计有什么典型差异.md)
14. [如果新增领域词汇，应该改 tokenizer 还是只做微调？](./14.新增领域词汇应改tokenizer还是微调.md)
15. [tokenization 错了会对检索、分类、生成分别造成什么影响？](./15.tokenization错误对检索分类生成的影响.md)
16. [为什么 LLM 更偏向 subword tokenization，而不是纯 character-level 或纯 word-level？](./16.为什么LLM偏向subword-tokenization.md)
17. [请用三句话解释 BPE 的训练过程？](./17.三句话解释BPE训练过程.md)
18. [BPE、WordPiece、Unigram、SentencePiece 的核心区别分别是什么？](./18.BPE、WordPiece、Unigram、SentencePiece的区别.md)
19. [WordPiece 为什么会出现 `[UNK]`，而 BPE 往往还能继续拆？](./19.WordPiece为什么会出现UNK而BPE能继续拆.md)
20. [tokenizer 里的 normalization 和 pre-tokenization 分别在做什么？为什么重要？](./20.normalization和pre-tokenization分别做什么.md)

## 工程与应用（21–30）

21. [为什么有些 tokenizer 是可逆的，而有些不是严格可逆的？](./21.为什么有些tokenizer可逆有些不严格可逆.md)
22. [padding 和 truncation 分别是什么？为什么对 batch 训练和推理很重要？](./22.padding和truncation分别是什么.md)
23. [为什么英文、中文、阿拉伯语在同一个模型里的 token 成本可能差很多？](./23.为什么不同语言token成本不同.md)
24. [为什么空格、标点、缩进、换行在 tokenizer 里也很重要？](./24.为什么空格标点缩进换行重要.md)
25. [代码模型的 tokenizer 和通用文本 tokenizer，设计重点有什么不同？](./25.代码模型和通用文本tokenizer的设计重点.md)
26. [什么是 byte-level BPE？它相比普通子词切分有什么优缺点？](./26.什么是byte-level-BPE.md)
27. [怎么判断一个 tokenizer 设计得好不好？应该看哪些指标？](./27.怎么判断tokenizer设计得好不好.md)
28. [什么情况下值得为垂直领域重新训练 tokenizer？](./28.什么情况下值得重训垂直领域tokenizer.md)
29. [什么是 OOV（未登录词）？subword tokenization 如何缓解它？](./29.什么是OOV以及subword如何缓解.md)
30. [tokenizer 的词表大小和模型规模有什么关系？为什么不能无脑增大词表？](./30.词表大小和模型规模有什么关系.md)

## 补充材料

- [Tokenizer 算法总览](./13.aTokenizer（分词器）算法.md)
- [词表与 tokenization 的区别图](./16.a.词表、tokenization区别.png)
- [Attention 计算深挖](<./10.a 深度理解attention计算.md>)
- [专题研究报告](./deep-research-report.md)

## 推荐复习方式

第一遍只看每题的“结论先行”和“面试回答要点”；第二遍手算 BPE、长度和显存公式；第三遍用目标模型的真实 tokenizer 验证中文、英文、代码、空白和特殊 token。面试回答时先给结论，再解释机制、取舍和工程验证方法。

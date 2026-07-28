# Unigram 高频面试题

Unigram 是概率化子词模型：在切分 lattice 上学习 piece 概率，并从大候选词表逐步剪枝。以下 30 题覆盖概率原理、训练算法、采样与工程部署。

## 基础概念（01-10）

1. [Unigram tokenizer 是什么？](./01.Unigram-tokenizer是什么.md)
2. [Unigram 为什么叫“一元语言模型”？](./02.Unigram为什么叫一元语言模型.md)
3. [什么是 Unigram 分词 lattice？](./03.什么是Unigram分词lattice.md)
4. [Viterbi 如何求 Unigram 最优切分？](./04.Viterbi如何求Unigram最优切分.md)
5. [前向算法如何计算所有切分的总概率？](./05.前向算法如何计算所有切分的总概率.md)
6. [Unigram 初始大候选词表如何构造？](./06.Unigram初始大候选词表如何构造.md)
7. [EM 如何训练 Unigram 子词概率？](./07.EM如何训练Unigram子词概率.md)
8. [Unigram 如何评估删除一个 token 的损失？](./08.Unigram如何评估删除一个token的损失.md)
9. [Required chars 和 UNK 如何保证 Unigram 可分？](./09.required-chars和UNK如何保证Unigram可分.md)
10. [SentencePiece 与 Unigram 是什么关系？](./10.SentencePiece与Unigram是什么关系.md)

## 训练与算法原理（11-20）

11. [Unigram 语料似然公式如何推导？](./11.Unigram语料似然公式如何推导.md)
12. [Unigram 与 BPE“从大到小”和“从小到大”有何本质差别？](./12.Unigram与BPE从大到小和从小到大有何本质差别.md)
13. [Unigram 与 WordPiece 的概率和贪心差异是什么？](./13.Unigram与WordPiece的概率和贪心差异是什么.md)
14. [N-best 分词如何从 Unigram lattice 中得到？](./14.n-best分词如何从Unigram-lattice中得到.md)
15. [Unigram 如何进行 subword regularization 采样？](./15.Unigram如何进行subword-regularization采样.md)
16. [Unigram tokenizer 和神经语言模型有什么区别？](./16.Unigram-tokenizer和神经语言模型有什么区别.md)
17. [空格元符号和 normalization 如何影响 Unigram？](./17.空格元符号和normalization如何影响Unigram.md)
18. [多语言 Unigram 语料如何采样？](./18.多语言Unigram语料如何采样.md)
19. [Unigram 词表大小和剪枝比例如何选择？](./19.Unigram词表大小和剪枝比例如何选择.md)
20. [Unigram 训练和推理复杂度是多少？](./20.Unigram训练和推理复杂度是多少.md)

## 工程与场景（21-30）

21. [如何训练并发布生产级 Unigram tokenizer？](./21.如何训练并发布生产级Unigram-tokenizer.md)
22. [如何实现一个最小可用 Unigram Viterbi 分词器？](./22.如何实现一个最小可用Unigram-Viterbi分词器.md)
23. [Log-sum-exp 为什么是 Unigram 训练关键？](./23.log-sum-exp为什么是Unigram训练关键.md)
24. [Unigram 解码可逆性和 offset 有哪些陷阱？](./24.Unigram解码可逆性和offset有哪些陷阱.md)
25. [如何系统评估 Unigram tokenizer？](./25.如何系统评估Unigram-tokenizer.md)
26. [剪枝后罕见字符消失如何排查？](./26.剪枝后罕见字符消失如何排查.md)
27. [随机分词如何保证可复现且不降低吞吐？](./27.随机分词如何保证可复现且不降低吞吐.md)
28. [垂直领域如何适配 Unigram 词表？](./28.垂直领域如何适配Unigram词表.md)
29. [随机子词正则化何时有效，何时有害？](./29.随机子词正则化何时有效何时有害.md)
30. [什么场景适合 Unigram，以及关键参数怎么调？](./30.什么场景适合Unigram以及关键参数怎么调.md)

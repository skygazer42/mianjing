# WordPiece 高频面试题

WordPiece 是 BERT 系列常见的子词方法。以下 30 题覆盖经典 BERT 管线、训练思想、MaxMatch 推理、性能与生产兼容。

## 基础概念（01-10）

1. [WordPiece 是什么，以及为什么 BERT 使用它？](./01.WordPiece是什么以及为什么BERT使用它.md)
2. [WordPiece 中的 ## 前缀表示什么？](./02.WordPiece中的井号前缀表示什么.md)
3. [WordPiece 的基础词表如何保证覆盖？](./03.WordPiece的基础词表如何保证覆盖.md)
4. [WordPiece 最长匹配算法如何工作？](./04.WordPiece最长匹配算法如何工作.md)
5. [BasicTokenizer 与 WordPieceTokenizer 如何分工？](./05.BasicTokenizer与WordPieceTokenizer如何分工.md)
6. [WordPiece 如何处理中文和无空格语言？](./06.WordPiece如何处理中文和无空格语言.md)
7. [Lowercase 和去重音如何影响 WordPiece？](./07.lowercase和去重音如何影响WordPiece.md)
8. [WordPiece 词表大小如何影响序列和模型参数？](./08.WordPiece词表大小如何影响序列和模型参数.md)
9. [WordPiece 子词边界是否等于语言学词素边界？](./09.WordPiece子词边界是否等于语言学词素边界.md)
10. [WordPiece 编码、解码与 offset 如何对应？](./10.WordPiece编码解码与offset如何对应.md)

## 训练与算法原理（11-20）

11. [WordPiece 训练目标为什么不能简单说成最高频合并？](./11.WordPiece训练目标为什么不能简单说成最高频合并.md)
12. [频率归一化评分如何理解 WordPiece 候选？](./12.频率归一化评分如何理解WordPiece候选.md)
13. [从语料训练 WordPiece 词表通常有哪些步骤？](./13.从语料训练WordPiece词表通常有哪些步骤.md)
14. [为什么一个字符缺失可能让整个词变成 [UNK]？](./14.为什么一个字符缺失可能让整个词变成UNK.md)
15. [MaxMatch 的复杂度与 Trie 优化是什么？](./15.MaxMatch复杂度与Trie优化是什么.md)
16. [WordPiece 候选剪枝为何重要？](./16.WordPiece候选剪枝为何重要.md)
17. [WordPiece 与 BPE 在训练和推理上如何系统比较？](./17.WordPiece与BPE在训练和推理上如何系统比较.md)
18. [WordPiece 与 Unigram 的搜索方式有什么区别？](./18.WordPiece与Unigram的搜索方式有什么区别.md)
19. [Whole Word Masking 与 WordPiece 是什么关系？](./19.Whole-Word-Masking与WordPiece是什么关系.md)
20. [多语言 WordPiece 为何容易出现词表竞争？](./20.多语言WordPiece为何容易出现词表竞争.md)

## 工程与场景（21-30）

21. [如何实现一个可验证的 WordPiece 编码器？](./21.如何实现一个可验证的WordPiece编码器.md)
22. [生产级 WordPiece 如何用 Trie 和缓存提速？](./22.生产级WordPiece如何用Trie和缓存提速.md)
23. [WordPiece 出现大量 [UNK] 如何定位和修复？](./23.WordPiece出现大量UNK如何定位和修复.md)
24. [如何给 BERT 添加领域 WordPiece 词汇？](./24.如何给BERT添加领域WordPiece词汇.md)
25. [哪些指标能评估 WordPiece 的碎片化程度？](./25.哪些指标能评估WordPiece的碎片化程度.md)
26. [Normalization 后的 offset 错位如何解决？](./26.normalization后的offset错位如何解决.md)
27. [如何保证训练、服务和移动端 WordPiece 一致？](./27.如何保证训练服务和移动端WordPiece一致.md)
28. [超长单词为什么可能造成 WordPiece 性能问题？](./28.超长单词为什么可能造成WordPiece性能问题.md)
29. [WordPiece 对分类、检索和生成任务影响有何不同？](./29.WordPiece对分类检索和生成任务影响有何不同.md)
30. [什么场景适合 WordPiece，以及何时不该更换它？](./30.什么场景适合WordPiece以及何时不该更换它.md)

# BPE 高频面试题

BPE（Byte Pair Encoding）以高频相邻符号对的贪心合并学习子词词表。下面 30 题按基础、训练原理与工程实践组织，每题均可独立复习。

## 基础概念（01-10）

1. [BPE 是什么，以及它解决了什么问题？](./01.BPE是什么以及它解决了什么问题.md)
2. [压缩算法 BPE 与 NLP 中的 BPE 有什么关系？](./02.压缩算法BPE与NLP中的BPE有什么关系.md)
3. [BPE 的初始符号为什么可以是字符或字节？](./03.BPE的初始符号为什么可以是字符或字节.md)
4. [预分词和词边界如何影响 BPE？](./04.预分词和词边界如何影响BPE.md)
5. [BPE 词表、merge 规则和 merge rank 分别是什么？](./05.BPE词表merge规则和merge-rank分别是什么.md)
6. [BPE 训练时相邻对频次如何统计？](./06.BPE训练时相邻对频次如何统计.md)
7. [BPE 遇到重叠 pair 和频次并列时如何处理？](./07.BPE遇到重叠pair和频次并列时如何处理.md)
8. [BPE 如何用固定 merge rank 编码新文本？](./08.BPE如何用固定merge-rank编码新文本.md)
9. [BPE 解码为什么通常可逆，又可能不严格可逆？](./09.BPE解码为什么通常可逆又可能不严格可逆.md)
10. [BPE 如何缓解 OOV，以及 byte-level 为何几乎没有 UNK？](./10.BPE如何缓解OOV以及byte-level为何几乎没有UNK.md)

## 训练与算法原理（11-20）

11. [BPE 的贪心目标是什么，以及它是全局最优吗？](./11.BPE的贪心目标是什么以及它是全局最优吗.md)
12. [BPE 的词表大小和 merge 次数如何决定？](./12.词表大小和merge次数如何决定.md)
13. [Byte-level BPE 如何处理 UTF-8 文本？](./13.byte-level-BPE如何处理UTF8文本.md)
14. [GPT-2 式字节到 Unicode 映射为什么存在？](./14.GPT2式字节到Unicode映射为什么存在.md)
15. [BPE 和 WordPiece 的核心区别是什么？](./15.BPE和WordPiece核心区别是什么.md)
16. [BPE 和 Unigram 的核心区别是什么？](./16.BPE和Unigram核心区别是什么.md)
17. [BPE-dropout 是什么，以及为什么能做子词正则化？](./17.BPE-dropout是什么以及为什么能做子词正则化.md)
18. [BPE 训练和编码的时间复杂度如何优化？](./18.BPE训练和编码的时间复杂度如何优化.md)
19. [大规模 BPE 训练如何并行化并保持确定性？](./19.大规模BPE训练如何并行化并保持确定性.md)
20. [Normalization 变化为什么会让 BPE 模型失效？](./20.normalization变化为什么会让BPE模型失效.md)

## 工程与场景（21-30）

21. [如何从零训练并发布一个生产级 BPE tokenizer？](./21.如何从零训练并发布一个生产级BPE-tokenizer.md)
22. [多语言和领域语料如何采样，避免 BPE 词表失衡？](./22.多语言和领域语料如何采样避免词表失衡.md)
23. [如何系统评估 BPE tokenizer 质量？](./23.如何系统评估BPE-tokenizer质量.md)
24. [BPE 训练与推理分词不一致如何排查？](./24.训练与推理分词不一致如何排查.md)
25. [已有模型如何扩展 BPE 词表？](./25.已有模型如何扩展BPE词表.md)
26. [特殊 token 与普通 BPE 合并应如何协调？](./26.特殊token与普通BPE合并应如何协调.md)
27. [流式 BPE 编码和 offset mapping 有哪些难点？](./27.流式BPE编码和offset-mapping有哪些难点.md)
28. [代码场景的 BPE 应该重点优化什么？](./28.代码场景的BPE应该重点优化什么.md)
29. [如何防御 token 膨胀和分词拒绝服务？](./29.如何防御token膨胀和分词拒绝服务.md)
30. [什么场景适合选择 BPE，以及如何调参？](./30.什么场景适合选择BPE以及如何调参.md)

## 动手实现

完成概念题后，可继续运行 [从零实现 BPE Tokenizer](../engineering-practice/01-bpe-tokenizer-from-scratch.ipynb)：它覆盖确定性训练、按 merge rank 编码、可逆解码、特殊 token、序列化、复杂度分析和契约测试。

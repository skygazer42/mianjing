# Embedding 高频面试题

Embedding 把离散符号或完整样本映射到连续向量空间。面试中既要讲清输入词表查表、输出 softmax 与权重共享，也要能讨论句向量训练、向量度量、近似最近邻索引和线上评估。

## 基础概念（01-10）

1. [one-hot 和 embedding 有什么区别？](./01.one-hot和embedding有什么区别.md)
2. [Embedding 矩阵的形状、查表和 one-hot 乘法如何对应？](./02.Embedding矩阵的形状查表和one-hot乘法如何对应.md)
3. [为什么训练后语义相近的 token embedding 往往更接近？](./03.为什么训练后语义相近的token-embedding往往更接近.md)
4. [Embedding 参数如何训练，反向传播时哪些行会收到梯度？](./04.Embedding参数如何训练反向传播时哪些行会收到梯度.md)
5. [Token embedding、词向量和上下文化表示有什么区别？](./05.Token-embedding词向量和上下文化表示有什么区别.md)
6. [为什么有些 Transformer 会缩放或归一化输入 embedding？](./06.为什么有些Transformer会缩放或归一化输入embedding.md)
7. [PAD、UNK、BOS 等特殊 token 的 embedding 应如何处理？](./07.PAD-UNK-BOS等特殊token的embedding应如何处理.md)
8. [词表大小如何影响 embedding 的参数量、显存和计算？](./08.词表大小如何影响embedding的参数量显存和计算.md)
9. [余弦相似度、点积和欧氏距离用于向量比较时有何区别？](./09.余弦相似度点积和欧氏距离用于向量比较时有何区别.md)
10. [Word2Vec、GloVe、FastText 与 LLM embedding 有什么区别？](./10.Word2Vec-GloVe-FastText与LLM-embedding有什么区别.md)

## 原理与训练（11-20）

11. [输入 embedding 和输出权重共享是什么，为什么有效？](./11.输入embedding和输出权重共享是什么为什么有效.md)
12. [权重共享有哪些限制，何时不应该共享输入输出 embedding？](./12.权重共享有哪些限制何时不应该共享输入输出embedding.md)
13. [输出 embedding、词表 softmax 和语言模型损失如何连接？](./13.输出embedding词表softmax和语言模型损失如何连接.md)
14. [扩充或替换词表后怎样初始化并训练新增 embedding？](./14.扩充或替换词表后怎样初始化并训练新增embedding.md)
15. [Embedding 维度如何选择，它与秩、容量和模型宽度有何关系？](./15.Embedding维度如何选择它与秩容量和模型宽度有何关系.md)
16. [负采样、层次 softmax 和 sampled softmax 为什么能加速训练？](./16.负采样层次softmax和sampled-softmax为什么能加速训练.md)
17. [什么是 embedding 各向异性、hubness 和表示坍塌？](./17.什么是embedding各向异性hubness和表示坍塌.md)
18. [向量做 L2 归一化会怎样改变训练、相似度和检索结果？](./18.向量做L2归一化会怎样改变训练相似度和检索结果.md)
19. [对比学习如何训练句向量，温度系数和负样本有什么作用？](./19.对比学习如何训练句向量温度系数和负样本有什么作用.md)
20. [CLS、mean、max 和 last-token pooling 应如何选择？](./20.CLS-mean-max和last-token-pooling应如何选择.md)

## 工程与评估（21-30）

21. [向量检索中如何选择相似度函数并保证训练与索引一致？](./21.向量检索中如何选择相似度函数并保证训练与索引一致.md)
22. [HNSW、IVF 和 PQ 的原理及取舍是什么？](./22.HNSW-IVF和PQ的原理及取舍是什么.md)
23. [Embedding 量化会怎样影响存储、吞吐和召回率？](./23.Embedding量化会怎样影响存储吞吐和召回率.md)
24. [如何构造 hard negative，并处理假负样本和批内偏差？](./24.如何构造hard-negative并处理假负样本和批内偏差.md)
25. [怎样离线和在线评估一个 embedding 模型？](./25.怎样离线和在线评估一个embedding模型.md)
26. [领域微调 embedding 时如何避免灾难性遗忘和表示坍塌？](./26.领域微调embedding时如何避免灾难性遗忘和表示坍塌.md)
27. [多语言 embedding 如何对齐，不同语言表现不均衡怎么办？](./27.多语言embedding如何对齐不同语言表现不均衡怎么办.md)
28. [如何排查 embedding 的 NaN、范数异常、低区分度和频率偏置？](./28.如何排查embedding的NaN范数异常低区分度和频率偏置.md)
29. [Embedding 服务如何做缓存、版本管理、批处理和一致性校验？](./29.Embedding服务如何做缓存版本管理批处理和一致性校验.md)
30. [面对分类、聚类、去重和检索场景，如何选择 embedding 方案？](./30.面对分类聚类去重和检索场景如何选择embedding方案.md)

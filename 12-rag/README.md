# RAG 高频面试题（30 题）

## 一句话定位

RAG（Retrieval-Augmented Generation）在生成前从可更新、可授权的外部知识源检索证据，让模型基于上下文回答；系统质量由摄取、切块、索引、召回、重排、上下文组装和生成共同决定。

## 基础流程与检索（01–10）

1. [RAG 是什么，主要解决什么问题？](./01.RAG是什么主要解决什么问题.md)
2. [RAG、微调和长上下文分别如何选择？](./02.RAG微调和长上下文分别如何选择.md)
3. [一个生产级 RAG 的完整链路是什么？](./03.一个生产级RAG完整链路是什么.md)
4. [稀疏检索和稠密检索有什么区别？](./04.稀疏检索和稠密检索有什么区别.md)
5. [chunk size 和 overlap 如何选择？](./05.chunk-size和overlap如何选择.md)
6. [embedding 模型如何选择和评估？](./06.embedding模型如何选择和评估.md)
7. [检索 top-k 越大越好吗？](./07.top-k越大越好吗.md)
8. [reranker 为什么有效，应该放在哪里？](./08.reranker为什么有效应该放在哪里.md)
9. [混合检索和 RRF 如何工作？](./09.混合检索和RRF如何工作.md)
10. [metadata filter 如何设计？](./10.metadata-filter如何设计.md)

## 召回增强与上下文构建（11–20）

11. [query rewrite、query expansion 和 HyDE 分别解决什么问题？](./11.query-rewrite-expansion-HyDE分别解决什么问题.md)
12. [多查询分解和多跳检索如何实现？](./12.多查询分解和多跳检索如何实现.md)
13. [parent-child retrieval 和 contextual chunking 有什么用？](./13.parent-child和contextual-chunking有什么用.md)
14. [HNSW 和 IVF 索引如何影响召回、延迟与内存？](./14.HNSW和IVF索引如何影响召回延迟内存.md)
15. [如何做去重、排序与上下文组装？](./15.如何做去重排序与上下文组装.md)
16. [RAG 如何提供可核验引用和溯源？](./16.RAG如何提供可核验引用和溯源.md)
17. [有检索上下文，为什么仍然会产生幻觉？](./17.有检索上下文为什么仍会幻觉.md)
18. [embedding 模型升级后，索引如何迁移？](./18.embedding升级后索引如何迁移.md)
19. [SQL 和知识图谱何时优于向量检索？](./19.SQL和知识图谱何时优于向量检索.md)
20. [GraphRAG 适合什么问题，代价是什么？](./20.GraphRAG适合什么问题代价是什么.md)

## 评估、安全与生产化（21–30）

21. [RAG 评估需要哪些检索、生成与端到端指标？](./21.RAG评估需要哪些检索与生成指标.md)
22. [如何构建 RAG 评测集，以及怎样使用 LLM-as-judge？](./22.如何构建RAG评测集以及使用LLM-as-judge.md)
23. [如何区分召回失败、重排失败和生成失败？](./23.如何区分召回失败重排失败和生成失败.md)
24. [多租户 RAG 如何做权限过滤？](./24.多租户RAG如何做权限过滤.md)
25. [如何防御提示注入和知识库投毒？](./25.如何防御提示注入和知识库投毒.md)
26. [知识库如何增量更新、删除并保证新鲜度？](./26.知识库如何增量更新删除与保证新鲜度.md)
27. [RAG 如何做缓存、降低延迟并控制成本？](./27.RAG如何做缓存降延迟和控成本.md)
28. [多模态 RAG 有哪些特殊难点？](./28.多模态RAG有哪些特殊难点.md)
29. [Agentic RAG 和迭代检索是什么？](./29.Agentic-RAG和迭代检索是什么.md)
30. [如何设计可观测、可回归的生产级 RAG 系统？](./30.如何设计可观测可回归的生产级RAG系统.md)

## 推荐复习方式

把 RAG 看成一条可测量的数据与请求流水线：先画清离线摄取和在线查询，再为每一阶段定义输入输出、指标和失败样例。面试回答应能区分“没有召回证据”“证据排序错误”和“模型没有忠实使用证据”。

## 工程实践

- [关键词搜索与 BM25](../engineering-practice/02-keyword-search-bm25.ipynb)：从 analyzer、倒排索引和打分解释做到过滤、更新与评估。
- [RAG 中的关键词召回](../engineering-practice/03-rag-keyword-retrieval.ipynb)：把版本、ACL、多字段召回、引用和故障 trace 串成完整链路。
- [知识图谱与 KG-RAG](../engineering-practice/05-knowledge-graph.ipynb)：实现 schema、实体归一、多跳查询和证据子图。
- [混合检索、重排与评估](../engineering-practice/06-hybrid-search-rerank-evaluation.ipynb)：实现 sparse+dense、RRF、重排、指标与超时降级。

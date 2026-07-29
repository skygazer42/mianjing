# 面试系统题：一题一本，从底层实现

本目录把常见的开放式面试题拆成独立中文 Notebook。每本围绕一个问题，从需求澄清、输入输出合同、数据结构、核心算法、复杂度、离线评估、线上失败模式到版本化发布逐层展开；实现主要使用 Python 标准库、NumPy 和 PyTorch 基础算子，不用搜索引擎、ANN、排序、实验平台等高耦合框架直接给出答案。

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | 面试问题 | Notebook |
| --- | --- | --- |
| 01 | 你会怎样设计支持短语、字段、删除和增量更新的倒排索引？ | [增量倒排索引](./01-inverted-index-incremental-search-from-scratch.ipynb) |
| 02 | IVF-PQ 向量检索怎么从零实现，召回率和成本怎样权衡？ | [IVF-PQ](./02-ivf-pq-vector-search-from-scratch-numpy.ipynb) |
| 03 | HNSW 为什么快，插入、搜索、删除和参数怎样实现？ | [HNSW](./03-hnsw-ann-search-from-scratch-numpy.ipynb) |
| 04 | 搜索拼写纠错与 Query Rewrite 应该怎样设计？ | [拼写纠错](./04-spell-correction-query-rewrite-from-scratch.ipynb) |
| 05 | 海量文本近重复检测怎样用 MinHash 与 LSH 实现？ | [MinHash/LSH](./05-minhash-lsh-near-duplicate-from-scratch.ipynb) |
| 06 | Learning to Rank 中 LambdaRank 怎样从指标推到梯度？ | [LambdaRank](./06-learning-to-rank-lambdarank-from-scratch-pytorch.ipynb) |
| 07 | Feature Store 怎样做 Point-in-Time Join，避免特征穿越？ | [Point-in-Time Join](./07-feature-store-point-in-time-join-from-scratch.ipynb) |
| 08 | 点击日志有位置偏差时，怎样做 IPS/SNIPS 反事实排序？ | [点击偏差与 IPS](./08-click-bias-ips-counterfactual-ranking-from-scratch.ipynb) |
| 09 | 海量流中怎样用 Count-Min Sketch 与 Space-Saving 找 Top-K？ | [流式 Top-K](./09-streaming-count-min-sketch-topk-from-scratch.ipynb) |
| 10 | Bloom Filter 为什么能防缓存穿透，删除和扩容怎样处理？ | [Bloom/Counting Filter](./10-bloom-counting-filter-from-scratch.ipynb) |
| 11 | 分类模型的概率校准和业务阈值应该怎样实现与评估？ | [校准与阈值](./11-model-calibration-thresholding-from-scratch-pytorch.ipynb) |
| 12 | 线上 A/B 实验如何处理随机化、CUPED、多指标和提前偷看？ | [A/B 实验](./12-ab-testing-sequential-experiment-from-scratch.ipynb) |

所有示例都使用离线受控数据，只用于验证机制与工程合同，不能把结果外推为真实流量、语料或业务收益。生产实现还需要分布式存储、并发控制、压测、权限、隐私、监控、灰度和回滚。

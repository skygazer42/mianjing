# 图表示学习与几何深度学习

本目录收录三个从基础张量算子开始实现的中文工程 Notebook。它们统一采用 CPU、离线、单线程配置，不依赖 PyG、DGL、gensim、NetworkX Node2Vec、e3nn 或现成 GNN/Transformer 架构。

| 编号 | Notebook | 核心内容 |
|---|---|---|
| 61 | [GraphCL：图对比学习](./61-graphcl-contrastive-learning-from-scratch-pytorch.ipynb) | 图增强合同、GIN、图级池化、多正例 NT-Xent、受控预训练与线性评估 |
| 62 | [Node2Vec：二阶游走与 Skip-Gram](./62-node2vec-skipgram-from-scratch-pytorch.ipynb) | `p/q` 精确转移、可复现游走、过滤式负采样、时间链接与节点评估 |
| 63 | [EGNN：E(n) 等变分子网络](./63-egnn-equivariant-molecular-from-scratch-pytorch.ipynb) | 径向消息、坐标更新、平移/旋转/反射/置换 oracle、属性预测与有限梯度 |

每本 Notebook 都包含公式、shape 和复杂度推导、失败模式、受控训练、训练与推理边界、生产差距、原始论文链接，以及带外发布信任锚。受控数据上的结果只用于证明实现和协议正确，不应解释为真实业务或科学基准的泛化结论。

# 工程实践 Notebooks

这里补充核心专题之外的“系统怎么真正做出来”。每份 notebook 都从接口与数据契约开始，包含可运行实现、断言、评估指标、失败 trace、生产取舍和研究来源，而不是只展示一个库函数调用。

## 运行环境

- Python 3.10+；不同专题按需使用 NumPy、pandas、scikit-learn、SciPy、NetworkX、Pillow、matplotlib 与 PyTorch 2.x，均不需要下载外部数据或模型。
- 在仓库根目录启动 Jupyter 后按编号运行；每份 notebook 都能从空内核独立执行，不依赖上一份 notebook 的变量。
- 示例均使用内置受控小数据，用来验证算法与系统契约，不代表真实业务数据上的效果。

## 第一组：检索、分类与知识系统

| 编号 | Notebook | 核心工程问题 |
| --- | --- | --- |
| 01 | [从零实现 BPE Tokenizer](./01-bpe-tokenizer-from-scratch.ipynb) | 如何训练 merge rules、按 merge rank 编码、可逆解码、序列化、评估与测试？ |
| 02 | [关键词搜索与 BM25](./02-keyword-search-bm25.ipynb) | analyzer、倒排索引、BM25/BM25F、查询语法、过滤、增量更新和相关性评估如何设计？ |
| 03 | [RAG 中的关键词召回](./03-rag-keyword-retrieval.ipynb) | BM25 在 RAG 离线/在线链路放在哪里，怎样处理 ACL、版本、引用、候选预算和故障归因？ |
| 04 | [文档分类工程](./04-document-classification.ipynb) | 标签体系、数据泄漏、TF-IDF baseline、类别不平衡、阈值/校准、OOD、漂移和部署契约怎么做？ |
| 05 | [知识图谱与 KG-RAG](./05-knowledge-graph.ipynb) | schema、实体关系抽取、消歧、溯源、幂等更新、多跳查询、证据子图与权限如何实现？ |
| 06 | [混合检索、重排与评估](./06-hybrid-search-rerank-evaluation.ipynb) | sparse+dense 如何融合，RRF、reranker、Recall/MRR/nDCG、超时降级和 trace 如何串起来？ |

## 第二组：NLP、CV、图学习与跨领域系统

| 编号 | Notebook | 核心工程问题 |
| --- | --- | --- |
| 07 | [NLP 数据质量流水线](./07-nlp-data-quality-pipeline.ipynb) | schema、Unicode、PII、exact/near dedup、文档族切分、质量门禁和漂移怎样实现？ |
| 08 | [NER 与实体链接](./08-ner-entity-linking.ipynb) | BIO/span、重叠实体、候选生成、tenant-scoped 消歧、拒识、指标和增量 KB 如何串联？ |
| 09 | [文本排序与 Hard Negative](./09-text-ranking-hard-negatives.ipynb) | pointwise/pairwise、负例挖掘、false negative、group/time split、MRR/nDCG 与 rerank 服务如何设计？ |
| 10 | [图像分类工程](./10-image-classification-engineering.ipynb) | 图像合同、增强、数据泄漏、baseline、校准、OOD、鲁棒性与批量推理如何落地？ |
| 11 | [目标检测：IoU、NMS 与 mAP](./11-object-detection-iou-nms-map.ipynb) | 坐标变换、匹配、class-aware NMS、Soft-NMS、AP/mAP、ignore/crowd 和后处理版本如何实现？ |
| 12 | [文档 OCR 与版面解析](./12-document-ocr-layout-pipeline.ipynb) | OCR token/box、阅读顺序、多栏、表格、低置信、provenance、CER/WER 与人工复核如何设计？ |
| 13 | [图算法工程](./13-graph-algorithms-engineering.ipynb) | 多重/加权图、BFS/DFS、最短路、PageRank、连通性、动态更新和 tenant 隔离如何实现？ |
| 14 | [GNN 消息传递与节点分类](./14-gnn-message-passing-node-classification.ipynb) | 归一化邻接、message passing、mask、oversmoothing、同配/异配、归纳与传导边界是什么？ |
| 15 | [链接预测与负采样](./15-link-prediction-negative-sampling.ipynb) | 时间边切分、candidate universe、random/hard negative、图特征、Hits/MRR/AUC 和冷启动怎么做？ |
| 16 | [多模态检索](./16-multimodal-retrieval.ipynb) | 双编码器、对称 InfoNCE、双向 Recall/MRR、hard negative、ACL 与向量索引版本如何实现？ |
| 17 | [两阶段推荐系统](./17-recommendation-two-stage.ipynb) | 隐式反馈、时间切分、多路召回、BPR、排序、冷启动、曝光偏差与在线服务如何串联？ |
| 18 | [时序异常检测](./18-time-series-anomaly-detection.ipynb) | 季节基线、MAD、阈值、point/event 指标、漂移、告警合并和流式状态怎么实现？ |

## 第三组：PyTorch 神经网络架构复现

这一组不调用现成网络架构；每本都显式实现 `nn.Module`、`forward`、损失、训练/推理路径和可执行正确性 oracle。小模型与合成数据服务于机制验证，不能把受控过拟合结果解释为真实业务泛化能力。

| 编号 | Notebook | 核心工程问题 |
| --- | --- | --- |
| 19 | [从零实现 RNN、LSTM 与 GRU](./19-rnn-lstm-gru-from-scratch.ipynb) | 三类 recurrent cell 的状态与门控如何手写，变长 mask、分块有状态推理和梯度合同怎样验证？ |
| 20 | [从零实现 Transformer Seq2Seq](./20-transformer-seq2seq-from-scratch.ipynb) | QKV、多头注意力、Encoder/Decoder、causal/padding mask、teacher forcing 与 greedy decode 如何实现？ |
| 21 | [从零实现 BiLSTM-CRF](./21-bilstm-crf-from-scratch.ipynb) | 双向循环编码、CRF 配分函数、gold score、Viterbi 与 BIO 约束如何从公式落到代码？ |
| 22 | [从零实现 CNN 与 ResNet](./22-cnn-resnet-from-scratch.ipynb) | LeNet、AlexNet、VGG、残差块和 BatchNorm 的形状、梯度、训练/评估状态如何验证？ |
| 23 | [从零实现 U-Net](./23-unet-segmentation-from-scratch.ipynb) | 编码器/解码器、skip connection、奇偶尺寸对齐、Dice+BCE 与滑窗推理如何实现？ |
| 24 | [从零实现 Vision Transformer](./24-vision-transformer-from-scratch.ipynb) | patch embedding、CLS/位置编码、手写 QKV、多头缩放注意力和 Encoder block 如何实现？ |
| 25 | [从零实现 GCN](./25-gcn-from-scratch-pytorch.ipynb) | 自环与对称归一化、`A_hat @ (XW)`、传导式节点分类和图快照合同如何实现？ |
| 26 | [从零实现 GraphSAGE](./26-graphsage-from-scratch-pytorch.ipynb) | 邻居采样、mean aggregation、归纳新节点推理、可信图快照与租户隔离如何实现？ |
| 27 | [从零实现 GAT](./27-gat-from-scratch-pytorch.ipynb) | 边注意力、按目标节点稳定 softmax、自环、多头 concat/mean 和有向消息如何实现？ |
| 28 | [从零实现神经推荐模型](./28-neural-recommender-from-scratch-pytorch.ipynb) | Two-Tower、NeuMF、BPR/BCE、曝光负例、全量 ranking 与主体权限如何串联？ |
| 29 | [从零实现 TCN 时序预测](./29-tcn-time-series-from-scratch-pytorch.ipynb) | causal/dilated convolution、残差块、感受野、严格时间切分和流式窗口如何实现？ |
| 30 | [从零实现 VAE](./30-vae-from-scratch-pytorch.ipynb) | 编码器/解码器、重参数化、ELBO、beta warmup、重建/生成与 OOD 分数如何实现？ |

## 第四组：进阶架构与跨领域复现

这一组继续只使用 PyTorch 基础算子搭建完整网络，覆盖预训练语言模型、检测与生成、图级/知识图谱建模、语音、强化学习和图文对齐。除 forward 与训练外，每本都要求独立数值 oracle、数据切分、推理协议和可信制品验证。

| 编号 | Notebook | 核心工程问题 |
| --- | --- | --- |
| 31 | [从零实现 GPT Decoder 与 KV Cache](./31-gpt-decoder-kv-cache-from-scratch.ipynb) | causal self-attention、pre-norm block、权重共享、逐 token KV cache 和生成策略如何实现并验证等价性？ |
| 32 | [从零实现 BERT Encoder 与预训练目标](./32-bert-encoder-pretraining-from-scratch.ipynb) | token/position/segment embedding、双向 attention、80/10/10 masking、MLM 与句子分类如何实现？ |
| 33 | [从零实现 TextCNN 与 HAN](./33-textcnn-han-from-scratch-pytorch.ipynb) | 多卷积核文本分类、手写双向 GRU、词/句层 attention 与变长文档 mask 如何实现？ |
| 34 | [从零实现 MobileNet 与 DenseNet](./34-mobilenet-densenet-from-scratch-pytorch.ipynb) | depthwise separable/inverted residual、dense connectivity、transition 与参数效率如何验证？ |
| 35 | [从零实现 DETR](./35-detr-object-detection-from-scratch-pytorch.ipynb) | CNN backbone、object query、手写 Encoder/Decoder、集合匹配与 no-object loss 如何实现？ |
| 36 | [从零实现 DDPM](./36-ddpm-diffusion-from-scratch-pytorch.ipynb) | 时间嵌入、噪声日程、Tiny U-Net、epsilon objective 与反向采样公式如何实现？ |
| 37 | [从零实现 GIN 图分类](./37-gin-graph-classification-from-scratch-pytorch.ipynb) | sum aggregation、learnable epsilon、多图 batching、graph pooling 与置换不变性如何实现？ |
| 38 | [从零实现 R-GCN 知识图谱模型](./38-rgcn-knowledge-graph-from-scratch-pytorch.ipynb) | 关系特定消息、inverse edge、DistMult、类型化负采样与 filtered ranking 如何实现？ |
| 39 | [从零实现 Graphormer 风格 Graph Transformer](./39-graph-transformer-from-scratch-pytorch.ipynb) | degree/spatial encoding、最短路 bias、padded graph batch 和图级表示如何实现？ |
| 40 | [从零实现 Conformer-CTC](./40-conformer-ctc-from-scratch-pytorch.ipynb) | macaron FFN、卷积增强 attention、手写 CTC 动态规划、对齐与离线 ASR 边界如何实现？ |
| 41 | [从零实现 Double DQN](./41-double-dqn-from-scratch-pytorch.ipynb) | Q 网络、经验回放、目标网络、terminal/truncated、Double DQN target 与策略发布如何实现？ |
| 42 | [从零实现 CLIP 风格双编码器](./42-clip-dual-encoder-from-scratch-pytorch.ipynb) | 图像/文本双塔、对称 InfoNCE、temperature、双向全候选检索与候选快照如何实现？ |

## 第五组：现代序列、视觉、图时序与决策模型

这一组进一步覆盖 encoder-decoder 预训练、选择性状态空间模型、替换词检测、层次视觉与两阶段检测、神经辐射场、异构/时序/层次图网络、策略优化、可逆生成模型和多任务推荐。每本仍从基础张量算子手写核心结构，并用可执行反例验证 mask、时间边界、坐标、密度、策略与任务语义。

| 编号 | Notebook | 核心工程问题 |
| --- | --- | --- |
| 43 | [从零实现 T5 风格 Span Corruption](./43-t5-span-corruption-from-scratch-pytorch.ipynb) | RMSNorm、相对位置 bucket、encoder-decoder attention、sentinel span corruption 与生成如何实现？ |
| 44 | [从零实现 Mamba 风格 Selective SSM](./44-mamba-selective-ssm-from-scratch-pytorch.ipynb) | input-dependent `Δ/B/C`、稳定状态更新、causal convolution、逐步/分块状态等价如何验证？ |
| 45 | [从零实现 ELECTRA 预训练](./45-electra-pretraining-from-scratch-pytorch.ipynb) | generator MLM、replacement sampling、replaced-token detection 与 special/padding 合同如何实现？ |
| 46 | [从零实现 Swin Transformer](./46-swin-transformer-from-scratch-pytorch.ipynb) | window/shifted-window attention、相对位置偏置、attention mask 与 patch merging 如何实现？ |
| 47 | [从零实现 Faster R-CNN](./47-faster-rcnn-from-scratch-pytorch.ipynb) | anchor、RPN、box delta、匹配/NMS、ROI pooling 与二阶段损失如何串联？ |
| 48 | [从零实现 NeRF 体渲染](./48-nerf-volume-rendering-from-scratch-pytorch.ipynb) | camera ray、位置编码、density/color MLP、alpha compositing 与 coarse/fine sampling 如何实现？ |
| 49 | [从零实现 HGT 异构图网络](./49-hgt-heterogeneous-graph-from-scratch-pytorch.ipynb) | 节点/关系类型特定 QKV、目标节点 softmax、多头消息与异构节点分类如何实现？ |
| 50 | [从零实现 TGN 时序图网络](./50-tgn-temporal-graph-network-from-scratch-pytorch.ipynb) | memory/mailbox、时间编码、事件顺序、temporal aggregation 与 prequential 评估如何实现？ |
| 51 | [从零实现 DiffPool 层次图网络](./51-diffpool-hierarchical-graph-from-scratch-pytorch.ipynb) | assignment、`S^T X`、`S^T A S`、link/entropy 辅助损失与多图 padding 如何实现？ |
| 52 | [从零实现 PPO Actor-Critic](./52-ppo-actor-critic-from-scratch-pytorch.ipynb) | rollout、GAE、terminated/truncated、clipped surrogate 与策略发布如何实现？ |
| 53 | [从零实现 RealNVP Normalizing Flow](./53-realnvp-normalizing-flow-from-scratch-pytorch.ipynb) | affine coupling、正逆变换、精确 log-det/likelihood 与可复现采样如何实现？ |
| 54 | [从零实现 MMoE 多任务推荐](./54-mmoe-multitask-recommendation-from-scratch-pytorch.ipynb) | expert、task gate、缺失标签、多任务 loss、分任务 AUC 与任务语义绑定如何实现？ |

## 第六组：LLM 对齐推理、进阶视觉、图表示与科学建模

这一组按方向拆到四个根目录子专题，继续坚持不用高层模型包代替核心架构。除手写 `nn.Module` 与 `forward` 外，还验证低比特/低秩训练语义、偏好数据合同、接受—拒绝采样、掩码和提示坐标、可微 3D 渲染、图增强与随机游走、几何等变性、连续控制、可解释时序和离散 codebook。

| 编号 | Notebook | 核心工程问题 |
| --- | --- | --- |
| 55 | [从零实现 LoRA 与教学版 QLoRA](../13-llm-training-inference/55-lora-qlora-from-scratch-pytorch.ipynb) | 低秩 adapter、冻结基座、合并等价、分组 4-bit 量化、保存与加载合同如何实现？ |
| 56 | [从零实现 DPO 偏好优化](../13-llm-training-inference/56-dpo-preference-optimization-from-scratch-pytorch.ipynb) | chosen/rejected 对数概率、reference policy、DPO loss、padding mask 与偏好数据切分如何实现？ |
| 57 | [从零实现 Speculative Decoding](../13-llm-training-inference/57-speculative-decoding-from-scratch-pytorch.ipynb) | draft/target 接受率、残差分布拒绝采样、EOS、缓存状态与分布正确性如何验证？ |
| 58 | [从零实现 Masked Autoencoder](../14-advanced-vision-3d/58-masked-autoencoder-from-scratch-pytorch.ipynb) | patchify、随机 masking、可见 token encoder、mask token decoder 与 masked loss 如何实现？ |
| 59 | [从零实现 SAM 风格提示分割](../14-advanced-vision-3d/59-sam-promptable-segmentation-from-scratch-pytorch.ipynb) | 图像编码、点/框提示、双向交互、mask token、IoU 头与坐标合同如何实现？ |
| 60 | [从零实现 3D Gaussian Splatting](../14-advanced-vision-3d/60-3d-gaussian-splatting-from-scratch-pytorch.ipynb) | 相机投影、协方差、深度排序、alpha compositing、可微优化与视角协议如何实现？ |
| 61 | [从零实现 GraphCL 图对比学习](../15-graph-representation-science/61-graphcl-contrastive-learning-from-scratch-pytorch.ipynb) | 图增强、双视图编码、projection head、NT-Xent、batch negatives 与增强身份如何实现？ |
| 62 | [从零实现 Node2Vec 与 Skip-Gram](../15-graph-representation-science/62-node2vec-skipgram-from-scratch-pytorch.ipynb) | 二阶有偏随机游走、`p/q`、上下文对、负采样、嵌入评估与图快照如何实现？ |
| 63 | [从零实现 EGNN 分子等变网络](../15-graph-representation-science/63-egnn-equivariant-molecular-from-scratch-pytorch.ipynb) | 标量消息、坐标更新、平移/旋转/置换等变性、padding mask 与分子回归如何实现？ |
| 64 | [从零实现 SAC 连续控制](../16-control-timeseries-generative/64-sac-continuous-control-from-scratch-pytorch.ipynb) | squashed Gaussian、双 Q、自动温度、replay、bootstrap 与 Polyak target 如何实现？ |
| 65 | [从零实现 N-BEATS 时序预测](../16-control-timeseries-generative/65-nbeats-time-series-from-scratch-pytorch.ipynb) | backcast/forecast、双残差堆叠、趋势/季节 basis、滚动原点评估如何实现？ |
| 66 | [从零实现 VQ-VAE](../16-control-timeseries-generative/66-vqvae-from-scratch-pytorch.ipynb) | 最近邻 codebook、straight-through、commitment/codebook loss、perplexity 与 code 解码如何实现？ |

## 第七组：开放式系统设计面试题的底层实现

这一组采用“一道问题一本 notebook”：先澄清需求和 SLO，再用 Python 标准库、NumPy 或 PyTorch 基础算子实现核心算法，最后覆盖离线 oracle、线上状态、版本发布与失败模式。教学代码不调用搜索引擎、ANN、排序、特征平台或实验平台的一站式接口，便于在面试中解释每个关键决策。

| 编号 | Notebook | 核心工程问题 |
| --- | --- | --- |
| 67 | [增量倒排索引](../17-interview-systems-from-scratch/67-inverted-index-incremental-search-from-scratch.ipynb) | 支持短语、字段、删除、段合并与快照发布的关键词检索怎样从零实现？ |
| 68 | [IVF-PQ 向量检索](../17-interview-systems-from-scratch/68-ivf-pq-vector-search-from-scratch-numpy.ipynb) | coarse quantizer、product quantization、ADC、`nprobe` 与 recall/成本曲线怎样实现？ |
| 69 | [HNSW 近邻检索](../17-interview-systems-from-scratch/69-hnsw-ann-search-from-scratch-numpy.ipynb) | 分层图、贪心下降、候选搜索、邻居裁剪、软删除与 recall/访问量怎样验证？ |
| 70 | [拼写纠错与 Query Rewrite](../17-interview-systems-from-scratch/70-spell-correction-query-rewrite-from-scratch.ipynb) | 候选生成、编辑距离、语言模型、置信拒识与 rewrite 日志怎样设计？ |
| 71 | [MinHash 与 LSH 近重复检测](../17-interview-systems-from-scratch/71-minhash-lsh-near-duplicate-from-scratch.ipynb) | shingle、MinHash、banding、候选精排与增量去重怎样实现？ |
| 72 | [LambdaRank 学习排序](../17-interview-systems-from-scratch/72-learning-to-rank-lambdarank-from-scratch-pytorch.ipynb) | 如何从 `ΔnDCG` 推出 pairwise lambda，训练手写 ranker 并做 query-level 评估？ |
| 73 | [Feature Store 的 Point-in-Time Join](../17-interview-systems-from-scratch/73-feature-store-point-in-time-join-from-scratch.ipynb) | event time、available time、as-of join、回填和在线离线一致性怎样避免特征穿越？ |
| 74 | [点击偏差与 IPS/SNIPS](../17-interview-systems-from-scratch/74-click-bias-ips-counterfactual-ranking-from-scratch.ipynb) | 位置偏差、propensity、support、clipping、ESS 与反事实排序评估怎样处理？ |
| 75 | [流式 Count-Min Sketch 与 Top-K](../17-interview-systems-from-scratch/75-streaming-count-min-sketch-topk-from-scratch.ipynb) | 固定内存下怎样估频、合并窗口、发现重 hitter 并量化误差？ |
| 76 | [Bloom 与 Counting Bloom Filter](../17-interview-systems-from-scratch/76-bloom-counting-filter-from-scratch.ipynb) | bit packing、双重散列、误判率、安全删除、分层扩容与缓存穿透怎样处理？ |
| 77 | [概率校准与业务阈值](../17-interview-systems-from-scratch/77-model-calibration-thresholding-from-scratch-pytorch.ipynb) | reliability、ECE/Brier、temperature/isotonic、成本阈值和分组监控怎样实现？ |
| 78 | [A/B 实验与序贯决策](../17-interview-systems-from-scratch/78-ab-testing-sequential-experiment-from-scratch.ipynb) | 随机化、SRM、CUPED、ratio metric、多重检验、提前偷看与非劣效护栏怎样实现？ |

## 第八组：机器学习系统面试题的一题一本回答

这一组把题目直接写在 Notebook 首屏，围绕 LLM/RAG 服务、分布式训练、可靠性、监控发布和在线决策展开。每本先给面试回答主线，再用可运行的底层状态机或数值算法证明关键结论；框架只作为生产替换点讨论，不作为核心实现。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 79 | [Continuous Batching 调度器](../18-ml-system-interview-questions/79-llm-continuous-batching-scheduler-from-scratch.ipynb) | LLM 推理如何处理 prefill/decode、token/KV budget、尾延迟、deadline 与租户公平？ |
| 80 | [多租户语义缓存](../18-ml-system-interview-questions/80-multitenant-semantic-cache-from-scratch.ipynb) | RAG/LLM 语义缓存如何避免陈旧命中、缓存投毒、跨租户和跨权限泄漏？ |
| 81 | [向量数据库分片与复制](../18-ml-system-interview-questions/81-vector-database-sharding-replication-from-scratch.ipynb) | 向量分片路由、local/global Top-K、过滤、副本故障和在线迁移怎样实现？ |
| 82 | [RAG 摄取与版本链路](../18-ml-system-interview-questions/82-rag-ingestion-versioning-idempotency-from-scratch.ipynb) | 文档、chunk、outbox、索引和删除怎样做到幂等、可追踪、可对账和可回滚？ |
| 83 | [多路召回预算与融合](../18-ml-system-interview-questions/83-multichannel-retrieval-budget-fusion-from-scratch.ipynb) | keyword/dense/entity/fresh 通道如何分配配额、去重融合并在超时后降级？ |
| 84 | [Ring AllReduce](../18-ml-system-interview-questions/84-ring-allreduce-distributed-training-from-scratch.ipynb) | Reduce-Scatter 与 All-Gather 如何实现，通信量、低精度和 bucket overlap 怎样分析？ |
| 85 | [限流算法与分层配额](../18-ml-system-interview-questions/85-rate-limiting-token-bucket-sliding-window-from-scratch.ipynb) | Token Bucket、Leaky Bucket、滑动窗口、多级原子扣费和故障策略怎样取舍？ |
| 86 | [At-Least-Once 任务队列](../18-ml-system-interview-questions/86-at-least-once-job-queue-idempotency-from-scratch.ipynb) | visibility lease、业务幂等、heartbeat、退避重试、DLQ 和 outbox 怎样串联？ |
| 87 | [模型漂移监控](../18-ml-system-interview-questions/87-ml-data-drift-monitoring-from-scratch.ipynb) | PSI/JS/KS/Page-Hinkley、延迟标签、分组切片和迟滞告警怎样实现？ |
| 88 | [Shadow、Canary 与回滚](../18-ml-system-interview-questions/88-model-canary-shadow-rollback-from-scratch.ipynb) | 模型如何稳定分流、设置质量/延迟 guardrail、处理多次查看并自动回滚？ |
| 89 | [LinUCB 在线探索](../18-ml-system-interview-questions/89-contextual-bandit-linucb-delayed-feedback-from-scratch.ipynb) | Contextual Bandit 如何训练、记录 propensity、处理延迟反馈并做 IPS/SNIPS？ |
| 90 | [Conformal Prediction](../18-ml-system-interview-questions/90-conformal-prediction-uncertainty-from-scratch.ipynb) | 如何为回归/分类输出带覆盖率目标的区间/集合，并说明分组与漂移限制？ |

## 第九组：主流机器学习与深度学习面试题的一题一本回答

这一组补齐高频基础题中最容易被追问实现细节的部分：数据泄漏、类别不平衡、指标阈值、数值稳定、归一化、梯度、优化器、混合精度、生成解码、蒸馏、量化和可复现训练。每本都从面试结论进入公式与反例，再用 NumPy/PyTorch 基础算子实现，最后落到线上或训练系统合同。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 91 | [数据切分与泄漏审计](../19-mainstream-ml-dl-interview-questions/91-dataset-splitting-data-leakage-from-scratch.ipynb) | 数据集怎样按 group/time 切分，并发现重复、统计量和未来特征泄漏？ |
| 92 | [类别不平衡、Focal 与阈值](../19-mainstream-ml-dl-interview-questions/92-class-imbalance-focal-loss-threshold-from-scratch.ipynb) | 采样、损失加权、Focal Loss 和成本阈值怎样联合设计？ |
| 93 | [ROC、PR、AUC 与阈值指标](../19-mainstream-ml-dl-interview-questions/93-roc-pr-auc-threshold-metrics-from-scratch.ipynb) | 排序指标与决策指标有什么区别，类别不平衡时如何选择？ |
| 94 | [稳定 Softmax 与交叉熵](../19-mainstream-ml-dl-interview-questions/94-softmax-cross-entropy-numerical-stability-from-scratch.ipynb) | log-sum-exp、梯度、padding mask、label smoothing 与 FP16 怎样实现？ |
| 95 | [BatchNorm、LayerNorm 与 RMSNorm](../19-mainstream-ml-dl-interview-questions/95-batchnorm-layernorm-rmsnorm-from-scratch-pytorch.ipynb) | 三类归一化的轴、状态、训练/推理差异和残差位置是什么？ |
| 96 | [梯度消失与爆炸诊断](../19-mainstream-ml-dl-interview-questions/96-vanishing-exploding-gradients-diagnosis-from-scratch-pytorch.ipynb) | 怎样用梯度 trace、初始化、残差和裁剪定位并治理深网训练问题？ |
| 97 | [手写 SGD、Momentum、Adam 与 AdamW](../19-mainstream-ml-dl-interview-questions/97-sgd-momentum-adam-adamw-from-scratch.ipynb) | 偏差修正、L2/解耦衰减、参数组和优化器断点状态怎样实现？ |
| 98 | [梯度累积、AMP 与裁剪](../19-mainstream-ml-dl-interview-questions/98-gradient-accumulation-amp-loss-scaling-clipping-from-scratch.ipynb) | 如何保证大 batch 等价，并正确安排 unscale、overflow、clip 与 step？ |
| 99 | [Greedy、Beam、Top-k 与 Top-p](../19-mainstream-ml-dl-interview-questions/99-greedy-beam-topk-topp-decoding-from-scratch.ipynb) | LLM 解码中的分数、长度、采样、重复限制和停止条件怎样实现？ |
| 100 | [知识蒸馏](../19-mainstream-ml-dl-interview-questions/100-knowledge-distillation-from-scratch-pytorch.ipynb) | Temperature、KL、`T²`、硬软目标、feature 与 mask 怎样设计？ |
| 101 | [INT8 PTQ 与 QAT](../19-mainstream-ml-dl-interview-questions/101-int8-ptq-qat-quantization-from-scratch.ipynb) | qparam、per-channel、整数 GEMM、校准和 fake quant 怎样实现？ |
| 102 | [可复现训练与断点续训](../19-mainstream-ml-dl-interview-questions/102-reproducible-training-checkpoint-resume-from-scratch.ipynb) | RNG、sampler、optimizer、scheduler、累积窗口和 checkpoint 怎样完整恢复？ |

## 推荐学习顺序

1. 先运行 01，理解“算法实现”必须包含训练产物、版本与正确性测试。
2. 运行 02，独立搭建关键词搜索；再运行 03，把检索器接入完整 RAG 链路。
3. 运行 06，学习多路召回、融合、重排、指标与线上降级。
4. 运行 04 和 05，扩展到分类系统与结构化知识系统。
5. NLP 工程继续运行 07–09；CV 文档链路运行 10–12；图学习运行 13–15。
6. 运行 16–18，把同样的合同、评估、安全和版本方法迁移到多模态、推荐与时序系统。
7. 按 `19–21 -> 22–24 -> 25–27 -> 28–30` 运行基础架构复现，分别覆盖 NLP、CV、图学习、推荐、时序与生成模型。
8. 再按 `31–33 -> 34–36 -> 37–39 -> 40–42` 运行进阶复现，进入预训练模型、检测/扩散、图级建模、语音、强化学习与图文对齐。
9. 最后按 `43–45 -> 46–48 -> 49–51 -> 52–54` 运行现代架构与跨领域系统，重点比较序列状态、空间层次、事件时间、策略数据和多任务语义的不同合同。
10. 继续按 `55–57 -> 58–60 -> 61–63 -> 64–66` 运行专项复现，比较参数高效对齐、概率精确推理、提示/几何坐标、图增强/等变性、离策略控制与离散潜变量各自的正确性 oracle。
11. 面试系统题按 `67–72 -> 73–78` 运行：先掌握检索、纠错、去重和排序，再进入特征时序、反事实学习、流式结构、校准与在线实验。
12. 继续运行 `79–84 -> 85–90`：从 LLM/RAG 服务与分布式通信，扩展到流量/队列可靠性、漂移、灰度、在线探索和不确定性。
13. 最后运行 `91–96 -> 97–102`：先建立数据、指标和数值基础，再串联优化、混合精度、生成、压缩与可复现训练。

## 统一验收标准

- notebook JSON 符合 nbformat 4.5，每个 cell 有唯一 id；
- 从头到尾按顺序执行，不依赖前一次内核残留；
- 代码有断言或指标输出，受控小数据的结果不冒充线上泛化效果；
- 区分教学实现与生产组件，说明替换点、复杂度、权限和版本契约；
- 引用原始论文或官方文档，算法名和公式不靠二手博客定义；
- 对 ACL、旧版本、空 gold、数据泄漏、索引迁移等失败模式有明确处理。

## 工程研究方法

一个工程问题至少要回答六层：

```text
业务目标与 SLO
  -> 输入/输出与版本契约
  -> 数据结构和核心算法
  -> 离线评估与回归集
  -> 在线延迟、成本、可观测和降级
  -> 安全、权限、更新与回滚
```

只实现算法主体通常只能算 demo。例如 BM25 得分正确，不代表关键词搜索系统已经处理 analyzer 版本、字段权重、ACL、删除、分片与评估；能抽取三元组，也不代表知识图谱已经解决实体消歧、来源、时间和幂等更新。

## 后续可继续扩展

- DiskANN/GPU ANN、learned sparse retrieval、跨地域复制与在线压测
- 多跳规划、Agentic RAG、检索反馈学习与端到端故障归因
- 多标签/层级分类与人工审核工作流
- 检索服务 API、压测、缓存、灰度与回滚
- 音频事件检测、说话人识别与语音增强
- 视觉语言生成、视频理解、视频扩散与动态 3D 场景
- CQL/IQL、offline RL、world model 与安全策略评估
- 地理空间、uplift/因果图、深度 contextual bandit 与安全离线强化学习

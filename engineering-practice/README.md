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

## 第十组：生成式 AI 与 Agent 高频面试题的一题一本回答

这一组依据当前 AI/LLM Engineer 题单补齐 Agent、评测、安全和后训练缺口。实现不把 Agent 框架、`generate()`、SFT Trainer 或评测平台当答案，而是显式写出状态机、schema、mask、统计量、权限和失败路径。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 103 | [Prompt/RAG/SFT/Tool 方案选择](../20-genai-agent-interview-questions/103-prompt-rag-finetuning-tool-choice-from-scratch.ipynb) | 怎样区分知识、行为和动作缺口，并以质量、成本、延迟和风险做决策？ |
| 104 | [LLM/Agent 黄金集评测](../20-genai-agent-interview-questions/104-llm-evaluation-golden-set-release-gate-from-scratch.ipynb) | 黄金集、grader、轨迹、置信区间、slice 和发布门禁怎样设计？ |
| 105 | [LLM-as-a-Judge 偏差校准](../20-genai-agent-interview-questions/105-llm-as-judge-bias-calibration-from-scratch.ipynb) | 怎样处理位置、冗长、随机性和 Judge 版本偏差？ |
| 106 | [Agent Tool Calling](../20-genai-agent-interview-questions/106-agent-tool-calling-schema-idempotency-from-scratch.ipynb) | schema、权限、幂等、审批、重试和 trace 怎样串成可靠执行链路？ |
| 107 | [ReAct Agent 有界循环](../20-genai-agent-interview-questions/107-react-agent-loop-budget-cycle-detection-from-scratch.ipynb) | Action/Observation、预算、循环检测、重规划和终止条件怎样实现？ |
| 108 | [Prompt Injection 信任边界](../20-genai-agent-interview-questions/108-prompt-injection-trust-boundary-defense-from-scratch.ipynb) | 怎样处理直接/间接注入、taint、最小权限和高风险动作审批？ |
| 109 | [约束 JSON 解码](../20-genai-agent-interview-questions/109-constrained-json-decoding-trie-from-scratch.ipynb) | 如何把 schema 编译成 trie 状态并逐步 mask 非法 token？ |
| 110 | [幻觉、引用与拒答](../20-genai-agent-interview-questions/110-hallucination-grounding-citation-abstention-from-scratch.ipynb) | 怎样验证 claim-evidence、引用覆盖、矛盾并校准拒答阈值？ |
| 111 | [上下文窗口与 Agent Memory](../20-genai-agent-interview-questions/111-context-window-memory-budgeting-from-scratch.ipynb) | 如何预算、选材、重排、摘要、管理长期记忆和安全截断？ |
| 112 | [SFT Template、Mask 与 Packing](../20-genai-agent-interview-questions/112-sft-chat-template-loss-mask-packing-from-scratch-pytorch.ipynb) | role token、assistant-only loss、causal shift 和会话隔离怎样实现？ |
| 113 | [Reward Model 与 KL 策略](../20-genai-agent-interview-questions/113-reward-model-bradley-terry-kl-policy-from-scratch-pytorch.ipynb) | Bradley–Terry、tie、prompt split、reward hacking 与 KL 约束是什么？ |
| 114 | [质量/成本/延迟模型路由](../20-genai-agent-interview-questions/114-quality-cost-latency-model-routing-from-scratch.ipynb) | 边际收益、阈值、cascade、预算、探索日志和故障降级怎样设计？ |

## 第十一组：Agent Loop 深入面试题的一题一本回答

这一组继续深入 Agent 的生产控制面。每本不以框架调用代替答案，而是手写计划 DAG、并行 Join、BM25 工具发现、事件溯源、审批票据、共享黑板、多跳证据图、反思停止策略、Capability VM、JSON-RPC 生命周期和 trace/replay，并明确教学实现与生产安全边界。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 115 | [Workflow 与 Agent 模式选择](../21-agent-loop-interview-questions/115-workflow-vs-agent-pattern-selection-from-scratch.ipynb) | 什么时候用固定 Workflow，什么时候用 Agent？Sequential、Routing、Parallel、Orchestrator 和 Evaluator-Optimizer 怎样选？ |
| 116 | [计划 DAG 与调度器](../21-agent-loop-interview-questions/116-agent-plan-dag-scheduler-from-scratch.ipynb) | Agent 生成计划后，怎样校验 DAG、并行调度、处理失败和动态重规划？ |
| 117 | [并行工具执行与 Join](../21-agent-loop-interview-questions/117-parallel-tool-execution-join-consistency-from-scratch.ipynb) | Agent 怎样安全并行调用工具，处理依赖、限流、部分失败和结果合并？ |
| 118 | [大规模 Tool Catalog 检索](../21-agent-loop-interview-questions/118-large-tool-catalog-retrieval-bm25-from-scratch.ipynb) | Agent 面对成百上千个工具时，怎样做 Tool Discovery、召回和选择？ |
| 119 | [持久化 Agent 与事件重放](../21-agent-loop-interview-questions/119-durable-agent-event-sourcing-resume-from-scratch.ipynb) | 长时间运行的 Agent 怎样做到崩溃恢复、精确重放和安全取消？ |
| 120 | [Human-in-the-Loop](../21-agent-loop-interview-questions/120-human-in-the-loop-approval-interrupt-resume-from-scratch.ipynb) | 哪些动作必须审批，审批票据怎样绑定动作，如何中断、超时与恢复？ |
| 121 | [Multi-Agent Handoff 与 Blackboard](../21-agent-loop-interview-questions/121-multi-agent-handoff-blackboard-isolation-from-scratch.ipynb) | 什么时候需要 Multi-Agent，Handoff、共享状态、隔离和写冲突怎样设计？ |
| 122 | [Agentic RAG 多跳查询规划](../21-agent-loop-interview-questions/122-agentic-rag-multihop-query-planning-from-scratch.ipynb) | 怎样分解问题、逐跳检索、构建证据图、处理时间冲突并判断停止？ |
| 123 | [Reflection / Evaluator-Optimizer](../21-agent-loop-interview-questions/123-evaluator-optimizer-reflection-loop-from-scratch.ipynb) | 怎样把评价变成可执行修订，并避免共享盲点、循环和越改越差？ |
| 124 | [安全代码执行与 Capability VM](../21-agent-loop-interview-questions/124-safe-code-execution-capability-vm-from-scratch.ipynb) | Agent 执行代码时怎样做白名单、资源限制、文件/网络隔离和结果审计？ |
| 125 | [MCP 生命周期与最小协议](../21-agent-loop-interview-questions/125-mcp-jsonrpc-lifecycle-capability-from-scratch.ipynb) | Host、Client、Server、Tools、Resources、Prompts、JSON-RPC 和能力协商是什么？ |
| 126 | [Agent Trace、Replay 与成本归因](../21-agent-loop-interview-questions/126-agent-observability-trace-replay-cost-from-scratch.ipynb) | 怎样定位 Agent 的慢、贵、循环、工具错误和质量回归？ |

## 第十二组：LLM 系统与推理面试题的一题一本回答

这一组从模型训练预算延伸到分布式 mesh、模型状态分片、attention/KV 内存，再进入 reasoning model 的后训练与 test-time search。每本显式实现公式、数组分片、物理块、token mask、搜索状态或 verifier，不把 DeepSpeed、vLLM、RL trainer 和 Agent 框架本身当答案。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 127 | [Scaling Law 与训练预算](../22-llm-systems-reasoning-interview-questions/127-llm-scaling-law-compute-budget-from-scratch.ipynb) | 给定训练算力、数据上限和推理量，怎样选择参数量、训练 token 与集群工期？ |
| 128 | [LLM 3D 并行规划](../22-llm-systems-reasoning-interview-questions/128-llm-3d-parallelism-planner-from-scratch.ipynb) | DP、TP、PP、Sequence Parallel 分别解决什么，怎样结合拓扑、显存和 bubble 选型？ |
| 129 | [ZeRO 分片与通信](../22-llm-systems-reasoning-interview-questions/129-zero-sharding-memory-communication-from-scratch.ipynb) | ZeRO-1/2/3 分别切什么，参数生命周期、offload 和跨 world-size checkpoint 怎样实现？ |
| 130 | [FlashAttention 与 Online Softmax](../22-llm-systems-reasoning-interview-questions/130-flash-attention-online-softmax-from-scratch.ipynb) | 为什么 FlashAttention 仍是精确 attention，运行最大值、分块和 causal mask 怎样实现？ |
| 131 | [PagedAttention KV Block Manager](../22-llm-systems-reasoning-interview-questions/131-paged-attention-kv-block-manager-from-scratch.ipynb) | 动态 KV Cache 怎样做块表、按需增长、共享、Copy-on-Write、回收和准入？ |
| 132 | [Prefix Cache 与 Radix Trie](../22-llm-systems-reasoning-interview-questions/132-prefix-cache-radix-trie-isolation-from-scratch.ipynb) | Prefix Cache 怎样匹配 token、复用完整块、版本失效、隔离租户并参与调度？ |
| 133 | [LLM PPO](../22-llm-systems-reasoning-interview-questions/133-llm-ppo-token-level-kl-gae-from-scratch-pytorch.ipynb) | RLHF 中 token-level KL、末端 reward、GAE、policy/value clip 和 response mask 怎样串联？ |
| 134 | [GRPO](../22-llm-systems-reasoning-interview-questions/134-grpo-group-relative-policy-optimization-from-scratch-pytorch.ipynb) | Group-relative advantage 为什么能省 critic，零方差、clip、KL 和 stale rollout 怎样处理？ |
| 135 | [Self-Consistency](../22-llm-systems-reasoning-interview-questions/135-self-consistency-correlated-voting-from-scratch.ipynb) | 多路径投票为什么有效，怎样处理 parser、相关错误、加权投票、聚类和提前停止？ |
| 136 | [Tree of Thoughts](../22-llm-systems-reasoning-interview-questions/136-tree-of-thought-budgeted-search-from-scratch.ipynb) | Thought 怎样变成状态，generator、evaluator、剪枝、回溯、verifier 与预算怎样设计？ |
| 137 | [Agent Context Compaction](../22-llm-systems-reasoning-interview-questions/137-agent-context-compaction-structured-memory-from-scratch.ipynb) | 长时间 Agent 怎样压缩上下文，同时保留事实来源、工具制品、权限和恢复能力？ |
| 138 | [Process Reward 与 Verifier Search](../22-llm-systems-reasoning-interview-questions/138-process-reward-verifier-guided-search-from-scratch.ipynb) | PRM 与 ORM 有何区别，step 标签、masked loss、路径聚合和 verifier-guided search 怎样实现？ |

## 第十三组：LLM 数据配方、推理服务与 Agent 互操作面试题

这一组连接训练数据、单机推理算法、线上服务控制面与 Agent 生态接口。每本都从面试回答主线进入底层实现：显式计算采样概率、token 统计、激活/KV/权重内存，手写缓存与路由状态机，并用协议验证、风险策略和分层指标覆盖 Agent 的发现、动作、工具与技能生命周期。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 139 | [预训练数据混合与 DoReMi](../23-llm-data-serving-agent-interop-interview-questions/139-llm-pretraining-data-mixture-sampling-from-scratch.ipynb) | 多领域语料怎样设定 mixture、temperature、上下界与反馈更新，并避免小域过采样和验证集污染？ |
| 140 | [Causal LM Loss、PPL 与 BPB](../23-llm-data-serving-agent-interop-interview-questions/140-causal-lm-loss-perplexity-bpb-from-scratch-pytorch.ipynb) | next-token shift、padding/文档边界 mask、分布式聚合、滑窗评分和跨 tokenizer 比较怎样做对？ |
| 141 | [Activation Checkpointing 与重计算](../23-llm-data-serving-agent-interop-interview-questions/141-activation-checkpointing-recomputation-from-scratch.ipynb) | 激活显存由什么决定，重计算怎样换显存，RNG、原地修改和副作用为什么会破坏梯度？ |
| 142 | [MHA、MQA、GQA 与 KV Cache](../23-llm-data-serving-agent-interop-interview-questions/142-mha-mqa-gqa-kv-cache-from-scratch.ipynb) | 三种注意力怎样映射 query head 与 KV head，输出如何等价验证，KV 显存和带宽怎样估算？ |
| 143 | [Attention Sink 与滚动 KV](../23-llm-data-serving-agent-interop-interview-questions/143-streaming-attention-sink-rolling-kv-from-scratch.ipynb) | 流式长文本怎样保留 sink、淘汰局部 token、维护绝对位置，并识别有限窗口无法回答的问题？ |
| 144 | [GPTQ、AWQ 与 Weight-only Quantization](../23-llm-data-serving-agent-interop-interview-questions/144-gptq-awq-weight-only-quantization-from-scratch.ipynb) | group-wise 量化、校准激活、显著通道保护、误差指标、元数据和发布门禁怎样实现？ |
| 145 | [多租户 LoRA Adapter Serving](../23-llm-data-serving-agent-interop-interview-questions/145-multitenant-lora-adapter-serving-from-scratch.ipynb) | 一个共享基座怎样批量服务多 adapter，处理版本、缓存淘汰、租户隔离、热更新和回退？ |
| 146 | [Prefill–Decode 解耦与路由](../23-llm-data-serving-agent-interop-interview-questions/146-prefill-decode-disaggregation-router-from-scratch.ipynb) | 为什么拆分 prefill/decode，KV 传输、节点选择、准入、SLO、goodput 和故障降级怎样权衡？ |
| 147 | [A2A Agent Card 与 Task 生命周期](../23-llm-data-serving-agent-interop-interview-questions/147-a2a-agent-card-task-lifecycle-from-scratch.ipynb) | Agent 怎样发现彼此、协商能力并管理 task、message、artifact、流式事件、取消和终态？ |
| 148 | [Computer-use Agent 安全闭环](../23-llm-data-serving-agent-interop-interview-questions/148-computer-use-agent-grounding-safety-loop-from-scratch.ipynb) | screenshot–ground–act–observe 循环怎样处理坐标映射、陈旧画面、动作审批、幂等与轨迹评估？ |
| 149 | [Agent Tool Schema 设计与评测](../23-llm-data-serving-agent-interop-interview-questions/149-agent-tool-schema-design-evaluation-from-scratch.ipynb) | 工具名称、描述、JSON Schema、错误语义、分页、幂等和选择/参数/执行分层指标怎样设计？ |
| 150 | [Agent Skills 渐进式披露](../23-llm-data-serving-agent-interop-interview-questions/150-agent-skills-progressive-disclosure-from-scratch.ipynb) | 大量技能怎样只暴露元数据、按需加载说明和资源，同时保证路径、完整性、版本与路由可评测？ |

## 第十四组：LLM 效率、对齐与 Agent 评测面试题

这一组从数值格式、长上下文/专家并行进入 KV 与服务调度，再把优化对象扩展到对齐数据、多模态模型、工具轨迹、委托权限和长程可靠性。实现显式写出 online softmax、dispatch、位打包、Roofline、`nn.Module.forward`、loss mask、授权 claims 与统计估计，不以一站式训练/服务/Agent 框架代替回答。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 151 | [FP8 格式与 Delayed Scaling](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/151-fp8-format-delayed-scaling-from-scratch.ipynb) | E4M3/E5M2 怎样取舍，scale、amax history、margin、饱和与高精度主权重怎样实现？ |
| 152 | [Ring Attention 与 Context Parallel](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/152-ring-attention-context-parallel-from-scratch.ipynb) | 序列怎样跨设备切分，KV block 如何绕 ring，并用 online softmax 保持精确 causal attention？ |
| 153 | [MoE Expert Parallel 与负载均衡](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/153-moe-expert-parallel-load-balancing-from-scratch.ipynb) | Top-k、capacity、dispatch/All-to-All、专家合并、辅助损失和 loss-free bias 怎样实现？ |
| 154 | [KV Cache 低比特量化](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/154-kv-cache-quantization-from-scratch.ipynb) | 为什么 K/V 常采用不同 qparam 轴，2-bit packing、residual window 和 attention 误差怎样验证？ |
| 155 | [LLM 推理 Roofline 与容量规划](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/155-llm-inference-roofline-capacity-from-scratch.ipynb) | Prefill/decode 为什么分别偏计算/带宽受限，AI、延迟下界、batch 摊销和副本数怎样估算？ |
| 156 | [Chunked Prefill 调度器](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/156-chunked-prefill-scheduler-from-scratch.ipynb) | 怎样保护 decode TPOT、推进长 prompt、处理 KV 准入、绝对位置、公平和 chunk-size 搜索？ |
| 157 | [Constitutional AI 与 RLAIF](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/157-constitutional-ai-rlaif-pipeline-from-scratch.ipynb) | 原则怎样变成 critique/revision、AI preference、reward 数据、冲突升级和发布门禁？ |
| 158 | [Rejection Sampling Fine-Tuning](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/158-rejection-sampling-finetuning-bestofn-from-scratch-pytorch.ipynb) | Best-of-N 怎样过滤、排序、去重、控制 reward 偏差，再做 assistant-only SFT 与迭代评测？ |
| 159 | [LLaVA 风格视觉语言模型](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/159-llava-vision-language-projector-from-scratch-pytorch.ipynb) | 怎样手写 patch encoder、projector、视觉 token 拼接、causal decoder、loss mask 和两阶段训练？ |
| 160 | [Tool-use SFT 轨迹与 Loss Mask](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/160-tool-use-sft-trajectory-loss-mask-from-scratch.ipynb) | 调用/结果事件怎样校验、序列化、监督、原子截断、隔离坏轨迹并执行式评测？ |
| 161 | [Agent OAuth 委托授权](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/161-agent-oauth-delegated-authorization-from-scratch.ipynb) | Audience、scope、token exchange、DPoP、replay、step-up approval 怎样防 confused deputy？ |
| 162 | [长程 Agent Eval 与 pass@k/pass^k](../24-llm-efficiency-alignment-agent-evaluation-interview-questions/162-long-horizon-agent-evaluation-passk-from-scratch.ipynb) | 状态式任务、组合 grader、多 trial、paired bootstrap、trace replay 和污染门禁怎样设计？ |

## 第十五组：现代 LLM 架构、检索与 Agent 安全面试题

这一组把最新架构机制与生产控制面放在同一条验证链：从 latent cache、多 token 目标和模型/流水并行，进入可验证奖励与模型合并，再比较多向量/学习型稀疏检索、评测去污染，以及 MCP Client Features、信息流安全和相关多 Agent 共识。每本都要求 full-reference、边界反例或策略 oracle，不把论文术语和框架调用当作实现。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 163 | [Multi-Head Latent Attention](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/163-multi-head-latent-attention-mla-cache-from-scratch-pytorch.ipynb) | MLA 低秩 KV、解耦 RoPE、矩阵吸收和逐 token latent cache 怎样实现并验证等价？ |
| 164 | [Multi-Token Prediction](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/164-multi-token-prediction-mtp-from-scratch-pytorch.ipynb) | 多 horizon 标签、文档边界、加权 loss、候选树和 verifier 接受前缀怎样实现？ |
| 165 | [Tensor Parallel Column/Row Linear](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/165-tensor-parallel-column-row-linear-from-scratch.ipynb) | Column/Row 切分、collective、vocab-parallel loss、梯度与 checkpoint 重分片怎样验证？ |
| 166 | [Pipeline Parallel 1F1B](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/166-pipeline-parallel-1f1b-scheduler-from-scratch.ipynb) | GPipe/1F1B 的依赖、bubble、激活内存、微批权重和 optimizer barrier 怎样设计？ |
| 167 | [RLVR 与可验证奖励](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/167-rlvr-verifiable-rewards-from-scratch-pytorch.ipynb) | 数学/代码 verifier、奖励分解、group advantage、策略 loss 和 reward hacking 门禁怎样实现？ |
| 168 | [Task Arithmetic、TIES 与 DARE](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/168-task-arithmetic-ties-dare-model-merging-from-scratch.ipynb) | 同 base 模型的 delta、冲突、trim、drop-rescale、scale 搜索和制品谱系怎样处理？ |
| 169 | [ColBERT Late Interaction](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/169-colbert-late-interaction-maxsim-from-scratch-pytorch.ipynb) | MaxSim、in-batch negatives、候选召回、residual compression 和索引版本怎样落地？ |
| 170 | [SPLADE Learned Sparse Retrieval](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/170-splade-learned-sparse-retrieval-from-scratch-pytorch.ipynb) | 学习型扩展、max pooling、FLOPS 正则、impact index、剪枝量化和 postings 怎样实现？ |
| 171 | [LLM Benchmark 去污染](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/171-llm-benchmark-decontamination-from-scratch.ipynb) | Exact、N-gram containment、MinHash、阈值、时间边界和 raw-clean score 怎样设计？ |
| 172 | [MCP Sampling、Elicitation 与 Roots](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/172-mcp-sampling-elicitation-roots-capability-from-scratch.ipynb) | Client Features、版本能力协商、有界 sampling loop、两类 elicitation 和 roots 怎样实现？ |
| 173 | [Agent Taint 与 Provenance](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/173-agent-taint-provenance-prompt-injection-defense-from-scratch.ipynb) | 外部内容污点怎样传播，并在 side-effect/egress sink 前结合用户意图、审批与 provenance 门禁？ |
| 174 | [Multi-Agent Debate 与相关共识](../25-modern-llm-architecture-retrieval-agent-safety-interview-questions/174-multi-agent-debate-correlated-consensus-from-scratch.ipynb) | 多数票何时失效，相关错误、簇限权、证据、Judge 偏差与停止预算怎样处理？ |

## 第十六组：LLM 动态计算、后训练、Agentic RAG 与 Agent Loop 面试题

这一组从模型内部的数值稳定、动态深度、提前退出、低比特网络与扩散式生成出发，进入 KTO/RLOO 后训练，再把检索反思、纠错路由、树搜索、隐藏状态估计和长期记忆治理接入 Agent Loop。每本都用基础算子或显式状态机暴露关键合同，并以 full-reference、梯度方向、边界输入或安全策略作为 correctness oracle。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 175 | [QK-Norm 与 Attention Logit Softcapping](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/175-qk-norm-attention-logit-softcapping-from-scratch-pytorch.ipynb) | Q/K 归一化、可学习温度、softcap 与 mask 的顺序和稳定性怎样验证？ |
| 176 | [Mixture-of-Depths Token Routing](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/176-mixture-of-depths-token-routing-from-scratch-pytorch.ipynb) | token top-k、固定容量、未选 token 旁路、路由梯度和 causal decode 怎样实现？ |
| 177 | [LayerSkip Early Exit 与 Self-Speculative](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/177-layerskip-early-exit-self-speculative-from-scratch-pytorch.ipynb) | 共享 LM head、early-exit loss、layer dropout、完整层验证与加速边界怎样设计？ |
| 178 | [BitNet b1.58 Ternary BitLinear](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/178-bitnet-b158-ternary-bitlinear-from-scratch-pytorch.ipynb) | absmean 三值量化、激活 int8、STE、整数点积、base-3 打包和真实存储怎样验证？ |
| 179 | [Masked Diffusion Language Model](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/179-masked-diffusion-language-model-from-scratch-pytorch.ipynb) | 前向 masking、时间条件、masked denoising loss、置信去噪和 infilling 怎样实现？ |
| 180 | [KTO Unpaired Preference Optimization](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/180-kto-unpaired-preference-optimization-from-scratch-pytorch.ipynb) | 单样本偏好下的 sequence log-ratio、KL 基线、loss aversion、梯度方向和类别失衡怎样处理？ |
| 181 | [RLOO / REINFORCE Leave-One-Out](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/181-rloo-reinforce-leave-one-out-from-scratch-pytorch.ipynb) | prompt-local LOO baseline、response mask、KL shaping、stale rollout 和无信号组怎样处理？ |
| 182 | [Self-RAG Adaptive Retrieval 与 Reflection](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/182-self-rag-adaptive-retrieval-reflection-from-scratch.ipynb) | Retrieve、ISREL、ISSUP、ISUSE 怎样控制按需检索、证据过滤、生成和有限重试？ |
| 183 | [Corrective RAG Retrieval Evaluator](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/183-corrective-rag-retrieval-evaluator-from-scratch.ipynb) | Correct/Ambiguous/Incorrect 三态怎样驱动 knowledge strips、外部 fallback、重组和降级？ |
| 184 | [LATS / MCTS Agent Planning](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/184-lats-mcts-agent-planning-from-scratch.ipynb) | Selection、Expansion、Simulation、Backpropagation 怎样用于工具规划并隔离真实副作用？ |
| 185 | [POMDP Belief-State Agent Loop](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/185-agent-pomdp-belief-state-loop-from-scratch.ipynb) | noisy observation 怎样更新 belief，期望效用和信息增益如何决定 inspect、execute 或 stop？ |
| 186 | [长期 Agent Memory 的巩固与遗忘](../26-llm-dynamic-posttraining-rag-agent-loop-interview-questions/186-agent-long-term-memory-consolidation-forgetting-from-scratch.ipynb) | 事实怎样追加、修订、按时点查询、失效、受权检索、压缩并接受遗忘评测？ |

## 第十七组：LLM 推理优化与 Agent 训练面试题

这一组连接推理内核与 Agent 后训练：EAGLE 的草稿—验证提交、H₂O 的 KV 淘汰、Native Sparse Attention 的 block 合同，以及 Agent trace 到 RL transition 的解耦；随后把同一套可验证合同用于有状态工具评测、代码 Agent、interruption-aware KV、跨工具副作用、多 Agent handoff、上下文压缩、MCP schema、动作前审批、RoPE 长上下文、流式协议、并行工具调用、chat template、Activation Steering、Contrastive Decoding、Semantic Entropy、知识编辑、水印、软提示、输出 PII、test-time compute 分配、SAE 稀疏特征、父子 RAG 回填、HyDE grounding、Agent 错误恢复、KV cache 非对称量化、LoRA adapter 池、批处理随机性、stop string 提交、Contextual Retrieval、RAPTOR 分层树、长上下文位置评测、Agent 停滞 gate、Text-to-SQL AST、GraphRAG local/global、valid-time RAG 和指令权威解析。每本都用可复放的小状态与断言区分“候选/近似”同“最终 target、权限或 learner 合同”。

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 187 | [EAGLE 特征级推测解码](../27-llm-inference-agent-training-interview-questions/187-eagle-feature-speculative-decoding-from-scratch.ipynb) | feature draft、最长接受前缀、target verifier 与 branch KV 怎样精确提交？ |
| 188 | [H₂O Heavy-Hitter KV Cache](../27-llm-inference-agent-training-interview-questions/188-h2o-heavy-hitter-kv-cache-from-scratch.ipynb) | 累计 attention、recent window、heavy-hitter budget 与因果顺序怎样决定淘汰？ |
| 189 | [Native Sparse Attention](../27-llm-inference-agent-training-interview-questions/189-native-sparse-attention-from-scratch.ipynb) | block selection、局部窗口、全局块、causal mask 与稀疏算量怎样实现？ |
| 190 | [Agent Lightning 轨迹 Credit Assignment](../27-llm-inference-agent-training-interview-questions/190-agent-lightning-trajectory-credit-assignment-from-scratch.ipynb) | 如何把 Agent event trace 转为 transition、return-to-go、train/eval group split 与 rollout version gate？ |
| 191 | [τ-bench 有状态工具评测](../27-llm-inference-agent-training-interview-questions/191-taubench-stateful-tool-agent-evaluation-from-scratch.ipynb) | 最终状态、用户确认、领域策略、工具 trace 与 pass^k 可靠性怎样一起评测？ |
| 192 | [SWE-bench 代码 Agent 沙箱](../27-llm-inference-agent-training-interview-questions/192-swe-bench-code-agent-sandbox-from-scratch.ipynb) | inspect、revision gate、patch、可执行测试、最小 diff 与评分制品怎样实现？ |
| 193 | [INFERCEPT 中断感知 Agent KV 恢复](../27-llm-inference-agent-training-interview-questions/193-infercept-interruption-aware-agent-kv-resume-from-scratch.ipynb) | tool/human interruption 怎样冻结 snapshot、正确复用 KV、预算准入或主动重算？ |
| 194 | [Agent Saga、补偿与幂等](../27-llm-inference-agent-training-interview-questions/194-agent-saga-compensation-idempotency-from-scratch.ipynb) | 跨工具副作用怎样通过 idempotency key、逆序 compensation、审计和人工例外安全收束？ |
| 195 | [多 Agent Supervisor/Worker 委派](../27-llm-inference-agent-training-interview-questions/195-multi-agent-supervisor-handoff-from-scratch.ipynb) | task、能力、预算、parent trace、输入版本、handoff 验收与循环上限怎样设计？ |
| 196 | [Agent Context 压缩与检索恢复](../27-llm-inference-agent-training-interview-questions/196-agent-context-compaction-retrieval-from-scratch.ipynb) | pinned 约束、预算、摘要覆盖范围、版本失配和原文 evidence retrieval 怎样实现？ |
| 197 | [MCP Tool Schema 版本与契约测试](../27-llm-inference-agent-training-interview-questions/197-mcp-tool-schema-versioning-contract-tests-from-scratch.ipynb) | protocol negotiation、schema validation、adapter、错误闭合与 golden contract tests 怎样实现？ |
| 198 | [Agent 动作前审批与 Policy Gate](../27-llm-inference-agent-training-interview-questions/198-agent-pre-action-approval-policy-gate-from-scratch.ipynb) | 风险分级、参数 digest、一次性 approval、过期/重放拒绝与审计怎样实现？ |
| 199 | [RoPE 长上下文缩放](../27-llm-inference-agent-training-interview-questions/199-rope-long-context-scaling-from-scratch.ipynb) | RoPE 相对位置、PI/YaRN 缩放、频率表、KV 坐标版本和短/长窗口评测怎样验证？ |
| 200 | [LLM 流式 API 事件与恢复](../27-llm-inference-agent-training-interview-questions/200-llm-streaming-events-sse-resume-from-scratch.ipynb) | delta 分类、sequence、terminal、usage、断连 replay、错误和流式指标怎样实现？ |
| 201 | [Agent 并行 Tool Call 一致性](../27-llm-inference-agent-training-interview-questions/201-agent-parallel-tool-call-id-consistency-from-scratch.ipynb) | call id、并行 dispatch、乱序 result commit、顺序 join、重复拒绝和 result ledger 怎样实现？ |
| 202 | [Chat Template 训练/服务一致性](../27-llm-inference-agent-training-interview-questions/202-chat-template-train-serving-compatibility-from-scratch.ipynb) | role token、tool call id、generation prompt、template fingerprint 与 golden rendering 怎样实现？ |
| 203 | [Activation Steering / Representation Engineering](../27-llm-inference-agent-training-interview-questions/203-activation-steering-representation-engineering-from-scratch.ipynb) | contrast direction、归一化、指定 layer/token 注入、剂量曲线、行为/任务/安全分桶评测怎样实现？ |
| 204 | [Contrastive Decoding](../27-llm-inference-agent-training-interview-questions/204-contrastive-decoding-expert-amateur-from-scratch.ipynb) | expert/amateur token 对齐、plausibility constraint、log-ratio 分数、空候选与质量评测怎样实现？ |
| 205 | [Semantic Entropy 不确定性与拒答](../27-llm-inference-agent-training-interview-questions/205-semantic-entropy-uncertainty-abstention-from-scratch.ipynb) | sample clustering、cluster mass entropy、多解/证据冲突、阈值校准与 risk-coverage 怎样实现？ |
| 206 | [ROME 风格知识编辑](../27-llm-inference-agent-training-interview-questions/206-rome-rank-one-knowledge-editing-from-scratch.ipynb) | rank-one delta、rewrite、paraphrase generalization、locality、冲突版本与 rollback 怎样验证？ |
| 207 | [LLM 绿色名单水印与检测](../27-llm-inference-agent-training-interview-questions/207-llm-greenlist-watermark-detection-from-scratch.ipynb) | keyed green list、logit bias、z-score、阈值、攻击切片和 key rotation 怎样实现？ |
| 208 | [Soft Prompt Tuning](../27-llm-inference-agent-training-interview-questions/208-soft-prompt-tuning-frozen-base-from-scratch.ipynb) | frozen base、连续 prompt forward/gradient、prompt registry、兼容性、租户隔离与发布制品怎样实现？ |
| 209 | [LLM 输出 PII Redaction Policy Gate](../27-llm-inference-agent-training-interview-questions/209-llm-output-pii-redaction-policy-gate-from-scratch.ipynb) | span scan、right-to-left redaction、mask/block、未知格式、最小化审计和检测指标怎样实现？ |
| 210 | [自适应 Test-Time Compute 预算分配](../27-llm-inference-agent-training-interview-questions/210-adaptive-test-time-compute-budget-allocation-from-scratch.ipynb) | value-cost 动作、全局组合预算 oracle、admission、regret、质量/成本/公平指标怎样实现？ |
| 211 | [Sparse Autoencoder LLM 可解释性](../27-llm-inference-agent-training-interview-questions/211-sparse-autoencoder-llm-interpretability-from-scratch.ipynb) | activation 编码、ReLU/top-k 稀疏化、重构误差、feature usage 和干预实验怎样验证？ |
| 212 | [RAG 父子切块与上下文回填](../27-llm-inference-agent-training-interview-questions/212-rag-parent-child-chunking-context-from-scratch.ipynb) | child 召回、parent 去重回填、ACL/版本门禁、双层引用与陈旧索引拒绝怎样实现？ |
| 213 | [HyDE Query Expansion、RRF 与 Grounding](../27-llm-inference-agent-training-interview-questions/213-hyde-query-expansion-rrf-grounding-from-scratch.ipynb) | 原 query/假设文档候选怎样融合，且如何保证答案只能引用真实文档？ |
| 214 | [Agent Tool Error Recovery 与熔断](../27-llm-inference-agent-training-interview-questions/214-agent-tool-error-recovery-circuit-breaker-from-scratch.ipynb) | 错误分类、幂等重试、指数退避、circuit breaker、fallback 和人工升级怎样实现？ |
| 215 | [KV Cache 非对称量化与异常值回退](../27-llm-inference-agent-training-interview-questions/215-llm-kv-cache-asymmetric-quantization-outlier-fallback-from-scratch.ipynb) | group-wise affine quantization、outlier residual、版本 gate、attention oracle 和字节账本怎样实现？ |
| 216 | [S-LoRA 多 Adapter 服务与版本化内存池](../27-llm-inference-agent-training-interview-questions/216-slora-multi-adapter-serving-versioned-pool-from-scratch.ipynb) | base+delta forward、租户授权、refcount 驱逐、兼容 batch、池满排队与不可变热更新怎样实现？ |
| 217 | [连续批处理 Batch-Invariant 随机采样](../27-llm-inference-agent-training-interview-questions/217-llm-continuous-batching-batch-invariant-sampling-from-scratch.ipynb) | request/step/seed 坐标 RNG、CDF sample、调度重排、全局 RNG 反例、trace 与版本 gate 怎样实现？ |
| 218 | [LLM 流式 Stop Sequence 安全提交](../27-llm-inference-agent-training-interview-questions/218-llm-streaming-stop-sequence-safe-commit-from-scratch.ipynb) | 前缀缓冲、跨 chunk 匹配、flush、overlap、finish reason 与 stop 配置门禁怎样实现？ |
| 219 | [RAG Contextual Retrieval 与来源版本](../27-llm-inference-agent-training-interview-questions/219-rag-contextual-retrieval-provenance-versioning-from-scratch.ipynb) | contextual index text、raw evidence、ACL、context model/version、失效和检索/引用双指标怎样实现？ |
| 220 | [RAPTOR 分层摘要检索与来源链](../27-llm-inference-agent-training-interview-questions/220-raptor-hierarchical-summary-retrieval-provenance-from-scratch.ipynb) | leaf、聚类、summary tree、level route、展开 evidence、树失效与错误传播怎样实现？ |
| 221 | [长上下文 Needle 位置鲁棒性评测](../27-llm-inference-agent-training-interview-questions/221-llm-long-context-needle-position-robustness-evaluation-from-scratch.ipynb) | 长度×位置×干扰、答案 parser、无答案/冲突对照、切片统计与版本可比性怎样实现？ |
| 222 | [Agent Loop 停滞检测与停止策略](../27-llm-inference-agent-training-interview-questions/222-agent-loop-stagnation-fingerprint-budget-stop-policy-from-scratch.ipynb) | action/state fingerprint、progress、budget、side-effect retry、fallback/escalation 和误杀评测怎样实现？ |
| 223 | [Text-to-SQL Schema Linking 与 Policy Gate](../27-llm-inference-agent-training-interview-questions/223-text-to-sql-schema-linking-policy-gate-from-scratch.ipynb) | schema candidate、受限 AST、表/列/角色/租户/limit、参数 SQL、执行 evidence 与版本 gate 怎样实现？ |
| 224 | [GraphRAG Local/Global Search 与来源](../27-llm-inference-agent-training-interview-questions/224-graphrag-local-global-community-provenance-from-scratch.ipynb) | entity/edge/chunk provenance、local neighborhood、community report map-reduce、raw evidence、ACL/version 和分层评测怎样实现？ |
| 225 | [Temporal RAG 有效时间、冲突与引用](../27-llm-inference-agent-training-interview-questions/225-temporal-rag-valid-time-conflict-citation-from-scratch.ipynb) | valid/published time、time-first retrieval、conflict gate、interval citation、追加更新与时态指标怎样实现？ |
| 226 | [Agent 指令层级冲突与来源控制](../27-llm-inference-agent-training-interview-questions/226-agent-instruction-hierarchy-conflict-provenance-from-scratch.ipynb) | authority、同级 clarify、external evidence、action gate、decision trace 与注入/误拒评测怎样实现？ |

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
14. 继续运行 `103–108 -> 109–114`：从方案判断与评测进入 Agent 工具/安全，再学习约束生成、记忆、SFT、RLHF 与模型路由。
15. 最后运行 `115–120 -> 121–126`：先实现单 Agent 控制面，再进入多 Agent、多跳 RAG、反思、安全执行、MCP 与全链路观测。
16. 继续运行 `127–132 -> 133–138`：先建立训练/推理系统底层，再学习 reasoning model 的策略优化、采样搜索、上下文压缩与过程验证。
17. 继续运行 `139–144 -> 145–150`：先贯通数据 mixture、目标函数、激活/KV 与低比特权重，再进入多租户推理、P/D 解耦和 Agent 互操作工程。
18. 继续运行 `151–156 -> 157–162`：先比较数值、并行、缓存和调度优化，再把同样的可验证合同应用到对齐、多模态、工具训练、授权与 Agent 可靠性。
19. 继续运行 `163–168 -> 169–174`：先验证现代架构、并行、RLVR 与模型合并，再把独立证据、版本和权限合同应用到检索、去污染、MCP 与多 Agent 安全决策。
20. 继续运行 `175–180 -> 181–186`：先比较动态计算、低比特与扩散生成的 correctness oracle，再串联偏好优化、Agentic RAG、树搜索、belief state 和长期记忆治理。
21. 继续运行 `187–222 -> 223–226`：在推理、Agent、表征、知识与发布边界之上，将自然语言落为受控结构化查询、图谱/时态证据，并把指令优先级、外部数据与危险动作分成可审计的三道门。

## 统一验收标准

- notebook JSON 符合 nbformat 4.5，每个 cell 有唯一 id；
- 从头到尾按顺序执行，不依赖前一次内核残留；
- 每个有效代码行都有中文行内注释；空行、纯注释行和多行字符串内容不作为代码行计数，注释仍应优先说明设计意图、张量形状、状态边界或失败分支；
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

# 机器学习系统面试题：问题驱动 Notebook

这里坚持“一道面试问题对应一本可运行 Notebook”。每本第一屏直接给出问题和回答主线，再依次展开需求/SLO、数据与版本合同、底层算法、可执行反例、离线评估、线上状态、失败处理、发布与回滚。核心实现只使用 Python 标准库、NumPy 或 PyTorch 基础算子，不调用网关、向量数据库、任务队列、监控平台、实验平台等高耦合组件代替答案。

| 编号 | 面试问题 | Notebook 回答 |
| --- | --- | --- |
| 79 | 你会怎样设计 LLM 推理的 continuous batching 调度器？ | [调度状态机、token/KV budget、尾延迟与公平性](./79-llm-continuous-batching-scheduler-from-scratch.ipynb) |
| 80 | 你会怎样设计多租户 RAG/LLM 语义缓存？ | [安全命名空间、语义阈值、TTL/LRU、失效与防击穿](./80-multitenant-semantic-cache-from-scratch.ipynb) |
| 81 | 向量数据库的分片、路由、复制、过滤和迁移怎样设计？ | [分片检索、全局 Top-K、副本故障与双路由迁移](./81-vector-database-sharding-replication-from-scratch.ipynb) |
| 82 | RAG 文档摄取怎样实现幂等更新、版本追踪和安全删除？ | [确定性 chunk、outbox、tombstone、对账与快照发布](./82-rag-ingestion-versioning-idempotency-from-scratch.ipynb) |
| 83 | 关键词、向量、实体等多路召回的配额、融合和超时降级怎样设计？ | [边际预算、RRF、通道消融、deadline 与 bootstrap](./83-multichannel-retrieval-budget-fusion-from-scratch.ipynb) |
| 84 | 分布式训练中的 Ring AllReduce 怎样实现，通信量如何计算？ | [Reduce-Scatter、All-Gather、精度、bucket 与 overlap](./84-ring-allreduce-distributed-training-from-scratch.ipynb) |
| 85 | 高并发服务如何限流，Token Bucket、Leaky Bucket 和滑动窗口怎样取舍？ | [三种算法、分层原子扣费、优先级和分布式故障策略](./85-rate-limiting-token-bucket-sliding-window-from-scratch.ipynb) |
| 86 | 任务队列怎样实现 at-least-once、幂等、重试和 DLQ？ | [visibility lease、generation receipt、账本、退避与 outbox](./86-at-least-once-job-queue-idempotency-from-scratch.ipynb) |
| 87 | 线上模型的数据漂移、预测漂移和性能退化怎样监控？ | [PSI、JS、KS、Page-Hinkley、延迟标签与迟滞告警](./87-ml-data-drift-monitoring-from-scratch.ipynb) |
| 88 | 模型上线怎样做 shadow、canary、灰度放量和自动回滚？ | [稳定分流、guardrail、序贯查看与发布状态机](./88-model-canary-shadow-rollback-from-scratch.ipynb) |
| 89 | 推荐/广告在线探索怎样实现 LinUCB，并处理 propensity 和延迟反馈？ | [LinUCB、regret、epsilon propensity、IPS/SNIPS 与安全候选](./89-contextual-bandit-linucb-delayed-feedback-from-scratch.ipynb) |
| 90 | 怎样用 Conformal Prediction 输出带覆盖率目标的区间或集合？ | [有限样本分位数、回归区间、分类集合、Mondrian 与漂移反例](./90-conformal-prediction-uncertainty-from-scratch.ipynb) |

所有实验使用固定 seed 的离线受控数据，目的在于验证机制与工程合同，不代表线上吞吐、模型质量或统计保证能无条件外推。生产替换组件后，仍应保留 Notebook 中展示的版本、隔离、评估、故障与回滚边界。

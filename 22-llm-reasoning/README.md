# LLM 系统与推理面试题

这一组继续采用“一道面试问题一本 Notebook”，覆盖大模型训练预算、分布式训练、推理内核、KV 缓存，以及 reasoning model 常见的 PPO、GRPO、Self-Consistency、Tree of Thoughts、Context Compaction 和 Process Reward Model。

每本都先给出可直接用于面试的回答主线，再用 Python、NumPy 或 PyTorch 基础张量实现关键公式、数据结构和状态机。示例不调用训练器、推理服务或 Agent 框架代替核心逻辑；受控数据只用于验证机制，不代表真实模型效果或 GPU kernel 性能。

## Notebook 索引

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 01 | [Scaling Law 与训练预算](./01-llm-scaling-law-compute-budget-from-scratch.ipynb) | 给定训练算力、数据上限和推理量，怎样选择参数量、训练 token 与集群工期？ |
| 02 | [LLM 3D 并行规划](./02-llm-3d-parallelism-planner-from-scratch.ipynb) | DP、TP、PP、Sequence Parallel 分别解决什么，怎样结合拓扑、显存和 bubble 选型？ |
| 03 | [ZeRO 分片与通信](./03-zero-sharding-memory-communication-from-scratch.ipynb) | ZeRO-1/2/3 分别切什么，参数生命周期、offload 和跨 world-size checkpoint 怎样实现？ |
| 04 | [FlashAttention 与 Online Softmax](./04-flash-attention-online-softmax-from-scratch.ipynb) | 为什么 FlashAttention 仍是精确 attention，运行最大值、分块和 causal mask 怎样实现？ |
| 05 | [PagedAttention KV Block Manager](./05-paged-attention-kv-block-manager-from-scratch.ipynb) | 动态 KV Cache 怎样做块表、按需增长、共享、Copy-on-Write、回收和准入？ |
| 06 | [Prefix Cache 与 Radix Trie](./06-prefix-cache-radix-trie-isolation-from-scratch.ipynb) | Prefix Cache 怎样匹配 token、复用完整块、版本失效、隔离租户并参与调度？ |
| 07 | [LLM PPO](./07-llm-ppo-token-level-kl-gae-from-scratch-pytorch.ipynb) | RLHF 中 token-level KL、末端 reward、GAE、policy/value clip 和 response mask 怎样串联？ |
| 08 | [GRPO](./08-grpo-group-relative-policy-optimization-from-scratch-pytorch.ipynb) | Group-relative advantage 为什么能省 critic，零方差、clip、KL 和 stale rollout 怎样处理？ |
| 09 | [Self-Consistency](./09-self-consistency-correlated-voting-from-scratch.ipynb) | 多路径投票为什么有效，怎样处理 parser、相关错误、加权投票、聚类和提前停止？ |
| 10 | [Tree of Thoughts](./10-tree-of-thought-budgeted-search-from-scratch.ipynb) | Thought 怎样变成状态，generator、evaluator、剪枝、回溯、verifier 与预算怎样设计？ |
| 11 | [Agent Context Compaction](./11-agent-context-compaction-structured-memory-from-scratch.ipynb) | 长时间 Agent 怎样压缩上下文，同时保留事实来源、工具制品、权限和恢复能力？ |
| 12 | [Process Reward 与 Verifier Search](./12-process-reward-verifier-guided-search-from-scratch.ipynb) | PRM 与 ORM 有何区别，step 标签、masked loss、路径聚合和 verifier-guided search 怎样实现？ |

## 建议学习路线

1. 运行 01–03：从单次训练预算进入多卡 mesh、模型状态分片与恢复。
2. 运行 04–06：理解 attention 算法本身、动态 KV 物理内存和跨请求前缀复用的三个不同层次。
3. 运行 07–08：对比 PPO 的 value/GAE 与 GRPO 的组内相对基线，重点检查 old/reference policy 和 token mask。
4. 运行 09–12：从多样化采样进入显式搜索、长程上下文维护和 step-level verifier。

## 高频误区

- Scaling Law 是限定模型族与训练配方下的经验拟合，不是可以跨数据集直接搬用的自然常数。
- TP、PP、DP 的乘积等于 GPU 数只是必要条件，还要满足维度整除、拓扑、显存和有效 batch。
- FlashAttention 降低 HBM IO 与中间矩阵存储，但没有把精确 attention 的算术复杂度变成线性。
- PagedAttention 解决 KV 物理块管理；Prefix Cache 解决跨请求逻辑前缀复用，两者不能混为一个概念。
- GRPO 不需要 critic，并不代表不需要 old policy、reference KL、组内多样性和稳定奖励。
- Self-Consistency、ToT 与 PRM 都增加 test-time compute；必须报告相对简单基线的单位成本净收益。
- Context Compaction 的原始事件日志仍是事实源，摘要不能无来源地升级权限或覆盖未完成任务。

## 主要研究入口

本组以原始论文和官方工程资料为主，包括 [Chinchilla](https://arxiv.org/abs/2203.15556)、[Megatron 3D Parallelism](https://arxiv.org/abs/2104.04473)、[ZeRO](https://arxiv.org/abs/1910.02054)、[FlashAttention](https://arxiv.org/abs/2205.14135)、[PagedAttention](https://arxiv.org/abs/2309.06180)、[DeepSeekMath / GRPO](https://arxiv.org/abs/2402.03300)、[Tree of Thoughts](https://arxiv.org/abs/2305.10601)、[Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) 与 [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)。

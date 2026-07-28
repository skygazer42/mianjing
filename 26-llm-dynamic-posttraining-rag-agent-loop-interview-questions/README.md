# LLM 动态计算、后训练、Agentic RAG 与 Agent Loop 面试题

这一组继续采用“一道面试问题一本 Notebook”，覆盖 QK-Norm 与 logit softcapping、Mixture-of-Depths、LayerSkip、BitNet b1.58、masked diffusion language model、KTO、RLOO、Self-RAG、CRAG、LATS、POMDP Agent Loop 和长期记忆治理。

每本先给出可直接用于面试的回答主线，再用 Python、NumPy 或 PyTorch 基础算子手写核心公式、模型模块或有界状态机。代码单元均包含解释设计意图和边界的中文注释，并用受控数据与断言验证不变量；这些教学实现不冒充训练大模型的质量、线上吞吐或真实工具环境的安全性。

## Notebook 索引

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 175 | [QK-Norm 与 Attention Logit Softcapping](./175-qk-norm-attention-logit-softcapping-from-scratch-pytorch.ipynb) | Q/K 归一化、可学习温度和 logit softcap 分别解决什么，怎样手写并验证不会破坏 mask？ |
| 176 | [Mixture-of-Depths Token Routing](./176-mixture-of-depths-token-routing-from-scratch-pytorch.ipynb) | MoD 与 MoE 有何区别，token top-k、固定容量、旁路 residual、训练路由和自回归推理怎样实现？ |
| 177 | [LayerSkip Early Exit 与 Self-Speculative](./177-layerskip-early-exit-self-speculative-from-scratch-pytorch.ipynb) | 怎样让中间层直接预测 token，并用剩余层验证，early-exit loss、layer dropout、接受率和缓存复用如何设计？ |
| 178 | [BitNet b1.58 Ternary BitLinear](./178-bitnet-b158-ternary-bitlinear-from-scratch-pytorch.ipynb) | 1.58-bit 为什么是三值权重，absmean 量化、STE、master weight、整数计算和真实存储收益怎样验证？ |
| 179 | [Masked Diffusion Language Model](./179-masked-diffusion-language-model-from-scratch-pytorch.ipynb) | 扩散 LLM 与自回归 LLM 有何区别，前向 masking、时间条件、masked loss、置信去噪与 infilling 怎样实现？ |
| 180 | [KTO Unpaired Preference Optimization](./180-kto-unpaired-preference-optimization-from-scratch-pytorch.ipynb) | 只有 desirable/undesirable 单样本时怎样做偏好优化，sequence log-ratio、KL reference point 和 loss aversion 如何实现？ |
| 181 | [RLOO / REINFORCE Leave-One-Out](./181-rloo-reinforce-leave-one-out-from-scratch-pytorch.ipynb) | Leave-One-Out baseline 怎样降低方差，response token loss、KL shaping、stale rollout 和零方差组怎样处理？ |
| 182 | [Self-RAG Adaptive Retrieval 与 Reflection](./182-self-rag-adaptive-retrieval-reflection-from-scratch.ipynb) | Reflection token 分别控制什么，Retrieve、ISREL、ISSUP、ISUSE 怎样组成可评测的有界状态机？ |
| 183 | [Corrective RAG Retrieval Evaluator](./183-corrective-rag-retrieval-evaluator-from-scratch.ipynb) | CRAG 的 Correct/Ambiguous/Incorrect 分支如何设计，knowledge strip、外部检索和重组怎样避免引入更多噪声？ |
| 184 | [LATS / MCTS Agent Planning](./184-lats-mcts-agent-planning-from-scratch.ipynb) | Selection、Expansion、Simulation、Backpropagation 如何落到工具环境，为什么不能在真实副作用上随意分支？ |
| 185 | [POMDP Belief-State Agent Loop](./185-agent-pomdp-belief-state-loop-from-scratch.ipynb) | 为什么 observation 不等于真实 state，Agent 怎样用 noisy tool result 更新 belief，并在高风险动作前主动取证？ |
| 186 | [长期 Agent Memory 的巩固与遗忘](./186-agent-long-term-memory-consolidation-forgetting-from-scratch.ipynb) | 记忆不只是向量库：事实如何追加、修订、失效、检索、压缩，并避免继续使用过期偏好？ |

## 建议学习路线

1. 运行 175–179：从注意力数值稳定进入 token 级动态深度、层级提前退出、三值网络与非自回归式去噪，始终用 full-reference 或边界不变量区分“公式正确”和“实际加速”。
2. 运行 180–181：比较 unpaired KTO 与 grouped RLOO 的数据合同、基线和梯度方向，重点核对 reference、mask、rollout policy 与 reward 版本。
3. 运行 182–183：先让 Self-RAG 学会按需检索和自我批判，再让 CRAG 在召回失败时路由、切片和降级；相关、支持、有用和来源可信必须分开判断。
4. 运行 184–186：最后把树搜索、隐藏状态估计和长期记忆放入 Agent Loop，明确模拟与真实执行、观察与世界状态、审计保留与停止召回之间的边界。

## 高频误区

- QK-Norm 和 softcap 都是稳定性机制，不会替代 causal/padding mask，也不能只凭较小 logit 宣称质量更高。
- MoD 的 top-k 是 token 深度路由，MoE 的 top-k 是专家路由；理论 FLOPs 下降不等于 wall-clock 延迟必然下降。
- Early exit 的高置信不等于预测正确；self-speculative 还必须由完整模型验证最长可接受前缀。
- “1.58 bit”描述三值权重的信息下界，不包含 scale、布局、激活、master weight 与 kernel 元数据。
- Masked diffusion 可以并行去噪，但步数、重掩码策略和双向条件决定实际速度与质量，不能直接套用自回归 perplexity 结论。
- KTO 不要求成对偏好，RLOO 需要同 prompt 多个 rollout；把二者的数据分组和 baseline 混用会改变目标。
- Self-RAG 的 reflection token 与 CRAG 的 evaluator 都可能误判，需要单独校准、记录分支率并设置有限重试。
- MCTS 里的模拟轨迹不是已执行事实；带副作用工具只能在隔离模型中搜索，提交前必须重新鉴权与审批。
- POMDP belief 是基于观测模型的概率摘要，不是真实状态；相关或陈旧观测会导致过度自信。
- 长期记忆删除不是简单删向量：线上停止召回、版本失效、审计保留和法定物理删除是不同合同。

## 主要研究入口

动态架构与生成部分参考 [Query-Key Normalization](https://arxiv.org/abs/2010.04245)、[Mixture-of-Depths](https://arxiv.org/abs/2404.02258)、[LayerSkip](https://arxiv.org/abs/2404.16710)、[BitNet b1.58](https://arxiv.org/abs/2402.17764) 与 [Masked Diffusion Language Models](https://arxiv.org/abs/2406.07524)。

后训练、RAG 与 Agent 部分参考 [KTO](https://arxiv.org/abs/2402.01306)、[RLOO](https://arxiv.org/abs/2402.14740)、[Self-RAG](https://arxiv.org/abs/2310.11511)、[CRAG](https://arxiv.org/abs/2401.15884)、[LATS](https://arxiv.org/abs/2310.04406)、[OSWorld](https://arxiv.org/abs/2404.07972) 与 [MemGPT](https://arxiv.org/abs/2310.08560)。

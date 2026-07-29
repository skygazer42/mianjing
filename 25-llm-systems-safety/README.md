# 现代 LLM 架构、检索与 Agent 安全面试题

这一组继续采用“一道面试问题一本 Notebook”，覆盖 MLA、Multi-Token Prediction、Tensor/Pipeline Parallel、RLVR、模型合并、ColBERT、SPLADE、评测去污染，以及 MCP Client Features、Agent 污点传播和 Multi-Agent Debate。

每本先给出可直接用于面试的回答主线，再用 Python、NumPy 或 PyTorch 基础算子实现核心公式、模型模块、调度器或策略状态机。所有代码单元都有必要的中文注释和可执行断言；小张量、单进程 collective 与离线协议模拟只验证机制，不冒充真实模型质量、集群性能或生产安全。

## Notebook 索引

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 01 | [Multi-Head Latent Attention](./01-multi-head-latent-attention-mla-cache-from-scratch-pytorch.ipynb) | MLA 压缩了什么，低秩 KV、解耦 RoPE、矩阵吸收和逐 token latent cache 怎样实现并验证等价？ |
| 02 | [Multi-Token Prediction](./02-multi-token-prediction-mtp-from-scratch-pytorch.ipynb) | 多 horizon 标签、packed-document mask、加权 loss、候选树和 verifier 接受前缀怎样实现？ |
| 03 | [Tensor Parallel Column/Row Linear](./03-tensor-parallel-column-row-linear-from-scratch.ipynb) | Column/Row Parallel 为什么这样切，All-Gather/All-Reduce、vocab loss、梯度和重分片怎样验证？ |
| 04 | [Pipeline Parallel 1F1B](./04-pipeline-parallel-1f1b-scheduler-from-scratch.ipynb) | GPipe 与 1F1B 的依赖、warmup/steady/cooldown、bubble、激活峰值和更新屏障怎样设计？ |
| 05 | [RLVR 与可验证奖励](./05-rlvr-verifiable-rewards-from-scratch-pytorch.ipynb) | 数学/代码 verifier、奖励分解、group advantage、clipped loss 和 reward hacking 门禁怎样实现？ |
| 06 | [Task Arithmetic、TIES 与 DARE](./06-task-arithmetic-ties-dare-model-merging-from-scratch.ipynb) | 多个同 base 微调模型怎样处理 delta、符号冲突、trim、drop-rescale、scale 搜索和发布？ |
| 07 | [ColBERT Late Interaction](./07-colbert-late-interaction-maxsim-from-scratch-pytorch.ipynb) | token-level MaxSim、in-batch loss、候选召回、residual compression 和索引版本怎样落地？ |
| 08 | [SPLADE Learned Sparse Retrieval](./08-splade-learned-sparse-retrieval-from-scratch-pytorch.ipynb) | 学习型词表扩展、`log1p(ReLU)`、max pooling、FLOPS 正则和 impact index 怎样实现？ |
| 09 | [LLM Benchmark 去污染](./09-llm-benchmark-decontamination-from-scratch.ipynb) | Exact、N-gram containment、MinHash、阈值校准、时间边界和 raw-clean score 怎样设计？ |
| 10 | [MCP Sampling、Elicitation 与 Roots](./10-mcp-sampling-elicitation-roots-capability-from-scratch.ipynb) | Client Features 如何协商，sampling tool loop、form/URL elicitation、roots 与审批预算怎样实现？ |
| 11 | [Agent Taint 与 Provenance](./11-agent-taint-provenance-prompt-injection-defense-from-scratch.ipynb) | 外部内容污点怎样穿过摘要/解析传播，并在网络、写入等危险 sink 前做确定性门禁？ |
| 12 | [Multi-Agent Debate 与相关共识](./12-multi-agent-debate-correlated-consensus-from-scratch.ipynb) | 多数票何时失效，相关错误、簇限权、证据去重、Judge 偏差和停止预算怎样处理？ |

## 建议学习路线

1. 运行 01–04：先从模型内部的 cache/辅助头进入设备内张量切分与设备间流水调度，始终用 full-reference oracle 验证近似和并行路径。
2. 运行 05–06：比较“优化同一个模型”和“组合多个模型”两类后训练手段，重点检查 verifier、holdout、冲突与制品谱系。
3. 运行 07–09：从多向量检索到学习型稀疏检索，再进入评测污染；理解质量提升必须排除候选漏召、索引错配和训练—评测重叠。
4. 运行 10–12：最后把 Agent 能力、数据来源和多方决策串起来，区分协议能力、真正权限、证据独立性与系统级安全控制。

## 高频误区

- MLA 的结构性缓存压缩不等于量化；显式重建数学正确，也不代表已经获得硬件加速。
- MTP 多预测几个 token 不会自动带来无偏加速；跨文档标签和首个拒绝后的 token 都不能继续使用。
- TP/PP 的“切分能运行”不等于 forward/gradient/权重版本正确；collective 与更新屏障是语义的一部分。
- Verifier 是 RLVR 的规格和攻击面；错误或可投机的 verifier 会把优化推向错误目标。
- 模型合并只对共享同一 base 和参数语义的 checkpoint 有合理前提，参数范数小不代表任务回归小。
- ColBERT/SPLADE 的离线矩阵得分不代表检索系统完成；候选 recall、postings、ACL、压缩和版本共同决定线上结果。
- 去污染规则过松会漏报，过严会选择性删难题；必须发布命中证据、阈值版本和 raw/clean 两套分数。
- MCP Roots 是信息提示，不是操作系统沙箱；能力协商也不等于用户批准了每次高风险动作。
- 清洗外部文本或让模型“忽略注入”不能洗掉 untrusted provenance，side-effect sink 仍需确定策略。
- 多个同源 Agent 的一致可能只是相关错误；克隆数量、重复证据和自报置信都不能当独立事实。

## 主要研究入口

架构与训练部分参考 [DeepSeek-V2](https://arxiv.org/abs/2405.04434)、[Multi-token Prediction](https://arxiv.org/abs/2404.19737)、[Megatron-LM](https://arxiv.org/abs/1909.08053)、[GPipe](https://arxiv.org/abs/1811.06965)、[Tülu 3](https://arxiv.org/abs/2411.15124)、[TIES](https://arxiv.org/abs/2306.01708) 与 [DARE](https://arxiv.org/abs/2311.03099)。

检索、协议与安全部分参考 [ColBERT](https://arxiv.org/abs/2004.12832)、[SPLADE](https://arxiv.org/abs/2107.05720)、[训练数据去重](https://arxiv.org/abs/2107.06499)、[MCP 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/index)、[AgentDojo](https://arxiv.org/abs/2406.13352) 与 [Multiagent Debate](https://arxiv.org/abs/2305.14325)。

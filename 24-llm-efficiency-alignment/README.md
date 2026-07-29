# LLM 效率、对齐与 Agent 评测面试题

这一组继续采用“一道面试问题一本 Notebook”，覆盖 FP8、长上下文并行、MoE Expert Parallel、KV Cache 量化、推理 Roofline、Chunked Prefill，以及 Constitutional AI、拒绝采样微调、多模态指令模型、Tool-use SFT、Agent 委托授权和长程评测。

每本都先给出面试回答主线，再用 Python、NumPy 或 PyTorch 基础算子实现核心公式、模型模块或状态机。所有代码单元都有必要的中文注释与可执行断言；受控模拟验证机制和失败边界，不冒充真实 GPU kernel、在线安全系统或模型泛化结果。

## Notebook 索引

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 01 | [FP8 格式与 Delayed Scaling](./01-fp8-format-delayed-scaling-from-scratch.ipynb) | E4M3/E5M2 怎样取舍，scale、amax history、margin、饱和与高精度主权重怎样实现？ |
| 02 | [Ring Attention 与 Context Parallel](./02-ring-attention-context-parallel-from-scratch.ipynb) | 序列怎样跨设备切分，KV block 如何绕 ring，并用 online softmax 保持精确 causal attention？ |
| 03 | [MoE Expert Parallel 与负载均衡](./03-moe-expert-parallel-load-balancing-from-scratch.ipynb) | Top-k、capacity、dispatch/All-to-All、专家合并、辅助损失和 loss-free bias 怎样实现？ |
| 04 | [KV Cache 低比特量化](./04-kv-cache-quantization-from-scratch.ipynb) | 为什么 K/V 常采用不同 qparam 轴，2-bit packing、residual window 和 attention 误差怎样验证？ |
| 05 | [LLM 推理 Roofline 与容量规划](./05-llm-inference-roofline-capacity-from-scratch.ipynb) | Prefill/decode 为什么分别偏计算/带宽受限，AI、延迟下界、batch 摊销和副本数怎样估算？ |
| 06 | [Chunked Prefill 调度器](./06-chunked-prefill-scheduler-from-scratch.ipynb) | 怎样保护 decode TPOT、推进长 prompt、处理 KV 准入、绝对位置、公平和 chunk-size 搜索？ |
| 07 | [Constitutional AI 与 RLAIF](./07-constitutional-ai-rlaif-pipeline-from-scratch.ipynb) | 原则怎样变成 critique/revision、AI preference、reward 数据、冲突升级和发布门禁？ |
| 08 | [Rejection Sampling Fine-Tuning](./08-rejection-sampling-finetuning-bestofn-from-scratch-pytorch.ipynb) | Best-of-N 怎样过滤、排序、去重、控制 reward 偏差，再做 assistant-only SFT 与迭代评测？ |
| 09 | [LLaVA 风格视觉语言模型](./09-llava-vision-language-projector-from-scratch-pytorch.ipynb) | 怎样手写 patch encoder、projector、视觉 token 拼接、causal decoder、loss mask 和两阶段训练？ |
| 10 | [Tool-use SFT 轨迹与 Loss Mask](./10-tool-use-sft-trajectory-loss-mask-from-scratch.ipynb) | 调用/结果事件怎样校验、序列化、监督、原子截断、隔离坏轨迹并执行式评测？ |
| 11 | [Agent OAuth 委托授权](./11-agent-oauth-delegated-authorization-from-scratch.ipynb) | Audience、scope、token exchange、DPoP、replay、step-up approval 怎样防 confused deputy？ |
| 12 | [长程 Agent Eval 与 pass@k/pass^k](./12-long-horizon-agent-evaluation-passk-from-scratch.ipynb) | 状态式任务、组合 grader、多 trial、paired bootstrap、trace replay 和污染门禁怎样设计？ |

## 建议学习路线

1. 运行 01–03：从单张量数值格式进入序列并行和专家并行，始终区分数学等价、通信组织与硬件 kernel。
2. 运行 04–06：把 KV/权重/计算字节放进同一容量模型，再实现兼顾 TTFT、TPOT 与公平性的调度策略。
3. 运行 07–10：比较原则反馈、Best-of-N、多模态指令和工具轨迹四类训练数据的 provenance 与 loss mask。
4. 运行 11–12：最后进入 Agent 的执行权限和评测证据，理解“能完成一次”与“持续可靠且无越权”的区别。

## 高频误区

- FP8 格式、scale recipe 与 Tensor Core kernel 是三层问题；仿真误差小不代表训练稳定或真实加速。
- Ring Attention 遍历全部 KV block，仍是二次计算；它扩展单设备可容纳的序列，不是线性 attention 近似。
- MoE 激活参数少不等于通信少；最热 expert、最慢 rank、capacity drop 和 All-to-All 拓扑决定尾部。
- KV 量化的 K per-channel、V per-token 来自经验分布，必须对目标层/头校准，不能背成不可变规则。
- Roofline 是硬件上界模型而非延迟预测器；实测差距还包含 kernel、同步、通信、padding 和排队。
- Chunk 越小不一定越好：TPOT 干扰降低的同时，启动开销和长 prompt TTFT 可能上升。
- Constitutional AI 的 principle 与 AI judge 都可能有盲点；冲突、高影响 slice 和低置信仍需人审。
- Best-of-N 会提高观测 reward，也会放大奖励模型漏洞和选择分布偏移；必须用独立 evaluator 验收。
- LLaVA 的 projector 对齐视觉/语言空间，但视觉 token 数、冻结策略和 grounding 数据共同决定效果。
- Tool result 是外部观察，不应默认作为模型输出监督；call-result 也不能在截断时被拆开。
- OAuth scope 不是对象级授权；Agent token 还需精确 audience、tenant、ACL、proof 与动作审批。
- `pass@k` 会随尝试次数上升，`pass^k` 会下降；面向用户的可靠性不能只报“多试总能成功”。

## 主要研究入口

效率部分参考 [FP8 Formats](https://arxiv.org/abs/2209.05433)、[Ring Attention](https://arxiv.org/abs/2310.01889)、[DeepSeek-V3](https://arxiv.org/abs/2412.19437)、[KIVI](https://arxiv.org/abs/2402.02750)、[Roofline](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-134.pdf) 与 [SARATHI](https://arxiv.org/abs/2308.16369)。

对齐与 Agent 部分参考 [Constitutional AI](https://arxiv.org/abs/2212.08073)、[Llama 2](https://arxiv.org/abs/2307.09288)、[LLaVA](https://arxiv.org/abs/2304.08485)、[Toolformer](https://arxiv.org/abs/2302.04761)、[MCP Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) 与 [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)。

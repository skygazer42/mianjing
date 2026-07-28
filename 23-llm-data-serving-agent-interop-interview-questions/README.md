# LLM 数据、推理服务与 Agent 互操作面试题

这一组继续采用“一道面试问题一本 Notebook”，补齐预训练数据配方、语言模型评估、显存换算、低比特推理、多租户服务，以及 Agent 互操作、Computer Use、工具设计和渐进式技能加载等工程高频题。

每本先给出可直接用于面试的回答框架，再用 Python、NumPy 或 PyTorch 基础算子实现核心公式、数据结构和状态机。代码单元都配有必要的中文注释和可执行断言；受控小数据用于验证机制与失败边界，不代表真实集群吞吐或线上模型质量。

## Notebook 索引

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 139 | [预训练数据混合与 DoReMi](./139-llm-pretraining-data-mixture-sampling-from-scratch.ipynb) | 多领域语料怎样设定 mixture、temperature、上下界与反馈更新，并避免小域过采样和验证集污染？ |
| 140 | [Causal LM Loss、PPL 与 BPB](./140-causal-lm-loss-perplexity-bpb-from-scratch-pytorch.ipynb) | next-token shift、padding/文档边界 mask、分布式聚合、滑窗评分和跨 tokenizer 比较怎样做对？ |
| 141 | [Activation Checkpointing 与重计算](./141-activation-checkpointing-recomputation-from-scratch.ipynb) | 激活显存由什么决定，重计算怎样换显存，RNG、原地修改和副作用为什么会破坏梯度？ |
| 142 | [MHA、MQA、GQA 与 KV Cache](./142-mha-mqa-gqa-kv-cache-from-scratch.ipynb) | 三种注意力怎样映射 query head 与 KV head，输出如何等价验证，KV 显存和带宽怎样估算？ |
| 143 | [Attention Sink 与滚动 KV](./143-streaming-attention-sink-rolling-kv-from-scratch.ipynb) | 流式长文本怎样保留 sink、淘汰局部 token、维护绝对位置，并识别有限窗口无法回答的问题？ |
| 144 | [GPTQ、AWQ 与 Weight-only Quantization](./144-gptq-awq-weight-only-quantization-from-scratch.ipynb) | group-wise 量化、校准激活、显著通道保护、误差指标、元数据和发布门禁怎样实现？ |
| 145 | [多租户 LoRA Adapter Serving](./145-multitenant-lora-adapter-serving-from-scratch.ipynb) | 一个共享基座怎样批量服务多 adapter，处理版本、缓存淘汰、租户隔离、热更新和回退？ |
| 146 | [Prefill–Decode 解耦与路由](./146-prefill-decode-disaggregation-router-from-scratch.ipynb) | 为什么拆分 prefill/decode，KV 传输、节点选择、准入、SLO、goodput 和故障降级怎样权衡？ |
| 147 | [A2A Agent Card 与 Task 生命周期](./147-a2a-agent-card-task-lifecycle-from-scratch.ipynb) | Agent 怎样发现彼此、协商能力并管理 task、message、artifact、流式事件、取消和终态？ |
| 148 | [Computer-use Agent 安全闭环](./148-computer-use-agent-grounding-safety-loop-from-scratch.ipynb) | screenshot–ground–act–observe 循环怎样处理坐标映射、陈旧画面、动作审批、幂等与轨迹评估？ |
| 149 | [Agent Tool Schema 设计与评测](./149-agent-tool-schema-design-evaluation-from-scratch.ipynb) | 工具名称、描述、JSON Schema、错误语义、分页、幂等和选择/参数/执行分层指标怎样设计？ |
| 150 | [Agent Skills 渐进式披露](./150-agent-skills-progressive-disclosure-from-scratch.ipynb) | 大量技能怎样只暴露元数据、按需加载说明和资源，同时保证路径、完整性、版本与路由可评测？ |

## 建议学习路线

1. 运行 139–141：从训练数据分布进入 token-level 目标、可比指标和激活显存，用同一套“分子/分母/边界”思维检查训练链路。
2. 运行 142–144：依次理解 KV 头共享、有限缓存和权重量化；每一步都先做数值 oracle，再讨论 kernel 与硬件优化。
3. 运行 145–146：把单请求算法放进多租户服务，重点计算 adapter/KV 的驻留、搬运、排队和尾延迟成本。
4. 运行 147–150：从跨 Agent 任务协议进入 GUI 动作、工具 API 与技能包；比较“通信协议、动作能力、知识封装”三种不同抽象。

## 高频误区

- 数据 mixture 不是按原始语料量直接采样；去重、质量、epoch 上限和目标分布必须一起版本化。
- PPL 必须按有效 token 的总负对数似然聚合；先平均各 batch 的 PPL 会产生错误权重，跨 tokenizer 更应报告 BPB 等可比量。
- Activation Checkpointing 主要减少保存的激活，不会自动减少参数、梯度和优化器状态；随机算子还要恢复一致的 RNG。
- MQA/GQA 减少 KV head，并不等于随意平均已经生成的缓存；head 映射、RoPE 位置和 checkpoint 转换必须明确。
- Attention Sink 与滚动窗口只改善有限缓存下的稳定性，不能恢复已经淘汰的事实，也不是长上下文能力的充分条件。
- GPTQ/AWQ 都依赖代表性校准数据；只看权重重建误差，不能替代端到端质量、延迟、峰值显存和 kernel 支持检查。
- 多 LoRA 服务的难点不只是低秩乘法，还包括 adapter 身份、基座兼容、批内分组、缓存抖动和跨租户隔离。
- Prefill–decode 解耦不是必然提速：KV 传输与排队成本超过资源隔离收益时，应保留共置或降级路径。
- A2A 负责 Agent 间任务协作，工具/资源协议负责 Agent 与能力之间的连接；二者可以组合，但不能混成一个生命周期。
- Computer-use Agent 每次高风险动作前都应验证当前画面与目标；旧截图坐标正确，也可能在页面变化后点错对象。
- Tool Schema 和 Skill 都是需要版本、权限、来源与回归评测的接口契约，不能把模型“看懂描述”当作可靠性保证。

## 主要研究入口

数据与训练部分参考 [DoReMi](https://arxiv.org/abs/2305.10429)、[The Pile](https://arxiv.org/abs/2101.00027)、[DataComp-LM](https://arxiv.org/abs/2406.11794) 和 [PyTorch Checkpoint 文档](https://pytorch.org/docs/stable/checkpoint.html)；注意力与量化部分参考 [GQA](https://arxiv.org/abs/2305.13245)、[StreamingLLM](https://arxiv.org/abs/2309.17453)、[GPTQ](https://arxiv.org/abs/2210.17323) 与 [AWQ](https://arxiv.org/abs/2306.00978)。

服务与 Agent 部分参考 [Punica](https://arxiv.org/abs/2310.18547)、[S-LoRA](https://arxiv.org/abs/2311.03285)、[DistServe](https://arxiv.org/abs/2401.09670)、[A2A 1.0 Specification](https://github.com/a2aproject/A2A/blob/main/docs/specification.md)、[OSWorld](https://arxiv.org/abs/2404.07972)、[Writing Effective Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) 与 [Agent Skills Specification](https://agentskills.io/specification)。

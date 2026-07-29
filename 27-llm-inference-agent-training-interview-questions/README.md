# LLM 推理优化与 Agent 训练面试题

这一组继续采用“一道面试问题一本 Notebook”，从 EAGLE 特征级推测解码、H₂O heavy-hitter KV cache、Native Sparse Attention 与 Agent Lightning 式轨迹切片/credit assignment，延伸到有状态 Tool-Agent-User 评测、代码 Agent 沙箱、可中断 KV 恢复、工具副作用补偿、多 Agent 委派、上下文压缩、MCP 契约、动作前审批、RoPE 长上下文、流式协议、并行工具调用、chat template、Activation Steering、Contrastive Decoding、Semantic Entropy 与知识编辑。

每本使用 Python、NumPy 与标准库手写关键状态机、缓存或训练数据合同。每个有效代码行都有中文行内注释；小数据断言只验证实现不变量，不代表大模型吞吐、真实工具安全或线上泛化。

## Notebook 索引

| 编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 187 | [EAGLE 特征级推测解码](./187-eagle-feature-speculative-decoding-from-scratch.ipynb) | feature draft、最长接受前缀、target verifier 与 branch KV 如何保证精确提交？ |
| 188 | [H₂O Heavy-Hitter KV Cache](./188-h2o-heavy-hitter-kv-cache-from-scratch.ipynb) | 累计 attention score、recent window 与容量预算如何共同决定淘汰？ |
| 189 | [Native Sparse Attention](./189-native-sparse-attention-from-scratch.ipynb) | block 选择、局部窗口、全局块、causal mask 与稀疏算量如何实现和验证？ |
| 190 | [Agent Lightning 轨迹 Credit Assignment](./190-agent-lightning-trajectory-credit-assignment-from-scratch.ipynb) | 怎样把 Agent event trace 切为 transition，计算 return-to-go，并用版本门禁隔离 rollout 与 learner？ |
| 191 | [τ-bench 有状态 Tool-Agent-User 评测](./191-taubench-stateful-tool-agent-evaluation-from-scratch.ipynb) | 怎样同时验证最终数据库状态、用户确认、领域策略和多次运行可靠性？ |
| 192 | [SWE-bench 代码 Agent 沙箱](./192-swe-bench-code-agent-sandbox-from-scratch.ipynb) | observe、patch、test、revision gate 和最小变更约束怎样做成可复放 loop？ |
| 193 | [INFERCEPT 中断感知 KV 恢复](./193-infercept-interruption-aware-agent-kv-resume-from-scratch.ipynb) | 怎样区分 pause 与结束、用 snapshot 防止错误 KV 复用，并在显存预算下选择保留或重算？ |
| 194 | [Agent Saga、补偿与幂等](./194-agent-saga-compensation-idempotency-from-scratch.ipynb) | 当连续调用有副作用工具时，怎样防重复执行、处理半完成，并安全收束失败？ |
| 195 | [多 Agent Supervisor/Worker 委派](./195-multi-agent-supervisor-handoff-from-scratch.ipynb) | 怎样把任务、能力、预算、父 trace 与输入版本绑定到 handoff，避免越权、循环与陈旧结果？ |
| 196 | [Agent Context 压缩与证据恢复](./196-agent-context-compaction-retrieval-from-scratch.ipynb) | 怎样在固定窗口下保留约束、任务状态和可回查证据，并防止摘要漂移？ |
| 197 | [MCP Tool Schema 版本与契约测试](./197-mcp-tool-schema-versioning-contract-tests-from-scratch.ipynb) | 怎样协商协议版本、迁移旧参数、拒绝不兼容调用并用 golden tests 防回归？ |
| 198 | [Agent 动作前审批与 Policy Gate](./198-agent-pre-action-approval-policy-gate-from-scratch.ipynb) | 怎样将审批绑定到精确参数、策略版本和有效期，阻断过期、重放和参数替换？ |
| 199 | [RoPE 长上下文缩放](./199-rope-long-context-scaling-from-scratch.ipynb) | 怎样缩放位置、验证短/长上下文，并防止不同 RoPE 配置的 KV cache 错误复用？ |
| 200 | [LLM 流式 API 事件与恢复](./200-llm-streaming-events-sse-resume-from-scratch.ipynb) | 怎样设计 delta、finish/error、usage、sequence 与 replay，使流式 API 不漏字或误完成？ |
| 201 | [Agent 并行 Tool Call 一致性](./201-agent-parallel-tool-call-id-consistency-from-scratch.ipynb) | 多个 tool call 乱序返回时，怎样用 call id、状态机、顺序汇合和 result ledger 保证一致？ |
| 202 | [Chat Template 训练/服务一致性](./202-chat-template-train-serving-compatibility-from-scratch.ipynb) | 怎样稳定编译 role/tool 消息，区分 generation prompt，并防止模板版本污染模型输入和 cache？ |
| 203 | [Activation Steering / Representation Engineering](./203-activation-steering-representation-engineering-from-scratch.ipynb) | 怎样估计、归一化和注入 steering vector，并用 layer/位置/版本 gate、剂量曲线和任务保持评测控制副作用？ |
| 204 | [Contrastive Decoding](./204-contrastive-decoding-expert-amateur-from-scratch.ipynb) | 怎样对齐 expert/amateur 概率、过滤不可信候选、计算对比分数，并验证质量、成本与失败边界？ |
| 205 | [Semantic Entropy 不确定性与拒答](./205-semantic-entropy-uncertainty-abstention-from-scratch.ipynb) | 怎样把采样结果语义聚类、计算熵、避免多解误判，并以 risk-coverage 校准拒答阈值？ |
| 206 | [ROME 风格知识编辑](./206-rome-rank-one-knowledge-editing-from-scratch.ipynb) | 怎样用 rank-one update 改写事实，同时验证 rewrite、paraphrase generalization、locality、冲突和回滚？ |

## 建议学习路线

1. 运行 187–189：从 target 验证、KV 淘汰到稀疏注意力，先区分理论省算与精确生成/硬件实际加速。
2. 运行 190：把 Agent 执行事件转换成可训练数据，明确 episode、credit、policy version 和 train/eval 隔离。
3. 运行 191–192：把 Agent 的可靠性落到最终状态 oracle、策略门禁、代码 patch 基线与可执行测试。
4. 运行 193–194：最后处理长链路现实问题——工具/人工中断时的 KV 正确恢复，以及跨工具副作用的幂等、补偿和审计。
5. 运行 195–198：再处理规模化协作与治理——带能力的 handoff、可恢复的上下文、MCP 工具演进和不可绕过的动作前审批。
6. 运行 199–202：将底层 LLM 输入/输出契约补齐——位置坐标、流式事件、并行工具消息与 chat template 必须都可版本化、验证和复放。
7. 运行 203–206：最后进入模型内部和不确定性——显式控制表征、对比式解码、语义级不确定性与可回滚的知识编辑都要有独立 oracle。

## 主要研究入口

参考 [EAGLE](https://arxiv.org/abs/2401.15077)、[H₂O](https://arxiv.org/abs/2306.14048)、[Native Sparse Attention](https://arxiv.org/abs/2502.11089)、[Agent Lightning](https://arxiv.org/abs/2508.03680)、[τ-bench](https://arxiv.org/abs/2406.12045)、[SWE-bench](https://arxiv.org/abs/2310.06770)、[INFERCEPT](https://arxiv.org/abs/2402.01869)、[AutoGen](https://arxiv.org/abs/2308.08155)、[MemGPT](https://arxiv.org/abs/2310.08560)、[MCP Versioning](https://modelcontextprotocol.io/docs/learn/versioning)、[Position Interpolation](https://arxiv.org/abs/2306.15595)、[SSE](https://w3c.github.io/eventsource/)、[Representation Engineering](https://arxiv.org/abs/2310.01405)、[Contrastive Decoding](https://arxiv.org/abs/2210.15097)、[Semantic Entropy](https://arxiv.org/abs/2302.09664) 与 [ROME](https://arxiv.org/abs/2202.05262)。

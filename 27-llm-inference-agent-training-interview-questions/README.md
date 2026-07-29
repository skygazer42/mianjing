# LLM 推理优化与 Agent 训练面试题

这一组继续采用“一道面试问题一本 Notebook”，从 EAGLE 特征级推测解码、H₂O heavy-hitter KV cache、Native Sparse Attention 与 Agent Lightning 式轨迹切片/credit assignment，延伸到有状态 Tool-Agent-User 评测、代码 Agent 沙箱、可中断 KV 恢复和工具副作用补偿。

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

## 建议学习路线

1. 运行 187–189：从 target 验证、KV 淘汰到稀疏注意力，先区分理论省算与精确生成/硬件实际加速。
2. 运行 190：把 Agent 执行事件转换成可训练数据，明确 episode、credit、policy version 和 train/eval 隔离。
3. 运行 191–192：把 Agent 的可靠性落到最终状态 oracle、策略门禁、代码 patch 基线与可执行测试。
4. 运行 193–194：最后处理长链路现实问题——工具/人工中断时的 KV 正确恢复，以及跨工具副作用的幂等、补偿和审计。

## 主要研究入口

参考 [EAGLE](https://arxiv.org/abs/2401.15077)、[H₂O](https://arxiv.org/abs/2306.14048)、[Native Sparse Attention](https://arxiv.org/abs/2502.11089)、[Agent Lightning](https://arxiv.org/abs/2508.03680)、[τ-bench](https://arxiv.org/abs/2406.12045)、[SWE-bench](https://arxiv.org/abs/2310.06770)、[INFERCEPT](https://arxiv.org/abs/2402.01869) 与 [AgentDojo](https://arxiv.org/abs/2406.13352)。

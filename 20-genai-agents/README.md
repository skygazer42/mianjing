# 生成式 AI 与 Agent 高频面试题：一题一本 Notebook

这一组来自当前 AI Engineer / LLM Engineer 题单中反复出现、且前面专题尚未独立实现的方向：技术方案选择、生成式评测、Agent 循环与工具安全、结构化生成、幻觉治理、上下文记忆、SFT、RLHF 和模型路由。每本第一屏给出可直接用于面试的回答主线，再用 Python 标准库、NumPy 或 PyTorch 基础算子实现关键机制、反例、门禁与版本合同。

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | 面试问题 | Notebook 回答 |
| --- | --- | --- |
| 01 | Prompt、RAG、微调和 Tool Calling 应该怎样选择？ | [知识/行为/动作缺口、组合架构、成本效用与发布实验](./01-prompt-rag-finetuning-tool-choice-from-scratch.ipynb) |
| 02 | 怎样搭建可靠的 LLM/Agent 评测体系？ | [黄金集、确定性 grader、轨迹、paired bootstrap、slice 与门禁](./02-llm-evaluation-golden-set-release-gate-from-scratch.ipynb) |
| 03 | LLM-as-a-Judge 能直接当真值吗，怎样校准偏差？ | [原子 rubric、位置交换、风格探针、人工一致性与 Judge 聚合](./03-llm-as-judge-bias-calibration-from-scratch.ipynb) |
| 04 | 怎样设计可靠的 Agent Tool Calling？ | [严格 schema、真实身份授权、幂等账本、审批、重试与 trace](./04-agent-tool-calling-schema-idempotency-from-scratch.ipynb) |
| 05 | 怎样实现 ReAct Agent 循环并防止死循环和成本失控？ | [显式状态机、Action/Observation、预算、cycle detector 与错误策略](./05-react-agent-loop-budget-cycle-detection-from-scratch.ipynb) |
| 06 | 怎样防御直接/间接 Prompt Injection？ | [信任标签、taint、完整鉴权、最小权限、绑定审批与红队门禁](./06-prompt-injection-trust-boundary-defense-from-scratch.ipynb) |
| 07 | 怎样实现可靠的 JSON Structured Output？ | [有限 schema、trie 状态机、逐 token mask、语义校验与 fallback](./07-constrained-json-decoding-trie-from-scratch.ipynb) |
| 08 | 怎样降低并评估幻觉，引用和拒答机制如何设计？ | [原子 claim、证据 ACL、支持/矛盾、引用指标、阈值与故障归因](./08-hallucination-grounding-citation-abstention-from-scratch.ipynb) |
| 09 | 上下文窗口有限时，Prompt、证据和 Agent Memory 怎样管理？ | [硬预算、knapsack、位置重排、结构化摘要、TTL/ACL 与安全截断](./09-context-window-memory-budgeting-from-scratch.ipynb) |
| 10 | SFT 的 Chat Template、Loss Mask 与 Packing 怎样实现？ | [对话 schema、角色 token、causal shift、block mask、截断与 TinyLM](./10-sft-chat-template-loss-mask-packing-from-scratch-pytorch.ipynb) |
| 11 | Reward Model、Bradley–Terry Loss 和 KL 约束是什么？ | [偏好对、稳定损失、tie、group split、手写训练、校准与 KL 策略](./11-reward-model-bradley-terry-kl-policy-from-scratch-pytorch.ipynb) |
| 12 | 多个模型之间怎样做质量、成本和延迟感知路由？ | [边际收益、逻辑路由器、阈值/cascade、预算、IPS 与熔断](./12-quality-cost-latency-model-routing-from-scratch.ipynb) |

推荐顺序是 `01–03` 先建立方案与评测判断，`04–09` 学习 Agent/生成系统的运行与安全边界，`10–11` 深入后训练，最后用 `12` 把质量、成本和可靠性放进同一个线上决策。Notebook 中的模拟模型和受控数据用于证明机制，不代表真实基础模型或业务流量上的效果。

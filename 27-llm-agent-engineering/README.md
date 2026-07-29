# LLM 推理优化与 Agent 训练面试题

这一组继续采用“一道面试问题一本 Notebook”，从 EAGLE 特征级推测解码、H₂O heavy-hitter KV cache、Native Sparse Attention 与 Agent Lightning 式轨迹切片/credit assignment，延伸到有状态 Tool-Agent-User 评测、代码 Agent 沙箱、可中断 KV 恢复、工具副作用补偿、多 Agent 委派、上下文压缩、MCP 契约、动作前审批、RoPE 长上下文、流式协议、并行工具调用、chat template、Activation Steering、Contrastive Decoding、Semantic Entropy、知识编辑、水印、软提示、输出 PII、test-time compute 分配、SAE 稀疏特征、父子分块/回填、HyDE 假设文档锚定、Agent 工具错误恢复、KV cache 量化、LoRA 多租户服务、batch-invariant 采样、stop sequence 安全提交、Contextual Retrieval、RAPTOR、长上下文位置鲁棒性、Agent 停滞检测、Text-to-SQL、GraphRAG、时态 RAG、指令层级冲突控制、Web Research Agent 的证据账本、版面多模态 RAG、代码库符号检索、训练数据 PII 治理、checkpoint 制品兼容、MCP OAuth、工具后置条件、反馈记忆冲突治理、Medusa 树验证、CUDA Graph 调度、SimPO、DOM 浏览器 Agent、DoRA、持续预训练、前缀缓存感知路由、JIT 凭据代理、ORPO、弹性训练恢复、请求取消/背压和工具供应链完整性。

每本使用 Python、NumPy 与标准库手写关键状态机、缓存或训练数据合同。每个有效代码行都有中文行内注释；小数据断言只验证实现不变量，不代表大模型吞吐、真实工具安全或线上泛化。

## Notebook 索引

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 01 | [EAGLE 特征级推测解码](./01-eagle-feature-speculative-decoding-from-scratch.ipynb) | feature draft、最长接受前缀、target verifier 与 branch KV 如何保证精确提交？ |
| 02 | [H₂O Heavy-Hitter KV Cache](./02-h2o-heavy-hitter-kv-cache-from-scratch.ipynb) | 累计 attention score、recent window 与容量预算如何共同决定淘汰？ |
| 03 | [Native Sparse Attention](./03-native-sparse-attention-from-scratch.ipynb) | block 选择、局部窗口、全局块、causal mask 与稀疏算量如何实现和验证？ |
| 04 | [Agent Lightning 轨迹 Credit Assignment](./04-agent-lightning-trajectory-credit-assignment-from-scratch.ipynb) | 怎样把 Agent event trace 切为 transition，计算 return-to-go，并用版本门禁隔离 rollout 与 learner？ |
| 05 | [τ-bench 有状态 Tool-Agent-User 评测](./05-taubench-stateful-tool-agent-evaluation-from-scratch.ipynb) | 怎样同时验证最终数据库状态、用户确认、领域策略和多次运行可靠性？ |
| 06 | [SWE-bench 代码 Agent 沙箱](./06-swe-bench-code-agent-sandbox-from-scratch.ipynb) | observe、patch、test、revision gate 和最小变更约束怎样做成可复放 loop？ |
| 07 | [INFERCEPT 中断感知 KV 恢复](./07-infercept-interruption-aware-agent-kv-resume-from-scratch.ipynb) | 怎样区分 pause 与结束、用 snapshot 防止错误 KV 复用，并在显存预算下选择保留或重算？ |
| 08 | [Agent Saga、补偿与幂等](./08-agent-saga-compensation-idempotency-from-scratch.ipynb) | 当连续调用有副作用工具时，怎样防重复执行、处理半完成，并安全收束失败？ |
| 09 | [多 Agent Supervisor/Worker 委派](./09-multi-agent-supervisor-handoff-from-scratch.ipynb) | 怎样把任务、能力、预算、父 trace 与输入版本绑定到 handoff，避免越权、循环与陈旧结果？ |
| 10 | [Agent Context 压缩与证据恢复](./10-agent-context-compaction-retrieval-from-scratch.ipynb) | 怎样在固定窗口下保留约束、任务状态和可回查证据，并防止摘要漂移？ |
| 11 | [MCP Tool Schema 版本与契约测试](./11-mcp-tool-schema-versioning-contract-tests-from-scratch.ipynb) | 怎样协商协议版本、迁移旧参数、拒绝不兼容调用并用 golden tests 防回归？ |
| 12 | [Agent 动作前审批与 Policy Gate](./12-agent-pre-action-approval-policy-gate-from-scratch.ipynb) | 怎样将审批绑定到精确参数、策略版本和有效期，阻断过期、重放和参数替换？ |
| 13 | [RoPE 长上下文缩放](./13-rope-long-context-scaling-from-scratch.ipynb) | 怎样缩放位置、验证短/长上下文，并防止不同 RoPE 配置的 KV cache 错误复用？ |
| 14 | [LLM 流式 API 事件与恢复](./14-llm-streaming-events-sse-resume-from-scratch.ipynb) | 怎样设计 delta、finish/error、usage、sequence 与 replay，使流式 API 不漏字或误完成？ |
| 15 | [Agent 并行 Tool Call 一致性](./15-agent-parallel-tool-call-id-consistency-from-scratch.ipynb) | 多个 tool call 乱序返回时，怎样用 call id、状态机、顺序汇合和 result ledger 保证一致？ |
| 16 | [Chat Template 训练/服务一致性](./16-chat-template-train-serving-compatibility-from-scratch.ipynb) | 怎样稳定编译 role/tool 消息，区分 generation prompt，并防止模板版本污染模型输入和 cache？ |
| 17 | [Activation Steering / Representation Engineering](./17-activation-steering-representation-engineering-from-scratch.ipynb) | 怎样估计、归一化和注入 steering vector，并用 layer/位置/版本 gate、剂量曲线和任务保持评测控制副作用？ |
| 18 | [Contrastive Decoding](./18-contrastive-decoding-expert-amateur-from-scratch.ipynb) | 怎样对齐 expert/amateur 概率、过滤不可信候选、计算对比分数，并验证质量、成本与失败边界？ |
| 19 | [Semantic Entropy 不确定性与拒答](./19-semantic-entropy-uncertainty-abstention-from-scratch.ipynb) | 怎样把采样结果语义聚类、计算熵、避免多解误判，并以 risk-coverage 校准拒答阈值？ |
| 20 | [ROME 风格知识编辑](./20-rome-rank-one-knowledge-editing-from-scratch.ipynb) | 怎样用 rank-one update 改写事实，同时验证 rewrite、paraphrase generalization、locality、冲突和回滚？ |
| 21 | [LLM 绿色名单水印与检测](./21-llm-greenlist-watermark-detection-from-scratch.ipynb) | 怎样生成 green list、偏置采样、计算 z-score，并处理短文本、编辑攻击、阈值和密钥轮换？ |
| 22 | [Soft Prompt Tuning](./22-soft-prompt-tuning-frozen-base-from-scratch.ipynb) | 怎样冻结基座并训练连续提示，将 prompt id、形状、模板、租户和评测作为发布制品管理？ |
| 23 | [LLM 输出 PII Redaction Policy Gate](./23-llm-output-pii-redaction-policy-gate-from-scratch.ipynb) | 怎样扫描 PII span、按风险掩码或阻断、处理未知格式，并以最小化审计和 precision/recall 验收？ |
| 24 | [自适应 Test-Time Compute 预算分配](./24-adaptive-test-time-compute-budget-allocation-from-scratch.ipynb) | 怎样按样本收益与成本分配采样/搜索预算，并评测质量、延迟、regret、公平与策略漂移？ |
| 25 | [Sparse Autoencoder LLM 可解释性](./25-sparse-autoencoder-llm-interpretability-from-scratch.ipynb) | 怎样从激活编码、ReLU 稀疏化、top-k、重构误差、feature usage 和干预实验理解 SAE 的单义特征边界？ |
| 26 | [RAG 父子切块与上下文回填](./26-rag-parent-child-chunking-context-from-scratch.ipynb) | 怎样用 child 精确召回、parent 去重回填、ACL/版本门禁与双层引用同时控制上下文充分性和陈旧索引？ |
| 27 | [HyDE Query Expansion、RRF 与 Grounding](./27-hyde-query-expansion-rrf-grounding-from-scratch.ipynb) | 怎样隔离假设文档、融合原 query/HyDE 候选、只用真实证据生成，并处理 hallucinated expansion？ |
| 28 | [Agent Tool Error Recovery 与熔断](./28-agent-tool-error-recovery-circuit-breaker-from-scratch.ipynb) | 怎样分类 transient/permanent/unknown 错误，设计带幂等键的重试、熔断、fallback 与人工升级？ |
| 29 | [KV Cache 非对称量化与异常值回退](./29-llm-kv-cache-asymmetric-quantization-outlier-fallback-from-scratch.ipynb) | 怎样定义 group-wise scale/zero、异常值 residual、版本门禁、attention oracle 和真实字节账本？ |
| 30 | [S-LoRA 多 Adapter 服务与版本化内存池](./30-slora-multi-adapter-serving-versioned-pool-from-scratch.ipynb) | 怎样实现 base + LoRA delta、租户/base 授权、refcount 驱逐、兼容 batch 和不可变热更新？ |
| 31 | [连续批处理的 Batch-Invariant 随机采样](./31-llm-continuous-batching-batch-invariant-sampling-from-scratch.ipynb) | 怎样以 request/step/seed 坐标 RNG 隔离采样，避免队列顺序影响输出，并正确声明复现边界？ |
| 32 | [LLM 流式 Stop Sequence 安全提交](./32-llm-streaming-stop-sequence-safe-commit-from-scratch.ipynb) | 怎样跨 token/chunk 匹配 stop string，缓冲潜在前缀，并避免将停止串或尾部泄露给客户端？ |
| 33 | [RAG Contextual Retrieval 与来源版本](./33-rag-contextual-retrieval-provenance-versioning-from-scratch.ipynb) | 怎样将文档级 context 加入检索表示，同时保留 raw evidence、ACL、生成器版本和失效门禁？ |
| 34 | [RAPTOR 分层摘要检索与来源链](./34-raptor-hierarchical-summary-retrieval-provenance-from-scratch.ipynb) | 怎样递归聚类/摘要，按层检索后展开 leaf evidence，并处理 summary 的版本失效与错误传播？ |
| 35 | [长上下文 Needle 位置鲁棒性评测](./35-llm-long-context-needle-position-robustness-evaluation-from-scratch.ipynb) | 怎样控制长度、位置、干扰、解析与无答案对照，避免用单一 needle 误判真实长文理解？ |
| 36 | [Agent Loop 停滞检测与停止策略](./36-agent-loop-stagnation-fingerprint-budget-stop-policy-from-scratch.ipynb) | 怎样基于 action/state fingerprint、进展、预算和副作用语义识别循环，并避免误杀正常轮询？ |
| 37 | [Text-to-SQL Schema Linking 与 Policy Gate](./37-text-to-sql-schema-linking-policy-gate-from-scratch.ipynb) | 怎样将模型候选限制为 schema-aware AST，执行表/列/租户/参数/成本门禁并保存结果证据？ |
| 38 | [GraphRAG Local/Global Search 与来源](./38-graphrag-local-global-community-provenance-from-scratch.ipynb) | 怎样按实体邻域或社区报告选择检索路径，并将 edge/summary 展开为可核验原文？ |
| 39 | [Temporal RAG 有效时间、冲突与引用](./39-temporal-rag-valid-time-conflict-citation-from-scratch.ipynb) | 怎样按 valid-time 检索、拒绝同一时点的冲突事实，并给答案附上生效区间和来源？ |
| 40 | [Agent 指令层级冲突与来源控制](./40-agent-instruction-hierarchy-conflict-provenance-from-scratch.ipynb) | 怎样解析 system/developer/user/external 的冲突，处理同级澄清、外部注入与副作用授权？ |
| 41 | [Web Research Agent 证据账本与引用](./41-web-research-agent-claim-evidence-citation-ledger-from-scratch.ipynb) | 怎样规划搜索、过滤来源、建立 claim-evidence ledger、处理冲突/时效，并只渲染可核验主张？ |
| 42 | [多模态 RAG 版面 Region 与表格证据](./42-multimodal-rag-layout-region-table-evidence-from-scratch.ipynb) | 怎样以 page/bbox/模态为检索与引用单位，路由 text/table/image，并处理 OCR 低置信与版本？ |
| 43 | [Code RAG 符号、依赖与版本上下文](./43-code-rag-symbol-dependency-versioned-context-from-scratch.ipynb) | 怎样按 symbol 检索、有限 hop 展开依赖/测试、控制预算并阻止过期代码进入 patch 规划？ |
| 44 | [LLM 训练数据 PII 治理、删除与审计](./44-llm-training-data-pii-governance-deletion-audit-from-scratch.ipynb) | 怎样记录来源/许可/PII span、治理 manifest/tombstone、处理删除请求，并用授权 canary 监控泄露？ |
| 45 | [LLM Checkpoint Manifest、分片与兼容性](./45-llm-checkpoint-manifest-shards-compatibility-from-scratch.ipynb) | 怎样以 manifest/index/shard/shape/hash 与 tokenizer、模板、dtype、base revision 门禁安全加载并原子发布？ |
| 46 | [MCP OAuth Resource 与 Audience 授权](./46-mcp-oauth-resource-audience-authorization-from-scratch.ipynb) | 怎样发现元数据、申请 resource-bound token、验证 audience/scope/过期，并阻止 token passthrough？ |
| 47 | [Agent Tool 后置条件与 State Diff 验证](./47-agent-tool-postcondition-state-diff-verification-from-scratch.ipynb) | 怎样用 precondition、invocation id、权威回读、state diff 和 policy verifier 区分安全成功、未验证和失败？ |
| 48 | [Agent 反馈记忆冲突与来源治理](./48-agent-feedback-memory-conflict-provenance-from-scratch.ipynb) | 怎样将反馈变为版本化、可验证、可撤销且 ACL 隔离的长期记忆，并确定性解析冲突？ |
| 49 | [Medusa 多解码头与树形验证](./49-medusa-multi-head-tree-verification-from-scratch.ipynb) | 怎样用多个未来 token head 构造候选树、tree attention 批量验证，并只提交 target 接受路径与 KV？ |
| 50 | [LLM Serving CUDA Graph Dispatch](./50-llm-serving-cuda-graph-dispatch-from-scratch.ipynb) | 怎样按 BatchDescriptor 选择 full/piecewise/eager，管理 capture/replay、静态缓冲和动态形状 fallback？ |
| 51 | [SimPO Reference-Free 偏好优化](./51-simpo-reference-free-preference-optimization-from-scratch-pytorch.ipynb) | 为什么平均 token logprob 可作隐式奖励，target margin 与稳定 loss 怎样实现并验证梯度方向？ |
| 52 | [浏览器 Agent DOM 快照与陈旧动作验证](./52-browser-agent-dom-snapshot-stale-action-verification-from-scratch.ipynb) | 怎样用 page/version/ref、语义 grounding、动作审批、幂等提交和后置条件避免点错或只声称完成？ |
| 53 | [DoRA 权重分解低秩适配](./53-dora-weight-decomposed-low-rank-adaptation-from-scratch-pytorch.ipynb) | 怎样将权重 magnitude/direction 解耦，手写低秩方向更新、稳定归一化、梯度与 merge/发布合同？ |
| 54 | [LLM 持续预训练、Replay 与遗忘门禁](./54-llm-continual-pretraining-replay-forgetting-from-scratch-pytorch.ipynb) | 新领域数据到来后怎样 rewarm 学习率、混合旧域 replay，并用 general/domain 矩阵控制灾难性遗忘？ |
| 55 | [前缀缓存感知 LLM 副本路由](./55-prefix-cache-aware-llm-replica-routing-from-scratch.ipynb) | 怎样在 prefix KV 命中、队列等待、容量、租户隔离与公平之间选择副本，并处理陈旧目录？ |
| 56 | [Agent JIT Credential Broker 与无密钥工具执行](./56-agent-jit-credential-broker-secretless-tools-from-scratch.ipynb) | 怎样让模型只拿一次性 capability，由隔离 broker 代用凭据，并校验 audience/scope/TTL/参数与重放？ |
| 57 | [ORPO 单阶段 Odds-Ratio 偏好优化](./57-orpo-odds-ratio-monolithic-preference-optimization-from-scratch-pytorch.ipynb) | 怎样把 chosen SFT NLL 与 rejected odds-ratio penalty 合并为无需 reference model 的单阶段目标，并验证数值和梯度？ |
| 58 | [弹性分布式 LLM 训练与 Checkpoint 恢复](./58-elastic-distributed-llm-training-checkpoint-recovery-from-scratch.ipynb) | worker failure 或 membership change 后怎样重新 rendezvous、全员重启，并恢复不依赖 rank/world-size 的模型、数据、优化器与 RNG 状态？ |
| 59 | [LLM Serving 请求取消、背压与 KV 释放](./59-llm-serving-request-cancellation-backpressure-kv-release-from-scratch.ipynb) | 怎样处理断连/取消、队列准入、in-flight 竞态、幂等 abort、terminal event 与 KV block 精确回收？ |
| 60 | [Agent 工具供应链签名 Manifest 与来源](./60-agent-tool-supply-chain-signed-manifest-provenance-from-scratch.ipynb) | 怎样验签 publisher、schema、description、artifact 与 permission，绑定 plan digest，并阻断 tool poisoning、暗改与权限扩大？ |

## 建议学习路线

1. 运行 01–03：从 target 验证、KV 淘汰到稀疏注意力，先区分理论省算与精确生成/硬件实际加速。
2. 运行 04：把 Agent 执行事件转换成可训练数据，明确 episode、credit、policy version 和 train/eval 隔离。
3. 运行 05–06：把 Agent 的可靠性落到最终状态 oracle、策略门禁、代码 patch 基线与可执行测试。
4. 运行 07–08：最后处理长链路现实问题——工具/人工中断时的 KV 正确恢复，以及跨工具副作用的幂等、补偿和审计。
5. 运行 09–12：再处理规模化协作与治理——带能力的 handoff、可恢复的上下文、MCP 工具演进和不可绕过的动作前审批。
6. 运行 13–16：将底层 LLM 输入/输出契约补齐——位置坐标、流式事件、并行工具消息与 chat template 必须都可版本化、验证和复放。
7. 运行 17–20：最后进入模型内部和不确定性——显式控制表征、对比式解码、语义级不确定性与可回滚的知识编辑都要有独立 oracle。
8. 运行 21–24：把发布和推理控制面补齐——可检测来源、低成本多任务适配、输出侧隐私门禁，以及在全局预算下按样本分配 test-time compute。
9. 运行 25–28：再把表征可解释性、分层检索/证据锚定与 Agent 的失败恢复连成闭环；其中 HyDE 只能扩展检索候选，绝不能充当最终事实证据。
10. 运行 29–32：最后回到服务内核，比较低比特 KV 的误差账本、adapter 与 KV 的共享资源、并发采样的可审计随机性，以及流式生成的安全终止语义。
11. 运行 33–36：把检索从孤立 chunk 推进到可追溯的文档/层级结构，再用位置切片测试长上下文，最后把 Agent 的“何时继续”落为确定的进展、预算与副作用门禁。
12. 运行 37–40：将自然语言请求落为受控 SQL/图谱/时态事实合同，并把 Agent 的指令权威、外部内容信任和 action 授权分层处理。
13. 运行 41–44：把 Agent 的检索/浏览收束为证据账本，扩展到带版面与表格的多模态知识、代码库 API 上下文，以及训练数据的隐私、删除与审计。
14. 运行 45–48：把模型和 Agent 的制品、身份、行动结果与经验记忆都变成可验证合同，避免“能加载、拿到 token、返回 ok 或写入记忆”被误当成正确性。
15. 运行 49–52：从多 token 推测和 GPU replay 的推理优化进入 reference-free 偏好学习，最后把浏览器 Agent 的观察、动作与功能成功绑定到可验证页面状态。
16. 运行 53–56：从参数高效适配和持续预训练的能力—遗忘权衡，进入多副本 cache locality 调度与 Agent 最小权限的即时凭据执行。
17. 运行 57–60：比较 ORPO 单阶段偏好目标与已有 DPO/SimPO，再把长时训练和在线推理的失败恢复、以及 Agent 工具供应链纳入一致状态和完整性门禁。

## 主要研究入口

补充参考 [Hugging Face Sharded Checkpoint](https://huggingface.co/docs/transformers/main/big_models)、[MCP Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)、[STATE-Bench](https://github.com/microsoft/STATE-Bench) 与 [Memory Conflict Resolution](https://arxiv.org/abs/2606.01435)。

本批参考 [Medusa](https://arxiv.org/abs/2401.10774)、[vLLM CUDA Graphs](https://docs.vllm.ai/en/latest/design/cuda_graphs/)、[SimPO](https://arxiv.org/abs/2405.14734)、[WebArena](https://arxiv.org/abs/2307.13854) 与 [BrowserGym](https://arxiv.org/abs/2412.05467)。

本批补充参考 [DoRA](https://arxiv.org/abs/2402.09353)、[Continual Pre-Training](https://arxiv.org/abs/2308.04014)、[Preble](https://arxiv.org/abs/2407.00023) 与 [Agentic AI Secure Adoption](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services)。

本批参考 [ORPO](https://arxiv.org/abs/2403.07691)、[PyTorch Elastic](https://docs.pytorch.org/docs/stable/elastic/run)、[vLLM Abort Race](https://github.com/vllm-project/vllm/issues/26400)、[OWASP MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning) 与 [NSA MCP Security](https://media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF)。

参考 [EAGLE](https://arxiv.org/abs/2401.15077)、[H₂O](https://arxiv.org/abs/2306.14048)、[Native Sparse Attention](https://arxiv.org/abs/2502.11089)、[Agent Lightning](https://arxiv.org/abs/2508.03680)、[τ-bench](https://arxiv.org/abs/2406.12045)、[SWE-bench](https://arxiv.org/abs/2310.06770)、[INFERCEPT](https://arxiv.org/abs/2402.01869)、[AutoGen](https://arxiv.org/abs/2308.08155)、[MemGPT](https://arxiv.org/abs/2310.08560)、[MCP Versioning](https://modelcontextprotocol.io/docs/learn/versioning)、[Position Interpolation](https://arxiv.org/abs/2306.15595)、[SSE](https://w3c.github.io/eventsource/)、[Representation Engineering](https://arxiv.org/abs/2310.01405)、[Contrastive Decoding](https://arxiv.org/abs/2210.15097)、[Semantic Entropy](https://arxiv.org/abs/2302.09664)、[ROME](https://arxiv.org/abs/2202.05262)、[LLM Watermark](https://arxiv.org/abs/2301.10226)、[Prompt Tuning](https://arxiv.org/abs/2104.08691)、[Adaptive Test-Time Compute](https://arxiv.org/abs/2604.14853)、[Sparse Autoencoders](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)、[HyDE](https://arxiv.org/abs/2212.10496)、[ReAct](https://arxiv.org/abs/2210.03629)、[Toolformer](https://arxiv.org/abs/2302.04761)、[KIVI](https://arxiv.org/abs/2402.02750)、[S-LoRA](https://arxiv.org/abs/2311.03285)、[vLLM Reproducibility](https://docs.vllm.ai/en/v0.9.1/usage/reproducibility.html)、[Transformers StopStringCriteria](https://huggingface.co/docs/transformers/en/internal/generation_utils)、[Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)、[RAPTOR](https://arxiv.org/abs/2401.18059)、[Lost in the Middle](https://arxiv.org/abs/2307.03172)、[AgentBench](https://arxiv.org/abs/2308.03688)、[PICARD](https://arxiv.org/abs/2109.05093)、[Microsoft GraphRAG](https://microsoft.github.io/graphrag//query/overview/)、[IA-RAG](https://arxiv.org/abs/2606.06044)、[Model Spec Chain of Command](https://model-spec.openai.com/2025-02-12.html)、[WebGPT](https://arxiv.org/abs/2112.09332)、[SK-VQA](https://arxiv.org/abs/2406.19593)、[RepoCoder](https://arxiv.org/abs/2303.12570) 与 [Training Data Extraction](https://arxiv.org/abs/2012.07805)。

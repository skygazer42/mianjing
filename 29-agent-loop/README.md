# Agent Loop 运行时内核面试题（01–30）

这一组题聚焦一个常被框架 API 掩盖、但面试最爱追问的对象：**单个 Agent 循环的运行时内核**——loop 每一步「怎么转、怎么记、怎么走、怎么停」。不谈多 Agent 编排、MCP 协议或工具目录治理（那些在相邻专题里），只把一个 `while` 循环内部的状态机、观察回喂、上下文演化、终止判定、回放与评测拆到能从零写出来。

每题配一篇可复述的中文答案和一本独立可运行的 Notebook。所有实现只依赖 Python 标准库与少量 NumPy，不用任何 Agent 框架替代循环内核；每本 Notebook 都用脱敏可复放的业务事件，展示 baseline、状态迁移、失败反例与修正。受控小数据只解释机制，不外推为线上收益。

## 与相邻专题的分工（重要）

| 专题 | 关注点 | 本专题不重复的原因 |
| --- | --- | --- |
| `21-agent-loop` | 生产级**架构模式选择**：Workflow vs Agent、DAG 调度、MCP、安全代码 VM、多 Agent Handoff、Agentic RAG | 那是「选哪种结构」；这里是「一个循环内部怎么实现」 |
| `29-智能代理` | **工具控制面 + 副作用事务**：工具路由/校验/幂等、Saga 补偿、记忆分层、评测门禁 | 那是「工具与事务怎么管」；这里是「循环步怎么推进」 |

显式去重点：本专题题 5「loop step 级幂等」≠ 智能代理「工具调用幂等键」；题 11/12「循环内上下文动态演化」≠ 智能代理「按预算一次性选 context」；题 26/27「loop step 粒度可回放 trace + 确定性重放」≠ 21「成本归因 trace」、≠ 智能代理「trace 分层评分」；题 19/20「循环自身停止信号」≠ 智能代理「终态 grader」。

## A. 循环骨架与状态机（loop 怎么"转"）

| # | 面试题 | Notebook |
| --- | --- | --- |
| 01 | [Agent Loop 最小运行时骨架怎么设计？](./01.AgentLoop最小运行时骨架怎么设计.md) | [nb](./01-agent-loop-skeleton.ipynb) |
| 02 | [ReAct 式 Thought–Action–Observation 交织与直接函数调用循环怎么选？](./02.ReAct交织与函数调用循环怎么选.md) | [nb](./02-react-vs-function-calling-loop.ipynb) |
| 03 | [单步决策粒度：一步产出一个还是一组动作？](./03.单步决策粒度怎么定.md) | [nb](./03-step-action-granularity.ipynb) |
| 04 | [循环主控制器怎么写：驱动、注入观察、判断继续/停止？](./04.循环主控制器怎么写.md) | [nb](./04-loop-controller.ipynb) |
| 05 | [循环 step 级幂等：同一步被重试重复执行怎么不污染状态？](./05.循环step级幂等怎么保证.md) | [nb](./05-loop-step-idempotency.ipynb) |
| 06 | [循环状态对象怎么设计：goal/history/scratchpad/step/budget？](./06.循环状态对象怎么设计.md) | [nb](./06-loop-state-schema.ipynb) |
| 07 | [同步循环 vs 事件驱动循环：何时让出控制权等外部事件？](./07.同步循环与事件驱动循环怎么选.md) | [nb](./07-sync-vs-event-driven-loop.ipynb) |
| 08 | [单步怎么做成纯函数以支持单测与回放？](./08.单步怎么做成纯函数.md) | [nb](./08-pure-step-testable.ipynb) |

## B. 观察 · 上下文 · 工作记忆的循环内演化（loop 怎么"记"）

| # | 面试题 | Notebook |
| --- | --- | --- |
| 09 | [Observation 怎么规范化后回喂模型？](./09.Observation怎么规范化回喂.md) | [nb](./09-observation-normalization.ipynb) |
| 10 | [超大 observation 怎么做选择性读取与分页？](./10.超大observation怎么选择性读取.md) | [nb](./10-large-observation-selective-read.ipynb) |
| 11 | [循环历史滚动窗口：保留/丢弃哪些步、按什么信号？](./11.循环历史滚动窗口怎么设计.md) | [nb](./11-history-rolling-window.ipynb) |
| 12 | [循环历史摘要压缩：何时触发、压缩什么、不丢什么？](./12.循环历史摘要压缩怎么做.md) | [nb](./12-history-summarization.ipynb) |
| 13 | [Scratchpad/working memory 在循环内怎么维护与失效？](./13.循环内scratchpad怎么维护.md) | [nb](./13-scratchpad-working-memory.ipynb) |
| 14 | [Context 中毒：一条错误观察怎么隔离与回滚？](./14.context中毒怎么隔离与回滚.md) | [nb](./14-context-poisoning-isolation.ipynb) |
| 15 | [跨步指代一致性：前几步产出的实体/ID 怎么稳定引用？](./15.跨步指代一致性怎么保持.md) | [nb](./15-cross-step-reference-consistency.ipynb) |
| 16 | [循环内 token 预算怎么记账与逼近上限时降级？](./16.循环内token预算怎么记账与降级.md) | [nb](./16-loop-token-budget-accounting.ipynb) |

## C. 决策 · 行动 · 推进控制（loop 怎么"走"）

| # | 面试题 | Notebook |
| --- | --- | --- |
| 17 | [每步 action 合法性怎么用结构化输出/受控解码约束？](./17.每步action合法性怎么约束.md) | [nb](./17-action-validity-constraint.ipynb) |
| 18 | [无进展 loop stall 怎么检测重复动作/震荡并打破？](./18.无进展loop-stall怎么检测.md) | [nb](./18-loop-stall-detection.ipynb) |
| 19 | [终止条件：完成/无进展/超预算/超时四类信号怎么排优先级？](./19.终止条件四类停止信号怎么设计.md) | [nb](./19-termination-signals.ipynb) |
| 20 | [完成判定：模型自称完成 vs 客观后置验证，怎么防假完成？](./20.完成判定怎么防假完成.md) | [nb](./20-done-detection.ipynb) |
| 21 | [提前终止 vs 过度执行怎么成因分析与防护？](./21.提前终止与过度执行怎么防护.md) | [nb](./21-premature-stop-vs-overrun.ipynb) |
| 22 | [失败后 backtrack 换策略：回退到哪个检查点？](./22.失败后backtrack换策略怎么做.md) | [nb](./22-backtrack-strategy-switch.ipynb) |
| 23 | [Look-ahead 试探怎么在不产生真实副作用下预演？](./23.look-ahead试探怎么不产生副作用.md) | [nb](./23-lookahead-dry-run.ipynb) |
| 24 | [探索 vs 利用：给循环一个探索预算怎么设计？](./24.探索与利用预算怎么平衡.md) | [nb](./24-explore-exploit-budget.ipynb) |

## D. 稳健性 · 可观测 · 评测（loop 怎么"稳"和"验"）

| # | 面试题 | Notebook |
| --- | --- | --- |
| 25 | [子循环嵌套：内层 loop 的深度/预算/结果回传怎么隔离？](./25.子循环嵌套怎么隔离与回传.md) | [nb](./25-nested-subloop-isolation.ipynb) |
| 26 | [循环级 trace：每步记录什么才能回放与因果定位？](./26.循环级trace每步记什么.md) | [nb](./26-loop-step-trace.ipynb) |
| 27 | [确定性重放：固定模型输出与观察后怎么让整条 loop 可复现？](./27.确定性重放怎么实现.md) | [nb](./27-deterministic-replay.ipynb) |
| 28 | [循环失败注入测试：工具失败/观察缺失/超预算/乱序怎么注入？](./28.循环失败注入测试怎么设计.md) | [nb](./28-loop-fault-injection.ipynb) |
| 29 | [循环成本与延迟模型：端到端=Σ每步，怎么压缩步数？](./29.循环成本与延迟模型怎么建.md) | [nb](./29-loop-cost-latency-model.ipynb) |
| 30 | [循环级发布门禁：固定任务集怎么评测一次 loop 改动的回归？](./30.循环级发布门禁怎么设计.md) | [nb](./30-loop-release-gate.ipynb) |

## 学习路线

1. 先学 01–08：把「一个循环怎么转」从框架黑箱变成可写出的状态机、纯函数步和确定性控制器。
2. 再学 09–16：理解循环推进过程中观察与上下文如何动态演化，以及怎么防止历史膨胀和 context 中毒。
3. 然后学 17–24：掌握每步动作的约束、打转检测、终止判定与回退/试探/探索预算这些「推进控制」。
4. 最后学 25–30：把嵌套子循环、可回放 trace、确定性重放、失败注入、成本模型和发布门禁补齐，让一个 loop 可诊断、可评测、可安全迭代。

## 面试时应主动说明的边界

- 循环内的「思考」只是模型提议，动作是否合法、是否执行、是否停止由确定性外壳裁决。
- 「终止」必须同时定义完成判定与超预算/超时兜底；只靠模型自称完成会「假完成」或「过度执行」。
- 「上下文压缩」「滚动窗口」是有损操作，必须说明丢弃了什么、在什么任务上会失败。
- 教学循环用受控小数据和可预测的假模型，验证的是状态机与停止条件，不代表真实模型或线上业务效果。

## 原始资料

- [Anthropic：Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- [τ-bench: A Benchmark for Tool-Agent-User Interaction](https://arxiv.org/abs/2406.12045)
- [OpenTelemetry GenAI 语义约定](https://opentelemetry.io/docs/specs/semconv/gen-ai/)

## 运行与验收

在仓库根目录启动 Jupyter，逐本从空内核运行。每本使用受控小数据，断言集中在最后一个代码单元，只保护状态机、停止条件和数值结论等关键不变量。批量校验：

```bash
python3 scripts/validate_teaching_notebooks.py 29-agent-loop/
```

# 智能代理高频面试题（01–30）

这一组题把“模型会调用工具”落成可验证的控制面：先决定是否需要工具，再发现、校验、执行、验证结果，并为有副作用的动作提供幂等、重试、熔断与降级。每个问题都有一篇可复述的中文答案和一份独立可运行的 Notebook；实验都使用脱敏、可复放的业务事件，展示 baseline、状态迁移、失败反例与修复。受控小数据只用于解释机制，不能外推为线上收益。

## 决策与工具控制面（01–10）

1. [追问或执行的 VOI 怎样设计？](./01.追问或执行的VOI怎样设计.md) · [Notebook](./01-voi-clarify-or-act.ipynb)
2. [Agent 怎样判断 need-tool？](./02.Agent怎样判断need-tool.md) · [Notebook](./02-need-tool-decision.ipynb)
3. [学习型 Tool Router 怎样训练和兜底？](./03.学习型Tool-Router怎样训练和兜底.md) · [Notebook](./03-tool-router.ipynb)
4. [大规模工具目录怎样做工具发现？](./04.大规模工具目录怎样做工具发现.md) · [Notebook](./04-tool-discovery.ipynb)
5. [工具 Schema 应怎样设计？](./05.工具Schema应怎样设计.md) · [Notebook](./05-tool-schema.ipynb)
6. [为什么参数校验必须在模型之后？](./06.为什么参数校验必须在模型之后.md) · [Notebook](./06-parameter-validation.ipynb)
7. [怎样验证工具结果而不是相信工具文本？](./07.怎样验证工具结果而不是相信工具文本.md) · [Notebook](./07-tool-result-verification.ipynb)
8. [有副作用的工具为什么需要幂等键？](./08.有副作用的工具为什么需要幂等键.md) · [Notebook](./08-idempotency-key.ipynb)
9. [重试和指数退避怎样避免放大故障？](./09.重试和指数退避怎样避免放大故障.md) · [Notebook](./09-retry-backoff.ipynb)
10. [熔断与降级怎样保护 Agent 系统？](./10.熔断与降级怎样保护Agent系统.md) · [Notebook](./10-circuit-breaker-fallback.ipynb)
11. [Agent 如何做可执行的任务分解？](./11.Agent如何做可执行的任务分解.md) · [Notebook](./11-task-decomposition.ipynb)
12. [有预算的规划搜索怎样设计？](./12.有预算的规划搜索怎样设计.md) · [Notebook](./12-budgeted-planning-search.ipynb)
13. [执行中如何动态重规划？](./13.执行中如何动态重规划.md) · [Notebook](./13-dynamic-replanning.ipynb)
14. [并行工具调用与 Join 怎样保证一致性？](./14.并行工具调用与Join怎样保证一致性.md) · [Notebook](./14-parallel-tools-join.ipynb)
15. [多 Agent 如何共享状态而不互相污染？](./15.多Agent如何共享状态而不互相污染.md) · [Notebook](./15-shared-state.ipynb)
16. [怎样检测多 Agent 写冲突？](./16.怎样检测多Agent写冲突.md) · [Notebook](./16-write-conflict-detection.ipynb)
17. [人类审批怎样绑定具体动作？](./17.人类审批怎样绑定具体动作.md) · [Notebook](./17-human-approval.ipynb)
18. [工具后置条件怎样设计与验证？](./18.工具后置条件怎样设计与验证.md) · [Notebook](./18-tool-postconditions.ipynb)
19. [为什么 Agent 必须权威状态回读？](./19.为什么Agent必须权威状态回读.md) · [Notebook](./19-authoritative-readback.ipynb)
20. [Saga 补偿事务怎样处理长链路副作用？](./20.Saga补偿事务怎样处理长链路副作用.md) · [Notebook](./20-saga-compensation.ipynb)
21. [Session Reset 后怎样安全恢复 Agent？](./21.Session-Reset后怎样安全恢复Agent.md) · [Notebook](./21-session-reset.ipynb)
22. [Agent 间怎样用 Artifact Handoff 交接？](./22.Agent间怎样用Artifact-Handoff交接.md) · [Notebook](./22-artifact-handoff.ipynb)
23. [长程 Agent Harness 怎样隔离与恢复？](./23.长程Agent-Harness怎样隔离与恢复.md) · [Notebook](./23-long-running-harness.ipynb)
24. [Context 怎样选择并遵守 token 预算？](./24.Context怎样选择并遵守token预算.md) · [Notebook](./24-context-selection-budget.ipynb)
25. [工作记忆、情景记忆和长期记忆怎样分层？](./25.工作记忆情景记忆和长期记忆怎样分层.md) · [Notebook](./25-memory-layers.ipynb)
26. [时间冲突怎样驱动记忆更新？](./26.时间冲突怎样驱动记忆更新.md) · [Notebook](./26-temporal-memory-conflicts.ipynb)
27. [Trace 怎样做分层 Grading？](./27.Trace怎样做分层Grading.md) · [Notebook](./27-trace-layered-grading.ipynb)
28. [怎样定位第一处因果错误？](./28.怎样定位第一处因果错误.md) · [Notebook](./28-first-causal-error.ipynb)
29. [最终状态 Grader 怎样设计？](./29.最终状态Grader怎样设计.md) · [Notebook](./29-final-state-grader.ipynb)
30. [安全、成本、质量发布门禁怎样设计？](./30.安全成本质量发布门禁怎样设计.md) · [Notebook](./30-release-gates.ipynb)

## 学习顺序

先学 01–03：把“是否行动”从提示词判断变成可计算、可回退的策略；再学 04–07：把工具的发现、契约与结果核验闭环；然后学 08–10：理解分布式副作用和依赖故障时的确定性控制面；接着学 11–20：把受限工具调用组织成可恢复、可审批、可审计的长程任务；最后学 21–30：掌握长程运行的 context reset、artifact 交接、因果评测与发布门禁。

## 原始资料

- [Anthropic：Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Model Context Protocol：Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- [Toolformer](https://arxiv.org/abs/2302.04761)
- [Gorilla / APIBench](https://arxiv.org/abs/2305.15334)
- [Google SRE Book：Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)

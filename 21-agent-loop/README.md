# Agent Loop 深入面试题

这一组延续“一道面试问题一本 Notebook”的形式，聚焦生产级 Agent 循环中最常被追问、也最容易被框架 API 掩盖的部分：模式选择、计划调度、并行工具、工具发现、持久化恢复、人工审批、多 Agent 协作、多跳 RAG、反思优化、安全执行、MCP 和可观测性。

所有实现只依赖 Python 标准库与少量 NumPy，不使用 Agent 框架替代核心逻辑。每本 Notebook 都包含面试回答主线、状态或数据契约、从零实现、反例断言、评测方法、生产边界和原始资料。

## Notebook 索引

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | Notebook 回答 | 面试问题 |
| --- | --- | --- |
| 01 | [Workflow 与 Agent 模式选择](./01-workflow-vs-agent-pattern-selection-from-scratch.ipynb) | 什么时候用固定 Workflow，什么时候用 Agent？Sequential、Routing、Parallel、Orchestrator 和 Evaluator-Optimizer 怎样选？ |
| 02 | [计划 DAG 与调度器](./02-agent-plan-dag-scheduler-from-scratch.ipynb) | Agent 生成计划后，怎样校验 DAG、并行调度、处理失败和动态重规划？ |
| 03 | [并行工具执行与 Join](./03-parallel-tool-execution-join-consistency-from-scratch.ipynb) | Agent 怎样安全并行调用工具，处理依赖、限流、部分失败和结果合并？ |
| 04 | [大规模 Tool Catalog 检索](./04-large-tool-catalog-retrieval-bm25-from-scratch.ipynb) | Agent 面对成百上千个工具时，怎样做 Tool Discovery、召回和选择？ |
| 05 | [持久化 Agent 与事件重放](./05-durable-agent-event-sourcing-resume-from-scratch.ipynb) | 长时间运行的 Agent 怎样做到崩溃恢复、精确重放和安全取消？ |
| 06 | [Human-in-the-Loop](./06-human-in-the-loop-approval-interrupt-resume-from-scratch.ipynb) | 哪些动作必须审批，审批票据怎样绑定动作，如何中断、超时与恢复？ |
| 07 | [Multi-Agent Handoff 与 Blackboard](./07-multi-agent-handoff-blackboard-isolation-from-scratch.ipynb) | 什么时候需要 Multi-Agent，Handoff、共享状态、隔离和写冲突怎样设计？ |
| 08 | [Agentic RAG 多跳查询规划](./08-agentic-rag-multihop-query-planning-from-scratch.ipynb) | 怎样分解问题、逐跳检索、构建证据图、处理时间冲突并判断停止？ |
| 09 | [Reflection / Evaluator-Optimizer](./09-evaluator-optimizer-reflection-loop-from-scratch.ipynb) | 怎样把评价变成可执行修订，并避免共享盲点、循环和越改越差？ |
| 10 | [安全代码执行与 Capability VM](./10-safe-code-execution-capability-vm-from-scratch.ipynb) | Agent 执行代码时怎样做白名单、资源限制、文件/网络隔离和结果审计？ |
| 11 | [MCP 生命周期与最小协议](./11-mcp-jsonrpc-lifecycle-capability-from-scratch.ipynb) | Host、Client、Server、Tools、Resources、Prompts、JSON-RPC 和能力协商是什么？ |
| 12 | [Agent Trace、Replay 与成本归因](./12-agent-observability-trace-replay-cost-from-scratch.ipynb) | 怎样定位 Agent 的慢、贵、循环、工具错误和质量回归？ |

## 建议学习路线

1. 先运行 01，建立“能用确定性 Workflow 就不扩大自主性”的架构判断。
2. 再运行 02–06，掌握单 Agent 的计划、执行、持久化和人工控制面。
3. 运行 07–09，理解多 Agent、多跳检索和评价优化循环何时产生净收益。
4. 最后运行 10–12，把执行隔离、开放协议和全链路观测补齐。

## 面试时应主动说明的边界

- LLM 只提出计划或候选动作，权限、schema、预算、幂等和提交仍由确定性控制面负责。
- “并行”“重试”“恢复”都必须定义副作用语义；没有 invocation key 和 checkpoint，就不能声称恰好一次。
- Tool Discovery、MCP 能力发现和真正授权是三件事，模型看见工具不代表可以调用。
- Reflection 与 Multi-Agent 会增加 token、延迟和相关错误，必须与更简单基线做逐任务消融。
- 教学 AST VM 不是操作系统沙箱；生产环境仍需独立身份、容器或 microVM、网络代理和资源配额。
- Trace 记录结构化元数据、版本和因果关系，不默认保存秘密、完整提示或原始工具结果。

## 运行与验收

在仓库根目录启动 Jupyter，逐本从空内核运行。每本均使用受控小数据，断言用于验证状态机、权限、停止条件和数值结论；它们是机制测试，不代表真实模型或线上业务的最终效果。

主要研究入口包括 [Anthropic 的 Agent 构建模式](https://www.anthropic.com/engineering/building-effective-agents)、[MCP Architecture](https://modelcontextprotocol.io/docs/learn/architecture)、[MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)、[AgentBench](https://arxiv.org/abs/2308.03688) 与 [OpenTelemetry GenAI 语义约定](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/)。

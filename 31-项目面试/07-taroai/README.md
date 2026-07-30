# Taroai：项目面试题

仓库：[`skygazer42/Taroai`](https://github.com/skygazer42/Taroai)。Taroai 是云优先、多租户 Agent 工作空间：FastAPI 控制平面、异步 worker、PostgreSQL/Redis/S3 或 MinIO 数据平面，支持模型、MCP/连接器、ACL 检索、记忆、沙箱、浏览器、评测、审计、计费和定时触发。`infra/docker-compose.yml` 明确了 healthcheck、worker、副本、可选 sandbox profile 与资源上限。

## 多租户平台与权限模型

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [用控制面与数据面解释 Taroai 的总体架构。](./01.md) | API、workers、Postgres、Redis、MinIO、模型和外部 controller 的边界。 |
| 02 | [workspace、tenant、user、Agent、skill、tool、run 的 ownership 如何建模？](./02.md) | 每张资源表的 tenant key 与访问检查位置。 |
| 03 | [RBAC、SSO、SCIM 与资源级 ACL 各解决什么问题？](./03.md) | 身份、角色、人员同步与对象权限不可混为一谈。 |
| 04 | [如何保证 tenant A 永远不能通过 ID 猜测访问 tenant B 的 artifact 或记忆？](./04.md) | 服务端 scope、存储 key、DB RLS/查询和负向测试。 |
| 05 | [外部分享链接如何设计有效期、撤销与最小权限？](./05.md) | token hash、secret rotation、访问审计。 |
| 06 | [为什么 Web、API、agent worker、trigger worker 要拆为独立 service？](./06.md) | 扩缩容、失败域、权限与部署节奏。 |
| 07 | [`agent-worker` 两副本如何避免同一任务被执行两次？](./07.md) | queue claim、lease、幂等 run 与 fencing。 |
| 08 | [API readiness 为什么依赖 Postgres、Redis、MinIO 与迁移完成？](./08.md) | Compose `depends_on` 不是运行时正确性保证。 |
| 09 | [schema migration 在多副本服务启动时如何防止竞争？](./09.md) | 单独 migration job、锁和回滚计划。 |
| 10 | [本地 Compose 默认密钥与生产密钥策略为何必须不同？](./10.md) | `dev_only` 默认值、secret manager、启动 gate。 |

## Agent 执行、工具与知识

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [一次 Agent run 的状态机、输入快照和可重放边界是什么？](./11.md) | queued/running/tool waiting/succeeded/failed/cancelled。 |
| 12 | [模型调用、工具调用、浏览器和沙箱输出如何聚合为用户可理解的证据？](./12.md) | event log、artifact、引用和 UI 展开策略。 |
| 13 | [动态工具发现/MCP 如何避免“模型看到什么就能调用什么”？](./13.md) | allowlist、tenant policy、参数 schema 和审批。 |
| 14 | [工具调用失败、超时或副作用不明确时如何重试？](./14.md) | 幂等分类、compensation、retry budget。 |
| 15 | [模型 provider 的抽象接口应包含哪些能力差异？](./15.md) | streaming、tool calling、vision、context、rate limit、价格。 |
| 16 | [文件摄取到 ACL 检索的索引流程如何做版本与删除传播？](./16.md) | document version、chunk、embedding、tombstone。 |
| 17 | [短期上下文、用户记忆、团队知识和 Agent 记忆如何区分？](./17.md) | scope、TTL、可编辑性、检索优先级。 |
| 18 | [为什么 sandbox 与 browser controller 以可选 profile 部署？](./18.md) | 攻击面、资源、授权和按需启用。 |
| 19 | [Docker sandbox 的只读 rootfs、drop capabilities、PID/memory/CPU limit 分别防什么？](./19.md) | 证据：`Dockerfile.sandbox` 与 Compose 环境变量。 |
| 20 | [即使沙箱受限，如何防止 Agent 用网络、挂载或秘密解析器绕过策略？](./20.md) | egress、mount、secret broker、审计与最小权限。 |

## 调度、运营与安全追问

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [`trigger_due` 与 `trigger_scheduler` 为什么分开？如何处理错过的定时任务？](./21.md) | polling、时钟、backfill、幂等 schedule key。 |
| 22 | [webhook trigger 的签名、重放防护和 tenant 映射怎样设计？](./22.md) | signing secret、timestamp、nonce 和 audit。 |
| 23 | [如何对每个 tenant 实施模型 token、工具、沙箱与存储的配额？](./23.md) | 预估、硬限制、账单和超额体验。 |
| 24 | [系统的 evaluation gate 应在发布 Agent 的哪个阶段运行？](./24.md) | prompt/skill/tool/config 变更后的离线与线上 shadow。 |
| 25 | [对含副作用的 Agent，审批应该出现在计划前、工具前还是结果前？](./25.md) | 风险等级、不可逆动作与用户体验。 |
| 26 | [怎样将一次失败从 UI 追到 API、worker、provider、sandbox 和对象存储？](./26.md) | trace ID、run ID、structured logs 和 timeline。 |
| 27 | [Redis、Postgres、MinIO 任一短暂不可用时，哪些请求能接受、哪些必须拒绝？](./27.md) | 一致性、缓存和 durability 的边界。 |
| 28 | [你如何做灾备：run 状态、artifact、密钥和审计日志的 RPO/RTO 各是多少？](./28.md) | 备份、恢复演练与风险披露。 |
| 29 | [设计一次 Agent 压测，如何区分 LLM 限流、worker 饱和与 sandbox 配额？](./29.md) | workload、队列深度、分段延迟、失败注入。 |
| 30 | [如果只能在下一季度做三项工作，你如何在功能、可靠性与安全之间排序？](./30.md) | 必须给出量化风险和验证标准。 |

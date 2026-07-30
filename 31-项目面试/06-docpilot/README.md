# DocPilot：项目面试题

仓库：[`skygazer42/DocPilot`](https://github.com/skygazer42/DocPilot)。DocPilot 是独立的生产级文档解析服务，覆盖 PDF、Office、图片、邮件、网页与文本，返回 Markdown、structured JSON、chunks、ingest records 与资产；以 Flask/OpenAPI 暴露同步、流式和异步接口，具备健康检查、指标、artifact 持久化、审计、限流和多解析引擎路由。

## 服务定位与 API 契约

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [为什么 DocPilot 只做解析，不直接承担向量检索和问答？](./01.md) | 边界、复用、扩缩容和失败隔离。 |
| 02 | [描述 `/api/v1/parse` 的输入、输出和同步/异步选择条件。](./02.md) | 文件、engine、profile、artifact、chunk 选项。 |
| 03 | [Markdown、`structured.json`、`chunks.jsonl`、`ingest.jsonl` 各面向什么消费者？](./03.md) | 不同格式必须共享哪些稳定 ID。 |
| 04 | [API 如何表达部分成功：正文成功但表格/OCR 失败？](./04.md) | manifest、warning、错误码与可重试性。 |
| 05 | [如何定义 artifact 的生命周期与下载鉴权？](./05.md) | key、tenant、过期、删除与引用计数。 |
| 06 | [OpenAPI 怎样成为 SDK、前端和集成方的契约，而非过期文档？](./06.md) | CI schema diff、contract test 和版本化。 |
| 07 | [`health`、`ready`、`metrics` 的语义为何不同？](./07.md) | 进程活着、依赖可用、可观测性。 |
| 08 | [API key、认证 header 和 CORS 如何设计，怎样避免默认不安全？](./08.md) | `main.py` 中鉴权配置、环境变量与 preflight。 |
| 09 | [上传文件如何限制体积、类型、压缩炸弹和恶意内容？](./09.md) | `validate_file`、魔数、页数/像素/解压预算。 |
| 10 | [请求 ID、tenant ID 与审计事件如何贯穿一次解析？](./10.md) | `X-Request-ID`、`X-Tenant-ID` 和 audit store。 |

## 多引擎解析与结构化产物

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [`docpilot`、`paddleocr_vl`、`mineru`、`plain` 应如何路由？](./11.md) | 格式、质量、时延、硬件与可用性策略。 |
| 12 | [为什么需要兼容 `deepdoc` 旧别名，如何避免永久技术债？](./12.md) | alias 生命周期、遥测、弃用告警。 |
| 13 | [PDF 原生文本、扫描件 OCR、复杂多栏版面分别走什么策略？](./13.md) | 质量检测、回退与 provenance。 |
| 14 | [表格、公式、图片等 asset 如何关联回页码、坐标和文本块？](./14.md) | `ParseAsset/Block/Manifest` 的关系。 |
| 15 | [chunk 如何保证不跨越不应切断的标题、表格或语义单元？](./15.md) | strategy、token 上限、overlap 与结构边界。 |
| 16 | [token 计数在不同模型 tokenizer 下为何不稳定，服务如何声明口径？](./16.md) | 默认 tokenizer、近似误差与 profile version。 |
| 17 | [对 Office、邮件和网页，怎样防止外部资源抓取带来 SSRF 或不稳定？](./17.md) | allowlist、网络隔离、超时与原始副本。 |
| 18 | [多引擎对同一 PDF 产物不同，你如何评测并选择默认策略？](./18.md) | 标注集、CER/WER、结构 F1、成本/时延。 |
| 19 | [如何保持解析结果的可复现性？](./19.md) | 输入 hash、engine/model/version/config 和代码 build info。 |
| 20 | [文档重新上传或重复解析时，怎样去重又不违反 tenant 隔离？](./20.md) | content hash 的作用域、artifact key 与访问控制。 |

## 异步、运维与安全追问

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [为什么大文件/模型密集解析要异步化？任务状态机如何设计？](./21.md) | queued/running/succeeded/failed/cancelled 与幂等键。 |
| 22 | [回调投递失败如何重试，怎样避免把同一结果写入下游多次？](./22.md) | signature、retry、dead letter、幂等 consumer。 |
| 23 | [admission control 与 rate limit 分别保护什么资源？](./23.md) | 并发 GPU/CPU 池、租户配额和响应头。 |
| 24 | [`main.py` 中全局 app/配置/缓存的初始化顺序会带来哪些测试风险？](./24.md) | import side effect、环境隔离和 app factory。 |
| 25 | [OCR 模型未下载、GPU 不可用或 Java/Tika 缺失时，接口应如何降级？](./25.md) | readiness、明确 capability 与可操作错误。 |
| 26 | [Prometheus 指标怎样避免记录文件名等高基数字段？](./26.md) | 只记录引擎、结果、格式、tenant tier 等有限 label。 |
| 27 | [如何做 retention janitor，既删掉过期 artifact 又不误删活跃任务结果？](./27.md) | tombstone、引用检查、延迟删除和审计。 |
| 28 | [你会怎样构造安全回归集：密码 PDF、畸形文件、提示注入、超大图？](./28.md) | 隔离样本、资源上限和无敏感内容原则。 |
| 29 | [解释一次从用户报错到具体 parser/model 的排障路径。](./29.md) | request→manifest→trace→worker/resource→input。 |
| 30 | [若吞吐增长十倍，你优先改进什么：解析路由、队列、缓存还是模型？](./30.md) | 用 workload 分布与压测证据回答。 |

# ForeSight：项目面试题

仓库：[`skygazer42/ForeSight`](https://github.com/skygazer42/ForeSight)。这是时序预测工具包：统一模型注册、walk-forward 回测、概率预测、CLI/Python API、面板数据 `unique_id / ds / y` 长表格式。`pyproject.toml` 显示核心仅依赖 NumPy/Pandas，重型后端通过 extras 按需安装，并提供 `foresight` CLI。

## 产品与公共接口

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [ForeSight 的目标用户、核心工作流和你负责的内容是什么？](./01.md) | 不将模型数量当作价值；证据：README、`src/foresight/`。 |
| 02 | [为什么把统一 API、模型 registry、CLI 和 artifact schema 作为稳定表面？](./02.md) | 解释兼容承诺与内部实现解耦。 |
| 03 | [`unique_id / ds / y` 长表格式为何适合 panel/global forecasting？](./03.md) | 与宽表的转换、频率、缺失和多序列边界。 |
| 04 | [Python API 与 CLI 如何复用同一套业务逻辑，避免行为分叉？](./04.md) | service 层、参数 schema、端到端测试。 |
| 05 | [`foresight doctor` 应检查什么，为什么比导入失败更早暴露问题？](./05.md) | extras、运行时、数据目录和 provider 可用性。 |
| 06 | [基础安装只依赖 NumPy/Pandas 有何收益和代价？](./06.md) | 最小安装、导入延迟与可选后端错误提示。 |
| 07 | [250+ 模型如何避免“同名但语义不同”的配置灾难？](./07.md) | model spec、能力元数据和参数标准化。 |
| 08 | [如何定义并演进 forecast artifact 的序列化契约？](./08.md) | 版本号、schema migration、反序列化兼容。 |
| 09 | [GPL-3.0-only 的包许可证会如何影响用户集成与发布？](./09.md) | 区分法律建议与需要法务确认的边界。 |
| 10 | [你会如何设计一次从包发布到 PyPI 安装的 release gate？](./10.md) | build、wheel、clean env、smoke test、签名。 |

## 模型执行与回测

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [registry 如何解析模型名、后端依赖和运行时 adapter？](./11.md) | 证据：`models/registry.py`、`models/runtime.py`。 |
| 12 | [新接入一个 statsmodels 或 torch 模型，需要遵守什么接口？](./12.md) | `fit/predict`、随机性、频率、协变量和序列 ID。 |
| 13 | [walk-forward backtesting 的训练窗、预测窗与 step 如何定义？](./13.md) | 画出时间线，严禁未来数据泄漏。 |
| 14 | [多序列 panel 回测如何保证每个序列只看到自己的过去？](./14.md) | join、排序、group 切分和全局模型的合法信息。 |
| 15 | [缺失时间戳、非等频数据和 DST 如何处理？](./15.md) | 显式 frequency contract，不默默填补。 |
| 16 | [概率预测输出哪些对象，区间覆盖率怎么评估？](./16.md) | quantile、sample、calibration、PICP/CRPS。 |
| 17 | [20+ 指标如何保证方向一致、尺度可比和异常可解释？](./17.md) | MASE/sMAPE/RMSE 边界、零值与聚合口径。 |
| 18 | [leaderboard 应如何防止不同模型使用不同数据或不同预算导致不公平？](./18.md) | 固定 split、超时、资源、随机种子和失败记录。 |
| 19 | [全局模型和每序列局部模型各自在什么数据条件下更合适？](./19.md) | 样本量、同质性、冷启动和推理成本。 |
| 20 | [模型训练失败或不支持某个数据特性时，框架如何给出可行动错误？](./20.md) | capability matrix、preflight 和降级建议。 |

## 质量、性能与生产追问

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [如何为跨 7 个后端的统一接口写有效测试，而不依赖每个大依赖？](./21.md) | contract tests、mock、optional CI matrix。 |
| 22 | [README 所说的 stable/beta/experimental 如何落实到版本与 CI？](./22.md) | 文档、弃用策略、测试覆盖和支持边界。 |
| 23 | [如何缓存训练产物，同时确保数据、特征和模型配置变更会失效缓存？](./23.md) | content hash、schema/version 和 lineage。 |
| 24 | [时间序列数据量很大时，内存与特征生成的瓶颈在哪里？](./24.md) | lazy loading、分区、向量化和并行。 |
| 25 | [预测服务如何监控 drift、校准退化和数据到达延迟？](./25.md) | online metric、告警阈值和 retrain policy。 |
| 26 | [如何保证随机模型在两次运行间可复现？](./26.md) | 全局 RNG、后端种子、硬件非确定性与记录。 |
| 27 | [展示一个从错误预测回溯到原始数据、切分和模型 artifact 的诊断链。](./27.md) | lineages、run ID、配置快照和图表。 |
| 28 | [如果用户请求一个未安装的 extra，为什么不能直接在运行时 `pip install`？](./28.md) | 可复现、供应链、安全和服务权限。 |
| 29 | [你会如何做性能基准，区分 fit、forecast、加载和端到端耗时？](./29.md) | 数据规模、硬件、warmup、p50/p95 和成本。 |
| 30 | [下一个版本你优先投入一个新模型还是改进评测/兼容层？为什么？](./30.md) | 从用户风险、维护负担和证据作取舍。 |

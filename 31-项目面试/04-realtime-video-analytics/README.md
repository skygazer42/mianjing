# Realtime Video Analytics（32 Streams）：项目面试题

仓库：[`skygazer42/realtime-video-analytics-32streams`](https://github.com/skygazer42/realtime-video-analytics-32streams)。参考实现支持最多 32 路 RTSP/RTMP、异步 OpenCV 采集、H.265/FFmpeg、多种推理后端、轻量追踪、Kafka、Prometheus/Grafana 与 WebSocket 仪表盘；配置采用 YAML，提供 Docker、模拟流和本地 RTSP 演示。

## 架构、吞吐与时序

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [用一张图说明一帧从 RTSP 输入到 dashboard/Kafka 的数据路径。](./01.md) | 标出采集、队列、检测、追踪、事件、存储和推送。 |
| 02 | [“最多 32 路”具体受哪些资源约束？如何做容量估算？](./02.md) | 解码、显存、CPU、PCIe、网络、队列和目标 FPS。 |
| 03 | [为什么使用异步 OpenCV capture，在哪里仍可能阻塞？](./03.md) | IO、解码器、GIL、线程/进程边界。 |
| 04 | [RTSP 断开重连时如何避免旧帧、时间倒流和资源泄露？](./04.md) | epoch、重连退避、状态机和句柄回收。 |
| 05 | [H.264 与 H.265 在延迟、CPU 负载和兼容性上如何取舍？](./05.md) | FFmpeg 后端、硬解与指标验证。 |
| 06 | [为何每路都需要独立的目标 FPS、模型与 ROI 配置？](./06.md) | 多租户优先级、资源预算和 YAML schema。 |
| 07 | [处理速度低于输入帧率时，采用阻塞、丢旧帧还是采样？](./07.md) | 结合实时性目标、事件完整性与背压。 |
| 08 | [如何实现优先级调度，避免低优先级流饿死？](./08.md) | token/配额、加权轮询、老化和可观测性。 |
| 09 | [多路视频的时间戳是否可直接比较？不同摄像头时钟如何处理？](./09.md) | 时钟源、NTP、接收时间和事件窗口。 |
| 10 | [你怎样定义端到端延迟并量到 p50/p95/p99？](./10.md) | capture、decode、infer、emit、render 分段埋点。 |

## 检测、追踪、动作与事件

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [Ultralytics、ONNX Runtime、OpenVINO、TensorRT、RKNN 如何统一 detector 接口？](./11.md) | 输入预处理、输出坐标、错误与 capability contract。 |
| 12 | [模型、类别表和预处理版本不一致会造成什么线上故障？](./12.md) | artifact manifest、hash 与启动期校验。 |
| 13 | [检测结果如何从 letterbox 坐标还原到原图？](./13.md) | scale/pad 记录、边界裁剪和单元测试。 |
| 14 | [IOU tracker 的状态、匹配代价和失联轨迹如何设计？](./14.md) | track 生命周期、阈值和 ID switch。 |
| 15 | [何时应升级到 ByteTrack/DeepSORT，为什么没有一开始就上？](./15.md) | 小目标、遮挡、外观特征、计算成本。 |
| 16 | [detection、tracking、temporal action model 的窗口如何对齐？](./16.md) | 帧号、时间戳、缺帧与暖机。 |
| 17 | [ROI 多边形过滤放在检测前还是检测后？各自的性能与语义差异？](./17.md) | crop/mask、框中心/IoU 判定和可视化。 |
| 18 | [motion detection 驱动自适应 FPS 时，怎样避免漏掉短暂关键事件？](./18.md) | 最低采样率、事件触发升频和回放。 |
| 19 | [怎样设计事件的去重、合并和关闭语义？](./19.md) | event key、debounce、cooldown、track 生命周期。 |
| 20 | [推理后端给出不同置信度分布时，阈值是否能共用？](./20.md) | 校准、每模型 profile 和离线评测。 |

## 可靠性、观测和交付

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [Kafka sink 不可用时，系统应丢弃、落盘还是阻塞？](./21.md) | 业务优先级、磁盘上限、重放与告警。 |
| 22 | [Prometheus 指标应包含哪些 label，如何防止 label cardinality 爆炸？](./22.md) | stream ID 是否应成为 label 的取舍。 |
| 23 | [dashboard 通过 WebSocket 推送什么粒度的数据，如何避免前端被淹没？](./23.md) | 状态聚合、节流、最后值与订阅过滤。 |
| 24 | [`/health` 与“某一路相机可用”的健康语义有何区别？](./24.md) | liveness、readiness、stream health 与依赖健康。 |
| 25 | [如何用 FFmpeg 模拟器和 file-source 做可重复的端到端 smoke test？](./25.md) | 固定视频、断流注入、golden event。 |
| 26 | [Docker 部署中 GPU、模型文件、密钥和持久化状态如何管理？](./26.md) | runtime、挂载、image 分层与 secrets。 |
| 27 | [哪些故障会导致内存/显存逐步增长，你如何定位？](./27.md) | frame queue、tensor、capture 句柄和 heap/profile。 |
| 28 | [如何安全地在线修改 YAML 配置并回滚？](./28.md) | 配置校验、原子切换、版本和影子流。 |
| 29 | [请设计一次压测，验证 4→32 路扩容时的退化曲线。](./29.md) | 固定分辨率/模型、资源监控、SLO 与失败条件。 |
| 30 | [如果要从 Python 参考实现迁移到 DeepStream/TensorRT，哪些接口与测试必须保留？](./30.md) | detector/tracker contract、事件语义、parity 测试。 |

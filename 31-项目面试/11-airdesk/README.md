# AirDesk：项目面试题

仓库：[`skygazer42/AirDesk`](https://github.com/skygazer42/AirDesk)。AirDesk 是浏览器端手势交互原型：React 19 + TypeScript/Vite，使用本地打包的 MediaPipe Web Hand Landmarker（WASM/模型），支持 pinch、open palm、two-finger slide、fist、point、circle 六种意图；以 Three.js 组织空间任务卡，并可把自然语言命令 POST 给本地 runner 或使用浏览器 fallback。项目配置了 Vitest、Playwright 和 build 校验。

## 浏览器视觉与手势识别

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [描述从摄像头帧到任务卡行为的完整数据流。](./01.md) | getUserMedia、landmark、gesture state、Three.js/React 渲染。 |
| 02 | [为什么将 MediaPipe WASM 和模型打包在 `public/vendor/mediapipe`，而不是 CDN？](./02.md) | 离线、隐私、可用性、首次加载与更新代价。 |
| 03 | [21 点 hand landmark 怎样转换为稳定手势特征？](./03.md) | 距离归一化、角度、手掌尺度、左右手镜像。 |
| 04 | [pinch、point、fist 等手势容易互相混淆，如何设计优先级？](./04.md) | 置信度、状态机、时间连续性和冲突解析。 |
| 05 | [如何抗抖动，防止一帧误判造成点击或删除？](./05.md) | debounce、hysteresis、最短持续时间、cooldown。 |
| 06 | [two-finger slide 的位移如何从相机坐标映射到屏幕/3D 坐标？](./06.md) | 镜像、分辨率、坐标系、灵敏度和边界。 |
| 07 | [circle 手势的轨迹检测如何区分随意挥手？](./07.md) | 轨迹缓冲、闭合度、方向、速度和置信度。 |
| 08 | [30fps 推理/渲染会占多少主线程时间，如何保证 UI 不掉帧？](./08.md) | requestVideoFrameCallback、worker、节流和 profiling。 |
| 09 | [多只手或手离开画面时，如何维护 active hand 与交互状态？](./09.md) | hand ID、丢失超时和状态 reset。 |
| 10 | [用户没有摄像头、权限被拒绝或浏览器不支持 WASM 时怎样降级？](./10.md) | fallback gesture pad、明确错误和可访问性。 |

## 交互、3D 与命令执行

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [为什么用 Three.js 空间任务卡，而不是普通 2D 列表？](./11.md) | 任务可视化价值与认知/性能成本。 |
| 12 | [React state 与 Three.js scene state 如何同步，怎样避免每帧触发 React render？](./12.md) | imperative ref、事件桥、帧循环边界。 |
| 13 | [手势意图应该直接执行动作还是先映射为统一 command？](./13.md) | 意图层、可测试性、可配置性与权限。 |
| 14 | [`VITE_AIRDESK_COMMAND_ENDPOINT` 的网络协议、超时、重试和响应 schema 如何设计？](./14.md) | 本地 runner 不可信时的输入校验。 |
| 15 | [为什么提供浏览器 fallback 命令响应？它不能伪装成真实 Agent 的哪些能力？](./15.md) | demo 降级与结果来源标识。 |
| 16 | [手势驱动高风险动作时，如何实现确认、撤销和误操作恢复？](./16.md) | dwell/confirm、undo stack 和权限。 |
| 17 | [如何给用户解释识别到的手势、当前模式与失败原因？](./17.md) | 即时 visual feedback、教程和 telemetry。 |
| 18 | [触控、鼠标、键盘与手势如何共存而不让用户迷失？](./18.md) | input abstraction、focus、快捷键与无障碍。 |
| 19 | [摄像头图像是否上传？如果将来接入云端模型，如何重做隐私设计？](./19.md) | 本地处理声明、consent、最小化与删除。 |
| 20 | [如何针对不同光照、肤色、相机位置和左右手做公平性与鲁棒性测试？](./20.md) | 测试矩阵、失败率与不恰当结论边界。 |

## 前端工程与质量追问

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [`npm run build` 中 `tsc -b` 与 Vite build 分别捕获什么问题？](./21.md) | typecheck、asset bundle 和部署产物。 |
| 22 | [Vitest 单元测试最适合覆盖哪些纯逻辑？](./22.md) | gesture classifier、mapping、reducer、endpoint client。 |
| 23 | [Playwright E2E 如何模拟摄像头与 media permissions，而不依赖真人手势？](./23.md) | fake device、录像、mock landmark 与 golden state。 |
| 24 | [摄像头停止、组件卸载或路由切换时如何释放 MediaStream 和动画循环？](./24.md) | track.stop、dispose、RAF cancel 和内存检查。 |
| 25 | [本地 WASM/模型 asset 如何版本化与缓存失效？](./25.md) | 文件 hash、service worker、兼容矩阵。 |
| 26 | [为什么 localhost 能访问摄像头而局域网 HTTP 常被浏览器拦截？](./26.md) | secure context、HTTPS 和部署方式。 |
| 27 | [如何测量 first camera-ready、first landmark、gesture-to-action 的体验指标？](./27.md) | 埋点时间点、p50/p95 与设备分层。 |
| 28 | [发现某型号摄像头启动失败时，你的排查顺序是什么？](./28.md) | enumerateDevices、permission、format、HTTPS、日志。 |
| 29 | [如果将来要支持双手复杂操作，现有架构在哪些点需要重构？](./29.md) | input model、state machine、3D interaction 与测试。 |
| 30 | [哪些产品假设尚未被验证？你如何设计小实验验证用户愿意长期用手势操作？](./30.md) | 任务完成率、疲劳、学习曲线和访谈。 |

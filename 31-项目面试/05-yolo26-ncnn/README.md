# YOLO26 NCNN：项目面试题

仓库：[`skygazer42/yolo26-NCNN`](https://github.com/skygazer42/yolo26-NCNN)。C++ + NCNN 推理示例支持 YOLO26 detection/segmentation、常规 one-to-many NMS 导出及 end-to-end one-to-one raw 输出；CMake 建立 `yolo26` 库、检测/分割可执行文件，并提供 TopK、NMS、mask parity 工具。

## 模型导出与运行时接口

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [请说明 PyTorch 权重到 NCNN 端侧推理的完整制品链。](./01.md) | `*.pt`、ONNX/NCNN param/bin、类别表、输入尺寸与版本。 |
| 02 | [为什么仓库不提交模型权重和导出目录？](./02.md) | 体积、许可、可复现下载与 manifest。 |
| 03 | [one-to-many NMS 输出与 one-to-one raw 输出有什么差异？](./03.md) | 为什么 raw 图内无 TopK，后处理责任在哪里。 |
| 04 | [`--post=nms` 与 `--post=topk` 的前置条件、输出语义和风险是什么？](./04.md) | 不匹配时怎样快速失败。 |
| 05 | [`--box=cxcywh` 和 `--box=xyxy` 为什么不能仅靠猜测？](./05.md) | 模型导出 metadata、断言和样例图。 |
| 06 | [CMake 如何把公共库、可选 segmentation 和 helper tools 分层？](./06.md) | 证据：`CMakeLists.txt` 的 target 和 option。 |
| 07 | [NCNN、OpenCV 与 C++ ABI 版本不兼容时如何诊断？](./07.md) | CMake find_package、动态库和最小环境。 |
| 08 | [CPU 与 `--gpu` 运行路径有什么差别，何时 GPU 反而更慢？](./08.md) | 上传开销、小 batch、设备能力和 profiling。 |
| 09 | [模型输入尺寸变动时，哪些预处理/后处理参数必须同步改变？](./09.md) | resize、stride、坐标缩放、mask 原图映射。 |
| 10 | [如何将模型、导出脚本和运行命令做成可重复的 release artifact？](./10.md) | lockfile、hash、命令记录和 CI。 |

## 检测与分割的数值正确性

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [letterbox 预处理怎样记录 scale 和 padding，并精确逆变换 bbox？](./11.md) | 奇数 padding、边界裁剪和单测。 |
| 12 | [置信度通常如何由 objectness/class score 组合？](./12.md) | 模型输出格式差异，不能硬编码假设。 |
| 13 | [class-aware NMS 与 class-agnostic NMS 的业务差别是什么？](./13.md) | `--agnostic` 的适用场景和误杀风险。 |
| 14 | [`--iou`、`--conf`、`--max-det` 共同如何影响精度、延迟和内存？](./14.md) | 需要用指标而非直觉调参。 |
| 15 | [TopK 方案为什么仍可能出现重复框？`--dedup` 应如何定义？](./15.md) | 同类/跨类、坐标近似和稳定排序。 |
| 16 | [NMS parity 工具需要比较哪些内容才有意义？](./16.md) | box、score、class、排序、阈值与容差。 |
| 17 | [segmentation prototype 与每个 detection mask coefficient 如何组合？](./17.md) | 张量形状、sigmoid、crop 和 resize 顺序。 |
| 18 | [`--retina` 模式改变了哪一步 mask 处理，质量/性能怎样权衡？](./18.md) | 原分辨率 mask 与低分辨率 crop。 |
| 19 | [mask parity 允许哪些浮点误差，什么时候误差意味着实现 bug？](./19.md) | 精度、resize 插值、阈值和视觉 diff。 |
| 20 | [如果 C++ 结果与 Python 结果不一致，你的二分排查顺序是什么？](./20.md) | 输入 blob→原始输出→decode→NMS/mask→渲染。 |

## 性能、鲁棒性与部署追问

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [单张延迟应拆分测量哪些阶段，如何避免把图片读写混进 benchmark？](./21.md) | preprocess、extract、postprocess、draw 分别计时。 |
| 22 | [如何选择 NCNN 线程数和 CPU affinity，避免与摄像头/业务线程争用？](./22.md) | 热核、大小核、吞吐与 p99。 |
| 23 | [如何评估 FP16/INT8 量化带来的精度损失？](./23.md) | calibration set、per-class AP、边缘样例。 |
| 24 | [端侧内存紧张时，模型加载、workspace 和图像 buffer 如何治理？](./24.md) | 复用、池化、上限与 OOM 处理。 |
| 25 | [非法 param/bin、类别数不匹配或空图片输入时如何给出安全错误？](./25.md) | 输入验证与不崩溃原则。 |
| 26 | [为什么需要检测与分割各自独立的 CLI，而不是一个万能二进制？](./26.md) | 模型 contract、可维护性与发布体积。 |
| 27 | [怎样为 Android/嵌入式设备构建交叉编译和 smoke test？](./27.md) | toolchain、ABI、设备农场和资源限制。 |
| 28 | [用户要求新增姿态/OBB 模型，你如何扩展而不破坏现有接口？](./28.md) | task enum、output decoder、feature flag 和 regression。 |
| 29 | [请给出一次“模型看起来跑通但结果全错”的典型根因。](./29.md) | RGB/BGR、归一化、布局、输出格式或类别表。 |
| 30 | [线上发布前你会设哪些 correctness/performance gate？](./30.md) | parity、golden image、延迟、内存、崩溃率与回滚。 |

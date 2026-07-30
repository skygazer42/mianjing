# Ultralight Digital Human：项目面试题

仓库：`skygazer42/Ultralight-Digital-Human`（私有）。项目实现端到端口型驱动数字人：数据处理、Landmark、HuBERT/Wenet/AVE 音频分支、SyncNet、UNet、覆盖均衡/困难样本采样，并覆盖 PyTorch、ONNX Runtime、TensorRT、MNN 推理路径。`train.py` 中可见 `WeightedRandomSampler`、感知损失、SyncNet、梯度裁剪、学习率调度与早停参数。

## 数据、时序与模型设计

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [口型驱动的输入、输出和监督信号分别是什么？](./01.md) | 视频帧、音频特征、目标帧、Landmark 与时间对齐。 |
| 02 | [HuBERT、Wenet、AVE 分支为什么对应不同帧率/分辨率约束？](./02.md) | README 的 25fps/20fps/320×320 合同。 |
| 03 | [视频帧率与音频特征错位一个 frame 会产生什么现象，如何检测？](./03.md) | A/V offset 实验、SyncNet 指标与可视化。 |
| 04 | [数据预处理如何保证人脸 crop、关键点和音频来自同一原始片段？](./04.md) | sample ID、时间戳、hash 和清单。 |
| 05 | [Landmark 检测失败、遮挡、侧脸或运动模糊样本怎样处理？](./05.md) | 过滤、重试、质量标签与不确定性。 |
| 06 | [UNet 为什么适合该任务？输入中哪些区域/通道承载身份与语音条件？](./06.md) | encoder/decoder、skip connection 和条件融合。 |
| 07 | [Base 160 与 328 模型如何权衡质量、显存、延迟与数据量？](./07.md) | 不能仅以分辨率大断言更好。 |
| 08 | [为什么需要 SyncNet，而不只最小化像素 L1/L2 损失？](./08.md) | 清晰度并不等于音画同步。 |
| 09 | [`cosine_loss`、BCE 和同步权重的数值含义是什么？](./09.md) | embedding 相似度范围、label 与梯度稳定性。 |
| 10 | [`train.py` 的感知损失为什么固定 ImageNet backbone 并设为 eval/frozen？](./10.md) | `MobileNetV3`、归一化与可训练参数边界。 |

## 采样、训练与评估

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [覆盖均衡加权采样要解决什么数据偏差？](./11.md) | 视角、人物、嘴型、音素或动作长尾。 |
| 12 | [`WeightedRandomSampler(..., replacement=True)` 为什么可能造成过拟合？](./12.md) | 有效样本量、权重截断和 validation 切分。 |
| 13 | [`weights_hard.npy` 优先于 `weights.npy` 的逻辑是什么？](./13.md) | hard-negative/hard-sample 的定义与失效机制。 |
| 14 | [困难样本挖掘怎样避免模型只学习噪声或标签错误？](./14.md) | warm-up、混合比例、质量阈值和人工抽检。 |
| 15 | [训练/验证/测试为什么必须按原视频或说话人切分？](./15.md) | 相邻帧泄漏和身份泄漏。 |
| 16 | [DataLoader 的 `num_workers`、pin memory、persistent workers 如何影响吞吐与稳定性？](./16.md) | 证据：`make_dataloader`。 |
| 17 | [梯度裁剪、早停、调度器各主要防什么训练故障？](./17.md) | gradient explosion、过拟合、plateau。 |
| 18 | [多个 loss 的权重如何调，而不是靠主观感觉？](./18.md) | 量纲、梯度范数、ablation、目标指标。 |
| 19 | [除了重建误差，你如何评价唇形同步、视觉自然度与身份保持？](./19.md) | Sync、LPIPS/FID、人工 MOS 与 failure slice。 |
| 20 | [如何保证离线训练结果可复现？](./20.md) | seed、代码/数据/model hash、环境和 non-determinism。 |

## 推理、部署与工程追问

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [从 PyTorch 到 ONNX Runtime、TensorRT、MNN 时，最易发生哪些语义偏差？](./21.md) | dynamic shape、opset、预后处理、精度与 A/V 对齐。 |
| 22 | [如何设计 PyTorch/ONNX/TRT 的逐层或逐输出 parity 测试？](./22.md) | 固定输入、容差、目标帧和最终视频 diff。 |
| 23 | [实时场景为什么需要帧队列与背压，而不是逐帧同步推理？](./23.md) | 延迟累积、drop policy、音频连续性。 |
| 24 | [GPU 不可用时，当前代码如何运行？用户体验上如何提示性能限制？](./24.md) | `cuda` fallback 与功能/性能边界。 |
| 25 | [checkpoint 载入为什么使用 `map_location`，`weights_only` 解决了什么风险？](./25.md) | 兼容 fallback 与反序列化安全。 |
| 26 | [模型、SyncNet、ASR 特征提取器版本不匹配时怎样 fail fast？](./26.md) | manifest、shape/spec 和启动检查。 |
| 27 | [手机端 MNN 部署面对的内存、线程和热量约束如何评估？](./27.md) | 真实设备 benchmark 和质量降级。 |
| 28 | [数据与生成视频可能涉及肖像/声音，训练和演示需满足哪些授权与删除要求？](./28.md) | consent、来源、用途限制和 retention。 |
| 29 | [请讲一个同步差的样例，从音频、特征、数据到模型的排查顺序。](./29.md) | 避免只重训；先证实数据时间轴。 |
| 30 | [若要把质量提升作为下阶段目标，你会优先改善数据、loss、架构还是部署？](./30.md) | 给出基线、假设和可证伪实验。 |

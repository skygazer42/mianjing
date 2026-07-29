# 控制、时序与离散生成模型

本目录继续采用“公式 → 手写 `nn.Module`/`forward` → 数值 oracle → 受控训练 → 发布合同”的结构，覆盖连续控制、可解释时序分解和离散潜变量生成。

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | Notebook | 核心问题 |
| --- | --- | --- |
| 01 | [SAC 连续控制](./01-sac-continuous-control-from-scratch-pytorch.ipynb) | squashed Gaussian、双 Q、entropy temperature、replay、bootstrap 与软更新如何实现？ |
| 02 | [N-BEATS 时序预测](./02-nbeats-time-series-from-scratch-pytorch.ipynb) | backcast/forecast、残差堆叠、趋势/季节 basis、严格时间切分与直接多步预测如何实现？ |
| 03 | [VQ-VAE 离散潜变量](./03-vqvae-from-scratch-pytorch.ipynb) | 最近邻 codebook、straight-through、commitment/codebook loss、perplexity 与 code 解码如何实现？ |

三本均使用离线合成小数据，只验证机制、数值合同和工程边界，不代表真实机器人、业务时序或图像生成质量。运行环境为 Python 3.10+、PyTorch 2.x、CPU 单线程，不下载外部模型或数据。

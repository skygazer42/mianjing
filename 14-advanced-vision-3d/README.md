# 进阶视觉与三维重建（58–60）

这一目录用 PyTorch 基础算子复现现代视觉预训练、可提示分割与可微三维渲染的关键机制。三本 Notebook 均为中文讲解、CPU/offline/单线程可运行；不调用 `torchvision.models`、`timm`、SAM 包、`nerfstudio`、`pytorch3d`、现成 Transformer 或 `nn.MultiheadAttention`。

| 编号 | Notebook | 核心问题 |
| --- | --- | --- |
| 58 | [从零实现 Masked Autoencoder](./58-masked-autoencoder-from-scratch-pytorch.ipynb) | patch 双射、逐样本确定性 masking、visible-only encoder、restore index、mask token decoder 与 masked-only loss如何实现？ |
| 59 | [从零实现 SAM 风格可提示分割](./59-sam-promptable-segmentation-from-scratch-pytorch.ipynb) | 正/负/填充点、box prompt、双向 cross-attention、多 mask、IoU head 与最佳候选选择如何串联？ |
| 60 | [从零实现教学版 3D Gaussian Splatting](./60-3d-gaussian-splatting-from-scratch-pytorch.ipynb) | 相机投影、Jacobian covariance、椭圆权重、深度排序、front-to-back 合成与可微优化如何实现？ |

## 运行与边界

- 在本目录或仓库根目录使用 Python 3.10+、PyTorch 2.x 顺序运行；不下载数据或模型。
- 每本均包含公式与 shape、数值 oracle、受控训练/推理、复杂度、失败模式、生产差距及原始论文/官方链接。
- 合成数据上的低 loss 或高 IoU 只证明实现通过受控机制测试，不能解释为自然图像泛化、官方 SAM 能力或真实新视角合成质量。
- 发布示例逐参数绑定 key/dtype/shape/bytes，并绑定 data、split、preprocess、camera/recipe；loader 只信任包外只读 publisher registry，整体重签伪造会被拒绝。

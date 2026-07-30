# Diffusion Models：项目面试题

仓库：[`skygazer42/Diffusion-Models`](https://github.com/skygazer42/Diffusion-Models)。仓库以学习与对比为目标，组织 VAE、β-VAE、VQ-VAE、ELBO、Glow/flow、DDPM 和简化 DALL·E 的 Notebook/PyTorch 实现，并计划比较 CIFAR-10、MNIST、CelebA 上的 FID、IS、重建误差和采样结果。README 中包含上游 `jhlucc` 链接，面试时需先如实区分 fork/复用与实际贡献。

## 贡献边界与实验设计

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 01 | [本仓库哪些模型、Notebook、实验和文档由你新增或修改？](./01.md) | 先说明 upstream/fork 边界、commit 与许可证。 |
| 02 | [为什么把 VAE、flow、diffusion、text-to-image 放在同一学习仓库？](./02.md) | 比较共同的生成目标与不同概率建模假设。 |
| 03 | [如何让跨模型对比公平，而不是各自用不同数据/预处理/训练预算？](./03.md) | 固定 split、分辨率、compute、seed 与报告。 |
| 04 | [MNIST、CIFAR-10、CelebA 分别适合验证什么，哪些结论不能外推？](./04.md) | 数据复杂度、分辨率和指标局限。 |
| 05 | [Notebook 如何避免隐藏状态造成“从头运行失败”？](./05.md) | restart-run-all、依赖、随机种子、路径和 CI。 |
| 06 | [训练配置、模型权重、样本和指标如何形成可追溯实验记录？](./06.md) | config hash、git SHA、environment、artifact。 |
| 07 | [FID、IS、MSE 各测什么，为什么不能只报一个分数？](./07.md) | fidelity/diversity、重建与生成、样本量。 |
| 08 | [生成样本看似漂亮但 mode collapse 时，哪些指标或可视化能发现？](./08.md) | coverage、nearest neighbor、类分布和人工检查。 |
| 09 | [如何处理公开数据集许可、CelebA 图像使用和生成内容风险？](./09.md) | 许可、用途限制和报告边界。 |
| 10 | [若只保留一个模型作为入门基线，你会选哪个，为什么？](./10.md) | 学习曲线、计算量、可解释性与可复现。 |

## VAE、VQ-VAE 与 Flow

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 11 | [从 ELBO 推导 VAE 的重建项与 KL 项，各自如何影响 latent space？](./11.md) | 说明变分下界，不把 ELBO 写成任意 loss。 |
| 12 | [重参数化技巧为何必要，梯度如何穿过随机采样？](./12.md) | `z = μ + σ ⊙ ε` 与数值稳定性。 |
| 13 | [β-VAE 增大 β 后，解耦、重建质量和 posterior collapse 如何权衡？](./13.md) | KL annealing、capacity 与实验。 |
| 14 | [posterior collapse 如何检测与缓解？](./14.md) | KL 曲线、decoder 强度、free bits、warm-up。 |
| 15 | [VQ-VAE 的 codebook 更新、commitment loss 和 dead code 如何理解？](./15.md) | EMA/SGD、perplexity、重初始化。 |
| 16 | [VQ-VAE 为什么有利于后续 Transformer/DALL·E 式离散建模？](./16.md) | 图像 token、上下文长度和信息损失。 |
| 17 | [Glow/normalizing flow 如何得到精确 likelihood，代价是什么？](./17.md) | invertibility、Jacobian log-det 和架构限制。 |
| 18 | [flow 与 VAE 的 latent prior、推理速度和样本质量如何比较？](./18.md) | exact density 不等于感知质量。 |
| 19 | [如何检查 encoder/decoder、codebook 或 flow 的 tensor shape 与梯度正确性？](./19.md) | 最小样本、assert、finite-difference/golden test。 |
| 20 | [重建 MSE 很低是否意味着生成模型好？](./20.md) | 解释训练目标与先验采样的差异。 |

## DDPM、采样与文本图像追问

| # | 面试题 | 追问 / 回答证据 |
| --- | --- | --- |
| 21 | [DDPM 前向加噪和反向去噪的基本概率过程是什么？](./21.md) | noise schedule、closed-form q(x_t|x_0)。 |
| 22 | [为什么常预测 epsilon，替代预测 x0/v 有什么影响？](./22.md) | 参数化、损失加权和采样稳定性。 |
| 23 | [beta schedule 怎样影响信噪比、训练难度和采样质量？](./23.md) | linear/cosine、可视化 SNR。 |
| 24 | [U-Net、时间嵌入与 skip connection 各承担什么角色？](./24.md) | 多尺度去噪与 condition 注入。 |
| 25 | [DDIM 为何可以更少步采样，它改变了什么随机性/质量权衡？](./25.md) | 快速采样不等于无损等价。 |
| 26 | [classifier-free guidance 的原理和过强 guidance 的副作用是什么？](./26.md) | 条件/无条件、饱和与多样性下降。 |
| 27 | [如何排查训练损失下降但采样全是噪声？](./27.md) | normalization、timestep、schedule、EMA、采样公式。 |
| 28 | [简化 DALL·E 的 VQ-VAE 与 Transformer 之间，训练数据和 token contract 如何定义？](./28.md) | 图像 token 序、文本 token、mask、codebook version。 |
| 29 | [长时间生成训练如何做 mixed precision、gradient accumulation、EMA 与 checkpoint 恢复？](./29.md) | 显存、数值溢出、断点一致性。 |
| 30 | [如果要把仓库从“学习代码”升级为可信复现，你会优先补哪些测试和实验报告？](./30.md) | 基线表、配置、环境、指标置信区间和失败案例。 |

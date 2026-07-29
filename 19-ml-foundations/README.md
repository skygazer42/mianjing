# 主流机器学习与深度学习面试题：一题一本 Notebook

这一组聚焦算法工程师、机器学习工程师和大模型工程师都会遇到的基础追问。每本 Notebook 首屏直接给结论，再从数学合同、NumPy/PyTorch 底层实现、失败反例、数值稳定性、评估方式、训练状态与部署边界逐层展开。代码不依赖一站式训练、生成、量化或评估框架，方便在面试中把“为什么这样做”讲清楚。

本目录采用独立编号，Notebook 文件名从 `01` 连续排列；全库总序只在工程实践总索引中保留。

| 目录编号 | 面试问题 | Notebook 回答 |
| --- | --- | --- |
| 01 | 数据集应该怎样切分，如何系统发现 Data Leakage？ | [group/time split、embargo、指纹去重、train-only fit 与特征时点审计](./01-dataset-splitting-data-leakage-from-scratch.ipynb) |
| 02 | 类别极不平衡时，采样、加权、Focal Loss 与阈值怎样取舍？ | [稳定加权 BCE、Focal、加权采样、成本阈值与分组验收](./02-class-imbalance-focal-loss-threshold-from-scratch.ipynb) |
| 03 | ROC-AUC、PR-AUC、Precision、Recall 与业务阈值应该怎样选择？ | [并列分数、手写 ROC/PR/AP、成本约束、测试冻结与 bootstrap](./03-roc-pr-auc-threshold-metrics-from-scratch.ipynb) |
| 04 | 怎样数值稳定地实现 Softmax 与 Cross Entropy？ | [log-sum-exp、解析/数值梯度、mask、label smoothing 与 FP16 边界](./04-softmax-cross-entropy-numerical-stability-from-scratch.ipynb) |
| 05 | BatchNorm、LayerNorm 与 RMSNorm 有什么区别，怎样手写？ | [归一化轴、running stats、train/eval、残差块与混合精度](./05-batchnorm-layernorm-rmsnorm-from-scratch-pytorch.ipynb) |
| 06 | 梯度消失和爆炸怎样定位与治理？ | [深链式梯度、激活函数、Xavier/He、残差、global clip 与更新比](./06-vanishing-exploding-gradients-diagnosis-from-scratch-pytorch.ipynb) |
| 07 | 不用 `torch.optim`，怎样实现 SGD、Momentum、Adam 与 AdamW？ | [偏差修正、解耦衰减、参数组、公平收敛实验与状态恢复](./07-sgd-momentum-adam-adamw-from-scratch.ipynb) |
| 08 | 梯度累积、AMP Loss Scaling 与梯度裁剪应该怎样正确组合？ | [尾批加权、同步边界、动态 scale、原子 overflow skip 与 global norm](./08-gradient-accumulation-amp-loss-scaling-clipping-from-scratch.ipynb) |
| 09 | 怎样从零实现 Greedy、Beam Search、Top-k 与 Top-p 解码？ | [稳定 logprob、temperature、长度惩罚、采样、重复约束与停止原因](./09-greedy-beam-topk-topp-decoding-from-scratch.ipynb) |
| 10 | 知识蒸馏怎样设计，Temperature、KL 与 `T²` 分别做什么？ | [硬软目标、teacher eval、feature adapter、token mask、cache 与训练验收](./10-knowledge-distillation-from-scratch-pytorch.ipynb) |
| 11 | INT8 量化怎样从零实现，PTQ 与 QAT 如何取舍？ | [对称/affine、per-channel、int32 GEMM、校准、STE 与敏感层回退](./11-int8-ptq-qat-quantization-from-scratch.ipynb) |
| 12 | 怎样保证训练可复现，并做到断点续训结果一致？ | [多 RNG、sampler cursor、完整状态、Dropout 逐位验证与原子 checkpoint](./12-reproducible-training-checkpoint-resume-from-scratch.ipynb) |

建议顺序是 `01–03` 先建立数据与评估边界，`04–08` 理解训练数值和状态，`09–11` 进入生成、压缩与部署，最后用 `12` 把所有随机性和训练状态串成可恢复系统。固定 seed 的受控数据只用于验证机制；真实项目还需在目标数据、硬件和 SLO 下重新评估。

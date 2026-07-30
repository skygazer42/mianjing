# LLM Core 面试题（01–30）

本目录是一题一答的中文面试材料。每题均配套独立 Notebook：真实语义样本、基线、手写机制、中间量、失败修复和最后的少量回归断言。所有 Notebook 已保存输出，且每个有效代码行均附中文同行注释。

## 题目目录

01. [01. Muon 和 MuonClip 如何改变隐藏层矩阵更新？](./01.Muon和MuonClip如何改变隐藏层矩阵更新.md)（[Notebook](./01-muon.ipynb)）
02. [02. μP 为什么能让不同宽度的超参数更可迁移？](./02.μP为什么能让不同宽度的超参数更可迁移.md)（[Notebook](./02-mup.ipynb)）
03. [03. 什么是 Gradient Noise Scale，如何用它指导 batch size？](./03.什么是GradientNoiseScale如何用它指导batchsize.md)（[Notebook](./03-gradient-noise-scale.ipynb)）
04. [04. Critical Batch Size 应该怎样测量和使用？](./04.CriticalBatchSize应该怎样测量和使用.md)（[Notebook](./04-critical-batch.ipynb)）
05. [05. LLM 训练出现 Loss Spike，如何诊断与恢复？](./05.LLM训练出现LossSpike如何诊断与恢复.md)（[Notebook](./05-loss-spike.ipynb)）
06. [06. Pre-LN 与 Post-LN Transformer 有什么训练差异？](./06.Pre-LN与Post-LNTransformer有什么训练差异.md)（[Notebook](./06-pre-ln-post-ln.ipynb)）
07. [07. 深层 Transformer 为什么需要残差缩放和初始化策略？](./07.深层Transformer为什么需要残差缩放和初始化策略.md)（[Notebook](./07-residual-scaling.ipynb)）
08. [08. RMSNorm 是什么，为什么 LLM 常用它？](./08.RMSNorm是什么为什么LLM常用它.md)（[Notebook](./08-rmsnorm.ipynb)）
09. [09. SwiGLU 如何实现，和 ReLU FFN 有何取舍？](./09.SwiGLU如何实现和ReLUFFN有何取舍.md)（[Notebook](./09-swiglu.ipynb)）
10. [10. 学习率 Warmup、稳定段和衰减应怎样设计？](./10.学习率Warmup、稳定段和衰减应怎样设计.md)（[Notebook](./10-lr-schedule.ipynb)）
11. [11. 为什么语言模型 loss 要按有效 token 归一化？](./11.为什么语言模型loss要按有效token归一化.md)（[Notebook](./11-token-normalized-loss.ipynb)）
12. [12. 动态 batch 如何按 token budget 设计？](./12.动态batch如何按tokenbudget设计.md)（[Notebook](./12-dynamic-batch.ipynb)）
13. [13. 全局梯度裁剪和自适应梯度裁剪如何取舍？](./13.全局梯度裁剪和自适应梯度裁剪如何取舍.md)（[Notebook](./13-gradient-clipping.ipynb)）
14. [14. 为什么优化器要使用参数组学习率？](./14.为什么优化器要使用参数组学习率.md)（[Notebook](./14-parameter-groups.ipynb)）
15. [15. Weight Decay 为什么通常排除 bias 和 norm？](./15.WeightDecay为什么通常排除bias和norm.md)（[Notebook](./15-weight-decay-exclusions.ipynb)）
16. [16. z-loss 解决什么问题，如何实现？](./16.z-loss解决什么问题如何实现.md)（[Notebook](./16-z-loss.ipynb)）
17. [17. Embedding 与输出层权重绑定如何实现？](./17.Embedding与输出层权重绑定如何实现.md)（[Notebook](./17-weight-tying.ipynb)）
18. [18. Sequence Packing 如何减少 padding，又如何保持样本独立？](./18.SequencePacking如何减少padding又如何保持样本独立.md)（[Notebook](./18-sequence-packing.ipynb)）
19. [19. 文档边界 mask 如何防止 packed sequence 信息泄漏？](./19.文档边界mask如何防止packedsequence信息泄漏.md)（[Notebook](./19-document-boundary-mask.ipynb)）
20. [20. Activation Checkpoint 重计算如何在显存与算力间权衡？](./20.ActivationCheckpoint重计算如何在显存与算力间权衡.md)（[Notebook](./20-activation-checkpointing.ipynb)）
21. [21. Delta Attention 如何用增量写入替代直接累加记忆？](./21.DeltaAttention如何用增量写入替代直接累加记忆.md)（[Notebook](./21-delta-attention.ipynb)）
22. [22. 固定状态记忆与 KV Cache 应如何比较？](./22.固定状态记忆与KVCache应如何比较.md)（[Notebook](./22-fixed-state-vs-kv-cache.ipynb)）
23. [23. 线性注意力如何用 recurrent state 流式计算？](./23.线性注意力如何用recurrentstate流式计算.md)（[Notebook](./23-linear-attention-state.ipynb)）
24. [24. Hybrid Attention 应如何选择全注意力与线性层？](./24.HybridAttention应如何选择全注意力与线性层.md)（[Notebook](./24-hybrid-attention.ipynb)）
25. [25. GSPO 为什么使用序列级 ratio，如何手写它？](./25.GSPO为什么使用序列级ratio如何手写它.md)（[Notebook](./25-gspo-sequence-ratio.ipynb)）
26. [26. GRPO 的 token ratio 为什么会产生长度偏差？](./26.GRPO的tokenratio为什么会产生长度偏差.md)（[Notebook](./26-grpo-token-ratio.ipynb)）
27. [27. RLOO baseline 如何降低 REINFORCE 方差？](./27.RLOObaseline如何降低REINFORCE方差.md)（[Notebook](./27-rloo-baseline.ipynb)）
28. [28. Reference-Free Preference Optimization 如何避免参考模型？](./28.Reference-FreePreferenceOptimization如何避免参考模型.md)（[Notebook](./28-reference-free-preference.ipynb)）
29. [29. 如何检测并阻断 Reward Hacking？](./29.如何检测并阻断RewardHacking.md)（[Notebook](./29-reward-hacking.ipynb)）
30. [30. 后训练如何用 KL 控制和发布回滚防止策略漂移？](./30.后训练如何用KL控制和发布回滚防止策略漂移.md)（[Notebook](./30-kl-control-rollback.ipynb)）

## 学习建议

先读 Markdown 的结论和追问，再打开同题 Notebook 观察真实输入、基线和失败案例。小数据的目的只是把机制拆开，不应被解读为生产收益。

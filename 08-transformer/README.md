# Transformer 高频面试题（30 题）

Transformer 用注意力完成 token 间的信息交换，用前馈网络完成逐 token 的非线性变换，再借助残差连接与归一化稳定深层训练。本目录聚焦架构、训练与推理算子；位置旋转细节见 `09-rope`，缓存与服务调度见 `10-kv-cache`。

## 基础与架构（01-10）

1. [Transformer 为什么能取代 RNN 成为大模型主流架构？](./01.Transformer为什么能取代RNN成为大模型主流架构.md)
2. [一个 Transformer block 的完整数据流是什么？](./02.一个Transformer-block的完整数据流是什么.md)
3. [Scaled Dot-Product Attention 中 Q、K、V 分别是什么？](./03.Scaled-Dot-Product-Attention中QKV分别是什么.md)
4. [多头注意力相比单头注意力真正多了什么？](./04.多头注意力相比单头注意力真正多了什么.md)
5. [Encoder-only、Decoder-only 和 Encoder-Decoder 如何区分？](./05.Encoder-only、Decoder-only和Encoder-Decoder如何区分.md)
6. [causal mask 与 padding mask 有什么区别？](./06.causal-mask与padding-mask有什么区别.md)
7. [残差连接为什么能让 Transformer 训练得更深？](./07.残差连接为什么能让Transformer训练得更深.md)
8. [LayerNorm 与 RMSNorm 的原理和取舍是什么？](./08.LayerNorm与RMSNorm的原理和取舍是什么.md)
9. [Pre-Norm 与 Post-Norm 有什么区别？](./09.Pre-Norm与Post-Norm有什么区别.md)
10. [FFN 在 Transformer 中承担什么作用？](./10.FFN在Transformer中承担什么作用.md)

## 训练与原理（11-20）

11. [GELU、ReLU 与 SwiGLU 为什么会影响 FFN？](./11.GELU、ReLU与SwiGLU为什么会影响FFN.md)
12. [Transformer 为什么必须显式注入位置信息？](./12.Transformer为什么必须显式注入位置信息.md)
13. [因果语言建模、掩码语言建模和 Seq2Seq 目标有何不同？](./13.因果语言建模、掩码语言建模和Seq2Seq目标有何不同.md)
14. [teacher forcing 与标签右移是怎么回事？](./14.teacher-forcing与标签右移是怎么回事.md)
15. [交叉熵与困惑度怎样衡量语言模型？](./15.交叉熵与困惑度怎样衡量语言模型.md)
16. [如何估算 Transformer 的参数量与训练 FLOPs？](./16.如何估算Transformer的参数量与训练FLOPs.md)
17. [加深、加宽、增加头数分别会带来什么？](./17.加深、加宽、增加头数分别会带来什么.md)
18. [深层 Transformer 的初始化与残差缩放为什么重要？](./18.深层Transformer的初始化与残差缩放为什么重要.md)
19. [Attention mask 与 softmax 有哪些数值稳定性陷阱？](./19.Attention-mask与softmax有哪些数值稳定性陷阱.md)
20. [Dropout、权重衰减和正则化在大模型训练中如何使用？](./20.Dropout、权重衰减和正则化在大模型训练中如何使用.md)

## 工程与推理（21-30）

21. [Transformer 的训练、prefill 与 decode 计算形态为何不同？](./21.Transformer的训练、prefill与decode计算形态为何不同.md)
22. [FlashAttention 为什么更快且结果仍是精确注意力？](./22.FlashAttention为什么更快且结果仍是精确注意力.md)
23. [数据、张量、流水线与序列并行如何组合？](./23.数据、张量、流水线与序列并行如何组合.md)
24. [混合精度训练为何会溢出或下溢？](./24.混合精度训练为何会溢出或下溢.md)
25. [MoE Transformer 如何以较低计算量扩大参数规模？](./25.MoE-Transformer如何以较低计算量扩大参数规模.md)
26. [Encoder-Decoder 中 cross-attention 如何工作？](./26.Encoder-Decoder中cross-attention如何工作.md)
27. [为什么 decoder-only 模型适合统一多种生成任务？](./27.为什么decoder-only模型适合统一多种生成任务.md)
28. [Attention 的二次复杂度有哪些常见优化路线？](./28.Attention的二次复杂度有哪些常见优化路线.md)
29. [如何定位 Transformer 实现中的 loss 不降与 NaN？](./29.如何定位Transformer实现中的loss不降与NaN.md)
30. [从零实现 Transformer 时应做哪些正确性测试？](./30.从零实现Transformer时应做哪些正确性测试.md)

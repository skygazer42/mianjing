# Self-Attention 高频面试题

Self-attention 让每个 token 按内容相关性聚合序列信息。题库覆盖 Q/K/V 数学、mask 与反传，多头及 MQA/GQA 变体，以及 FlashAttention、分布式、量化与性能诊断。

## 基础概念（01-10）

1. [Q、K、V 分别是什么，为什么不能只用一份表示？](./01.Q-K-V分别是什么为什么不能只用一份表示.md)
2. [Scaled dot-product attention 的完整公式和张量形状是什么？](./02.Scaled-dot-product-attention的完整公式和张量形状是什么.md)
3. [Attention score 为什么要除以 \(\sqrt{d_k}\)？](./03.Attention-score为什么要除以根号d_k.md)
4. [Softmax 在 attention 中做了什么，权重一定代表重要性吗？](./04.Softmax在attention中做了什么权重一定代表重要性吗.md)
5. [Self-attention 与 cross-attention 有什么区别？](./05.Self-attention与cross-attention有什么区别.md)
6. [Causal mask 如何阻止看到未来 token？](./06.Causal-mask如何阻止看到未来token.md)
7. [Padding mask、causal mask 和 segment mask 如何组合？](./07.Padding-mask-causal-mask和segment-mask如何组合.md)
8. [Multi-head attention 为什么比单头更有表达力？](./08.Multi-head-attention为什么比单头更有表达力.md)
9. [多头注意力的投影矩阵形状、参数量和输出如何计算？](./09.多头注意力的投影矩阵形状参数量和输出如何计算.md)
10. [Self-attention 为什么是 \(O(n^2)\)，时间和显存分别花在哪里？](./10.Self-attention为什么是O-n2时间和显存分别花在哪里.md)

## 原理与变体（11-20）

11. [Self-attention 反向传播时梯度如何经过 softmax、Q、K、V？](./11.Self-attention反向传播时梯度如何经过softmax-Q-K-V.md)
12. [为什么不能把 attention 权重直接当作模型解释？](./12.为什么不能把attention权重直接当作模型解释.md)
13. [MHA、MQA 和 GQA 的结构及取舍是什么？](./13.MHA-MQA和GQA的结构及取舍是什么.md)
14. [GQA 的分组映射、参数量和质量折中如何计算？](./14.GQA的分组映射参数量和质量折中如何计算.md)
15. [布尔 mask 与加性 mask 如何实现，常见错误有哪些？](./15.布尔mask与加性mask如何实现常见错误有哪些.md)
16. [Attention 的 softmax 如何保证数值稳定？](./16.Attention的softmax如何保证数值稳定.md)
17. [Attention dropout 应加在哪里，训练和推理有何不同？](./17.Attention-dropout应加在哪里训练和推理有何不同.md)
18. [Prefill 和逐 token 解码时 attention 的计算形状有何不同？](./18.Prefill和逐token解码时attention的计算形状有何不同.md)
19. [FlashAttention 的核心原理是什么，为什么更快更省显存？](./19.FlashAttention的核心原理是什么为什么更快更省显存.md)
20. [FlashAttention 会不会改变 attention 结果和复杂度？](./20.FlashAttention会不会改变attention结果和复杂度.md)

## 工程与评估（21-30）

21. [稀疏、局部和线性 attention 各自怎样降低长序列成本？](./21.稀疏局部和线性attention各自怎样降低长序列成本.md)
22. [如何估算 attention 的峰值显存并选择分块策略？](./22.如何估算attention的峰值显存并选择分块策略.md)
23. [什么是 attention sink，长上下文中为何会出现注意力退化？](./23.什么是attention-sink长上下文中为何会出现注意力退化.md)
24. [位置编码如何与 attention score 交互？](./24.位置编码如何与attention-score交互.md)
25. [融合 QKV、张量布局和 kernel 选择为什么影响性能？](./25.融合QKV张量布局和kernel选择为什么影响性能.md)
26. [Attention 在 tensor parallel 和 sequence parallel 中如何通信？](./26.Attention在tensor-parallel和sequence-parallel中如何通信.md)
27. [量化 Q/K/V 和 attention 中间值有哪些风险？](./27.量化Q-K-V和attention中间值有哪些风险.md)
28. [如何排查 attention 的 NaN、mask 泄漏、形状和头映射错误？](./28.如何排查attention的NaN-mask泄漏形状和头映射错误.md)
29. [如何正确评测和 profile 一个 attention 实现？](./29.如何正确评测和profile一个attention实现.md)
30. [如何在 MHA、GQA、MQA、Flash 与局部 attention 之间选型？](./30.如何在MHA-GQA-MQA-Flash与局部attention之间选型.md)

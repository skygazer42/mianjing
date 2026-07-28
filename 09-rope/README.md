# RoPE 高频面试题（30 题）

RoPE（Rotary Position Embedding）以位置相关的正交旋转作用于 Query 与 Key，使注意力点积自然包含相对位移。本目录聚焦数学性质、实现正确性、长上下文扩展与替代位置机制。

## 基础与数学（01-10）

1. [RoPE 是什么，与绝对位置编码有何核心区别？](./01.RoPE是什么与绝对位置编码有何核心区别.md)
2. [RoPE 的二维旋转公式如何推导？](./02.RoPE的二维旋转公式如何推导.md)
3. [为什么 RoPE 的注意力点积只依赖相对位置？](./03.为什么RoPE的注意力点积只依赖相对位置.md)
4. [RoPE 的频率、base 与维度配对分别表示什么？](./04.RoPE的频率、base与维度配对分别表示什么.md)
5. [为什么 RoPE 通常只旋转 Q 和 K 而不旋转 V？](./05.为什么RoPE通常只旋转Q和K而不旋转V.md)
6. [interleaved 与 split-half 两种 RoPE 实现有何区别？](./06.interleaved与split-half两种RoPE实现有何区别.md)
7. [RoPE 的 cos、sin 缓存与 position offset 如何处理？](./07.RoPE的cos、sin缓存与position-offset如何处理.md)
8. [RoPE 为什么保持向量范数，却仍能改变注意力？](./08.RoPE为什么保持向量范数却仍能改变注意力.md)
9. [RoPE 为什么特别适合 decoder-only 模型？](./09.RoPE为什么特别适合decoder-only模型.md)
10. [rotary dimension 与 head dimension 应如何设置？](./10.rotary-dimension与head-dimension应如何设置.md)

## 长上下文原理（11-20）

11. [RoPE 在训练长度之外为什么会外推失效？](./11.RoPE在训练长度之外为什么会外推失效.md)
12. [训练上下文长度与可推理长度是什么关系？](./12.训练上下文长度与可推理长度是什么关系.md)
13. [Position Interpolation 如何扩展 RoPE 上下文？](./13.Position-Interpolation如何扩展RoPE上下文.md)
14. [NTK-aware RoPE scaling 的直觉与公式是什么？](./14.NTK-aware-RoPE-scaling的直觉与公式是什么.md)
15. [Dynamic NTK scaling 为什么要随序列长度变化？](./15.Dynamic-NTK-scaling为什么要随序列长度变化.md)
16. [YaRN 如何组合频率缩放与注意力温度？](./16.YaRN如何组合频率缩放与注意力温度.md)
17. [LongRoPE 的非均匀插值解决了什么问题？](./17.LongRoPE的非均匀插值解决了什么问题.md)
18. [Llama 3 风格的分频段 RoPE scaling 如何理解？](./18.Llama3风格的分频段RoPE-scaling如何理解.md)
19. [增大 RoPE theta/base 会发生什么？](./19.增大RoPE-theta或base会发生什么.md)
20. [只对部分 head 维度应用 RoPE 有什么取舍？](./20.只对部分head维度应用RoPE有什么取舍.md)

## 实现与选型（21-30）

21. [RoPE 在 BF16、FP16 下有哪些精度陷阱？](./21.RoPE在BF16、FP16下有哪些精度陷阱.md)
22. [RoPE 如何兼容 MHA、MQA 与 GQA？](./22.RoPE如何兼容MHA、MQA与GQA.md)
23. [使用 KV Cache 时 RoPE 应在何时、按什么位置应用？](./23.使用KV-Cache时RoPE应在何时按什么位置应用.md)
24. [左 padding 与变长 batch 的 position id 如何构造？](./24.左padding与变长batch的position-id如何构造.md)
25. [序列 packing 时 RoPE 位置应连续还是重置？](./25.序列packing时RoPE位置应连续还是重置.md)
26. [RoPE 如何扩展到二维图像与多模态位置？](./26.RoPE如何扩展到二维图像与多模态位置.md)
27. [RoPE 与 ALiBi 应如何比较和选择？](./27.RoPE与ALiBi应如何比较和选择.md)
28. [RoPE 与绝对位置 embedding、相对位置 bias 有何区别？](./28.RoPE与绝对位置embedding、相对位置bias有何区别.md)
29. [如何为 RoPE 实现设计正确性测试？](./29.如何为RoPE实现设计正确性测试.md)
30. [长上下文 RoPE scaling 应如何评估与选型？](./30.长上下文RoPE-scaling应如何评估与选型.md)

# MoE 高频面试题（30 题）

## 一句话定位

MoE（Mixture of Experts）用可学习路由为每个 token 只激活少数专家，以稀疏计算换取更大的总参数容量；它节省的是单 token 激活计算，不会自动解决显存、负载均衡和跨卡通信问题。

## 基础概念与路由（01–10）

1. [MoE 和 Dense 模型有什么区别？](./01.MoE和Dense模型有什么区别.md)
2. [MoE 为什么参数很多，但计算量不会同比例增加？](./02.MoE为什么参数多但计算量不同比例增加.md)
3. [router / gate 如何计算 token 到 expert 的分配？](./03.router和gate如何计算token到expert的分配.md)
4. [top-1 和 top-2 routing 有什么区别？](./04.top-1和top-2-routing有什么区别.md)
5. [MoE 为什么通常替换 Transformer 中的 FFN？](./05.MoE通常为什么替换Transformer中的FFN.md)
6. [expert 真的会自动学出不同专业吗？](./06.expert真的会自动学出不同专业吗.md)
7. [token-level 和 sequence-level routing 有什么区别？](./07.token-level和sequence-level-routing有什么区别.md)
8. [shared expert 和 routed expert 分别做什么？](./08.shared-expert和routed-expert分别做什么.md)
9. [capacity factor 是什么，如何影响专家容量？](./09.capacity-factor是什么如何影响容量.md)
10. [token dropping 和 padding 分别如何处理专家过载？](./10.token-dropping和padding分别如何处理专家过载.md)

## 训练、稳定性与并行（11–20）

11. [load balancing loss 如何设计？](./11.load-balancing-loss如何设计.md)
12. [router z-loss 解决什么稳定性问题？](./12.router-z-loss解决什么稳定性问题.md)
13. [expert collapse 是什么，如何诊断和缓解？](./13.expert-collapse是什么如何诊断缓解.md)
14. [无辅助损失负载均衡如何工作？](./14.无辅助损失负载均衡如何工作.md)
15. [router noise 和 jitter 有什么作用？](./15.router-noise和jitter有什么作用.md)
16. [top-k 离散选择如何反向传播？](./16.top-k离散选择如何反向传播.md)
17. [如何从 Dense 模型 upcycle 成 MoE？](./17.如何从Dense模型upcycle成MoE.md)
18. [expert parallel 与 data、tensor、pipeline parallel 有什么区别？](./18.expert-parallel和data-tensor-pipeline-parallel有什么区别.md)
19. [all-to-all 通信为什么是 MoE 的瓶颈？](./19.all-to-all通信为什么是MoE瓶颈.md)
20. [MoE 微调为什么容易出现路由漂移或专家失衡？](./20.MoE微调为什么容易路由漂移或专家失衡.md)

## 推理、部署与系统设计（21–30）

21. [MoE 推理一定比相同 FLOPs 的 Dense 模型快吗？](./21.MoE推理一定比同FLOPs的Dense模型快吗.md)
22. [batch 和并发如何影响专家负载与尾延迟？](./22.batch和并发如何影响专家负载与延迟.md)
23. [专家放置、复制和动态路由如何优化？](./23.专家放置复制和动态路由如何优化.md)
24. [MoE 量化有哪些特殊难点？](./24.MoE量化有哪些特殊难点.md)
25. [MoE 的参数、激活与通信显存如何估算？](./25.MoE显存占用如何估算.md)
26. [dropless MoE 和容量受限 MoE 如何选择？](./26.dropless-MoE和容量受限MoE如何选择.md)
27. [expert-choice routing 和 token-choice routing 有什么区别？](./27.expert-choice-routing和token-choice-routing有什么区别.md)
28. [如何监控和排查 MoE 训练故障？](./28.如何监控和排查MoE训练故障.md)
29. [MoE 部署为什么依赖集群拓扑和通信带宽？](./29.MoE部署为什么依赖集群拓扑和通信带宽.md)
30. [什么场景应该选择 MoE，而不是 Dense 模型？](./30.什么场景应该选择MoE而不是Dense模型.md)

## 推荐复习方式

先能手写单个 MoE 层的 dispatch—expert—combine 流程，再推导每个 token 的激活参数与专家容量，最后从 all-to-all、负载长尾和显存放置解释“理论 FLOPs 不等于真实延迟”。

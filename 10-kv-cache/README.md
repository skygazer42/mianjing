# KV Cache 高频面试题（30 题）

KV Cache 是自回归推理的核心状态：保存历史 token 在各层产生的 Key 与 Value，让新 token 无需重复投影整段前缀。本目录聚焦形状与显存、prefill/decode、缓存组织以及多请求服务。

## 基础概念（01-10）

1. [KV Cache 是什么，缓存了哪些张量？](./01.KV-Cache是什么缓存了哪些张量.md)
2. [KV Cache 为什么能加速自回归解码？](./02.KV-Cache为什么能加速自回归解码.md)
3. [prefill 与 decode 阶段的 KV Cache 行为有何不同？](./03.prefill与decode阶段的KV-Cache行为有何不同.md)
4. [KV Cache 的常见张量形状与布局是什么？](./04.KV-Cache的常见张量形状与布局是什么.md)
5. [如何推导 KV Cache 的显存占用公式？](./05.如何推导KV-Cache的显存占用公式.md)
6. [哪些模型与请求参数决定 KV Cache 大小？](./06.哪些模型与请求参数决定KV-Cache大小.md)
7. [增量追加 KV 时如何保证 causal attention 正确？](./07.增量追加KV时如何保证causal-attention正确.md)
8. [MHA、MQA、GQA 对 KV Cache 有什么影响？](./08.MHA、MQA、GQA对KV-Cache有什么影响.md)
9. [为什么缓存 K 和 V，而通常不缓存 Q？](./09.为什么缓存K和V而通常不缓存Q.md)
10. [训练阶段为什么通常不使用 KV Cache？](./10.训练阶段为什么通常不使用KV-Cache.md)

## 缓存原理与优化（11-20）

11. [连续预分配 KV Cache 为什么会浪费和碎片化？](./11.连续预分配KV-Cache为什么会浪费和碎片化.md)
12. [PagedAttention 解决了什么问题？](./12.PagedAttention解决了什么问题.md)
13. [KV block table 与 copy-on-write 如何工作？](./13.KV-block-table与copy-on-write如何工作.md)
14. [continuous batching 如何提升 decode 吞吐？](./14.continuous-batching如何提升decode吞吐.md)
15. [调度器如何做 admission、抢占与容量预测？](./15.调度器如何做admission抢占与容量预测.md)
16. [prefix caching 如何复用公共前缀？](./16.prefix-caching如何复用公共前缀.md)
17. [beam search 如何共享、复制与重排 KV Cache？](./17.beam-search如何共享复制与重排KV-Cache.md)
18. [speculative decoding 如何与 KV Cache 协同？](./18.speculative-decoding如何与KV-Cache协同.md)
19. [KV Cache 量化如何节省显存，代价是什么？](./19.KV-Cache量化如何节省显存代价是什么.md)
20. [KV Cache offload 与分层存储如何设计？](./20.KV-Cache-offload与分层存储如何设计.md)

## 服务工程（21-30）

21. [滑动窗口、淘汰与 StreamingLLM 类策略有何区别？](./21.滑动窗口淘汰与StreamingLLM类策略有何区别.md)
22. [chunked prefill 如何平衡 TTFT 与 decode 延迟？](./22.chunked-prefill如何平衡TTFT与decode延迟.md)
23. [KV Cache 布局如何影响 attention kernel 性能？](./23.KV-Cache布局如何影响attention-kernel性能.md)
24. [张量并行下 KV Cache 如何分片？](./24.张量并行下KV-Cache如何分片.md)
25. [流水线与跨节点推理中 KV Cache 放在哪里？](./25.流水线与跨节点推理中KV-Cache放在哪里.md)
26. [多租户服务如何做 KV Cache 容量与隔离？](./26.多租户服务如何做KV-Cache容量与隔离.md)
27. [TTFT、TPOT、ITL 与吞吐应如何联合分析？](./27.TTFT、TPOT、ITL与吞吐应如何联合分析.md)
28. [如何完成一道 KV Cache 显存估算题？](./28.如何完成一道KV-Cache显存估算题.md)
29. [KV Cache 常见正确性 bug 如何定位？](./29.KV-Cache常见正确性bug如何定位.md)
30. [如何设计一个高并发长上下文 KV Cache 系统？](./30.如何设计一个高并发长上下文KV-Cache系统.md)

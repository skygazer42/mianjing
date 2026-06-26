# MoE

## 一句话定位

MoE（Mixture of Experts）通过稀疏路由让每个 token 只激活少数专家，从而在不线性增加计算量的前提下扩大参数规模。

## 高频面试题

1. MoE 为什么能做到“参数很多，但每次计算不那么多”？
2. router / gate 是怎么工作的？
3. top-1 和 top-2 routing 有什么差别？
4. load balancing loss 是干什么的？
5. MoE 在训练和推理阶段分别有哪些工程难点？

## 原理剖析

- dense FFN 是“所有 token 都走同一套参数”。
- MoE 改成“先让 router 给 token 打分，再把 token 发到少数几个 expert”。
- 所以总参数量可以大，但单次前向实际只用到部分 expert。
- 训练时要避免所有 token 都挤到同一个 expert 上，所以需要负载均衡约束。
- 推理时还要处理跨卡通信、专家并行和延迟抖动问题。

## 极简实现

```python
def route_token(token_score: list[float]) -> int:
    return max(range(len(token_score)), key=lambda i: token_score[i])


def expert_0(x: float) -> float:
    return x + 1


def expert_1(x: float) -> float:
    return x * 2


expert_id = route_token([0.2, 0.8])
result = expert_0(3.0) if expert_id == 0 else expert_1(3.0)
print(expert_id, result)
```

## 继续追问

1. 为什么 MoE 常常“参数翻倍，但 FLOPs 没翻倍”？
2. expert collapse 是什么，怎么缓解？
3. 为什么 MoE 对集群通信拓扑更敏感？

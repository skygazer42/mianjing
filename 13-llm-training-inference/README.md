# 13 · LLM 训练与推理工程

本目录用 PyTorch 基础算子复现参数高效微调、偏好优化与 speculative decoding。三本 Notebook 都从公式和张量形状出发，包含手写 nn.Module/forward、受控训练或精确概率实验、失败 oracle、数据与切分合同，以及带包外信任根的发布加载。

| 编号 | Notebook | 核心问题 |
| --- | --- | --- |
| 55 | [LoRA 与教学版 QLoRA](./55-lora-qlora-from-scratch-pytorch.ipynb) | 低秩增量、冻结 base、merge/unmerge、groupwise int4 frozen base、adapter 梯度和可信保存/加载如何实现？ |
| 56 | [DPO 偏好优化](./56-dpo-preference-optimization-from-scratch-pytorch.ipynb) | masked sequence log-prob、policy/reference log-ratio、β、label smoothing、pair 泄漏与数值稳定性怎样验证？ |
| 57 | [Speculative Decoding](./57-speculative-decoding-from-scratch-pytorch.ipynb) | draft propose、target verify、拒绝残差、bonus token、EOS、随机数与请求级 cache rollback 如何保持 target 分布？ |

## 运行

- Python 3.10+、PyTorch 2.x；CPU、离线、单线程，不下载数据或模型。
- 从仓库根目录启动 Jupyter，按 55 → 56 → 57 顺序学习；每本也能从空内核独立运行。
- 未使用 transformers、peft、bitsandbytes、TRL、vLLM 或现成网络架构。

## 结果边界

受控闭集只用于验证公式、梯度、mask、概率和发布合同，不能外推为真实 LLM 的泛化、对齐或吞吐结果。55 的 4-bit 层是对称均匀 groupwise 教学实现，不是 NF4、double quantization 或 packed kernel；57 逐 token 调 target 用于审计分布，生产实现应对 proposal block 做并行 target 验证并管理分层 KV cache。

每本发布示例都逐项摘要 state 的 key、dtype、shape、bytes，并绑定完整 tokenizer、数据、split 和 recipe。包内自签摘要不作为信任根；加载器只接受包外 MappingProxy registry 中预先登记的整体摘要，并返回封装请求语义的 Published wrapper。

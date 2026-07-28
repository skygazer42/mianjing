# LLM / NLP 面试知识库

这个仓库按技术主题组织大模型与 NLP 高频面试题，既适合快速复习，也可通过 notebook 手算和运行核心算法。

## 12 个专题

1. [Token](./01-token/README.md)：文本单位、词表、成本与 tokenizer 工程（[Notebook](./01-token/token.ipynb)）
2. [BPE](./02-bpe/README.md)：高频 pair 合并、byte-level BPE 与训练实现（[Notebook](./02-bpe/bpe.ipynb)）
3. [WordPiece](./03-wordpiece/README.md)：最长匹配、`[UNK]`、词表训练与部署一致性（[Notebook](./03-wordpiece/wordpiece.ipynb)）
4. [Unigram](./04-unigram/README.md)：概率分词、EM、剪枝与 subword regularization（[Notebook](./04-unigram/unigram.ipynb)）
5. [Embedding](./05-embedding/README.md)：查表、权重共享、对比学习与向量检索（[Notebook](./05-embedding/embedding.ipynb)）
6. [Positional Encoding](./06-positional-encoding/README.md)：绝对/相对位置、偏置与长度外推（[Notebook](./06-positional-encoding/positional-encoding.ipynb)）
7. [Self-Attention](./07-self-attention/README.md)：QKV、mask、MHA/MQA/GQA 与高效实现（[Notebook](./07-self-attention/self-attention.ipynb)）
8. [Transformer](./08-transformer/README.md)：block、归一化、FFN、训练与架构取舍（[Notebook](./08-transformer/transformer.ipynb)）
9. [RoPE](./09-rope/README.md)：旋转位置编码、相对位置性质与长上下文 scaling（[Notebook](./09-rope/rope.ipynb)）
10. [KV Cache](./10-kv-cache/README.md)：prefill/decode、显存估算、分页与服务调度（[Notebook](./10-kv-cache/kv-cache.ipynb)）
11. [MoE](./11-moe/README.md)：稀疏路由、负载均衡、专家并行与部署（[Notebook](./11-moe/moe.ipynb)）
12. [RAG](./12-rag/README.md)：摄取、召回、重排、评估、安全与生产化（[Notebook](./12-rag/rag.ipynb)）

## 每个专题包含什么

- `README.md`：按基础、原理、工程分组的 30 道题目总览，可直接跳到答案。
- `01.*.md`–`30.*.md`：每题一个独立文件；先给结论，再讲机制、公式/例子、工程取舍、误区和延伸追问。
- `*.ipynb`：详细中文教程，包含学习目标、核心推导、最小可运行实现、中间结果、边界案例、练习和面试总结。

个别目录还保留专题研究、图示和补充材料，它们不占 30 道主问题编号。

## 工程实践

[工程实践 Notebooks](./engineering-practice/README.md) 专门回答“系统怎么实现和验证”，现有 138 份中文实验：前 18 份覆盖 tokenizer/检索/RAG、NLP 数据与实体链接、CV/OCR、图算法与 GNN、多模态、推荐及时序系统；19–66 用 PyTorch 手写 `class XxxNet(nn.Module)` 与 `forward`，复现 NLP、LLM 训练推理、2D/3D 视觉、图表示与等变网络、推荐、时序、生成、语音和强化学习架构；67–138 则把开放式系统设计、主流 ML/DL、生成式 AI、Agent Loop、LLM 系统与推理面试题拆成一题一本，从底层公式和状态机实现到评测、安全、部署与失败处理。

第 55–66 份按方向放在根目录的 [LLM 训练与推理](./13-llm-training-inference/README.md)、[进阶视觉与 3D](./14-advanced-vision-3d/README.md)、[图表示与科学学习](./15-graph-representation-science/README.md) 和 [控制、时序与离散生成](./16-control-timeseries-generative/README.md) 中；第 67–78 份位于 [面试系统题底层实现](./17-interview-systems-from-scratch/README.md)，第 79–90 份位于 [机器学习系统面试题](./18-ml-system-interview-questions/README.md)，第 91–102 份位于 [主流机器学习与深度学习面试题](./19-mainstream-ml-dl-interview-questions/README.md)，第 103–114 份位于 [生成式 AI 与 Agent 高频面试题](./20-genai-agent-interview-questions/README.md)，第 115–126 份位于 [Agent Loop 深入面试题](./21-agent-loop-interview-questions/README.md)，第 127–138 份位于 [LLM 系统与推理面试题](./22-llm-systems-reasoning-interview-questions/README.md)，主索引仍由工程实践 README 统一维护。

## 推荐学习顺序

1. tokenizer 主线：`token -> BPE -> WordPiece -> Unigram`
2. 表示学习：`Embedding -> Positional Encoding`
3. 模型结构：`Self-Attention -> Transformer -> RoPE`
4. 推理与系统：`KV Cache -> MoE -> RAG`

第一遍只看每题的结论和面试要点；第二遍手推公式、运行 notebook；第三遍从工程指标、失败模式和方案取舍组织完整回答。不要只背定义：面试追问通常会落到张量形状、复杂度、数值稳定性、容量估算和线上诊断。

## 内容约定

- 公式说明变量与适用假设，不把近似复杂度当精确性能。
- 教学代码优先展示核心机制，并明确与生产实现的差距。
- 涉及模型版本或具体实现时，以对应 checkpoint、官方配置或原始论文为准。
- tokenizer、模型权重、chat template、索引和服务配置都应视为有版本的接口契约。

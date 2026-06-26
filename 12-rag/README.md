# RAG

## 一句话定位

RAG（Retrieval-Augmented Generation）把外部检索和生成模型结合起来，让模型回答时不只依赖参数记忆。

## 高频面试题

1. RAG 主要解决的是什么问题？
2. RAG 和微调分别适合解决什么问题？
3. chunk size、overlap、top-k 为什么会影响效果？
4. 向量检索和关键词检索怎么选？
5. RAG 为什么仍然可能幻觉？

## 原理剖析

- 用户先发出 query。
- 系统把 query 编码成检索向量，去知识库里找最相关的若干文档片段。
- 再把这些片段连同问题一起拼进 prompt，交给大模型生成答案。
- 所以 RAG 的质量不只取决于模型，还取决于切块、召回、重排和 prompt 组织。
- 检索错了、切块不对、上下文污染，都会让答案失真。

## 极简实现

```python
def overlap_score(query: str, doc: str) -> int:
    q_words = set(query.lower().split())
    d_words = set(doc.lower().split())
    return len(q_words & d_words)


docs = [
    "tokenization splits text into subwords",
    "rag combines retrieval with generation",
    "kv cache speeds up decoding",
]

query = "how does rag work"
ranked = sorted(docs, key=lambda doc: overlap_score(query, doc), reverse=True)
print(ranked[:2])
```

## 继续追问

1. RAG 为什么经常要配 reranker？
2. 什么时候该优先改检索，而不是改大模型？
3. 企业知识库场景里，RAG 的评估指标通常看什么？

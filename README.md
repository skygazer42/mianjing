# mianjing

面向 LLM / NLP 面试准备的仓库。

设计目标很直接：

- 每个技术一个文件夹，避免内容搅在一起
- 每个文件夹都包含 5 个固定部分：一句话定位、高频面试题、原理剖析、极简实现、继续追问
- 先用能快速复习的骨架搭起来，后续再逐个主题深挖

## 目录结构

1. [01-token](./01-token/README.md)
2. [02-bpe](./02-bpe/README.md)
3. [03-wordpiece](./03-wordpiece/README.md)
4. [04-unigram](./04-unigram/README.md)
5. [05-embedding](./05-embedding/README.md)
6. [06-positional-encoding](./06-positional-encoding/README.md)
7. [07-self-attention](./07-self-attention/README.md)
8. [08-transformer](./08-transformer/README.md)
9. [09-rope](./09-rope/README.md)
10. [10-kv-cache](./10-kv-cache/README.md)
11. [11-moe](./11-moe/README.md)
12. [12-rag](./12-rag/README.md)

## 推荐学习顺序

1. 先看 tokenizer 主线：`token -> bpe -> wordpiece -> unigram`
2. 再看表示学习：`embedding -> positional encoding`
3. 再看模型结构：`self-attention -> transformer -> rope`
4. 最后看推理和系统设计：`kv-cache -> moe -> rag`

## 每个主题统一结构

每个目录下的 `README.md` 先保持同一套格式：

1. 一句话定位
2. 高频面试题
3. 原理剖析
4. 极简实现
5. 继续追问

## 后续扩写建议

当某个主题内容变大时，可以把单个 `README.md` 拆成：

- `questions.md`：只放面试题和答题要点
- `notes.md`：只放原理推导
- `demo.py`：只放可运行的极简实现
- `figures/`：只放图和示意图

这样既适合快速背面经，也适合后面沉淀成系统笔记。

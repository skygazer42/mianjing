# Token

## 一句话定位

token 是模型处理文本时的离散基本单位，字符串必须先切成 token，才能再映射成 id 和向量。

## 高频面试题

1. token、word、character 三者分别是什么？
2. 为什么同一句话在不同模型里 token 数可能不同？
3. token 数量为什么会影响训练吞吐、上下文长度和推理成本？
4. token 和 embedding 的关系是什么？
5. 中文、英文、代码的 tokenization 难点分别在哪里？

## 原理剖析

- 模型不能直接吃字符串，必须先把文本切分成更稳定的离散单元。
- token 设计本质是在做折中：词表越大，单个 token 表达越强，但 embedding 矩阵更大。
- token 越细，序列越长，attention 成本越高。
- 同一个词在不同上下文里可以被切成不同 token 组合，这也是不同 tokenizer 表现差异的来源。

## 极简实现

```python
import re

def simple_tokenize(text: str) -> list[str]:
    text = text.lower().strip()
    return re.findall(r"\w+|[^\w\s]", text)


text = "Hello, Token!"
tokens = simple_tokenize(text)
print(tokens)  # ['hello', ',', 'token', '!']
```

这个实现只是演示“先切分，再编码”的基本思路，不等于生产级 tokenizer。

## 继续追问

1. 如果 tokenizer 改了，原来的 embedding 能不能直接复用？
2. 为什么大模型里 token 数往往直接决定 API 价格？
3. 为什么代码模型通常会有更适合代码语料的 tokenizer？

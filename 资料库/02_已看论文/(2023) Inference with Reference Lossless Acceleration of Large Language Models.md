Tags: #Tag_自然语言处理 
# Information
---
Speculative Decoding

# Mainly Idea
---
![[Pasted image 20240610162724.png]]
找一个预言家（速度很快），预测出LLM可能输出的下一词和下下一个词，然后并行通过语言模型进行结果预测，如果预言家很准确，速度一下就增加3倍，如果不准确，只取正确的预测结果。

预言家可以有很多模型担任（譬如，大模型型轻量化的模型，或者所搜引擎）

检索任务可能大模型有一部分span的内容和reference的内容一样，
如果大模型在预测下一个词的时候，我们假设下一个词就是reference里面的下一个词，并行让大模型预测下下一个词，那么如果大模型预测的下一个词就是reference里面的词，则可以直接使用并行预测结果下下一个词。这个可以加速预测过程。

# Question
---


# Reference
---
- [【生成式AI導論 2024】第16講：可以加速所有語言模型生成速度的神奇外掛 — Speculative Decoding (youtube.com)](https://www.youtube.com/watch?v=MAbGgsWKrg8)

# Attachment
---
![[2304.04487v1.pdf]]
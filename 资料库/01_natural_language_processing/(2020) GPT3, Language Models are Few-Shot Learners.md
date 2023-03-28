# Information
---
- OpenAI
- [[(2017) Proximal Policy Optimization Algorithms]]
# Mainly Idea
---


# Reference
---
- 如何训练Few-shot？
	- 训练过程有个2048的长度限制，一条数据，将通过将多条数据合成一起，凑2048的长度，进行训练。
	- 测试过程，可以给与多个few-shot的样例，但是不能超过2048的长度。
- 长文档训练速度问题：使用了[[(2019) Sparse Transformer]]
	- 解决一条数据很长，导致计算量大的问题
	- 更长的也可以考虑[[Sequence Parallelism, Long Sequence Training from System Perspective]]

# Attachment
---
![[gpt1.pdf]]

![[gpt2.pdf]]

![[gpt3.pdf]]
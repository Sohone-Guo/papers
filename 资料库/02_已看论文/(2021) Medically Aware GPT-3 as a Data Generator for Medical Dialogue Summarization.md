Tags: #Tag_自然语言处理 
# Information
---


# Mainly Idea
---
使用GPT3产生训练数据进行模型训练。Medical Summarizer

- GPT3本身是否是好的Medical Summarizer?
	- 本身有问题，Missing info, repeat redundant等
	- 提高GPT3的效果
		- 方法：输出多个结果，在多个结果中选一个最好的（利用NER Coverage）。
	- 最终效果：
		- ![[Pasted image 20230529175956.png]]
- GPT3产生的数据和真实数据，在2个其他pretrain上进行测评，
	- ![[Pasted image 20230529182304.png]]
	- GCF是生成的数据，由210条真实数据生成出来，每条数据对应多个生成的摘要伪标签。
# Reference
---


# Attachment
---
![[2110.07356.pdf]]
# Information
---
- ACL 2021
- #Flow-based
- DiscreteFlow
- FlowSeq

# Mainly Idea
---
##### Non-Autoregressive Language Flow
- Sentence 转化为embedding后，作为一个整体，映射到隐层，再通过可逆函数，映射回embedding, Embedding转化成字词，通过相似度匹配
- 为了减少Sentence长度的影响，框架有多个Block，每个block都会对长度减半。

##### Autoregressive Language Flow
![[Pasted image 20230507225454.png]]

Seq-to-Seq Generation with Flow
- 将输入的句子，通过Flow到隐层空间，将隐层空间的信息，作为Decoder输入的一部分。
- 论文觉得Flow-based提取的Context vector可能比Encoder提取的更准确或者有额外信息。

QA Data Augmentation Results
- 直接使用：QA任务，增广question， 类似paraphrase
	- ![[Pasted image 20230507231109.png]]
	- ![[Pasted image 20230507225715.png]]

# Reference
---
- Time-dimention permutaion
	- permutation: [[(2015) NICE, NON-LINEAR INDEPENDENT COMPONENTS ESTIMATION]] 里面有一个GIT
		- ![[Pasted image 20230507213126.png]]
- Affine coupling with RNN and Transformer
	- ![[Pasted image 20230507212429.png]]
	- Affine: [[(2018) Glow, Generative Flow with Invertible 1x1 Convolutions]]

# Attachment
---
![[2021.acl-long.355.pdf]]
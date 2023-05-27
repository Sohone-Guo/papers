#Tag_基础理论 
# Information
---


# Mainly Idea
---
![[Pasted image 20230516220513.png]]
- w1和wk哪个是$N(0,I)$?
	- w1是
- 结构：
	- z0 = Encoder(x)
	- zk = flow(z0)
	- x = Decoder(zk)
	- loss = KL(z0| N(0, I)) - log(|det()|) + reconstruction
- 预测：
	- z0 = 随机一个
	- zk = flow(z0)
	- x = Decoder(zk)
![[Pasted image 20230516224643.png]]
K是Flow的层数
# Reference
---
- [[(2014) Stochastic Backpropagation and Approximate Inference in Deep Generative Models]] H-VAE参考
- [[(2015) NICE, NON-LINEAR INDEPENDENT COMPONENTS ESTIMATION]]

# Attachment
---
![[Variational inference with normalizing flows.pdf]]
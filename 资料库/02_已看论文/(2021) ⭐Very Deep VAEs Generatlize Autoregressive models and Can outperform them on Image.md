#Tag_基础理论 #Tag_计算机视觉 
# Information
---
- [[Openai]]

# Mainly Idea
---
- 定义：为什么更多层数的 VAE 能超过 AR? 
	- 相比于Autoregressive, 每一个P(下一个像素点 | 当前像素点)， 如果结构型VAE，有多层，假设32x32的图片，每个点从左上到右下，按照前后关系都有一个分布，也可以实现P(下一个像素点 | 当前像素点)，具有结构能力，并且会更好。
	- 当Q(Z|X) = 1 和 P(X|Z)=1，具备唯一确认的值，则相当于Autoregressive.
- 并且通过实验验证了此部分

# Reference
---


# Attachment
---
![[2011.10650.pdf]]
Tags: #Tag_计算机视觉 
# Information
---


# Mainly Idea
---
![[Pasted image 20230619124606.png]]
a) 是传统的，b)是所提方案

- 训练阶段(b) 仅为Generator, 因为GAN还有Discriminator端)
	- $z$: 是随机数值
	- $w$: 是 $z$通过一串的网络获得
	- Const 4x4x512：是一个可学习的固定值。
	- Noise：是random noise


# Question
---
- $y_s和y_b$ 由$w$而来，一半为$s$， 另一半为$b$
- style mixing是先sample两个$z$，中间部分融合获得。

# Reference
---


# Attachment
---
![[styleGAN.pdf]]
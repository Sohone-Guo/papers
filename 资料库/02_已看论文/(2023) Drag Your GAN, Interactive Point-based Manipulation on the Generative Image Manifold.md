Tags: #Tag_计算机视觉 #Tag_多模态 
# Information
---
- [[google]]
- MIT

# Mainly Idea
---
![[Pasted image 20230621111357.png]]
- 在Generator的其中一个隐层上进行操作。
	- 将隐层通过resize的方式，扩充与图片大小一致。
	- for i in range(1000+):
		- 获得红点范围的特征，获得蓝色点范围的特征
		- 获得红色点到蓝色点一小步的特征（F'）
		- 更新参数，使得F'的特征趋近与红色特征
		- 更新红色位置：那红色的特征最近距离搜索，最像的位置为最新位置
	- 直到红色位置和蓝色位置一样为止。

# Question
---
- <font color="#c00000">What is the a feature-based motion supervision?</font>
	- motion supervision: A loss that enforces handle points to move towards target points is used to optimize the latent. ?
		- loss需要训练还是预测的时候使用？预测过程中使用loss进行变化
		- 原理很像，假设鼻子移到嘴巴的位置
			- 找到：特征鼻子，特征嘴巴
			- 传递一个loss, 嘴巴的特征接近鼻子（<font color="#c00000">譬如生成了一句话，其中一个字不喜欢，就监督这一个字趋近指定的字，句子其他部分会自动改变</font>）
- <font color="#c00000">A new point tracking approach?</font>
	- update the positions of the handle points to track the corresponding points on the object.
	- 以：假设鼻子移到嘴巴的位置为例，因为每次一步不是很确定移动的位置，重新定位鼻子的位置的时候
		- 提取鼻子特征
		- 根据移动的范围，譬如鼻子特征，最像的就是新的位置

# Reference
---
- StyleGAN: [[(2019) A Style-Based Generator Architecture for Generative Adversarial Networks]]
- StyleGAN2: [[(2020) Analyzing and Improving the Image Quality of StyleGAN]]

# Attachment
---
![[2305.10973.pdf]]
# Tutorial
---
- Foward differentation model (tangent mode AD)
	- ![[Pasted image 20230524102254.png]]
	- 从前往后计算，先计算$x_1$的Forward Tangent, 再计算$x_2$的Forward Tangent
- Reverse Automatic Differentiation (adjoint mode AD)
	- ![[Pasted image 20230524102408.png]]
	- 从后往前计算，先计算$y_1$的Forward Tangent, 再计算$y_2$的Forward Tangent
- Jacobian矩阵
	- ![[Pasted image 20230524102726.png]]
	- 根据计算的Loss
		- Forward: ![[Pasted image 20230524102809.png]]
		- backward:Vector-Jacobian
	- ![[Pasted image 20230524102939.png]]
	- ![[Pasted image 20230524103234.png]]

# Reference
---
- [【自动微分】系列第三篇！微分的两种模式！前向微分和正向微分！对应反向传播！ - YouTube](https://www.youtube.com/watch?v=QczW36K9A90)
- [(78 封私信 / 84 条消息) 反向传播算法和自动微分反向模式有什么区别？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/320987507/answer/2496838800)
- [Automatic Differentiation: Forward and Reverse (jingnanshi.com)](https://jingnanshi.com/blog/autodiff.html)
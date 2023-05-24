# 2018
---
- [[(2018) Neural Ordinary Differential Equations]]
	- 将Resnet通过ODE从离散转连续，
	- 优点：
		- 过程可逆
		- 数据可连续
	- 问题：
		- 简单梯度：内存占比大，
		- 解决方案:使用Adjoint sensitivity method 通过可逆过程减少内存开销
	- 优化了Normalizing flow的计算复杂度变成Continuous normalizing flows[[Researching on Flow-based]]

# 2021
---
- [[(2021) A Memory efficient and Reverse accurate integrator for neural ODEs]]
	- [[(2018) Neural Ordinary Differential Equations]] 通过Adjoint sensitivity method的可逆过程减少内存开销，但是可逆过程不精确，本论文提高可逆过程精确。
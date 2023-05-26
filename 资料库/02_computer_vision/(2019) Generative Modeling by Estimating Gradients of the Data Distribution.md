# Information
---
- Score function

# Mainly Idea
---
estimating and sampling from the score of the logarithnmic data density, which is the gradient of the log-density function at the input data point.

主要解决这个公式：
![[Pasted image 20230525155000.png]]
有两种方法
- Denoising score matching
	- ![[Pasted image 20230525155111.png]]
- Sliced score matching
	- ![[Pasted image 20230525155124.png]]

# Reference
---
- Langevin dynamics ?
	- for sampling. which approximately works by gradually moving a random initial sample to high density regoins along the vector field of scores.
	- ![[Pasted image 20230525155152.png]]
- Score function ?
	- which is the gradient of the log-density function at the input data point.
	- 怎么获得？
		- 用NN with score matching 学习这个
- Score matching ?
	- [[(2005) Estimation of Non-Normalized Statistical Models by Score Matching]]
- Score estimation
- 与neural ODE的关系？[[(2018) Neural Ordinary Differential Equations]]
	- ODE是考虑时间/层级之间的变化，导致Y的变化
	- Score Function考虑的是真数据假数据之间的变化，

# Attachment
---
![[Generative modeling by estimating gradients of the data distribution.pdf]]
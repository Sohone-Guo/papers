# Information
---
- Score function

# Mainly Idea
---
estimating and sampling from the score of the logarithnmic data density, which is the gradient of the log-density function at the input data point.

# Reference
---
- Langevin dynamics ?
	- for sampling. which approximately works by gradually moving a random initial sample to high density regoins along the vector field of scores.
- Score function ?
	- which is the gradient of the log-density function at the input data point.
	- 怎么获得？
		- 用NN with score matching 学习这个
- Score matching ?

# Attachment
---
![[Generative modeling by estimating gradients of the data distribution.pdf]]
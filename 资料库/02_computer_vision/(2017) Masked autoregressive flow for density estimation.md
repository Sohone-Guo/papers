# Information
---


# Mainly Idea
---
There are mainly two families of neural density estimators that are both flexible and tractable:
- Autoregressive models decompose the joint density as a product of conditions, and model each conditional in turn.
- Normalizing flows transform a base density into the target density by an invertible transformation with tractable Jacobian.

当前问题：Autoregressive models 对顺序很敏感，换一个顺序可能就失败了，所提方法，使得Autoregressive models 换顺序不会失败。
![[Pasted image 20230517142230.png]]

# Reference
---
- [[(2016) Improved variational inference with inverse autoregressive flow]]
- [[(2017) Density estimation using Real NVP]]

Video
- [Masked Autoregressive Flow for Density Estimation on Vimeo](https://vimeo.com/252105837)
- [Generative Model for Density Estimation - YouTube](https://www.youtube.com/watch?v=VjlWNQA7fZg)

之所以叫Mask
![[Pasted image 20230517142402.png]]

# Attachment
---
![[1705.07057.pdf]]
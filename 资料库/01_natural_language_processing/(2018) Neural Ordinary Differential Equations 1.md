# Information
---


# Mainly Idea
---
Models sucb as residual networks, recurrent neural netowrk decoders, and normalizing flows:
$h_{t+1}=h_{t}+f(h_t,\theta)$  → $\frac{dh(t)}{dt}=f(h(t),t,\theta)$

The model can be trained directly, but incurs a high memory cost.


# Reference
---
- 相关资料
	- https://www.youtube.com/watch?v=sIFnARdTVvE
- 其他资料
	- 公式离散化
		- ![[Pasted image 20230522134317.png]]
	- what is the adjoint sensitivity method?
		- ?
	- Reverse-mode differentiation of an ODE solution
		- ![[Pasted image 20230522134243.png]]
# Attachment
---
![[Neural Ordinary Differential Equation.pdf]]